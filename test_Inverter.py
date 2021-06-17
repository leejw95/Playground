import StickDiagram
import DesignParameters
import copy
import DRC
import NMOS
import PMOS
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import math

class _Inverter(StickDiagram._StickDiagram) :

    def __init__(self, _DesignParameter = None, _Name = 'Inverter') :
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name = self._NameDeclaration(_Name = _Name), _GDSFile = self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None,\
                                  _VDD2VSSHeight = None, _Dummy = None, _NumSupplyCoX = None, _NumSupplyCoY = None, \
                                  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, NumViaPoly2Met1CoX = None, \
                                  NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None, NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None, _SLVT = None) :

        _DRCObj = DRC.DRC()
        _Name = 'Inverter'

        #####################################_NMOS Generation######################################
        _NMOSinputs = copy.deepcopy(NMOS._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger
        _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_DesignObj = NMOS._NMOS(_DesignParameter = None, \
                                                                                                           _Name = 'NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)


        #####################################_PMOS Generation######################################
        _PMOSinputs = copy.deepcopy(PMOS._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger
        _PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj = PMOS._PMOS(_DesignParameter = None, \
                                                                                                            _Name = 'PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)


        #####################################VDD Generation######################################
        _ContactNum = _NumSupplyCoX
        if _ContactNum == None:
            _ContactNum = int((self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        if _ContactNum < 2 :
            _ContactNum = 2

        if _NumSupplyCoY is None :
            _NumSupplyCoY = 1

        _Nbodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY
        _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj = NbodyContact._NbodyContact(_DesignParameter = None,\
                                                                                                                     _Name = 'NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)


        #####################################VSS Generation######################################
        _Pbodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
        _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCoY
        _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj = PbodyContact._PbodyContact(_DesignParameter = None, \
                                                                                                                     _Name = 'PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)
        del _ContactNum

        #####################################VIA Generation for PMOS Output######################################
        _ViaNum = NumViaPMOSMet12Met2CoY
        if _ViaNum == None :
            _ViaNum = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2 :
            _ViaNum = 2

        if NumViaPMOSMet12Met2CoX == None :
            NumViaPMOSMet12Met2CoX = 1

        _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaPMOSMet12Met2CoX
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj = ViaMet12Met2._ViaMet12Met2(_DesignParameter = None, \
                                                                                                                                  _Name = 'ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
        del _ViaNum


        #####################################VIA Generation for NMOS Output######################################
        _ViaNum = NumViaNMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2 :
            _ViaNum = 2

        if NumViaNMOSMet12Met2CoX == None:
            NumViaNMOSMet12Met2CoX = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaNMOSMet12Met2CoX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj = ViaMet12Met2._ViaMet12Met2(_DesignParameter = None, \
                                                                                                                                  _Name = 'ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
        del _ViaNum


        #####################################VIA Generation for PMOS Gate######################################
        _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
                           self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1 :
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None :
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None :
            _tmpNumCOY = 1
        else :
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

        self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj = ViaPoly2Met1._ViaPoly2Met1(_DesignParameter = None, \
                                                                                                                                _Name = 'ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        del _tmpNumCOX
        del _tmpNumCOY

        #####################################VIA Generation for NMOS Gate######################################
        _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
                           self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]
        _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None :
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None :
            _tmpNumCOY = 1
        else :
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

        self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj = ViaPoly2Met1._ViaPoly2Met1(_DesignParameter = None, \
                                                                                                                         _Name = 'ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)
        del _tmpNumCOX
        del _tmpNumCOY

        #####################################Coordinates setting######################################
        _LengthSpaceBtwInputMet1 = 2 * _DRCObj._PolygateMinSpace2Co + _ChannelLength
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]] ### PbodyContact Coordinate setting

        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
                                                                max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3]]
                                                            #  self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
                                                            #     max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3]] ### _PpMinExtensiononPactive???
                                                            # #+ (self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] * 1 /2)]]

        _VDD2VSSMinHeight = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     2 * _DRCObj._Metal1MinSpace3 + 2 * self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 3 * _DRCObj._Metal1MinSpace2




        #self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] * 1 / 2 + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] * 1 / 2 + \
                            #self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] + \
                            #self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                            #+ _DRCObj._PolygateMinSpace2OD + _DRCObj._OdMinSpace + float(_DRCObj._Metal1MinEnclosureArea) / float(2 * _LengthSpaceBtwInputMet1) # + 2 * _DRCObj._Metal1MinSpaceAtCorner + _DRCObj._Metal1MinSpace2 +f

        if _VDD2VSSHeight == None :
            _VDD2VSSHeight = _VDD2VSSMinHeight

        else :
            if _VDD2VSSHeight < _VDD2VSSMinHeight :
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)
#               raise NotImplementedError

        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, _VDD2VSSHeight - max((self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] * 1 / 2), (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 1 / 2)) - \
                                                             (self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] * 1 / 2) - _DRCObj._OdMinSpace]]

        tmpNMOSOutputRouting = []
        tmpPMOSOutputRouting = []

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            tmpPMOSOutputRouting.append([self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], \
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]])
            tmpNMOSOutputRouting.append([self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], \
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]])

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting

        self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - \
                                                                        max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) * 1 / 2 - self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 1 / 2 - max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)]]

        self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + \
                                                                        max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) * 1 / 2 + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 1 / 2 + max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)]]

        _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
        _LengthNPolyDummyEdge2OriginX = (int(_Finger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
        _LengthPPolyDummyEdge2OriginX = (int(_Finger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2


        #####################################VIA re-Coordinates for Poly Dummy######################################
#        if ((self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2 - (int(_Finger / 2) * _LengthBtwPoly2Poly + _ChannelLength / 2) > 0) :
#            _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + 1
#            _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
#            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown]]
#            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp]]

        if _Finger == 1 :
            _LengthBtwPolyDummyEdge2PolyEdge = (_LengthBtwPoly2Poly * (_Finger / 2 + 0.5) - _ChannelLength / 2) - self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2
            _LengthNPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            _LengthPPolyDummytoGoUp_Finger2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyDummytoGoUp_Finger2]]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyDummytoGoUp_Finger2]]


        #####################################VSS&VDD Met1 Routing######################################
        tmpNMOSSupplyRouting = []
        tmpPMOSSupplyRouting = []
        for i in range(0, len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
        self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
        self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting


        #####################################Input Met1 Routing######################################
        tmpInputRouting = []
        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth

        if _Finger % 2 == 0 :
            for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1) :
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], \
                                          [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]])

        elif _Finger % 2 != 0 :
            for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) :
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], \
                                          [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]])

        if _Finger == 1 :
            tmpInputRouting = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], \
                                          [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        if _Finger == 2 :
            tmpInputRouting = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], \
                                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting
            #[[[self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]], \
            #                                                        [[self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]], \
            #                                                        [[self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]]]


        #####################################Output Met2 Boundary&Routing######################################
        tmpOutputRouting = []

        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype = DesignParameters._LayerMapping['METAL2'][1],  _XYCoordinates = [], _Width = None)
        self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]], \
                                      [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]]])
                                                                       ## [[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][tmp -1][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][tmp - 1][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRouting

        self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype = DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates = [], _Width = None)
        self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth

        self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], \
                                                                      self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                                                     [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], \
                                                                      self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]]], \
                                                                     [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0], \
                                                                       self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                                                      [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], \
                                                                       self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]]


        #####################################Additional Poly Routing######################################
        self._DesignParameter['_AdditionalPolyOnPMOS'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['POLY'][0], _Datatype = DesignParameters._LayerMapping['POLY'][1], \
                                                                                      _XYCoordinates = [], _Width = None)
        self._DesignParameter['_AdditionalPolyOnNMOS'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['POLY'][0], _Datatype = DesignParameters._LayerMapping['POLY'][1], \
                                                                                      _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = _DRCObj._PolygateMinWidth
        self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = _DRCObj._PolygateMinWidth


        tmpAdditionalPolyOnPMOS = []
        tmpAdditionalPolyOnNMOS = []

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])) :
            tmpAdditionalPolyOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]], \
                                              [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1] - _DRCObj._PolygateMinWidth]])
            tmpAdditionalPolyOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]], \
                                              [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1] + _DRCObj._PolygateMinWidth]])

        self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmpAdditionalPolyOnPMOS
        self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmpAdditionalPolyOnNMOS

        del tmpAdditionalPolyOnPMOS
        del tmpAdditionalPolyOnNMOS

        self._DesignParameter['_AdditionalPolyOnGate'] =  self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=None, _YWidth=None, _ElementName=None,)
        self._DesignParameter['_AdditionalPolyOnGate']['_XWidth'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate']['_YWidth'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate']['_XYCoordinates'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] + self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates']




        #####################################NWELL Generation & Coordinates#######################################
        _SupplyRailYwidth = _DRCObj._CoMinWidth * _NumSupplyCoY + _DRCObj._CoMinSpace * _NumSupplyCoY
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['NWELL'][0],_Datatype = DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive, \
                                                          self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX)
        #        self._DesignParameter['_NWLayer']['_YWidth'] = (self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + _DRCObj._NwMinEnclosurePactive + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) * 2  ###self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + _DRCObj._NwMinEnclosurePactive

        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYwidth / 2 + _DRCObj._NwMinEnclosurePactive], \
                                                                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2]]]

        if _SLVT == True :
            self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive, \
                                                          self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX, self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT)
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYwidth / 2 + _DRCObj._NwMinEnclosurePactive], \
                                                                    [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], min(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2 - _DRCObj._NwMinSpacetoSLVT)]]]

        #####################################Pin Generation & Coordinates#######################################
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VSS')
        self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VIN')
        self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VOUT')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + \
                    self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2), round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + \
                    self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]]
        self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2), round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1]) / 2)]]


        #####################################Poly Dummy#######################################
#        _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
#        _LengthPolyDummyEdge2OriginX = (int(_Finger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
#        _LengthPolyDummyEdge2OriginY =
#        _LengthPolyDummytoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPolyDummyEdge2OriginX * _LengthPolyDummyEdge2OriginX)
#        if (self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2 - (int(_Finger / 2) * _LengthBtwPoly2Poly + _ChannelLength / 2) > 0 :
#            _tmpLengthPolyDummytoGoDown =





if __name__ == '__main__':
    lst = ['_Finger', '_ChannelWidth', '_ChannelLength', '_NPRatio', '_VDD2VSSHeight', '_Dummy', '_SLVT', '_LVT',
           '_HVT', '_NumSupplyCOX'
        , '_NumSupplyCOY', '_SupplyMet1XWidth', '_SupplyMet1YWidth', '_NumVIAPoly2Met1COX', '_NumVIAPoly2Met1COY',
           '_NumVIAMet12COX', '_NumVIAMet12COY']
    # ans = [6, 200, 30, 2, 2000, True, True, False, False, 4, 2, None, None, None, None, None, None]
    ans = []
    for i in range(5):
        print (lst[i] + '?')
        n = input()
        ans.append(n)

    _Finger = ans[0]
    _ChannelWidth = ans[1]
    _ChannelLength = ans[2]
    _NPRatio = ans[3]
    _VDD2VSSHeight = ans[4]
    # _Dummy = True
    # _SLVT = True
    # _LVT = False
    # _HVT = False
    # _NumSupplyCOX = None
    # _NumSupplyCOY = None
    # _SupplyMet1XWidth = None
    # _SupplyMet1YWidth = None
    # _NumVIAPoly2Met1COX = None
    # _NumVIAPoly2Met1COY = None
    # _NumVIAMet12COX = None
    # _NumVIAMet12COY = None
    InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter')
    InverterObj._CalculateDesignParameter(_Finger = _Finger, _ChannelWidth = _ChannelWidth, _ChannelLength = _ChannelLength, _NPRatio = _NPRatio, _VDD2VSSHeight = _VDD2VSSHeight,
                                          _Dummy = True, _NumSupplyCoX = None, _NumSupplyCoY = None, _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, NumViaPoly2Met1CoX = None, \
                                  NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None, NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None,
                                          _SLVT = True)

    InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = InverterObj._DesignParameter)
    _fileName = 'test_InverterJIChoFile.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    import ftplib

    print ('###############      Sending to FTP Server...      ##################')

    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('test_InverterJIChoFile.gds', 'rb')
    ftp.storbinary('STOR test_InverterJIChoFile.gds', myfile)
    myfile.close()
    ftp.close()
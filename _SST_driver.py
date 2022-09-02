import PbodyContact_iksu
import StickDiagram
import DesignParameters
import copy
import DRC
import SST_GuardRingResistor
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import ViaMet12Met2
import ViaMet22Met3
import ViaPoly2Met1


class _SST_driver(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(_NumofRes=None, _PType=True, _XWidth=None, _YWidth=None, _Width=None,
                                           _RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None,
                                           _Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                           _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                           _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                           _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None,
                                           _NumViaPMOSMet12Met2CoY=None, _NumViaNMOSMet12Met2CoX=None,
                                           _NumViaNMOSMet12Met2CoY=None, _XVT=None)


    def __init__(self, _DesignParameter = None, _Name = None) :
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict( _MET3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _NumofRes=None, _PType = True, _XWidth = None, _YWidth = None, _Width = None,
                                  _RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None,
                                  _Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None, _VDD2VSSHeight=None, _Dummy=None,
                                  _NumSupplyCoX=None, _NumSupplyCoY=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                  _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None, _NumViaPMOSMet12Met2CoY=None, _NumViaNMOSMet12Met2CoX=None,
                                  _NumViaNMOSMet12Met2CoY=None, _XVT=None):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        _GRResistorinputs = copy.deepcopy(SST_GuardRingResistor._SST_GuardRingResistor._ParametersForDesignCalculation)
        _GRResistorinputs['_NumofRes'] = _NumofRes
        _GRResistorinputs['_PType'] = _PType
        _GRResistorinputs['_XWidth'] = _XWidth
        _GRResistorinputs['_YWidth'] = _YWidth
        _GRResistorinputs['_Width'] = _Width
        _GRResistorinputs['_RWidth'] = _RWidth
        _GRResistorinputs['_RLength'] = _RLength
        _GRResistorinputs['_NumofCOX'] = _NumofCOX
        _GRResistorinputs['_NumofCOY'] = _NumofCOY

        self._DesignParameter['_SST_GuardRingResistor'] = self._SrefElementDeclaration(_DesignObj=SST_GuardRingResistor._SST_GuardRingResistor(_DesignParameter=None, _Name='GuardRingResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._CalculateSSTGuardRingResistorParameter(**_GRResistorinputs)
        self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._CalculateSSTGuardRingResistorParameter(**dict(_NumofRes=2, _PType = True, _XWidth = 2000.0, _YWidth = 2000.0, _Width = _Width,
                                           _RWidth=_RWidth, _RLength=_RLength, _NumofCOX=None, _NumofCOY=_NumofCOY))

        _XYCoordinatesofSST = [[0, 0]]



        #####################################_NMOS Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger
        _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_XVT'] = _XVT

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)



        #####################################_PMOS Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger
        _PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_XVT'] = _XVT

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)



        #####################################VDD Generation######################################
        _ContactNum = _NumSupplyCoX
        if _ContactNum == None:
            _ContactNum = int((self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
        if _ContactNum < 2:
            _ContactNum = 2

        if _NumSupplyCoY is None:
            _NumSupplyCoY = _Width // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)

        _Nbodyinputs = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY
        _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)



        #####################################VSS Generation######################################
        _Pbodyinputs = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
        _Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
        _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCoY
        _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact_iksu._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)
        del _ContactNum



        #####################################VIA Generation for PMOS Output######################################
        _ViaNum = _NumViaPMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2:
            _ViaNum = 2

        if _NumViaPMOSMet12Met2CoX == None:
            NumViaPMOSMet12Met2CoX = 1

        _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaPMOSMet12Met2CoX
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
        del _ViaNum



        #####################################VIA Generation for NMOS Output######################################
        _ViaNum = _NumViaNMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2:
            _ViaNum = 2

        if _NumViaNMOSMet12Met2CoX == None:
            NumViaNMOSMet12Met2CoX = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaNMOSMet12Met2CoX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
        del _ViaNum

        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = \
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = \
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']



        #####################################VIA Generation for PMOS Gate######################################
        _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        #####################################VIA Generation for NMOS Gate######################################
        _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

        _LenBtwMOSGates = max(_LenBtwPMOSGates, _LenBtwNMOSGates)

        _VIAMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if _NumViaPoly2Met1CoX != None:
            _tmpNumCOX = _NumViaPoly2Met1CoX

        if _NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = _NumViaPoly2Met1CoY

        _VIAMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

        self._DesignParameter['_VIAMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOSGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1)
        del _tmpNumCOX
        del _tmpNumCOY

        #################################  GuardRing Placement ####################################
        _PRESMinSpace = 400
        self._DesignParameter['_SST_GuardRingResistor']['_XYCoordinates'] = [[_XYCoordinatesofSST[0][0] ,
                                                                              _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2]]
        # HeightofNMOS = _RWidth // 2 + _DRCObj._RXMinSpacetoPRES + _Width + _DRCObj._PpMinExtensiononPactive2 + _ChannelWidth // 2 + _DRCObj._PolygateMinExtensionOnOD + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate
        if _XWidth == None:
            _XWidth = float(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _Width)
            if _XWidth < _NumofRes * (_RLength + _PRESMinSpace) - _PRESMinSpace + _DRCObj._RXMinSpacetoPRES * 2:
                raise NotImplementedError # want to not raise error, change Nbodycontact's XWidth of VDD to stretch or _XWidth calculation to original equation in "SST_GuardRingResistor"


        self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._CalculateSSTGuardRingResistorParameter(**dict(_NumofRes=_NumofRes, _PType=_PType,
                                                                                                                     _XWidth=_XWidth, _YWidth=_YWidth, _Width=_Width,
                                                                                                                     _RWidth=_RWidth, _RLength=_RLength,
                                                                                                                     _NumofCOX=_NumofCOX, _NumofCOY=_NumofCOY))
        if _SupplyMet1YWidth == None:
            _SupplyMet1YWidth = _Width



        #####################################Coordinates setting######################################
        _LengthSpaceBtwInputMet1 = 2 * _DRCObj._PolygateMinSpace2Co + _ChannelLength

        _LengthBtwPoly2Poly = 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
        _LengthPolyDummyEdge2OriginX = (int(_Finger // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength // 2 \
                                       - (self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) // 2

        # self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]  ### PbodyContact Coordinate setting

        HeightofNMOS = self.FloorMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
                                                + max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                      self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2
                                                + _DRCObj._Metal1DefaultSpace, MinSnapSpacing)

        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, HeightofNMOS]]

        _VDD2VSSMinHeight = self.CeilMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
                                                    + max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                          self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
                                                    + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
                                                    + max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                          self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
                                                    + 2 * _DRCObj._Metal1DefaultSpace + self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                                                    + 2 * _DRCObj._Metal1DefaultSpace + _DRCObj._Metal1MinSpace, MinSnapSpacing)

        if _VDD2VSSHeight == None:
            _VDD2VSSHeight = _VDD2VSSMinHeight

        else:
            if _VDD2VSSHeight < _VDD2VSSMinHeight:
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)
                raise NotImplementedError

        self._DesignParameter['_INVVDD2VSSMinHeight'] = {'_Ignore': _VDD2VSSHeight, '_DesignParametertype': None,
                                                         '_ElementName': None, '_XYCoordinates': None, '_Width': None,
                                                         '_Layer': None, '_Datatype': None}

        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

        HeightofPMOS = self.CeilMinSnapSpacing(_VDD2VSSHeight - self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
                                               - max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                     self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2
                                               - _DRCObj._Metal1DefaultSpace, MinSnapSpacing)

        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, HeightofPMOS]]  ### PODummyLayer -> POLayer

        tmpNMOSOutputRouting = []
        tmpPMOSOutputRouting = []

        for i in range(len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpPMOSOutputRouting.append([self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]
                                         + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]
                                         + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]])
            tmpNMOSOutputRouting.append([self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0]
                                         + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]
                                         + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]])

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting

        YCoordinateofNPoly = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'],
                                                                                          self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2
        YCoordinateofPPoly = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'],
                                                                                          self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2

        self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                                                        self.CeilMinSnapSpacing((YCoordinateofNPoly + YCoordinateofPPoly) // 2, MinSnapSpacing)]]



        #####################################VSS&VDD Met1 Routing######################################
        tmpNMOSSupplyRouting = []
        tmpPMOSSupplyRouting = []
        for i in range(len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]
                                          + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]
                                          + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]],
                                         [self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]
                                          + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], _XYCoordinatesofSST[0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0]
                                          + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]
                                          + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]],
                                         [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0]
                                          + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                   _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                   _XYCoordinates=[], _Width=None)
        self._DesignParameter['_NMOSSupplyRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                   _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                   _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PMOSSupplyRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting



        #####################################Input Met1 Routing######################################
        tmpInputRouting = []
        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth

        if _Finger % 2 == 0:
            for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1):
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]])

        elif _Finger % 2 != 0:
            for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                         self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]])

        # if _Finger == 1 :
        #     tmpInputRouting =  [[[0, self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        if _Finger == 2:
            tmpInputRouting = [[[0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        if _Finger == 3:
            tmpInputRouting = [[[0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting



        ###################################### NMOS-to-Resistor Routing ########################################
        self._DesignParameter['_NtoRVRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                               _XYCoordinates=[], _Width=None)
        self._DesignParameter['_NtoRVRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_NtoRHRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_NtoRHRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        _ResMetalYCoordinate = _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2 \
                               + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_OPLayer']['_YWidth'] // 2 \
                               + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth
        tmp_NtoR = []
        # need to define range values
        for i in range(3, len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates']) // 2 - 2):
            tmp_NtoR.append([[self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                              self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                             _ResMetalYCoordinate]])
        self._DesignParameter['_NtoRVRouting']['_XYCoordinates'] = tmp_NtoR
        self._DesignParameter['_NtoRHRouting']['_XYCoordinates'] = [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates']]




        ###################################### PMOS-to-Resistor Routing ########################################
        self._DesignParameter['_PtoRVRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PtoRVRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        self._DesignParameter['_PtoRHRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PtoRHRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        _ResMetalYCoordinate = _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2 \
                               + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_OPLayer']['_YWidth'] // 2 \
                               + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth
        tmp_PtoR = []
        # need to define range values
        for i in range(len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates']) // 2 + 2, len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates']) - 3):
            tmp_PtoR.append([[self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],
                              self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][1]],
                             [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],
                              _ResMetalYCoordinate]])
        self._DesignParameter['_PtoRVRouting']['_XYCoordinates'] = tmp_PtoR
        self._DesignParameter['_PtoRHRouting']['_XYCoordinates'] = [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates']]


        #########################################Output Routing##########################################
        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_OutputRouting']['_Width'] = self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = [[[_XYCoordinatesofSST[0][0] - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                                                                          - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                       _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2
                                                                       - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]],
                                                                      [_XYCoordinatesofSST[0][0] + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                                                                       + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                       _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2 - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]]]]



        #####################################VIA Generation for resistor######################################

        _RViaNum = int(self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] //
                          (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        _VIANRMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANRMet12['_ViaMet12Met2NumberOfCOX'] = _RViaNum
        _VIANRMet12['_ViaMet12Met2NumberOfCOY'] = _NumofCOY

        self._DesignParameter['_ViaMet12Met2OnResistor'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='_VIANRMet12In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANRMet12)

        self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']


        self._DesignParameter['_ViaMet12Met2OnResistor']['_XYCoordinates'] \
            = [[_XYCoordinatesofSST[0][0] - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                - self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2
                - _PRESMinSpace // 2 - _DRCObj._PRESlayeroverPoly - _DRCObj._CoMinEnclosureByPO - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide,
                 _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2
                 - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]],
                 [_XYCoordinatesofSST[0][0] + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                 + self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2
                 + _PRESMinSpace // 2 + _DRCObj._PRESlayeroverPoly + _DRCObj._CoMinEnclosureByPO + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide,
                 _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2
                 - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]]]

        _RViaNum2 = int(self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] //
                       (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _VIANRMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANRMet23['_ViaMet22Met3NumberOfCOX'] = _RViaNum2
        _VIANRMet23['_ViaMet22Met3NumberOfCOY'] = _NumofCOY

        self._DesignParameter['_ViaMet22Met3OnResistor'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='_VIANRMet23In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnResistor']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_VIANRMet23)



        self._DesignParameter['_ViaMet22Met3OnResistor']['_XYCoordinates'] \
            = [[_XYCoordinatesofSST[0][0] + self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                + self._DesignParameter['_ViaMet12Met2OnResistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2
                + _PRESMinSpace // 2 + _DRCObj._PRESlayeroverPoly - _DRCObj._CoMinEnclosureByPO - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide,
                _XYCoordinatesofSST[0][1] - _RWidth // 2 - _DRCObj._RXMinSpacetoPRES - _Width // 2
                - self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]]]

        # for covering all vertical M3
        self._DesignParameter['_MET3Layer']['_XWidth'] = self._DesignParameter['_SST_GuardRingResistor']['_DesignObj']._DesignParameter['SSTresistor']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_MET3Layer']['_YWidth'] = \
        self._DesignParameter['_ViaMet22Met3OnResistor']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
        self._DesignParameter['_MET3Layer']['_XYCoordinates'] = [self._DesignParameter['_ViaMet12Met2OnResistor']['_XYCoordinates'][1]]


        #####################################VIA Generation for PMOS M3######################################

        _ViaNum3 = _NumViaPMOSMet12Met2CoY
        if _ViaNum3 == None:
            _ViaNum3 = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (
                        _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum3 < 2:
            _ViaNum3 = 2

        if _NumViaPMOSMet12Met2CoX == None:
            NumViaPMOSMet12Met2CoX = 1

        _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = NumViaPMOSMet12Met2CoX
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNum3

        self._DesignParameter['_ViaMet22Met3OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_VIAPMOSMet23)



        self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates']




        #####################################Additional Poly Routing######################################
        self._DesignParameter['_AdditionalPolyOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                      _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                      _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                      _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                      _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = _DRCObj._PolygateMinWidth
        self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = _DRCObj._PolygateMinWidth

        tmpAdditionalPolyOnPMOS = []
        tmpAdditionalPolyOnNMOS = []

        for i in range(len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpAdditionalPolyOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                             self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] +
                                             self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                                            [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                             self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1] -
                                             self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2,
                                                                     _DRCObj._MinSnapSpacing)]])
            tmpAdditionalPolyOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                             self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                                             self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                            [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                             self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1] +
                                             self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2,
                                             _DRCObj._MinSnapSpacing)]])

        self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmpAdditionalPolyOnPMOS
        self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmpAdditionalPolyOnNMOS

        del tmpAdditionalPolyOnPMOS
        del tmpAdditionalPolyOnNMOS

        self._DesignParameter['_AdditionalPolyOnGate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                          _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None)
        self._DesignParameter['_AdditionalPolyOnGate']['_XWidth'] = \
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate']['_YWidth'] = \
        self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate']['_XYCoordinates'] = self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'] + \
                                                                           self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates']



        #####################################NWELL&PP/NP Layer Generation & Coordinates#######################################
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                         _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                         _XYCoordinates=[], _Width=None)
        # if DesignParameters._Technology == '028nm' : self._DesignParameter['_NWLayer']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT
        self._DesignParameter['_NWLayer']['_Width'] = \
        self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                 self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] +
                                                                                         self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] // 2
                                                                                         + _DRCObj._NwMinEnclosurePactive2, MinSnapSpacing)],
                                                                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]
                                                                 - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2]]]

        if DesignParameters._Technology != '028nm':
            self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                             _XYCoordinates=[], _Width=None)
            self._DesignParameter['_PPLayer']['_Width'] = \
            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                                    [self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][0],
                                                                     self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1],
                                                                                             2 * MinSnapSpacing)]]]

            self._DesignParameter['_NPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                                                                             _XYCoordinates=[], _Width=None)
            self._DesignParameter['_NPLayer']['_Width'] = \
            self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
            self._DesignParameter['_NPLayer']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                                    [self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][0],
                                                                     self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1],
                                                                                             2 * MinSnapSpacing)]]]

            _SupplyRailYwidth = _DRCObj._CoMinWidth * _NumSupplyCoY + _DRCObj._CoMinSpace * _NumSupplyCoY
            self._DesignParameter['_AdditionalNWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                       _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                       _XYCoordinates=[], _Width=None)
            self._DesignParameter['_AdditionalNWLayer']['_Width'] = \
            self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2

            self._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                               self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]
                                                                                                       + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] // 2
                                                                                                       + _DRCObj._NwMinEnclosurePactive2, MinSnapSpacing)],
                                                                              [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                               self.FloorMinSnapSpacing(self._DesignParameter['_PPLayer']['_XYCoordinates'][0][1][1],
                                                                                                        MinSnapSpacing)]]]


        #####################################Pin Generation & Coordinates#######################################
        # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VDD')
        # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VSS')
        self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'OUT')

        # self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        # self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0,0]]
        # self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + \
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2), MinSnapSpacing), self.CeilMinSnapSpacing(round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + \
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2), MinSnapSpacing)]]
        self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2), MinSnapSpacing), self.CeilMinSnapSpacing(round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1]) / 2), MinSnapSpacing)]]



if __name__ == '__main__':
    _NumofRes = 2               # number of resistor
    _PType = True               # for "P"subring
    _XWidth = None              # GuardRing XWidth(metal1 edge-to-edge)
    _YWidth = None              # GuardRing YWidth(metal1 edge-to-edge)
    _Width = 300                # Guardring & VDD width
    _RWidth = 1680              # Resistor Ywidth
    _RLength = 7372             # Resistor Xwidth
    _NumofCOX = None            # Resistor port's number of contact (X direction)
    _NumofCOY = 1               # Resistor port's number of contact (Y direction)
    _Finger = 128               # number of MOS finger
    _ChannelWidth = 200         # NMOS channel width
    _ChannelLength = 30         # MOS channel length
    _NPRatio = 2                # PMOS channel width / NMOS channel width
    _VDD2VSSHeight = None       # VDD-to-VSS height
    _Dummy = True               # create Dummy
    _NumSupplyCoX = None        # number of VDD contact (X direction)
    _NumSupplyCoY = None        # number of VDD contact (Y direction)
    _SupplyMet1XWidth = None
    _SupplyMet1YWidth = None
    _NumViaPoly2Met1CoX = None
    _NumViaPoly2Met1CoY = None
    _NumViaPMOSMet12Met2CoX = None
    _NumViaPMOSMet12Met2CoY = None
    _NumViaNMOSMet12Met2CoX = None
    _NumViaNMOSMet12Met2CoY = None
    _XVT = 'LVT'                # threshold voltage

    DesignParameters._Technology = '028nm'
    TopObj = _SST_driver(_DesignParameter=None, _Name='_SST_driver')
    TopObj._CalculateDesignParameter(_NumofRes=_NumofRes, _PType=_PType, _XWidth=_XWidth, _YWidth=_YWidth, _Width=_Width,
                                     _RWidth=_RWidth, _RLength=_RLength, _NumofCOX=_NumofCOX, _NumofCOY=_NumofCOY,
                                     _Finger=_Finger, _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength, _NPRatio=_NPRatio,
                                     _VDD2VSSHeight=_VDD2VSSHeight, _Dummy=_Dummy, _NumSupplyCoX=_NumSupplyCoX, _NumSupplyCoY=_NumSupplyCoY,
                                     _SupplyMet1XWidth=_SupplyMet1XWidth, _SupplyMet1YWidth=_SupplyMet1YWidth, _NumViaPoly2Met1CoX=_NumViaPoly2Met1CoX,
                                     _NumViaPoly2Met1CoY=_NumViaPoly2Met1CoY, _NumViaPMOSMet12Met2CoX=_NumViaPMOSMet12Met2CoX,
                                     _NumViaPMOSMet12Met2CoY=_NumViaPMOSMet12Met2CoY, _NumViaNMOSMet12Met2CoX=_NumViaNMOSMet12Met2CoX,
                                     _NumViaNMOSMet12Met2CoY=_NumViaNMOSMet12Met2CoY, _XVT=_XVT)
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_SST_driver.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      #############################')

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_SST_driver.gds', 'rb')
    ftp.storbinary('STOR _SST_driver.gds', myfile)
    myfile.close()

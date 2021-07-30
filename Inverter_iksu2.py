import math
import copy
#
import StickDiagram
import DesignParameters
import DRC
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
from Private import FileManage
import CoordinateCalc


class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                           _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                           _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                           _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None,
                                           _NumViaPMOSMet12Met2CoY=None, _NumViaNMOSMet12Met2CoX=None,
                                           _NumViaNMOSMet12Met2CoY=None, _SLVT=None, _SupplyLine=None)

    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter

        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                  _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                  _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                  _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None, _NumViaPMOSMet12Met2CoY=None,
                                  _NumViaNMOSMet12Met2CoX=None, _NumViaNMOSMet12Met2CoY=None, _SLVT=None, _SupplyLine=None):

        _DRCObj = DRC.DRC()
        _Name = 'Inverter'

        # _NMOS Generation ---------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_SLVT'] = _SLVT

        self._DesignParameter['_NMOS'] = \
            self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None,
                                                                        _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)
        del NMOSparameters

        # _PMOS Generation ---------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_SLVT'] = _SLVT

        self._DesignParameter['_PMOS'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None,
                                                                        _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)
        del PMOSparameters

        # VDD Generation -----------------------------------------------------------------------------------------------
        _ContactNum = _NumSupplyCoX

        if _NumSupplyCoY is None:
            _NumSupplyCoY = 1

        if _ContactNum == None:
            xWidthOfPMOS = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            _ContactNum = int(xWidthOfPMOS // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        NbodyParameters = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters['_NumberOfNbodyCOX'] = _ContactNum if (_ContactNum > 2) else 2
        NbodyParameters['_NumberOfNbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        NbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        NbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)
        del NbodyParameters

        # VSS Generation -----------------------------------------------------------------------------------------------
        PbodyParameters = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        PbodyParameters['_NumberOfPbodyCOX'] = _ContactNum if (_ContactNum > 2) else 2
        PbodyParameters['_NumberOfPbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        PbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        PbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**PbodyParameters)
        del PbodyParameters
        del _ContactNum

        # VIA Generation for PMOS Output -------------------------------------------------------------------------------
        _ViaNum = _NumViaPMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaPMOSMet12Met2CoX if (_NumViaPMOSMet12Met2CoX != None) else 1
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum if (_ViaNum > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = \
            self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                                               _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIAPMOSMet12)
        del VIAPMOSMet12

        # VIA Generation for NMOS Output -------------------------------------------------------------------------------
        _ViaNum = _NumViaNMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaNMOSMet12Met2CoX if (_NumViaNMOSMet12Met2CoX != None) else 1
        VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum if (_ViaNum > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = \
            self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                                               _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIANMOSMet12)
        del VIANMOSMet12
        del _ViaNum



        # VIA Generation for PMOS Gate ---------------------------------------------------------------------------------

        # Prev. design
        # _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
        #                    - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        # _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        # changed design
        _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                           + _ChannelLength
        unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
        # _tmpNumCOX = (int(_LenBtwPMOSGates - _DRCObj._CoMinWidth - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide) // unitLengthBtwCOX) + 1
        _tmpNumCOX = (int(_LenBtwPMOSGates - _DRCObj._CoMinWidth) // unitLengthBtwCOX) + 1

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1
        if _NumViaPoly2Met1CoX != None:
            _tmpNumCOX = _NumViaPoly2Met1CoX

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumViaPoly2Met1CoY if (_NumViaPoly2Met1CoY != None) else 1

        self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,
                                                                                                                        _Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] -20

        del _tmpNumCOX

        # VIA Generation for NMOS Gate ---------------------------------------------------------------------------------

        _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] \
                           + _ChannelLength
        unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
        # _tmpNumCOX = (int(_LenBtwNMOSGates - _DRCObj._CoMinWidth - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide) // unitLengthBtwCOX) + 1
        _tmpNumCOX = (int(_LenBtwNMOSGates - _DRCObj._CoMinWidth) // unitLengthBtwCOX) + 1


        _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        if _tmpNumCOX < 1:
            _tmpNumCOX = 1
        if _NumViaPoly2Met1CoX != None:
            _tmpNumCOX = _NumViaPoly2Met1CoX

        _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumViaPoly2Met1CoY if (_NumViaPoly2Met1CoY != None) else 1

        self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,
                                                                                                                        _Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)
        self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = \
        self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] - 20
        del _tmpNumCOX



        # Coordinates setting ------------------------------------------------------------------------------------------
        DistanceBtwVSS2NMOS = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                             + 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                         self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                             + _DRCObj._Metal1MinSpace3

        DistanceBtwVDD2PMOS = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                             + 0.5 * max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'],
                                         self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                             + _DRCObj._OdMinSpace

        # Calculate Minimum Height of VDD to VSS
        if _Finger != 1:
            _VDD2VSSMinHeight = DistanceBtwVSS2NMOS \
                                + 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                + max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2) \
                                + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                + 0.5 * self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                + max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2) \
                                + 0.5 * max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                + DistanceBtwVDD2PMOS

        else:
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth

            _LengthBtwPolyDummyEdge2PolyEdge = (_LengthBtwPoly2Poly * (_Finger / 2 + 0.5) - _ChannelLength / 2) \
                                               - self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2

            _LengthNPolyDummytoGoUp_Finger2 = math.sqrt(
                _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            _LengthPPolyDummytoGoUp_Finger2 = math.sqrt(
                _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1

            _VDD2VSSMinHeight = DistanceBtwVSS2NMOS \
                                + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                + _LengthNPolyDummytoGoUp_Finger2 \
                                + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] \
                                + 0.5 * self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] \
                                + _LengthPPolyDummytoGoUp_Finger2 \
                                + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                + DistanceBtwVDD2PMOS

        if _VDD2VSSHeight == None:
            _VDD2VSSHeight = _VDD2VSSMinHeight
        else:
            if _VDD2VSSHeight < _VDD2VSSMinHeight:
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)  # Need to Print More information(input parameter...)
                raise NotImplementedError

        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, DistanceBtwVSS2NMOS]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - DistanceBtwVDD2PMOS)]]

        #
        tmpNMOSOutputRouting = []
        tmpPMOSOutputRouting = []

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpPMOSOutputRouting.append(CoordinateCalc.Add(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i],
                                                           self._DesignParameter['_PMOS']['_XYCoordinates'][0])
                                        )
            tmpNMOSOutputRouting.append(CoordinateCalc.Add(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i],
                                                           self._DesignParameter['_NMOS']['_XYCoordinates'][0])
                                        )

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting

        DistanceBtwNMOS2PolyInput = 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                              self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                    + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                    + max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)

        DistanceBtwPMOS2PolyInput = 0.5 * max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                              self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                    + 0.5 * self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                    + max(_DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)

        self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [
            [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
             self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
        ]

        self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [
            [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
             self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
        ]

        #####################################VIA re-Coordinates for Poly Dummy######################################
        # what is it? -> to avoid conflict between dummy poly and input contact polt
        if _Finger == 1:
            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                 self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 +
                 self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer'][
                     '_YWidth'] / 2 + _LengthNPolyDummytoGoUp_Finger2]]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                 self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 -
                 self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer'][
                     '_YWidth'] / 2 - _LengthPPolyDummytoGoUp_Finger2]]

        # VSS & VDD Met1 Routing ---------------------------------------------------------------------------------------
        # appended_list = [[x1, y1], [x2, y2]] : route from (x1,y1) to (x2,y2)
        tmpNMOSSupplyRouting = []
        tmpPMOSSupplyRouting = []

        for i in range(0, len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]],
                                         [self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]
                                         ])

            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]],
                                         [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]
                                         ])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                   _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                   _XYCoordinates=[], _Width=None)
        self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                   _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                   _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting

        # Input Met1 Routing -------------------------------------------------------------------------------------------
        tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]

        # exception case..?
        if _Finger in (1, 2, 3):
            tmpInputRouting = [[[0, self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                [0, self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]]]
        # Even Number Finger
        elif _Finger % 2 == 0:
            for i in range(1, len(
                    self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1):
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]
                                        ])
        # Odd Number Finger
        else:
            for i in range(1, len(
                    self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]
                                        ])

        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting

        #####################################Output Met2 Boundary&Routing######################################
        tmpOutputRouting = []

        if _Finger == 3:
            tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][1][0],  # 2 * 0
                                      self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[
                                          '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][1][1]],
                                     [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                                      self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][1][0],
                                      self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                                      self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[
                                          '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][1][1]]
                                     ])
        else:
            for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) / 2):
                tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][0],
                                          self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i][1]],
                                         [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][0],
                                          self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i][1]]
                                         ])


        if _Finger == 3:
            tmpOutputRouting.append([CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][1]),
                                     CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][1])
                                     ])
        else:
            for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) / 2):
                tmpOutputRouting.append([CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i]),
                                         CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                            self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i])
                                         ])



        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                               _XYCoordinates=[], _Width=None)
        self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRouting


        self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                              _XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = [
            [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
              self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]],
             [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],
              self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]]],
            [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],
              self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]],
             [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0],
              self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]
        ]  # row line on PMOS, NMOS

        # # #
        if _VDD2VSSHeight == _VDD2VSSMinHeight and _Finger == 3:

            _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 2
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)

            tmpXWidth = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            tmpYWidth = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']


            tmpXCoordinate = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
                             - self._DesignParameter['_OutputRouting']['_Width']/2 \
                             - _DRCObj._MetalxMinSpaceAtCorner \
                             - tmpXWidth/2
            tmpYCoordinate = self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]
            self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = [[tmpXCoordinate, tmpYCoordinate]]
            self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = \
                self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

        if _VDD2VSSHeight == _VDD2VSSMinHeight and _Finger == 4:

            _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 2
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)

            tmpXWidth = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            tmpYWidth = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']


            tmpXCoordinate = self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
                             + self._DesignParameter['_OutputRouting']['_Width']/2 \
                             + _DRCObj._MetalxMinSpaceAtCorner \
                             + tmpXWidth/2
            tmpYCoordinate = self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]
            self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = [[tmpXCoordinate, tmpYCoordinate]]
            self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = \
                self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

        # # #

        # if not, how works?
        if _VDD2VSSHeight == _VDD2VSSMinHeight and _Finger > 4:  #
            # M1V1M2
            _MaxLengthofM2 = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2][0] \
                                 - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] \
                                 - _DRCObj._MetalxMinWidth - 2*_DRCObj._MetalxMinSpaceAtCorner)

            _NumViaInputM12 = (_MaxLengthofM2 - 2*_DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) \
                              // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1   # calculate based on M2

            _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12
            _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)

            tmp = []
            for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2 - 1):
                tmp.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2*i + 1][0],
                            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]])
            self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmp
            del tmp

            # M2V2M3
            _NumViaInputM23 = _NumViaInputM12
            _ViaMet22Met3forInput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOX'] = _NumViaInputM23
            _ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3forInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3forInput)

            tmp = []
            for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2 - 1):
                tmp.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i + 1][0],
                            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]])
            self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'] = tmp
            del tmp

            self._DesignParameter['_CLKMet3InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['_CLKMet3InRouting']['_Width'] = self._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_CLKMet3InRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0],
                                                                             self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][-1]]]

        # Additional Poly Routing --------------------------------------------------------------------------------------
        '''
        Function : Route poly layers [ {NMOS gate poly - Input M1 poly(column)}, {PMOS gate poly - Input M1 poly(column)}, {Input gate poly left - Input gate poly right(row)} ]
        Output   : Update self._DesignParameter['_AdditionalPolyOn{}'] PMOS, NMOS, Gate
        '''

        self._DesignParameter['_AdditionalPolyOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = _DRCObj._PolygateMinWidth
        self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = _DRCObj._PolygateMinWidth

        tmpAdditionalPolyOnPMOS = []
        tmpAdditionalPolyOnNMOS = []

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpAdditionalPolyOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                                            [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1] - _DRCObj._PolygateMinWidth]])
            tmpAdditionalPolyOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                            [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                             self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1] + _DRCObj._PolygateMinWidth]])

        self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmpAdditionalPolyOnPMOS
        self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmpAdditionalPolyOnNMOS

        del tmpAdditionalPolyOnPMOS
        del tmpAdditionalPolyOnNMOS

        self._DesignParameter['_AdditionalPolyOnGate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None,)
        self._DesignParameter['_AdditionalPolyOnGate']['_XWidth'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                                                                    - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate']['_YWidth'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate']['_XYCoordinates'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] + self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates']


        # NWELL & SLVT Generation & Coordinates ------------------------------------------------------------------------
        '''
        Function : Generate NWELL by PathElementDeclaration (column line)
        Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        '''

        _SupplyRailYWidth = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']

        NWLayerXWidth = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive,
                            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX)

        XYCoordinatesOfNW_top = [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0],
                                 self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive]
        XYCoordinatesOfNW_bot = [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2] # why use this condition?

        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        self._DesignParameter['_NWLayer']['_Width'] = NWLayerXWidth
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]

        if _SLVT == True:
            self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive,
                                                              self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX, self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT)
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive], \
                                                                    [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]]]

            if _VDD2VSSHeight == _VDD2VSSMinHeight:  # why use this condition?
                self._DesignParameter['_SLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1])
                self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']
                self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]
                self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                                                          (self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]) / 2]]

        # Pin Generation & Coordinates ---------------------------------------------------------------------------------

        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VSS')
        self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VIN')
        self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VOUT')

        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + \
                    self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2), round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + \
                    self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]]
        self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2), round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] + \
                    self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1]) / 2)]]

        # SupplyLine Generation & Coordinates --------------------------------------------------------------------------

        if _SupplyLine == True:
            self._DesignParameter['_Met2LayerOnSupply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerOnSupply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerOnSupply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_Met2LayerOnSupply']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met3LayerOnSupply']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met4LayerOnSupply']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            self._DesignParameter['_Met2LayerOnSupply']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerOnSupply']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerOnSupply']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            self._DesignParameter['_Met2LayerOnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met3LayerOnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met4LayerOnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

            _ViaNumSupplyX = int(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumSupplyY = int(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            if _ViaNumSupplyX < 1:
                _ViaNumSupplyX = 1
            if _ViaNumSupplyY < 1:
                _ViaNumSupplyY = 1

            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumSupplyX
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumSupplyY
            self._DesignParameter['_ViaMet12Met2OnSupply'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSupplyIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnSupply']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2OnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumSupplyX
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumSupplyY
            self._DesignParameter['_ViaMet22Met3OnSupply'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSupplyIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnSupply']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3OnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

            _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumSupplyX
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumSupplyY
            self._DesignParameter['_ViaMet32Met4OnSupply'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnSupplyIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnSupply']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVDDMet32Met4)
            self._DesignParameter['_ViaMet32Met4OnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']


    # end of 'def _CalculateDesignParameter' ---------------------------------------------------------------------------


if __name__ == '__main__':
    # User-Defined Parameters
    _Finger = 3
    _ChannelWidth = 200
    _ChannelLength = 30
    _NPRatio = 2
    _VDD2VSSHeight = None  # None
    _Dummy = True
    _SLVT = True
    _LVT = False
    _HVT = False
    _NumSupplyCOX = None
    _NumSupplyCOY = None
    _SupplyMet1XWidth = None
    _SupplyMet1YWidth = None
    _NumVIAPoly2Met1COX = None
    _NumVIAPoly2Met1COY = None
    _NumViaPMOSMet12Met2CoX = None
    _NumViaPMOSMet12Met2CoY = None
    _NumViaNMOSMet12Met2CoX = None
    _NumViaNMOSMet12Met2CoY = None
    _NumVIAMet12COX = None
    _NumVIAMet12COY = None
    _SupplyLine = True

    # Generate Inverter Layout Object
    InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter')
    InverterObj._CalculateDesignParameter(_NPRatio=_NPRatio, _Dummy=_Dummy, _SLVT=_SLVT, _Finger=_Finger,
                                          _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength,
                                          _VDD2VSSHeight=_VDD2VSSHeight, _SupplyLine=_SupplyLine,
                                          _NumSupplyCoX=_NumSupplyCOX, _NumSupplyCoY=_NumSupplyCOY,
                                          _SupplyMet1XWidth=_SupplyMet1XWidth, _SupplyMet1YWidth=_SupplyMet1YWidth,
                                          _NumViaPoly2Met1CoX=_NumVIAPoly2Met1COX,
                                          _NumViaPoly2Met1CoY=_NumVIAPoly2Met1COY,
                                          _NumViaPMOSMet12Met2CoX=_NumViaPMOSMet12Met2CoX,
                                          _NumViaPMOSMet12Met2CoY=_NumViaPMOSMet12Met2CoY,
                                          _NumViaNMOSMet12Met2CoX=_NumViaNMOSMet12Met2CoX,
                                          _NumViaNMOSMet12Met2CoY=_NumViaNMOSMet12Met2CoY,
                                          )

    InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=InverterObj._DesignParameter)
    _fileName = 'Inverter0729.gds'                                    # Need to get current date / time
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')
    FileManage.Upload2FTP(_fileName=_fileName)

    print ('###############      Finished      ##################')  # Need to get project name(inverter_iksu2.py)

# end of 'main():' ---------------------------------------------------------------------------------------------

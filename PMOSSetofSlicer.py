import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ContGeneration
import math
import DesignParameters
import user_define_exceptions

import copy
import DRC

import ftplib
from ftplib import FTP
import base64

class _PMOSWithDummyOfSlicer(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
                                        _CLKinputPMOSFinger1=None, _CLKinputPMOSFinger2=None, _PMOSFinger=None, _PMOSChannelWidth=None,
                                        _ChannelLength=None, _Dummy=False, _SLVT=False, _GuardringWidth=None, _Guardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight=None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None)


    def __init__(self, _DesignParameter=None, _Name='PMOSWithDummyOfSlicer'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateDesignParameter(self, _CLKinputPMOSFinger1 = None, _CLKinputPMOSFinger2 = None, _PMOSFinger = None, _PMOSChannelWidth = None,
                                      _ChannelLength = None, _Dummy = False, _SLVT = False, _GuardringWidth = None, _Guardring = False,
                                      _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
                                      _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
                                 ):

            _DRCObj = DRC.DRC()
            _XYCoordinateOfPMOS = [[0, 0]]
            _PODummyWidth = 30
            _Name = 'PMOSSetofSlicer'
            _CLKinputPMOSFinger = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2

            ##############################################################################################################################################################
            ################################################################### PMOS Generation  #########################################################################
            ##############################################################################################################################################################

            # PMOS1(CLK input) Generation
            _PMOS1inputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
            _PMOS1inputs['_PMOSNumberofGate'] = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2
            _PMOS1inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS1inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS1inputs['_PMOSDummy'] = _Dummy
            _PMOS1inputs['_SLVT'] = _SLVT
            self._DesignParameter['_PMOS1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS1In{}'.format(_Name)))[0]
            self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS1inputs)

            # PMOS2(CLK input) Generation
            _PMOS2inputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
            _PMOS2inputs['_PMOSNumberofGate'] = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2
            _PMOS2inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS2inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS2inputs['_PMOSDummy'] = _Dummy
            _PMOS2inputs['_SLVT'] = _SLVT
            self._DesignParameter['_PMOS2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS2In{}'.format(_Name)))[0]
            self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS2inputs)

            # PMOS3 Generation
            _PMOS3inputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
            _PMOS3inputs['_PMOSNumberofGate'] = _PMOSFinger
            _PMOS3inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS3inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS3inputs['_PMOSDummy'] = _Dummy
            _PMOS3inputs['_SLVT'] = _SLVT
            self._DesignParameter['_PMOS3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS3In{}'.format(_Name)))[0]
            self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS3inputs)

            # PMOS4 Generation
            _PMOS4inputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
            _PMOS4inputs['_PMOSNumberofGate'] = _PMOSFinger
            _PMOS4inputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOS4inputs['_PMOSChannellength'] = _ChannelLength
            _PMOS4inputs['_PMOSDummy'] = _Dummy
            _PMOS4inputs['_SLVT'] = _SLVT
            self._DesignParameter['_PMOS4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS4In{}'.format(_Name)))[0]
            self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS4inputs)

            #############################################################################################################################################################################
            ################################################################### PMOS Gate Generation ####################################################################################
            #############################################################################################################################################################################
            # CONT Generation for PMOS1 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSGate1In{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS1)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            # CONT Generation for PMOS2 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS2 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS2['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSGate2In{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS2)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            # CONT Generation for PMOS3 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS3 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS3['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSGate3In{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS3)
            del _tmpNumCOX
            del _LenBtwPMOSGates
            #
            # CONT Generation for PMOS4 Gate
            _LenBtwPMOSGates = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1PMOS4 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOX < 1:
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
                _VIAPMOSPoly2Met1PMOS4['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSGate4In{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1PMOS4)
            del _tmpNumCOX
            del _LenBtwPMOSGates

            ##################################################################################################################################################################################
            #################################################################### Coordinate Settings #########################################################################################
            ##################################################################################################################################################################################
            _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength
            _LengthPMOSBtwCOnDummy= _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth/2) + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _PODummyWidth/2
            _LengthPMOSBtwPOnDummy= _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co) + _ChannelLength / 2 \
                                    + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _PODummyWidth/2

            # PMOS3(L) Coordinate Setting
            if (_PMOSFinger % 2) == 0:
                _xycoordinatetmp = [[_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]
            elif (_PMOSFinger % 2) == 1:
                _xycoordinatetmp = [[_XYCoordinateOfPMOS[0][0] - (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]
                self._DesignParameter['_PMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]

            # PMOS4(R) Coordinate Setting
            if (_PMOSFinger % 2) == 0:
                self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwCOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]
            elif (_PMOSFinger % 2) == 1:
                self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] + (_LengthPMOSBtwPO*(_PMOSFinger//2) + _LengthPMOSBtwPOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]

            # CLK PMOS1(L) Coordinate Setting
            if (_CLKinputPMOSFinger % 2) == 0:
                self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]
            elif (_CLKinputPMOSFinger % 2) == 1:
                self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] - abs(2*tmp) - (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]

            # CLK PMOS2(R) Coordinate Setting
            if (_CLKinputPMOSFinger % 2) == 0:
                self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwCOnDummy)  + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]
            elif (_CLKinputPMOSFinger % 2) == 1:
                self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[_XYCoordinateOfPMOS[0][0] + abs(2*tmp) + (_LengthPMOSBtwPO*(_CLKinputPMOSFinger//2) + _LengthPMOSBtwPOnDummy)  + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfPMOS[0][1]]]

            # PMOS Gate Coordinate Setting
            self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2- \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace - _DRCObj._Metal1MinSpacetoGate

                                                                                  ]]

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - \
                                                                           self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace - _DRCObj._Metal1MinSpacetoGate
                                                                                  ]]


            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - \
                                                                            self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace - _DRCObj._Metal1MinSpacetoGate
                                                                                  ]]

            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - \
                                                                            self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace - _DRCObj._Metal1MinSpacetoGate
                                                                                  ]]



            if _PMOSFinger == 1 :
                _LengthBtwPoly2Poly2 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
                _LengthNPolyDummyEdge2OriginX2 = (int(_PMOSFinger / 2) + 1) * _LengthBtwPoly2Poly2 - _ChannelLength / 2 - (
                self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
                # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX2 * _LengthNPolyDummyEdge2OriginX2) + 1
                # _LengthPPolyVIAtoGoDown = math.sqrt(
                #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
                self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'] = [
                  #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2],
                    [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp2], \
                    ]
                self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'] = [
                    [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp2]
                   ]



















            ##################################################################################################################################################################################
            ################################################################# PMOS VIA1 Generation ###########################################################################################
            ##################################################################################################################################################################################
            # VIA Generation for PMOS12 Output
            _VIACLKPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIACLKPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIACLKPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet12)

            # tmp = []
            # for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            #     tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS12tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            # PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger/2):
                            tmpx=[j - (_CLKinputPMOSFinger/2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx = [j - (_CLKinputPMOSFinger/2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx=[j - (_CLKinputPMOSFinger/2-0.5)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx = [j - (_CLKinputPMOSFinger/2-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'] = tmp
            del tmp
            del tmpx
            del _ViaNumY
            print('x')

            # VIA Generation for PMOS23 Output
            _VIACLKPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIACLKPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIACLKPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet23)

            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []

            # for i in range(0, int((_CLKinputPMOSFinger1 + 1) // 2)) :
            #     tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            #     tmp.append([-(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

            tmpx = []
            tmpy = []
            PMOS23tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS23tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS23tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            # PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger/2):
                            tmpx=[j - (_CLKinputPMOSFinger/2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                    #for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx = [j - (_CLKinputPMOSFinger/2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx=[j - (_CLKinputPMOSFinger/2-0.5)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, _CLKinputPMOSFinger/2 + 1):
                            tmpx = [j - (_CLKinputPMOSFinger/2-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)]
            for i in range(len(self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'])):
                tmpy.append([-1 * self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'][i][1]])
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)] + tmpy

            del tmp
            del tmpx
            del tmpy
            del _ViaNumY
            print('x')

            # VIA Generation for PMOS34 Output
            _VIACLKPMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _VIACLKPMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _ViaNumY < 1:
                _ViaNumY = 1
            _VIACLKPMOSMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnPMOSOutputIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIACLKPMOSMet34)

            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
                                 self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            tmpy = []
            PMOS23tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                         self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS23tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1,
                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS23tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                          self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            PMOS12tmp4 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]
            if (_CLKinputPMOSFinger % 2) == 0:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger / 2):
                            tmpx = [
                                j - (_CLKinputPMOSFinger / 2 - 1) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1,
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp3:
                        for i in range(0, _CLKinputPMOSFinger / 2 + 1):
                            tmpx = [j - (_CLKinputPMOSFinger / 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1,
                                    self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)

            elif (_CLKinputPMOSFinger % 2) == 1:
                if (_CLKinputPMOSFinger1 % 2) == 0:
                    for j in PMOS12tmp:
                        for i in range(0, _CLKinputPMOSFinger / 2 + 1):
                            tmpx = [
                                j - (_CLKinputPMOSFinger / 2 - 0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1,
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)
                elif (_CLKinputPMOSFinger1 % 2) == 1:
                    for j in PMOS12tmp2:
                        for i in range(0, _CLKinputPMOSFinger / 2 + 1):
                            tmpx = [
                                j - (_CLKinputPMOSFinger / 2 - 0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1,
                                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]
                            tmp.append(tmpx)


            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)]
            for i in range(len(self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'])):
                tmpy.append([-1 * self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][1]])
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'] = tmp[0:int((_CLKinputPMOSFinger1+1) // 2)] + tmpy
            del tmp
            del tmpx
            del tmpy
            del _ViaNumY
            print('x')


            # VIA Generation for Inner PMOS34 Output
            _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn2{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)

            _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _ViaNumY < 1 :
                _ViaNumY = 1
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumY
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn2{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)


            # tmp1 = []
            # tmp2 = []
            # for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            #     tmp1.append([self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            #     tmp2.append([-(self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]])

            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            PMOS34tmp = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]+_LengthPMOSBtwMet1]
            PMOS34tmp2 = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]]

            if (_PMOSFinger % 2) == 1:
                for j in PMOS34tmp:
                    for i in range(0, (_PMOSFinger-1)/ 2 + 1):
                        tmpx=[j - ((_PMOSFinger+1)/2 + 0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1 * (2*i+1), self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            elif (_PMOSFinger % 2) == 0:
                for j in PMOS34tmp2:
                    for i in range(0, _PMOSFinger/2+1):
                        tmpx=[j - (_PMOSFinger/2)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1 * (2*i), self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'] = tmp
  #          self._DesignParameter['_ViaMet22Met3OnPMOSOutput2']['_XYCoordinates'] = tmp
            del tmp
            del tmpx
          #  del tmp1
          #  del tmp2
            del _ViaNumY
            print('x')

            #######################################################################################################################################################################################
            ############################################### Additional POLY Layer Generation to avoid DRC Error ####################################################################################
            ########################################################################################################################################################################################
            self._DesignParameter['_AdditionalPolyOnPMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            # PMOS1 Poly Layer Generation
            tmp1 = [[[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_AdditionalPolyOnPMOS1']['_XYCoordinates'] = tmp1
            self._DesignParameter['_AdditionalPolyOnPMOS1']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']


            self._DesignParameter['_AdditionalPolyGateOnPMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS1']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnPMOS1']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp

    # PMOS2 Poly Layer Generation
            tmp2 = [[[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS2']['_XYCoordinates'] = tmp2
            self._DesignParameter['_AdditionalPolyOnPMOS2']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS2']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnPMOS2']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp



            # PMOS3 Poly Layer Generation
            tmp3 = [[[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS3']['_XYCoordinates'] = tmp3
            self._DesignParameter['_AdditionalPolyOnPMOS3']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS3']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnPMOS3']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp



            # PMOS4 Poly Layer Generation
            tmp4 = [[[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnPMOS4']['_XYCoordinates'] = tmp4
            self._DesignParameter['_AdditionalPolyOnPMOS4']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnPMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnPMOS4']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnPMOS4']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp

            #########################################################################################################################################
            ############################################### Guardring Generation ####################################################################
            #########################################################################################################################################
            if _Guardring == True:
                print ('#################################     Guardring Layer Generation ###########################################')
                self._DesignParameter['_RingMetal1Layer1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400)
                self._DesignParameter['_RingMetal1Layer2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400)
                self._DesignParameter['_RingMetal1Layer3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingMetal1Layer4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingODLayer1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingODLayer2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingODLayer3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingODLayer4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=400)

                self._DesignParameter['_RingMetal1Layer1']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer2']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer3']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer4']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer1']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer2']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer3']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer4']['_Width'] = _GuardringWidth

                toptmp = self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + (_DRCObj._PMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + 10
                bottomtmp = self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 - (_DRCObj._PMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) - 2*_DRCObj._Metal1MinEnclosureCO2 - self._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] # - _DRCObj._CoMinWidth - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']
                lefttmp = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (_DRCObj._PMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - 35
                righttmp = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + (_DRCObj._PMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + 35

                tmp5 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2, toptmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2, toptmp]]] # top
                tmp6 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2, bottomtmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2, bottomtmp]]] # bottom
                tmp7 = [[[lefttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2], [lefttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2]]] # left
                tmp8 = [[[righttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2], [righttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2]]] #right

                self._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'] = tmp5
                self._DesignParameter['_RingMetal1Layer2']['_XYCoordinates'] = tmp6
                self._DesignParameter['_RingMetal1Layer3']['_XYCoordinates'] = tmp7
                self._DesignParameter['_RingMetal1Layer4']['_XYCoordinates'] = tmp8

                self._DesignParameter['_RingODLayer1']['_XYCoordinates'] = tmp5
                self._DesignParameter['_RingODLayer2']['_XYCoordinates'] = tmp6
                self._DesignParameter['_RingODLayer3']['_XYCoordinates'] = tmp7
                self._DesignParameter['_RingODLayer4']['_XYCoordinates'] = tmp8


            # CONT Generation for Guardring
                self._DesignParameter['_CONT1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_CONT2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

                self._DesignParameter['_CONT1']['_XWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT1']['_YWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT2']['_XWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT2']['_YWidth'] = _DRCObj._CoMinWidth

                _XNumberOfCO1 = int((righttmp - lefttmp - self._DesignParameter['_RingMetal1Layer1']['_Width']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) # Horizontal Ring
                _YNumberOfCO1 = self._DesignParameter['_RingMetal1Layer1']['_Width'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                _XNumberOfCO2 = self._DesignParameter['_RingMetal1Layer1']['_Width'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                _YNumberOfCO2 = (toptmp - bottomtmp - self._DesignParameter['_RingMetal1Layer1']['_Width']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)  # Verical Ring

            # CONT Coordinate Setting
            _LengthRingBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
            tmp = []
            tmp2=[toptmp, bottomtmp]

            for i in range(0, _XNumberOfCO1):
                for j in range(0, _YNumberOfCO1):
                    for k in tmp2:
                        if (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 0:
                            _xycoordinatetmp = [(righttmp+lefttmp)/2 - (_XNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 1:
                            _xycoordinatetmp = [(righttmp+lefttmp)/2 - (_XNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 0:
                            _xycoordinatetmp = [(righttmp+lefttmp)/2 - (_XNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 1:
                            _xycoordinatetmp = [(righttmp+lefttmp)/2 - (_XNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        tmp.append(_xycoordinatetmp)
            self._DesignParameter['_CONT1']['_XYCoordinates'] = tmp

            tmp = []
            tmp2 = [-1, 1]
            for i in range(0, _XNumberOfCO2):
                for j in range(0, _YNumberOfCO2):
                    for k in tmp2:
                        if (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 0:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp+bottomtmp)/2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp+bottomtmp)/2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 0:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp+bottomtmp)/2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp+bottomtmp)/2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        tmp.append(_xycoordinatetmp)
            self._DesignParameter['_CONT2']['_XYCoordinates'] = tmp

            #########################################################################################################################################
            ############################################### NW layer Generation #####################################################################
            #########################################################################################################################################
            self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NWLayer']['_XWidth'] = righttmp - lefttmp + self._DesignParameter['_RingMetal1Layer1']['_Width'] + 2*_DRCObj._NwMinSpacetoRX
            self._DesignParameter['_NWLayer']['_YWidth'] = toptmp - bottomtmp + self._DesignParameter['_RingMetal1Layer1']['_Width'] + 2*_DRCObj._NwMinSpacetoRX
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[(righttmp+lefttmp)/2, (toptmp+bottomtmp)/2]]

            ###########################################################################################################################################
            ############################################### SLVT layer Generation #####################################################################
            ###########################################################################################################################################
            self._DesignParameter['_SLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],_Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]
            self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']
            self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = [[(righttmp+lefttmp)/2, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]

            ###########################################################################################################################################
            ############################################### BP layer Generation #####################################################################
            ###########################################################################################################################################
            self._DesignParameter['_BPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_BPLayer']['_XWidth'] = self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]
            self._DesignParameter['_BPLayer']['_YWidth'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']
            self._DesignParameter['_BPLayer']['_XYCoordinates'] = [[(righttmp+lefttmp)/2, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]]

            #########################################################################################################################################
            ################################################ Routing Generation #####################################################################
            #########################################################################################################################################
            # PMOS Metal1 VDD --- Source Routing
            self._DesignParameter['_VDDMet1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_VDDMet1']['_Width'] = _DRCObj._CoMinWidth + 2*_DRCObj._Metal1MinEnclosureCO

            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmpx  = []
            VDDtmp = toptmp
            MOStmp = self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2
            # PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1, self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]
            # PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]
            PMOS34tmp = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]]
            PMOS34tmp2 = [self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]-_LengthPMOSBtwMet1]

            PMOS12tmp = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1]
            PMOS12tmp2 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] - _LengthPMOSBtwMet1]
            PMOS12tmp3 = [self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0]]

            print('x')



            ##################### PMOS12 VDD Met2 Routing Coordinate ############################
            if (_CLKinputPMOSFinger % 2) == 0: # Even = Finger1+Finger2
                if (_CLKinputPMOSFinger1 % 2) == 1: # Even = Finger1+Finger2 and Odd = Finger1
                    for i in range (0, _CLKinputPMOSFinger/2): # The number of the VDD routing
                        for k in PMOS12tmp3:
                            tmpx.append([[k-(_CLKinputPMOSFinger/2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, VDDtmp],
                                         [k-(_CLKinputPMOSFinger/2 - 1)*_LengthPMOSBtwMet1 + (2*i)*_LengthPMOSBtwMet1, MOStmp]])
                elif (_CLKinputPMOSFinger1 % 2) == 0: # Even = Finger1+Finger2 and Even = Finger1
                    for i in range (0, _CLKinputPMOSFinger/2 + 1):
                        for k in PMOS12tmp3:
                            tmpx.append([[k - (_CLKinputPMOSFinger / 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, VDDtmp],
                                         [k - (_CLKinputPMOSFinger / 2) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MOStmp]])

            elif (_CLKinputPMOSFinger % 2) == 1: # Odd = Finger1+Finger2
                if (_CLKinputPMOSFinger1 % 2) == 0: # Odd = Finger1 + Finger2 and Even = Finger1
                    for i in range (0, (_CLKinputPMOSFinger/2 + 1)): # + 0.5
                        for k in PMOS12tmp:
                            tmpx.append([[k - ((_CLKinputPMOSFinger / 2)+0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, VDDtmp],
                                         [k - ((_CLKinputPMOSFinger / 2)+0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MOStmp]])
                elif (_CLKinputPMOSFinger1 % 2) == 1: # Odd = Finger1+Finger2 and Odd = Finger1
                    for i in range (0, (_CLKinputPMOSFinger/2 + 1)): # + 0.5
                        for k in PMOS12tmp2:
                            tmpx.append([[k - ((_CLKinputPMOSFinger/2)-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, VDDtmp],
                                         [k - ((_CLKinputPMOSFinger/2)-0.5) * _LengthPMOSBtwMet1 + (2 * i) * _LengthPMOSBtwMet1, MOStmp]])



            if (_PMOSFinger % 2 ) == 1:
                for i in range(0, (_PMOSFinger - 1)/2 + 1 ):
                    for k in PMOS34tmp2:
                        tmpx.append([[k - ((_PMOSFinger+1)/2-0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), VDDtmp],
                                     [k - ((_PMOSFinger+1)/2-0.5)*_LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MOStmp]
                                    ])
            elif (_PMOSFinger % 2) == 0:
                for i in range(0, _PMOSFinger / 2):
                    for k in PMOS34tmp:
                        tmpx.append([[k - (_PMOSFinger/2) * _LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), VDDtmp],
                                     [k - (_PMOSFinger/2) * _LengthPMOSBtwMet1 + _LengthPMOSBtwMet1*(i*2+1), MOStmp]
                                    ])

            self._DesignParameter['_VDDMet1']['_XYCoordinates'] = tmpx

            print('x')

            # axis variable
            self._DesignParameter['PMOS_toptmp']= {'_Ignore': toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_bottomtmp']= {'_Ignore': bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_righttmp']= {'_Ignore': righttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['PMOS_lefttmp']= {'_Ignore': lefttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}




            #########################################################################################################################################
            ################################################ Routing Generation #####################################################################
            #########################################################################################################################################
            # # PMOS Met2 Routing
            # self._DesignParameter['_Met2PMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met2PMOS']['_Width'] = _DRCObj._MetalxMinWidth
            # # k = len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'])
            # k = _CLKinputPMOSFinger//2
            #
            # self._DesignParameter['_Met2PMOS']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0], self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1], self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k+2]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k], self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0]],
            #
            #                                                         [self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k+1], self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][-1]]
            #                                                        ]

            print('xxx')

            pass
if __name__ == '__main__':
    PMOSSetofSlicerObj = _PMOSWithDummyOfSlicer(_DesignParameter=None, _Name='PMOSSetofSlicer')
    PMOSSetofSlicerObj._CalculateDesignParameter(_ChannelLength=30, _VDD2VSSHeight=None, _Dummy=True, _SLVT=True,
                                                       _GuardringWidth=100, _Guardring=True,
                                                       _PMOSFinger=2, _CLKinputPMOSFinger1=2, _CLKinputPMOSFinger2=2, _PMOSChannelWidth=1000)

    PMOSSetofSlicerObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PMOSSetofSlicerObj._DesignParameter)
    _fileName = 'autoInverter_HeightCal2.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = PMOSSetofSlicerObj._CreateGDSStream(PMOSSetofSlicerObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
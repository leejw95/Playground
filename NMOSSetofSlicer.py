import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import math
import ContGeneration

import DesignParameters
import user_define_exceptions

import copy
import DRC

import ftplib
from ftplib import FTP
import base64

class _NMOSWithDummyOfSlicer(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
        _DATAinputNMOSFinger = None, _NMOSFinger=None, _CLKinputNMOSFinger=None, _NMOSChannelWidth=None,
        _ChannelLength=None, _Dummy=False, _SLVT=False, _GuardringWidth=None, _Guardring=False,
        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NPRatio=None, _VDD2VSSHeight=None,
        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None)



    def __init__(self, _DesignParameter=None, _Name='NMOSSetofSlicer'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateDesignParameter(self, _DATAinputNMOSFinger = None, _NMOSFinger = None, _CLKinputNMOSFinger = None, _NMOSChannelWidth = None,
                                      _ChannelLength = None, _Dummy = False, _SLVT = False, _GuardringWidth = None, _Guardring = False,
                                      _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NPRatio = None, _VDD2VSSHeight = None,
                                      _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
                                 ):

            _DRCObj = DRC.DRC()
            _XYCoordinateOfNMOS = [[0, 0]]
            _PODummyWidth = 30
            _Name = 'NMOSSetofSlicer'
            ##############################################################################################################################################################
            ################################################################### PMOS Generation  #########################################################################
            ##############################################################################################################################################################

            # NMOS1(Data input) Generation
            _NMOS1inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOS1inputs['_NMOSNumberofGate'] = _DATAinputNMOSFinger
            _NMOS1inputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOS1inputs['_NMOSChannellength'] = _ChannelLength
            _NMOS1inputs['_NMOSDummy'] = _Dummy
            _NMOS1inputs['_SLVT'] = _SLVT
            self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS1In{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS1inputs)

            # NMOS2(Data input) Generation
            _NMOS2inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOS2inputs['_NMOSNumberofGate'] = _DATAinputNMOSFinger
            _NMOS2inputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOS2inputs['_NMOSChannellength'] = _ChannelLength
            _NMOS2inputs['_NMOSDummy'] = _Dummy
            _NMOS2inputs['_SLVT'] = _SLVT
            self._DesignParameter['_NMOS2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS2In{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS2inputs)

            # NMOS3 Generation
            _NMOS3inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOS3inputs['_NMOSNumberofGate'] = _NMOSFinger
            _NMOS3inputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOS3inputs['_NMOSChannellength'] = _ChannelLength
            _NMOS3inputs['_NMOSDummy'] = _Dummy
            _NMOS3inputs['_SLVT'] = _SLVT
            self._DesignParameter['_NMOS3'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS3In{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS3inputs)

            # NMOS4 Generation
            _NMOS4inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOS4inputs['_NMOSNumberofGate'] = _NMOSFinger
            _NMOS4inputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOS4inputs['_NMOSChannellength'] = _ChannelLength
            _NMOS4inputs['_NMOSDummy'] = _Dummy
            _NMOS4inputs['_SLVT'] = _SLVT
            self._DesignParameter['_NMOS4'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS4In{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS4inputs)

            # NMOS5(CLK input) Generation
            _NMOS5inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOS5inputs['_NMOSNumberofGate'] = _CLKinputNMOSFinger
            _NMOS5inputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOS5inputs['_NMOSChannellength'] = _ChannelLength
            _NMOS5inputs['_NMOSDummy'] = _Dummy
            _NMOS5inputs['_SLVT'] = _SLVT
            self._DesignParameter['_NMOS5'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0,_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS5In{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS5']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS5inputs)
            ##################################################################################################################################################################################

            #############################################################################################################################################################################
            ################################################################### NMOS Gate Generation ####################################################################################
            #############################################################################################################################################################################
            # VIA1 Generation for NMOS1 Gate (Data Input)
            _LenBtwNMOSGates = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1NMOS1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOY = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOY < 1:
                _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOY'] = 2
                if _DATAinputNMOSFinger == 1 :
                    _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOY
                _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOY'] = 2
                if _DATAinputNMOSFinger == 1 :
                    _VIANMOSPoly2Met1NMOS1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1NMOS1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSGate1In{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1NMOS1)
            del _tmpNumCOY
            del _LenBtwNMOSGates

            # VIA Generation for NMOS2 Gate (Data Input)
            _LenBtwNMOSGates = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1NMOS2 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOY = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOY < 1:
                _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOY'] = 2
                if _DATAinputNMOSFinger == 1 :
                    _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOY'] = 1

            else:
                _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOY
                _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOY'] = 2
                if _DATAinputNMOSFinger == 1 :
                    _VIANMOSPoly2Met1NMOS2['_ViaPoly2Met1NumberOfCOY'] = 1


            self._DesignParameter['_VIANMOSPoly2Met1NMOS2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSGate2In{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1NMOS2)
            del _tmpNumCOY
            del _LenBtwNMOSGates

            # VIA Generation for NMOS3 Gate
            _LenBtwNMOSGates = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1NMOS3 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOY = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOY < 1:
                _VIANMOSPoly2Met1NMOS3['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIANMOSPoly2Met1NMOS3['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIANMOSPoly2Met1NMOS3['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOY
                _VIANMOSPoly2Met1NMOS3['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1NMOS3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSGate3In{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1NMOS3)
            del _tmpNumCOY
            del _LenBtwNMOSGates

            #
            # VIA Generation for NMOS4 Gate
            _LenBtwNMOSGates = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1NMOS4 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOY = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

            if _tmpNumCOY < 1:
                _VIANMOSPoly2Met1NMOS4['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIANMOSPoly2Met1NMOS4['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIANMOSPoly2Met1NMOS4['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOY
                _VIANMOSPoly2Met1NMOS4['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1NMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSGate4In{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1NMOS4)
            del _tmpNumCOY
            del _LenBtwNMOSGates

            # VIA Generation for NMOS5 Gate
            _LenBtwNMOSGates = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
                               self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1NMOS5 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOY = int(_LenBtwNMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            # _tmpNumCOX = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)


            if _tmpNumCOY < 1:
                _VIANMOSPoly2Met1NMOS5['_ViaPoly2Met1NumberOfCOX'] = 1
                _VIANMOSPoly2Met1NMOS5['_ViaPoly2Met1NumberOfCOY'] = 1
            else:
                _VIANMOSPoly2Met1NMOS5['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOY
                _VIANMOSPoly2Met1NMOS5['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1NMOS5'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGate5In{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1NMOS5)
            del _tmpNumCOY
            del _LenBtwNMOSGates

            ##################################################################################################################################################################################
            #################################################################### Coordinate Settings #########################################################################################
            ##################################################################################################################################################################################

            _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength
            _LengthNMOSBtwCOnDummy= _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth/2) + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _PODummyWidth/2
            _LengthNMOSBtwPOnDummy= _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co) + _ChannelLength / 2 \
                                    + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + _PODummyWidth/2

            # NMOS3(L) Coordinate Setting
            if (_NMOSFinger % 2) == 0:
                _xycoordinatetmp = [[_XYCoordinateOfNMOS[0][0] - (_LengthNMOSBtwPO*(_NMOSFinger//2) + _LengthNMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2 , _XYCoordinateOfNMOS[0][1]]]
                self._DesignParameter['_NMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]
            elif (_NMOSFinger % 2) == 1:
                _xycoordinatetmp = [[_XYCoordinateOfNMOS[0][0] - (_LengthNMOSBtwPO*(_NMOSFinger//2) + _LengthNMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]
                self._DesignParameter['_NMOS3']['_XYCoordinates'] = _xycoordinatetmp
                tmp=_xycoordinatetmp[0][0]

            # NMOS4(R) Coordinate Setting
            if (_NMOSFinger % 2) == 0:
                self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] + (_LengthNMOSBtwPO*(_NMOSFinger//2) + _LengthNMOSBtwCOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]
            elif (_NMOSFinger % 2) == 1:
                self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] + (_LengthNMOSBtwPO*(_NMOSFinger//2) + _LengthNMOSBtwPOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]

            # DATA NMOS1(L) Coordinate Setting
            if (_DATAinputNMOSFinger % 2) == 0:
                self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] - abs(2*tmp) - (_LengthNMOSBtwPO*(_DATAinputNMOSFinger//2) + _LengthNMOSBtwCOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]
            elif (_DATAinputNMOSFinger % 2) == 1:
                self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] - abs(2*tmp) - (_LengthNMOSBtwPO*(_DATAinputNMOSFinger//2) + _LengthNMOSBtwPOnDummy) - _DRCObj._PolygateMinSpace/2 - _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]

            # DATA NMOS2(R) Coordinate Setting
            if (_DATAinputNMOSFinger % 2) == 0:
                self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] + abs(2*tmp) + (_LengthNMOSBtwPO*(_DATAinputNMOSFinger//2) + _LengthNMOSBtwCOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]
            elif (_DATAinputNMOSFinger % 2) == 1:
                self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0] + abs(2*tmp) + (_LengthNMOSBtwPO*(_DATAinputNMOSFinger//2) + _LengthNMOSBtwPOnDummy) + _DRCObj._PolygateMinSpace/2 + _PODummyWidth/2, _XYCoordinateOfNMOS[0][1]]]

            # CLK NMOS5 Coordinate Setting
            SpaceBtwNMOS = 250
            if (_DATAinputNMOSFinger % 2) == 0:
                self._DesignParameter['_NMOS5']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0],
                                                                      _XYCoordinateOfNMOS[0][1] - (self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + SpaceBtwNMOS)
                                                                    ]]
            elif (_DATAinputNMOSFinger % 2) == 1:
                self._DesignParameter['_NMOS5']['_XYCoordinates'] = [[_XYCoordinateOfNMOS[0][0],
                                                                      _XYCoordinateOfNMOS[0][1] - (self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + SpaceBtwNMOS)
                                                                    ]]

            if _CLKinputNMOSFinger > 2 * _NMOSFinger + 4 :
                self._DesignParameter['_NMOS5']['_XYCoordinates'] = [[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] -  _DRCObj._PolygateMinSpace - 3 *_DRCObj._PolygateMinWidth]]




            #################################################################### NMOS Gate Coordinate Setting ###################################################################
            # self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
            #                                                                self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                                self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate ]]
            #
            # self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
            #                                                                self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                                self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate ]]
            #
            # self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
            #                                                                 self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                                 self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate ]]
            #
            # self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
            #                                                                 self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                                 self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate ]]
            #
            # self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'] = [[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0],
            #                                                                 self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                                 self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpacetoGate ]]

            # if _DATAinputNMOSFinger == 1:
            #     _LengthBtwPoly2Poly1 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            #     _LengthNPolyDummyEdge2OriginX1 = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly1 - _ChannelLength / 2 - (
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #     # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
            #     # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #
            #     _LengthNPolyVIAtoGoUp1 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX1 * _LengthNPolyDummyEdge2OriginX1) + 1
            #     # _LengthPPolyVIAtoGoDown = math.sqrt(
            #     #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'] = [
            #         [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp1],
            #         ]
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'] = [
            #     [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp1]
            #        ]
            #
            # if _NMOSFinger == 1 :
            #     _LengthBtwPoly2Poly2 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            #     _LengthNPolyDummyEdge2OriginX2 = (int(_NMOSFinger / 2) + 1) * _LengthBtwPoly2Poly2 - _ChannelLength / 2 - (
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #     # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
            #     # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #
            #     _LengthNPolyVIAtoGoUp2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX2 * _LengthNPolyDummyEdge2OriginX2) + 1
            #     # _LengthPPolyVIAtoGoDown = math.sqrt(
            #     #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'] = [
            #       #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2],
            #         [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2], \
            #         ]
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'] = [
            #         [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2]
            #        ]
            # #
            # if _CLKinputNMOSFinger == 1 :
            #     _LengthBtwPoly2Poly3 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            #     _LengthNPolyDummyEdge2OriginX3 = (int(_CLKinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly3 - _ChannelLength / 2 - (
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #     # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
            #     # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            #
            #     _LengthNPolyVIAtoGoUp3 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX3 * _LengthNPolyDummyEdge2OriginX3) + 1
            #     # _LengthPPolyVIAtoGoDown = math.sqrt(
            #     #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            #     self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'] = [
            #       #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2],
            #         [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp3]
            #        ]





            ##################################################################################################################################################################################
            ################################################################# NMOS VIA1 Generation ###########################################################################################
            ##################################################################################################################################################################################
            ####################################################### VIA Generation for Data NMOS Drain #######################################################
            _VIADataPMOSDrainMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIADataPMOSDrainMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumCOY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1 ####int(_NMOSChannelWidth // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _ViaNumCOY < 1 :
                _ViaNumCOY = 1
            # if 400 <= _NMOSChannelWidth < 800 :
            #     _ViaNumCOY = _ViaNumCOY - 1
            # if _NMOSChannelWidth < 400 :
            #     _VIaNumCOY = 2
            _VIADataPMOSDrainMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumCOY
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIADataPMOSDrainMet12)

            _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
            _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp1 = []
            tmp2 = []
            if _DATAinputNMOSFinger % 2 == 0 :
                for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
                    tmp1.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4])
                    tmp1.append([self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4])
                for j in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
                    tmp2.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][1] - _LengthbtwViaCentertoViaCenter / 4])
                    tmp2.append([self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][1] - _LengthbtwViaCentertoViaCenter / 4])
            elif _DATAinputNMOSFinger % 2 != 0:
                for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
                    tmp1.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4])
                    tmp1.append([self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4])
                for j in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
                    tmp2.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][1] - _LengthbtwViaCentertoViaCenter / 4])
                    tmp2.append([self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][1] - _LengthbtwViaCentertoViaCenter / 4])


            # tmpx = []
            # NMOS12tmp = [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0]]
            # if (_DATAinputNMOSFinger % 2) == 1:
            #     for i in range(0, (_DATAinputNMOSFinger-1)/2 + 1):
            #         for j in NMOS12tmp:
            #             tmpx = [j - ((_DATAinputNMOSFinger-1)/2 + 0.5)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1*(2*i),
            #                     self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] \
            #                     + (self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2]
            #             tmp.append(tmpx)
            # elif (_DATAinputNMOSFinger % 2) == 0:
            #     for i in range(0, (_DATAinputNMOSFinger)/2 + 1):
            #         for j in NMOS12tmp:
            #             tmpx = [j - (_DATAinputNMOSFinger/2)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1*(2*i),
            #                     self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] \
            #                     + (self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2]
            #             tmp.append(tmpx)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'] = tmp1 + tmp2
            del tmp1
            del tmp2
            del _ViaNumCOY



            ############################################################### VIA Generation for Inner NMOS Drain ##############################################################
            _VIAInnerPMOSDrainMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNumCOY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1 ###int(_NMOSChannelWidth // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) - 1
            if _ViaNumCOY < 1:
                _ViaNumCOY = 1

            _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumCOY

            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn3{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAInnerPMOSDrainMet12)
            #

            #
            # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            # tmp1 = []
            # tmp2 = []
            #
            #
            # tmp = []
            # tmpx = []
            # NMOS12tmp = [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0]-_LengthNMOSBtwMet1, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]]
            # NMOS12tmp2 = [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - _LengthNMOSBtwMet1, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] - _LengthNMOSBtwMet1]
            #
            #
            #
            # if (_NMOSFinger % 2) == 1:
            #     for j in NMOS12tmp:
            #         for i in range(0, (_NMOSFinger - 1) / 2 + 1):
            #             tmpx = [j - ((_NMOSFinger - 1) / 2 + 0.5) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2 * i + 1), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - _LengthbtwViaCentertoViaCenter / 4] #- _DRCObj._MetalxMinSpace4]
            #             tmp.append(tmpx)
            #
            # elif (_NMOSFinger % 2) == 0:
            #     for j in NMOS12tmp2:
            #         for i in range(0, (_NMOSFinger)/2 + 1):
            #             tmpx = [j - (_NMOSFinger/2)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1*(2*i+1), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - _LengthbtwViaCentertoViaCenter / 4]#- _DRCObj._MetalxMinSpace4]
            #             tmp.append(tmpx)
            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'] = tmp
            # del tmp1
            # del tmp2
            # del _ViaNumCOY
            #
            # _VIAInnerPMOSDrainMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOX'] = 1
            # _ViaNumCOY2 = int((_NMOSChannelWidth / 2 - _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            # if _ViaNumCOY2 < 2:
            #     _ViaNumCOY2 = 1
            # else :
            #     _ViaNumCOY2 = 2
            _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumCOY
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn3{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAInnerPMOSDrainMet12)
            tmp = []
            # if _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOY'] != 1 :
            #     for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            #         tmp.append([self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][1]])
            #         tmp.append([-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][1]])
            #     self._DesignParameter['_AdditionalViaMet12Met2OnNMOSOutput3']['_XYCoordinates'] = tmp
            tmpx = []
            #if _VIAInnerPMOSDrainMet12['_ViaMet12Met2NumberOfCOY'] == 1 :
            for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmpx.append([self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4]) ##self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_AdditionalViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2])
                tmpx.append([-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + _LengthbtwViaCentertoViaCenter / 4])##self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_AdditionalViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2])
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'] = tmpx

            del tmp
            del tmpx
            del _ViaNumCOY

            # if (self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea) :
            #     if (_NMOSFinger == 1):
            #         self._DesignParameter['_Met2OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #         self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'] = 73
            #         self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] = 174
            #         self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates']
            #
            #         self._DesignParameter['_Met3OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #         self._DesignParameter['_Met3OnNMOS4forArea']['_XWidth'] = 73
            #         self._DesignParameter['_Met3OnNMOS4forArea']['_YWidth'] = 174



                   # self._DesignParameter['_Met3OnNMOS4forArea']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates']

                # self._DesignParameter['_Met2OnNMOS4forDRC'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                # self._DesignParameter['_Met2OnNMOS4forDRC']['_Width'] = self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth']
                # self._DesignParameter['_Met2OnNMOS4forDRC']['_XYCoordinates'] = [[self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'][0], [self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2], \
                #                                                                  [self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'][1], [self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2]]]]
                #





            ############################################################### Met2 Generation for Inner NMOS Drain ##############################################################
            # self._DesignParameter['InnerNMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['InnerNMOS1']['_Width'] = _DRCObj._MetalxMinWidth
            #
            # k=len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'])
            # self._DesignParameter['InnerNMOS1']['_XYCoordinates'] = [[
            #                                                          [self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0],
            #                                                           self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]],
            #                                                          [self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][k/2-1][0],
            #                                                           self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]]],
            #
            #                                                          [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][-1][0],
            #                                                           self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][k/2][0],
            #                                                            self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]]
            #                                                         ]]
            #
            #
            # print('x')

            ############################################################### VIA Generation for Inner NMOS Source ##############################################################
            # _VIAInnerPMOSSourceMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _VIAInnerPMOSSourceMet12['_ViaMet12Met2NumberOfCOX'] = 1
            # _ViaNumCOY = int(_NMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _ViaNumCOY < 1:
            #     _ViaNumCOY = 1
            # _VIAInnerPMOSSourceMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumCOY
            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput4'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn4{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAInnerPMOSSourceMet12)
            #
            # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            # tmp = []
            # tmpx = []
            # NMOS12tmp = [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0]+_LengthNMOSBtwMet1, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]]
            # NMOS12tmp2 = [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + _LengthNMOSBtwMet1, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]+_LengthNMOSBtwMet1]
            #
            # if (_NMOSFinger % 2) == 1:
            #     for j in NMOS12tmp:
            #         for i in range(0, (_NMOSFinger-1)/2 + 1):
            #             tmpx = [j - ((_NMOSFinger-1)/2 + 0.5)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1*(2*i),
            #                     self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] \
            #                     + (self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2]
            #             tmp.append(tmpx)
            #
            #
            # elif (_NMOSFinger % 2) == 0:
            #     for j in NMOS12tmp2:
            #         for i in range(0, _NMOSFinger/2):
            #             tmpx = [j - (_NMOSFinger / 2) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2 * i),
            #                     self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] \
            #                     + (self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2
            #                     ]
            #             tmp.append(tmpx)
            # self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'] = tmp
            # del _ViaNumCOY


            ############################################################### VIA Generation for CLK NMOS Drain ##############################################################
            _VIACLKNMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)

            _tmpNumCOY = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)
            _VIACLKNMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _VIACLKNMOSMet12['_ViaMet12Met2NumberOfCOY'] = _tmpNumCOY

            self._DesignParameter['_ViaMet12Met2OnNMOSOutput5'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn5{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIACLKNMOSMet12)

            _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            tmpx = []
            if (_CLKinputNMOSFinger % 2) == 1:
                for i in range(0, (_CLKinputNMOSFinger-1)/ 2 + 1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - ((_CLKinputNMOSFinger+1)/2 + 0.5)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i+1), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            elif (_CLKinputNMOSFinger % 2) == 0:
                for i in range(0, _CLKinputNMOSFinger/2+1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - (_CLKinputNMOSFinger/2)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'] = tmp
            del _tmpNumCOY



            _VIACLKNMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

            _tmpNumCOY = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)
            _VIACLKNMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _VIACLKNMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumCOY

            self._DesignParameter['_ViaMet22Met3OnNMOSOutput5'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn5{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIACLKNMOSMet23)

            tmp = []
            tmpx = []
            if (_CLKinputNMOSFinger % 2) == 1:
                for i in range(0, (_CLKinputNMOSFinger-1)/ 2 + 1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - ((_CLKinputNMOSFinger+1)/2 + 0.5)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i+1), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            elif (_CLKinputNMOSFinger % 2) == 0:
                for i in range(0, _CLKinputNMOSFinger/2+1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - (_CLKinputNMOSFinger/2)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput5']['_XYCoordinates'] = tmp
            del _tmpNumCOY


            _VIACLKNMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)

            _tmpNumCOY = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)
            _VIACLKNMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _VIACLKNMOSMet34['_ViaMet32Met4NumberOfCOY'] = _tmpNumCOY

            self._DesignParameter['_ViaMet32Met4OnNMOSOutput5'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnPMOSOutputIn5{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIACLKNMOSMet34)

            tmp = []
            tmpx = []
            if (_CLKinputNMOSFinger % 2) == 1:
                for i in range(0, (_CLKinputNMOSFinger-1)/ 2 + 1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - ((_CLKinputNMOSFinger+1)/2 + 0.5)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i+1), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            elif (_CLKinputNMOSFinger % 2) == 0:
                for i in range(0, _CLKinputNMOSFinger/2+1):
                        tmpx=[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - (_CLKinputNMOSFinger/2)*_LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (2*i), self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]
                        tmp.append(tmpx)
            self._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_XYCoordinates'] = tmp
            del _tmpNumCOY


            self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4,  self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - \
                                                                           self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

            self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] - max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4, self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - \
                                                                           self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

            self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4, self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + \
                                                                            self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2]]

            self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4, self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + \
                                                                            self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2]]

            self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'] = [[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] + max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4, self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + \
                                                                            self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2]]
            ##+ _DRCObj._Metal1MinSpacetoGate



            if _DATAinputNMOSFinger == 1:
                _LengthBtwPoly2Poly1 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
                _LengthNPolyDummyEdge2OriginX1 = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly1 - _ChannelLength / 2 - (
                self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
                # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp1 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX1 * _LengthNPolyDummyEdge2OriginX1) + 1
                # _LengthPPolyVIAtoGoDown = math.sqrt(
                #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
                self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp1],
                    ]
                self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp1]
                   ]

            if _NMOSFinger == 1 :
                _LengthBtwPoly2Poly2 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
                _LengthNPolyDummyEdge2OriginX2 = (int(_NMOSFinger / 2) + 1) * _LengthBtwPoly2Poly2 - _ChannelLength / 2 - (
                self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
                # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp2 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX2 * _LengthNPolyDummyEdge2OriginX2) + 1
                # _LengthPPolyVIAtoGoDown = math.sqrt(
                #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
                self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'] = [
                  #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2],
                    [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2], \
                    ]
                self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2]
                   ]
            #
            if _CLKinputNMOSFinger == 1 :
                _LengthBtwPoly2Poly3 = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
                _LengthNPolyDummyEdge2OriginX3 = (int(_CLKinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly3 - _ChannelLength / 2 - (
                self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
                # _LengthPPolyDummyEdge2OriginX = (int(_DATAinputNMOSFinger / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (
                # self._DesignParameter['_NMOSFinger']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

                _LengthNPolyVIAtoGoUp3 = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX3 * _LengthNPolyDummyEdge2OriginX3) + 1
                # _LengthPPolyVIAtoGoDown = math.sqrt(
                #     _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
                self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'] = [
                  #  [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp2],
                    [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp3]
                   ]












            #######################################################################################################################################################################################
            ############################################### Additional POLY Layer Generation to avoid DRC Error ####################################################################################
            ########################################################################################################################################################################################
            self._DesignParameter['_AdditionalPolyOnNMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnNMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnNMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnNMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnNMOS5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            # NMOS1 Poly Layer Generation
            tmp1 = [[[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_AdditionalPolyOnNMOS1']['_XYCoordinates'] = tmp1
            self._DesignParameter['_AdditionalPolyOnNMOS1']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnNMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnNMOS1']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnNMOS1']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp

            # NMOS2 Poly Layer Generation
            tmp2 = [[[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnNMOS2']['_XYCoordinates'] = tmp2
            self._DesignParameter['_AdditionalPolyOnNMOS2']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnNMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnNMOS2']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnNMOS2']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp


            # NMOS3 Poly Layer Generation
            tmp3 = [[[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'] = tmp3
            self._DesignParameter['_AdditionalPolyOnNMOS3']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnNMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnNMOS3']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnNMOS3']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp


            # NMOS4 Poly Layer Generation
            tmp4 = [[[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'] = tmp4
            self._DesignParameter['_AdditionalPolyOnNMOS4']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnNMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnNMOS4']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnNMOS4']['_Width'] = _DRCObj._PolygateMinWidth
            del tmp


            # NMOS5 Poly Layer Generation
            tmp5 = [[[self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2 +\
                      self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0],
                      self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]]]]
            self._DesignParameter['_AdditionalPolyOnNMOS5']['_XYCoordinates'] = tmp5
            self._DesignParameter['_AdditionalPolyOnNMOS5']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_AdditionalPolyGateOnNMOS5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=400)

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]]])
            self._DesignParameter['_AdditionalPolyGateOnNMOS5']['_XYCoordinates'] = tmp
            self._DesignParameter['_AdditionalPolyGateOnNMOS5']['_Width'] = _DRCObj._PolygateMinWidth
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
                self._DesignParameter['_RingPpLayer1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingPpLayer2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingPpLayer3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_RingPpLayer4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=400)

                self._DesignParameter['_RingMetal1Layer1']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer2']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer3']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingMetal1Layer4']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer1']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer2']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer3']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingODLayer4']['_Width'] = _GuardringWidth
                self._DesignParameter['_RingPpLayer1']['_Width'] = 2 * _DRCObj._PpMinExtensiononPactive2 + _GuardringWidth
                self._DesignParameter['_RingPpLayer2']['_Width'] = 2 * _DRCObj._PpMinExtensiononPactive2 + _GuardringWidth
                self._DesignParameter['_RingPpLayer3']['_Width'] = 2 * _DRCObj._PpMinExtensiononPactive2 + _GuardringWidth
                self._DesignParameter['_RingPpLayer4']['_Width'] = 2 * _DRCObj._PpMinExtensiononPactive2 + _GuardringWidth

                # if _NMOSChannelWidth < 400 :
                #     toptmp = self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + (2 * _DRCObj._NMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + 2*_DRCObj._Metal1MinEnclosureCO2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                # else :
                toptmp = self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace3 + self._DesignParameter['_RingMetal1Layer1']['_Width'] / 2#####self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 + (_DRCObj._NMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + 2*_DRCObj._Metal1MinEnclosureCO2 + self._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                bottomtmp = self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 - (_DRCObj._PMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) - 10
                    # self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 - (_DRCObj._NMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) \
                    #         - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 - self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']/2 - SpaceBtwNMOS - 10
                lefttmp   = min(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (_DRCObj._NMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) - 35
                righttmp  = max(self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + (_DRCObj._NMOS2GuardringMinSpace + self._DesignParameter['_RingMetal1Layer1']['_Width']/2) + 35

                tmp5 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2, toptmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2, toptmp]]] # top
                tmp6 = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2, bottomtmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2, bottomtmp]]] # bottom
                tmp7 = [[[lefttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2], [lefttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2]]] # left
                tmp8 = [[[righttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2], [righttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2]]] #right

                print('x')

                self._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'] = tmp5
                self._DesignParameter['_RingMetal1Layer2']['_XYCoordinates'] = tmp6
                self._DesignParameter['_RingMetal1Layer3']['_XYCoordinates'] = tmp7
                self._DesignParameter['_RingMetal1Layer4']['_XYCoordinates'] = tmp8

                self._DesignParameter['_RingODLayer1']['_XYCoordinates'] = tmp5
                self._DesignParameter['_RingODLayer2']['_XYCoordinates'] = tmp6
                self._DesignParameter['_RingODLayer3']['_XYCoordinates'] = tmp7
                self._DesignParameter['_RingODLayer4']['_XYCoordinates'] = tmp8

                self._DesignParameter['_RingPpLayer1']['_XYCoordinates'] = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2-_DRCObj._PpMinWidth+135+14, toptmp], [righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2+_DRCObj._PpMinWidth-135-14, toptmp]]] # top
                self._DesignParameter['_RingPpLayer2']['_XYCoordinates'] = [[[lefttmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2-_DRCObj._PpMinWidth+135+14, bottomtmp],[righttmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2+_DRCObj._PpMinWidth-135-14, bottomtmp]]] # bottom
                self._DesignParameter['_RingPpLayer3']['_XYCoordinates'] = [[[lefttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2+_DRCObj._PpMinWidth-135-14], [lefttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2-_DRCObj._PpMinWidth+135+14]]]
                self._DesignParameter['_RingPpLayer4']['_XYCoordinates'] = [[[righttmp, toptmp+self._DesignParameter['_RingMetal1Layer1']['_Width']/2+_DRCObj._PpMinWidth-135-14], [righttmp, bottomtmp-self._DesignParameter['_RingMetal1Layer1']['_Width']/2-_DRCObj._PpMinWidth+135+14]]]


            ############################################################### CONT Generation for Guardring ##############################################################
                self._DesignParameter['_CONT1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_CONT2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

                self._DesignParameter['_CONT1']['_XWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT1']['_YWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT2']['_XWidth'] = _DRCObj._CoMinWidth
                self._DesignParameter['_CONT2']['_YWidth'] = _DRCObj._CoMinWidth

                _XNumberOfCO1 = int((righttmp - lefttmp - self._DesignParameter['_RingMetal1Layer1']['_Width']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) # Horizontal Ring
                _YNumberOfCO1 = int(self._DesignParameter['_RingMetal1Layer1']['_Width'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
                _XNumberOfCO2 = int(self._DesignParameter['_RingMetal1Layer1']['_Width'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
                _YNumberOfCO2 = int((toptmp - bottomtmp - self._DesignParameter['_RingMetal1Layer1']['_Width']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))  # Verical Ring

            ############################################################### CONT Coordinate Setting ##############################################################
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
                                                (toptmp + bottomtmp) / 2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp + bottomtmp) / 2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 0:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp + bottomtmp) / 2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [tmp7[0][0][0]*k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                (toptmp + bottomtmp) / 2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        tmp.append(_xycoordinatetmp)
            self._DesignParameter['_CONT2']['_XYCoordinates'] = tmp


            ###########################################################################################################################################
            ############################################### SLVT layer Generation #####################################################################
            ###########################################################################################################################################
            self._DesignParameter['_SLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],_Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]
            self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']
            self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = [[(righttmp+lefttmp)/2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]]


            #########################################################################################################################################
            ################################################ Routing Generation #####################################################################
            #########################################################################################################################################
            # NMOS5 Metal1 GND-Source Routing
            self._DesignParameter['_VSSMet1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_VSSMet1']['_Width'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO

            _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmpx = []
            VSStmp = bottomtmp
            MOStmp = self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2

            if (_CLKinputNMOSFinger % 2) == 1:
                for i in range(0, (_CLKinputNMOSFinger - 1) / 2 + 1):
                        tmpx.append([[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - ((_CLKinputNMOSFinger + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (i * 2 + 1), VSStmp],
                                     [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - ((_CLKinputNMOSFinger + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (i * 2 + 1), MOStmp]
                                     ])
            elif (_CLKinputNMOSFinger % 2) == 0:
                for i in range(0, _CLKinputNMOSFinger / 2):
                        tmpx.append([[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - (_CLKinputNMOSFinger / 2) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (i * 2 + 1), VSStmp],
                                     [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] - (_CLKinputNMOSFinger / 2) * _LengthNMOSBtwMet1 + _LengthNMOSBtwMet1 * (i * 2 + 1), MOStmp]
                                     ])

            self._DesignParameter['_VSSMet1']['_XYCoordinates'] = tmpx

            ############################################################### axis variable ##############################################################
            self._DesignParameter['NMOS_toptmp']= {'_Ignore': toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['NMOS_bottomtmp']= {'_Ignore': bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['NMOS_righttmp']= {'_Ignore': righttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
            self._DesignParameter['NMOS_lefttmp']= {'_Ignore': lefttmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

            ######################################################## NMOS Met2 Routing ########################################################
            self._DesignParameter['_Met1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met1Routing']['_Width'] = _DRCObj._Metal1MinWidth

            self._DesignParameter['_Met1Routing']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_Met1Routing']['_Width'] / 2 - _DRCObj._MetalxMinSpace2], [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_Met1Routing']['_Width'] / 2 - _DRCObj._MetalxMinSpace2]], \
                                                                       [[-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_Met1Routing']['_Width'] / 2 - _DRCObj._MetalxMinSpace2], [-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['_Met1Routing']['_Width'] / 2 - _DRCObj._MetalxMinSpace2]]]



            self._DesignParameter['_Met1NMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met1NMOS']['_Width'] = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
                tmp.append([[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]], \
                            [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_Met1Routing']['_XYCoordinates'][0][0][1]]])

                tmp.append([[-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]], \
                            [-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['_Met1Routing']['_XYCoordinates'][0][0][1]]])


            self._DesignParameter['_Met1NMOS']['_XYCoordinates'] = tmp
            del tmp



            self._DesignParameter['_Met2NMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2NMOS']['_Width'] = _DRCObj._MetalxMinWidth
#            k=len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'])
            tmp = []
            for i in range(0, len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'])) :
                tmp.append([[self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][i][1]],[self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4]])
          #  tmp.append([[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]])
            tmp.append([[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]])
            # for i in range(0, len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
            #     tmp.append([[self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]]])

            # if _NMOSChannelWidth < 400 :
            #     RoutingForShortWidth =  _LengthbtwViaCentertoViaCenter / 2
            # else :
            #     RoutingForShortWidth = 0

            if _NMOSFinger == 1 :
                self._DesignParameter['_Met2NMOS']['_XYCoordinates'] = tmp + [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4]],
                                                                        [[-(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4]],
                                                                        [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2 - _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [-(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2 - _LengthbtwViaCentertoViaCenter / 4]],
                                                                        ]

            else :
                self._DesignParameter['_Met2NMOS']['_XYCoordinates'] = tmp + [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4]],
                                                                        [[-(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [-(self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2 + _LengthbtwViaCentertoViaCenter / 4]],
                                                                        [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2 - _LengthbtwViaCentertoViaCenter / 4], \
                                                                        [-(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2 - _LengthbtwViaCentertoViaCenter / 4]],
                                                                        ]







            self._DesignParameter['_SLVTforArea'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_SLVTforArea']['_Width'] = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']
            self._DesignParameter['_SLVTforArea']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2]]]







            self._DesignParameter['_Met3NMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3NMOS']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met3NMOS']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]]]  ##+ [[[self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]], [self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][_NMOSFinger // 2][0] +  _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]]], [[-(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][_NMOSFinger // 2][0] +  _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]], [-(self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] -  _DRCObj._MetalxMinWidth / 2), self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1]]]]




            self._DesignParameter['_Met4NMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4NMOS']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met4NMOS']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]]]



#                                                                           # [self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][-1]], \
                                                                          #
                                                                          # [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][0][1]-(self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2+_DRCObj._MetalxMinWidth/2],
                                                                          #  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][-1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][0][1]-(self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2+_DRCObj._MetalxMinWidth/2]],
                                                                          #
                                                                          # [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][0][1]+(self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2-_DRCObj._MetalxMinWidth/2],
                                                                          #  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][k/2-1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1]+(self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2-_DRCObj._MetalxMinWidth/2]],
                                                                          #
                                                                          # [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][-1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][0][1] + (self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 - _DRCObj._MetalxMinWidth / 2],
                                                                          #  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][k/2][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1] + (self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 - _DRCObj._MetalxMinWidth / 2]],
                                                                          #
                                                                          # [self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][0],
                                                                          #  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][0][1]-(self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2+_DRCObj._MetalxMinWidth/2]],
                                                                          # [self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][-1],
                                                                          #  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_XYCoordinates'][-1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_XYCoordinates'][0][1] - (self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 + _DRCObj._MetalxMinWidth / 2]]

            del tmp
            print('x')
            print('x')


            ############################################################### Code for re-coordinating of NMOS5 ##############################################################













if __name__ == '__main__':
    NMOSSetofSlicerObj = _NMOSWithDummyOfSlicer(_DesignParameter=None, _Name='NMOSSetofSlicer')
    NMOSSetofSlicerObj._CalculateDesignParameter(_ChannelLength=30, _NPRatio=None, _VDD2VSSHeight=None, _Dummy=True, _SLVT=True,
                                                       _GuardringWidth=100, _Guardring=True,
                                                       _NMOSFinger=2, _DATAinputNMOSFinger=1, _CLKinputNMOSFinger=3, _NMOSChannelWidth=1000)

    NMOSSetofSlicerObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=NMOSSetofSlicerObj._DesignParameter)
    _fileName = 'autoInverter_HeightCal2.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = NMOSSetofSlicerObj._CreateGDSStream(NMOSSetofSlicerObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()


    import ftplib
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('myungguk', 'vmfl!225')
    ftp.cwd('/mnt/sdd/myungguk')
    myfile = open('autoInverter_HeightCal2.gds', 'rb')
    ftp.storbinary('STOR autoInverter_HeightCal2.gds', myfile)
    myfile.close()
    ftp.close()
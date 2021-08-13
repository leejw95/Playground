import math
import copy
import random

#
import StickDiagram
import DesignParameters
import DRC
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import PbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4

#
from Private import FileManage
from Private import MyInfo
import CoordinateCalc
import DRCchecker


class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                           _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                           _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                           _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None,
                                           _NumViaPMOSMet12Met2CoY=None, _NumViaNMOSMet12Met2CoX=None,
                                           _NumViaNMOSMet12Met2CoY=None, _XVT=None, _SupplyLine=None,
                                           _StandAlone_DRCFREE=None)

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
                                  _NumViaNMOSMet12Met2CoX=None, _NumViaNMOSMet12Met2CoY=None, _XVT=None, _SupplyLine=None,
                                  _StandAlone_DRCFREE=None):

        _DRCObj = DRC.DRC()
        _Name = 'Inverter'

        MinSnapSpacing = _DRCObj._MinSnapSpacing


        ''' ------------------------------------------ MOSFET Generation ------------------------------------------- '''
        # 1) _NMOS Generation ------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_XVT'] = _XVT

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_Reflect=[1,0,0], _Angle=0, _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)
        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'] \
            = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']  # swap source-drain


        # 2) _PMOS Generation ------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'] \
            = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']  # swap source-drain


        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        '''
        Need : PMOS(for NbodyContact), NMOS(for PbodyContact)
        Input : _NumSupplyCoX     (optional, default 2)
                _NumSupplyCoY     (optional, default 1)
                _SupplyMet1XWidth (optional)
                _SupplyMet1YWidth (optional)
        '''
        # 1) VDD Generation --------------------------------------------------------------------------------------------
        if _NumSupplyCoX == None:
            XWidthOfPMOS = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            NumSupplyCoXOnVDDVSS = int(XWidthOfPMOS // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
        else:
            NumSupplyCoXOnVDDVSS = _NumSupplyCoX

        NbodyParameters = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters['_NumberOfNbodyCOX'] = NumSupplyCoXOnVDDVSS if (NumSupplyCoXOnVDDVSS > 2) else 2
        NbodyParameters['_NumberOfNbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        NbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        NbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)


        # 2) VSS Generation --------------------------------------------------------------------------------------------
        PbodyParameters = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
        PbodyParameters['_NumberOfPbodyCOX'] = NumSupplyCoXOnVDDVSS if (NumSupplyCoXOnVDDVSS > 2) else 2
        PbodyParameters['_NumberOfPbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        PbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        PbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact_iksu._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**PbodyParameters)


        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        '''
        Need : PMOS, NMOS
        Input : _NumViaPMOSMet12Met2CoX (optional) / default : 1 / if not 1, it won't work properly(Not Tested).
                _NumViaPMOSMet12Met2CoY (optional) / default : calculated by 'YWidth of MOSFET's S/D Metal1' / minimum : 2
        '''
        # 1) VIA Generation for PMOS Output ----------------------------------------------------------------------------
        if _NumViaPMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfPMOSMet1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYPMOS = _NumViaPMOSMet12Met2CoY

        VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaPMOSMet12Met2CoX if (_NumViaPMOSMet12Met2CoX != None) else 1
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIAPMOSMet12)

        # 1-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])

        Area_M1for_ViaMet12Met2OnPMOSOutput = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] \
                                              * self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        if Area_M1for_ViaMet12Met2OnPMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.RoundupMinSnapSpacing((float(_DRCObj._Metal1MinArea) / float(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])), MinSnapSpacing*2)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea


        # 2) VIA Generation for NMOS Output ----------------------------------------------------------------------------
        if _NumViaNMOSMet12Met2CoY == None:  # Default : calculate
            YWidthOfNMOSMet1 = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYNMOS = int((YWidthOfNMOSMet1 - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        else:
            NumViaYNMOS = _NumViaNMOSMet12Met2CoY

        VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaNMOSMet12Met2CoX if (_NumViaNMOSMet12Met2CoX != None) else 1
        VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIANMOSMet12)

        # 2-1) Metal1 YWidth re-calculation
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            = max(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
        Area_M1for_ViaMet12Met2OnNMOSOutput = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] \
                                              * self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        if Area_M1for_ViaMet12Met2OnNMOSOutput < _DRCObj._Metal1MinArea:
            YWidth_recalculated_byMinArea = self.RoundupMinSnapSpacing((float(_DRCObj._Metal1MinArea) / float(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])), MinSnapSpacing * 2)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea


        # 3) VIA Generation for Finger=1 / or calculate input poly-M1 contact YWidth     -> Need to check
        if _Finger == 1:
            _VIAMOSPoly2Met1_F1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOX'] = 1  # Need to Modify (by calculation for wide channel length)
            _VIAMOSPoly2Met1_F1['_ViaPoly2Met1NumberOfCOY'] = 1  # Need to Modify (by user input parameter)
            self._DesignParameter['_VIANMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1_F1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)
            self._DesignParameter['_VIAPMOSPoly2Met1_F1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1_F1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1_F1)
        else:
            WidthOfInputXM1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2  # how?? you have to choose / Need to Modify (by user input parameter) / ambiguous name


        ''' ------------------------------------------ Coordinates setting ----------------------------------------- '''
        # 1) Calculate Distance Between 'Supply rail' and 'MOSFET'  : concern (028nm, 065nm) and (Dummy T/F)
        if DesignParameters._Technology == '028nm':
            tempDRC_OdMinSpace = 80
            DistanceBtwVSS2NMOS1 = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            DistanceBtwVSS2NMOS2 = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + tempDRC_OdMinSpace     # OD Layer(for Pbody) - OD Layer (for NMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVSS2NMOS3 = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                       + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Pbody) - PO Dummy Layer (for NMOS)     OD=RX
            else:
                DistanceBtwVSS2NMOS3 = 0
            DistanceBtwVSS2NMOS = max(DistanceBtwVSS2NMOS1, DistanceBtwVSS2NMOS2, DistanceBtwVSS2NMOS3)

            DistanceBtwVDD2PMOS1 = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + tempDRC_OdMinSpace
            DistanceBtwVD2PMOS2 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                   + tempDRC_OdMinSpace  # OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
            if '_PODummyLayer' in self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter:
                DistanceBtwVDD2PMOS3 = 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                                       + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                       + _DRCObj._PolygateMinSpace2OD  # OD Layer(for Nbody) - PO Dummy Layer (for PMOS)     OD=RX
            else:
                DistanceBtwVDD2PMOS3 = 0
            DistanceBtwVDD2PMOS = max(DistanceBtwVDD2PMOS1, DistanceBtwVD2PMOS2, DistanceBtwVDD2PMOS3)

        elif DesignParameters._Technology == '065nm':
            DistanceBtwVSS2NMOS = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] \
                                  + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']

            DistanceBtwVDD2PMOS = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] \
                                  + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']
        else:
            raise NotImplementedError


        # 2) Calculate Distance between 'MOSFET' and 'Input gate Contact'
        if _Finger != 1:
            if DesignParameters._Technology == '028nm':  # Need to Merge
                DistanceBtwNMOS2PolyInput = 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                      self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                            + 0.5 * WidthOfInputXM1 \
                                            + _DRCObj._Metal1MinSpace2

                DistanceBtwPMOS2PolyInput = 0.5 * max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                      self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                            + 0.5 * WidthOfInputXM1 \
                                            + _DRCObj._Metal1MinSpace2

            elif DesignParameters._Technology == '065nm':    # Need to check
                DistanceBtwNMOS2PolyInput = 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                      self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                            + 0.5 * WidthOfInputXM1 \
                                            + _DRCObj._Metal1MinSpace

                DistanceBtwPMOS2PolyInput = 0.5 * max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                      self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                            + 0.5 * WidthOfInputXM1 \
                                            + _DRCObj._Metal1MinSpace


        elif (_Finger == 1) and (DesignParameters._Technology == '028nm'):  # assumption (same finger on PMOS NMOS)

            XCoordinateOfViaF1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] \
                                 + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * 0.5 \
                                 + _DRCObj._Metal1MinSpaceAtCorner \
                                 + self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * 0.5

            _LengthBtwPolyDummyEdge2PolyEdge = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] \
                                               - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] * 0.5 \
                                               - XCoordinateOfViaF1 \
                                               - self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] * 0.5 \

            ''' Prev. Design
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth

            _LengthBtwPolyDummyEdge2PolyEdge = (_LengthBtwPoly2Poly * (_Finger * 0.5 + 0.5) - _ChannelLength / 2) \
                                               - self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2
            '''
            _LengthNPolyDummytoGoUp_Finger2 = math.sqrt(
                _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1
            _LengthPPolyDummytoGoUp_Finger2 = math.sqrt(
                _DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthBtwPolyDummyEdge2PolyEdge * _LengthBtwPolyDummyEdge2PolyEdge) + 1

            DistanceBtwNMOS2PolyInput = 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                                        + _LengthNPolyDummytoGoUp_Finger2 \
                                        + 0.5 * self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            DistanceBtwPMOS2PolyInput = 0.5 * self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] \
                                        + _LengthPPolyDummytoGoUp_Finger2 \
                                        + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']
        else:
            raise NotImplementedError


        # 3) Calculate Total Minimum Height of Inverter (Between Supply rails, VDD - VSS)
        if DesignParameters._Technology == '028nm':
            _VDD2VSSMinHeight = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS
        elif DesignParameters._Technology == '065nm':  # Need to consider NP PP Layer overlapped
            # 1) Overlapped polygate of PMOS and NMOS -> PP and NP are overlapped
            _VDD2VSSMinHeight1 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS  # Maybe Not seletec
            # 2) calculate by PP and NP layer -> It works, but not a general design. -> Need Very Wide Poly routing and specific width M1
            _VDD2VSSMinHeight2 = DistanceBtwVSS2NMOS \
                                 + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] \
                                 + 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] \
                                 + DistanceBtwVDD2PMOS
            # 3)  two independant poly gates and gap by '_PolygateMinSpace2'
            _VDD2VSSMinHeight3 = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS + WidthOfInputXM1 + _DRCObj._PolygateMinSpace2  # originally spacing to_DRCObj._PolygateMinSpace

            _VDD2VSSMinHeight = max(_VDD2VSSMinHeight1, _VDD2VSSMinHeight2, _VDD2VSSMinHeight3)
        else:
            raise NotImplementedError

        # 4) Determine the total height and Validate it
        if _VDD2VSSHeight == None:
            _VDD2VSSHeight = _VDD2VSSMinHeight
        else:
            if _VDD2VSSHeight < _VDD2VSSMinHeight:
                print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)  # Need to Print More information(input parameter...)
                raise NotImplementedError

        # 5) Setting Coordinates of 'SupplyLines and MOSFETs'
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, DistanceBtwVSS2NMOS]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - DistanceBtwVDD2PMOS)]]

        # 6) Setting Coordinates of 'Output Routing Via (M1V1M2) '
        tmpNMOSOutputRouting = []
        tmpPMOSOutputRouting = []
        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):  # Assumption : same MOSFETs' fingers
            tmpPMOSOutputRouting.append(CoordinateCalc.Add(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i],
                                                           self._DesignParameter['_PMOS']['_XYCoordinates'][0]))
            tmpNMOSOutputRouting.append(CoordinateCalc.Add(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i],
                                                           self._DesignParameter['_NMOS']['_XYCoordinates'][0]))

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting


        #####################################VIA re-Coordinates for Poly Dummy######################################
        # Need to Modify
        if (_Finger == 1) and (DesignParameters._Technology == '028nm'):
            self._DesignParameter['_VIANMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                 self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 +
                 self._DesignParameter['_VIANMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyDummytoGoUp_Finger2]]
            self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_XYCoordinates'] = [
                [XCoordinateOfViaF1,  # self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                 self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 -
                 self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyDummytoGoUp_Finger2]]
        elif (_Finger == 1) and (DesignParameters._Technology == '065nm'):
            raise NotImplementedError
        elif DesignParameters._Technology not in ('028nm', '065nm'):
            raise NotImplementedError
        else:
            pass



        # Poly Boundary Generation MOS Gate -----------------------------------------------------------------------
        '''
        Require : PMOS, NMOS
        '''
        if _Finger != 1:
            _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                               - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                               + _ChannelLength
            _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                               - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] \
                               + _ChannelLength

        elif (_Finger == 1) and (DesignParameters._Technology == '028nm'):
            _LenBtwPMOSGates = self._DesignParameter['_VIAPMOSPoly2Met1_F1']['_XYCoordinates'][0][0] \
                               - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
            _LenBtwNMOSGates = self._DesignParameter['_VIANMOSPoly2Met1_F1']['_XYCoordinates'][0][0] \
                               - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]
        else:
            raise NotImplementedError

        self._DesignParameter['_PolyRouteXOnPMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_PolyRouteXOnNMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'] = _LenBtwPMOSGates
        self._DesignParameter['_PolyRouteXOnNMOS']['_XWidth'] = _LenBtwNMOSGates
        self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # calculated when only one row -> should be changed
        self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        # Additional Poly Routing --------------------------------------------------------------------------------------
        '''
        Function : Route poly layers [ {Input gate poly left - Input gate poly right(row)}, {NMOS gate poly - Input M1 poly(column)}, {PMOS gate poly - Input M1 poly(column)} ]
        Output   : Update self._DesignParameter['_PolyRouteXOn{PMOS, NMOS}'] & self._DesignParameter['_PolyRouteYOn{PMOS, NMOS}'] 
        Require  : NMOS, PMOS (XYCoordinates)
        '''
        # Row Line (Only setting Coordinates)
        if _Finger != 1:
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]
        elif (_Finger == 1) and (DesignParameters._Technology == '028nm'):
            self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + _LenBtwPMOSGates*0.5,
                 self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
            ]

            self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
                [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + _LenBtwPMOSGates*0.5,
                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
            ]
        else:
            raise NotImplementedError

        # Column Line
        self._DesignParameter['_PolyRouteYOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PolyRouteYOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PolyRouteYOnPMOS']['_Width'] = _ChannelLength
        self._DesignParameter['_PolyRouteYOnNMOS']['_Width'] = _ChannelLength

        tmpPolyRouteYOnPMOS = []
        tmpPolyRouteYOnNMOS = []

        for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpPolyRouteYOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]]])
            tmpPolyRouteYOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_PolyRouteYOnPMOS']['_XYCoordinates'] = tmpPolyRouteYOnPMOS
        self._DesignParameter['_PolyRouteYOnNMOS']['_XYCoordinates'] = tmpPolyRouteYOnNMOS


        # VSS & VDD Supply Routing (Metal1) ----------------------------------------------------------------------------
        '''
        Function : Route 'VDD-PMOS(source)' and 'VSS-NMOS(source)' by 'METAL1'
                   (Set the Leftmost Metal of MOSFET as the source)
        Require  : NMOS, PMOS, NbodyContact, PbodyContact (Coordinates)
        '''
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

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting


        # Output Metal (1&2) Boundary & Routing ------------------------------------------------------------------------

        # Output M1 Routing (Column Line)
        tmpOutputRoutingM1Y = []

        for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) / 2):
            tmpOutputRoutingM1Y.append([CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                           self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i]),
                                        CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                           self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i])
                                        ])  #

        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case (6, 10, 14, 18, ...)
            del tmpOutputRoutingM1Y[-1]
            tmpOutputRoutingM1Y.append(
                [CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                    self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1]),
                 CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                    self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])])
        else:
            pass

        self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRoutingM1Y

        # Output M2 Routing (Row Line)
        self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
                                                                      self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]],
                                                                     [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],
                                                                      self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]]],
                                                                    [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],
                                                                      self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]],
                                                                     [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0],
                                                                      self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]
                                                                    ]


        # Input Contact (Poly to M1)------------------------------------------------------------------------------------
        '''
        Function : Make Contact(Poly to M1) for _PolyRouteXOn{}
                   2 kind of calculation
                   (1) surrounded by output metal(left and right)   if _Finger > 4
                   (2) rightmost 
        Require : OutputRouting, _PolyRouteXOn{NMOS PMOS}, PMOS, NMOS
        
        '''
        # (1) surrounded by output metal  /  of Input Contact (Poly to M1)
        if _Finger > 3:             # No Need else statement (when finger is 1, 2, 3, it covers on (2))
            # Calculate Number of Contact_X 'tmpNumCOX'
            lengthM1BtwOutputRouting = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_Width'] \
                                       - 2 * _DRCObj._Metal1MinSpaceAtCorner

            unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
            tmpNumCOX = int((lengthM1BtwOutputRouting - _DRCObj._CoMinWidth - 2*_DRCObj._Metal1MinEnclosureCO2) // unitLengthBtwCOX) + 1

            # NMOS & PMOS
            _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)

            tmpInputPCCOM1onNMOS = []
            tmpInputPCCOM1onPMOS = []

            for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
                tmpInputPCCOM1onNMOS.append([self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][2*i + 1][0],
                                             self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]])
                tmpInputPCCOM1onPMOS.append([self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][2*i + 1][0],
                                             self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]])

            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onNMOS
            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onPMOS

            # exception case
            if (_Finger % 4 == 2) and (_Finger != 2):
                del self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][-1]
                del self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][-1]


        ## (2) rightmost output metal  /  of Input Contact (Poly to M1)
        if (_Finger % 4 == 2) and (_Finger != 2):  # exception case
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-2][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                - 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                - _DRCObj._Metal1MinSpaceAtCorner
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2                # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._Metal1MinEnclosureCO2              # Calculate by M1-CO
        elif _Finger != 1:
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightPOBoundary = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] \
                                 + 0.5 * _ChannelLength
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2                # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightPOBoundary - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO-CO
        elif (_Finger == 1) and (DesignParameters._Technology == '028nm'):
            tmpLeftCoBoundary = 0
            tmpRightCoBoundary = 0
        else:
            raise NotImplementedError

        NumCoRightMost = int((tmpRightCoBoundary - tmpLeftCoBoundary - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        if NumCoRightMost > 0:
            _VIAMOSPoly2Met1RightMost = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOX'] = NumCoRightMost
            _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAMOSPoly2Met1RightMost'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1RightMostOnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1RightMost)
            self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'] = [
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary)/2,MinSnapSpacing), self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]],
                [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary)/2,MinSnapSpacing), self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]]
            ]  # both NMOS & PMOS

        if '_VIAPMOSPoly2Met1_F1' in self._DesignParameter:
            self._DesignParameter['_VIANMOSPoly2Met1'] = self._DesignParameter['_VIANMOSPoly2Met1_F1']
            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._DesignParameter['_VIAPMOSPoly2Met1_F1']
            del self._DesignParameter['_VIANMOSPoly2Met1_F1']
            del self._DesignParameter['_VIAPMOSPoly2Met1_F1']


        # Input Met1 Routing -------------------------------------------------------------------------------------------
        '''
        When there is a gap between (routed) poly gates, route them by Met1 (column line)
        Strategy : Route Input M1 on the same YCoordinates as the SupplyRouting M1
                   (Supply M1 outside the poly gate route is ignored)
        '''
        tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]

        if '_VIANMOSPoly2Met1' in self._DesignParameter:
            for i in range(0, len(self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'])):
                tmpInputRouting.append([self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][i],
                                        self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i]])
        if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
            tmpInputRouting.append(self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'])

        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting


        ################################################################################################################
        # # Input M1 Route up tp M2
        if DesignParameters._Technology in ('028nm', '065nm'):
            # count input M1 segement
            tmpCount_GateViaLayer = 0

            if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
                tmpCount_GateViaLayer += 1
                flag_exception_rightmost = True
            else:
                flag_exception_rightmost = False
            if '_VIAPMOSPoly2Met1' in self._DesignParameter:
                tmpCount_GateViaLayer += len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])

            if (DesignParameters._Technology == '028nm') and (tmpCount_GateViaLayer > 1) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
                # M1V1M2
                # (1) Normal width
                _LengthM1_VIAPMOSPoly2Met1 = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                _NumViaInputM12 = int((_LengthM1_VIAPMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2*_DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)

                # (2) RightMost
                if flag_exception_rightmost:
                    _LengthM1_VIAPMOSPoly2Met1_RightMost = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                    _NumViaInputM12_RightMost = int((_LengthM1_VIAPMOSPoly2Met1_RightMost - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                                    // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                    _ViaMet12Met2forInput2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12_RightMost
                    _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOY'] = 1
                    self._DesignParameter['_ViaMet12Met2forInput2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInput2In{}'.format(_Name)))[0]
                    self._DesignParameter['_ViaMet12Met2forInput2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput2)


                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i][0],
                                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs
                del tmpXYs

                if flag_exception_rightmost:
                    self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'] = \
                        [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'][0][0],
                          self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]]]

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                                                                                 self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]]
                if flag_exception_rightmost:
                    self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
                        [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                         self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'][0]]]

            elif (DesignParameters._Technology in ('028nm', '065nm')) and (tmpCount_GateViaLayer > 1):
                # M1V1M2
                # (1) Normal width
                _LengthM1Y_VIAMOSPoly2Met1 = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                                              + abs(self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1]-self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1])
                _NumViaInputM12 = int((_LengthM1Y_VIAMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2*_DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
                                      // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

                _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 1
                _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = _NumViaInputM12 if _NumViaInputM12 < 3 else 3
                self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2forInput)

                tmpXYs = []
                for i in range(0, len(self._DesignParameter['_InputRouting']['_XYCoordinates'])):
                    tmpXYs.append([self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][0],
                                   (self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][1]+self._DesignParameter['_InputRouting']['_XYCoordinates'][i][1][1])/2 ])
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs

                self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
                self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._MetalxMinWidth
                self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
                                                                                 self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]]


        # end of 'if _VDD2VSSHeight == _VDD2VSSMinHeight:'




        # exception case... Need to Modify later
        _DRC_Metal1MinimumArea = 10000
        _DRC_M1MinWidth_WhenCalcMinArea = 130

        if (_Finger == 1) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
            tmpX = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            tmpY = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if (tmpX * tmpY) < _DRC_Metal1MinimumArea:
                tmpY_calc = _DRC_Metal1MinimumArea / tmpX
                if tmpY_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE
                    tmpY_calc = _DRC_M1MinWidth_WhenCalcMinArea

                self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = tmpY_calc

        elif (_Finger == 2) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
            tmpX = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            tmpY = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if (tmpX * tmpY) < _DRC_Metal1MinimumArea:
                tmpX_calc = _DRC_Metal1MinimumArea / tmpY
                if tmpX_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE
                    tmpX_calc = _DRC_M1MinWidth_WhenCalcMinArea
                self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = tmpX_calc
                self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] = \
                    self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] \
                    + tmpX_calc/2 - tmpX/2


        ''' ---------------------------------------- PP/NP Additional Layer ---------------------------------------- '''
        if DesignParameters._Technology == '028nm':
            pass
        elif DesignParameters._Technology == '065nm':
            Ybot_PolyRouteXOnPMOS = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - 0.5 * self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']
            Ytop_PolyRouteXOnNMOS = self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + 0.5 * self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth']

            # case 1) Enlarge each PP/NP Layers
            if abs(Ybot_PolyRouteXOnPMOS - Ytop_PolyRouteXOnNMOS) >= 2*_DRCObj._PpMinEnclosureOfPo:
                self._DesignParameter['_PIMPforGatePoly'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1])
                self._DesignParameter['_NIMPforGatePoly'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1])

                self._DesignParameter['_PIMPforGatePoly']['_XYCoordinates'] = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates']
                self._DesignParameter['_PIMPforGatePoly']['_XWidth'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_PIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
                self._DesignParameter['_NIMPforGatePoly']['_YWidth'] = self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo

            # case 2) Fill the gap between PP&NP Layer with only NP Layer
            else:
                Ybot_PPLayerOnPMOS = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
                Ytop_NPLayerOnNMOS = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 0.5 * self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']

                self._DesignParameter['_NIMPforGatePoly'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1])
                self._DesignParameter['_NIMPforGatePoly']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
                self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = [[[self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ybot_PPLayerOnPMOS],
                                                                                [self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ytop_NPLayerOnNMOS]]]
        else:
            raise NotImplementedError


        ''' --------------------------------- NWELL & XVT Generation & Coordinates --------------------------------- '''
        '''
        Function    : Generate NWELL by PathElementDeclaration (column line)
        Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        '''
        tempDRC_NwMinEnclosurePONotDummy = 167  # GR270
        tempDRC_NwMinEnclosurePactive2 = 112  # GR260a
        _SupplyRailYWidth = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']
        XWidth1_NWLayer = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive
        XWidth2_NWLayer = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * tempDRC_NwMinEnclosurePactive2
        XWidth3_NWLayer = abs(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) \
                          + _ChannelLength + 2 * tempDRC_NwMinEnclosurePONotDummy

        XWidth_NWLayer = max(XWidth1_NWLayer, XWidth2_NWLayer, XWidth3_NWLayer)  # Need to Modify for 65nm

        XYCoordinatesOfNW_top = CoordinateCalc.Add(self._DesignParameter['NbodyContact']['_XYCoordinates'][0],
                                                   [0, _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive])
        XYCoordinatesOfNW_bot = CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                   [0, - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2 - _DRCObj._NwMinEnclosurePactive])

        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        self._DesignParameter['_NWLayer']['_Width'] = XWidth_NWLayer
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]]


        if (DesignParameters._Technology == '028nm') and (_XVT != None):   # Need to check
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
            _XVTLayer = '_' + _XVT + 'Layer'

            # self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive,
            #                                                   self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX,
            #                                                   self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT)
            # self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
            #                                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive],
            #                                                         [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
            #                                                          self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]
            #                                                         ]]

            if _VDD2VSSHeight == _VDD2VSSMinHeight:  # why use this condition?
                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1])
                self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']
                self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                                                          (self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]) / 2]]

            elif (_VDD2VSSHeight != _VDD2VSSMinHeight) and (_StandAlone_DRCFREE == True):   # Need to Modify : Should check by another way (XVT's area)
                xvtY_calc = math.ceil(_DRCObj._XvtMinArea2 / self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']) + 1

                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1])
                self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']
                self._DesignParameter[_XVTLayer]['_YWidth'] = xvtY_calc
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                                                          (self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + xvtY_calc * 0.5 - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']*0.5)]]

                xvtPMOS_bot = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth'] / 2
                xvtNMOS_top = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth'] / 2 + xvtY_calc

                if (xvtPMOS_bot - xvtNMOS_top) < _DRCObj._XvtMinSpace:
                    self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']
                    self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]
                    self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [
                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                         (self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]) / 2]]


        # Pin Generation & Coordinates ---------------------------------------------------------------------------------
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.05, _Angle=0, _TEXT='VIN')
        self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.05, _Angle=0, _TEXT='VOUT')

        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2),
                                                                 round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]]
        self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2),
                                                                  round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1]) / 2)]]

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

    _Finger = 6
    _ChannelWidth = 200
    _ChannelLength = 30
    _NPRatio = 2
    _Dummy = True
    _XVT = 'HVT'

    _VDD2VSSHeight = None  # None / 1750
    _NumSupplyCOX = 8  # None
    _NumSupplyCOY = 1

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
    _SupplyLine = False
    _StandAlone_DRCFREE = True

    _fileName = 'Inverter.gds'
    libname = 'TEST_INV1'

    # Generate Inverter Layout Object
    print ('Technology Process', DesignParameters._Technology)
    InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter')
    InverterObj._CalculateDesignParameter(_NPRatio=_NPRatio, _Dummy=_Dummy, _XVT=_XVT, _Finger=_Finger,
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
                                          _StandAlone_DRCFREE=_StandAlone_DRCFREE
                                          )
    InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=InverterObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)

    FileManage.Upload2FTP(
        server=My.server,
        user=My.ID,
        password=My.PW,
        directory=My.Dir_GDS,
        filename=_fileName
    )

    FileManage.StreamIn(
        server=My.server,
        port=22,
        ID=My.ID,
        PW=My.PW,
        Dir_Work=My.Dir_Work,
        Dir_GDS=My.Dir_GDS,
        libname=libname,
        filename=_fileName,
        tech=DesignParameters._Technology
    )

    print ('###############      Finished      ##################')
    # end of 'main():' ---------------------------------------------------------------------------------------------

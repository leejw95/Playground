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

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_Reflect=[1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)

        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'] \
            = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']

        del NMOSparameters

        # _PMOS Generation ---------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_SLVT'] = _SLVT

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)

        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'] \
            = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']

        del PMOSparameters

        # VDD Generation -----------------------------------------------------------------------------------------------
        '''
        Need : PMOS(for NbodyContact), NMOS(for PbodyContact)
        Input : _NumSupplyCoX     (optional, default 2)
                _NumSupplyCoY     (optional, default 1)
                _SupplyMet1XWidth (optional)
                _SupplyMet1YWidth (optional)
        '''
        if _NumSupplyCoX == None:
            XWidthOfPMOS = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            NumSupplyCoXOnVDDVSS = int(XWidthOfPMOS // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        else:
            NumSupplyCoXOnVDDVSS = _NumSupplyCoX

        NbodyParameters = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters['_NumberOfNbodyCOX'] = NumSupplyCoXOnVDDVSS if (NumSupplyCoXOnVDDVSS > 2) else 2
        NbodyParameters['_NumberOfNbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        NbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        NbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)

        del NbodyParameters
        del XWidthOfPMOS


        # VSS Generation -----------------------------------------------------------------------------------------------
        PbodyParameters = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        PbodyParameters['_NumberOfPbodyCOX'] = NumSupplyCoXOnVDDVSS if (NumSupplyCoXOnVDDVSS > 2) else 2
        PbodyParameters['_NumberOfPbodyCOY'] = _NumSupplyCoY if (_NumSupplyCoY != None) else 1
        PbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        PbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**PbodyParameters)

        del PbodyParameters
        del NumSupplyCoXOnVDDVSS

        # VIA Generation for PMOS Output -------------------------------------------------------------------------------
        '''
        Need : PMOS, NMOS
        Input : _NumViaPMOSMet12Met2CoX (optional)
                _NumViaPMOSMet12Met2CoY (optional)    
        '''
        if _NumViaPMOSMet12Met2CoY == None:
            YWidthOfPMOSMet1 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYPMOS = int(YWidthOfPMOSMet1 // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        else:
            NumViaYPMOS = _NumViaPMOSMet12Met2CoY

        VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaPMOSMet12Met2CoX if (_NumViaPMOSMet12Met2CoX != None) else 1
        VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIAPMOSMet12)

        del VIAPMOSMet12
        del YWidthOfPMOSMet1
        del NumViaYPMOS

        # VIA Generation for NMOS Output -------------------------------------------------------------------------------
        if _NumViaNMOSMet12Met2CoY == None:
            YWidthOfNMOSMet1 = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            NumViaYNMOS = int(YWidthOfNMOSMet1 // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        else:
            NumViaYNMOS = _NumViaNMOSMet12Met2CoY

        VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumViaNMOSMet12Met2CoX if (_NumViaNMOSMet12Met2CoX != None) else 1
        VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

        self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**VIANMOSMet12)

        del VIANMOSMet12
        del NumViaYNMOS

        # Poly Boundary Generation for PMOS Gate -----------------------------------------------------------------------
        '''
        Require : PMOS, NMOS
        '''
        _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                           + _ChannelLength

        self._DesignParameter['_PolyRouteXOnPMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'] = _LenBtwPMOSGates
        self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        # Poly Boundary Generation for NMOS Gate -----------------------------------------------------------------------

        _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
                           - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] \
                           + _ChannelLength

        self._DesignParameter['_PolyRouteXOnNMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_PolyRouteXOnNMOS']['_XWidth'] = _LenBtwPMOSGates
        self._DesignParameter['_PolyRouteXOnNMOS']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide


        # Coordinates setting ------------------------------------------------------------------------------------------
        WidthOfInputXM1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2  # how?? you have to choose

        DistanceBtwVSS2NMOS = 0.5 * self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
                             + 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                         self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                             + _DRCObj._Metal1MinSpace3  # need to check, ambiguous

        DistanceBtwVDD2PMOS = 0.5 * self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] \
                             + 0.5 * max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'],
                                         self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                             + _DRCObj._OdMinSpace  # need to check, ambiguous

        DistanceBtwNMOS2PolyInput = 0.5 * max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                              self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                    + 0.5 * WidthOfInputXM1 \
                                    + _DRCObj._Metal1MinSpaceAtCorner     # 50: for test...

        DistanceBtwPMOS2PolyInput = 0.5 * max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                              self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) \
                                    + 0.5 * WidthOfInputXM1 \
                                    + _DRCObj._Metal1MinSpaceAtCorner       # 50: for test... max(_DRCObj._Metal1MinWidth,50)

        # Calculate Minimum Height of VDD to VSS
        if _Finger != 1:
            _VDD2VSSMinHeight = DistanceBtwVSS2NMOS + DistanceBtwNMOS2PolyInput \
                                + DistanceBtwPMOS2PolyInput + DistanceBtwVDD2PMOS
        else:
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth

            _LengthBtwPolyDummyEdge2PolyEdge = (_LengthBtwPoly2Poly * (_Finger / 2 + 0.5) - _ChannelLength / 2) \
                                               - self._DesignParameter['_PolyRouteXOnNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2

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

        # Setting Coordinates of SupplyLines, MOSFETs
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, DistanceBtwVSS2NMOS]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - DistanceBtwVDD2PMOS)]]

        # Output Routing Via (M1V1M2) Coordinates Setting
        '''
        Description : Setting XYCoordinates of '_ViaMet12Met2On{}Output' Object
        Require : PMOS, NMOS (XYCoordinates) and '_ViaMet12Met2On{}Output' Object
        '''
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

        del tmpPMOSOutputRouting
        del tmpNMOSOutputRouting



        # Additional Poly Routing --------------------------------------------------------------------------------------
        '''
        Function : Route poly layers [ {Input gate poly left - Input gate poly right(row)}, {NMOS gate poly - Input M1 poly(column)}, {PMOS gate poly - Input M1 poly(column)} ]
        Output   : Update self._DesignParameter['_PolyRouteYOn{}'] PMOS, NMOS
        Require  : NMOS, PMOS (XYCoordinates)
        '''
        # Row Line (Only setting Coordinates)
        self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'] = [
            [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
             self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + DistanceBtwNMOS2PolyInput]
        ]

        self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'] = [
            [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
             self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - DistanceBtwPMOS2PolyInput]
        ]

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
                                         self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - _DRCObj._PolygateMinWidth]])
            tmpPolyRouteYOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + _DRCObj._PolygateMinWidth]])

        self._DesignParameter['_PolyRouteYOnPMOS']['_XYCoordinates'] = tmpPolyRouteYOnPMOS
        self._DesignParameter['_PolyRouteYOnNMOS']['_XYCoordinates'] = tmpPolyRouteYOnNMOS

        del tmpPolyRouteYOnPMOS
        del tmpPolyRouteYOnNMOS


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

        del tmpNMOSSupplyRouting
        del tmpPMOSSupplyRouting

        # Output Metal (1&2) Boundary & Routing ------------------------------------------------------------------------

        # Output M1 Routing (Column Line)
        tmpOutputRoutingM1Y = []

        if _Finger == 3:  # exception case
            tmpOutputRoutingM1Y.append([CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                           self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][1]),
                                        CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                           self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][1])
                                        ])
        else:
            for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) / 2):
                tmpOutputRoutingM1Y.append([CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                               self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2 * i]),
                                            CoordinateCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
                                                               self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2 * i])
                                            ])

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
        if _Finger > 4:
            # Calculate Number of Contact_X 'tmpNumCOX'
            lengthM1BtwOutputRouting = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
                                       - self._DesignParameter['_OutputRouting']['_Width'] \
                                       - 2 * _DRCObj._Metal1MinSpaceAtCorner

            unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
            tmpNumCOX = int((lengthM1BtwOutputRouting - _DRCObj._CoMinWidth - 2*_DRCObj._Metal1MinEnclosureCO2) // unitLengthBtwCOX) + 1

            # NMOS
            _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)

            tmpInputPCCOM1 = []

            for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
                tmpInputPCCOM1.append([self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][2*i + 1][0],
                                       self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]])

            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1
            # self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 50  # for test

            # PMOS
            _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)

            tmpInputPCCOM1onPMOS = []

            for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
                tmpInputPCCOM1onPMOS.append([self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][2*i + 1][0],
                                             self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]])

            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onPMOS
            # self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 50  # for test

            del unitLengthBtwCOX
            del tmpNumCOX
            del _VIANMOSPoly2Met1
            del tmpInputPCCOM1
            del tmpInputPCCOM1onPMOS

        ## (2) rightmost output metal  /  of Input Contact (Poly to M1)
        if _Finger == 3:
            tmpRightM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                 - 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                 - _DRCObj._Metal1MinSpaceAtCorner
            tmpLeftPolyBoundary = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] \
                                  - 0.5 * _ChannelLength
            tmpLeftCoBoundary = tmpLeftPolyBoundary + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO-CO
            tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._Metal1MinEnclosureCO   # Calculate by M1 - CO
        else:
            tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
                                + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
                                + _DRCObj._Metal1MinSpaceAtCorner
            tmpRightM1Boundary = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] \
                                  + 0.5 * _ChannelLength
            tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO  # Calculate by M1-CO
            tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO - CO

        NumCoRightMost = int((tmpRightCoBoundary - tmpLeftCoBoundary - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        if NumCoRightMost > 0:
            _VIANMOSPoly2Met1RightMost = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)

            _VIANMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOX'] = NumCoRightMost
            _VIANMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1RightMost'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1RightMostOnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1RightMost']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1RightMost)
            self._DesignParameter['_VIANMOSPoly2Met1RightMost']['_XYCoordinates'] = [[(tmpLeftCoBoundary+tmpRightCoBoundary)/2,
                                                                                     self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]],
                                                                                     [(tmpLeftCoBoundary + tmpRightCoBoundary)/2,
                                                                                      self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]]
                                                                                     ]  # both NMOS & PMOS
            # self._DesignParameter['_VIANMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 50  # for test








        ##
        # else:
        #     pass  # Not yet Implemented









        # # # Input M1 Route up tp M2 or M3 -> pass, later
        if _VDD2VSSHeight == _VDD2VSSMinHeight:
            if _Finger == 3:
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
                tmpYCoordinate = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = [[tmpXCoordinate, tmpYCoordinate]]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = \
                    self._DesignParameter['_PolyRouteXOnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            elif _Finger == 4:
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
                tmpYCoordinate = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]
                self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = [[tmpXCoordinate, tmpYCoordinate]]
                self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = \
                    self._DesignParameter['_PolyRouteXOnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            elif _Finger > 4:  #
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
                                self._DesignParameter['PolyRouteXOnNMOS']['_XYCoordinates'][0][1]])
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
                                self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]])
                self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'] = tmp
                del tmp

                self._DesignParameter['_CLKMet3InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
                self._DesignParameter['_CLKMet3InRouting']['_Width'] = self._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_CLKMet3InRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0],
                                                                                 self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][-1]]]
            # Need when finger == (1,2)
        # end of 'if _VDD2VSSHeight == _VDD2VSSMinHeight:'

        # Input Met1 Routing -------------------------------------------------------------------------------------------
        # -> Modify that after Input Contact ???
        '''
        When there is a gap between (routed) poly gates, route them by Met1 (column line)
        Strategy : Route Input M1 on the same YCoordinates as the SupplyRouting M1
                   (Supply M1 outside the poly gate route is ignored)
        '''
        tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]

        # exception case..?
        if _Finger in (1, 2, 3):
            tmpInputRouting = [[[0, self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]],
                                [0, self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]]]]
        else:
            if _Finger % 2 == 0:  # Even Finger
                range_InputRoutingM1 = range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1)
            else:                 # Odd Finger
                range_InputRoutingM1 = range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']))

            for i in range_InputRoutingM1:
                tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1]],
                                        [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                         self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting

        del tmpInputRouting

        # NWELL & SLVT Generation & Coordinates ------------------------------------------------------------------------
        '''
        Function    : Generate NWELL by PathElementDeclaration (column line)
        Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        '''

        _SupplyRailYWidth = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']

        NWLayerXWidth = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive,
                            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX)

        XYCoordinatesOfNW_top = CoordinateCalc.Add(self._DesignParameter['NbodyContact']['_XYCoordinates'][0],
                                                   [0, _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive])
        XYCoordinatesOfNW_bot = CoordinateCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
                                                   [0, - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2])

        ''' Prev. Design
        XYCoordinatesOfNW_top = [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0],
                                 self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive]
        XYCoordinatesOfNW_bot = [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                 self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2] # why use this condition?
        '''
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        self._DesignParameter['_NWLayer']['_Width'] = NWLayerXWidth
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]

        if _SLVT == True:   # Need to check
            self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive,
                                                              self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX,
                                                              self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT)
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                     self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYWidth / 2 + _DRCObj._NwMinEnclosurePactive],
                                                                    [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                     self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]
                                                                    ]]

            if _VDD2VSSHeight == _VDD2VSSMinHeight:  # why use this condition?
                self._DesignParameter['_SLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1])
                self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']
                self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]
                self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
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
    # User-Defined Parameters
    _Finger = 18
    _ChannelWidth = 200
    _ChannelLength = 30
    _NPRatio = 2
    _VDD2VSSHeight = 2000   # None / 2000
    _Dummy = True
    _SLVT = True
    _LVT = False
    _HVT = False
    _NumSupplyCOX = None  #
    _NumSupplyCOY = 2
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
    _fileName = 'Inverter0802.gds'                                    # Need to get current date / time
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')
    FileManage.Upload2FTP(_fileName=_fileName)

    print ('###############      Finished      ##################')  # Need to get project name(inverter_iksu2.py)

# end of 'main():' ---------------------------------------------------------------------------------------------

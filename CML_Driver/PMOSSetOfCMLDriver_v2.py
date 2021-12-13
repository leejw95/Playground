import math
import copy

#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from SthPack import CoordCalc, BoundaryCalc

#
import PMOSWithDummy_iksu
import NbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import psubring


class PMOSSetOfCMLDriver(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None, _NumFingerOfInputPair=None,
                                           _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None, _NumFingerOfCurrentSource=None,
                                           _WidthOfMiddleRoutingIP=None, _WidthOfMiddleRoutingCS=None, _XVT=None,
                                           _NumCoYOfNbodybtwIPandCS=None, _YWidthOfNbodybtwIPandCS=None,
                                           _SubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[]),

                POHforIP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                POVforIP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                M1forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                M2forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M1VforIP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                M2HforIPSource=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[]),
                M2HforIPDrain=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[]),

                POHforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                POVforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                M1forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                M2forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M1VforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                M2HforCSSource=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M2HforCSDrain=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),

                M2HforCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3HforCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M2VforCS2IP=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[]),
                M3VforCS2IP=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[]),

                M2VForCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                             _XYCoordinates=[]),
                M3VForCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                             _XYCoordinates=[]),

                M2ForNbody=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                             _XYCoordinates=[]),



                M1forNbodyExtention=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                ODforNbodyExtention=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[]),
                M1forCSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                _NWLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[]),
                _Met1BoundaryOfSubring=dict(_DesignParametertype=7, _XWidth=None, _YWidth=None, _XYCoordinates=[]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateInputPair_v2(self,
                               _FingerWidthOfInputPair=None,
                               _FingerLengthOfInputPair=None,
                               _NumFingerOfInputPair=None,
                               _WidthOfMiddleRoutingIP=None,
                               _XVT=None):
        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        ''' check # of all fingers '''
        assert _NumFingerOfInputPair % 2 == 0
        NumFingerOfIP = _NumFingerOfInputPair // 2

        ''' ------------------------------------- PMOS Generation -------------------------------------------------- '''
        PMOSParam_InputPair = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSParam_InputPair['_PMOSNumberofGate'] = NumFingerOfIP
        PMOSParam_InputPair['_PMOSChannelWidth'] = _FingerWidthOfInputPair
        PMOSParam_InputPair['_PMOSChannellength'] = _FingerLengthOfInputPair
        PMOSParam_InputPair['_PMOSDummy'] = True
        PMOSParam_InputPair['_XVT'] = _XVT
        # PMOSParam_InputPair['_DistanceBtwFinger'] = 130

        self._DesignParameter['PMOS_IP'] = self._SrefElementDeclaration(
            _DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS_IP']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_InputPair)

        DistanceBtwGateOfIP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']

        ''' PP and XVT Layer btw Input Pair '''
        self._DesignParameter['_PPLayer']['_YWidth'] = self.getYWidth('PMOS_IP', '_PPLayer')
        self._DesignParameter['_PPLayer']['_XWidth'] = self.getXWidth('PMOS_IP', '_PPLayer') - (NumFingerOfIP + 2) * DistanceBtwGateOfIP

        if DesignParameters._Technology == '028nm':
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
            _XVTLayer = '_' + _XVT + 'Layer'
            self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1], _XYCoordinates=[[0, 0]])
            self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']
            self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] \
                                                          - (NumFingerOfIP + 2) * DistanceBtwGateOfIP
        else:
            raise NotImplementedError


        ''' ----------------------- Poly for PMOS Input Pair Middle Routing ----------------------------------- '''
        self._DesignParameter['POHforIP']['_XWidth'] = DistanceBtwGateOfIP * (NumFingerOfIP-1) + _FingerLengthOfInputPair
        self._DesignParameter['POHforIP']['_YWidth'] = _WidthOfMiddleRoutingIP


        ''' ------------------------------------- Coordinates setting ---------------------------------------------- '''
        DistanceXBtwIP2Origin = (NumFingerOfIP / 2.0 + 1) * DistanceBtwGateOfIP
        DistanceYBtwMidRouting2IP1 = .5 * (self.getYWidth('PMOS_IP', '_Met1Layer') + self.getYWidth('POHforIP')) \
                                     + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify
        DistanceYBtwMidRouting2IP2 = .5 * (self.getYWidth('PMOS_IP', '_Met1Layer') + self.getYWidth('POHforIP')) \
                                     + _DRCObj._VIAxMinSpaceFor3neighboring  # Distance between Source/Drain's Via - to - PolyGate Metal's Via (for worst enclosure condition)
        DistanceYBtwMidRouting2IP = max(DistanceYBtwMidRouting2IP1, DistanceYBtwMidRouting2IP2)

        XYs_PMright = [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                       [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]
        XYs_PMleft = [[-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                      [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]

        self._DesignParameter['PMOS_IP']['_XYCoordinates'] = XYs_PMright + XYs_PMleft
        self._DesignParameter['POHforIP']['_XYCoordinates'] = [[+DistanceXBtwIP2Origin, 0],
                                                               [-DistanceXBtwIP2Origin, 0]]
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[0, +DistanceYBtwMidRouting2IP],
                                                               [0, -DistanceYBtwMidRouting2IP]]
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self.getXY('_PPLayer')


        ''' -------------------------------------- Vertical PolyGate ----------------------------------------------- '''
        self._DesignParameter['POVforIP']['_XWidth'] = _FingerLengthOfInputPair
        self._DesignParameter['POVforIP']['_YWidth'] = 2 * DistanceYBtwMidRouting2IP - self.getYWidth('PMOS_IP', '_POLayer')

        for XYs_PO1 in self.getXY('POHforIP'):
            for XYs_PO2 in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']:
                self._DesignParameter['POVforIP']['_XYCoordinates'].append(CoordCalc.Add(XYs_PO1, XYs_PO2))


        ''' ----------------------------------- Text for PMOS_IP source/drain -------------------------------------- '''
        self._DesignParameter['PMOS_IP_Source'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='S', _XYCoordinates=[])
        for XYs_PMOS in XYs_PMright:
            for XYs_Source in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']:
                self._DesignParameter['PMOS_IP_Source']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Source))
        for XYs_PMOS in XYs_PMleft:
            for XYs_Source in CoordCalc.FlipXs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']):
                self._DesignParameter['PMOS_IP_Source']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Source))

        self._DesignParameter['PMOS_IP_Drain'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='D', _XYCoordinates=[])
        for XYs_PMOS in XYs_PMright:
            for XYs_Drain in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']:
                self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Drain))
        for XYs_PMOS in XYs_PMleft:
            for XYs_Drain in CoordCalc.FlipXs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']):
                self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Drain))


        ''' ------------------------------------- M1V1M2 for IP Source/Drain ------------------------------------------------ '''
        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = 1
        Via1Params['_ViaMet12Met2NumberOfCOY'] = 2
        self._DesignParameter['M1V1M2OnPMOSIP'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2forIP_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['M1V1M2OnPMOSIP']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)

        DistanceYBtwM2H = self.getYWidth('M1V1M2OnPMOSIP', '_Met2Layer') + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width

        tmpXYs = []
        for XYs in self.getXY('PMOS_IP_Source'):
            tmpXYs.append(CoordCalc.Add(XYs, [0, +DistanceYBtwM2H / 2]))
        for XYs in self.getXY('PMOS_IP_Drain'):
            tmpXYs.append(CoordCalc.Add(XYs, [0, -DistanceYBtwM2H / 2]))
        self._DesignParameter['M1V1M2OnPMOSIP']['_XYCoordinates'] = tmpXYs


        ''' ----------------------------- horizontal routing M2 for PMOS_IP Source/Drain -------------------------------- '''
        self._DesignParameter['M2HforIPSource']['_XWidth'] = \
            CoordCalc.MinMaxXY(self.getXY('M1V1M2OnPMOSIP'))[2] \
            - CoordCalc.MinMaxXY(self.getXY('M1V1M2OnPMOSIP'))[0] \
            + self.getXWidth('M1V1M2OnPMOSIP', '_Met2Layer')
        self._DesignParameter['M2HforIPSource']['_YWidth'] = self.getYWidth('M1V1M2OnPMOSIP', '_Met2Layer')
        self._DesignParameter['M2HforIPDrain']['_XWidth'] = \
            abs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
            + self.getXWidth('M1V1M2OnPMOSIP', '_Met2Layer')
        self._DesignParameter['M2HforIPDrain']['_YWidth'] = self.getYWidth('M1V1M2OnPMOSIP', '_Met2Layer')

        self._DesignParameter['M2HforIPSource']['_XYCoordinates'] = [
            [0, -DistanceYBtwMidRouting2IP + DistanceYBtwM2H / 2],
            [0, +DistanceYBtwMidRouting2IP + DistanceYBtwM2H / 2]
        ]
        self._DesignParameter['M2HforIPDrain']['_XYCoordinates'] = [
            [+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - DistanceYBtwM2H / 2],
            [-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - DistanceYBtwM2H / 2],
            [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP - DistanceYBtwM2H / 2],
            [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP - DistanceYBtwM2H / 2]
        ]

        ''' ---------------------- M1V Routing -------------------- '''
        step_M1VRouting = 8  # input parameter
        xlist_SD = []
        for XY in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']:
            xlist_SD.append(XY[0])
        xlist_SD.sort(reverse=True)

        tmpXYs = []
        for i in range(0, len(xlist_SD)):
            if (i // step_M1VRouting) % 2 == 0:
                tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[i], 0],
                               [-DistanceXBtwIP2Origin - xlist_SD[i], 0]])
        self._DesignParameter['M1VforIP']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1VforIP']['_XWidth'] = self.getXWidth('M1V1M2OnPMOSIP', '_Met1Layer')
        self._DesignParameter['M1VforIP']['_YWidth'] = DistanceYBtwMidRouting2IP * 2 + self.getYWidth('PMOS_IP', '_Met1Layer')


        ''' ------------------- M1V1M2, M2V2M3 on PMOSIP Gate(poly) Generate & Place ------------------------------- '''
        NumViaSetOnGate = math.trunc(NumFingerOfIP / float(step_M1VRouting * 2))
        assert NumViaSetOnGate >= 1, f'M1V1M2OnPMOSIPGate Generation Failed. - should have more fingers.' \
                                     f'NumFingerOfIP = {NumFingerOfIP}, ' \
                                     f'step_M1VRouting = {step_M1VRouting},' \
                                     f'-> NumViaSetOnGate = {NumViaSetOnGate}'
        tmpXYs = []
        for i in range(0, NumViaSetOnGate):
            tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[0] - ((step_M1VRouting - 1) / 2.0 + step_M1VRouting) * (xlist_SD[0] - xlist_SD[1]) - (2 * i * step_M1VRouting) * (xlist_SD[0] - xlist_SD[1]), 0],
                           [-DistanceXBtwIP2Origin - xlist_SD[0] + ((step_M1VRouting - 1) / 2.0 + step_M1VRouting) * (xlist_SD[0] - xlist_SD[1]) + (2 * i * step_M1VRouting) * (xlist_SD[0] - xlist_SD[1]), 0]])
        self._DesignParameter['M1forIPGate']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1forIPGate']['_XWidth'] = (step_M1VRouting - 2) * (xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfInputPair
        self._DesignParameter['M1forIPGate']['_YWidth'] = self.getYWidth('POHforIP')

        NumViaXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=self.getXWidth('M1forIPGate'), _YWidth=self.getYWidth('M1forIPGate'))
        assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, 'M1V1M2OnPMOSIPGate Generation Failed.'

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['PolyContactOnPMOSIPGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPMOSIPGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        self._DesignParameter['PolyContactOnPMOSIPGate']['_XYCoordinates'] = self.getXY('M1forIPGate')

        # ) M2
        YWidthOfIPGate = self.getYWidth('M1forIPGate')
        self._DesignParameter['M2forIPGate']['_XWidth'] = self.getXWidth('M1forIPGate')
        self._DesignParameter['M2forIPGate']['_YWidth'] = YWidthOfIPGate
        self._DesignParameter['M2forIPGate']['_XYCoordinates'] = self.getXY('M1forIPGate')

        # ) M1V1M2
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=self.getXWidth('M1forIPGate'), _YWidth=self.getYWidth('M1forIPGate'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPMOSIPGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**ViaParams)
        self._DesignParameter['M1V1M2OnPMOSIPGate']['_XYCoordinates'] = self.getXY('M1forIPGate')



        self._DesignParameter['M3forIPGate']['_XWidth'] = self.getXWidth('POHforIP')
        self._DesignParameter['M3forIPGate']['_YWidth'] = self.getYWidth('POHforIP')
        self._DesignParameter['M3forIPGate']['_XYCoordinates'] = self.getXY('POHforIP')



    def _CalculateCurrentSource(self, _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None,
                                _NumFingerOfCurrentSource=None, _WidthOfMiddleRoutingCS=None, _XVT=None):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        assert _NumFingerOfCurrentSource % 2 == 0
        NumFingerOfCS = _NumFingerOfCurrentSource // 2

        """ ======================================================================================================= """
        """ --------------------------------------- PMOS for Current Source --------------------------------------- """
        """ ======================================================================================================= """
        ''' PMOS Generation '''
        PMOSParam_CurrentSource = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSParam_CurrentSource['_PMOSNumberofGate'] = NumFingerOfCS
        PMOSParam_CurrentSource['_PMOSChannelWidth'] = _FingerWidthOfCurrentSource
        PMOSParam_CurrentSource['_PMOSChannellength'] = _FingerLengthOfCurrentSource
        PMOSParam_CurrentSource['_PMOSDummy'] = True
        PMOSParam_CurrentSource['_XVT'] = _XVT
        self._DesignParameter['PMOS_CS'] = self._SrefElementDeclaration(
            _DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSCS_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS_CS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_CurrentSource)

        DistanceBtwGateOfCS = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']


        ''' Poly & M1 for PMOS CurrentSource Middle Routing '''
        self._DesignParameter['POHforCS']['_XWidth'] = DistanceBtwGateOfCS * (NumFingerOfCS-1) + _FingerLengthOfCurrentSource
        self._DesignParameter['POHforCS']['_YWidth'] = _WidthOfMiddleRoutingCS


        ''' ----------------------------- Coordinates setting '''
        # 0: CenterSource, 1: ShiftRight, 2: FlipS&D 3: ShiftLeft -> I want to put Source to Center(XCoordinate).
        CaseOfCSFingers = (NumFingerOfCS % 4)
        if CaseOfCSFingers == 1:
            OffsetXforCenterSourceOfCS = +0.5 * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']
        elif CaseOfCSFingers == 2:  # swap source-drain
            OffsetXforCenterSourceOfCS = 0
            self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'], self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'] \
                = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'], self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']
        elif CaseOfCSFingers == 3:
            OffsetXforCenterSourceOfCS = -0.5 * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']
        else:  # CaseOfCSFingers is 0
            OffsetXforCenterSourceOfCS = 0

        DistanceYBtwMidRouting2CS1 = .5 * (self.getYWidth('PMOS_CS', '_Met1Layer') + self.getYWidth('POHforCS')) \
                                     + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify
        DistanceYBtwMidRouting2CS2 = .5 * (self.getYWidth('PMOS_CS', '_Met1Layer') + self.getYWidth('POHforCS')) \
                                     + _DRCObj._VIAxMinSpaceFor3neighboring  # Distance between Source/Drain's Via - to - PolyGate Metal's Via (for worst enclosure condition)
        DistanceYBtwMidRouting2CS = max(DistanceYBtwMidRouting2CS1, DistanceYBtwMidRouting2CS2)

        self._DesignParameter['POHforCS']['_XYCoordinates'] = [[OffsetXforCenterSourceOfCS, 0]]
        self._DesignParameter['PMOS_CS']['_XYCoordinates'] = \
            [CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0], [0, -DistanceYBtwMidRouting2CS]),
             CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0], [0, +DistanceYBtwMidRouting2CS])]


        ''' Vertical Gate for Current Source'''
        self._DesignParameter['POVforCS']['_XWidth'] = _FingerLengthOfCurrentSource
        self._DesignParameter['POVforCS']['_YWidth'] = DistanceYBtwMidRouting2CS * 2 - self.getYWidth('PMOS_CS', '_POLayer')
        for XYs_PO1 in self._DesignParameter['POHforCS']['_XYCoordinates']:
            for XYs_PO2 in self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']:
                self._DesignParameter['POVforCS']['_XYCoordinates'].append(CoordCalc.Add(XYs_PO1, XYs_PO2))


        ''' Text for PMOS_CS source/drain '''
        self._DesignParameter['PMOS_CS_Source'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='S', _XYCoordinates=[])
        self._DesignParameter['PMOS_CS_Drain'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='D', _XYCoordinates=[])
        for XYs_PMOS in self._DesignParameter['PMOS_CS']['_XYCoordinates']:
            for XYs_Source in self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']:
                self._DesignParameter['PMOS_CS_Source']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Source))
            for XYs_Drain in self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']:
                self._DesignParameter['PMOS_CS_Drain']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Drain))



        ''' ------------------------------------- M1V1M2 for CS Source/Drain ------------------------------------------------ '''
        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = 1
        Via1Params['_ViaMet12Met2NumberOfCOY'] = 2
        self._DesignParameter['M1V1M2OnPMOSCS'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2forCS_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['M1V1M2OnPMOSCS']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)

        DistanceYBtwM2H = self.getYWidth('M1V1M2OnPMOSCS', '_Met2Layer') + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width

        tmpXYs = []
        for XYs in self.getXY('PMOS_CS_Source'):
            tmpXYs.append(CoordCalc.Add(XYs, [0, +DistanceYBtwM2H / 2]))
        for XYs in self.getXY('PMOS_CS_Drain'):
            tmpXYs.append(CoordCalc.Add(XYs, [0, -DistanceYBtwM2H / 2]))
        self._DesignParameter['M1V1M2OnPMOSCS']['_XYCoordinates'] = tmpXYs

        # ''' M1V1M2 for Current Source'''
        # NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
        #     _XWidth=self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
        #     _YWidth=self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - 0.5 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # assert NumViaY >= 2, 'FingerWidth should be longer.'
        #
        # Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        # Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaX
        # Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaY
        # self._DesignParameter['M1V1M2OnPMOSCS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSCS_In{}'.format(_Name)), _XYCoordinates=[])[0]
        # self._DesignParameter['M1V1M2OnPMOSCS']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)
        #
        # for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
        #     self._DesignParameter['M1V1M2OnPMOSCS']['_XYCoordinates'].append(
        #         CoordCalc.Add(XYs, [0, +self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        # for XYs in self._DesignParameter['PMOS_CS_Drain']['_XYCoordinates']:
        #     self._DesignParameter['M1V1M2OnPMOSCS']['_XYCoordinates'].append(
        #         CoordCalc.Add(XYs, [0, -self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        #
        # self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['M1V1M2OnPMOSCS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        # ''' M2V2M3 on PMOSCS Source / Drain Generate & Place '''
        # M2V2M3Params_CS = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        # M2V2M3Params_CS['_ViaMet22Met3NumberOfCOX'] = 1
        # M2V2M3Params_CS['_ViaMet22Met3NumberOfCOY'] = 2
        # self._DesignParameter['M2V2M3OnPMOSCS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSCS_In{}'.format(_Name)))[0]
        # self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3Params_CS)
        #
        # DistanceYBtwM3H_CS = self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] \
        #                      + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width
        # NumM3HOnCS = int(round(float(_FingerWidthOfCurrentSource) / (DistanceYBtwM3H_CS * 2)))
        # # print('Number of M3H on CS is ', float(_FingerWidthOfCurrentSource) / (DistanceYBtwM3H_CS * 2))
        # assert NumM3HOnCS >= 1, '_FingerWidthOfCurrentSource should be longer.'
        # OffsetVia2_CS = self.FloorMinSnapSpacing(0.5 * (_FingerWidthOfCurrentSource - self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']), MinSnapSpacing)
        #
        # tmpXYs = []
        # for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
        #     for i in range(0, NumM3HOnCS):
        #         if XYs[1] < self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:
        #             tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i)]))  # Lower Source
        #         else:
        #             tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i + 1)]))  # Upper Source
        # for XYs in self._DesignParameter['PMOS_CS_Drain']['_XYCoordinates']:
        #     for i in range(0, NumM3HOnCS):
        #         if XYs[1] > self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:
        #             tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i)]))  # Upper Drain
        #         else:
        #             tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i + 1)]))  # Lower Drain
        # self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'] = tmpXYs
        #
        #
        # ''' horizontal routing M3 for PMOS Current Source '''
        # self._DesignParameter['M3HforCSSource']['_XWidth'] = \
        #     CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[2] \
        #     - CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[0] \
        #     + self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        # self._DesignParameter['M3HforCSSource']['_YWidth'] = _DRCObj._Metal1MinWidth
        #
        # self._DesignParameter['M3HforCSDrain']['_XWidth'] = \
        #     abs(self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
        #         - self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
        #     + self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        # self._DesignParameter['M3HforCSDrain']['_YWidth'] = _DRCObj._Metal1MinWidth
        #
        # tmpXYs = []
        # for i in range(0, NumM3HOnCS):
        #     tmpXYs.append(CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
        #                                 [0, - DistanceYBtwMidRouting2CS + OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i)]))
        #     tmpXYs.append(CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
        #                                 [0, + DistanceYBtwMidRouting2CS - OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i + 1)]))
        # self._DesignParameter['M3HforCSSource']['_XYCoordinates'] = tmpXYs
        #
        # tmpXYs = []
        # for i in range(0, NumM3HOnCS):
        #     tmpXYs.extend(
        #         [CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
        #                        [0, + DistanceYBtwMidRouting2CS - OffsetVia2_CS + DistanceYBtwM3H_CS * (2*i)]),
        #          CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
        #                        [0, - DistanceYBtwMidRouting2CS + OffsetVia2_CS - DistanceYBtwM3H_CS * (2*i+1)])])
        # self._DesignParameter['M3HforCSDrain']['_XYCoordinates'] = tmpXYs

        ''' ----------------------------- horizontal routing M2 for PMOS_IP Source/Drain -------------------------------- '''
        self._DesignParameter['M2HforCSSource']['_XWidth'] = \
            CoordCalc.MinMaxXY(self.getXY('M1V1M2OnPMOSCS'))[2] \
            - CoordCalc.MinMaxXY(self.getXY('M1V1M2OnPMOSCS'))[0] \
            + self.getXWidth('M1V1M2OnPMOSCS', '_Met2Layer')
        self._DesignParameter['M2HforCSSource']['_YWidth'] = self.getYWidth('M1V1M2OnPMOSCS', '_Met2Layer')
        self._DesignParameter['M2HforCSDrain']['_XWidth'] = \
            abs(self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                - self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
            + self.getXWidth('M1V1M2OnPMOSCS', '_Met2Layer')
        self._DesignParameter['M2HforCSDrain']['_YWidth'] = self.getYWidth('M1V1M2OnPMOSCS', '_Met2Layer')

        self._DesignParameter['M2HforCSSource']['_XYCoordinates'] = [
            [OffsetXforCenterSourceOfCS, -DistanceYBtwMidRouting2CS + DistanceYBtwM2H / 2],
            [OffsetXforCenterSourceOfCS, +DistanceYBtwMidRouting2CS + DistanceYBtwM2H / 2]
        ]
        self._DesignParameter['M2HforCSDrain']['_XYCoordinates'] = [
            [OffsetXforCenterSourceOfCS, -DistanceYBtwMidRouting2CS - DistanceYBtwM2H / 2],
            [OffsetXforCenterSourceOfCS, +DistanceYBtwMidRouting2CS - DistanceYBtwM2H / 2]
        ]


        ''' M1V for CS Routing '''
        step_M1V_CS_Routing = 8  # input parameter
        xlist_SD = []
        for XY in self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']:
            xlist_SD.append(XY[0])
        # xlist_SD.sort(reverse=True)

        tmpXYs = []
        for i, XY in enumerate(self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']):
            if (i // step_M1V_CS_Routing) % 2 == 0:
                tmpXYs.append(CoordCalc.Add(XY, self._DesignParameter['POHforCS']['_XYCoordinates'][0]))
        self._DesignParameter['M1VforCS']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1VforCS']['_XWidth'] = self.getXWidth('M1V1M2OnPMOSCS', '_Met1Layer')
        self._DesignParameter['M1VforCS']['_YWidth'] = DistanceYBtwMidRouting2CS * 2 + self.getYWidth('PMOS_CS', '_Met1Layer')




        ''' ------------------- M1V1M2, M2V2M3 on PMOSIP Gate(poly) Generate & Place ------------------------------- '''
        NumViaSetOnGate = math.trunc(NumFingerOfCS / float(step_M1V_CS_Routing * 2))
        assert NumViaSetOnGate >= 1, f'M1V1M2OnPMOSCSGate Generation Failed. - should have more fingers.' \
                                     f'NumFingerOfCS = {NumFingerOfCS}, ' \
                                     f'step_M1V_CS_Routing = {step_M1V_CS_Routing},' \
                                     f'-> NumViaSetOnGate = {NumViaSetOnGate}'
        tmpXYs = []
        for i in range(0, NumViaSetOnGate):
            tmpXYs.extend([[OffsetXforCenterSourceOfCS + xlist_SD[0] - ((step_M1V_CS_Routing - 1) / 2.0 + step_M1V_CS_Routing) * (xlist_SD[0] - xlist_SD[1]) - (2 * i * step_M1V_CS_Routing) * (xlist_SD[0] - xlist_SD[1]), 0],])
        self._DesignParameter['M1forCSGate']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1forCSGate']['_XWidth'] = (step_M1V_CS_Routing - 2) * abs(xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfCurrentSource
        self._DesignParameter['M1forCSGate']['_YWidth'] = self.getYWidth('POHforCS')

        NumViaXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=self.getXWidth('M1forCSGate'), _YWidth=self.getYWidth('M1forCSGate'))
        assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, 'M1V1M2OnPMOSCSGate Generation Failed.'

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['PolyContactOnPMOSCSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPMOSCSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        self._DesignParameter['PolyContactOnPMOSCSGate']['_XYCoordinates'] = self.getXY('M1forCSGate')

        # ) M2
        YWidthOfCSGate = self.getYWidth('M1forCSGate')
        self._DesignParameter['M2forCSGate']['_XWidth'] = self.getXWidth('M1forCSGate')
        self._DesignParameter['M2forCSGate']['_YWidth'] = YWidthOfCSGate
        self._DesignParameter['M2forCSGate']['_XYCoordinates'] = self.getXY('M1forCSGate')

        # ) M1V1M2
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=self.getXWidth('M1forCSGate'), _YWidth=self.getYWidth('M1forCSGate'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPMOSCSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**ViaParams)
        self._DesignParameter['M1V1M2OnPMOSCSGate']['_XYCoordinates'] = self.getXY('M1forCSGate')





        # ''' M1V1M2, M2V2M3 on PMOS CS Gate(poly) Generate & Place '''
        # NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
        #     _XWidth=(step_M1V_CS_Routing - 2) * abs(xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfCurrentSource,
        #     _YWidth=_WidthOfMiddleRoutingCS)
        # assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, 'M1V1M2OnPMOSCSGate Generation Failed.'
        #
        # M1V1M2OnPMOSCSGateParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        # M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        # M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        # self._DesignParameter['M1V1M2OnPMOSCSGate'] = self._SrefElementDeclaration(
        #     _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSCSGate_In{}'.format(_Name)))[0]
        # self._DesignParameter['M1V1M2OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M1V1M2OnPMOSCSGateParams)
        #
        # NumViaSetOnCSGate = math.trunc(NumFingerOfCS / float(step_M1V_CS_Routing * 2))
        # assert NumViaSetOnCSGate >= 1, 'M1V1M2OnPMOSCSGate Generation Failed. - should have more fingers.'
        #
        # tmpXYs = []
        # for i in range(0, NumViaSetOnCSGate):
        #     tmpXYs.append(CoordCalc.Add(
        #         self._DesignParameter['POHforCS']['_XYCoordinates'][0],
        #         [xlist_SD[0] + ((3 * step_M1V_CS_Routing - 1) / 2.0 + 2 * i * step_M1V_CS_Routing) * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'], 0]))
        # self._DesignParameter['M1V1M2OnPMOSCSGate']['_XYCoordinates'] = tmpXYs
        #
        # M2V2M3OnPMOSCSGateParams = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        # M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOX'] = M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOX']
        # M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOY'] = M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOY']
        # self._DesignParameter['M2V2M3OnPMOSCSGate'] = self._SrefElementDeclaration(
        #     _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSCSGate_In{}'.format(_Name)))[0]
        # self._DesignParameter['M2V2M3OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3OnPMOSCSGateParams)
        # self._DesignParameter['M2V2M3OnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['M1V1M2OnPMOSCSGate']['_XYCoordinates']
        #
        self._DesignParameter['M3forCSGate']['_XWidth'] = self.getXWidth('POHforCS')
        self._DesignParameter['M3forCSGate']['_YWidth'] = self.getYWidth('POHforCS')
        self._DesignParameter['M3forCSGate']['_XYCoordinates'] = self.getXY('POHforCS')



    def _CalculateDesignParameter(self, _FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None,
                                  _NumFingerOfInputPair=None,
                                  _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None,
                                  _NumFingerOfCurrentSource=None,
                                  _WidthOfMiddleRoutingIP=None, _WidthOfMiddleRoutingCS=None, _XVT=None,

                                  _NumCoYOfNbodybtwIPandCS=None, _YWidthOfNbodybtwIPandCS=None,

                                  _SubringWidth=None):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _DRCtemp_metal1minspace = 165
        _DRCtemp_metal1minspace2 = 95       # 41

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        assert _NumFingerOfInputPair % 2 == 0
        assert _NumFingerOfCurrentSource % 2 == 0
        NumFingerOfIP = _NumFingerOfInputPair // 2
        NumFingerOfCS = _NumFingerOfCurrentSource // 2

        ''' --------------------------------- PMOS IP & CS Generation ---------------------------------------------- '''
        self._CalculateInputPair_v2(_FingerWidthOfInputPair=_FingerWidthOfInputPair,
                                    _FingerLengthOfInputPair=_FingerLengthOfInputPair,
                                    _NumFingerOfInputPair=_NumFingerOfInputPair,
                                    _WidthOfMiddleRoutingIP=_WidthOfMiddleRoutingIP,
                                    _XVT=_XVT)
        self._CalculateCurrentSource(_FingerWidthOfCurrentSource=_FingerWidthOfCurrentSource,
                                     _FingerLengthOfCurrentSource=_FingerLengthOfCurrentSource,
                                     _NumFingerOfCurrentSource=_NumFingerOfCurrentSource,
                                     _WidthOfMiddleRoutingCS=_WidthOfMiddleRoutingCS,
                                     _XVT=_XVT)

        ''' -------------------------- Nbody Contact (between PMOS_IP and PMOS_CS) Generation ---------------------- '''
        XWidthOfNbody_byIP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (_NumFingerOfInputPair + 2) \
                             + self._DesignParameter['M1V1M2OnPMOSIP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        XWidthOfNbody_byCS = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (_NumFingerOfCurrentSource/2 + 1) \
                             + self._DesignParameter['M1V1M2OnPMOSCS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        XWidthOfNbody = max(XWidthOfNbody_byIP, XWidthOfNbody_byCS)
        NumNbodyCoX = int(XWidthOfNbody / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) - 1  # Bad Equation
        ''' -------------------------------------------------------------------------------------------------------- '''
        # 1) by YWidth (_YWidthOfNbodybtwIPandCS)
        YWidthOfNbodybtwIPandCS_byYWidth = _YWidthOfNbodybtwIPandCS if _YWidthOfNbodybtwIPandCS != None else 0
        NumNbodyCoY_byYWidth = (YWidthOfNbodybtwIPandCS_byYWidth - _DRCObj._CoMinWidth
                                - 2 * max(_DRCObj._Metal1MinEnclosureCO2, _DRCObj._CoMinEnclosureByPOAtLeastTwoSide)) \
                               // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + 1

        # 2) by ContactNum (_NumCoYOfNbodybtwIPandCS)
        NumNbodyCoY_byContactNum = _NumCoYOfNbodybtwIPandCS if _NumCoYOfNbodybtwIPandCS != None else 2
        YWidthOfNbodybtwIPandCS_byContactNum = (NumNbodyCoY_byContactNum - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) \
                                           + _DRCObj._CoMinWidth \
                                           + 2 * max(_DRCObj._Metal1MinEnclosureCO2, _DRCObj._CoMinEnclosureByPOAtLeastTwoSide)

        NumNbodyCoY = max(NumNbodyCoY_byYWidth, NumNbodyCoY_byContactNum)
        YWidthOfNbody = max(YWidthOfNbodybtwIPandCS_byYWidth, YWidthOfNbodybtwIPandCS_byContactNum)
        ''' -------------------------------------------------------------------------------------------------------- '''


        NbodyParameters = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters.update({'_NumberOfNbodyCOX': NumNbodyCoX, '_NumberOfNbodyCOY': NumNbodyCoY,
                                '_Met1XWidth': XWidthOfNbody, '_Met1YWidth': YWidthOfNbody})
        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(
            _DesignObj=NbodyContact_iksu._NbodyContact(_Name='NbodyContact_In{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)


        # ''' M2H,M3H on CS for routing CS to IP '''
        # if XWidthOfNbody_byIP > XWidthOfNbody_byCS:
        #     XWidthForRouteCS2IP = self._DesignParameter['M2HforIPSource']['_XWidth']
        #     XOffsetForRouteCS2IP = 0
        # else:
        #     XWidthForRouteCS2IP = self._DesignParameter['M2HforCSDrain']['_XWidth']
        #     XOffsetForRouteCS2IP = self._DesignParameter['POHforCS']['_XYCoordinates'][0][0]
        #
        # self._DesignParameter['M2HforCS2IP']['_XWidth'] = XWidthForRouteCS2IP
        # self._DesignParameter['M2HforCS2IP']['_YWidth'] = _DRCObj._MetalxMinWidth
        #
        # YEnclosureCoordOfM2V2M3onCS1 = CoordCalc.getSortedList_ascending(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[1][0] \
        #                                - self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2.0
        # YEnclosureCoordOfM2V2M3onCS2 = CoordCalc.getSortedList_ascending(self._DesignParameter['M1V1M2OnPMOSCS']['_XYCoordinates'])[1][1] \
        #                                - self._DesignParameter['M1V1M2OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2.0 \
        #                                - self._DesignParameter['M2HforCS2IP']['_YWidth'] \
        #                                - _DRCObj._MetalxMinSpaceAtCorner
        # YEnclosureCoordOfM2V2M3onCS = min(YEnclosureCoordOfM2V2M3onCS1, YEnclosureCoordOfM2V2M3onCS2)
        #
        # self._DesignParameter['M2HforCS2IP']['_XYCoordinates'] = \
        #     [[XOffsetForRouteCS2IP, YEnclosureCoordOfM2V2M3onCS + self._DesignParameter['M2HforCS2IP']['_YWidth']*0.5]]
        #
        # M3HforCS2IP_LowerBound = YEnclosureCoordOfM2V2M3onCS
        # M3HforCS2IP_UpperBound = CoordCalc.getXYCoords_MinY(self._DesignParameter['M3HforCSDrain']['_XYCoordinates'])[0][1] \
        #                          + self._DesignParameter['M3HforCSDrain']['_YWidth'] / 2.0
        #
        # M3HforCS2IP_YWidth = self.FloorMinSnapSpacing((M3HforCS2IP_UpperBound - M3HforCS2IP_LowerBound), 2*MinSnapSpacing)
        # assert M3HforCS2IP_YWidth > _DRCObj._MetalxMinWidth
        # M3HforCS2IP_YCenter = self.FloorMinSnapSpacing((M3HforCS2IP_UpperBound + M3HforCS2IP_LowerBound)/2.0, MinSnapSpacing)
        #
        # self._DesignParameter['M3HforCS2IP']['_XWidth'] = self._DesignParameter['M2HforCS2IP']['_XWidth']
        # self._DesignParameter['M3HforCS2IP']['_YWidth'] = M3HforCS2IP_YWidth
        # self._DesignParameter['M3HforCS2IP']['_XYCoordinates'] = [[XOffsetForRouteCS2IP, M3HforCS2IP_YCenter]]


        ''' ---------------------------------- Coordinates setting ------------------------------------------------- '''
        DistanceYBtwMidRouting2IP = abs(self._DesignParameter['PMOS_IP']['_XYCoordinates'][0][1])
        DistanceYBtwMidRouting2CS = abs(self._DesignParameter['PMOS_CS']['_XYCoordinates'][0][1])

        # 1) Calculate YCoord of PMOS CS - by OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
        DistanceYBtwNbody2PMOSIP_byOD = \
            0.5 * self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
            + _DRCObj._OdMinSpace
        DistanceYBtwNbody2PMOSCS_byOD = \
            0.5 * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
            + _DRCObj._OdMinSpace

        # 1-2)
        DistanceYBtwNbody2PMOSIP_byM1 = \
            0.5 * self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + _DRCObj._Metal1DefaultSpace
        DistanceYBtwNbody2PMOSCS_byM1 = \
            0.5 * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + _DRCObj._Metal1DefaultSpace

        DistanceYBtwNbody2PMOSIP = max(DistanceYBtwNbody2PMOSIP_byOD, DistanceYBtwNbody2PMOSIP_byM1)
        DistanceYBtwNbody2PMOSCS = max(DistanceYBtwNbody2PMOSCS_byOD, DistanceYBtwNbody2PMOSCS_byM1)

        OffsetYOfPMOSCS1 = DistanceYBtwMidRouting2IP + DistanceYBtwNbody2PMOSIP \
                           + DistanceYBtwNbody2PMOSCS + DistanceYBtwMidRouting2CS

        # 2) Calculate YCoord of PMOS CS - by M3 Enclose
        XWidthGapBtwIPSource = \
            2*self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] \
            - self._DesignParameter['M1V1M2OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        tmpDRC_MxEnclosedArea = 59000  # Need to Modify
        M3YMinGapBtwIPSource2CSDrain = self.CeilMinSnapSpacing(float(tmpDRC_MxEnclosedArea) / XWidthGapBtwIPSource,
                                                               2*MinSnapSpacing)
        # OffsetYOfPMOSCS2 = \
        #     CoordCalc.getXYCoords_MaxY(self._DesignParameter['M2HforIPSource']['_XYCoordinates'])[0][1] \
        #     + self._DesignParameter['M2HforIPSource']['_YWidth'] / 2.0 + M3YMinGapBtwIPSource2CSDrain \
        #     + self._DesignParameter['M2HforCS2IP']['_YWidth'] / 2.0 \
        #     + abs(self._DesignParameter['M2HforCS2IP']['_XYCoordinates'][0][1])
        OffsetYOfPMOSCS2=0
        OffsetYOfPMOSCS = self.CeilMinSnapSpacing(max(OffsetYOfPMOSCS1, OffsetYOfPMOSCS2), 2*MinSnapSpacing)

        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, DistanceYBtwMidRouting2IP + DistanceYBtwNbody2PMOSIP]]


        ''' Relocation of Current Source '''
        ObjListRelatedCS = ['PMOS_CS', 'PolyContactOnPMOSCSGate', 'PMOS_CS_Source', 'PMOS_CS_Drain', 'M1V1M2OnPMOSCS',
                            'M1V1M2OnPMOSCSGate',
                             'POHforCS', 'POVforCS', 'M1forCSGate', 'M2forCSGate', 'M3forCSGate',
                            'M1VforCS', 'M2HforCSSource', 'M2HforCSDrain', 'M2HforCS2IP', 'M3HforCS2IP']
        for DesignObj in ObjListRelatedCS:
            self.YShiftUp(DesignObj, OffsetYOfPMOSCS)


        # ''' -------------------------------------------------------------------------------------------------------- '''
        # ''' Vertical Routing  CS(drain) to IP(source) '''
        # # self._DesignParameter['M2VforCS2IP']['_Width'] = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        # # self._DesignParameter['M3VforCS2IP']['_Width'] = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        # #
        # # tmpXYs = []
        # # for XY in CoordCalc.getXYCoords_MaxY(self._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates']):
        # #     tmpXYs.append([XY, [XY[0], self._DesignParameter['M2HforCS2IP']['_XYCoordinates'][0][1]]])
        # # self._DesignParameter['M2VforCS2IP']['_XYCoordinates'] = tmpXYs
        # # self._DesignParameter['M3VforCS2IP']['_XYCoordinates'] = tmpXYs
        #
        # ''' -------------------------------------------------------------------------------------------------------- '''
        # VariableForM2VForCS2IP_1 = 3
        # VariableForM2VForCS2IP_2 = 10
        # VariableForM2VForCS2IP_3 = VariableForM2VForCS2IP_2 - VariableForM2VForCS2IP_1 - 2
        #
        #
        # upperYOfM2VForCS2IP = CoordCalc.getSortedList_ascending(self.getXY('M2HforCS2IP'))[1][0] - self.getYWidth('M2HforCS2IP') / 2
        # lowerYOfM2VForCS2IP = CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSIP', '_Met2Layer'))[1][-1] + self.getYWidth('M2V2M3OnPMOSIP', '_Met2Layer') / 2
        # self._DesignParameter['M2VForCS2IP']['_YWidth'] = upperYOfM2VForCS2IP - lowerYOfM2VForCS2IP
        #
        # DistanceXBtwPoly_IP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']
        # self._DesignParameter['M2VForCS2IP']['_XWidth'] = DistanceXBtwPoly_IP * (VariableForM2VForCS2IP_1 - 1) + self.getXWidth('M2V2M3OnPMOSIP', '_Met2Layer')
        #
        # MaxXBorderOfM2VForCS2IP = CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSIP', '_Met2Layer'))[0][-1] + self.getXWidth('M2V2M3OnPMOSIP', '_Met2Layer') / 2
        # MaxXCoordOfM2VForCS2IP = MaxXBorderOfM2VForCS2IP - self.getXWidth('M2VForCS2IP') / 2
        # DistanceXBtwM2VForCS2IP = DistanceXBtwPoly_IP * VariableForM2VForCS2IP_2
        # NumOnesideOfM2VForCS2IP = int(MaxXCoordOfM2VForCS2IP / DistanceXBtwM2VForCS2IP)
        #
        # tmpXYs = []
        # tmpXYs.append([0,(upperYOfM2VForCS2IP + lowerYOfM2VForCS2IP) / 2])
        # for i in range(0, NumOnesideOfM2VForCS2IP):
        #     tmpXYs.append([+DistanceXBtwM2VForCS2IP * (i+1), (upperYOfM2VForCS2IP + lowerYOfM2VForCS2IP) / 2])
        #     tmpXYs.append([-DistanceXBtwM2VForCS2IP * (i+1), (upperYOfM2VForCS2IP + lowerYOfM2VForCS2IP) / 2])
        # self._DesignParameter['M2VForCS2IP']['_XYCoordinates'] = tmpXYs
        #
        #
        # ''' ----------------------------------------------- Nbody M2 ----------------------------------------------- '''
        #
        # self._DesignParameter['M2ForNbody']['_XWidth'] = (VariableForM2VForCS2IP_3 - 1) * DistanceXBtwPoly_IP + self.getXWidth('M2V2M3OnPMOSIP', '_Met2Layer')
        # self._DesignParameter['M2ForNbody']['_YWidth'] = self.getYWidth('NbodyContact', '_Met1Layer')
        #
        # # MaxXCoordOfM2ForNbody = MaxXBorderOfM2VForCS2IP - self.getXWidth('M2ForNbody') / 2
        # # NumOnesideOfM2ForNbody = int((MaxXCoordOfM2VForCS2IP) / DistanceXBtwM2VForCS2IP)
        # tmpXYs = []
        # for i in range(0, NumOnesideOfM2VForCS2IP):
        #     tmpXYs.append([+DistanceXBtwM2VForCS2IP * (i+0.5), self.getXY('NbodyContact')[0][1]])
        #     tmpXYs.append([-DistanceXBtwM2VForCS2IP * (i+0.5), self.getXY('NbodyContact')[0][1]])
        # self._DesignParameter['M2ForNbody']['_XYCoordinates'] = tmpXYs
        #
        #
        # Boundary_Met1LayerOfNbody = dict(_XWidth=self.getXWidth('NbodyContact', '_Met1Layer'),
        #                                  _YWidth=self.getYWidth('NbodyContact', '_Met1Layer'),
        #                                  _XYCoordinates=self.getXY('NbodyContact', '_Met1Layer'))
        # OverlappedBoundaryForVia1OnNbody = BoundaryCalc.getOverlappedBoundaryElement(
        #     Boundary_Met1LayerOfNbody,
        #     self._DesignParameter['M2ForNbody']
        # )
        # NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
        #     _XWidth=OverlappedBoundaryForVia1OnNbody['_XWidth'],
        #     _YWidth=OverlappedBoundaryForVia1OnNbody['_YWidth']
        # )
        # Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        # Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaXYs[0]
        # Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaXYs[1]
        # self._DesignParameter['Via1OnNbody'] = self._SrefElementDeclaration(
        #     _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1OnNbody_In{}'.format(_Name)),_XYCoordinates=[])[0]
        # self._DesignParameter['Via1OnNbody']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**Via1Params)
        # self._DesignParameter['Via1OnNbody']['_XYCoordinates'] = OverlappedBoundaryForVia1OnNbody['_XYCoordinates']
        #
        #
        ''' Subring '''
        print('##############################     SubRing Generation    ########################################')
        DistanceXBtwIP2Origin = abs(self._DesignParameter['POHforIP']['_XYCoordinates'][0][0])
        OffsetXforCenterSourceOfCS = abs(self._DesignParameter['POHforCS']['_XYCoordinates'][0][0])

        XWidthOfSubring1_ODtoOD = max(2*DistanceXBtwIP2Origin + self.getXWidth('PMOS_IP', '_ODLayer'),
                                      2*OffsetXforCenterSourceOfCS + self.getXWidth('PMOS_CS', '_ODLayer')) \
                                  + 2 * _DRCObj._OdMinSpace
        XWidthOfSubring2_PolytoOD = max(2 * DistanceXBtwIP2Origin + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfIP + 1) + _FingerLengthOfInputPair,
                                        2 * OffsetXforCenterSourceOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfCS + 1) + _FingerLengthOfCurrentSource) \
                                    + 2 * _DRCObj._PolygateMinSpace2OD
        XWidthOfSubring3_Met1toMet1 = max(2 * DistanceXBtwIP2Origin + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfIP + self.getXWidth('M1VforIP'),
                                          2 * OffsetXforCenterSourceOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfCS + self.getXWidth('M1VforCS')) \
                                      + 2 * _DRCtemp_metal1minspace
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring2_PolytoOD, XWidthOfSubring3_Met1toMet1)


        YdownwardOfSubring = self.FloorMinSnapSpacing(
            CoordCalc.getSortedList_ascending(self.getXY('PMOS_IP', '_Met1Layer'))[1][0]
            - self.getYWidth('PMOS_IP', '_Met1Layer') / 2 - _DRCObj._Metal1DefaultSpace, 2 * MinSnapSpacing)
        YupwardOfSubring = self.CeilMinSnapSpacing(
            CoordCalc.getSortedList_ascending(self.getXY('PMOS_CS', '_Met1Layer'))[1][-1]
            + self.getYWidth('PMOS_CS', '_Met1Layer') / 2 + _DRCObj._Metal1DefaultSpace, 2 * MinSnapSpacing)

        YWidthOfSubring = YupwardOfSubring - YdownwardOfSubring
        YcenterOfSubring = (YupwardOfSubring + YdownwardOfSubring) / 2.0


        PSubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PSubringInputs['_PType'] = False
        PSubringInputs['_XWidth'] = XWidthOfSubring
        PSubringInputs['_YWidth'] = YWidthOfSubring
        PSubringInputs['_Width'] = _SubringWidth
        self._DesignParameter['_Subring'] = self._SrefElementDeclaration(
            _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='Subring_In{}'.format(_Name)))[0]
        self._DesignParameter['_Subring']['_DesignObj']._CalculatePSubring(**PSubringInputs)


        ''' Coordinates Settings of Subring and Nwell or ... '''
        self._DesignParameter['_Subring']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['_NWLayer']['_XWidth'] = XWidthOfSubring
        self._DesignParameter['_NWLayer']['_YWidth'] = YWidthOfSubring
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = self.getXY('_Subring')

        self._DesignParameter['_Subring']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['M1forNbodyExtention']['_XWidth'] = XWidthOfSubring
        self._DesignParameter['M1forNbodyExtention']['_YWidth'] = self.getYWidth('NbodyContact', '_Met1Layer')
        self._DesignParameter['M1forNbodyExtention']['_XYCoordinates'] = self.getXY('NbodyContact')

        self._DesignParameter['ODforNbodyExtention']['_XWidth'] = XWidthOfSubring
        self._DesignParameter['ODforNbodyExtention']['_YWidth'] = self.getYWidth('NbodyContact', '_ODLayer')
        self._DesignParameter['ODforNbodyExtention']['_XYCoordinates'] = self.getXY('NbodyContact')

        ''' Connect Between CurrentSource's source and subring(VDD) '''
        tmpXYs = []
        for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
            if XYs[1] > self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:  # upper PMOS's source
                tmpXYs.append([XYs, [XYs[0], YcenterOfSubring + YWidthOfSubring * 0.5]])
            else:  # lower PMOS's source
                tmpXYs.append([XYs, [XYs[0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + self.getYWidth('NbodyContact', '_Met1Layer')/2]])
        self._DesignParameter['M1forCSSupplyRouting']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1forCSSupplyRouting']['_Width'] = self.getXWidth('PMOS_CS', '_Met1Layer')


        ''' Metal1 Boundary(Outline) of Subring  '''
        upperYCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][1] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'])[1][-1] \
                         + self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'] / 2.0
        lowerYCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][1] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'])[1][0] \
                         - self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'] / 2.0

        RightXCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][0] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'])[0][-1] \
                         + self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] / 2.0
        LeftXCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][0] \
                        + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'])[0][0] \
                        - self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] / 2.0

        self._DesignParameter['_Met1BoundaryOfSubring']['_XWidth'] = RightXCoord_M1 - LeftXCoord_M1
        self._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] = upperYCoord_M1 - lowerYCoord_M1
        self._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'] = [[(RightXCoord_M1 + LeftXCoord_M1) / 2.0,
                                                                              (upperYCoord_M1 + lowerYCoord_M1) / 2.0]]

        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')


    def YShiftUp(self, DesignObj, OffsetY):

        tmpXYs = []
        for XY in self._DesignParameter[DesignObj]['_XYCoordinates']:
            tmpXYs.append(CoordCalc.Add(XY, [0, OffsetY]))

        self._DesignParameter[DesignObj]['_XYCoordinates'] = tmpXYs


if __name__ == '__main__':
    from Private import MyInfo
    from SthPack import PlaygroundBot

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_PMOSSet5'
    cellname = 'PMOSSetOfCML'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _FingerWidthOfInputPair=1000,            # ''' Input Pair '''
        _FingerLengthOfInputPair=30,
        _NumFingerOfInputPair=200,
        _WidthOfMiddleRoutingIP=200,

        _FingerWidthOfCurrentSource=1000,        # ''' Current Source '''
        _FingerLengthOfCurrentSource=30,
        _NumFingerOfCurrentSource=320,
        _WidthOfMiddleRoutingCS=350,

        _NumCoYOfNbodybtwIPandCS=None,
        _YWidthOfNbodybtwIPandCS=450,

        _XVT='SLVT',                      # @ 028nm, 'SLVT' 'LVT' 'RVT' 'HVT' / @ 065nm, 'LVT' 'HVT' or None
        _SubringWidth=1000,
    )

    Mode_DRCCheck = False            # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''
            InputParams['_FingerWidthOfInputPair'] = DRCchecker.RandomParam(start=400, stop=1000, step=100)
            InputParams['_FingerLengthOfInputPair'] = DRCchecker.RandomParam(start=30, stop=60, step=10)
            InputParams['_NumFingerOfInputPair'] = DRCchecker.RandomParam(start=30, stop=500, step=2)
            InputParams['_WidthOfMiddleRoutingIP'] = DRCchecker.RandomParam(start=100, stop=500, step=10)

            InputParams['_FingerWidthOfCurrentSource'] = DRCchecker.RandomParam(start=400, stop=1000, step=100)
            InputParams['_FingerLengthOfCurrentSource'] = DRCchecker.RandomParam(start=30, stop=60, step=10)
            InputParams['_NumFingerOfCurrentSource'] = DRCchecker.RandomParam(start=30, stop=500, step=2)
            InputParams['_WidthOfMiddleRoutingCS'] = DRCchecker.RandomParam(start=100, stop=500, step=10)
        else:
            pass
        print(
            "=============================   Last Layout Object's Input Parameters are   =============================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print(
            "=========================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = PMOSSetOfCMLDriver(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('##################################      Sending to FTP Server...      ##################################')
        Checker = DRCchecker.DRCchecker(
            username=My.ID,
            password=My.PW,
            WorkDir=My.Dir_Work,
            DRCrunDir=My.Dir_DRCrun,
            GDSDir=My.Dir_GDS,
            libname=libname,
            cellname=cellname,
        )
        Checker.Upload2FTP()

        if Mode_DRCCheck:
            print('###############      DRC checking... {0}/{1}      ##################'.format(ii + 1, Num_DRCCheck))
            # Bot.send2Bot(f'Start DRCChecker...\nTotal Number Of Run : {Num_DRCCheck}')
            try:
                Checker.DRCchecker()
            except Exception as e:
                print('Error Occurred: ', e)
                print("=============================   Last Layout Object's Input Parameters are   =============================")
                tmpStr = '\n'.join(f'{k} : {v}' for k,v in InputParams.items())
                print(tmpStr)
                print("=========================================================================================================")

                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\n'
                             f'ErrMsg : {e}\n'
                             f'============================='
                             f'{tmpStr}\n'
                             f'=============================')
            else:
                if (ii + 1) == Num_DRCCheck:
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number Of Run : {Num_DRCCheck}')
                    # elapsed time, start time, end time, main python file name
                else:
                    pass
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print('########################################      Finished       ###########################################')

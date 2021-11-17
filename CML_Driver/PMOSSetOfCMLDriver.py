import math
import copy

#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from Private import MyInfo
from SthPack import PrintStr, CoordCalc
from SthPack import PlaygroundBot

#
import PMOSWithDummy_iksu
import NbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
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
                M3forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M5forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[]),
                M2VforIP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3HforIPSource=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[]),
                M3HforIPDrain=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[]),

                POHforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                POVforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[]),
                M1forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                M3forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M5forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[]),
                M2VforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3HforCSSource=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M3HforCSDrain=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),

                M2HforCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[]),
                M3HforCS2IP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[]),
                M2VforCS2IP=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[]),
                M3VforCS2IP=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[]),

                M1forNbodyExtention=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                ODforNbodyExtention=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[]),
                M1forCSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[]),
                _NWLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[]),
                _Met1BoundaryOfSubring=dict(_DesignParametertype=7, _XWidth=None, _YWidth=None, _XYCoordinates=[]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameterInputPair(self,
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

        ''' PMOS Generation '''
        PMOSParam_InputPair = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSParam_InputPair['_PMOSNumberofGate'] = NumFingerOfIP
        PMOSParam_InputPair['_PMOSChannelWidth'] = _FingerWidthOfInputPair
        PMOSParam_InputPair['_PMOSChannellength'] = _FingerLengthOfInputPair
        PMOSParam_InputPair['_PMOSDummy'] = True
        PMOSParam_InputPair['_XVT'] = _XVT
        self._DesignParameter['PMOS_IP'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS_IP']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_InputPair)

        DistanceBtwGateOfIP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']

        ''' PP and XVT Layer btw Input Pair '''
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] \
                                                       - (NumFingerOfIP + 2) * DistanceBtwGateOfIP

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

        ''' Poly & M1 for PMOS Input Pair Middle Routing '''
        self._DesignParameter['POHforIP']['_XWidth'] = DistanceBtwGateOfIP * (NumFingerOfIP-1) + _FingerLengthOfInputPair
        self._DesignParameter['POHforIP']['_YWidth'] = _WidthOfMiddleRoutingIP

        self._DesignParameter['M1forIPGate']['_XWidth'] = self._DesignParameter['POHforIP']['_XWidth']
        self._DesignParameter['M1forIPGate']['_YWidth'] = self._DesignParameter['POHforIP']['_YWidth']

        NumContactXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=self._DesignParameter['POHforIP']['_XWidth'],
            _YWidth=self._DesignParameter['POHforIP']['_YWidth'])

        PolyContactParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        PolyContactParams['_ViaPoly2Met1NumberOfCOX'] = NumContactXY[0]
        PolyContactParams['_ViaPoly2Met1NumberOfCOY'] = NumContactXY[1]
        self._DesignParameter['PolyContactOnPMOSIPGate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPMOSIPGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**PolyContactParams)

        ''' Coordinates setting '''
        DistanceXBtwIP2Origin = (NumFingerOfIP / 2.0 + 1) * DistanceBtwGateOfIP
        DistanceYBtwMidRouting2IP1 = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                     + self._DesignParameter['M1forIPGate']['_YWidth'] * 0.5 \
                                     + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify
        DistanceYBtwMidRouting2IP2 = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                     + self._DesignParameter['M1forIPGate']['_YWidth'] * 0.5 \
                                     + _DRCObj._VIAxMinSpaceFor3neighboring  # Distance between Source/Drain's Via - to - PolyGate Metal's Via (for worst enclosure condition)
        DistanceYBtwMidRouting2IP = max(DistanceYBtwMidRouting2IP1, DistanceYBtwMidRouting2IP2)

        XYs_PMright = [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                       [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]
        XYs_PMleft = [[-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                      [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]

        self._DesignParameter['PMOS_IP']['_XYCoordinates'] = XYs_PMright + XYs_PMleft
        self._DesignParameter['POHforIP']['_XYCoordinates'] = [[+DistanceXBtwIP2Origin, 0],
                                                               [-DistanceXBtwIP2Origin, 0]]
        self._DesignParameter['M1forIPGate']['_XYCoordinates'] = self._DesignParameter['POHforIP']['_XYCoordinates']
        self._DesignParameter['PolyContactOnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['POHforIP']['_XYCoordinates']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[0, +DistanceYBtwMidRouting2IP],
                                                               [0, -DistanceYBtwMidRouting2IP]]
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_PPLayer']['_XYCoordinates']

        ''' Vertical Gate '''
        self._DesignParameter['POVforIP']['_XWidth'] = _FingerLengthOfInputPair
        self._DesignParameter['POVforIP']['_YWidth'] = 2*DistanceYBtwMidRouting2IP - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

        for XYs_PO1 in self._DesignParameter['POHforIP']['_XYCoordinates']:
            for XYs_PO2 in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']:
                self._DesignParameter['POVforIP']['_XYCoordinates'].append(CoordCalc.Add(XYs_PO1, XYs_PO2))

        ''' Text for PMOS_IP source/drain '''
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

        ''' M1V1M2 for IP '''
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            _XWidth=self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - 0.5*(_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
        )
        assert NumViaY >= 2, 'FingerWidth should be longer.'

        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaX
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaY
        self._DesignParameter['_Via1OnPMOSIP'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)

        for XYs in self._DesignParameter['PMOS_IP_Source']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(CoordCalc.Add(XYs, [0, +self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        for XYs in self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(CoordCalc.Add(XYs, [0, -self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))

        self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        ''' M2V2M3 on PMOSIP Source / Drain Generate & Place '''
        M2V2M3Params = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3Params['_ViaMet22Met3NumberOfCOX'] = 1
        M2V2M3Params['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['M2V2M3OnPMOSIP'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3Params)

        DistanceYBtwM3H = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] \
                          + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width
        NumM3HOnIP = int(round(float(_FingerWidthOfInputPair) / (DistanceYBtwM3H * 2)))
        # print('Number of M3H on IP is ', float(_FingerWidthOfInputPair) / (DistanceYBtwM3H * 2))
        assert NumM3HOnIP >= 1, '_FingerWidthOfInputPair should be longer.'
        OffsetVia2 = self.FloorMinSnapSpacing(0.5 * (_FingerWidthOfInputPair - self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']), MinSnapSpacing)

        tmpXYs = []
        for XYs in self._DesignParameter['PMOS_IP_Source']['_XYCoordinates']:
            for i in range(0, NumM3HOnIP):
                if XYs[1] < 0:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2 - DistanceYBtwM3H * (2 * i)]))  # Lower Source
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2 + DistanceYBtwM3H * (2 * i + 1)]))  # Upper Source
        for XYs in self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates']:
            for i in range(0, NumM3HOnIP):
                if XYs[1] > 0:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2 + DistanceYBtwM3H * (2 * i)]))  # Upper Drain
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2 - DistanceYBtwM3H * (2 * i + 1)]))  # Lower Drain
        self._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates'] = tmpXYs

        ''' horizontal routing M3 for PMOS Input Pair '''
        self._DesignParameter['M3HforIPSource']['_XWidth'] = CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates'])[2] \
                                                             - CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates'])[0] \
                                                             + self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['M3HforIPSource']['_YWidth'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['M3HforIPDrain']['_XWidth'] = abs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                                                                 - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
                                                             + self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['M3HforIPDrain']['_YWidth'] = _DRCObj._MetalxMinWidth

        tmpXYs = []
        for i in range(0, NumM3HOnIP):
            tmpXYs.append([0, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2 * i)])
            tmpXYs.append([0, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2 * i + 1)])
        self._DesignParameter['M3HforIPSource']['_XYCoordinates'] = tmpXYs

        tmpXYs = []
        for i in range(0, NumM3HOnIP):
            tmpXYs.extend(
                [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2 * i)],
                 [-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2 * i)],
                 [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2 * i + 1)],
                 [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2 * i + 1)]])
        self._DesignParameter['M3HforIPDrain']['_XYCoordinates'] = tmpXYs

        ''' M2V Routing '''
        step_M2Routing = 8  # input parameter
        xlist_SD = []
        for XY in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']:
            xlist_SD.append(XY[0])
        xlist_SD.sort(reverse=True)

        tmpXYs = []
        for i in range(0, len(xlist_SD)):
            if (i // step_M2Routing) % 2 == 0:
                tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[i], 0],
                               [-DistanceXBtwIP2Origin - xlist_SD[i], 0]])
        self._DesignParameter['M2VforIP']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M2VforIP']['_XWidth'] = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['M2VforIP']['_YWidth'] = DistanceYBtwMidRouting2IP * 2


        ''' M1V1M2, M2V2M3 on PMOSIP Gate(poly) Generate & Place '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=(step_M2Routing - 2) * (xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfInputPair,
            _YWidth=_WidthOfMiddleRoutingIP
        )
        assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, 'M1V1M2OnPMOSIPGate Generation Failed.'

        M1V1M2OnPMOSIPGateParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPMOSIPGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M1V1M2OnPMOSIPGateParams)

        NumViaSetOnGate = math.trunc(NumFingerOfIP / float(step_M2Routing * 2))
        assert NumViaSetOnGate >= 1, f'M1V1M2OnPMOSIPGate Generation Failed. - should have more fingers.' \
                                     f'NumFingerOfIP = {NumFingerOfIP}, ' \
                                     f'step_M2Routing = {step_M2Routing},' \
                                     f'-> NumViaSetOnGate = {NumViaSetOnGate}'

        tmpXYs = []
        for i in range(0, NumViaSetOnGate):
            tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[0] - ((step_M2Routing - 1) / 2.0 + step_M2Routing) * (xlist_SD[0] - xlist_SD[1]) - (2 * i * step_M2Routing) * (xlist_SD[0] - xlist_SD[1]), 0],
                           [-DistanceXBtwIP2Origin - xlist_SD[0] + ((step_M2Routing - 1) / 2.0 + step_M2Routing) * (xlist_SD[0] - xlist_SD[1]) + (2 * i * step_M2Routing) * (xlist_SD[0] - xlist_SD[1]), 0]])
        self._DesignParameter['M1V1M2OnPMOSIPGate']['_XYCoordinates'] = tmpXYs

        M2V2M3OnPMOSIPGateParams = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOX'] = M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOX']
        M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOY'] = M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOY']
        self._DesignParameter['M2V2M3OnPMOSIPGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3OnPMOSIPGateParams)
        self._DesignParameter['M2V2M3OnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['M1V1M2OnPMOSIPGate']['_XYCoordinates']

        self._DesignParameter['M3forIPGate']['_XWidth'] = self._DesignParameter['M1forIPGate']['_XWidth']
        self._DesignParameter['M3forIPGate']['_YWidth'] = self._DesignParameter['M1forIPGate']['_YWidth']
        self._DesignParameter['M3forIPGate']['_XYCoordinates'] = self._DesignParameter['M1forIPGate']['_XYCoordinates']

        ''' M3V3M4, M4V4M5 for IP and CS gate  '''
        M3V3M4OnPMOSIPGateParams = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        M3V3M4OnPMOSIPGateParams['_ViaMet32Met4NumberOfCOX'] = M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOX']
        M3V3M4OnPMOSIPGateParams['_ViaMet32Met4NumberOfCOY'] = M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOY']
        self._DesignParameter['M3V3M4OnPMOSIPGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M3V3M4OnPMOSIPGateParams)
        self._DesignParameter['M3V3M4OnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['M2V2M3OnPMOSIPGate']['_XYCoordinates']

        M4V4M5OnPMOSIPGateParams = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        M4V4M5OnPMOSIPGateParams['_ViaMet42Met5NumberOfCOX'] = M3V3M4OnPMOSIPGateParams['_ViaMet32Met4NumberOfCOX']
        M4V4M5OnPMOSIPGateParams['_ViaMet42Met5NumberOfCOY'] = M3V3M4OnPMOSIPGateParams['_ViaMet32Met4NumberOfCOY']
        self._DesignParameter['M4V4M5OnPMOSIPGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='ViaMet42Met5OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M4V4M5OnPMOSIPGateParams)
        self._DesignParameter['M4V4M5OnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['M3V3M4OnPMOSIPGate']['_XYCoordinates']

        self._DesignParameter['M5forIPGate']['_XWidth'] = self._DesignParameter['M1forIPGate']['_XWidth']
        self._DesignParameter['M5forIPGate']['_YWidth'] = self._DesignParameter['M1forIPGate']['_YWidth']
        self._DesignParameter['M5forIPGate']['_XYCoordinates'] = self._DesignParameter['M1forIPGate']['_XYCoordinates']


    def _CalculateDesignParameterCurrentSource(self, _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None,
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
        self._DesignParameter['PMOS_CS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSCS_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS_CS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_CurrentSource)

        DistanceBtwGateOfCS = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList']


        ''' Poly & M1 for PMOS CurrentSource Middle Routing '''
        self._DesignParameter['POHforCS']['_XWidth'] = DistanceBtwGateOfCS * (NumFingerOfCS-1) + _FingerLengthOfCurrentSource
        self._DesignParameter['POHforCS']['_YWidth'] = _WidthOfMiddleRoutingCS

        self._DesignParameter['M1forCSGate']['_XWidth'] = self._DesignParameter['POHforCS']['_XWidth']
        self._DesignParameter['M1forCSGate']['_YWidth'] = self._DesignParameter['POHforCS']['_YWidth']

        NumContactXY_CS = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=self._DesignParameter['POHforCS']['_XWidth'], _YWidth=self._DesignParameter['POHforCS']['_YWidth'])
        PolyContactParams_forCS = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        PolyContactParams_forCS['_ViaPoly2Met1NumberOfCOX'] = NumContactXY_CS[0]
        PolyContactParams_forCS['_ViaPoly2Met1NumberOfCOY'] = NumContactXY_CS[1]
        self._DesignParameter['PolyContactOnPMOSCSGate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSCS_In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPMOSCSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**PolyContactParams_forCS)


        ''' Coordinates setting '''
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

        DistanceYBtwMidRouting2CS1 = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                     + self._DesignParameter['M1forCSGate']['_YWidth'] * 0.5 \
                                     + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify
        DistanceYBtwMidRouting2CS2 = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                     + self._DesignParameter['M1forCSGate']['_YWidth'] * 0.5 \
                                     + _DRCObj._VIAxMinSpaceFor3neighboring  # Distance between Source/Drain's Via - to - PolyGate Metal's Via (for worst enclosure condition)
        DistanceYBtwMidRouting2CS = max(DistanceYBtwMidRouting2CS1, DistanceYBtwMidRouting2CS2)

        self._DesignParameter['POHforCS']['_XYCoordinates'] = [[OffsetXforCenterSourceOfCS, 0]]
        self._DesignParameter['PMOS_CS']['_XYCoordinates'] = \
            [CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0], [0, -DistanceYBtwMidRouting2CS]),
             CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0], [0, +DistanceYBtwMidRouting2CS])]
        self._DesignParameter['M1forCSGate']['_XYCoordinates'] = self._DesignParameter['POHforCS']['_XYCoordinates']
        self._DesignParameter['PolyContactOnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['POHforCS']['_XYCoordinates']


        ''' Vertical Gate for Current Source'''
        self._DesignParameter['POVforCS']['_XWidth'] = _FingerLengthOfCurrentSource
        self._DesignParameter['POVforCS']['_YWidth'] = DistanceYBtwMidRouting2CS * 2 - self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
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


        ''' M1V1M2 for Current Source'''
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            _XWidth=self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - 0.5 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        assert NumViaY >= 2, 'FingerWidth should be longer.'

        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaX
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaY
        self._DesignParameter['_Via1OnPMOSCS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSCS_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['_Via1OnPMOSCS']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)

        for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSCS']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, +self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        for XYs in self._DesignParameter['PMOS_CS_Drain']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSCS']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, -self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))

        self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_Via1OnPMOSCS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        ''' M2V2M3 on PMOSCS Source / Drain Generate & Place '''
        M2V2M3Params_CS = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3Params_CS['_ViaMet22Met3NumberOfCOX'] = 1
        M2V2M3Params_CS['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['M2V2M3OnPMOSCS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSCS_In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3Params_CS)

        DistanceYBtwM3H_CS = self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] \
                             + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width
        NumM3HOnCS = int(round(float(_FingerWidthOfCurrentSource) / (DistanceYBtwM3H_CS * 2)))
        # print('Number of M3H on CS is ', float(_FingerWidthOfCurrentSource) / (DistanceYBtwM3H_CS * 2))
        assert NumM3HOnCS >= 1, '_FingerWidthOfCurrentSource should be longer.'
        OffsetVia2_CS = self.FloorMinSnapSpacing(0.5 * (_FingerWidthOfCurrentSource - self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']), MinSnapSpacing)

        tmpXYs = []
        for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
            for i in range(0, NumM3HOnCS):
                if XYs[1] < self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i)]))  # Lower Source
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i + 1)]))  # Upper Source
        for XYs in self._DesignParameter['PMOS_CS_Drain']['_XYCoordinates']:
            for i in range(0, NumM3HOnCS):
                if XYs[1] > self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i)]))  # Upper Drain
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i + 1)]))  # Lower Drain
        self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'] = tmpXYs


        ''' horizontal routing M3 for PMOS Current Source '''
        self._DesignParameter['M3HforCSSource']['_XWidth'] = \
            CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[2] \
            - CoordCalc.MinMaxXY(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[0] \
            + self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['M3HforCSSource']['_YWidth'] = _DRCObj._Metal1MinWidth

        self._DesignParameter['M3HforCSDrain']['_XWidth'] = \
            abs(self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                - self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
            + self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['M3HforCSDrain']['_YWidth'] = _DRCObj._Metal1MinWidth

        tmpXYs = []
        for i in range(0, NumM3HOnCS):
            tmpXYs.append(CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
                                        [0, - DistanceYBtwMidRouting2CS + OffsetVia2_CS - DistanceYBtwM3H_CS * (2 * i)]))
            tmpXYs.append(CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
                                        [0, + DistanceYBtwMidRouting2CS - OffsetVia2_CS + DistanceYBtwM3H_CS * (2 * i + 1)]))
        self._DesignParameter['M3HforCSSource']['_XYCoordinates'] = tmpXYs

        tmpXYs = []
        for i in range(0, NumM3HOnCS):
            tmpXYs.extend(
                [CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
                               [0, + DistanceYBtwMidRouting2CS - OffsetVia2_CS + DistanceYBtwM3H_CS * (2*i)]),
                 CoordCalc.Add(self._DesignParameter['POHforCS']['_XYCoordinates'][0],
                               [0, - DistanceYBtwMidRouting2CS + OffsetVia2_CS - DistanceYBtwM3H_CS * (2*i+1)])])
        self._DesignParameter['M3HforCSDrain']['_XYCoordinates'] = tmpXYs


        ''' M2V for CS Routing '''
        step_M2V_CS_Routing = 8  # input parameter
        xlist_SD = []
        for XY in self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']:
            xlist_SD.append(XY[0])
        # xlist_SD.sort(reverse=True)

        tmpXYs = []
        for i, XY in enumerate(self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']):
            if (i // step_M2V_CS_Routing) % 2 == 0:
                tmpXYs.append(CoordCalc.Add(XY, self._DesignParameter['POHforCS']['_XYCoordinates'][0]))
        self._DesignParameter['M2VforCS']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M2VforCS']['_XWidth'] = self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['M2VforCS']['_YWidth'] = DistanceYBtwMidRouting2CS * 2


        ''' M1V1M2, M2V2M3 on PMOS CS Gate(poly) Generate & Place '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=(step_M2V_CS_Routing - 2) * abs(xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfCurrentSource,
            _YWidth=_WidthOfMiddleRoutingCS)
        assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, 'M1V1M2OnPMOSCSGate Generation Failed.'

        M1V1M2OnPMOSCSGateParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPMOSCSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M1V1M2OnPMOSCSGateParams)

        NumViaSetOnCSGate = math.trunc(NumFingerOfCS / float(step_M2V_CS_Routing * 2))
        assert NumViaSetOnCSGate >= 1, 'M1V1M2OnPMOSCSGate Generation Failed. - should have more fingers.'

        tmpXYs = []
        for i in range(0, NumViaSetOnCSGate):
            tmpXYs.append(CoordCalc.Add(
                self._DesignParameter['POHforCS']['_XYCoordinates'][0],
                [xlist_SD[0] + ((3 * step_M2V_CS_Routing - 1) / 2.0 + 2 * i * step_M2V_CS_Routing) * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'], 0]))
        self._DesignParameter['M1V1M2OnPMOSCSGate']['_XYCoordinates'] = tmpXYs

        M2V2M3OnPMOSCSGateParams = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOX'] = M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOX']
        M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOY'] = M1V1M2OnPMOSCSGateParams['_ViaMet12Met2NumberOfCOY']
        self._DesignParameter['M2V2M3OnPMOSCSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3OnPMOSCSGateParams)
        self._DesignParameter['M2V2M3OnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['M1V1M2OnPMOSCSGate']['_XYCoordinates']

        self._DesignParameter['M3forCSGate']['_XWidth'] = self._DesignParameter['M1forCSGate']['_XWidth']
        self._DesignParameter['M3forCSGate']['_YWidth'] = self._DesignParameter['M1forCSGate']['_YWidth']
        self._DesignParameter['M3forCSGate']['_XYCoordinates'] = self._DesignParameter['M1forCSGate']['_XYCoordinates']


        ''' M3V3M4, M4V4M5 for CS gate  '''
        M3V3M4OnPMOSCSGateParams = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        M3V3M4OnPMOSCSGateParams['_ViaMet32Met4NumberOfCOX'] = M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOX']
        M3V3M4OnPMOSCSGateParams['_ViaMet32Met4NumberOfCOY'] = M2V2M3OnPMOSCSGateParams['_ViaMet22Met3NumberOfCOY']
        self._DesignParameter['M3V3M4OnPMOSCSGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4OnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M3V3M4OnPMOSCSGateParams)
        self._DesignParameter['M3V3M4OnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['M2V2M3OnPMOSCSGate']['_XYCoordinates']

        M4V4M5OnPMOSCSGateParams = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        M4V4M5OnPMOSCSGateParams['_ViaMet42Met5NumberOfCOX'] = M3V3M4OnPMOSCSGateParams['_ViaMet32Met4NumberOfCOX']
        M4V4M5OnPMOSCSGateParams['_ViaMet42Met5NumberOfCOY'] = M3V3M4OnPMOSCSGateParams['_ViaMet32Met4NumberOfCOY']
        self._DesignParameter['M4V4M5OnPMOSCSGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='ViaMet42Met5OnPMOSCSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5OnPMOSCSGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M4V4M5OnPMOSCSGateParams)
        self._DesignParameter['M4V4M5OnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['M3V3M4OnPMOSCSGate']['_XYCoordinates']

        self._DesignParameter['M5forCSGate']['_XWidth'] = self._DesignParameter['M1forCSGate']['_XWidth']
        self._DesignParameter['M5forCSGate']['_YWidth'] = self._DesignParameter['M1forCSGate']['_YWidth']
        self._DesignParameter['M5forCSGate']['_XYCoordinates'] = self._DesignParameter['M1forCSGate']['_XYCoordinates']


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

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        assert _NumFingerOfInputPair % 2 == 0
        assert _NumFingerOfCurrentSource % 2 == 0
        NumFingerOfIP = _NumFingerOfInputPair // 2
        NumFingerOfCS = _NumFingerOfCurrentSource // 2

        ''' PMOS IP & CS Generation '''
        self._CalculateDesignParameterInputPair(_FingerWidthOfInputPair=_FingerWidthOfInputPair,
                                                _FingerLengthOfInputPair=_FingerLengthOfInputPair,
                                                _NumFingerOfInputPair=_NumFingerOfInputPair,
                                                _WidthOfMiddleRoutingIP=_WidthOfMiddleRoutingIP,
                                                _XVT=_XVT)
        self._CalculateDesignParameterCurrentSource(_FingerWidthOfCurrentSource=_FingerWidthOfCurrentSource,
                                                    _FingerLengthOfCurrentSource=_FingerLengthOfCurrentSource,
                                                    _NumFingerOfCurrentSource=_NumFingerOfCurrentSource,
                                                    _WidthOfMiddleRoutingCS=_WidthOfMiddleRoutingCS,
                                                    _XVT=_XVT)

        ''' Nbody Contact (between PMOS_IP and PMOS_CS) Generation '''
        XWidthOfNbody_byIP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (_NumFingerOfInputPair + 2) \
                             + self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        XWidthOfNbody_byCS = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (_NumFingerOfCurrentSource/2 + 1) \
                             + self._DesignParameter['_Via1OnPMOSCS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
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


        ''' M2H,M3H on CS for routing CS to IP '''
        if XWidthOfNbody_byIP > XWidthOfNbody_byCS:
            XWidthForRouteCS2IP = self._DesignParameter['M3HforIPSource']['_XWidth']
            XOffsetForRouteCS2IP = 0
        else:
            XWidthForRouteCS2IP = self._DesignParameter['M3HforCSDrain']['_XWidth']
            XOffsetForRouteCS2IP = self._DesignParameter['POHforCS']['_XYCoordinates'][0][0]

        self._DesignParameter['M2HforCS2IP']['_XWidth'] = XWidthForRouteCS2IP
        self._DesignParameter['M2HforCS2IP']['_YWidth'] = _DRCObj._MetalxMinWidth

        YEnclosureCoordOfM2V2M3onCS1 = CoordCalc.getSortedList_ascending(self._DesignParameter['M2V2M3OnPMOSCS']['_XYCoordinates'])[1][0] \
                                       - self._DesignParameter['M2V2M3OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2.0
        YEnclosureCoordOfM2V2M3onCS2 = CoordCalc.getSortedList_ascending(self._DesignParameter['_Via1OnPMOSCS']['_XYCoordinates'])[1][1] \
                                       - self._DesignParameter['_Via1OnPMOSCS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2.0 \
                                       - self._DesignParameter['M2HforCS2IP']['_YWidth'] \
                                       - _DRCObj._MetalxMinSpaceAtCorner
        YEnclosureCoordOfM2V2M3onCS = min(YEnclosureCoordOfM2V2M3onCS1, YEnclosureCoordOfM2V2M3onCS2)

        self._DesignParameter['M2HforCS2IP']['_XYCoordinates'] = \
            [[XOffsetForRouteCS2IP, YEnclosureCoordOfM2V2M3onCS + self._DesignParameter['M2HforCS2IP']['_YWidth']*0.5]]

        M3HforCS2IP_LowerBound = YEnclosureCoordOfM2V2M3onCS
        M3HforCS2IP_UpperBound = CoordCalc.getXYCoords_MinY(self._DesignParameter['M3HforCSDrain']['_XYCoordinates'])[0][1] \
                                 + self._DesignParameter['M3HforCSDrain']['_YWidth'] / 2.0

        M3HforCS2IP_YWidth = self.FloorMinSnapSpacing((M3HforCS2IP_UpperBound - M3HforCS2IP_LowerBound), 2*MinSnapSpacing)
        assert M3HforCS2IP_YWidth > _DRCObj._MetalxMinWidth
        M3HforCS2IP_YCenter = self.FloorMinSnapSpacing((M3HforCS2IP_UpperBound + M3HforCS2IP_LowerBound)/2.0, MinSnapSpacing)

        self._DesignParameter['M3HforCS2IP']['_XWidth'] = self._DesignParameter['M2HforCS2IP']['_XWidth']
        self._DesignParameter['M3HforCS2IP']['_YWidth'] = M3HforCS2IP_YWidth
        self._DesignParameter['M3HforCS2IP']['_XYCoordinates'] = [[XOffsetForRouteCS2IP, M3HforCS2IP_YCenter]]


        ''' Coordinates setting '''
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
            + max(_DRCObj._Metal1MinSpace2, _DRCObj._Metal1MinSpaceAtCorner)
        DistanceYBtwNbody2PMOSCS_byM1 = \
            0.5 * self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + max(_DRCObj._Metal1MinSpace2, _DRCObj._Metal1MinSpaceAtCorner)

        # 1-3)
        DistanceYBtwNbody2PMOSIP_byM2 = \
            CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSIP', '_Met2Layer'))[1][-1] + self.getYWidth('M2V2M3OnPMOSIP', '_Met2Layer') / 2 \
            + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
            + _DRCtemp_metal1minspace - DistanceYBtwMidRouting2IP
        # DistanceYBtwNbody2PMOSIP_byM2 = 0

        DistanceYBtwNbody2PMOSIP = max(DistanceYBtwNbody2PMOSIP_byOD, DistanceYBtwNbody2PMOSIP_byM1, DistanceYBtwNbody2PMOSIP_byM2)
        DistanceYBtwNbody2PMOSCS = max(DistanceYBtwNbody2PMOSCS_byOD, DistanceYBtwNbody2PMOSCS_byM1)

        OffsetYOfPMOSCS1 = DistanceYBtwMidRouting2IP + DistanceYBtwNbody2PMOSIP \
                           + DistanceYBtwNbody2PMOSCS + DistanceYBtwMidRouting2CS

        # 2) Calculate YCoord of PMOS CS - by M3 Enclose
        XWidthGapBtwIPSource = \
            2*self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] \
            - self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        tmpDRC_MxEnclosedArea = 59000  # Need to Modify
        M3YMinGapBtwIPSource2CSDrain = self.CeilMinSnapSpacing(float(tmpDRC_MxEnclosedArea) / XWidthGapBtwIPSource,
                                                               2*MinSnapSpacing)
        OffsetYOfPMOSCS2 = \
            CoordCalc.getXYCoords_MaxY(self._DesignParameter['M3HforIPSource']['_XYCoordinates'])[0][1] \
            + self._DesignParameter['M3HforIPSource']['_YWidth'] / 2.0 + M3YMinGapBtwIPSource2CSDrain \
            + self._DesignParameter['M3HforCS2IP']['_YWidth'] / 2.0 \
            + abs(self._DesignParameter['M3HforCS2IP']['_XYCoordinates'][0][1])

        OffsetYOfPMOSCS = self.CeilMinSnapSpacing(max(OffsetYOfPMOSCS1, OffsetYOfPMOSCS2), 2*MinSnapSpacing)

        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, DistanceYBtwMidRouting2IP + DistanceYBtwNbody2PMOSIP]]


        ''' Relocation of Current Source '''
        ObjListRelatedCS = ['PMOS_CS', 'PolyContactOnPMOSCSGate', 'PMOS_CS_Source', 'PMOS_CS_Drain', '_Via1OnPMOSCS',
                            'M2V2M3OnPMOSCS', 'M1V1M2OnPMOSCSGate', 'M2V2M3OnPMOSCSGate', 'M3V3M4OnPMOSCSGate',
                            'M4V4M5OnPMOSCSGate', 'POHforCS', 'POVforCS', 'M1forCSGate', 'M3forCSGate', 'M5forCSGate',
                            'M2VforCS', 'M3HforCSSource', 'M3HforCSDrain', 'M2HforCS2IP', 'M3HforCS2IP']
        for DesignObj in ObjListRelatedCS:
            self.YShiftUp(DesignObj, OffsetYOfPMOSCS)


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' Vertical Routing  CS(drain) to IP(source) '''
        self._DesignParameter['M2VforCS2IP']['_Width'] = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['M3VforCS2IP']['_Width'] = self._DesignParameter['M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']

        tmpXYs = []
        for XY in CoordCalc.getXYCoords_MaxY(self._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates']):
            tmpXYs.append([XY, [XY[0], self._DesignParameter['M2HforCS2IP']['_XYCoordinates'][0][1]]])
        self._DesignParameter['M2VforCS2IP']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M3VforCS2IP']['_XYCoordinates'] = tmpXYs

        ''' -------------------------------------------------------------------------------------------------------- '''


        ''' Subring '''
        print('##############################     SubRing Generation    ########################################')
        DistanceXBtwIP2Origin = abs(self._DesignParameter['POHforIP']['_XYCoordinates'][0][0])
        OffsetXforCenterSourceOfCS = abs(self._DesignParameter['POHforCS']['_XYCoordinates'][0][0])



        XWidthOfSubring1_ODtoOD = max(2*DistanceXBtwIP2Origin + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
                                      2*OffsetXforCenterSourceOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) \
                                  + 2 * _DRCObj._OdMinSpace
        XWidthOfSubring2_PolytoOD = max(2 * DistanceXBtwIP2Origin + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfIP + 1) + _FingerLengthOfInputPair,
                                        2 * OffsetXforCenterSourceOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfCS + 1) + _FingerLengthOfCurrentSource) \
                                    + 2 * _DRCObj._PolygateMinSpace2OD
        XWidthOfSubring3_Met1toMet1 = max(2 * DistanceXBtwIP2Origin + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfIP + self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
                                          2 * OffsetXforCenterSourceOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfCS + self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) \
                                      + 2 * _DRCtemp_metal1minspace
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring2_PolytoOD, XWidthOfSubring3_Met1toMet1)

        # YWidth Of Subring - by Met1 spacing
        # YdownwardOfSubring_byM2V2M3 = self.CeilMinSnapSpacing(abs(CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSIP', '_Met2Layer'))[1][0]
        #                                                       - self.getYWidth('M2V2M3OnPMOSIP', '_Met2Layer') / 2 - _DRCtemp_metal1minspace), 2*MinSnapSpacing)
        # YdownwardOfSubring_byMet1 = self.CeilMinSnapSpacing(DistanceYBtwMidRouting2IP + 0.5*_FingerWidthOfInputPair + _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        # YdownwardOfSubring = max(YdownwardOfSubring_byM2V2M3, YdownwardOfSubring_byMet1)
        # YupwardOfSubring = self.CeilMinSnapSpacing(OffsetYOfPMOSCS + DistanceYBtwMidRouting2CS + 0.5*_FingerWidthOfCurrentSource + _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        # YWidthOfSubring = YdownwardOfSubring + YupwardOfSubring
        # YcenterOfSubring = (YupwardOfSubring - YdownwardOfSubring) / 2.0


        YdownwardOfSubring_byM2V2M3 = self.FloorMinSnapSpacing(CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSIP', '_Met2Layer'))[1][0]
                                                               - self.getYWidth('M2V2M3OnPMOSIP', '_Met2Layer') / 2 - _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YupwardOfSubring_byM2V2M3 = self.CeilMinSnapSpacing(CoordCalc.getSortedList_ascending(self.getXY('M2V2M3OnPMOSCS', '_Met2Layer'))[1][-1]
                                                            + self.getYWidth('M2V2M3OnPMOSCS', '_Met2Layer') / 2 + _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YdownwardOfSubring_byM1 = self.FloorMinSnapSpacing(
            CoordCalc.getSortedList_ascending(self.getXY('PMOS_IP', '_Met1Layer'))[1][0]
            - self.getYWidth('PMOS_IP', '_Met1Layer') / 2 - _DRCtemp_metal1minspace, 2 * MinSnapSpacing)
        YupwardOfSubring_byM1 = self.CeilMinSnapSpacing(
            CoordCalc.getSortedList_ascending(self.getXY('PMOS_CS', '_Met1Layer'))[1][-1]
            + self.getYWidth('PMOS_CS', '_Met1Layer') / 2 + _DRCtemp_metal1minspace, 2 * MinSnapSpacing)

        YdownwardOfSubring = min(YdownwardOfSubring_byM2V2M3, YdownwardOfSubring_byM1)
        YupwardOfSubring = max(YupwardOfSubring_byM2V2M3, YupwardOfSubring_byM1)

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
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = self._DesignParameter['_Subring']['_XYCoordinates']

        self._DesignParameter['_Subring']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['M1forNbodyExtention']['_XWidth'] = XWidthOfSubring
        self._DesignParameter['M1forNbodyExtention']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['M1forNbodyExtention']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

        self._DesignParameter['ODforNbodyExtention']['_XWidth'] = XWidthOfSubring
        self._DesignParameter['ODforNbodyExtention']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['ODforNbodyExtention']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

        ''' Connect Between CurrentSource's source and subring(VDD) '''
        tmpXYs = []
        for XYs in self._DesignParameter['PMOS_CS_Source']['_XYCoordinates']:
            if XYs[1] > self._DesignParameter['POHforCS']['_XYCoordinates'][0][1]:  # upper PMOS's source
                tmpXYs.append([XYs, [XYs[0], YcenterOfSubring + YWidthOfSubring * 0.5]])
            else:  # lower PMOS's source
                tmpXYs.append([XYs, [XYs[0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
        self._DesignParameter['M1forCSSupplyRouting']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M1forCSSupplyRouting']['_Width'] = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']


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

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_PMOSSet3'
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

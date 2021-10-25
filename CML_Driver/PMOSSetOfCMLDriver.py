import math
import copy

#
import StickDiagram
import DesignParameters
import DRC
from Private import FileManage
from Private import MyInfo

#
import PMOSWithDummy_iksu
import psubring
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import CoordCalc
import NbodyContact_iksu


class PMOSSetOfCMLDriver(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None, _NumFingerOfInputPair=None,
                                           _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None, _NumFingerOfCurrentSource=None,
                                           _WidthOfMiddleRouting=None, _XVT=None, _SubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POforIPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                               _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                _POforIPLayerV=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                M1forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                M3forIPGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL3'][1]),

                _POforCS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                # _POforCSLayerV=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                #                                                 _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                M1forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                # M3forCSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                #                                              _Datatype=DesignParameters._LayerMapping['METAL3'][1]),

                _M2VforIP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                           _Datatype=DesignParameters._LayerMapping['METAL2'][1]),
                _M3HforIPSource=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                 _Datatype=DesignParameters._LayerMapping['METAL3'][1]),
                _M3HforIPDrain=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL3'][1]),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None, _NumFingerOfInputPair=None,
                                  _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None, _NumFingerOfCurrentSource=None,
                                  _WidthOfMiddleRouting=None, _XVT=None, _SubringWidth=None):

        _DRCObj = DRC.DRC()
        _Name = 'PMOSSetOfCML'
        _XYCoordinateOfPMOSSet = [[0,0]]
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print ('#########################################################################################################')
        print ('                                    {}  PMOSSet Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ''' check # of all fingers '''
        NumFingerOfIP = _NumFingerOfInputPair/2
        NumFingerOfCS = _NumFingerOfCurrentSource/2


        ''' PMOS Generation '''
        PMOSParam_InputPair = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSParam_InputPair['_PMOSNumberofGate'] = NumFingerOfIP
        PMOSParam_InputPair['_PMOSChannelWidth'] = _FingerWidthOfInputPair
        PMOSParam_InputPair['_PMOSChannellength'] = _FingerLengthOfInputPair
        PMOSParam_InputPair['_PMOSDummy'] = True
        PMOSParam_InputPair['_XVT'] = _XVT
        self._DesignParameter['PMOS_IP'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS_IP']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_InputPair)

        DistanceBtwGateOfCS = abs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
                                  - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0])


        ''' PP and XVT Layer btw Input Pair '''
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] \
                                                       - (NumFingerOfIP + 2) * DistanceBtwGateOfCS

        if DesignParameters._Technology == '028nm':
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
            _XVTLayer = '_' + _XVT + 'Layer'
            self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVT][0],
                                                                                _Datatype=DesignParameters._LayerMapping[_XVT][1],
                                                                                _XYCoordinates=[[0,0]])
            self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']
            self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] \
                                                          - (NumFingerOfIP + 2) * DistanceBtwGateOfCS
        else:
            raise NotImplementedError


        ''' Poly & M1 for PMOS Input Pair Middle Routing '''
        self._DesignParameter['_POforIPLayer']['_XWidth'] = abs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
                                                                - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) \
                                                            + _FingerLengthOfInputPair
        self._DesignParameter['_POforIPLayer']['_YWidth'] = _WidthOfMiddleRouting

        self._DesignParameter['M1forIPGate']['_XWidth'] = self._DesignParameter['_POforIPLayer']['_XWidth']
        self._DesignParameter['M1forIPGate']['_YWidth'] = self._DesignParameter['_POforIPLayer']['_YWidth']

        NumContactXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            XWidth=self._DesignParameter['_POforIPLayer']['_XWidth'],
            YWidth=self._DesignParameter['_POforIPLayer']['_YWidth'])

        PolyContactParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        PolyContactParams['_ViaPoly2Met1NumberOfCOX'] = NumContactXY[0]
        PolyContactParams['_ViaPoly2Met1NumberOfCOY'] = NumContactXY[1]
        self._DesignParameter['_PolyContactOnPMOSIPGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['_PolyContactOnPMOSIPGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**PolyContactParams)


        ''' Coordinates setting '''
        DistanceXBtwIP2Origin = (NumFingerOfIP / 2.0 + 1) * DistanceBtwGateOfCS
        DistanceYBtwMidRouting2IP = self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                    + self._DesignParameter['M1forIPGate']['_YWidth'] * 0.5 \
                                    + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify

        XYs_PMright = [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                       [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]
        XYs_PMleft = [[-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                      [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]
        XYs_PMup = [[-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                    [+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP]]
        XYs_PMdown = [[-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP],
                      [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]

        self._DesignParameter['PMOS_IP']['_XYCoordinates'] = XYs_PMright + XYs_PMleft
        self._DesignParameter['_POforIPLayer']['_XYCoordinates'] = [[+DistanceXBtwIP2Origin, 0],
                                                                    [-DistanceXBtwIP2Origin, 0]]
        self._DesignParameter['M1forIPGate']['_XYCoordinates'] = self._DesignParameter['_POforIPLayer']['_XYCoordinates']
        self._DesignParameter['_PolyContactOnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['_POforIPLayer']['_XYCoordinates']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[0, +DistanceYBtwMidRouting2IP],
                                                               [0, -DistanceYBtwMidRouting2IP]]
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_PPLayer']['_XYCoordinates']


        ''' Vertical Gate '''
        self._DesignParameter['_POforIPLayerV']['_XWidth'] = _FingerLengthOfInputPair
        self._DesignParameter['_POforIPLayerV']['_YWidth'] = DistanceYBtwMidRouting2IP * 2 \
                                                             - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

        for XYs_PO1 in self._DesignParameter['_POforIPLayer']['_XYCoordinates']:
            for XYs_PO2 in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']:
                self._DesignParameter['_POforIPLayerV']['_XYCoordinates'].append(CoordCalc.Add(XYs_PO1, XYs_PO2))


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
        self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'] = []
        for XYs_PMOS in XYs_PMright:
            for XYs_Drain in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']:
                self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Drain))
        for XYs_PMOS in XYs_PMleft:
            for XYs_Drain in CoordCalc.FlipXs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']):
                self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'].append(CoordCalc.Add(XYs_PMOS, XYs_Drain))


        ''' M1V1M2 '''
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            YWidth=self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                   - 0.5 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        assert NumViaY >= 2, 'FingerWidth should be longer.'

        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaX
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaY
        self._DesignParameter['_Via1OnPMOSIP'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via1Params)

        for XYs in self._DesignParameter['PMOS_IP_Source']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, +self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        for XYs in self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, -self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))

        self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']


        ''' M2V2M3 on PMOSIP Source / Drain Generate & Place '''
        M2V2M3Params = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3Params['_ViaMet22Met3NumberOfCOX'] = 1
        M2V2M3Params['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['_M2V2M3OnPMOSIP'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSIP_In{}'.format(_Name)))[0]
        self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3Params)

        DistanceYBtwM3H = self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] \
                          + _DRCObj._MetalxMinSpace3  # Bad DRC usage -> Need to check Metal Width
        NumM3HOnIP = int(round(float(_FingerWidthOfInputPair) / (DistanceYBtwM3H * 2)))
        print('Number of M3H on IP is ', float(_FingerWidthOfInputPair) / (DistanceYBtwM3H * 2))
        assert NumM3HOnIP >= 1, '_FingerWidthOfInputPair should be longer.'
        OffsetVia2 = self.FloorMinSnapSpacing(0.5 * (_FingerWidthOfInputPair - self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']), MinSnapSpacing)

        tmpXYs = []
        for XYs in self._DesignParameter['PMOS_IP_Source']['_XYCoordinates']:
            for i in range(0, NumM3HOnIP):
                if XYs[1] < 0:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2 - DistanceYBtwM3H * (2*i)]))       # Lower Source
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2 + DistanceYBtwM3H * (2*i + 1)]))   # Upper Source
        for XYs in self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates']:
            for i in range(0, NumM3HOnIP):
                if XYs[1] > 0:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, -OffsetVia2 + DistanceYBtwM3H * (2*i)]))       # Upper Drain
                else:
                    tmpXYs.append(CoordCalc.Add(XYs, [0, +OffsetVia2 - DistanceYBtwM3H * (2*i + 1)]))   # Lower Drain
        self._DesignParameter['_M2V2M3OnPMOSIP']['_XYCoordinates'] = tmpXYs


        ''' horizontal routing M3 '''
        self._DesignParameter['_M3HforIPSource']['_XWidth'] = CoordCalc.MinMaxXY(self._DesignParameter['_M2V2M3OnPMOSIP']['_XYCoordinates'])[2] \
                                                             - CoordCalc.MinMaxXY(self._DesignParameter['_M2V2M3OnPMOSIP']['_XYCoordinates'])[0] \
                                                             + self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['_M3HforIPSource']['_YWidth'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_M3HforIPDrain']['_XWidth'] = abs(self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
                                                                 - self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]) \
                                                             + self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['_M3HforIPDrain']['_YWidth'] = _DRCObj._Metal1MinWidth

        tmpXYs = []
        for i in range(0, NumM3HOnIP):
            tmpXYs.append([0, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2*i)])
            tmpXYs.append([0, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2*i + 1)])
        self._DesignParameter['_M3HforIPSource']['_XYCoordinates'] = tmpXYs

        tmpXYs = []
        for i in range(0, NumM3HOnIP):
            tmpXYs.extend(
                [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2*i)],
                 [-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP - OffsetVia2 + DistanceYBtwM3H * (2*i)],
                 [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2*i + 1)],
                 [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP + OffsetVia2 - DistanceYBtwM3H * (2*i + 1)]])
        self._DesignParameter['_M3HforIPDrain']['_XYCoordinates'] = tmpXYs


        ''' M2V Routing '''
        step_M2Routing = 8      # input parameter
        xlist_SD = []
        for XY in self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']:
            xlist_SD.append(XY[0])
        xlist_SD.sort(reverse=True)

        tmpXYs = []
        for i in range(0, len(xlist_SD)):
            if (i // step_M2Routing) % 2 == 0:
                tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[i], 0],
                               [-DistanceXBtwIP2Origin - xlist_SD[i], 0]])
        self._DesignParameter['_M2VforIP']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['_M2VforIP']['_XWidth'] = self._DesignParameter['_M2V2M3OnPMOSIP']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['_M2VforIP']['_YWidth'] = DistanceYBtwMidRouting2IP * 2


        ''' M1V1M2, M2V2M3 on PMOSIP Gate(poly) Generate & Place '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            XWidth=(step_M2Routing-2) * (xlist_SD[0] - xlist_SD[1]) + _FingerLengthOfInputPair,
            YWidth=_WidthOfMiddleRouting)
        assert NumViaXY[0] >= 1 and NumViaXY[0] >= 1, '_M1V1M2OnPMOSIPGate Generation Failed.'

        M1V1M2OnPMOSIPGateParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['_M1V1M2OnPMOSIPGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['_M1V1M2OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M1V1M2OnPMOSIPGateParams)

        NumViaSetOnGate = math.trunc(NumFingerOfIP / float(step_M2Routing * 2))
        assert NumViaSetOnGate >= 1, '_M1V1M2OnPMOSIPGate Generation Failed. - should have more fingers.'
        tmpXYs = []
        for i in range(0, NumViaSetOnGate):
            tmpXYs.extend([[+DistanceXBtwIP2Origin + xlist_SD[0] - ((step_M2Routing-1)/2.0 + step_M2Routing) * (xlist_SD[0]-xlist_SD[1]) - (2*i*step_M2Routing) * (xlist_SD[0]-xlist_SD[1]), 0],
                           [-DistanceXBtwIP2Origin - xlist_SD[0] + ((step_M2Routing-1)/2.0 + step_M2Routing) * (xlist_SD[0]-xlist_SD[1]) + (2*i*step_M2Routing) * (xlist_SD[0]-xlist_SD[1]), 0]])
        self._DesignParameter['_M1V1M2OnPMOSIPGate']['_XYCoordinates'] = tmpXYs


        M2V2M3OnPMOSIPGateParams = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOX'] = M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOX']
        M2V2M3OnPMOSIPGateParams['_ViaMet22Met3NumberOfCOY'] = M1V1M2OnPMOSIPGateParams['_ViaMet12Met2NumberOfCOY']
        self._DesignParameter['_M2V2M3OnPMOSIPGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='ViaMet22Met3OnPMOSIPGate_In{}'.format(_Name)))[0]
        self._DesignParameter['_M2V2M3OnPMOSIPGate']['_DesignObj']._CalculateDesignParameterSameEnclosure(**M2V2M3OnPMOSIPGateParams)
        self._DesignParameter['_M2V2M3OnPMOSIPGate']['_XYCoordinates'] = self._DesignParameter['_M1V1M2OnPMOSIPGate']['_XYCoordinates']

        self._DesignParameter['M3forIPGate']['_XWidth'] = self._DesignParameter['M1forIPGate']['_XWidth']
        self._DesignParameter['M3forIPGate']['_YWidth'] = self._DesignParameter['M1forIPGate']['_YWidth']
        self._DesignParameter['M3forIPGate']['_XYCoordinates'] = self._DesignParameter['M1forIPGate']['_XYCoordinates']

        ''' Nbody Contact '''
        XWidthOfNbody = DistanceXBtwIP2Origin * 2 + xlist_SD[0] * 2 + self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        NumNbodyCoX = int(XWidthOfNbody / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
        NumNbodyCoY = 2

        NbodyParameters = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters.update({'_NumberOfNbodyCOX': NumNbodyCoX, '_NumberOfNbodyCOY': NumNbodyCoY})
        NbodyParameters.update({'_Met1XWidth': XWidthOfNbody, '_Met1YWidth': None})
        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_Name='NbodyContact_In{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)

        # Calculate Distance between PMOS and Nbody
        DistanceBtwVD2PMOS = 0.5 * self._DesignParameter['PMOS_IP']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                             + 0.5 * self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] \
                             + _DRCObj._OdMinSpace  # OD Layer(for Nbody) - OD Layer (for PMOS)     OD=RX
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, DistanceYBtwMidRouting2IP + DistanceBtwVD2PMOS]]


        ''' PMOS for Current Source '''
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


        ''' Poly & M1 for PMOS CurrentSource Middle Routing '''
        self._DesignParameter['_POforCS']['_XWidth'] = abs(
            self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
            - self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) \
                                                            + _FingerLengthOfInputPair
        self._DesignParameter['_POforCS']['_YWidth'] = _WidthOfMiddleRouting

        self._DesignParameter['M1forCSGate']['_XWidth'] = self._DesignParameter['_POforCS']['_XWidth']
        self._DesignParameter['M1forCSGate']['_YWidth'] = self._DesignParameter['_POforCS']['_YWidth']

        NumContactXY_CS = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            XWidth=self._DesignParameter['_POforCS']['_XWidth'],
            YWidth=self._DesignParameter['_POforCS']['_YWidth'])

        PolyContactParams_forCS = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        PolyContactParams_forCS['_ViaPoly2Met1NumberOfCOX'] = NumContactXY_CS[0]
        PolyContactParams_forCS['_ViaPoly2Met1NumberOfCOY'] = NumContactXY_CS[1]
        self._DesignParameter['_PolyContactOnPMOSCSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSCS_In{}'.format(_Name)))[0]
        self._DesignParameter['_PolyContactOnPMOSCSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**PolyContactParams_forCS)


        ''' Coordinates setting '''
        DistanceYBtwMidRouting2CS = self._DesignParameter['PMOS_CS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                    + self._DesignParameter['M1forCSGate']['_YWidth'] * 0.5 \
                                    + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify
        XYs_PMOSCS = [[0, 10000+DistanceYBtwMidRouting2CS], [0, 10000-DistanceYBtwMidRouting2CS]]

        self._DesignParameter['PMOS_CS']['_XYCoordinates'] = XYs_PMOSCS
        self._DesignParameter['_POforCS']['_XYCoordinates'] = [[(XYs_PMOSCS[0][0] + XYs_PMOSCS[1][0])/2.0, (XYs_PMOSCS[0][1] + XYs_PMOSCS[1][1])/2.0]]
        self._DesignParameter['M1forCSGate']['_XYCoordinates'] = self._DesignParameter['_POforCS']['_XYCoordinates']
        self._DesignParameter['_PolyContactOnPMOSCSGate']['_XYCoordinates'] = self._DesignParameter['_POforCS']['_XYCoordinates']



        print('test')


if __name__ == '__main__':

    # Input Parameters for Layout Object
    _FingerWidthOfInputPair = 1000
    _FingerLengthOfInputPair = 30
    _NumFingerOfInputPair = 200
    _FingerWidthOfCurrentSource = 1000
    _FingerLengthOfCurrentSource = 30
    _NumFingerOfCurrentSource = 320
    _XVT = 'SLVT'
    _SubringWidth = 1000
    _WidthOfMiddleRouting = 320

    _fileName = 'PMOSSetOfCML.gds'
    libname = 'TEST_PMOSSet'

    # Generate Layout Object
    LayoutObj = PMOSSetOfCMLDriver(_Name='PMOSSetOfCML')
    LayoutObj._CalculateDesignParameter(_FingerWidthOfInputPair=_FingerWidthOfInputPair,
                                        _FingerLengthOfInputPair=_FingerLengthOfInputPair,
                                        _NumFingerOfInputPair=_NumFingerOfInputPair,
                                        _FingerWidthOfCurrentSource=_FingerWidthOfCurrentSource,
                                        _FingerLengthOfCurrentSource=_FingerLengthOfCurrentSource,
                                        _NumFingerOfCurrentSource=_NumFingerOfCurrentSource,
                                        _WidthOfMiddleRouting=_WidthOfMiddleRouting,
                                        _XVT=_XVT, _SubringWidth=_SubringWidth)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)

    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
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

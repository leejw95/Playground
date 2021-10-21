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


class PMOSSetOfCMLDriver(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None, _NumFingerOfInputPair=None,
                                           _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None, _NumFingerOfCurrentSource=None,
                                           _WidthOfMiddleRouting=None,
                                           _XVT=None, _SubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POforIPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                               _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                _POforIPLayerV=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                _M1forIPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _FingerWidthOfInputPair=None, _FingerLengthOfInputPair=None, _NumFingerOfInputPair=None,
                                  _FingerWidthOfCurrentSource=None, _FingerLengthOfCurrentSource=None, _NumFingerOfCurrentSource=None,
                                  _WidthOfMiddleRouting=None,
                                  _XVT=None, _SubringWidth=None):

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
        self._DesignParameter['_PMOS_IP'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS_IP']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_InputPair)

        DistanceBtwGateOfCS = abs(self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
                                  - self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0])


        ''' PP and XVT Layer btw Input Pair '''
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] \
                                                       - (NumFingerOfIP + 2) * DistanceBtwGateOfCS

        if DesignParameters._Technology == '028nm':
            assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
            _XVTLayer = '_' + _XVT + 'Layer'
            self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVT][0],
                                                                                _Datatype=DesignParameters._LayerMapping[_XVT][1],
                                                                                _XYCoordinates=[[0,0]])
            self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']
            self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] \
                                                          - (NumFingerOfIP + 2) * DistanceBtwGateOfCS
        else:
            raise NotImplementedError


        ''' Poly & M1 for PMOS Input Pair Middle Routing '''
        self._DesignParameter['_POforIPLayer']['_XWidth'] = abs(self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]
                                                                - self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]) \
                                                            + _FingerLengthOfInputPair
        self._DesignParameter['_POforIPLayer']['_YWidth'] = _WidthOfMiddleRouting


        self._DesignParameter['_M1forIPLayer']['_XWidth'] = self._DesignParameter['_POforIPLayer']['_XWidth']
        self._DesignParameter['_M1forIPLayer']['_YWidth'] = self._DesignParameter['_POforIPLayer']['_YWidth']

        ''' Coordnates setting '''
        DistanceXBtwIP2Origin = (NumFingerOfIP / 2.0 + 1) * DistanceBtwGateOfCS
        DistanceYBtwMidRouting2IP = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.5 \
                                    + self._DesignParameter['_M1forIPLayer']['_YWidth'] * 0.5 \
                                    + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace2)  # Need2Modify

        self._DesignParameter['_PMOS_IP']['_XYCoordinates'] = [[+DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                                                               [-DistanceXBtwIP2Origin, +DistanceYBtwMidRouting2IP],
                                                               [+DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP],
                                                               [-DistanceXBtwIP2Origin, -DistanceYBtwMidRouting2IP]]
        self._DesignParameter['_POforIPLayer']['_XYCoordinates'] = [[+DistanceXBtwIP2Origin, 0],
                                                                    [-DistanceXBtwIP2Origin, 0]]
        self._DesignParameter['_M1forIPLayer']['_XYCoordinates'] = self._DesignParameter['_POforIPLayer']['_XYCoordinates']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[0, +DistanceYBtwMidRouting2IP],
                                                               [0, -DistanceYBtwMidRouting2IP]]
        self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_PPLayer']['_XYCoordinates']



        ''' Vertical Gate '''
        self._DesignParameter['_POforIPLayerV']['_XWidth'] = _FingerLengthOfInputPair
        self._DesignParameter['_POforIPLayerV']['_YWidth'] = DistanceYBtwMidRouting2IP * 2 \
                                                             - self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        tmpXYs = []
        for XYs_PO1 in self._DesignParameter['_POforIPLayer']['_XYCoordinates']:
            for XYs_PO2 in self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']:
                tmpXYs.append(CoordCalc.Add(XYs_PO1, XYs_PO2))
        self._DesignParameter['_POforIPLayerV']['_XYCoordinates'] = tmpXYs



        ''' Text '''
        self._DesignParameter['PMOS_IP_Source'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0],
            _Mag=0.1, _Angle=0, _TEXT='S'
        )
        tmpXYs = []
        for XYs_PMOS in self._DesignParameter['_PMOS_IP']['_XYCoordinates']:
            for XYs_Source in self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']:
                tmpXYs.append(CoordCalc.Add(XYs_PMOS, XYs_Source))
        self._DesignParameter['PMOS_IP_Source']['_XYCoordinates'] = tmpXYs


        self._DesignParameter['PMOS_IP_Drain'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0],
            _Mag=0.1, _Angle=0, _TEXT='D'
        )
        tmpXYs = []
        for XYs_PMOS in self._DesignParameter['_PMOS_IP']['_XYCoordinates']:
            for XYs_Drain in self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']:
                tmpXYs.append(CoordCalc.Add(XYs_PMOS, XYs_Drain))
        self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates'] = tmpXYs



        ''' M1V1M2 '''
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            YWidth=self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                   - 0.5 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace),
        )
        print(NumViaX, NumViaY)

        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaX
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaY
        self._DesignParameter['_Via1OnPMOSIP'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_Via1OnPMOSIP']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**Via1Params)

        for XYs in self._DesignParameter['PMOS_IP_Source']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, +self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))
        for XYs in self._DesignParameter['PMOS_IP_Drain']['_XYCoordinates']:
            self._DesignParameter['_Via1OnPMOSIP']['_XYCoordinates'].append(
                CoordCalc.Add(XYs, [0, -self.CeilMinSnapSpacing(0.25 * (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace), MinSnapSpacing)]))


        YWidthOfM3 = self._DesignParameter['_PMOS_IP']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 0.75 -


        # [XYs for XYs in self._DesignParameter['_PMOS_IP']['_XYCoordinates']]


        # PMOSParam_CurrentSource = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        # PMOSParam_CurrentSource['_PMOSNumberofGate'] = NumFingerOfCS
        # PMOSParam_CurrentSource['_PMOSChannelWidth'] = _FingerWidthOfCurrentSource
        # PMOSParam_CurrentSource['_PMOSChannellength'] = _FingerLengthOfCurrentSource
        # PMOSParam_CurrentSource['_PMOSDummy'] = True
        # PMOSParam_CurrentSource['_XVT'] = _XVT
        # self._DesignParameter['_PMOS_CS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOS2In{}'.format(_Name)))[0]
        # self._DesignParameter['_PMOS_CS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSParam_CurrentSource)





    ''' end of def _Calculate DesignParameter '''


if __name__ == '__main__':

    # Input Parameters for Layout Object
    _FingerWidthOfInputPair = 400
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

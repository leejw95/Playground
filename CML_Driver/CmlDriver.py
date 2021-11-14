import copy
import time
#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from SthPack import BoundaryCalc, CoordCalc
from SthPack import PlaygroundBot
from Private import MyInfo

#
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import psubring
from CML_Driver import PMOSSetOfCMLDriver
from CML_Driver import opppcres_with_subring


class CmlLDriver(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
        _FingerWidthOfInputPair=None,
        _FingerLengthOfInputPair=None,
        _NumFingerOfInputPair=None,
        _FingerWidthOfCurrentSource=None,
        _FingerLengthOfCurrentSource=None,
        _NumFingerOfCurrentSource=None,
        _WidthOfMiddleRoutingIP=None,
        _WidthOfMiddleRoutingCS=None,
        _XVT=None,
        _SubringWidth=None,
        _ResWidth_LoadR=None,
        _ResLength_LoadR=None,
        _NumCOY_LoadR=None,
        _NumRows_LoadR=None,
        _NumStripes_LoadR=None,
        _RoutingWidth_LoadR=None,
        _Dummy_LoadR=None,
        _SubringWidth_LoadR=None,
        _TransmissionLineWidth=None,
        _TransmissionLineDistance=None,
    )


    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )


    def _CalculateDesignParameter(self, _FingerWidthOfInputPair=None,
                                  _FingerLengthOfInputPair=None,
                                  _NumFingerOfInputPair=None,
                                  _FingerWidthOfCurrentSource=None,
                                  _FingerLengthOfCurrentSource=None,
                                  _NumFingerOfCurrentSource=None,
                                  _WidthOfMiddleRoutingIP=None,
                                  _WidthOfMiddleRoutingCS=None,
                                  _XVT=None,
                                  _SubringWidth=None,

                                  _ResWidth_LoadR=None,
                                  _ResLength_LoadR=None,
                                  _NumCOY_LoadR=None,
                                  _NumRows_LoadR=None,
                                  _NumStripes_LoadR=None,
                                  _RoutingWidth_LoadR=None,
                                  _Dummy_LoadR=None,
                                  _SubringWidth_LoadR=None,

                                  _TerminationR=None,
                                  _ResWidth_TerminationR=None,
                                  _ResLength_TerminationR=None,
                                  _NumCOY_TerminationR=None,
                                  _NumRows_TerminationR=None,
                                  _NumStripes_TerminationR=None,
                                  _RoutingWidth_TerminationR=None,
                                  _Dummy_TerminationR=None,
                                  _SubringWidth_TerminationR=None,
                                  _TransmissionLineWidth=None,
                                  _TransmissionLineDistance=None,
                                  ):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        print('     Calculate PMOSSet_In{}     '.format(_Name).center(105, '#'))
        PMOSSetParam = copy.deepcopy(PMOSSetOfCMLDriver.PMOSSetOfCMLDriver._ParametersForDesignCalculation)
        PMOSSetParam['_FingerWidthOfInputPair'] = _FingerWidthOfInputPair
        PMOSSetParam['_FingerLengthOfInputPair'] = _FingerLengthOfInputPair
        PMOSSetParam['_NumFingerOfInputPair'] = _NumFingerOfInputPair
        PMOSSetParam['_FingerWidthOfCurrentSource'] = _FingerWidthOfCurrentSource
        PMOSSetParam['_FingerLengthOfCurrentSource'] = _FingerLengthOfCurrentSource
        PMOSSetParam['_NumFingerOfCurrentSource'] = _NumFingerOfCurrentSource
        PMOSSetParam['_WidthOfMiddleRoutingIP'] = _WidthOfMiddleRoutingIP
        PMOSSetParam['_WidthOfMiddleRoutingCS'] = _WidthOfMiddleRoutingCS
        PMOSSetParam['_XVT'] = _XVT
        PMOSSetParam['_SubringWidth'] = _SubringWidth
        self._DesignParameter['PMOSSet'] = self._SrefElementDeclaration(_DesignObj=PMOSSetOfCMLDriver.PMOSSetOfCMLDriver(_DesignParameter=None, _Name='PMOSSet_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOSSet']['_DesignObj']._CalculateDesignParameter(**PMOSSetParam)
        self._DesignParameter['PMOSSet']['_XYCoordinates'] = [[0,0]]


        print('   Calculate RoadResistors_In{}   '.format(_Name).center(105, '#'))
        ResistorParam_LoadR = copy.deepcopy(opppcres_with_subring.OpppcresWithSubring._ParametersForDesignCalculation)
        ResistorParam_LoadR['_ResWidth'] = _ResWidth_LoadR
        ResistorParam_LoadR['_ResLength'] = _ResLength_LoadR
        ResistorParam_LoadR['_NumCOY'] = _NumCOY_LoadR
        ResistorParam_LoadR['_NumRows'] = _NumRows_LoadR
        ResistorParam_LoadR['_NumStripes'] = _NumStripes_LoadR
        ResistorParam_LoadR['_RoutingWidth'] = _RoutingWidth_LoadR
        ResistorParam_LoadR['_Dummy'] = _Dummy_LoadR
        ResistorParam_LoadR['_SubringWidth'] = _SubringWidth_LoadR
        self._DesignParameter['LoadResistors'] = self._SrefElementDeclaration(_DesignObj=opppcres_with_subring.OpppcresWithSubring(_DesignParameter=None, _Name='LoadResistors_In{}'.format(_Name)))[0]
        self._DesignParameter['LoadResistors']['_DesignObj']._CalculateDesignParameter(**ResistorParam_LoadR)

        DistanceBtwSubrings_PMOSSetAndLoadR = \
            self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] / 2.0 \
            + _DRCObj._Metal1MinSpace4 \
            + self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] / 2.0
        self._DesignParameter['LoadResistors']['_XYCoordinates'] = \
            [[0, (self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'][0][1]
                  - DistanceBtwSubrings_PMOSSetAndLoadR
                  - self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'][0][1])]]


        print("   Connection Between InputPair's Drain and LoadResistor   ".center(105,'#'))
        ''' M2V for InputPair Drain - LoadR '''
        UpperYBoundaryOfLoadRSubring = \
            self._DesignParameter['LoadResistors']['_XYCoordinates'][0][1] \
            + self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'][0][1] \
            + self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] / 2.0

        tmpXYs = []
        for XYs in CoordCalc.getXYCoords_MinY(self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates']):
            tmpXYs.append([XYs, [XYs[0], UpperYBoundaryOfLoadRSubring]])

        self._DesignParameter['M2VForIPDrain2LoadR'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M2VforIP']['_XWidth'],
            _XYCoordinates=tmpXYs
        )


        ''' M2H for InputPair Drain - LoadR '''
        self._DesignParameter['M2HForIPDrain2LoadR'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])

        # 1) calculate 'RightBoundaryOfM2H2_byLoadR'
        RightBoundaryOfM2H_Case1ByLoadR = CoordCalc.getSortedList_ascending(self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met2A']['_XYCoordinates'])[0][-1] \
                                          + self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met2A']['_XWidth'] / 2.0

        # 2) Calculate 'RightBoundaryOfM2H1_byIP'
        for i,XYs in enumerate(CoordCalc.getXYCoords_MinY(self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M2V2M3OnPMOSIP']['_XYCoordinates'])):
            if i == 0:      # initialize
                LowestAbsXCoord = abs(XYs[0])
                LargestAbsXCoord = abs(XYs[0])
            else:
                if LowestAbsXCoord > abs(XYs[0]):
                    LowestAbsXCoord = abs(XYs[0])
                else:
                    pass
                if LargestAbsXCoord < abs(XYs[0]):
                    LargestAbsXCoord = abs(XYs[0])
                else:
                    pass
        RightBoundaryOfM2H_Case2ByIP = LargestAbsXCoord + self._DesignParameter['M2VForIPDrain2LoadR']['_Width'] / 2

        RightBoundaryOfM2H = max(RightBoundaryOfM2H_Case1ByLoadR, RightBoundaryOfM2H_Case2ByIP)
        LeftBoundaryOfM2H = LowestAbsXCoord - self._DesignParameter['M2VForIPDrain2LoadR']['_Width'] / 2

        self._DesignParameter['M2HForIPDrain2LoadR']['_XWidth'] = RightBoundaryOfM2H - LeftBoundaryOfM2H
        self._DesignParameter['M2HForIPDrain2LoadR']['_YWidth'] = _SubringWidth_LoadR / 2
        self._DesignParameter['M2HForIPDrain2LoadR']['_XYCoordinates'] = [
            [+(RightBoundaryOfM2H + LeftBoundaryOfM2H) / 2, UpperYBoundaryOfLoadRSubring - _SubringWidth_LoadR / 4],
            [-(RightBoundaryOfM2H + LeftBoundaryOfM2H) / 2, UpperYBoundaryOfLoadRSubring - _SubringWidth_LoadR / 4]
        ]

        ''' M2V_2nd for InputPair Drain - LoadR '''
        self._DesignParameter['M2V_2ndForIPDrain2LoadR'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])

        LowerYBoundaryOfM2V_2nd = self._DesignParameter['LoadResistors']['_XYCoordinates'][0][1] \
                                  + CoordCalc.getSortedList_ascending(self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_ViaMet22Met3']['_XYCoordinates'])[1][0] \
                                  - self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2
        UpperYBoundaryOfM2V_2nd = self._DesignParameter['M2HForIPDrain2LoadR']['_XYCoordinates'][0][1] \
                                  + self._DesignParameter['M2HForIPDrain2LoadR']['_YWidth'] / 2.0

        tmpXYs = []
        for XYs in CoordCalc.getXYCoords_MinY(self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_ViaMet22Met3']['_XYCoordinates']):
            tmpXYs.append(CoordCalc.Sum(self._DesignParameter['LoadResistors']['_XYCoordinates'][0],
                                        XYs,
                                        [0, (UpperYBoundaryOfM2V_2nd - LowerYBoundaryOfM2V_2nd) / 2 - self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2]))

        self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XWidth'] = self._DesignParameter['LoadResistors']['_DesignObj']._DesignParameter['_Met2A']['_XWidth']
        self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_YWidth'] = UpperYBoundaryOfM2V_2nd - LowerYBoundaryOfM2V_2nd
        self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XYCoordinates'] = tmpXYs


        ''' M3V for InputPair Drain - LoadR '''
        self._DesignParameter['M3VForIPDrain2LoadR'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self._DesignParameter['M2VForIPDrain2LoadR']['_Width'],
            _XYCoordinates=self._DesignParameter['M2VForIPDrain2LoadR']['_XYCoordinates']
        )


        ''' M3H for InputPair Drain - LoadR '''
        self._DesignParameter['M3HForIPDrain2LoadR'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self._DesignParameter['M2HForIPDrain2LoadR']['_XWidth'],
            _YWidth=self._DesignParameter['M2HForIPDrain2LoadR']['_YWidth'],
            _XYCoordinates=self._DesignParameter['M2HForIPDrain2LoadR']['_XYCoordinates']
        )

        ''' M4V_2nd for InputPair Drain - LoadR '''
        self._DesignParameter['M4V_2ndForIPDrain2LoadR'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XWidth'],
            _YWidth=self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_YWidth'],
            _XYCoordinates=self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XYCoordinates']
        )


        ''' M2V2M3(M2H - M3H) for InputPair Drain - LoadR '''
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=self._DesignParameter['M3HForIPDrain2LoadR']['_XWidth'],
            _YWidth=self._DesignParameter['M3HForIPDrain2LoadR']['_YWidth']
        )
        Via2Params = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        Via2Params['_ViaMet22Met3NumberOfCOX'] = NumViaXYs[0]
        Via2Params['_ViaMet22Met3NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via2ForM2HM3HIPDrainLoadR'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForM2HM3HIPDrainLoadR_In{}'.format(_Name)),_XYCoordinates=[])[0]
        self._DesignParameter['Via2ForM2HM3HIPDrainLoadR']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via2Params)
        self._DesignParameter['Via2ForM2HM3HIPDrainLoadR']['_XYCoordinates'] = self._DesignParameter['M3HForIPDrain2LoadR']['_XYCoordinates']


        ''' M3V3M4(M2H - M3H) for InputPair Drain - LoadR '''
        # Calculate Overlapped Area(XWidth, YWidth, XYCoordinates)
        # target Boundary : self._DesignParameter['M4V_2ndForIPDrain2LoadR'] & self._DesignParameter['M3HForIPDrain2LoadR']
        OverlappedBoundaryForVia3 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M3HForIPDrain2LoadR'], self._DesignParameter['M4V_2ndForIPDrain2LoadR'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=OverlappedBoundaryForVia3['_XWidth'],
            _YWidth=OverlappedBoundaryForVia3['_YWidth']
        )

        Via3Params = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        Via3Params['_ViaMet32Met4NumberOfCOX'] = NumViaXYs[0]
        Via3Params['_ViaMet32Met4NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via3ForIPDrainLoadR'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForIPDrainLoadR_In{}'.format(_Name)),_XYCoordinates=[])[0]
        self._DesignParameter['Via3ForIPDrainLoadR']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via3Params)
        self._DesignParameter['Via3ForIPDrainLoadR']['_XYCoordinates'] = OverlappedBoundaryForVia3['_XYCoordinates']


        ''' M5ForIPDrain2LoadR '''
        NumSthM4HForLoadR = _NumRows_LoadR * 2 - 1

        DistanceBtwM4V = CoordCalc.getSortedList_ascending(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XYCoordinates'])[0][1] \
                         - CoordCalc.getSortedList_ascending(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XYCoordinates'])[0][0]
        NumOneSide = len(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XYCoordinates']) / 2
        XWidthOfSthM4HForLoadR = (NumOneSide-1) * DistanceBtwM4V + self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XWidth']

        YWidthOfSthM4HForLoadR = self.FloorMinSnapSpacing(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_YWidth'] / NumSthM4HForLoadR, 2*MinSnapSpacing)
        self._DesignParameter['M5ForIPDrain2LoadR'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=XWidthOfSthM4HForLoadR,
            _YWidth=YWidthOfSthM4HForLoadR,
            _XYCoordinates=[]
        )

        tmpXYs = []
        for i in range(0, _NumRows_LoadR):
            tmp1 = CoordCalc.Sum(
                CoordCalc.getXYCoords_MaxX(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XYCoordinates'])[0],
                [0, (_NumRows_LoadR-1 - 2*i) * YWidthOfSthM4HForLoadR],
                [- XWidthOfSthM4HForLoadR / 2.0 + self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XWidth']/2.0, 0])
            tmp2 = CoordCalc.Sum(
                CoordCalc.getXYCoords_MinX(self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XYCoordinates'])[0],
                [0, (_NumRows_LoadR-1 - 2*i) * YWidthOfSthM4HForLoadR],
                [+ XWidthOfSthM4HForLoadR / 2.0 - self._DesignParameter['M4V_2ndForIPDrain2LoadR']['_XWidth']/2.0, 0])
            tmpXYs.append(tmp1)
            tmpXYs.append(tmp2)

        self._DesignParameter['M5ForIPDrain2LoadR']['_XYCoordinates'] = tmpXYs

        ''' M4V4M5 For IPDrain2LoadR '''
        OverlappedBoundaryForVia4 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M4V_2ndForIPDrain2LoadR'], self._DesignParameter['M5ForIPDrain2LoadR'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=OverlappedBoundaryForVia4['_XWidth'],
            _YWidth=OverlappedBoundaryForVia4['_YWidth']
        )

        Via4Params = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        Via4Params['_ViaMet42Met5NumberOfCOX'] = NumViaXYs[0]
        Via4Params['_ViaMet42Met5NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via4ForIPDrainLoadR'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForIPDrainLoadR_In{}'.format(_Name)),_XYCoordinates=[])[0]
        self._DesignParameter['Via4ForIPDrainLoadR']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via4Params)
        self._DesignParameter['Via4ForIPDrainLoadR']['_XYCoordinates'] = OverlappedBoundaryForVia4['_XYCoordinates']



        ''' M7A, M6A(Output) For LoadR '''
        if _TransmissionLineDistance is None:
            XCoordOfM7M6 = CoordCalc.getSortedList_ascending(self._DesignParameter['M5ForIPDrain2LoadR']['_XYCoordinates'])[0][-1]
        else:
            XCoordOfM7M6 = _TransmissionLineDistance / 2

        self._DesignParameter['M7Output'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0],
            _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=_TransmissionLineWidth if _TransmissionLineWidth != None else self.getYWidth('M5ForIPDrain2LoadR'),
            _YWidth=self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_YWidth'],
            _XYCoordinates=[[+XCoordOfM7M6, self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XYCoordinates'][0][1]],
                            [-XCoordOfM7M6, self._DesignParameter['M2V_2ndForIPDrain2LoadR']['_XYCoordinates'][0][1]]]
        )

        self._DesignParameter['M6ForIPDrain2LoadR'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self._DesignParameter['M7Output']['_XWidth'],
            _YWidth=self._DesignParameter['M7Output']['_YWidth'],
            _XYCoordinates=self._DesignParameter['M7Output']['_XYCoordinates']
        )



        ''' M5V5M6 For IPDrain2LoadR '''
        OverlappedBoundaryForVia5 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5ForIPDrain2LoadR'], self._DesignParameter['M6ForIPDrain2LoadR'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            _XWidth=OverlappedBoundaryForVia5['_XWidth'], _YWidth=OverlappedBoundaryForVia5['_YWidth'])

        Via5Params = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        Via5Params['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
        Via5Params['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via5ForIPDrainLoadR'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForIPDrainLoadR_In{}'.format(_Name)),_XYCoordinates=[])[0]
        self._DesignParameter['Via5ForIPDrainLoadR']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**Via5Params)
        self._DesignParameter['Via5ForIPDrainLoadR']['_XYCoordinates'] = OverlappedBoundaryForVia5['_XYCoordinates']


        ''' M6V6M7 For IPDrain2LoadR '''        # Same with 'Via5ForIPDrainLoadR'
        Via6Params = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        Via6Params['_ViaMet62Met7NumberOfCOX'] = NumViaXYs[0]
        Via6Params['_ViaMet62Met7NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via6ForIPDrainLoadR'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForIPDrainLoadR_In{}'.format(_Name)),_XYCoordinates=[])[0]
        self._DesignParameter['Via6ForIPDrainLoadR']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(**Via6Params)
        self._DesignParameter['Via6ForIPDrainLoadR']['_XYCoordinates'] = OverlappedBoundaryForVia5['_XYCoordinates']





        if _TerminationR:
            print('   Calculate TerminationResistors_In{}   '.format(_Name).center(105,'#'))
            ResistorParam_TerminationR = copy.deepcopy(opppcres_with_subring.OpppcresWithSubring._ParametersForDesignCalculation)
            ResistorParam_TerminationR['_ResWidth'] = _ResWidth_TerminationR
            ResistorParam_TerminationR['_ResLength'] = _ResLength_TerminationR
            ResistorParam_TerminationR['_NumCOY'] = _NumCOY_TerminationR
            ResistorParam_TerminationR['_NumRows'] = _NumRows_TerminationR
            ResistorParam_TerminationR['_NumStripes'] = _NumStripes_TerminationR
            ResistorParam_TerminationR['_RoutingWidth'] = _RoutingWidth_TerminationR
            ResistorParam_TerminationR['_Dummy'] = _Dummy_TerminationR
            ResistorParam_TerminationR['_SubringWidth'] = _SubringWidth_TerminationR
            self._DesignParameter['TerminationResistors'] = self._SrefElementDeclaration(_DesignObj=opppcres_with_subring.OpppcresWithSubring(_DesignParameter=None, _Name='TerminationResistors_In{}'.format(_Name)))[0]
            self._DesignParameter['TerminationResistors']['_DesignObj']._CalculateDesignParameter(**ResistorParam_TerminationR)

            DistanceBtwSubrings_PMOSSetAndTerminationR = \
                self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] / 2.0 \
                + _DRCObj._Metal1MinSpace4 \
                + self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] / 2.0
            self._DesignParameter['TerminationResistors']['_XYCoordinates'] = \
                [[0, (self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'][0][1]
                      + DistanceBtwSubrings_PMOSSetAndTerminationR
                      - self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'][0][1])]]

            print("Connection Between CurrentSource's Drain and TerminationResistor".center(105,'#'))

            ''' M5H '''
            ''' M5ForTerminationR '''
            NumtmpSth = _NumRows_TerminationR-1 if _NumRows_TerminationR > 1 else 1
            NumSthM4HForTerminationR = NumtmpSth * 2 - 1

            DistanceBtwM4V = CoordCalc.getSortedList_ascending(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0][1] \
                             - CoordCalc.getSortedList_ascending(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0][0]
            NumOneSide = len(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates']) / 2
            XWidthOfSthM4HForTerminationR = (NumOneSide - 1) * DistanceBtwM4V + self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XWidth']

            YWidthOfSthM4HForTerminationR = self.FloorMinSnapSpacing(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_YWidth'] / NumSthM4HForTerminationR, 2 * MinSnapSpacing)
            self._DesignParameter['M5ForTerminationR'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                _XWidth=XWidthOfSthM4HForTerminationR,
                _YWidth=YWidthOfSthM4HForTerminationR,
                _XYCoordinates=[]
            )
            tmpXYs = []
            for i in range(0, NumtmpSth):
                tmp1 = CoordCalc.Sum(
                    CoordCalc.getXYCoords_MaxX(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0],
                    self._DesignParameter['TerminationResistors']['_XYCoordinates'][0],
                    [- XWidthOfSthM4HForTerminationR / 2.0 + self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XWidth'] / 2.0, (NumtmpSth - 1 - 2 * i) * YWidthOfSthM4HForTerminationR])
                tmp2 = CoordCalc.Sum(
                    CoordCalc.getXYCoords_MinX(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0],
                    self._DesignParameter['TerminationResistors']['_XYCoordinates'][0],
                    [+ XWidthOfSthM4HForTerminationR / 2.0 - self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XWidth'] / 2.0, (NumtmpSth - 1 - 2 * i) * YWidthOfSthM4HForTerminationR])
                tmpXYs.append(tmp1)
                tmpXYs.append(tmp2)

            self._DesignParameter['M5ForTerminationR']['_XYCoordinates'] = tmpXYs


            ''' M4V4M5 For TerminationR '''
            BoundaryElementOfTermResistorMet4A = dict(
                _XWidth=self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XWidth'],
                _YWidth=self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_YWidth'],
                _XYCoordinates=[]
            )
            for XYs1 in self._DesignParameter['TerminationResistors']['_XYCoordinates']:
                for XYs2 in self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates']:
                    BoundaryElementOfTermResistorMet4A['_XYCoordinates'].append(CoordCalc.Add(XYs1, XYs2))

            OverlappedBoundaryForVia4Term = BoundaryCalc.getOverlappedBoundaryElement(
                BoundaryElementOfTermResistorMet4A, self._DesignParameter['M5ForTerminationR']
            )

            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
                _XWidth=OverlappedBoundaryForVia4Term['_XWidth'],
                _YWidth=OverlappedBoundaryForVia4Term['_YWidth']
            )

            Via4ParamsTerm = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            Via4ParamsTerm['_ViaMet42Met5NumberOfCOX'] = NumViaXYs[0]
            Via4ParamsTerm['_ViaMet42Met5NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via4ForTerminationR'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForTerminationR_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via4ForTerminationR']['_DesignObj']._CalculateDesignParameterSameEnclosure(**Via4ParamsTerm)
            self._DesignParameter['Via4ForTerminationR']['_XYCoordinates'] = OverlappedBoundaryForVia4Term['_XYCoordinates']


            ''' M5HExtendForIPGate '''
            self._DesignParameter['M5HExtendForIPGate'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[]
            )
            XLeftOfM5ForIPGate = self._DesignParameter['PMOSSet']['_XYCoordinates'][0][0] \
                                 + CoordCalc.getSortedList_ascending(self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XYCoordinates'])[0][-1] \
                                 - self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XWidth'] / 2.0
            XRightOfM5ForIPGate = self._DesignParameter['PMOSSet']['_XYCoordinates'][0][0] \
                                  + CoordCalc.getSortedList_ascending(self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XYCoordinates'])[0][-1] \
                                  + self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XWidth'] / 2.0

            XRightOfM5ForTerminationR = CoordCalc.getSortedList_ascending(self._DesignParameter['M5ForTerminationR']['_XYCoordinates'])[0][-1] \
                                        + self._DesignParameter['M5ForTerminationR']['_XWidth'] / 2.0

            XRightOfM5HExtendForIPGate = max(XRightOfM5ForIPGate, XRightOfM5ForTerminationR)

            self._DesignParameter['M5HExtendForIPGate']['_XWidth'] = XRightOfM5HExtendForIPGate - XLeftOfM5ForIPGate
            self._DesignParameter['M5HExtendForIPGate']['_YWidth'] = self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_YWidth']
            self._DesignParameter['M5HExtendForIPGate']['_XYCoordinates'] = [
                [+(XRightOfM5HExtendForIPGate + XLeftOfM5ForIPGate) / 2.0, self._DesignParameter['PMOSSet']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XYCoordinates'][0][1]],
                [-(XRightOfM5HExtendForIPGate + XLeftOfM5ForIPGate) / 2.0, self._DesignParameter['PMOSSet']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSSet']['_DesignObj']._DesignParameter['M5forIPGate']['_XYCoordinates'][0][1]],
            ]

            ''' M6VForIPGate2TerminationR '''       # Calculated by M5
            self._DesignParameter['M6VForIPGate2TerminationR'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL6'][0],
                _Datatype=DesignParameters._LayerMapping['METAL6'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[]
            )
            NumOfM6VForIPGate2TerminationR = _NumStripes_TerminationR

            UpperYOfM6VForIPGate2TerminationR = CoordCalc.getSortedList_ascending(self._DesignParameter['M5ForTerminationR']['_XYCoordinates'])[1][-1] \
                                                + self._DesignParameter['M5ForTerminationR']['_YWidth'] / 2.0
            LowerYOfM6VForIPGate2TerminationR = CoordCalc.getSortedList_ascending(self._DesignParameter['M5HExtendForIPGate']['_XYCoordinates'])[1][-1] \
                                                - self._DesignParameter['M5HExtendForIPGate']['_YWidth'] / 2.0
            self._DesignParameter['M6VForIPGate2TerminationR']['_YWidth'] = UpperYOfM6VForIPGate2TerminationR - LowerYOfM6VForIPGate2TerminationR


            self._DesignParameter['M6VForIPGate2TerminationR']['_XWidth'] = self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XWidth']

            DistanceXBtwM4VOfTermRes = (CoordCalc.getSortedList_ascending(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0][1] \
                                        - CoordCalc.getSortedList_ascending(self._DesignParameter['TerminationResistors']['_DesignObj']._DesignParameter['_Met4A']['_XYCoordinates'])[0][0]) / 2.0
            tmpXYs = []
            for i in range(0, NumOfM6VForIPGate2TerminationR):
                tmp1 = [
                    CoordCalc.getSortedList_ascending(self._DesignParameter['M5ForTerminationR']['_XYCoordinates'])[0][0] + (i - (NumOfM6VForIPGate2TerminationR - 1) / 2.0) * DistanceXBtwM4VOfTermRes,
                    (UpperYOfM6VForIPGate2TerminationR + LowerYOfM6VForIPGate2TerminationR) / 2.0]
                tmp2 = [
                    CoordCalc.getSortedList_ascending(self._DesignParameter['M5ForTerminationR']['_XYCoordinates'])[0][-1] + (i - (NumOfM6VForIPGate2TerminationR - 1) / 2.0) * DistanceXBtwM4VOfTermRes,
                    (UpperYOfM6VForIPGate2TerminationR + LowerYOfM6VForIPGate2TerminationR) / 2.0]
                tmpXYs.append(tmp1)
                tmpXYs.append(tmp2)

            self._DesignParameter['M6VForIPGate2TerminationR']['_XYCoordinates'] = tmpXYs



            ''' 1 M5V5M6 On TermRes '''
            OverlappedBoundaryForVia5Term1 = BoundaryCalc.getOverlappedBoundaryElement(
                self._DesignParameter['M5ForTerminationR'], self._DesignParameter['M6VForIPGate2TerminationR']
            )
            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
                _XWidth=OverlappedBoundaryForVia5Term1['_XWidth'],
                _YWidth=OverlappedBoundaryForVia5Term1['_YWidth']
            )
            Via5ParamsTerm1 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            Via5ParamsTerm1['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
            Via5ParamsTerm1['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via5ForTerminationR1'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForTerminationR1_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via5ForTerminationR1']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**Via5ParamsTerm1)
            self._DesignParameter['Via5ForTerminationR1']['_XYCoordinates'] = OverlappedBoundaryForVia5Term1['_XYCoordinates']

            ''' 2 M5V5M6 On InputGate '''
            OverlappedBoundaryForVia5Term2 = BoundaryCalc.getOverlappedBoundaryElement(
                self._DesignParameter['M5HExtendForIPGate'], self._DesignParameter['M6VForIPGate2TerminationR']
            )
            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
                _XWidth=OverlappedBoundaryForVia5Term2['_XWidth'],
                _YWidth=OverlappedBoundaryForVia5Term2['_YWidth']
            )
            Via5ParamsTerm2 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            Via5ParamsTerm2['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
            Via5ParamsTerm2['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via5ForTerminationR2'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForTerminationR2_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via5ForTerminationR2']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**Via5ParamsTerm2)
            self._DesignParameter['Via5ForTerminationR2']['_XYCoordinates'] = OverlappedBoundaryForVia5Term2['_XYCoordinates']


            ''' M7 For Input '''
            MinX_M5Term, MinY_M5Term, MaxX_M5Term, MaxY_M5Term = CoordCalc.MinMaxXY(self.getXY('M5ForTerminationR'))

            self._DesignParameter['M7Input'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL7'][0],
                _Datatype=DesignParameters._LayerMapping['METAL7'][1],
                _XWidth=self.getXWidth('M5ForTerminationR'),
                _YWidth=_TransmissionLineWidth if _TransmissionLineWidth != None else self.getYWidth('M5ForTerminationR'),
                _XYCoordinates=[[MinX_M5Term, (MinY_M5Term + MaxY_M5Term) / 2],
                                [MaxX_M5Term, (MinY_M5Term + MaxY_M5Term) / 2]]
            )


            OverlappedBoundaryForVia6Term = BoundaryCalc.getOverlappedBoundaryElement(
                self._DesignParameter['M6VForIPGate2TerminationR'], self._DesignParameter['M7Input']
            )
            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
                _XWidth=OverlappedBoundaryForVia6Term['_XWidth'],
                _YWidth=OverlappedBoundaryForVia6Term['_YWidth']
            )
            Via6ParamsTerm = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            Via6ParamsTerm['_ViaMet62Met7NumberOfCOX'] = NumViaXYs[0]
            Via6ParamsTerm['_ViaMet62Met7NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via6ForTerminationR'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForTerminationR_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via6ForTerminationR']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(**Via6ParamsTerm)
            self._DesignParameter['Via6ForTerminationR']['_XYCoordinates'] = OverlappedBoundaryForVia6Term['_XYCoordinates']


            # ''' Subring For CMLDriver '''
            # upperYOfSubring = self.getXY('TerminationResistors','_Met1BoundaryOfSubring')[0][1] \
            #                   + self.getYWidth('TerminationResistors','_Met1BoundaryOfSubring') / 2
            # lowerYOfSubring = self.getXY('LoadResistors','_Met1BoundaryOfSubring')[0][1] \
            #                   - self.getYWidth('LoadResistors','_Met1BoundaryOfSubring') / 2
            # centerYOfSubring = self.FloorMinSnapSpacing((upperYOfSubring + lowerYOfSubring) / 2, MinSnapSpacing)
            # halfYWidthOfSubring = self.CeilMinSnapSpacing(
            #     _DesignParameter=max(abs(upperYOfSubring - centerYOfSubring), abs(centerYOfSubring - lowerYOfSubring)),
            #     _MinSnapSpacing=2 * MinSnapSpacing
            # )
            #
            # rightXOfSubring_termR = self.getXY('TerminationResistors','_Met1BoundaryOfSubring')[0][0] \
            #                         + self.getXWidth('TerminationResistors','_Met1BoundaryOfSubring') / 2
            # leftXOfSubring_termR = self.getXY('TerminationResistors','_Met1BoundaryOfSubring')[0][0] \
            #                        - self.getXWidth('TerminationResistors','_Met1BoundaryOfSubring') / 2
            # rightXOfSubring_loadR = self.getXY('LoadResistors','_Met1BoundaryOfSubring')[0][0] \
            #                         + self.getXWidth('LoadResistors','_Met1BoundaryOfSubring') / 2
            # leftXOfSubring_loadR = self.getXY('LoadResistors','_Met1BoundaryOfSubring')[0][0] \
            #                        - self.getXWidth('LoadResistors','_Met1BoundaryOfSubring') / 2
            # halfXWidthOfSubring = self.CeilMinSnapSpacing(
            #     _MinSnapSpacing=2 * MinSnapSpacing,
            #     _DesignParameter=max(abs(rightXOfSubring_termR),
            #                          abs(leftXOfSubring_termR),
            #                          abs(rightXOfSubring_loadR),
            #                          abs(leftXOfSubring_loadR))
            # )
            #
            # SubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
            # SubringInputs['_PType'] = True
            # SubringInputs['_XWidth'] = 2 * (halfXWidthOfSubring + _DRCObj._Metal1MinSpace4)
            # SubringInputs['_YWidth'] = 2 * (halfYWidthOfSubring + _DRCObj._Metal1MinSpace4)
            # SubringInputs['_Width'] = _SubringWidth
            # self._DesignParameter['Subring'] = self._SrefElementDeclaration(
            #     _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='Subring_In{}'.format(_Name)))[0]
            # self._DesignParameter['Subring']['_DesignObj']._CalculatePSubring(**SubringInputs)
            # self._DesignParameter['Subring']['_XYCoordinates'] = [[0, centerYOfSubring]]


        else:
            ''' M5V5M6 For InputGate '''      # Just Copy PMOSSet's Via4
            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
                _XWidth=self.getXWidth('PMOSSet', 'M4V4M5OnPMOSIPGate', '_Met5Layer'),
                _YWidth=self.getYWidth('PMOSSet', 'M4V4M5OnPMOSIPGate', '_Met5Layer')
            )
            Via5Params = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            Via5Params['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
            Via5Params['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via5ForIPGate'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForIPGate_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via5ForIPGate']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**Via5Params)
            self._DesignParameter['Via5ForIPGate']['_XYCoordinates'] = self.getXY('PMOSSet', 'M4V4M5OnPMOSIPGate')

            ''' M6V6M7 InputGate '''
            Via6Params = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            Via6Params['_ViaMet62Met7NumberOfCOX'] = NumViaXYs[0]
            Via6Params['_ViaMet62Met7NumberOfCOY'] = NumViaXYs[1]
            self._DesignParameter['Via6ForIPGate'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForIPGate_In{}'.format(_Name)),
                _XYCoordinates=[])[0]
            self._DesignParameter['Via6ForIPGate']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**Via6Params)
            self._DesignParameter['Via6ForIPGate']['_XYCoordinates'] = self.getXY('Via5ForIPGate')

            ''' M7H For InputGate '''
            self._DesignParameter['M7HForInputGate'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL7'][0],
                _Datatype=DesignParameters._LayerMapping['METAL7'][1],
                _XWidth=None,
                _YWidth=self.getYWidth('Via6ForIPGate', '_Met7Layer'),
                _XYCoordinates=[]
            )

            aa = len(CoordCalc.getSortedList_ascending(self.getXY('Via6ForIPGate'))[0]) // 2
            M7HLeft = CoordCalc.getSortedList_ascending(self.getXY('Via6ForIPGate'))[0][aa]

            M7HRight_1 = CoordCalc.getSortedList_ascending(self.getXY('Via6ForIPGate'))[0][-1]
            M7HRight_2 = _TransmissionLineDistance / 2 if _TransmissionLineDistance != None else 0
            M7HRight = max(M7HRight_1, M7HRight_2)

            self._DesignParameter['M7HForInputGate']['_XWidth'] = M7HRight - M7HLeft

            self._DesignParameter['M7HForInputGate']['_XYCoordinates'] = [
                [+(M7HRight + M7HLeft) / 2, self.getXY('Via6ForIPGate')[0][1]],
                [-(M7HRight + M7HLeft) / 2, self.getXY('Via6ForIPGate')[0][1]],
            ]


            ''' M7Input '''
            self._DesignParameter['M7Input'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL7'][0],
                _Datatype=DesignParameters._LayerMapping['METAL7'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[]
            )
            if _TransmissionLineWidth != None:
                self._DesignParameter['M7Input']['_XWidth'] = _TransmissionLineWidth

                M7InputYDown = self.getXY('M7HForInputGate')[0][1] \
                               - self.getYWidth('M7HForInputGate') / 2
                M7InputYUp = self.getXY('PMOSSet', '_Met1BoundaryOfSubring')[0][1] \
                             + self.getYWidth('PMOSSet', '_Met1BoundaryOfSubring') / 2
                self._DesignParameter['M7Input']['_YWidth'] = M7InputYUp - M7InputYDown

                if _TransmissionLineDistance == None:
                    XCoordOfM7Input = abs(self.getXY('M7HForInputGate')[0][0])
                else:
                    XCoordOfM7Input = _TransmissionLineDistance / 2
                self._DesignParameter['M7Input']['_XYCoordinates'] = [
                    [+XCoordOfM7Input, (M7InputYUp + M7InputYDown) / 2],
                    [-XCoordOfM7Input, (M7InputYUp + M7InputYDown) / 2]
                ]

            else:
                if _TransmissionLineDistance == None:
                    self._DesignParameter['M7Input']['_XWidth'] = self.getXWidth('M7HForInputGate')
                    self._DesignParameter['M7Input']['_YWidth'] = self.getYWidth('M7HForInputGate')
                    self._DesignParameter['M7Input']['_XYCoordinates'] = self.getXY('M7HForInputGate')
                else:
                    self._DesignParameter['M7Input']['_XWidth'] = _DRCObj._MetalxMinWidth
                    self._DesignParameter['M7Input']['_YWidth'] = self.getYWidth('M7HForInputGate')
                    self._DesignParameter['M7Input']['_XYCoordinates'] = [
                        [+_TransmissionLineDistance / 2, self.getXY('M7HForInputGate')[0][1]],
                        [-_TransmissionLineDistance / 2, self.getXY('M7HForInputGate')[0][1]]
                    ]





        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')


if __name__ == '__main__':

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_CmlDriver_2'
    cellname = 'CmlDriver'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _FingerWidthOfInputPair=1000,           # ''' Input Pair '''
        _FingerLengthOfInputPair=30,
        _NumFingerOfInputPair=200,
        _WidthOfMiddleRoutingIP=208,
        _FingerWidthOfCurrentSource=1000,       # ''' Current Source '''
        _FingerLengthOfCurrentSource=30,
        _NumFingerOfCurrentSource=320,
        _WidthOfMiddleRoutingCS=350,

        _XVT='SLVT',
        _SubringWidth=1000,

        # ''' Load R '''
        _ResWidth_LoadR=3000,
        _ResLength_LoadR=2300,
        _NumCOY_LoadR=4,
        _NumRows_LoadR=2,
        _NumStripes_LoadR=5,
        _RoutingWidth_LoadR=None,
        _Dummy_LoadR=True,
        _SubringWidth_LoadR=1000,

        # ''' Termination R  '''
        _TerminationR=True,                    # True | False
        _ResWidth_TerminationR=3000,
        _ResLength_TerminationR=2300,
        _NumCOY_TerminationR=4,
        _NumRows_TerminationR=2,
        _NumStripes_TerminationR=5,
        _RoutingWidth_TerminationR=None,
        _Dummy_TerminationR=True,
        _SubringWidth_TerminationR=1000,

        # TransmissionLine
        _TransmissionLineWidth=4000,            # None | 4000
        _TransmissionLineDistance=32000,        # Default(None) : Calculated as Center Of LoadResistor | normal : 32000
    )


    Mode_DRCCheck = False       # True | False
    Num_DRCCheck = 10
    start_time = time.time()
    
    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''
            InputParams['_ResWidth_LoadR'] = DRCchecker.RandomParam(start=1000, stop=5000, step=100)
            InputParams['_ResLength_LoadR'] = DRCchecker.RandomParam(start=400, stop=5000, step=100)
            InputParams['_NumCOY_LoadR'] = DRCchecker.RandomParam(start=2, stop=5, step=1)
            InputParams['_NumRows_LoadR'] = DRCchecker.RandomParam(start=1, stop=4, step=1)
            InputParams['_NumStripes_LoadR'] = DRCchecker.RandomParam(start=2, stop=10, step=1)
        else:
            pass

        print("   Layout Object's Input Parameters are   ".center(105, '='))
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("".center(105, '='))

        ''' Generate Layout Object '''
        LayoutObj = CmlLDriver(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

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
            print(f'DRC checking... ({ii + 1}/{Num_DRCCheck})')

            try:
                Checker.DRCchecker()
            except Exception as e:
                print('Error Occurred: ', e)
                print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                print(tmpStr)
                print(''.center(105, '='))
                m, s = divmod(time.time() - start_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\nErrMsg : {e}\n'
                             f'**InputParameters:\n'
                             f'{tmpStr}\n'
                             f'****************************'
                             f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
            else:
                if (ii + 1) == Num_DRCCheck:
                    elapsed_time = time.time() - start_time
                    m, s = divmod(elapsed_time, 60)
                    h, m = divmod(m, 60)
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number of Run: {Num_DRCCheck}\n'
                                 f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
                else:
                    pass
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

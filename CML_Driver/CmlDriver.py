import math
import copy
import warnings

#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from Private import MyInfo
import CoordCalc

#
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
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
        _SubringWidth_LoadR=None
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
                                  _SubringWidth_TerminationR=None
                                  ):

        _DRCObj = DRC.DRC()
        _Name = 'CmlDriver'
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        ''' PMOSSet Generation '''
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


        ''' Output Load Resistor Set Generation '''
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
        self._DesignParameter['LoadResistors']['_XYCoordinates'] = [[0, -10000]]


        ''' Termination Resistor Set Generation '''
        if _TerminationR:
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
            self._DesignParameter['TerminationResistors']['_XYCoordinates'] = [[0, 15000]]
        else:
            pass
        print('test')


if __name__ == '__main__':

    libname = 'TEST_CmlDriver'
    cellname = 'CmlDriver'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _FingerWidthOfInputPair=1000,           # ''' Input Pair '''
        _FingerLengthOfInputPair=30,
        _NumFingerOfInputPair=200,
        _WidthOfMiddleRoutingIP=200,
        _FingerWidthOfCurrentSource=1000,       # ''' Current Source '''
        _FingerLengthOfCurrentSource=30,
        _NumFingerOfCurrentSource=320,
        _WidthOfMiddleRoutingCS=350,

        _XVT='SLVT',
        _SubringWidth=1000,

        _ResWidth_LoadR=3000,                   # ''' Load R '''
        _ResLength_LoadR=2300,
        _NumCOY_LoadR=4,
        _NumRows_LoadR=2,
        _NumStripes_LoadR=5,
        _RoutingWidth_LoadR=None,
        _Dummy_LoadR=True,
        _SubringWidth_LoadR=1000,

        _TerminationR=True,                     # ''' Termination R  '''
        _ResWidth_TerminationR=3000,
        _ResLength_TerminationR=2300,
        _NumCOY_TerminationR=4,
        _NumRows_TerminationR=2,
        _NumStripes_TerminationR=5,
        _RoutingWidth_TerminationR=None,
        _Dummy_TerminationR=True,
        _SubringWidth_TerminationR=1000,
    )


    Mode_DRCCheck = False            # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''
            InputParams['_ResWidth_LoadR'] = DRCchecker.RandomParam(start=1000, stop=5000, step=100)
            InputParams['_ResLength_LoadR'] = DRCchecker.RandomParam(start=400, stop=5000, step=100)
            InputParams['_NumCOY_LoadR'] = DRCchecker.RandomParam(start=1, stop=5, step=1)
            InputParams['_NumRows_LoadR'] = DRCchecker.RandomParam(start=1, stop=5, step=1)
            InputParams['_NumStripes_LoadR'] = DRCchecker.RandomParam(start=1, stop=10, step=1)
        else:
            pass

        ''' Generate Layout Object '''
        LayoutObj = CmlLDriver(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print ('##################################      Sending to FTP Server...      ##################################')
        My = MyInfo.USER(DesignParameters._Technology)
        Checker = DRCchecker.DRCchecker(
            username=My.ID,
            password=My.PW,
            WorkDir=My.Dir_Work,
            DRCrunDir=My.Dir_DRCrun,
            libname=libname,
            cellname=cellname,
        )
        Checker.Upload2FTP()

        if Mode_DRCCheck:
            print ('###############      DRC checking... {0}/{1}      ##################'.format(ii + 1, Num_DRCCheck))
            Checker.DRCchecker_PrintInputParams(InputParams)
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print ('########################################      Finished       ###########################################')
# end of 'main():' ---------------------------------------------------------------------------------------------

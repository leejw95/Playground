import math
import copy
import random
import warnings
#
import StickDiagram
import DesignParameters
import DRC
from Private import FileManage
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
    warnings.warn('fff')
    ''' Input Parameters for Layout Object '''
    _FingerWidthOfInputPair = 1000
    _FingerLengthOfInputPair = 30
    _NumFingerOfInputPair = 200
    _WidthOfMiddleRoutingIP = 200

    _FingerWidthOfCurrentSource = 1000
    _FingerLengthOfCurrentSource = 40
    _NumFingerOfCurrentSource = 320
    _WidthOfMiddleRoutingCS = 350

    _XVT = 'SLVT'
    _SubringWidth = 1000

    ''' Load R  '''
    _ResWidth_LoadR = 3000
    _ResLength_LoadR = 2300
    _NumCOY_LoadR = 4
    _NumRows_LoadR = 2
    _NumStripes_LoadR = 5
    _RoutingWidth_LoadR = None
    _Dummy_LoadR = True
    _SubringWidth_LoadR = 1000

    ''' Termination R  '''
    _TerminationR = True
    _ResWidth_TerminationR = 3000
    _ResLength_TerminationR = 2300
    _NumCOY_TerminationR = 4
    _NumRows_TerminationR = 2
    _NumStripes_TerminationR = 5
    _RoutingWidth_TerminationR = None
    _Dummy_TerminationR = True
    _SubringWidth_TerminationR = 1000


    # for tries in range(0, 100):
    #     ''' Input Parameters for Layout Object '''
    #     _FingerWidthOfInputPair = FileManage.RandomParam(start=400, stop=1000, step=100)
    #     _FingerLengthOfInputPair = FileManage.RandomParam(start=30, stop=60, step=10)
    #     _NumFingerOfInputPair = FileManage.RandomParam(start=30, stop=300, step=2)
    #     _WidthOfMiddleRoutingIP = FileManage.RandomParam(start=100, stop=500, step=10)
    #
    #     _FingerWidthOfCurrentSource = FileManage.RandomParam(start=400, stop=1000, step=100)
    #     _FingerLengthOfCurrentSource = FileManage.RandomParam(start=30, stop=60, step=10)
    #     _NumFingerOfCurrentSource = FileManage.RandomParam(start=30, stop=500, step=2)
    #     _WidthOfMiddleRoutingCS = FileManage.RandomParam(start=100, stop=500, step=10)
    #
    #     _XVT = 'SLVT'
    #     _SubringWidth = 1000
    #
    #     print ('###############      DRC checking... {}/100      ##################'.format(tries + 1))
    #     print ('_FingerWidthOfInputPair : {}',format(_FingerWidthOfInputPair))
    #     print ('_FingerLengthOfInputPair : {}',format(_FingerLengthOfInputPair))
    #     print ('_NumFingerOfInputPair : {}',format(_NumFingerOfInputPair))
    #     print ('_WidthOfMiddleRoutingIP : {}',format(_WidthOfMiddleRoutingIP))
    #     print ('_FingerWidthOfCurrentSource : {}',format(_FingerWidthOfCurrentSource))
    #     print ('_FingerLengthOfCurrentSource : {}',format(_FingerLengthOfCurrentSource))
    #     print ('_NumFingerOfCurrentSource : {}',format(_NumFingerOfCurrentSource))
    #     print ('_WidthOfMiddleRoutingCS : {}',format(_WidthOfMiddleRoutingCS))

    # Generate Layout Object
    LayoutObj = CmlLDriver(_Name=cellname)
    LayoutObj._CalculateDesignParameter(_FingerWidthOfInputPair=_FingerWidthOfInputPair,
                                        _FingerLengthOfInputPair=_FingerLengthOfInputPair,
                                        _NumFingerOfInputPair=_NumFingerOfInputPair,
                                        _FingerWidthOfCurrentSource=_FingerWidthOfCurrentSource,
                                        _FingerLengthOfCurrentSource=_FingerLengthOfCurrentSource,
                                        _NumFingerOfCurrentSource=_NumFingerOfCurrentSource,
                                        _WidthOfMiddleRoutingIP=_WidthOfMiddleRoutingIP,
                                        _WidthOfMiddleRoutingCS=_WidthOfMiddleRoutingCS,
                                        _XVT=_XVT,
                                        _SubringWidth=_SubringWidth,
                                        _ResWidth_LoadR=_ResWidth_LoadR,
                                        _ResLength_LoadR=_ResLength_LoadR,
                                        _NumCOY_LoadR=_NumCOY_LoadR,
                                        _NumRows_LoadR=_NumRows_LoadR,
                                        _NumStripes_LoadR=_NumStripes_LoadR,
                                        _RoutingWidth_LoadR=_RoutingWidth_LoadR,
                                        _Dummy_LoadR=_Dummy_LoadR,
                                        _SubringWidth_LoadR=_SubringWidth_LoadR,
                                        _TerminationR=_TerminationR,
                                        _ResWidth_TerminationR=_ResWidth_TerminationR,
                                        _ResLength_TerminationR=_ResLength_TerminationR,
                                        _NumCOY_TerminationR=_NumCOY_TerminationR,
                                        _NumRows_TerminationR=_NumRows_TerminationR,
                                        _NumStripes_TerminationR=_NumStripes_TerminationR,
                                        _RoutingWidth_TerminationR=_RoutingWidth_TerminationR,
                                        _Dummy_TerminationR=_Dummy_TerminationR,
                                        _SubringWidth_TerminationR=_SubringWidth_TerminationR,
                                        )
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
        # directory=My.Dir_Work,
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
    # print ('###############      Checking DRC...      ##################')
    # import DRCchecker
    # a = DRCchecker.DRCchecker(
    #     username=My.ID,
    #     password=My.PW,
    #     WorkDir=My.Dir_Work,
    #     DRCrunDir=My.Dir_DRCrun,
    #     libname=libname,
    #     cellname=cellname,
    # )
    # a.DRCchecker()

    print ('###############      Finished      ##################')
# end of 'main():' ---------------------------------------------------------------------------------------------
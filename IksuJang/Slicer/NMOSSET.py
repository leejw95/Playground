import StickDiagram
import DesignParameters
import copy
import DRC
from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import PSubRing


class NMOSSET(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='NMOSSET'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger_NM1=8,
                                  NumFinger_NM23=12,
                                  NumFinger_NM45=2,
                                  Width_NM1=1000,
                                  Width_NM23=1000,
                                  Width_NM45=1000,

                                  ChannelLength=30,
                                  XVT='SLVT',

                                  NumContact_NM1=1,
                                  NumContact_NM23=2,
                                  NumContact_NM45=1,
                                  NumContact_Subring=2
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        print('\n' + ''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')

        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['NM1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM23, _NMOSChannelWidth=Width_NM23, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM3In{}'.format(_Name)))[0]
        self._DesignParameter['NM3']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM23, _NMOSChannelWidth=Width_NM23, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM4'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM4In{}'.format(_Name)))[0]
        self._DesignParameter['NM4']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM45, _NMOSChannelWidth=Width_NM45, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM5'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM5In{}'.format(_Name)))[0]
        self._DesignParameter['NM5']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM45, _NMOSChannelWidth=Width_NM45, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))

        self._DesignParameter['NM1']['_XYCoordinates'] = [[0,-1000]]
        self._DesignParameter['NM2']['_XYCoordinates'] = [[-2500,0]]
        self._DesignParameter['NM3']['_XYCoordinates'] = [[2500,0]]
        self._DesignParameter['NM4']['_XYCoordinates'] = [[-500,0]]
        self._DesignParameter['NM5']['_XYCoordinates'] = [[500,0]]



        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')
        ''' -------------------------------------------------------------------------------------------------------- '''


if __name__ == '__main__':
    from Private import MyInfo
    import DRCchecker
    from SthPack import PlaygroundBot

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_Slicer'
    cellname = 'NMOSSET'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        NumFinger_NM1=8,
        NumFinger_NM23=12,
        NumFinger_NM45=2,
        Width_NM1=1000,
        Width_NM23=1000,
        Width_NM45=1000,

        ChannelLength=30,
        XVT='SLVT',

        NumContact_NM1=1,
        NumContact_NM23=2,
        NumContact_NM45=1,
        NumContact_Subring=2
    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass
        print("=============================   Last Layout Object's Input Parameters are   ===========================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("=======================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = NMOSSET(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('##################################      Sending to FTP Server...      #################################')
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

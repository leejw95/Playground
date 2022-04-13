import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc


from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4



class Resistor(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Resistor'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,

                                  Width_Res=1250,
                                  Length_Res=1234,
                                  NumContactY_Res=2,                    # option

                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print('\n' + ''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')


        ''' -------------------------------------------------------------------------------------------------------- '''

        ''' -------------------------------------------------------------------------------------------------------- '''
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

    libname = 'TEST_Resistor'
    cellname = 'Resistor'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        Width_Res=1250,
        Length_Res=1234,
        NumContactY_Res=2,           # option

    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass
        print("=============================   Last Layout Object's Input Parameters are   ==========================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("======================================================================================================")

        ''' Generate Layout Object '''
        LayoutObj = Resistor(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#################################      Sending to FTP Server...      #################################')
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
                tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
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

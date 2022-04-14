import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc


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

        NumContactY_Res = NumContactY_Res if NumContactY_Res is not None else 2

        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['_OPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1],
            _XWidth=Width_Res + _DRCObj._OPlayeroverPoly * 2,
            _YWidth=Length_Res,
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=Width_Res,
            _YWidth=Length_Res + _DRCObj._PolyoverOPlayer * 2,
            _XYCoordinates=[[0, 0]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
            _XWidth=_DRCObj._CoMinWidth,
            _YWidth=_DRCObj._CoMinWidth
        )

        NumContactX_Res = int((self.getXWidth('_POLayer') - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)

        tmpXYs = []
        originX = - (NumContactX_Res - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) / 2
        originY = self.getXYTop('_OPLayer')[0][1] + _DRCObj._CoMinSpace2OP + self.getYWidth('_COLayer') / 2
        for i in range(0, NumContactY_Res):
            for j in range(0, NumContactX_Res):
                tmpXYs.append([originX + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                               originY + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                tmpXYs.append([originX + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                               -originY - i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['_Met1LayerA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(NumContactX_Res - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2,
            _YWidth=(NumContactY_Res - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        )
        self._DesignParameter['_Met1LayerA']['_XYCoordinates'] = [
            [0, self.getXYTop('_OPLayer')[0][1] + _DRCObj._CoMinSpace2OP - _DRCObj._Metal1MinEnclosureCO3 + self.getYWidth('_Met1LayerA') / 2]
        ]
        self._DesignParameter['_Met1LayerB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(NumContactX_Res - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2,
            _YWidth=(NumContactY_Res - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        )
        self._DesignParameter['_Met1LayerB']['_XYCoordinates'] = [
            [0, -self.getXY('_Met1LayerA')[0][1]]
        ]




        ''' -------------------------------------------------------------------------------------------------------- '''

        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXYTop('_COLayer'))[0][1] + _DRCObj._CoMinEnclosureByPO2
        if topBoundary > self.getXYTop('_POLayer')[0][1]:
            self._DesignParameter['_POLayer']['_YWidth'] = topBoundary * 2

        else:
            pass


        self._DesignParameter['_PRESLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1],
            _XWidth=self.getXWidth('_POLayer') + _DRCObj._PRESlayeroverPoly * 2,
            _YWidth=self.getYWidth('_POLayer') + _DRCObj._PRESlayeroverPoly * 2,
            _XYCoordinates=[[0, 0]]
        )

        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=self.getXWidth('_PRESLayer'),
            _YWidth=self.getYWidth('_PRESLayer'),
            _XYCoordinates=self.getXY('_PRESLayer')
        )

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
        NumContactY_Res=4,           # option

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

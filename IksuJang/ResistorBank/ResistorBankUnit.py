import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc

from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import PSubRing

from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from IksuJang.BasicArchive import ViaMet42Met5
from IksuJang.BasicArchive import ViaMet52Met6

from IksuJang.ResistorBank import TransmissionGate
from IksuJang.ResistorBank import Resistor


class ResistorBankUnit(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='ResistorBankUnit'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger=10,
                                  Width_PM=540,
                                  Width_NM=270,

                                  Width_Res=1250,
                                  Length_Res=1234,

                                  NumContactY_Gate=1,                   # option
                                  NumContactY_innerSubring=2,           # option
                                  NumContactY_outerSubring=2,           # option
                                  NumContactY_Res=2,                    # option

                                  ChannelLength=30,
                                  XVT='SLVT',
                                  _GateSpacing=None
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print('\n' + ''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')

        # UnitPitch
        _UnitPitch = _GateSpacing + ChannelLength if _GateSpacing else _DRCObj._PolygateMinSpace + ChannelLength


        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['TransmissionGate'] = self._SrefElementDeclaration(_DesignObj=TransmissionGate.TransmissionGate(_Name='TGIn{}'.format(_Name)))[0]
        self._DesignParameter['TransmissionGate']['_DesignObj']._CalculateDesignParameter(
            **dict(NumFinger=NumFinger, Width_PM=Width_PM, Width_NM=Width_NM,
                   NumContactY_Gate=NumContactY_Gate, NumContactY_innerSubring=NumContactY_innerSubring,
                   ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing))
        self._DesignParameter['TransmissionGate']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['Resistor'] = self._SrefElementDeclaration(_DesignObj=Resistor.Resistor(_Name='ResIn{}'.format(_Name)))[0]
        self._DesignParameter['Resistor']['_DesignObj']._CalculateDesignParameter(
            **dict(Width_Res=Width_Res, Length_Res=Length_Res, NumContactY_Res=NumContactY_Res))
        self._DesignParameter['Resistor']['_XYCoordinates'] = [[0, 0]]


        #
        YCoord_resistor_reCalc = self.getXYTop('TransmissionGate', 'M3HOnPMSource')[0][1] - self.getXYTop('Resistor', '_Met1LayerA')[0][1]

        leftBoundary_PRES_reCalc1 = self.getXYRight('TransmissionGate', 'PSubring', 'right', '_ODLayer')[0][0] + _DRCObj._RXMinSpacetoPRES
        leftBoundary_PRES_reCalc2 = self.getXYRight('TransmissionGate', 'NSubring', 'right', '_ODLayer')[0][0] + _DRCObj._RXMinSpacetoPRES
        leftBoundary_PRES_reCalc = max(leftBoundary_PRES_reCalc1, leftBoundary_PRES_reCalc2)
        XCoord_resistor_reCalc = leftBoundary_PRES_reCalc - self.getXYLeft('Resistor', '_PRESLayer')[0][0]

        self._DesignParameter['Resistor']['_XYCoordinates'] = [[XCoord_resistor_reCalc, YCoord_resistor_reCalc]]


        ''' -------------------------------------------------------------------------------------------------------- '''
        # PSubring
        self._DesignParameter['PSubring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=1000, width=1000, contact=NumContactY_outerSubring))

        _topBoundary1 = self.getXYTop('TransmissionGate', 'NSubring', 'met_top')[0][1] + _DRCObj._Metal1DefaultSpace + self.getYWidth('PSubring', 'met_top') / 2
        _topBoundary2 = self.getXYTop('Resistor', '_PRESLayer')[0][1] + _DRCObj._RXMinSpacetoPRES + self.getYWidth('PSubring', 'met_top') / 2
        _topBoundary3 = self.getXYTop('TransmissionGate', 'NSubring', 'nw_top')[0][1] + _DRCObj._NwMinEnclosurePactive + self.getYWidth('PSubring', 'top', '_ODLayer') / 2
        _topBoundary = max(_topBoundary1, _topBoundary2, _topBoundary3)

        _botBoundary1 = self.getXYBot('TransmissionGate', 'PSubring', 'met_bot')[0][1] - _DRCObj._Metal1DefaultSpace - self.getYWidth('PSubring', 'met_bot') / 2
        _botBoundary2 = self.getXYBot('Resistor', '_PRESLayer')[0][1] - _DRCObj._RXMinSpacetoPRES - self.getYWidth('PSubring', 'met_bot') / 2
        _botBoundary = min(_botBoundary1, _botBoundary2)

        _rightBoundary = self.getXYRight('Resistor', '_PRESLayer')[0][0] + _DRCObj._RXMinSpacetoPRES + self.getXWidth('PSubring', 'met_right') / 2

        _leftBoundary1 = self.getXYLeft('TransmissionGate', 'PSubring', 'met_left')[0][0] - _DRCObj._Metal1DefaultSpace - self.getXWidth('PSubring', 'met_right') / 2
        _leftBoundary2 = self.getXYLeft('TransmissionGate', 'PSubring', 'left', '_PPLayer')[0][0] - _DRCObj._PpMinSpace - self.getXWidth('PSubring', 'left', '_PPLayer') / 2
        _leftBoundary3 = self.getXYLeft('TransmissionGate', 'NSubring', 'nw_left')[0][0] - _DRCObj._NwMinEnclosurePactive - self.getXWidth('PSubring', 'left', '_ODLayer') / 2
        _leftBoundary = min(_leftBoundary1, _leftBoundary2, _leftBoundary3)

        topBoundary = self.CeilMinSnapSpacing(_topBoundary, MinSnapSpacing * 2)
        botBoundary = self.FloorMinSnapSpacing(_botBoundary, MinSnapSpacing * 2)
        rightBoundary = self.CeilMinSnapSpacing(_rightBoundary, MinSnapSpacing * 2)
        leftBoundary = self.FloorMinSnapSpacing(_leftBoundary, MinSnapSpacing * 2)

        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(width=rightBoundary - leftBoundary,
                   height=topBoundary - botBoundary,
                   contact=NumContactY_outerSubring))
        self._DesignParameter['PSubring']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]
        ]


        topBoundary = self.getXYTop('TransmissionGate', 'PSubring', 'met_bot')[0][1]
        botBoundary = self.getXYBot('PSubring', 'met_bot')[0][1]
        self._DesignParameter['M1V_subringshort'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('TransmissionGate', 'PSubring', 'met_bot'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [self.getXY('TransmissionGate', 'PSubring', 'met_bot')[0][0], (topBoundary + botBoundary) / 2]
            ]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = self.getXYRight('Resistor', '_Met1LayerA')[0][0]
        leftBoundary = self.getXYLeft('TransmissionGate', 'M2VOnSource')[0][0]
        self._DesignParameter['M3H'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TransmissionGate', 'M3HOnPMSource'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('TransmissionGate', 'M3HOnPMSource')[0][1]]
            ]
        )

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('Resistor', '_Met1LayerA'),
                                                                       YWidth=self.getYWidth('M3H'))
        self._DesignParameter['Via2ForA'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForAIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForA']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForA']['_XYCoordinates'] = [[self.getXY('Resistor', '_Met1LayerA')[0][0], self.getXY('M3H')[0][1]]]

        self._DesignParameter['Via1ForA'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForAIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForA']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXYs[0], _ViaMet12Met2NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via1ForA']['_XYCoordinates'] = self.getXY('Via2ForA')

        ''' -------------------------------------------------------------------------------------------------------- '''
        try:
            NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
                XWidth=self.getXWidth('Resistor', '_Met1LayerB'),
                YWidth=self.getYWidth('Resistor', '_Met1LayerB'))
            if NumViaXYs[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXYs = (NumViaXYs[0], 2)

        self._DesignParameter['Via1ForB'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForBIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForB']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXYs[0], _ViaMet12Met2NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via1ForB']['_XYCoordinates'] = [
            [self.getXY('Resistor', '_Met1LayerB')[0][0],
             self.getXYTop('Resistor', '_Met1LayerB')[0][1] - self.getYWidth('Via1ForB', '_Met1Layer') / 2]
        ]
        self._DesignParameter['Via2ForB'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForBIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForB']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForB']['_XYCoordinates'] = self.getXY('Via1ForB')

        self._DesignParameter['Via3ForB'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForBIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForB']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForB']['_XYCoordinates'] = self.getXY('Via1ForB')

        self._DesignParameter['Via4ForB'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForBIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForB']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForB']['_XYCoordinates'] = self.getXY('Via1ForB')

        self._DesignParameter['Via5ForB'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForBIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForB']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXYs[0], _ViaMet52Met6NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via5ForB']['_XYCoordinates'] = self.getXY('Via1ForB')
        ''' -------------------------------------------------------------------------------------------------------- '''


        rightBoundary = self.getXYRight('TransmissionGate', 'Via4OnNMGate', '_Met5Layer')[0][0]
        leftBoundary = self.getXY('PSubring', 'met_left')[0][0]
        self._DesignParameter['M5H_S'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TransmissionGate', 'Via4OnNMGate', '_Met5Layer'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('TransmissionGate', 'Via4OnNMGate')[0][1]]
            ]
        )
        self._DesignParameter['M5H_SB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('TransmissionGate', 'Via4OnPMGate', '_Met5Layer'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('TransmissionGate', 'Via4OnPMGate')[0][1]]
            ]
        )

        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXY('M1V_subringshort'),
            _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('TransmissionGate', 'Via2ForVDD'),
            _Mag=0.04, _TEXT='VDD')

        self._DesignParameter['PIN_S'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('M5H_S'),
            _Mag=0.04, _TEXT='S')
        self._DesignParameter['PIN_SB'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('M5H_SB'),
            _Mag=0.04, _TEXT='SB')

        self._DesignParameter['PIN_VCM'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('TransmissionGate', 'M4_VCM'),
            _Mag=0.04, _TEXT='VCM')
        self._DesignParameter['PIN_VRX'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('Via5ForB'),
            _Mag=0.04, _TEXT='VRX')


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

    libname = 'TEST_ResistorBankUnit'
    cellname = 'ResistorBankUnit'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        NumFinger=8,
        Width_PM=550,
        Width_NM=274,

        Width_Res=1250,
        Length_Res=1234,

        NumContactY_Gate=1,          # option
        NumContactY_innerSubring=2,  # option
        NumContactY_outerSubring=2,  # option
        NumContactY_Res=2,           # option

        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
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
        LayoutObj = ResistorBankUnit(_Name=cellname)
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

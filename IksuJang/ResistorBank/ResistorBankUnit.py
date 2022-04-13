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

from IksuJang.ResistorBank import TransmissionGate
from IksuJang.ResistorBank import PolyResistor


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
                                  NumContactY_innerSubring=1,           # option
                                  NumContactY_outerSubring=1,           # option
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
        # NMOS, PMOS
        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger, _NMOSChannelWidth=Width_NM, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger, _PMOSChannelWidth=Width_PM, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, 0]]  # Temporal Setting, ReCalculated Later...
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, 0]]  # Temporal Setting, ReCalculated Later...

        # Supply Rail





        ''' --------------------------------------------- NWELL Layer ---------------------------------------------- '''

        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        # self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
        #     _XYCoordinates=self.getXY('VSSRail'),
        #     _Mag=0.04,  _TEXT='VSS')
        # self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
        #     _XYCoordinates=self.getXY('VDDRail'),
        #     _Mag=0.04, _TEXT='VDD')
        #
        # self._DesignParameter['PIN_S'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
        #     _XYCoordinates=[self.getXY('M3H_Input')[0]],
        #     _Mag=0.04, _TEXT='S')
        # self._DesignParameter['PIN_SB'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
        #     _XYCoordinates=[self.getXY('M2V')[0]],
        #     _Mag=0.04, _TEXT='SB')
        #
        # self._DesignParameter['PIN_VCM'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL4PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
        #     _XYCoordinates=[self.getXY('M2V')[0]],
        #     _Mag=0.04, _TEXT='VCM')
        # self._DesignParameter['PIN_VRX'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
        #     _XYCoordinates=[self.getXY('M2V')[0]],
        #     _Mag=0.04, _TEXT='VRX')


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
        NumContactY_innerSubring=1,  # option
        NumContactY_outerSubring=1,  # option
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

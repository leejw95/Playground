import math
import copy

#
import StickDiagram
import DesignParameters
import DRC

#
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
from Onesemicon import SupplyRail, ViaPoly2Met1_width

import ViaPoly2Met1
import ViaMet12Met2

#
from SthPack import CoordCalc


class TristateInverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ChannelWidth=200,
                                           _ChannelLength=30,
                                           _NPRatio=2,
                                           _XVT='SLVT',
                                           _DistanceBtwFinger=130,
                                           _Dummy=True,

                                           _VDD2VSSHeight=1800,
                                           _VDD2PMOSHeight=None,
                                           _VSS2NMOSHeight=None,
                                           )

    def __init__(self, _DesignParameter=None, _Name='TristateInverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                Met1YSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                _XYCoordinates=[], _Width=400),

                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

    def _CalculateDesignParameter(self,
                                  _ChannelWidth=None,
                                  _ChannelLength=None,
                                  _NPRatio=None,
                                  _XVT=None,
                                  _DistanceBtwFinger=None,
                                  _Dummy=None,

                                  _VDD2VSSHeight=None,
                                  _VDD2PMOSHeight=None,
                                  _VSS2NMOSHeight=None,
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print(''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))

        _Finger = 2
        Pitch = _DistanceBtwFinger

        YCoordOfPIN_EN = 650
        YCoordOfPIN_ENb = 950
        YCoordOfPIN_A = 750

        ''' ------------------------------------------ MOSFET Generation ------------------------------------------- '''
        # 1) Cascode NMOS Generation -----------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_XVT'] = _XVT
        NMOSparameters['_DistanceBtwFinger'] = _DistanceBtwFinger

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, 0]]

        # Delete middle metal1 layer and contact
        XYCoordOfNMOSDrain = CoordCalc.getXYCoords_MinX(self.getXY('_NMOS', '_Met1Layer'))
        XYCoordOfNMOSSource = CoordCalc.getXYCoords_MaxX(self.getXY('_NMOS', '_Met1Layer'))
        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'] = \
            XYCoordOfNMOSDrain + XYCoordOfNMOSSource
        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'] = \
            CoordCalc.getXYCoords_MinX(self.getXY('_NMOS', '_COLayer')) \
            + CoordCalc.getXYCoords_MaxX(self.getXY('_NMOS', '_COLayer'))
        del self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_METAL1PINDrawing']
        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = XYCoordOfNMOSSource
        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = XYCoordOfNMOSDrain

        # 2) Cascode PMOS Generation ------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = self.FloorMinSnapSpacing(_ChannelWidth * _NPRatio, 2*MinSnapSpacing)
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT
        PMOSparameters['_DistanceBtwFinger'] = _DistanceBtwFinger

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(
            _DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, 0]]

        # Delete middle metal1 layer and contact
        XYCoordOfPMOSDrain = CoordCalc.getXYCoords_MinX(self.getXY('_PMOS', '_Met1Layer'))
        XYCoordOfPMOSSource = CoordCalc.getXYCoords_MaxX(self.getXY('_PMOS', '_Met1Layer'))
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'] = \
            XYCoordOfPMOSDrain + XYCoordOfPMOSSource
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'] = \
            CoordCalc.getXYCoords_MinX(self.getXY('_PMOS', '_COLayer')) \
            + CoordCalc.getXYCoords_MaxX(self.getXY('_PMOS', '_COLayer'))
        del self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_METAL1PINDrawing']
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = XYCoordOfPMOSSource
        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = XYCoordOfPMOSDrain


        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        PbodyParams = copy.deepcopy(SupplyRail.SupplyRail._ParametersForDesignCalculation)
        PbodyParams.update({'NumPitch': _Finger + 1, 'isPbody': True})
        self._DesignParameter['SupplyRail_VSS'] = self._SrefElementDeclaration(
            _DesignObj=SupplyRail.SupplyRail(_DesignParameter=None, _Name='Pbody_In{}'.format(_Name)))[0]
        self._DesignParameter['SupplyRail_VSS']['_DesignObj']._CalculateDesignParameter(**PbodyParams)
        self._DesignParameter['SupplyRail_VSS']['_XYCoordinates'] = [[0,0]]

        NbodyParams = copy.deepcopy(SupplyRail.SupplyRail._ParametersForDesignCalculation)
        NbodyParams.update({'NumPitch': _Finger + 1, 'isPbody': False})
        self._DesignParameter['SupplyRail_VDD'] = self._SrefElementDeclaration(
            _DesignObj=SupplyRail.SupplyRail(_DesignParameter=None, _Name='Nbody_In{}'.format(_Name)))[0]
        self._DesignParameter['SupplyRail_VDD']['_DesignObj']._CalculateDesignParameter(**NbodyParams)
        self._DesignParameter['SupplyRail_VDD']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, _VSS2NMOSHeight]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, _VDD2VSSHeight - _VDD2PMOSHeight]]



        ''' Input Contact(PCCOM1) Generation '''
        ViaParams = copy.deepcopy(ViaPoly2Met1_width._ViaPoly2Met1_width._ParametersForDesignCalculation)
        ViaParams.update({
            '_ViaPoly2Met1NumberOfCOX': 1, '_ViaPoly2Met1NumberOfCOY': 2,
            'Met1XWidth': 66, 'Met1YWidth': 200,
            'POXWidth': 40, 'POYWidth': 200
        })
        self._DesignParameter['Via0'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1_width._ViaPoly2Met1_width(_Name='Via0_In{}'.format(_Name)))[0]
        self._DesignParameter['Via0']['_DesignObj']._ClaculateDesignParameter(**ViaParams)
        self._DesignParameter['Via0']['_XYCoordinates'] = [
            [+Pitch, YCoordOfPIN_A], [-Pitch, YCoordOfPIN_EN], [-Pitch, YCoordOfPIN_ENb]
        ]


        ''' ------------------------------------ Supply Routing (VSS / VDD) ---------------------------------------- '''
        # Met1Width = _DRCObj._Metal1MinWidth
        Met1Width = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3

        test = self.getXYwtBoudary('down', 'SupplyRail_VDD', '_Met1Layer')
        Path_VDD2PMOSSource = [[
            CoordCalc.Add(self.getXY('_PMOS', '_XYCoordinatePMOSSupplyRouting')[0], [0, -self.getYWidth('_PMOS', '_Met1Layer')/2]),
            [self.getXY('_PMOS', '_XYCoordinatePMOSSupplyRouting')[0][0], self.getXYwtBoudary('up', 'SupplyRail_VDD', '_Met1Layer')[0][1]]
        ]]
        Path_VSS2NMOSSource = [[
            CoordCalc.Add(self.getXY('_NMOS', '_XYCoordinateNMOSSupplyRouting')[0], [0, +self.getYWidth('_NMOS', '_Met1Layer') / 2]),
            [self.getXY('_NMOS', '_XYCoordinateNMOSSupplyRouting')[0][0], self.getXYwtBoudary('down', 'SupplyRail_VSS', '_Met1Layer')[0][1]]
        ]]
        self._DesignParameter['Met1YSupplyRouting']['_Width'] = Met1Width
        self._DesignParameter['Met1YSupplyRouting']['_XYCoordinates'] = Path_VDD2PMOSSource + Path_VSS2NMOSSource

        ''' --------------------------------------- Polygate Routing ----------------------------------------------- '''










        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))





if __name__ == '__main__':
    from Private import MyInfo
    from SthPack import PlaygroundBot
    import DRCchecker

    libname = 'Test_TristateInverter'
    cellname = 'TristateInverter_1'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = copy.deepcopy(TristateInverter._ParametersForDesignCalculation)
    InputParams.update({
        '_ChannelWidth':250,
        '_DistanceBtwFinger':130,
        '_VDD2PMOSHeight':400,
        '_VSS2NMOSHeight':275,
    })

    Mode_DRCCheck = False            # True | False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        # if Mode_DRCCheck:
        #     ''' Input Parameters for Layout Object '''
        #     InputParams['_Finger'] = DRCchecker.RandomParam(start=2, stop=20, step=1)               # DRCchecker.RandomParam(start=2, stop=20, step=1)
        #     InputParams['_ChannelWidth'] = DRCchecker.RandomParam(start=400, stop=1000, step=2)     # DRCchecker.RandomParam(start=200, stop=1000, step=2)
        #     InputParams['_ChannelLength'] = DRCchecker.RandomParam(start=10, stop=20, step=2)
        # else:
        #     pass

        ''' Generate Layout Object '''
        LayoutObj = TristateInverter(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)

        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('###############      Sending to FTP Server...      ##################')
        My = MyInfo.USER(DesignParameters._Technology)
        Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)
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
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number Of Trial : {Num_DRCCheck}')
                    # elapsed time, start time, end time, main python file name
                else:
                    pass
            # Checker.DRCchecker_PrintInputParams(InputParams)
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print('#############################      Finished      ################################')

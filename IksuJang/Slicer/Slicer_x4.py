import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc
from SthPack import BoundaryCalc

from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from IksuJang.BasicArchive import ViaMet42Met5
from IksuJang.BasicArchive import ViaMet52Met6
from IksuJang.BasicArchive import ViaMet62Met7

from IksuJang.Slicer import Slicer


class Slicer_x4(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Slicer_x4'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  StrongArmLatch_NumFinger_NM1=8,           #
                                  StrongArmLatch_NumFinger_NM23=12,
                                  StrongArmLatch_NumFinger_NM45=2,
                                  StrongArmLatch_Width_NM1=1000,
                                  StrongArmLatch_Width_NM23=1000,
                                  StrongArmLatch_Width_NM45=1000,

                                  StrongArmLatch_NumContactY_NM1=1,  # option
                                  StrongArmLatch_NumContactY_NM23=2,  # option
                                  StrongArmLatch_NumContactY_NM45=1,  # option
                                  StrongArmLatch_NumContact_NMOSSETSubring=2,  # option

                                  StrongArmLatch_NumFinger_PM12=2,
                                  StrongArmLatch_NumFinger_PM34=3,
                                  StrongArmLatch_NumFinger_PM56=6,
                                  StrongArmLatch_Width_PM=1000,

                                  StrongArmLatch_NumContactY_PM=1,  # option
                                  StrongArmLatch_NumContact_PMOSSETSubring=2,  # option

                                  StrongArmLatch_NumContact_Subring=2,


                                  SRLatch_NumFinger_M1=5,                   #
                                  SRLatch_NumFinger_M2=1,
                                  SRLatch_NumFinger_M3=2,
                                  SRLatch_NumFinger_M4=2,

                                  SRLatch_Width_PM1=400,
                                  SRLatch_Width_PM2=400,
                                  SRLatch_Width_PM3=400,
                                  SRLatch_Width_PM4=400,

                                  SRLatch_Width_NM1=200,
                                  SRLatch_Width_NM2=200,
                                  SRLatch_Width_NM3=200,
                                  SRLatch_Width_NM4=200,

                                  Inv_NumFinger=15,                         #
                                  Inv_Width_PM=600,
                                  Inv_Width_NM=200,
                                  Inv_NumContactY_Gate=1,

                                  NumContactY_SupplyRail=2,             # option
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
        InputParameters = dict(
            StrongArmLatch_NumFinger_NM1=StrongArmLatch_NumFinger_NM1,  #
            StrongArmLatch_NumFinger_NM23=StrongArmLatch_NumFinger_NM23,
            StrongArmLatch_NumFinger_NM45=StrongArmLatch_NumFinger_NM45,
            StrongArmLatch_Width_NM1=StrongArmLatch_Width_NM1,
            StrongArmLatch_Width_NM23=StrongArmLatch_Width_NM23,
            StrongArmLatch_Width_NM45=StrongArmLatch_Width_NM45,

            StrongArmLatch_NumContactY_NM1=StrongArmLatch_NumContactY_NM1,  # option
            StrongArmLatch_NumContactY_NM23=StrongArmLatch_NumContactY_NM23,  # option
            StrongArmLatch_NumContactY_NM45=StrongArmLatch_NumContactY_NM45,  # option
            StrongArmLatch_NumContact_NMOSSETSubring=StrongArmLatch_NumContact_NMOSSETSubring,  # option

            StrongArmLatch_NumFinger_PM12=StrongArmLatch_NumFinger_PM12,
            StrongArmLatch_NumFinger_PM34=StrongArmLatch_NumFinger_PM34,
            StrongArmLatch_NumFinger_PM56=StrongArmLatch_NumFinger_PM56,
            StrongArmLatch_Width_PM=StrongArmLatch_Width_PM,

            StrongArmLatch_NumContactY_PM=StrongArmLatch_NumContactY_PM,  # option
            StrongArmLatch_NumContact_PMOSSETSubring=StrongArmLatch_NumContact_PMOSSETSubring,  # option

            StrongArmLatch_NumContact_Subring=StrongArmLatch_NumContact_Subring,

            SRLatch_NumFinger_M1=SRLatch_NumFinger_M1,  #
            SRLatch_NumFinger_M2=SRLatch_NumFinger_M2,
            SRLatch_NumFinger_M3=SRLatch_NumFinger_M3,
            SRLatch_NumFinger_M4=SRLatch_NumFinger_M4,

            SRLatch_Width_PM1=SRLatch_Width_PM1,
            SRLatch_Width_PM2=SRLatch_Width_PM2,
            SRLatch_Width_PM3=SRLatch_Width_PM3,
            SRLatch_Width_PM4=SRLatch_Width_PM4,

            SRLatch_Width_NM1=SRLatch_Width_NM1,
            SRLatch_Width_NM2=SRLatch_Width_NM2,
            SRLatch_Width_NM3=SRLatch_Width_NM3,
            SRLatch_Width_NM4=SRLatch_Width_NM4,

            Inv_NumFinger=Inv_NumFinger,  #
            Inv_Width_PM=Inv_Width_PM,
            Inv_Width_NM=Inv_Width_NM,
            Inv_NumContactY_Gate=Inv_NumContactY_Gate,

            NumContactY_SupplyRail=NumContactY_SupplyRail,  # option
            ChannelLength=ChannelLength,
            XVT=XVT,
            _GateSpacing=_GateSpacing
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['Slicer'] = self._SrefElementDeclaration(_DesignObj=Slicer.Slicer(_Name='SlicerIn{}'.format(_Name)))[0]
        self._DesignParameter['Slicer']['_DesignObj']._CalculateDesignParameter(**InputParameters)
        self._DesignParameter['Slicer']['_XYCoordinates'] = [[0, 0]]

        ''' -------------------------------------------------------------------------------------------------------- '''
        # case 1
        YCoord_BotOfmettop = self.getXYBot('Slicer', 'StrongArmLatch', 'PSubring', 'met_top')[0][1]
        YCoord_BotOfmetbot = self.getXYBot('Slicer', 'StrongArmLatch', 'PSubring', 'met_bot')[0][1]
        YCoord_2ndSlicer_case1 = YCoord_BotOfmetbot - YCoord_BotOfmettop

        # case 2
        YCoord_TopOfRX = self.getXYTop('Slicer', 'SRLatch', 'SRLatchUp', 'VDDRail', '_ODLayer')[0][1]
        YCoord_BotOfRX = self.getXYBot('Slicer', 'Inverter', 'VSSRail', '_ODLayer')[0][1]
        YCoord_2ndSlicer_case2 = YCoord_BotOfRX - YCoord_TopOfRX - _DRCObj._OdMinSpace

        # case 3
        YCoord_TopOfNW = self.getXYTop('Slicer', 'SRLatch', 'SRLatchUp', '_NWLayer')[0][1]
        YCoord_BotOfRX = self.getXYBot('Slicer', 'Inverter', 'VSSRail', '_ODLayer')[0][1]
        YCoord_2ndSlicer_case3 = YCoord_BotOfRX - YCoord_TopOfNW - _DRCObj._NwMinSpacetoPactive

        YCoord_2ndSlicer = min(YCoord_2ndSlicer_case1, YCoord_2ndSlicer_case2, YCoord_2ndSlicer_case3)
        self._DesignParameter['Slicer']['_XYCoordinates'] = [
            [0, 0],
            [0, YCoord_2ndSlicer],
            [0, YCoord_2ndSlicer * 2],
            [0, YCoord_2ndSlicer * 3]
        ]

        ''' -------------------------------------------------------------------------------------------------------- '''
        YCoord_1stBotOfBP = self.getXYBot('Slicer', 'StrongArmLatch', 'PSubring', 'bot', '_PPLayer')[0][1]
        YCoord_2ndTopOfBP = self.getXYTop('Slicer', 'StrongArmLatch', 'PSubring', 'top', '_PPLayer')[1][1]

        if YCoord_2ndSlicer != YCoord_2ndSlicer_case1 and YCoord_1stBotOfBP - YCoord_2ndTopOfBP < _DRCObj._PpMinSpace:
            YCoord_2ndSlicer = YCoord_1stBotOfBP - self.getXYTop('Slicer', 'StrongArmLatch', 'PSubring', 'top', '_PPLayer')[0][1] - _DRCObj._PpMinSpace

        self._DesignParameter['Slicer']['_XYCoordinates'] = [
            [0, 0],
            [0, YCoord_2ndSlicer],
            [0, YCoord_2ndSlicer * 2],
            [0, YCoord_2ndSlicer * 3]
        ]
        ''' -------------------------------------------------------------------------------------------------------- '''
        YMargin_routing = 500

        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXYTop('Slicer', 'StrongArmLatch', 'PSubring', 'met_top'))[0][1]
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXYBot('Slicer', 'StrongArmLatch', 'PSubring', 'met_bot'))[0][1]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('Slicer', 'StrongArmLatch', 'PSubring', 'met_left'))[0][0]
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('Slicer', 'StrongArmLatch', 'PSubring', 'met_right'))[0][0]
        self._DesignParameter['M2V_01'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=_DRCObj._MetalxMinWidth*6,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        self._DesignParameter['M2V_02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=_DRCObj._MetalxMinWidth * 6,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        self._DesignParameter['M2V_01']['_XYCoordinates'] = [[leftBoundary + self.getXWidth('M2V_01') / 2, (topBoundary + botBoundary) / 2]]
        self._DesignParameter['M2V_02']['_XYCoordinates'] = [[rightBoundary - self.getXWidth('M2V_02') / 2, (topBoundary + botBoundary) / 2]]

        self._DesignParameter['M4V_03'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinWidth * 8,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        self._DesignParameter['M4V_04'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinWidth * 8,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        self._DesignParameter['M4V_03']['_XYCoordinates'] = [[leftBoundary + self.getXWidth('M4V_03') / 2, (topBoundary + botBoundary) / 2]]
        self._DesignParameter['M4V_04']['_XYCoordinates'] = [[rightBoundary - self.getXWidth('M4V_04') / 2, (topBoundary + botBoundary) / 2]]


        ''' -------------------------------------------------------------------------------------------------------- '''
        XCoord_right_SRLatch = self.getXYRight('Slicer', 'SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')[0][0]
        XCoord_right_Inverter = self.getXYRight('Slicer', 'Inverter', 'VDDRail', '_Met1Layer')[0][0]
        XCoord_right = max(XCoord_right_SRLatch, XCoord_right_Inverter)
        XCoord_left = CoordCalc.getXYCoords_MaxX(self.getXYRight('Slicer', 'StrongArmLatch', 'PSubring', 'met_right'))[0][0]
        XWidth_M6V = self.FloorMinSnapSpacing((XCoord_right - XCoord_left - 500) / 2, MinSnapSpacing*2)

        # VSS
        self._DesignParameter['M6V_05'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=XWidth_M6V,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        # VDD
        self._DesignParameter['M6V_06'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=XWidth_M6V,
            _YWidth=topBoundary - botBoundary + YMargin_routing * 2
        )
        self._DesignParameter['M6V_05']['_XYCoordinates'] = [[XCoord_left + self.getXWidth('M6V_05') / 2, (topBoundary + botBoundary) / 2]]
        self._DesignParameter['M6V_06']['_XYCoordinates'] = [[XCoord_right - self.getXWidth('M6V_06') / 2, (topBoundary + botBoundary) / 2]]



        ''' -------------------------------------------------------------------------------------------------------- '''
        # VSS
        rightBoundary = self.getXYRight('M6V_05')[0][0]
        leftBoundary = self.getXYLeft('M4V_03')[0][0]
        self._DesignParameter['M5H_07'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=800,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('Slicer', 'StrongArmLatch', 'M3_VSS')[3][1]]]
        )
        self._DesignParameter['M5H_08'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=800,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('Slicer', 'StrongArmLatch', 'M3_VSS')[1][1]]]
        )

        # VDD
        rightBoundary = self.getXYRight('M6V_06')[0][0]
        leftBoundary = self.getXYLeft('M4V_03')[0][0]
        self._DesignParameter['M5H_09'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=800,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2,
                 (self.getXY('Slicer', 'StrongArmLatch', 'M3_VDD')[3][1] + self.getXY('Slicer', 'SRLatch', 'SRLatchUp', 'VDDRail')[3][1]) / 2]]
        )
        self._DesignParameter['M5H_10'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=800,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2,
                 (self.getXY('Slicer', 'StrongArmLatch', 'M3_VDD')[1][1] +
                  self.getXY('Slicer', 'SRLatch', 'SRLatchUp', 'VDDRail')[1][1]) / 2]]
        )
        self._DesignParameter['M5H_11'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=800,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2,
                 (self.getXY('Slicer', 'StrongArmLatch', 'M3_VDD')[0][1] +
                  self.getXY('Slicer', 'SRLatch', 'SRLatchUp', 'VDDRail')[0][1]) / 2]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        # VSS
        OverlappedBoundaryForVia5_1 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_07'], self._DesignParameter['M6V_05'])
        OverlappedBoundaryForVia5_2 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_08'], self._DesignParameter['M6V_05'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=OverlappedBoundaryForVia5_1['_XWidth'], YWidth=OverlappedBoundaryForVia5_1['_YWidth'])

        Via5Params = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        Via5Params['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
        Via5Params['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via5For050708'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5For050708In{}'.format(_Name)))[0]
        self._DesignParameter['Via5For050708']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**Via5Params)
        self._DesignParameter['Via5For050708']['_XYCoordinates'] = OverlappedBoundaryForVia5_1['_XYCoordinates'] + OverlappedBoundaryForVia5_2['_XYCoordinates']

        # VDD
        OverlappedBoundaryForVia5_1 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_09'], self._DesignParameter['M6V_06'])
        OverlappedBoundaryForVia5_2 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_10'], self._DesignParameter['M6V_06'])
        OverlappedBoundaryForVia5_3 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_11'], self._DesignParameter['M6V_06'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=OverlappedBoundaryForVia5_1['_XWidth'], YWidth=OverlappedBoundaryForVia5_1['_YWidth'])
        Via5Params = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        Via5Params['_ViaMet52Met6NumberOfCOX'] = NumViaXYs[0]
        Via5Params['_ViaMet52Met6NumberOfCOY'] = NumViaXYs[1]
        self._DesignParameter['Via5For06091011'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5For06091011In{}'.format(_Name)))[0]
        self._DesignParameter['Via5For06091011']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**Via5Params)
        self._DesignParameter['Via5For06091011']['_XYCoordinates'] = OverlappedBoundaryForVia5_1['_XYCoordinates'] + OverlappedBoundaryForVia5_2['_XYCoordinates'] + OverlappedBoundaryForVia5_3['_XYCoordinates']

        ''' -------------------------------------------------------------------------------------------------------- '''
        # VSS
        XWidth = CoordCalc.getXYCoords_MaxX(self.getXY('Slicer', 'StrongArmLatch', 'NMOSSET', 'NM1', '_PODummyLayer'))[0][0] * 2
        YWidth = min(self.getYWidth('Slicer', 'StrongArmLatch', 'M3_VSS'), self.getYWidth('M5H_07'))
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=XWidth, YWidth=YWidth)
        self._DesignParameter['Via4ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))

        self._DesignParameter['Via4ForVSS']['_XYCoordinates'] = [
            [0, self.getXY('M5H_07')[0][1]],
            [0, self.getXY('M5H_08')[0][1]],
        ]
        self._DesignParameter['Via3ForVSS']['_XYCoordinates'] = self.getXY('Via4ForVSS')

        ''' -------------------------------------------------------------------------------------------------------- '''
        # VDD
        OverlappedBoundaryForVia4 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M5H_09'], self._DesignParameter['M4V_03'])

        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=OverlappedBoundaryForVia4['_XWidth'], YWidth=OverlappedBoundaryForVia4['_YWidth'])

        self._DesignParameter['Via4ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia4['_XYCoordinates']
        self._DesignParameter['Via4ForVDD']['_XYCoordinates'] = [
            [self.getXY('M4V_03')[0][0], self.getXY('M5H_09')[0][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('M5H_09')[0][1]],
            [self.getXY('M4V_03')[0][0], self.getXY('M5H_10')[0][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('M5H_10')[0][1]],
            [self.getXY('M4V_03')[0][0], self.getXY('M5H_11')[0][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('M5H_11')[0][1]],

        ]

        # VDD ##
        objElement_M3 = dict(
            _XWidth=self.getXWidth('Slicer', 'M3H_03'),
            _YWidth=self.getYWidth('Slicer', 'M3H_03'),
            _XYCoordinates=self.getXY('Slicer', 'M3H_03')
        )
        OverlappedBoundaryForVia3 = BoundaryCalc.getOverlappedBoundaryElement(
            objElement_M3, self._DesignParameter['M4V_03'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=OverlappedBoundaryForVia3['_XWidth'], YWidth=OverlappedBoundaryForVia3['_YWidth'])
        self._DesignParameter['Via3ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForVDD']['_XYCoordinates'] = [
            [self.getXY('M4V_03')[0][0], self.getXY('Slicer', 'M3H_03')[3][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('Slicer', 'M3H_03')[3][1]],
            [self.getXY('M4V_03')[0][0], self.getXY('Slicer', 'M3H_03')[2][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('Slicer', 'M3H_03')[2][1]],
            [self.getXY('M4V_03')[0][0], self.getXY('Slicer', 'M3H_03')[1][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('Slicer', 'M3H_03')[1][1]],
            [self.getXY('M4V_03')[0][0], self.getXY('Slicer', 'M3H_03')[0][1]],
            [self.getXY('M4V_04')[0][0], self.getXY('Slicer', 'M3H_03')[0][1]],
        ]

        # VDD SRLatch Inverter
        objElement_M4 = dict(
            _XWidth=self.getXWidth('Slicer', 'VDDVia3', '_Met4Layer'),
            _YWidth=self.getYWidth('Slicer', 'VDDVia3', '_Met4Layer'),
            _XYCoordinates=self.getXY('Slicer', 'VDDVia3', '_Met4Layer')
        )
        OverlappedBoundaryForVia4 = BoundaryCalc.getOverlappedBoundaryElement(
            objElement_M4, self._DesignParameter['M6V_06'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=OverlappedBoundaryForVia4['_XWidth'], YWidth=OverlappedBoundaryForVia4['_YWidth'])
        self._DesignParameter['Via4ForVDDR'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVDDRIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVDDR']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForVDDR']['_XYCoordinates'] = OverlappedBoundaryForVia4['_XYCoordinates']


        YCoord_Via4ForVDDR_ascending = CoordCalc.getSortedList_ascending(self.getXY('Via4ForVDDR'))[1]
        self._DesignParameter['Via5ForVDDR'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForVDDRIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForVDDR']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXYs[0], _ViaMet52Met6NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via5ForVDDR']['_XYCoordinates'] = [
            [self.getXY('Via4ForVDDR')[0][0], YCoord_Via4ForVDDR_ascending[0]],
            [self.getXY('Via4ForVDDR')[0][0], YCoord_Via4ForVDDR_ascending[2]],
            [self.getXY('Via4ForVDDR')[0][0], YCoord_Via4ForVDDR_ascending[3]],
            [self.getXY('Via4ForVDDR')[0][0], YCoord_Via4ForVDDR_ascending[4]],
            [self.getXY('Via4ForVDDR')[0][0], YCoord_Via4ForVDDR_ascending[6]],
        ]


        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=[[self.getXYTop('M6V_05')[0][0], self.getXYTop('M6V_05')[0][1] - 100]],
            _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[[self.getXYTop('M6V_06')[0][0], self.getXYTop('M6V_06')[0][1] - 100]],
            _Mag=0.04, _TEXT='VDD')

        for i in range(0, 4):
            self._DesignParameter[f'PIN_INp{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[self.getXY('Slicer', 'PIN_INp')[i]],
                _Mag=0.04, _TEXT=f'INp<{i}>')
            self._DesignParameter[f'PIN_INn{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[self.getXY('Slicer', 'PIN_INn')[i]],
                _Mag=0.04, _TEXT=f'INn<{i}>')
            self._DesignParameter[f'PIN_CLK{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[self.getXY('Slicer', 'PIN_CLK')[i]],
                _Mag=0.04, _TEXT=f'CLK<{i}>')
            self._DesignParameter[f'PIN_OUT{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[self.getXY('Slicer', 'PIN_OUT')[i]],
                _Mag=0.04, _TEXT=f'OUT<{i}>')
            self._DesignParameter[f'PIN_OUTb{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[self.getXY('Slicer', 'PIN_OUTb')[i]],
                _Mag=0.04, _TEXT=f'OUTb<{i}>')



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

    libname = 'TEST_Slicer_x4'
    cellname = 'Slicer_x4'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_20G = dict(
        StrongArmLatch_NumFinger_NM1=8,
        StrongArmLatch_NumFinger_NM23=12,
        StrongArmLatch_NumFinger_NM45=2,
        StrongArmLatch_Width_NM1=1000,
        StrongArmLatch_Width_NM23=1000,
        StrongArmLatch_Width_NM45=1000,

        StrongArmLatch_NumContactY_NM1=1,  # option
        StrongArmLatch_NumContactY_NM23=2,  # option
        StrongArmLatch_NumContactY_NM45=1,  # option
        StrongArmLatch_NumContact_NMOSSETSubring=2,  # option

        StrongArmLatch_NumFinger_PM12=2,
        StrongArmLatch_NumFinger_PM34=3,
        StrongArmLatch_NumFinger_PM56=6,
        StrongArmLatch_Width_PM=1000,

        StrongArmLatch_NumContactY_PM=1,  # option
        StrongArmLatch_NumContact_PMOSSETSubring=2,  # option

        StrongArmLatch_NumContact_Subring=2,


        SRLatch_NumFinger_M1=5,  #
        SRLatch_NumFinger_M2=1,
        SRLatch_NumFinger_M3=2,
        SRLatch_NumFinger_M4=2,

        SRLatch_Width_PM1=400,
        SRLatch_Width_PM2=400,
        SRLatch_Width_PM3=400,
        SRLatch_Width_PM4=400,

        SRLatch_Width_NM1=200,
        SRLatch_Width_NM2=200,
        SRLatch_Width_NM3=200,
        SRLatch_Width_NM4=200,

        Inv_NumFinger=16,  #
        Inv_Width_PM=600,
        Inv_Width_NM=200,
        Inv_NumContactY_Gate=1,

        NumContactY_SupplyRail=2,  # option
        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
    )
    InputParams_16G = dict(
        StrongArmLatch_NumFinger_NM1=12,
        StrongArmLatch_NumFinger_NM23=10,
        StrongArmLatch_NumFinger_NM45=1,
        StrongArmLatch_Width_NM1=500,
        StrongArmLatch_Width_NM23=1000,
        StrongArmLatch_Width_NM45=1000,

        StrongArmLatch_NumContactY_NM1=1,  # option
        StrongArmLatch_NumContactY_NM23=2,  # option
        StrongArmLatch_NumContactY_NM45=1,  # option
        StrongArmLatch_NumContact_NMOSSETSubring=2,  # option

        StrongArmLatch_NumFinger_PM12=3,
        StrongArmLatch_NumFinger_PM34=3,
        StrongArmLatch_NumFinger_PM56=4,
        StrongArmLatch_Width_PM=500,

        StrongArmLatch_NumContactY_PM=1,  # option
        StrongArmLatch_NumContact_PMOSSETSubring=2,  # option

        StrongArmLatch_NumContact_Subring=2,


        SRLatch_NumFinger_M1=2,  #
        SRLatch_NumFinger_M2=1,
        SRLatch_NumFinger_M3=1,
        SRLatch_NumFinger_M4=1,

        SRLatch_Width_PM1=500,
        SRLatch_Width_PM2=400,
        SRLatch_Width_PM3=400,
        SRLatch_Width_PM4=400,

        SRLatch_Width_NM1=250,
        SRLatch_Width_NM2=200,
        SRLatch_Width_NM3=200,
        SRLatch_Width_NM4=200,

        Inv_NumFinger=15,  #
        Inv_Width_PM=600,
        Inv_Width_NM=200,
        Inv_NumContactY_Gate=1,

        NumContactY_SupplyRail=2,  # option
        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
    )
    InputParams_12G = dict(
        StrongArmLatch_NumFinger_NM1=20,
        StrongArmLatch_NumFinger_NM23=8,
        StrongArmLatch_NumFinger_NM45=1,
        StrongArmLatch_Width_NM1=300,
        StrongArmLatch_Width_NM23=1000,
        StrongArmLatch_Width_NM45=1000,

        StrongArmLatch_NumContactY_NM1=1,  # option
        StrongArmLatch_NumContactY_NM23=2,  # option
        StrongArmLatch_NumContactY_NM45=1,  # option
        StrongArmLatch_NumContact_NMOSSETSubring=2,  # option

        StrongArmLatch_NumFinger_PM12=2,
        StrongArmLatch_NumFinger_PM34=3,
        StrongArmLatch_NumFinger_PM56=3,
        StrongArmLatch_Width_PM=500,

        StrongArmLatch_NumContactY_PM=1,  # option
        StrongArmLatch_NumContact_PMOSSETSubring=2,  # option

        StrongArmLatch_NumContact_Subring=2,


        SRLatch_NumFinger_M1=2,  #
        SRLatch_NumFinger_M2=1,
        SRLatch_NumFinger_M3=1,
        SRLatch_NumFinger_M4=1,

        SRLatch_Width_PM1=400,
        SRLatch_Width_PM2=400,
        SRLatch_Width_PM3=400,
        SRLatch_Width_PM4=400,

        SRLatch_Width_NM1=200,
        SRLatch_Width_NM2=200,
        SRLatch_Width_NM3=200,
        SRLatch_Width_NM4=200,

        Inv_NumFinger=15,  #
        Inv_Width_PM=600,
        Inv_Width_NM=200,
        Inv_NumContactY_Gate=1,

        NumContactY_SupplyRail=2,  # option
        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
    )
    InputParams = InputParams_20G

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
        LayoutObj = Slicer_x4(_Name=cellname)
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

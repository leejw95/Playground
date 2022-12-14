import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc

from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import NSubRing
from IksuJang.BasicArchive import PSubRing
from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from IksuJang.Slicer import NMOSSET
from IksuJang.Slicer import PMOSSET


class StrongArmLatch(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='StrongArmLatch'):
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

                                  NumContactY_NM1=1,            # option
                                  NumContactY_NM23=2,           # option
                                  NumContactY_NM45=1,           # option
                                  NumContact_NMOSSETSubring=2,  # option

                                  NumFinger_PM12=2,
                                  NumFinger_PM34=3,
                                  NumFinger_PM56=6,
                                  Width_PM=1000,

                                  NumContactY_PM=1,             # option
                                  NumContact_PMOSSETSubring=2,  # option

                                  NumContact_Subring=2,

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
        self._DesignParameter['PMOSSET'] = self._SrefElementDeclaration(_DesignObj=PMOSSET.PMOSSET(_Name='PMOSSETIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOSSET']['_DesignObj']._CalculateDesignParameter(
            **dict(NumFinger_PM12=NumFinger_PM12, NumFinger_PM34=NumFinger_PM34, NumFinger_PM56=NumFinger_PM56,
                   Width_PM=Width_PM, ChannelLength=ChannelLength, XVT=XVT,
                   NumContactY_PM=NumContactY_PM,
                   NumContact_Subring=NumContact_PMOSSETSubring, _GateSpacing=_GateSpacing)
        )
        self._DesignParameter['NMOSSET'] = self._SrefElementDeclaration(_DesignObj=NMOSSET.NMOSSET(_Name='NMOSSETIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOSSET']['_DesignObj']._CalculateDesignParameter(
            **dict(NumFinger_NM1=NumFinger_NM1, NumFinger_NM23=NumFinger_NM23, NumFinger_NM45=NumFinger_NM45,
                   Width_NM1=Width_NM1, Width_NM23=Width_NM23, Width_NM45=Width_NM45,
                   ChannelLength=ChannelLength, XVT=XVT,
                   NumContactY_NM1=NumContactY_NM1, NumContactY_NM23=NumContactY_NM23,
                   NumContactY_NM45=NumContactY_NM45,
                   NumContact_Subring=NumContact_NMOSSETSubring, _GateSpacing=_GateSpacing)
        )
        self._DesignParameter['PMOSSET']['_XYCoordinates'] = [[0, 0]]       # temporal setting. reCalculated Later.
        self._DesignParameter['NMOSSET']['_XYCoordinates'] = [[0, 0]]       # temporal setting. reCalculated Later.

        _YCoord_PMOSSET = abs(self.getXYBot('PMOSSET', 'NSubring', 'nw_bot')[0][1]) + _DRCObj._NwMinEnclosurePactive / 2
        _YCoord_NMOSSET = -abs(self.getXYTop('NMOSSET', 'PSubring', 'top', '_PPLayer')[0][1]) - _DRCObj._NwMinEnclosurePactive / 2
        YCoord_PMOSSET = self.CeilMinSnapSpacing(_YCoord_PMOSSET, MinSnapSpacing * 2)
        YCoord_NMOSSET = self.FloorMinSnapSpacing(_YCoord_NMOSSET, MinSnapSpacing*2)

        self._DesignParameter['PMOSSET']['_XYCoordinates'] = [[0, YCoord_PMOSSET]]
        self._DesignParameter['NMOSSET']['_XYCoordinates'] = [[0, YCoord_NMOSSET]]


        ''' ----------------------------------------------------- (net01) ------------------------------------------ '''
        # M4V
        topBoundary_M4V_net01 = self.getXYBot('PMOSSET', 'M3V3M4OnPM56Drain', '_Met4Layer')[0][1]
        botBoundary_M4V_net01 = self.getXYBot('NMOSSET', 'M2HUp')[0][1]
        tmpXYs = []
        for XYs in self.getXY('PMOSSET', 'M3V3M4OnPM56Drain'):
            tmpXYs.append([XYs[0], (topBoundary_M4V_net01 + botBoundary_M4V_net01) / 2])

        self._DesignParameter['M4V_net01'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('PMOSSET', 'M3V3M4OnPM56Drain', '_Met4Layer'),
            _YWidth=topBoundary_M4V_net01 - botBoundary_M4V_net01,
            _XYCoordinates=tmpXYs
        )

        # M3V3M4
        ViaParams = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        ViaParams['_ViaMet32Met4NumberOfCOX'] = 1
        ViaParams['_ViaMet32Met4NumberOfCOY'] = 2
        self._DesignParameter['M3V3M4Onnet01'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4Onnet01In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4Onnet01']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**ViaParams)

        tmpXYs = []
        for XYs in self.getXYBot('M4V_net01'):
            tmpXYs.append([XYs[0], XYs[1] + self.getYWidth('M3V3M4Onnet01', '_Met4Layer') / 2])
        self._DesignParameter['M3V3M4Onnet01']['_XYCoordinates'] = tmpXYs


        ''' -------------------------------------- M4V From NM45's Drain to PM12's Drain (net03) ----------------------------------------------- '''
        topBoundary_M4V_net03 = self.getXYTop('PMOSSET', 'M3V3M4OnPM12Drain', '_Met4Layer')[0][1]
        botBoundary_M4V_net03 = self.getXYBot('NMOSSET', 'M3V3M4OnNM45Middle', '_Met4Layer')[0][1]
        self._DesignParameter['M4V_net03'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinWidth*2,
            _YWidth=topBoundary_M4V_net03 - botBoundary_M4V_net03,
        )
        self._DesignParameter['M4V_net03']['_XYCoordinates'] = [
            [self.getXY('NMOSSET', 'M3V3M4OnNM45Middle')[0][0], (topBoundary_M4V_net03 + botBoundary_M4V_net03) / 2],
            [self.getXY('NMOSSET', 'M3V3M4OnNM45Middle')[1][0], (topBoundary_M4V_net03 + botBoundary_M4V_net03) / 2]
        ]

        ''' ---------------------------------------------- PSubring ------------------------------------------------ '''
        self._DesignParameter['PSubring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=1000, width=1000, contact=NumContact_Subring if NumContact_Subring is not None else 2)
        )       # temporal gen. ReCalculated Later.

        XWidthOfSubring1 = self.getXYRight('NMOSSET', 'PSubring', 'right', '_PPLayer')[0][0] + _DRCObj._PpMinSpace + self.getXWidth('PSubring', 'right', '_PPLayer') / 2
        XWidthOfSubring2 = self.getXYRight('PMOSSET', 'NSubring', 'nw_right')[0][0] + _DRCObj._NwMinEnclosurePactive + self.getXWidth('PSubring', 'right', '_PPLayer') / 2
        XWidthOfSubring = max(XWidthOfSubring1, XWidthOfSubring2) * 2

        _YdownwardOfSubring = self.getXYBot('NMOSSET', 'PSubring', 'bot', '_PPLayer')[0][1] - _DRCObj._PpMinSpace - self.getYWidth('PSubring', 'bot', '_PPLayer') / 2
        _YupwardOfSubring = self.getXYTop('PMOSSET', 'NSubring', 'nw_right')[0][1] + _DRCObj._NwMinEnclosurePactive + self.getYWidth('PSubring', 'top', '_PPLayer') / 2
        YdownwardOfSubring = self.FloorMinSnapSpacing(_YdownwardOfSubring, 2*MinSnapSpacing)
        YupwardOfSubring = self.CeilMinSnapSpacing(_YupwardOfSubring, 2*MinSnapSpacing)

        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=YupwardOfSubring-YdownwardOfSubring,
                   width=XWidthOfSubring,
                   contact=NumContact_Subring if NumContact_Subring is not None else 2)
        )
        self._DesignParameter['PSubring']['_XYCoordinates'] = [[0, (YupwardOfSubring + YdownwardOfSubring) / 2]]


        ''' --------------------------------- M2V (from PM12 to NM45) ---------------------------------------- '''
        topBoundary_M2V_net04 = self.getXYTop('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer')[0][1]
        botBoundary_M2V_net04 = self.getXYBot('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[0][1]
        self._DesignParameter['M2V_net04'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=_DRCObj._MetalxMinWidth * 2,
            _YWidth=topBoundary_M2V_net04 - botBoundary_M2V_net04
        )
        if NumFinger_NM45 == NumFinger_PM12:
            self._DesignParameter['M2V_net04']['_XYCoordinates'] = [
                [self.getXYTop('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[0][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2],
                [self.getXYTop('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[1][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2]
            ]
        elif NumFinger_NM45 > NumFinger_PM12:
            self._DesignParameter['M2V_net04']['_XYCoordinates'] = [
                [self.getXYTop('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[0][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2],
                [self.getXYTop('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[1][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2]
            ]
        else:   # NumFinger_NM45 < NumFinger_PM12:
            self._DesignParameter['M2V_net04']['_XYCoordinates'] = [
                [self.getXYTop('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer')[0][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2],
                [self.getXYTop('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer')[1][0], (topBoundary_M2V_net04 + botBoundary_M2V_net04) / 2]
            ]

        # Additional M2H Routing when 'NumFinger_NM45 != NumFinger_PM12'
        if NumFinger_NM45 == NumFinger_PM12:
            pass
        elif NumFinger_NM45 > NumFinger_PM12:
            leftBoundary_M2H_net04 = CoordCalc.getXYCoords_MaxX(self.getXYLeft('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer'))[0][0]
            rightBoundary_M2H_net04 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2V_net04'))[0][0]
            self._DesignParameter['M2H_net04'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=rightBoundary_M2H_net04 - leftBoundary_M2H_net04,
                _YWidth=self.getYWidth('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer'),
                _XYCoordinates=[
                    [-(rightBoundary_M2H_net04 + leftBoundary_M2H_net04) / 2, self.getXY('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer')[0][1]],
                    [+(rightBoundary_M2H_net04 + leftBoundary_M2H_net04) / 2, self.getXY('PMOSSET', 'M1V1M2OnPM12Gate', '_Met2Layer')[0][1]],
                ]
            )
        else:   # NumFinger_NM45 < NumFinger_PM12:
            leftBoundary_M2H_net04 = CoordCalc.getXYCoords_MaxX(self.getXYLeft('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer'))[0][0]
            rightBoundary_M2H_net04 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2V_net04'))[0][0]
            self._DesignParameter['M2H_net04'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=rightBoundary_M2H_net04 - leftBoundary_M2H_net04,
                _YWidth=self.getYWidth('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer'),
                _XYCoordinates=[
                    [-(rightBoundary_M2H_net04 + leftBoundary_M2H_net04) / 2,
                     self.getXY('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[0][1]],
                    [+(rightBoundary_M2H_net04 + leftBoundary_M2H_net04) / 2,
                     self.getXY('NMOSSET', 'M1V1M2OnNM45Gate', '_Met2Layer')[0][1]],
                ]
            )

        ''' -------------------------------------- CrossCoupled (M2-M4) (net03-net04) -------------------------------------------- '''
        YCoord_3of4 = self.FloorMinSnapSpacing(self.getXY('M2V_net04')[0][1] + self.getYWidth('M2V_net04') / 4, MinSnapSpacing)
        YCoord_1of4 = self.CeilMinSnapSpacing(self.getXY('M2V_net04')[0][1] - self.getYWidth('M2V_net04') / 4, MinSnapSpacing)

        # M2V2M3, M3V3M4
        self._DesignParameter['M2V2M3Onnet03net04'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3Onnet03net04In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3Onnet03net04']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
        self._DesignParameter['M3V3M4Onnet03net04'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4Onnet03net04In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4Onnet03net04']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))

        XCoordofVia0304_byM2 = self.FloorMinSnapSpacing(CoordCalc.getXYCoords_MaxX(self.getXYLeft('M2V_net04'))[0][0] - _DRCObj._MetalxMinSpaceAtCorner - self.getXWidth('M2V2M3Onnet03net04', '_Met2Layer') / 2, MinSnapSpacing)
        XCoordofVia0304_byM4 = CoordCalc.getXYCoords_MaxX(self.getXY('M4V_net03'))[0][0]
        XCoordofVia0304 = min(XCoordofVia0304_byM2, XCoordofVia0304_byM4)

        self._DesignParameter['M3V3M4Onnet03net04']['_XYCoordinates'] = [
            [+XCoordofVia0304, YCoord_1of4],
            [-XCoordofVia0304, YCoord_3of4]
        ]
        self._DesignParameter['M2V2M3Onnet03net04']['_XYCoordinates'] = self.getXY('M3V3M4Onnet03net04')


        # M2H
        leftBoundary_M2H_net0304_1of4 = CoordCalc.getXYCoords_MinX(self.getXYLeft('M2V_net04'))[0][0]
        RightBoundary_M2H_net0304_1of4 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2V2M3Onnet03net04', '_Met2Layer'))[0][0]
        leftBoundary_M2H_net0304_3of4 = CoordCalc.getXYCoords_MinX(self.getXYLeft('M2V2M3Onnet03net04', '_Met2Layer'))[0][0]
        RightBoundary_M2H_net0304_3of4 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2V_net04'))[0][0]
        self._DesignParameter['M2H_net0304'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=RightBoundary_M2H_net0304_1of4-leftBoundary_M2H_net0304_1of4,
            _YWidth=self.getXWidth('M2V_net04'),
            _XYCoordinates=[
                [(RightBoundary_M2H_net0304_1of4 + leftBoundary_M2H_net0304_1of4) / 2, YCoord_1of4],
                [(RightBoundary_M2H_net0304_3of4 + leftBoundary_M2H_net0304_3of4) / 2, YCoord_3of4]
            ]
        )

        ''' ----------------------------------------- M2V2M3 on M2HUp -------------------------------------------- '''
        RightBoundary_M3H_byM2up = CoordCalc.getXYCoords_MaxX(self.getXYRight('NMOSSET', 'M1V1M2OnNM2345Up', '_Met2Layer'))[0][0]
        RightBoundary_M3H_byVianet01 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M3V3M4Onnet01', '_Met3Layer'))[0][0]
        RightBoundary_M3H = max(RightBoundary_M3H_byM2up, RightBoundary_M3H_byVianet01)
        LeftBoundary_M3H_byM2up = self.getXYLeft('NMOSSET', 'NM3', '_Met1Layer')[0][0]
        LeftBoundary_M3H_byVianet01 = CoordCalc.getSortedList_ascending(self.getXYLeft('M3V3M4Onnet01', '_Met3Layer'))[0][int(len(self.getXYLeft('M3V3M4Onnet01', '_Met3Layer')) / 2)]
        LeftBoundary_M3H = min(LeftBoundary_M3H_byM2up, LeftBoundary_M3H_byVianet01)

        self._DesignParameter['M3HonM2HUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=RightBoundary_M3H - LeftBoundary_M3H,
            _YWidth=self.getYWidth('NMOSSET', 'M2HUp'),
            _XYCoordinates=[
                [-(RightBoundary_M3H + LeftBoundary_M3H) / 2, self.getXY('NMOSSET', 'M2HUp')[0][1]],
                [+(RightBoundary_M3H + LeftBoundary_M3H) / 2, self.getXY('NMOSSET', 'M2HUp')[0][1]]
            ]
        )
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('M3HonM2HUp'), YWidth=self.getYWidth('M3HonM2HUp'))
        self._DesignParameter['M2V2M3OnM2HUp'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnM2HUpIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnM2HUp']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnM2HUp']['_XYCoordinates'] = self.getXY('M3HonM2HUp')


        ''' -------------------------------------- M4V (net05) ------------------------------------------ '''
        topBoundary_M4V_net05 = self.getXYTop('PMOSSET', 'M2V2M3OnPM35PM46Gate', '_Met3Layer')[0][1]
        botBoundary_M4V_net05 = self.getXYBot('NMOSSET', 'M3HOnNM1Gate')[0][1]
        XCoord_M4V_net05_byPMOSSET = (self.getXY('PMOSSET', 'PM2', '_Met1Layer')[-1][0] + self.getXY('PMOSSET', 'PM46', '_Met1Layer')[0][0]) / 2
        XCoord_M4V_net05_byNMOSSET = (self.getXY('NMOSSET', 'NM5', '_Met1Layer')[-1][0] + self.getXY('NMOSSET', 'NM3', '_Met1Layer')[0][0]) / 2
        XCoord_M4V_net05 = max(XCoord_M4V_net05_byPMOSSET, XCoord_M4V_net05_byNMOSSET)
        self._DesignParameter['M4V_net05'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinWidth*2,
            _YWidth=topBoundary_M4V_net05-botBoundary_M4V_net05,
            _XYCoordinates=[
                [-XCoord_M4V_net05, (topBoundary_M4V_net05 + botBoundary_M4V_net05) / 2],
                [+XCoord_M4V_net05, (topBoundary_M4V_net05 + botBoundary_M4V_net05) / 2]
            ]
        )

        # recalculate
        self._DesignParameter['NMOSSET']['_DesignObj']._DesignParameter['M3V3M4OnNM1Gate']['_XYCoordinates'] = [
            [-XCoord_M4V_net05, self._DesignParameter['NMOSSET']['_DesignObj']._DesignParameter['M3V3M4OnNM1Gate']['_XYCoordinates'][0][1]],
            [+XCoord_M4V_net05, self._DesignParameter['NMOSSET']['_DesignObj']._DesignParameter['M3V3M4OnNM1Gate']['_XYCoordinates'][0][1]]
        ]
        self._DesignParameter['NMOSSET']['_DesignObj']._DesignParameter['M3HOnNM1Gate']['_XWidth'] = \
            max(XCoord_M4V_net05 * 2, self.getXWidth('NMOSSET', 'M3HOnNM1Gate'))

        # on PMOSSET
        rightBoundary_M3HOnPM35PM46Gate = CoordCalc.getXYCoords_MaxX(self.getXYRight('PMOSSET', 'M2V2M3OnPM35PM46Gate', '_Met3Layer'))[0][0]
        leftBoundary_M3HOnPM35PM46Gate = CoordCalc.getXYCoords_MaxX(self.getXYLeft('NMOSSET', 'M3V3M4OnNM1Gate', '_Met3Layer'))[0][0]
        self._DesignParameter['M3HOnPM35PM46Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary_M3HOnPM35PM46Gate-leftBoundary_M3HOnPM35PM46Gate,
            _YWidth=_DRCObj._MetalxMinWidth * 2
        )
        YCoord_M3HOnPM35PM46Gate = self.getXYTop('PMOSSET', 'M2V2M3OnPM35PM46Gate', '_Met3Layer')[0][1] - self.getYWidth('M3HOnPM35PM46Gate') / 2
        self._DesignParameter['M3HOnPM35PM46Gate']['_XYCoordinates'] = [
            [-(rightBoundary_M3HOnPM35PM46Gate + leftBoundary_M3HOnPM35PM46Gate) / 2, YCoord_M3HOnPM35PM46Gate],
            [+(rightBoundary_M3HOnPM35PM46Gate + leftBoundary_M3HOnPM35PM46Gate) / 2, YCoord_M3HOnPM35PM46Gate]
        ]

        self._DesignParameter['M3V3M4OnPM35PM46Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnPM35PM46GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPM35PM46Gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
        YCoord_M3V3M4OnPM35PM46Gate = self.getXYTop('M4V_net05')[0][1] - self.getYWidth('M3V3M4OnPM35PM46Gate', '_Met4Layer') / 2
        self._DesignParameter['M3V3M4OnPM35PM46Gate']['_XYCoordinates'] = [
            [-XCoord_M4V_net05, YCoord_M3V3M4OnPM35PM46Gate],
            [+XCoord_M4V_net05, YCoord_M3V3M4OnPM35PM46Gate]
        ]

        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' ---------------------------- M4V From NM1's Drain to NM23 (net02) -------------------------------------- '''
        topBoundary_M4V_net02 = self.getXYTop('NMOSSET', 'M2HDn')[0][1]
        botBoundary_M4V_net02 = self.getXYBot('NMOSSET', 'M3V3M4OnNM1', '_Met4Layer')[0][1]
        self._DesignParameter['M4V_net02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinSpace * 3,
            _YWidth=topBoundary_M4V_net02 - botBoundary_M4V_net02,
            _XYCoordinates=[[0, (topBoundary_M4V_net02 + botBoundary_M4V_net02) / 2]]
        )

        # M2 - M4 Via for net02
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXYLeft('M4V_net05')[1][0], YWidth=self.getYWidth('NMOSSET', 'M2HDn'))
        self._DesignParameter['M2V2M3OnM2HDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnM2HDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnM2HDn']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnM2HDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnM2HDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnM2HDn']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnM2HDn']['_XYCoordinates'] = self.getXY('NMOSSET', 'M2HDn')
        self._DesignParameter['M3V3M4OnM2HDn']['_XYCoordinates'] = self.getXY('NMOSSET', 'M2HDn')

        ''' --------------------------------- Up to M3 Supply Vias (VDD & VSS) ------------------------------------- '''
        # M3, M2 VDD Rail
        self._DesignParameter['M3_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('PMOSSET', 'NSubring', 'met_top'),
            _YWidth=self.getYWidth('PMOSSET', 'NSubring', 'met_top'),
            _XYCoordinates=self.getXY('PMOSSET', 'NSubring', 'met_top'),
        )
        self._DesignParameter['M2_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M3_VDD'),
            _YWidth=self.getYWidth('M3_VDD'),
            _XYCoordinates=self.getXY('M3_VDD'),
        )

        # M1V1M2, M2V2M3 VDD Rail
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('M3_VDD'), YWidth=self.getYWidth('M3_VDD'))
        self._DesignParameter['M1V1M2OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnVDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnVDD']['_XYCoordinates'] = self.getXY('M3_VDD')
        self._DesignParameter['M2V2M3OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnVDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnVDD']['_XYCoordinates'] = self.getXY('M3_VDD')

        # M3, M2 VSS Rail
        topBoundary_M3VSS = self.getXYTop('NMOSSET', 'PSubring', 'met_bot')[0][1]
        botBoundary_M3VSS = self.getXYBot('PSubring', 'met_bot')[0][1]
        self._DesignParameter['M3_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('PSubring', 'met_bot'),
            _YWidth=(topBoundary_M3VSS - botBoundary_M3VSS),
            _XYCoordinates=[[0, (topBoundary_M3VSS + botBoundary_M3VSS) / 2]],
        )
        self._DesignParameter['M2_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M3_VSS'),
            _YWidth=self.getYWidth('M3_VSS'),
            _XYCoordinates=self.getXY('M3_VSS'),
        )

        # M1V1M2, M2V2M3 VSS Rail
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(XWidth=self.getXWidth('M3_VSS'), YWidth=self.getYWidth('M3_VSS'))
        self._DesignParameter['M1V1M2OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnVSS']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnVSS']['_XYCoordinates'] = self.getXY('M3_VSS')
        self._DesignParameter['M2V2M3OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnVSS']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnVSS']['_XYCoordinates'] = self.getXY('M3_VSS')

        ''' -------------------------------------------------------------------------------------------------------- '''
        InputMet1_XWidth = self.getXWidth('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')
        InputMet1_YWidth = self.getYWidth('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')
        InputMet1_XY_INp = [self.getXY('NMOSSET', 'PolyContactOnNM23')[0]]
        InputMet1_XY_INn = [self.getXY('NMOSSET', 'PolyContactOnNM23')[1]]

        # Via1
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=InputMet1_XWidth, YWidth=InputMet1_YWidth)
        self._DesignParameter['Via1ForVIN'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForVINIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForVIN']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['Via1ForVIN']['_XYCoordinates'] = InputMet1_XY_INn + InputMet1_XY_INp


        # Via2
        RightBoundaryM4 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V_net05'))[0][0]
        leftBoundary_Via2 = max(RightBoundaryM4 + _DRCObj._MetalxMinSpace21, self.getXYLeft('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')[1][0])
        rightBoundary_Via2 = self.getXYRight('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')[1][0]
        InputMet4_XWidth = rightBoundary_Via2 - leftBoundary_Via2
        InputMet4_YWidth = self.getYWidth('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=InputMet4_XWidth, YWidth=InputMet4_YWidth)
        self._DesignParameter['Via2ForVIN'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForVINIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForVIN']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=1))
        self._DesignParameter['Via2ForVIN']['_XYCoordinates'] = [
            [-(rightBoundary_Via2 + leftBoundary_Via2) / 2, self.getXY('NMOSSET', 'PolyContactOnNM23')[0][1]],
            [+(rightBoundary_Via2 + leftBoundary_Via2) / 2, self.getXY('NMOSSET', 'PolyContactOnNM23')[0][1]],
        ]

        # Via3
        RightBoundaryM4 = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V_net05'))[0][0]
        leftBoundary_Via3 = max(RightBoundaryM4 + _DRCObj._MetalxMinSpace4, self.getXYLeft('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')[1][0])
        rightBoundary_Via3 = self.getXYRight('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')[1][0]
        InputMet4_XWidth = rightBoundary_Via3 - leftBoundary_Via3
        InputMet4_YWidth = self.getYWidth('NMOSSET', 'PolyContactOnNM23', '_Met1Layer')

        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=InputMet4_XWidth, YWidth=InputMet4_YWidth)
            if NumViaXY[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (NumViaXY[0], 2)

        self._DesignParameter['Via3ForVINp'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVINpIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVINp']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via3ForVINp']['_XYCoordinates'] = [
            [-(rightBoundary_Via3 + leftBoundary_Via3) / 2, self.getXY('NMOSSET', 'PolyContactOnNM23')[0][1]]
        ]

        self._DesignParameter['Via3ForVINn'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVINnIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVINn']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via3ForVINn']['_XYCoordinates'] = [
            [+(rightBoundary_Via3 + leftBoundary_Via3) / 2, self.getXY('NMOSSET', 'PolyContactOnNM23')[0][1]]
        ]


        ''' -------------------------------------------------------------------------------------------------------- '''

        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXY('M3_VSS'), _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('M3_VDD'), _Mag=0.04, _TEXT='VDD')

        self._DesignParameter['PIN_INp'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('NMOSSET', 'PolyContactOnNM23')[0]], _Mag=0.04, _TEXT='INp')
        self._DesignParameter['PIN_INn'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('NMOSSET', 'PolyContactOnNM23')[1]], _Mag=0.04, _TEXT='INn')

        self._DesignParameter['PIN_CLK'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('NMOSSET', 'M3HOnNM1Gate'), _Mag=0.04, _TEXT='CLK')

        self._DesignParameter['PIN_SSp'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('M4V_net03')[0]], _Mag=0.04, _TEXT='SSp')
        self._DesignParameter['PIN_SSn'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('M4V_net03')[1]], _Mag=0.04, _TEXT='SSn')


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
    cellname = 'StrongArmLatch'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_20G = dict(
        NumFinger_NM1=8,
        NumFinger_NM23=12,
        NumFinger_NM45=2,
        Width_NM1=1000,
        Width_NM23=1000,
        Width_NM45=1000,

        NumContactY_NM1=1,              # option
        NumContactY_NM23=2,             # option
        NumContactY_NM45=1,             # option
        NumContact_NMOSSETSubring=2,    # option

        NumFinger_PM12=2,
        NumFinger_PM34=3,
        NumFinger_PM56=6,
        Width_PM=1000,

        NumContactY_PM=1,               # option
        NumContact_PMOSSETSubring=2,    # option

        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None

    )

    InputParams_16G = dict(
        NumFinger_NM1=12,
        NumFinger_NM23=10,
        NumFinger_NM45=1,
        Width_NM1=500,
        Width_NM23=1000,
        Width_NM45=1000,

        NumContactY_NM1=1,              # option
        NumContactY_NM23=2,             # option
        NumContactY_NM45=1,             # option
        NumContact_NMOSSETSubring=2,    # option

        #
        NumFinger_PM12=3,
        NumFinger_PM34=3,
        NumFinger_PM56=4,
        Width_PM=500,

        NumContactY_PM=1,               # option
        NumContact_PMOSSETSubring=2,    # option

        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
    )

    InputParams_12G = dict(
        NumFinger_NM1=20,
        NumFinger_NM23=8,
        NumFinger_NM45=1,
        Width_NM1=300,
        Width_NM23=1000,
        Width_NM45=1000,

        NumContactY_NM1=1,              # option
        NumContactY_NM23=2,             # option
        NumContactY_NM45=1,             # option
        NumContact_NMOSSETSubring=2,    # option

        #
        NumFinger_PM12=2,
        NumFinger_PM34=3,
        NumFinger_PM56=3,
        Width_PM=500,

        NumContactY_PM=1,               # option
        NumContact_PMOSSETSubring=2,    # option

        ChannelLength=30,
        XVT='SLVT',
        _GateSpacing=None
    )
    InputParams = InputParams_12G

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
        LayoutObj = StrongArmLatch(_Name=cellname)
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

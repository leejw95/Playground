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
from IksuJang.BasicArchive import ViaMet42Met5
from IksuJang.BasicArchive import ViaMet52Met6
from IksuJang.BasicArchive import ViaMet62Met7

from IksuJang.Slicer import StrongArmLatch
from IksuJang.Slicer import SRLatch
from IksuJang.Slicer import Inverter


class Slicer(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Slicer'):
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
        # StrongArm Latch
        InputParameters_StrongArm = dict(
            NumFinger_NM1=StrongArmLatch_NumFinger_NM1,
            NumFinger_NM23=StrongArmLatch_NumFinger_NM23,
            NumFinger_NM45=StrongArmLatch_NumFinger_NM45,
            Width_NM1=StrongArmLatch_Width_NM1,
            Width_NM23=StrongArmLatch_Width_NM23,
            Width_NM45=StrongArmLatch_Width_NM45,
            NumContactY_NM1=StrongArmLatch_NumContactY_NM1,                        # option
            NumContactY_NM23=StrongArmLatch_NumContactY_NM23,                      # option
            NumContactY_NM45=StrongArmLatch_NumContactY_NM45,                      # option
            NumContact_NMOSSETSubring=StrongArmLatch_NumContact_NMOSSETSubring,    # option

            NumFinger_PM12=StrongArmLatch_NumFinger_PM12,
            NumFinger_PM34=StrongArmLatch_NumFinger_PM34,
            NumFinger_PM56=StrongArmLatch_NumFinger_PM56,
            Width_PM=StrongArmLatch_Width_PM,

            NumContactY_PM=StrongArmLatch_NumContactY_PM,                          # option
            NumContact_PMOSSETSubring=StrongArmLatch_NumContact_PMOSSETSubring,    # option
            NumContact_Subring=StrongArmLatch_NumContact_Subring,
            ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing
        )
        InputParameters_SRLatch = dict(
            NumFinger_M1=SRLatch_NumFinger_M1, NumFinger_M2=SRLatch_NumFinger_M2,
            NumFinger_M3=SRLatch_NumFinger_M3, NumFinger_M4=SRLatch_NumFinger_M4,
            Width_PM1=SRLatch_Width_PM1, Width_PM2=SRLatch_Width_PM2,
            Width_PM3=SRLatch_Width_PM3, Width_PM4=SRLatch_Width_PM4,
            Width_NM1=SRLatch_Width_NM1, Width_NM2=SRLatch_Width_NM2,
            Width_NM3=SRLatch_Width_NM3, Width_NM4=SRLatch_Width_NM4,

            NumContactY_SupplyRail=NumContactY_SupplyRail,  # option
            ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing
        )
        InputParameters_Inverter = dict(
            NumFinger=Inv_NumFinger,
            Width_PM=Inv_Width_PM,
            Width_NM=Inv_Width_NM,

            NumContactY_Gate=Inv_NumContactY_Gate,          # option
            NumContactY_SupplyRail=NumContactY_SupplyRail,  # option
            ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['StrongArmLatch'] = self._SrefElementDeclaration(_DesignObj=StrongArmLatch.StrongArmLatch(_Name='StrongArmLatchIn{}'.format(_Name)))[0]
        self._DesignParameter['StrongArmLatch']['_DesignObj']._CalculateDesignParameter(**InputParameters_StrongArm)
        self._DesignParameter['StrongArmLatch']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['SRLatch'] = self._SrefElementDeclaration(_DesignObj=SRLatch.SRLatch(_Name='SRLatchIn{}'.format(_Name)))[0]
        self._DesignParameter['SRLatch']['_DesignObj']._CalculateDesignParameter(**InputParameters_SRLatch)

        self._DesignParameter['Inverter'] = self._SrefElementDeclaration(_DesignObj=Inverter.Inverter(_Name='InverterIn{}'.format(_Name)))[0]
        self._DesignParameter['Inverter']['_DesignObj']._CalculateDesignParameter(**InputParameters_Inverter)
        self._DesignParameter['Inverter']['_XYCoordinates'] = [[0, 0]]


        ''' -------------------------------------------------------------------------------------------------------- '''
        _YCoord_SRLatch = self.getXY('StrongArmLatch', 'M3V3M4Onnet03net04')[0][1] + self.getXY('StrongArmLatch', 'M3V3M4Onnet03net04')[1][1]
        YCoord_SRLatch = self.FloorMinSnapSpacing(_YCoord_SRLatch, MinSnapSpacing)

        XCoord_SRLatch_case1 = self.getXYRight('StrongArmLatch', 'PSubring', 'right', '_PPLayer')[0][0] + _DRCObj._NwMinEnclosurePactive + self.getXWidth('SRLatch', 'SRLatchUp', '_NWLayer') / 2
        XCoord_SRLatch_case2 = self.getXYRight('StrongArmLatch', 'PSubring', 'right', '_PPLayer')[0][0] + _DRCObj._PpMinSpace + self.getXWidth('SRLatch', 'SRLatchUp', 'VSSRail', '_PPLayer') / 2
        XCoord_SRLatch = self.CeilMinSnapSpacing(max(XCoord_SRLatch_case1, XCoord_SRLatch_case2), MinSnapSpacing*2)
        self._DesignParameter['SRLatch']['_XYCoordinates'] = [[XCoord_SRLatch, YCoord_SRLatch]]

        rightBoundary = self.getXYRight('SRLatch', 'SRLatchUp', 'VSSRail', '_Met1Layer')[0][0]
        leftBoundary = self.getXYLeft('StrongArmLatch', 'PSubring', 'right', '_Met1Layer')[0][0]
        self._DesignParameter['M1H_01'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=self.getYWidth('SRLatch', 'SRLatchUp', 'VSSRail', '_Met1Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXYRight('SRLatch', 'SRLatchUp', 'VSSRail', '_Met1Layer')[0][1]]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        XCoord_bottomleftCO_SRLatch = CoordCalc.getXYCoords_MinX(self.getXYLeft('SRLatch', 'SRLatchDn', 'VDDRail', '_COLayer'))[0][0]
        YCoord_bottomleftCO_SRLatch = CoordCalc.getXYCoords_MinY(self.getXYBot('SRLatch', 'SRLatchDn', 'VDDRail', '_COLayer'))[0][1]

        XCoord_bottomleftCO_Inverter = CoordCalc.getXYCoords_MinX(self.getXYLeft('Inverter', 'VDDRail', '_COLayer'))[0][0]
        YCoord_bottomleftCO_Inverter = CoordCalc.getXYCoords_MinY(self.getXYBot('Inverter', 'VDDRail', '_COLayer'))[0][1]

        self._DesignParameter['Inverter']['_XYCoordinates'] = [
            [(XCoord_bottomleftCO_SRLatch - XCoord_bottomleftCO_Inverter),
             (YCoord_bottomleftCO_SRLatch - YCoord_bottomleftCO_Inverter)]
        ]

        rightBoundary = self.getXYRight('Inverter', 'VSSRail', '_Met1Layer')[0][0]
        leftBoundary = self.getXYLeft('StrongArmLatch', 'PSubring', 'right', '_Met1Layer')[0][0]
        self._DesignParameter['M1H_02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('Inverter', 'VSSRail', '_Met1Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2,
                             self.getXYRight('Inverter', 'VSSRail', '_Met1Layer')[0][1]]]
        )

        self._DesignParameter['M3H_03'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('StrongArmLatch', 'M3_VSS'),
            _YWidth=self.getYWidth('StrongArmLatch', 'M3_VDD'),
            _XYCoordinates=[[0, self.getXY('StrongArmLatch', 'M3_VDD')[0][1]]]
        )


        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=self.getXWidth('Inverter', 'VSSRail', '_Met1Layer'),
            YWidth=self.getYWidth('Inverter', 'VSSRail', '_Met1Layer'))
        self._DesignParameter['M1V1M2OnInverterVSS'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnInverterVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnInverterVSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnInverterVSS']['_XYCoordinates'] = self.getXY('Inverter', 'VSSRail')

        self._DesignParameter['M2H_02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1H_02'),
            _YWidth=self.getYWidth('M1H_02'),
            _XYCoordinates=self.getXY('M1H_02')
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        YCoord_M5HForSSp = CoordCalc.getXYCoords_MaxY(self.getXY('StrongArmLatch', 'M3V3M4Onnet03net04'))[0][1]
        YCoord_M5HForSSn = CoordCalc.getXYCoords_MinY(self.getXY('StrongArmLatch', 'M3V3M4Onnet03net04'))[0][1]

        NumViaXY = (2, 2)
        self._DesignParameter['M4V4M5ForSSp'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='M4V4M5ForSSpIn{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5ForSSp']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M4V4M5ForSSn'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='M4V4M5ForSSnIn{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5ForSSn']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))
        XCoord_M5HForSSp = CoordCalc.getXYCoords_MaxX(self.getXYLeft('StrongArmLatch', 'M4V_net03'))[0][0] + self.getXWidth('M4V4M5ForSSp', '_Met5Layer') / 2
        XCoord_M5HForSSn = CoordCalc.getXYCoords_MinX(self.getXYRight('StrongArmLatch', 'M4V_net03'))[0][0] - self.getXWidth('M4V4M5ForSSn', '_Met5Layer') / 2


        self._DesignParameter['M4V4M5ForSSp']['_XYCoordinates'] = [
            [XCoord_M5HForSSp, YCoord_M5HForSSp],
            [self.getXY('SRLatch', 'M4V_09')[0][0], YCoord_M5HForSSp]
        ]
        self._DesignParameter['M4V4M5ForSSn']['_XYCoordinates'] = [
            [XCoord_M5HForSSn, YCoord_M5HForSSn],
            [self.getXY('SRLatch', 'M4V_04')[0][0], YCoord_M5HForSSn]
        ]

        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V4M5ForSSp', '_Met5Layer'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M4V4M5ForSSp', '_Met5Layer'))[0][0]
        self._DesignParameter['M5HForSSp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getXWidth('M4V4M5ForSSp', '_Met5Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_M5HForSSp]]
        )
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V4M5ForSSn', '_Met5Layer'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M4V4M5ForSSn', '_Met5Layer'))[0][0]
        self._DesignParameter['M5HForSSn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getXWidth('M4V4M5ForSSn', '_Met5Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, YCoord_M5HForSSn]]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        # Inverter output to StrongArm Latch CLK input
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            XWidth=self.getXWidth('Inverter', 'M1V1M2ForPM', '_Met2Layer'),
            YWidth=self.getYWidth('Inverter', 'M1V1M2ForPM', '_Met2Layer'))
        self._DesignParameter['M2V2M3ForInvOut'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3ForInvOutIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3ForInvOut']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3ForInvOut']['_XYCoordinates'] = self.getXY('Inverter', 'M1V1M2ForPM')

        self._DesignParameter['M3V3M4ForInvOut'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4ForInvOutIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4ForInvOut']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4ForInvOut']['_XYCoordinates'] = self.getXY('M2V2M3ForInvOut')

        self._DesignParameter['M4V4M5ForInvOut'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='M4V4M5ForInvOutIn{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5ForInvOut']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M4V4M5ForInvOut']['_XYCoordinates'] = self.getXY('M2V2M3ForInvOut')

        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M2V2M3ForInvOut', '_Met3Layer'))[0][0]
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2V2M3ForInvOut', '_Met3Layer'))[0][0]
        self._DesignParameter['M3H_04'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=_DRCObj._MetalxMinWidth*4,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M2V2M3ForInvOut')[0][1]]]
        )

        NumViaXY = (2, 2)
        self._DesignParameter['M5V5M6_CLK03'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='M5V5M6_CLK03In{}'.format(_Name)))[0]
        self._DesignParameter['M5V5M6_CLK03']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXY[0], _ViaMet52Met6NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M5V5M6_CLK03']['_XYCoordinates'] = [[0, self.getXY('M4V4M5ForInvOut')[0][1]]]


        leftBoundary = self.getXYLeft('M5V5M6_CLK03', '_Met5Layer')[0][0]
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V4M5ForInvOut', '_Met5Layer'))[0][0]
        self._DesignParameter['M5H_05'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M5V5M6_CLK03', '_Met5Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M4V4M5ForInvOut')[0][1]]]
        )

        ##
        NumViaXY = (2, 2)
        self._DesignParameter['M5V5M6_CLK01'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='M5V5M6_CLK01In{}'.format(_Name)))[0]
        self._DesignParameter['M5V5M6_CLK01']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXY[0], _ViaMet52Met6NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M5V5M6_CLK01']['_XYCoordinates'] = [[0, self.getXY('StrongArmLatch', 'M4V_net05')[0][1]]]

        self._DesignParameter['M4V4M5_CLK02'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='M4V4M5_CLK02In{}'.format(_Name)))[0]
        self._DesignParameter['M4V4M5_CLK02']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M4V4M5_CLK02']['_XYCoordinates'] = self.getXY('StrongArmLatch', 'M4V_net05')

        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M4V4M5_CLK02', '_Met5Layer'))[0][0]
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4V4M5_CLK02', '_Met5Layer'))[0][0]
        self._DesignParameter['M5H_06'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M5V5M6_CLK01', '_Met5Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M5V5M6_CLK01')[0][1]]]
        )

        topBoundary = self.getXYTop('M5V5M6_CLK01', '_Met6Layer')[0][1]
        botBoundary = self.getXYBot('M5V5M6_CLK03', '_Met6Layer')[0][1]
        self._DesignParameter['M6V_07'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('M5V5M6_CLK03', '_Met6Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M5V5M6_CLK01')[0][0], (topBoundary + botBoundary) / 2]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = max(self.getXYRight('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')[0][0], self.getXYRight('Inverter', 'VDDRail', '_Met1Layer')[0][0])
        leftBoundary = min(self.getXYLeft('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')[0][0], self.getXYLeft('Inverter', 'VDDRail', '_Met1Layer')[0][0])
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=rightBoundary-leftBoundary,
            YWidth=self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer'))
        self._DesignParameter['VDDVia1'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='VDDVia1In{}'.format(_Name)))[0]
        self._DesignParameter['VDDVia1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['VDDVia1']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, self.getXY('SRLatch', 'SRLatchUp', 'VDDRail')[0][1]],
            [(rightBoundary + leftBoundary) / 2, self.getXY('SRLatch', 'SRLatchDn', 'VDDRail')[0][1]],
        ]

        self._DesignParameter['VDDVia2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='VDDVia2In{}'.format(_Name)))[0]
        self._DesignParameter['VDDVia2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['VDDVia2']['_XYCoordinates'] = self.getXY('VDDVia1')

        self._DesignParameter['VDDVia3'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='VDDVia3In{}'.format(_Name)))[0]
        self._DesignParameter['VDDVia3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['VDDVia3']['_XYCoordinates'] = self.getXY('VDDVia1')

        self._DesignParameter['VDDVia1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')
        self._DesignParameter['VDDVia1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')

        self._DesignParameter['VDDVia2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')
        self._DesignParameter['VDDVia2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia2']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')

        self._DesignParameter['VDDVia3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')
        self._DesignParameter['VDDVia3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = rightBoundary-leftBoundary
        self._DesignParameter['VDDVia3']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = self.getYWidth('SRLatch', 'SRLatchUp', 'VDDRail', '_Met1Layer')


        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXY('StrongArmLatch', 'M3_VSS'),
            _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('StrongArmLatch', 'M3_VDD') + self.getXY('SRLatch', 'SRLatchUp', 'VDDRail') + self.getXY('SRLatch', 'SRLatchDn', 'VDDRail'),
            _Mag=0.04, _TEXT='VDD')

        self._DesignParameter['PIN_INp'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('StrongArmLatch', 'NMOSSET', 'PolyContactOnNM23')[0]],
            _Mag=0.04, _TEXT='INp')
        self._DesignParameter['PIN_INn'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('StrongArmLatch', 'NMOSSET', 'PolyContactOnNM23')[1]],
            _Mag=0.04, _TEXT='INn')
        self._DesignParameter['PIN_CLK'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('Inverter', 'M3H_Input')[0]],
            _Mag=0.04, _TEXT='CLK')

        self._DesignParameter['PIN_OUT'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatch', 'SRLatchUp', 'M1V1M2OnNet07'),
            _Mag=0.04, _TEXT='OUT')
        self._DesignParameter['PIN_OUTb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatch', 'SRLatchDn', 'M1V1M2OnNet07'),
            _Mag=0.04, _TEXT='OUTb')


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

    libname = 'TEST_Slicer'
    cellname = 'Slicer'
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
        LayoutObj = Slicer(_Name=cellname)
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

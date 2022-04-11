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

from IksuJang.Slicer import SRLatchHalf


class SRLatch(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='SRLatch'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger_M1=5,
                                  NumFinger_M2=1,
                                  NumFinger_M3=2,
                                  NumFinger_M4=2,

                                  Width_PM1=400,
                                  Width_PM2=400,
                                  Width_PM3=400,
                                  Width_PM4=400,

                                  Width_NM1=200,
                                  Width_NM2=200,
                                  Width_NM3=200,
                                  Width_NM4=200,

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
        # NMOS, PMOS

        InputParameters = dict(
            NumFinger_M1=NumFinger_M1, NumFinger_M2=NumFinger_M2, NumFinger_M3=NumFinger_M3, NumFinger_M4=NumFinger_M4,
            Width_PM1=Width_PM1, Width_PM2=Width_PM2, Width_PM3=Width_PM3, Width_PM4=Width_PM4,
            Width_NM1=Width_NM1, Width_NM2=Width_NM2, Width_NM3=Width_NM3, Width_NM4=Width_NM4,
            NumContactY_SupplyRail=NumContactY_SupplyRail,  # option
            ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing
        )


        self._DesignParameter['SRLatchUp'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0,
            _DesignObj=SRLatchHalf.SRLatchHalf(_Name='SRLatchUpIn{}'.format(_Name)))[0]
        self._DesignParameter['SRLatchUp']['_DesignObj']._CalculateDesignParameter(**InputParameters)

        self._DesignParameter['SRLatchDn'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=SRLatchHalf.SRLatchHalf(_Name='SRLatchDnIn{}'.format(_Name)))[0]
        self._DesignParameter['SRLatchDn']['_DesignObj']._CalculateDesignParameter(**InputParameters)

        self._DesignParameter['SRLatchUp']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['SRLatchDn']['_XYCoordinates'] = [[0, 0]]


        ''' -------------------------------------------------------------------------------------------------------- '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=self.getXWidth('SRLatchUp', 'M1V1M2OnPM1Gate', '_Met1Layer'),
            YWidth=self.getYWidth('SRLatchUp', 'M1V1M2OnPM1Gate', '_Met1Layer'))
        self._DesignParameter['M2V2M3OnPM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnPM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPM1Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnPM1Gate']['_XYCoordinates'] = self.getXY('SRLatchUp', 'M1V1M2OnPM1Gate')


        rightBoundary = self.getXYRight('SRLatchUp', 'M1V1M2OnPM3Gate', '_Met2Layer')[0][0]
        leftBoundary = self.getXYLeft('M2V2M3OnPM1Gate', '_Met3Layer')[0][0]
        # botBoundary = 0
        self._DesignParameter['M3H_01'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=self.getYWidth('M2V2M3OnPM1Gate', '_Met3Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M2V2M3OnPM1Gate')[0][1]]]
        )

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=self.getXWidth('SRLatchUp', 'M1V1M2OnPM3Gate', '_Met2Layer'),
            YWidth=self.getYWidth('SRLatchUp', 'M1V1M2OnPM3Gate', '_Met2Layer'))
        self._DesignParameter['M3V3M4OnPM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnPM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPM1Gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnPM1Gate']['_XYCoordinates'] = [
            [self.getXY('SRLatchUp', 'M1V1M2OnPM3Gate')[0][0], self.getXY('M3H_01')[0][1]]
        ]

        self._DesignParameter['M3V3M4OnNM3Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNM3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNM3Gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnNM3Gate']['_XYCoordinates'] = self.getXY('SRLatchUp', 'M2V2M3OnNM3Gate')




        ''' --- '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=self.getXWidth('SRLatchUp', 'M1V1M2OnNet07', '_Met2Layer'),
            YWidth=self.getYWidth('SRLatchUp', 'M1V1M2OnNet07', '_Met2Layer'))
        self._DesignParameter['M2V2M3OnNet07'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnNet07In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnNet07']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnNet07']['_XYCoordinates'] = self.getXY('SRLatchUp', 'M1V1M2OnNet07')

        self._DesignParameter['M3V3M4OnNet07'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNet07In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNet07']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnNet07']['_XYCoordinates'] = self.getXY('SRLatchUp', 'M1V1M2OnNet07')


        ''' -------------------------------------------------------------------------------------------------------- '''
        NumViaXY = (2, 1)
        YCoord_PMSide = min(self.getXYBot('SRLatchUp', 'PolyContactOnPM1', '_Met1Layer')[0][1],
                            self.getXYBot('SRLatchUp', 'PolyContactOnPM2', '_Met1Layer')[0][1],
                            self.getXYBot('SRLatchUp', 'M1ForPM3Gate')[0][1],
                            self.getXYBot('SRLatchUp', 'PolyContactOnPM4', '_Met1Layer')[0][1])
        YCoord_NMSide = max(self.getXYTop('SRLatchUp', 'PolyContactOnNM1', '_Met1Layer')[0][1],
                            self.getXYTop('SRLatchUp', 'PolyContactOnNM2', '_Met1Layer')[0][1],
                            self.getXYTop('SRLatchUp', 'M1ForNM3Gate')[0][1],
                            self.getXYTop('SRLatchUp', 'PolyContactOnNM4', '_Met1Layer')[0][1])


        self._DesignParameter['M1V1M2OnM2Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnM2GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnM2Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnM2Gate']['_XYCoordinates'] = [
            [self.getXY('M2V2M3OnPM1Gate')[0][0], self._DesignParameter['SRLatchUp']['_DesignObj'].YCoordMidVia]
        ]

        self._DesignParameter['M2V2M3OnM2Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnM2GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnM2Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnM2Gate']['_XYCoordinates'] = self.getXY('M1V1M2OnM2Gate')

        self._DesignParameter['M3V3M4OnM2Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnM2GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnM2Gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnM2Gate']['_XYCoordinates'] = self.getXY('M1V1M2OnM2Gate')

        rightBoundary = self.getXYRight('SRLatchUp', 'M1VForNM2PM2Gate')[0][0]
        leftBoundary = self.getXYLeft('M1V1M2OnM2Gate', '_Met1Layer')[0][0]
        self._DesignParameter['M1H_02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M1V1M2OnM2Gate', '_Met1Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M1V1M2OnM2Gate')[0][1]]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
            XWidth=self.getXWidth('SRLatchDn', 'M1V1M2OnPM1Gate', '_Met2Layer'),
            YWidth=self.getYWidth('SRLatchDn', 'M1V1M2OnPM1Gate', '_Met2Layer'))
        self._DesignParameter['M2V2M3OnPM1GateDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnPM1GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPM1GateDn']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnPM1GateDn']['_XYCoordinates'] = self.getXY('SRLatchDn', 'M1V1M2OnPM1Gate')

        self._DesignParameter['M3V3M4OnPM1GateDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnPM1GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPM1GateDn']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnPM1GateDn']['_XYCoordinates'] = self.getXY('M2V2M3OnPM1GateDn')


        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = self.getXYRight('SRLatchDn', 'M2V2M3OnNM3Gate', '_Met3Layer')[0][0]
        leftBoundary = self.getXYLeft('M3V3M4OnM2Gate', '_Met3Layer')[0][0]
        self._DesignParameter['M3H_03'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('SRLatchDn', 'M2V2M3OnNM3Gate', '_Met3Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('SRLatchDn', 'M2V2M3OnNM3Gate', '_Met3Layer')[0][1]]]
        )

        NumViaXY = (2, 1)
        self._DesignParameter['M3V3M4OnNM3GateDn'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNM3GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNM3GateDn']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnNM3GateDn']['_XYCoordinates'] = [[self.getXY('M3V3M4OnM2Gate')[0][0], self.getXY('M3H_03')[0][1]]]

        topBoundary = self.getXYTop('M3V3M4OnM2Gate', '_Met4Layer')[0][1]
        botBoundary = self.getXYBot('M3V3M4OnPM1GateDn', '_Met4Layer')[0][1]
        self._DesignParameter['M4V_04'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M3V3M4OnNM3GateDn', '_Met4Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M3V3M4OnM2Gate', '_Met4Layer')[0][0], (topBoundary + botBoundary) / 2]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        NumViaXY = (1, 2)
        self._DesignParameter['M3V3M4_05'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_05In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4_05']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4_05']['_XYCoordinates'] = self.getXYRight('SRLatchDn', 'M3HOnNet12')

        self._DesignParameter['M2V2M3_06'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_06In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3_06']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3_06']['_XYCoordinates'] = self.getXYRight('SRLatchUp', 'M3HOnNet12')

        topBoundary = self.getXYTop('M2V2M3_06', '_Met2Layer')[0][1]
        botBoundary = self.getXYBot('SRLatchDn', 'M1V1M2OnNet07', '_Met2Layer')[0][1]
        self._DesignParameter['M2V_07'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=_DRCObj._MetalxMinWidth*2,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M2V2M3_06')[0][0], (topBoundary + botBoundary) / 2]]
        )

        topBoundary = self.getXYTop('M3V3M4OnNet07', '_Met4Layer')[0][1]
        botBoundary = self.getXYBot('M3V3M4_05', '_Met4Layer')[0][1]
        self._DesignParameter['M4V_08'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=_DRCObj._MetalxMinWidth * 2,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M3V3M4_05')[0][0], (topBoundary + botBoundary) / 2]]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        YCoord_PMSide = max(self.getXYTop('SRLatchDn', 'PolyContactOnPM1', '_Met1Layer')[0][1],
                            self.getXYTop('SRLatchDn', 'PolyContactOnPM2', '_Met1Layer')[0][1],
                            self.getXYTop('SRLatchDn', 'M1ForPM3Gate')[0][1],
                            self.getXYTop('SRLatchDn', 'PolyContactOnPM4', '_Met1Layer')[0][1])
        YCoord_NMSide = min(self.getXYBot('SRLatchDn', 'PolyContactOnNM1', '_Met1Layer')[0][1],
                            self.getXYBot('SRLatchDn', 'PolyContactOnNM2', '_Met1Layer')[0][1],
                            self.getXYBot('SRLatchDn', 'M1ForNM3Gate')[0][1],
                            self.getXYBot('SRLatchDn', 'PolyContactOnNM4', '_Met1Layer')[0][1])
        NumViaXY = (2, 1)
        self._DesignParameter['M1V1M2OnM2GateDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnM2GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnM2GateDn']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnM2GateDn']['_XYCoordinates'] = [
            [self.getXY('M3V3M4OnPM1Gate')[0][0], -self._DesignParameter['SRLatchDn']['_DesignObj'].YCoordMidVia]
        ]

        self._DesignParameter['M2V2M3OnM2GateDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnM2GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnM2GateDn']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnM2GateDn']['_XYCoordinates'] = self.getXY('M1V1M2OnM2GateDn')

        self._DesignParameter['M3V3M4OnM2GateDn'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnM2GateDnIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnM2GateDn']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnM2GateDn']['_XYCoordinates'] = self.getXY('M1V1M2OnM2GateDn')

        topBoundary = self.getXYTop('M3V3M4OnPM1Gate', '_Met4Layer')[0][1]
        botBoundary = self.getXYBot('M3V3M4OnM2GateDn', '_Met4Layer')[0][1]
        self._DesignParameter['M4V_09'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M3V3M4OnM2GateDn', '_Met4Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M3V3M4OnM2GateDn')[0][0], (topBoundary + botBoundary) / 2]]
        )

        rightBoundary = self.getXYRight('M1V1M2OnM2GateDn', '_Met1Layer')[0][0]
        leftBoundary = self.getXYLeft('SRLatchDn', 'M1VForNM2PM2Gate')[0][0]
        self._DesignParameter['M1H_10'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M1V1M2OnM2GateDn', '_Met1Layer'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('M1V1M2OnM2GateDn', '_Met1Layer')[0][1]]]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''






        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchUp', 'VSSRail') + self.getXY('SRLatchDn', 'VSSRail'),
            _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchUp', 'VDDRail') + self.getXY('SRLatchDn', 'VDDRail'),
            _Mag=0.04, _TEXT='VDD')

        self._DesignParameter['PIN_IN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchDn', 'M1VForNM2PM2Gate'),
            _Mag=0.04, _TEXT='IN')
        self._DesignParameter['PIN_INb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchUp', 'M1VForNM2PM2Gate'),
            _Mag=0.04, _TEXT='INb')

        self._DesignParameter['PIN_OUT'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchUp', 'M1V1M2OnNet07'),
            _Mag=0.04, _TEXT='OUT')
        self._DesignParameter['PIN_OUTb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SRLatchDn', 'M1V1M2OnNet07'),
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

    libname = 'TEST_SRLatch'
    cellname = 'SRLatch'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_20G = dict(
        NumFinger_M1=5,         # 5 1 2 2
        NumFinger_M2=1,
        NumFinger_M3=2,
        NumFinger_M4=2,

        Width_PM1=400,
        Width_PM2=400,
        Width_PM3=400,
        Width_PM4=400,

        Width_NM1=200,
        Width_NM2=200,
        Width_NM3=200,
        Width_NM4=200,
    )
    InputParams_16G = dict(
        NumFinger_M1=2,
        NumFinger_M2=1,
        NumFinger_M3=1,
        NumFinger_M4=1,

        Width_PM1=500,
        Width_PM2=400,
        Width_PM3=400,
        Width_PM4=400,

        Width_NM1=250,
        Width_NM2=200,
        Width_NM3=200,
        Width_NM4=200,
    )
    InputParams_12G = dict(
        NumFinger_M1=2,
        NumFinger_M2=1,
        NumFinger_M3=1,
        NumFinger_M4=1,

        Width_PM1=400,
        Width_PM2=400,
        Width_PM3=400,
        Width_PM4=400,

        Width_NM1=200,
        Width_NM2=200,
        Width_NM3=200,
        Width_NM4=200,
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
        LayoutObj = SRLatch(_Name=cellname)
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

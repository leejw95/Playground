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

from IksuJang.ResistorBank import ResistorBank
from IksuJang.Slicer import Slicer_x4


class RXCore(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='RXCore'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,

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


                                  NumX_Bank=4,                  ######
                                  NumY_Bank=8,
                                  NumFinger_resistorbank=10,
                                  Width_PM_resistorbank=540,
                                  Width_NM_resistorbank=270,

                                  Width_Res=1250,
                                  Length_Res=1234,

                                  NumContactY_Gate_resitorbank=1,                   # option
                                  NumContactY_innerSubring_resistorbank=2,           # option
                                  NumContactY_outerSubring_resistorbank=2,           # option
                                  NumContactY_Res=2,                         # option

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

        InputParameters_ResistorBank = dict(
            NumX_Bank=NumX_Bank,
            NumY_Bank=NumY_Bank,

            NumFinger=NumFinger_resistorbank,
            Width_PM=Width_PM_resistorbank,
            Width_NM=Width_NM_resistorbank,

            Width_Res=Width_Res,
            Length_Res=Length_Res,

            NumContactY_Gate=NumContactY_Gate_resitorbank,  # option
            NumContactY_innerSubring=NumContactY_innerSubring_resistorbank,  # option
            NumContactY_outerSubring=NumContactY_outerSubring_resistorbank,  # option
            NumContactY_Res=NumContactY_Res,  # option

            ChannelLength=ChannelLength,
            XVT=XVT,
            _GateSpacing=_GateSpacing
        )


        InputParameters_SlicerX4 = dict(
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
        self._DesignParameter['ResistorBank'] = self._SrefElementDeclaration(_DesignObj=ResistorBank.ResistorBank(_Name='ResistorBankIn{}'.format(_Name)))[0]
        self._DesignParameter['ResistorBank']['_DesignObj']._CalculateDesignParameter(**InputParameters_ResistorBank)
        self._DesignParameter['ResistorBank']['_XYCoordinates'] = [[0, 0]]

        self._DesignParameter['SlicerX4'] = self._SrefElementDeclaration(_DesignObj=Slicer_x4.Slicer_x4(_Name='SlicerX4In{}'.format(_Name)))[0]
        self._DesignParameter['SlicerX4']['_DesignObj']._CalculateDesignParameter(**InputParameters_SlicerX4)
        self._DesignParameter['SlicerX4']['_XYCoordinates'] = [[20000, 0]]



        XCoord_ResistorBankRightBoundary = self.getXYRight('ResistorBank', 'M5_VSS')[0][0] + _DRCObj._MetalxMinSpace11
        XCoord_SlicerX4LeftBoundary = self.getXYLeft('SlicerX4', 'M2V_01')[0][0]
        XCoord_SlicerX4_reClac = self.getXY('SlicerX4')[0][0] + (XCoord_ResistorBankRightBoundary - XCoord_SlicerX4LeftBoundary)

        YCoord_ResistorBank = self.getXY('ResistorBank', 'M6_VSS')[0][1]
        YCoord_SlicerX4 = self.getXY('SlicerX4', 'M6V_05')[0][1]
        YCoord_SlicerX4_reClac = YCoord_ResistorBank - YCoord_SlicerX4
        self._DesignParameter['SlicerX4']['_XYCoordinates'] = [[XCoord_SlicerX4_reClac, YCoord_SlicerX4_reClac]]

        self._DesignParameter['M6V_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('SlicerX4', 'M6V_05'),
            _YWidth=self.getYWidth('ResistorBank', 'M6_VSS'),
            _XYCoordinates=[
                [self.getXY('SlicerX4', 'M6V_05')[0][0], YCoord_ResistorBank]
            ]
        )
        self._DesignParameter['M6V_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('SlicerX4', 'M6V_06'),
            _YWidth=self.getYWidth('ResistorBank', 'M6_VSS'),
            _XYCoordinates=[
                [self.getXY('SlicerX4', 'M6V_06')[0][0], YCoord_ResistorBank]
            ]
        )









        ''' -------------------------------------------------------------------------------------------------------- '''

        InputMet4_XWidth = self.getXWidth('SlicerX4', 'Slicer', 'StrongArmLatch', 'Via3ForVINp', '_Met4Layer')
        InputMet4_YWidth = self.getYWidth('SlicerX4', 'Slicer', 'StrongArmLatch', 'Via3ForVINp', '_Met4Layer')
        InputMet4_XY_INp = self.getXY('SlicerX4', 'Slicer', 'StrongArmLatch', 'Via3ForVINp')  # every contact
        InputMet4_XY_INn = self.getXY('SlicerX4', 'Slicer', 'StrongArmLatch', 'Via3ForVINn')  # every contact
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=InputMet4_XWidth, YWidth=InputMet4_YWidth)

        # Via4
        self._DesignParameter['Via4ForVIN'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVINIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVIN']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via4ForVIN']['_XYCoordinates'] = InputMet4_XY_INp + InputMet4_XY_INn

        # Via5
        self._DesignParameter['Via5ForVIN'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForVINIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForVIN']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXY[0], _ViaMet52Met6NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via5ForVIN']['_XYCoordinates'] = InputMet4_XY_INp + InputMet4_XY_INn


        # INp
        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXYTop('Via5ForVIN', '_Met6Layer'))[0][1]
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXYBot('Via5ForVIN', '_Met6Layer'))[0][1]
        self._DesignParameter['M6V_INp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('Via5ForVIN', '_Met6Layer'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [InputMet4_XY_INp[0][0], (topBoundary + botBoundary) / 2]
            ]
        )
        self._DesignParameter['M6V_INn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('Via5ForVIN', '_Met6Layer'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [InputMet4_XY_INn[0][0], (topBoundary + botBoundary) / 2]
            ]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M6V_VDD'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('ResistorBank', 'M7_VSS'))[0][0]
        self._DesignParameter['M7_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('ResistorBank', 'M7_VDD')
        )
        self._DesignParameter['M7_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M7_VDD')
        )

        ObjListM7 = ['M7_VDD', 'M7_VSS']
        for Element in ObjListM7:
            tmpXYs = []
            for i, XY in enumerate(self.getXY('ResistorBank', Element)):
                tmpXYs.append([(rightBoundary + leftBoundary) / 2, XY[1]])
            self._DesignParameter[Element]['_XYCoordinates'] = tmpXYs

        # VRX
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M6V_INp'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('ResistorBank', 'M7_VSS'))[0][0]
        self._DesignParameter['M7_VRX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M7_VDD')
        )
        tmpXYs = []
        for i, XY in enumerate(self.getXY('ResistorBank', 'M7_VRX')):
            tmpXYs.append([(rightBoundary + leftBoundary) / 2, XY[1]])
        self._DesignParameter['M7_VRX']['_XYCoordinates'] = tmpXYs


        topBoundary = CoordCalc.getSortedList_ascending(self.getXYTop('M7_VRX'))[1][-1]
        botBoundary = CoordCalc.getSortedList_ascending(self.getXYBot('M7_VRX'))[1][0]
        YLength_M7VRX = topBoundary - botBoundary
        YLength_M6VINp = CoordCalc.getSortedList_ascending(self.getXYTop('M6V_INp'))[1][-1] - CoordCalc.getSortedList_ascending(self.getXYBot('M6V_INp'))[1][0]
        if YLength_M6VINp < YLength_M7VRX:
            self._DesignParameter['M6V_INp']['_YWidth'] = topBoundary - botBoundary
            self._DesignParameter['M6V_INp']['_XYCoordinates'] = [[self.getXY('M6V_INp')[0][0], (topBoundary + botBoundary) / 2]]
        else:
            pass

        ''' -------------------------------------------------------------------------------------------------------- '''
        # Via6
        # Via6 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6V_VSS'], self._DesignParameter['M7_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via6 VDD
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6V_VDD'], self._DesignParameter['M7_VDD'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via6 VRX
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6V_INp'], self._DesignParameter['M7_VRX'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVRX']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVRX']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''








        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=[self.getXYBot('M6V_VSS')[0]],
            _Mag=0.4,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXYBot('M6V_VDD')[0]],
            _Mag=0.4, _TEXT='VDD')

        self._DesignParameter['PIN_VCM'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXYBot('ResistorBank', 'M6_VCM')[0]],
            _Mag=0.4, _TEXT='VCM')

        # Vref
        self._DesignParameter['PIN_Vref'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('M6V_INn'),
            _Mag=0.4, _TEXT='Vref')

        # S<0:31>, SB<0:31>
        for i, XY in enumerate(self.getXYLeft('ResistorBank', 'RBU', 'M5H_S')):
            self._DesignParameter[f'PIN_S_{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[XY],
                _Mag=0.4, _TEXT=f'S<{i}>'
            )
        for i, XY in enumerate(self.getXYLeft('ResistorBank', 'RBU', 'M5H_SB')):
            self._DesignParameter[f'PIN_SB_{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[XY],
                _Mag=0.4, _TEXT=f'SB<{i}>'
            )

        # CLK 0, 90, 180, 270
        self._DesignParameter['PIN_CK0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SlicerX4', 'PIN_CLK0'),
            _Mag=0.4, _TEXT='CK0')
        self._DesignParameter['PIN_CK90'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SlicerX4', 'PIN_CLK1'),
            _Mag=0.4, _TEXT='CK90')
        self._DesignParameter['PIN_CK180'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SlicerX4', 'PIN_CLK2'),
            _Mag=0.4, _TEXT='CK180')
        self._DesignParameter['PIN_CK270'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('SlicerX4', 'PIN_CLK3'),
            _Mag=0.4, _TEXT='CK270')

        # OUT, OUTb
        for i in range(0, 4):
            self._DesignParameter[f'PIN_OUT{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=self.getXY('SlicerX4', f'PIN_OUT{i}'),
                _Mag=0.4, _TEXT=f'OUT<{i}>')
            self._DesignParameter[f'PIN_OUTb{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=self.getXY('SlicerX4', f'PIN_OUTb{i}'),
                _Mag=0.4, _TEXT=f'OUTb<{i}>')


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

    libname = 'CLI_RXCore'
    cellname = 'RXCore'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_ResistorBank = dict(
        NumX_Bank=4,
        NumY_Bank=8,
        NumFinger_resistorbank=8,
        Width_PM_resistorbank=550,
        Width_NM_resistorbank=274,

        Width_Res=1250,
        Length_Res=1234,

        NumContactY_Gate_resitorbank=1,  # option
        NumContactY_innerSubring_resistorbank=2,  # option
        NumContactY_outerSubring_resistorbank=2,  # option
        NumContactY_Res=2  # option
    )
    InputParams_SlicerX4_20G = dict(
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
    InputParams_SlicerX4_16G = dict(
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
    InputParams_SlicerX4_12G = dict(
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

    InputParams = dict(InputParams_ResistorBank, **InputParams_SlicerX4_12G)


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
        LayoutObj = RXCore(_Name=cellname)
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

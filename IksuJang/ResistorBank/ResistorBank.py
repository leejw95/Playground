import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc
from SthPack import BoundaryCalc

from IksuJang.BasicArchive import PSubRing

from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from IksuJang.BasicArchive import ViaMet42Met5
from IksuJang.BasicArchive import ViaMet52Met6
from IksuJang.BasicArchive import ViaMet62Met7

from IksuJang.ResistorBank import ResistorBankUnit


class ResistorBank(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='ResistorBank'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumX_Bank=4,
                                  NumY_Bank=8,
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
        self._DesignParameter['RBU'] = self._SrefElementDeclaration(_DesignObj=ResistorBankUnit.ResistorBankUnit(_Name='RBUIn{}'.format(_Name)))[0]
        self._DesignParameter['RBU']['_DesignObj']._CalculateDesignParameter(
            **dict(NumFinger=NumFinger, Width_PM=Width_PM, Width_NM=Width_NM,
                   Width_Res=Width_Res, Length_Res=Length_Res,
                   NumContactY_Gate=NumContactY_Gate, NumContactY_innerSubring=NumContactY_innerSubring,
                   NumContactY_outerSubring=NumContactY_outerSubring, NumContactY_Res=NumContactY_Res,
                   ChannelLength=ChannelLength, XVT=XVT, _GateSpacing=_GateSpacing))
        self._DesignParameter['RBU']['_XYCoordinates'] = [[0, 0]]

        rightBoundary_guardring = self.getXYRight('RBU', 'PSubring', 'met_right')[0][0]
        leftBoundary_guardring = self.getXYRight('RBU', 'PSubring', 'met_left')[0][0]
        topBoundary_guardring = self.getXYTop('RBU', 'PSubring', 'met_top')[0][1]
        botBoundary_guardring = self.getXYTop('RBU', 'PSubring', 'met_bot')[0][1]

        UnitDistanceX = rightBoundary_guardring - leftBoundary_guardring
        UnitDistanceY = topBoundary_guardring - botBoundary_guardring

        tmpXYs = []
        for j in range(0, NumY_Bank):
            for i in range(0, NumX_Bank):
                tmpXYs.append([UnitDistanceX * i, UnitDistanceY * j])

        self._DesignParameter['RBU']['_XYCoordinates'] = tmpXYs




        ''' -------------------------------------------------------------------------------------------------------- '''
        # M2 VSS
        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXYTop('RBU', 'PSubring', 'met_top'))[0][1] + self.getYWidth('RBU', 'PSubring', 'met_top')
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXYBot('RBU', 'PSubring', 'met_bot'))[0][1]
        self._DesignParameter['M2_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('RBU', 'PSubring', 'met_left'),
            _YWidth=topBoundary-botBoundary
        )

        originX_M2 = CoordCalc.getXYCoords_MinX(self.getXY('RBU', 'PSubring', 'met_left'))[0][0]
        UnitDistanceX_M2 = CoordCalc.getXYCoords_MinX(self.getXY('RBU', 'PSubring', 'met_right'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('RBU', 'PSubring', 'met_left'))[0][0]
        tmpXYs = []
        for i in range(0, NumX_Bank + 1):
            tmpXYs.append([originX_M2 + i * UnitDistanceX_M2, (topBoundary + botBoundary) / 2])
        self._DesignParameter['M2_VSS']['_XYCoordinates'] = tmpXYs

        # M3 VSS
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('RBU', 'PSubring', 'met_right'))[0][0] + self.getXWidth('RBU', 'PSubring', 'met_right')
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('RBU', 'PSubring', 'met_left'))[0][0]
        self._DesignParameter['M3_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=self.getYWidth('RBU', 'PSubring', 'met_bot') * 2
        )

        originY_M3 = CoordCalc.getXYCoords_MinY(self.getXYBot('RBU', 'PSubring', 'met_bot'))[0][1] + self.getYWidth('M3_VSS') / 2
        UnitDistanceY_M3 = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1] - CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_bot'))[0][1]
        tmpXYs = []
        for i in range(0, NumY_Bank + 1):
            tmpXYs.append([(rightBoundary + leftBoundary) / 2, originY_M3 + i * UnitDistanceY_M3])
        self._DesignParameter['M3_VSS']['_XYCoordinates'] = tmpXYs

        # M3 VDD
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('RBU', 'PSubring', 'met_right'))[0][0] + self.getXWidth('RBU', 'PSubring', 'met_right')
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('RBU', 'PSubring', 'met_left'))[0][0]
        self._DesignParameter['M3_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('RBU', 'TransmissionGate', 'Via2ForVDD', '_Met3Layer')
        )

        originY_M3 = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'TransmissionGate', 'Via2ForVDD', '_Met3Layer'))[0][1]
        UnitDistanceY_M3 = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1] - \
                           CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_bot'))[0][1]
        tmpXYs = []
        for i in range(0, NumY_Bank):
            tmpXYs.append([(rightBoundary + leftBoundary) / 2, originY_M3 + i * UnitDistanceY_M3])
        self._DesignParameter['M3_VDD']['_XYCoordinates'] = tmpXYs

        # M4 VCM
        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1]
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_bot'))[0][1]
        self._DesignParameter['M4_VCM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('RBU', 'TransmissionGate', 'M4_VCM'),
            _YWidth=topBoundary-botBoundary
        )

        originX_M4VCM = CoordCalc.getXYCoords_MinX(self.getXY('RBU', 'TransmissionGate', 'M4_VCM'))[0][0]
        tmpXYs = []
        for i in range(0, NumX_Bank):
            tmpXYs.append([originX_M4VCM + i * UnitDistanceX, (topBoundary + botBoundary) / 2])
        self._DesignParameter['M4_VCM']['_XYCoordinates'] = tmpXYs

        # M4 VSS VDD
        topBoundary_VSS = CoordCalc.getXYCoords_MaxY(self.getXYTop('M3_VSS'))[0][1]
        botBoundary_VSS = CoordCalc.getXYCoords_MinY(self.getXYBot('M3_VSS'))[0][1]
        self._DesignParameter['M4_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M2_VSS') * 2,
            _YWidth=topBoundary_VSS - botBoundary_VSS
        )
        topBoundary_VDD = CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1]
        botBoundary_VDD = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_bot'))[0][1]
        self._DesignParameter['M4_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M2_VSS') * 2,
            _YWidth=topBoundary_VDD - botBoundary_VDD
        )

        originX_M4VSS = CoordCalc.getSortedList_ascending(self.getXYLeft('M2_VSS'))[0][0] + self.getXWidth('M4_VSS') / 2
        originX_M4VDD = CoordCalc.getSortedList_ascending(self.getXYLeft('M2_VSS'))[0][1] + self.getXWidth('M4_VDD') / 2

        tmpXYs_M4VSS = []
        tmpXYs_M4VDD = []
        for i in range(0, NumX_Bank + 1):
            if i % 2 == 0:
                tmpXYs_M4VSS.append([originX_M4VSS + i * UnitDistanceX, (topBoundary_VSS + botBoundary_VSS) / 2])
            else:
                tmpXYs_M4VDD.append([originX_M4VSS + i * UnitDistanceX, (topBoundary_VDD + botBoundary_VDD) / 2])
        self._DesignParameter['M4_VSS']['_XYCoordinates'] = tmpXYs_M4VSS
        self._DesignParameter['M4_VDD']['_XYCoordinates'] = tmpXYs_M4VDD

        # M5 VDD VCM VSS VCM
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M4_VSS'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M4_VSS'))[0][0]
        self._DesignParameter['M5_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1]-CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'M3H'))[0][1]
        )
        self._DesignParameter['M5_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M5_VDD')
        )
        rightBoundary_M5VCM = CoordCalc.getXYCoords_MaxX(self.getXY('M2_VSS'))[0][0]
        leftBoundary_M5VCM = CoordCalc.getXYCoords_MinX(self.getXY('M2_VSS'))[0][0]
        self._DesignParameter['M5_VCM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=rightBoundary_M5VCM - leftBoundary_M5VCM,
            _YWidth=self.getYWidth('M5_VDD')
        )

        originY_M5 = CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1] - self.getYWidth('M5_VDD') / 2
        tmpXYs_VDD = []
        tmpXYs_VSS = []
        tmpXYs_VCM = []
        for i in range(0, NumY_Bank):
            if i % 2 == 1:
                tmpXYs_VCM.append([(rightBoundary_M5VCM + leftBoundary_M5VCM) / 2, originY_M5 - i * UnitDistanceY])
            else:
                if i % 4 == 0:
                    tmpXYs_VDD.append([(rightBoundary + leftBoundary) / 2, originY_M5 - i * UnitDistanceY])
                else:
                    tmpXYs_VSS.append([(rightBoundary + leftBoundary) / 2, originY_M5 - i * UnitDistanceY])
        self._DesignParameter['M5_VDD']['_XYCoordinates'] = tmpXYs_VDD
        self._DesignParameter['M5_VSS']['_XYCoordinates'] = tmpXYs_VSS
        self._DesignParameter['M5_VCM']['_XYCoordinates'] = tmpXYs_VCM

        # M6 VRX
        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXYTop('RBU', 'Via5ForB', '_Met6Layer'))[0][1]
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXYBot('RBU', 'Via5ForB', '_Met6Layer'))[0][1]
        self._DesignParameter['M6_VRX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=self.getXWidth('RBU', 'Via5ForB', '_Met6Layer'),
            _YWidth=topBoundary - botBoundary
        )
        originX_M6VRX = CoordCalc.getXYCoords_MinX(self.getXY('RBU', 'Via5ForB', '_Met6Layer'))[0][0]
        tmpXYs = []
        for i in range(0, NumX_Bank):
            tmpXYs.append([originX_M6VRX + i * UnitDistanceX, (topBoundary + botBoundary) / 2])
        self._DesignParameter['M6_VRX']['_XYCoordinates'] = tmpXYs

        # M6 VSS VDD VCM
        topBoundary = CoordCalc.getXYCoords_MaxY(self.getXY('RBU', 'PSubring', 'met_top'))[0][1]
        botBoundary = CoordCalc.getXYCoords_MinY(self.getXY('RBU', 'PSubring', 'met_bot'))[0][1]
        rightBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('RBU', 'TransmissionGate', 'PSubring', 'met_right'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYRight('RBU', 'TransmissionGate', 'PSubring', 'met_left'))[0][0]
        self._DesignParameter['M6_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=topBoundary - botBoundary
        )
        self._DesignParameter['M6_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary
        )
        self._DesignParameter['M6_VCM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary
        )
        originX_M6 = (rightBoundary + leftBoundary) / 2
        tmpXYs_VSS = []
        tmpXYs_VDD = []
        tmpXYs_VCM = []
        for i in range(0, NumX_Bank):
            if i == 0 or i == NumX_Bank-1:
                tmpXYs_VCM.append([originX_M6 + i * UnitDistanceX, (topBoundary + botBoundary) / 2])
            else:
                if i % 2 == 1:
                    tmpXYs_VSS.append([originX_M6 + i * UnitDistanceX, (topBoundary + botBoundary) / 2])
                else:
                    tmpXYs_VDD.append([originX_M6 + i * UnitDistanceX, (topBoundary + botBoundary) / 2])
        self._DesignParameter['M6_VCM']['_XYCoordinates'] = tmpXYs_VCM
        self._DesignParameter['M6_VSS']['_XYCoordinates'] = tmpXYs_VSS
        self._DesignParameter['M6_VDD']['_XYCoordinates'] = tmpXYs_VDD

        # M7
        M7_spacing = 1000
        M7_width = 1500
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2_VSS'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M2_VSS'))[0][0]
        self._DesignParameter['M7_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=M7_width
        )
        self._DesignParameter['M7_VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=M7_width
        )
        self._DesignParameter['M7_VCM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=M7_width
        )
        self._DesignParameter['M7_VRX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=M7_width
        )
        YCoord_M7VDD1 = self.getXYTop('M6_VSS')[0][1] - self.getYWidth('M7_VDD') / 2
        YCoord_M7VSS1 = YCoord_M7VDD1 - (M7_width + M7_spacing)
        YCoord_M7VSS2 = self.getXYBot('M6_VSS')[0][1] + self.getYWidth('M7_VDD') / 2
        YCoord_M7VDD2 = YCoord_M7VSS2 + (M7_width + M7_spacing)

        self._DesignParameter['M7_VDD']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, YCoord_M7VDD1],
            [(rightBoundary + leftBoundary) / 2, YCoord_M7VDD2],
        ]
        self._DesignParameter['M7_VSS']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, YCoord_M7VSS1],
            [(rightBoundary + leftBoundary) / 2, YCoord_M7VSS2],
        ]

        #
        Center = (YCoord_M7VSS1 + YCoord_M7VDD2) / 2
        _Num = int((YCoord_M7VSS1 - YCoord_M7VDD2 - M7_width * 2 - M7_spacing * 2) // (M7_width + M7_spacing) + 1)
        tmpXYs_VRX = []
        tmpXYs_VCM = []
        for i in range(0, _Num):
            if i % 2 == 0:
                tmpXYs_VRX.append([(rightBoundary + leftBoundary) / 2, Center + (M7_width + M7_spacing) * (i - (_Num-1) / 2)])
            else:
                tmpXYs_VCM.append([(rightBoundary + leftBoundary) / 2, Center + (M7_width + M7_spacing) * (i - (_Num-1) / 2)])

        self._DesignParameter['M7_VRX']['_XYCoordinates'] = tmpXYs_VRX
        self._DesignParameter['M7_VCM']['_XYCoordinates'] = tmpXYs_VCM


        ''' -------------------------------------------------------------------------------------------------------- '''
        # Via1 VSS
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('M2_VSS'), YWidth=self.getYWidth('M2_VSS'))
        self._DesignParameter['Via1ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForVSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXYs[0], _ViaMet12Met2NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via1ForVSS']['_XYCoordinates'] = self.getXY('M2_VSS')

        # Via2 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M2_VSS'], self._DesignParameter['M3_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via2ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via3 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M3_VSS'], self._DesignParameter['M4_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via3ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via3 VDD
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M3_VDD'], self._DesignParameter['M4_VDD'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via3ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']


        # Via4 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M4_VSS'], self._DesignParameter['M5_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via4ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via4 VDD
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M4_VDD'], self._DesignParameter['M5_VDD'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via4ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via4 VCM
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M4_VCM'], self._DesignParameter['M5_VCM'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via4ForVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4ForVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4ForVCM']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXYs[0], _ViaMet42Met5NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via4ForVCM']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']


        # Via5 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M5_VSS'], self._DesignParameter['M6_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via5ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXYs[0], _ViaMet52Met6NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via5ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via5 VDD
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M5_VDD'], self._DesignParameter['M6_VDD'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via5ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXYs[0], _ViaMet52Met6NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via5ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via5 VCM
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M5_VCM'], self._DesignParameter['M6_VCM'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via5ForVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Via5ForVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via5ForVCM']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(
            **dict(_ViaMet52Met6NumberOfCOX=NumViaXYs[0], _ViaMet52Met6NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via5ForVCM']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']


        # Via6
        # Via6 VSS
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6_VSS'], self._DesignParameter['M7_VSS'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVSS']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via6 VDD
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6_VDD'], self._DesignParameter['M7_VDD'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVDD']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via6 VCM
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6_VCM'], self._DesignParameter['M7_VCM'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVCM']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVCM']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']

        # Via6 VRX
        OverlappedBoundaryForVia = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M6_VRX'], self._DesignParameter['M7_VRX'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia['_XWidth'], YWidth=OverlappedBoundaryForVia['_YWidth'])
        self._DesignParameter['Via6ForVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_Name='Via6ForVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['Via6ForVRX']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(
            **dict(_ViaMet62Met7NumberOfCOX=NumViaXYs[0], _ViaMet62Met7NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via6ForVRX']['_XYCoordinates'] = OverlappedBoundaryForVia['_XYCoordinates']


        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXYBot('M6_VSS'),
            _Mag=0.4,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXYBot('M6_VDD'),
            _Mag=0.4, _TEXT='VDD')

        self._DesignParameter['PIN_VCM'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXYBot('M6_VCM'),
            _Mag=0.4, _TEXT='VCM')
        self._DesignParameter['PIN_VRX'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXYBot('M6_VRX'),
            _Mag=0.4, _TEXT='VRX')


        for i, XY in enumerate(self.getXYLeft('RBU', 'M5H_S')):
            self._DesignParameter[f'PIN_S_{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[XY],
                _Mag=0.4, _TEXT=f'S<{i}>'
            )
        for i, XY in enumerate(self.getXYLeft('RBU', 'M5H_SB')):
            self._DesignParameter[f'PIN_SB_{i}'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
                _XYCoordinates=[XY],
                _Mag=0.4, _TEXT=f'SB<{i}>'
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

    libname = 'TEST_ResistorBank'
    cellname = 'ResistorBank'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        NumX_Bank=4,
        NumY_Bank=8,
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
        LayoutObj = ResistorBank(_Name=cellname)
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

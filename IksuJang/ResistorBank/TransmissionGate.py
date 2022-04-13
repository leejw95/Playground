import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc
from SthPack import BoundaryCalc

from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import PSubRing
from IksuJang.BasicArchive import NSubRing

from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from IksuJang.BasicArchive import ViaMet42Met5
from IksuJang.BasicArchive import ViaMet52Met6
from IksuJang.BasicArchive import ViaMet62Met7



class TransmissionGate(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='TransmissionGate'):
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

                                  NumContactY_Gate=1,                   # option
                                  NumContactY_innerSubring=1,           # option

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

        #
        NumContactY_Gate = NumContactY_Gate if NumContactY_Gate is not None else 1
        NumContactY_innerSubring = NumContactY_innerSubring if NumContactY_innerSubring is not None else 1
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
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, 1800]]  # Temporal Setting, ReCalculated Later...


        ''' ----------------------------------------  Via1 -------------------------------------- '''
        # M1V1M2 For NMOS Drain
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('NMOS', '_Met1Layer'),
                                                                          YWidth=self.getYWidth('NMOS', '_Met1Layer'))
            if NumViaXY[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (1, 2)

        self._DesignParameter['Via1ForNMDrain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForNMDrainIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForNMDrain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via1ForNMSource'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForNMSourceIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForNMSource']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via2ForNMSource'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForNMSourceIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForNMSource']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

        # M1V1M2 For PMOS Drain
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('PMOS', '_Met1Layer'),
                                                                          YWidth=self.getYWidth('PMOS', '_Met1Layer'))
            if NumViaXY[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (1, 2)


        self._DesignParameter['Via1ForPMDrain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPMDrainIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPMDrain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via1ForPMSource'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPMSourceIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPMSource']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via2ForPMSource'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPMSourceIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPMSource']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

        ''' -------------------------------------------------------------------------------------------------------- '''
        offsetY = (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) / 4

        tmpXYs_NMSource = []
        tmpXYs_NMDrain = []
        for i, XYs in enumerate(self.getXY('NMOS', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_NMSource.append([XYs[0], self.FloorMinSnapSpacing(XYs[1] - offsetY, MinSnapSpacing)])
            else:
                tmpXYs_NMDrain.append([XYs[0], self.FloorMinSnapSpacing(XYs[1] + offsetY, MinSnapSpacing)])
        self._DesignParameter['Via1ForNMDrain']['_XYCoordinates'] = tmpXYs_NMDrain
        self._DesignParameter['Via1ForNMSource']['_XYCoordinates'] = tmpXYs_NMSource
        self._DesignParameter['Via2ForNMSource']['_XYCoordinates'] = tmpXYs_NMSource

        tmpXYs_PMSource = []
        tmpXYs_PMDrain = []
        for i, XYs in enumerate(self.getXY('PMOS', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_PMSource.append([XYs[0], self.CeilMinSnapSpacing(XYs[1] - offsetY, MinSnapSpacing)])
            else:
                tmpXYs_PMDrain.append([XYs[0], self.CeilMinSnapSpacing(XYs[1] + offsetY, MinSnapSpacing)])
        self._DesignParameter['Via1ForPMDrain']['_XYCoordinates'] = tmpXYs_PMDrain
        self._DesignParameter['Via1ForPMSource']['_XYCoordinates'] = tmpXYs_PMSource
        self._DesignParameter['Via2ForPMSource']['_XYCoordinates'] = tmpXYs_PMSource


        ''' -------------------------------------------------------------------------------------------------------- '''
        # PolyContact
        XWidth_PolyGate = self.getXYRight('NMOS', '_POLayer')[-1][0] * 2
        NumContactX_Gate = int((XWidth_PolyGate - 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        self._DesignParameter['PolyContactOnNM'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnNMIn{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnNM']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=NumContactX_Gate, _ViaPoly2Met1NumberOfCOY=NumContactY_Gate))
        self._DesignParameter['PolyContactOnNM']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PolyGate

        self._DesignParameter['PolyContactOnPM'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnPMIn{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPM']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=NumContactX_Gate, _ViaPoly2Met1NumberOfCOY=NumContactY_Gate))
        self._DesignParameter['PolyContactOnPM']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PolyGate

        self._DesignParameter['PolyContactOnNM']['_XYCoordinates'] = [[0, 0]]  # Temporal Setting, ReCalculated Later...
        self._DesignParameter['PolyContactOnPM']['_XYCoordinates'] = [[0, 0]]  # Temporal Setting, ReCalculated Later...

        # YCoordinates
        topBoundary_Met1ofNM = max(self.getXYTop('NMOS', '_Met1Layer')[0][1], self.getXYTop('Via1ForNMDrain', '_Met1Layer')[0][1])
        YCoord_PolyContactOnNM = topBoundary_Met1ofNM + _DRCObj._Metal1MinSpaceAtCorner + self.getYWidth('PolyContactOnNM', '_Met1Layer') / 2
        self._DesignParameter['PolyContactOnNM']['_XYCoordinates'] = [[0, YCoord_PolyContactOnNM]]

        botBoundary_Met1ofPM = min(self.getXYBot('PMOS', '_Met1Layer')[0][1], self.getXYTop('Via1ForPMDrain', '_Met1Layer')[0][1])
        YCoord_PolyContactOnPM = botBoundary_Met1ofPM - _DRCObj._Metal1MinSpaceAtCorner - self.getYWidth('PolyContactOnPM', '_Met1Layer') / 2
        self._DesignParameter['PolyContactOnPM']['_XYCoordinates'] = [[0, YCoord_PolyContactOnPM]]

        # POV
        topBoundary = self.getXYBot('PMOS', '_POLayer')[0][1]
        botBoundary = self.getXYTop('PolyContactOnPM', '_POLayer')[0][1]
        tmpXYs = []
        for XYs in self.getXY('PMOS', '_POLayer'):
            tmpXYs.append([XYs[0], (topBoundary + botBoundary) / 2])
        self._DesignParameter['POVForPM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('PMOS', '_POLayer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=tmpXYs
        )

        topBoundary = self.getXYBot('PolyContactOnNM', '_POLayer')[0][1]
        botBoundary = self.getXYTop('NMOS', '_POLayer')[0][1]
        tmpXYs = []
        for XYs in self.getXY('NMOS', '_POLayer'):
            tmpXYs.append([XYs[0], (topBoundary + botBoundary) / 2])
        self._DesignParameter['POVForNM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('NMOS', '_POLayer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=tmpXYs
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        _NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnNM', '_Met1Layer'), YWidth=self.getYWidth('PolyContactOnNM', '_Met1Layer'))
        NumViaXY = (2, _NumViaXY[1])
        self._DesignParameter['Via1OnNMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1OnNMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1OnNMGate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via2OnNMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2OnNMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2OnNMGate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via3OnNMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3OnNMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3OnNMGate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via4OnNMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4OnNMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4OnNMGate']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))

        self._DesignParameter['Via1OnPMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1OnPMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1OnPMGate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via2OnPMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2OnPMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2OnPMGate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via3OnPMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3OnPMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3OnPMGate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['Via4OnPMGate'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='Via4OnPMGateIn{}'.format(_Name)))[0]
        self._DesignParameter['Via4OnPMGate']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(
            **dict(_ViaMet42Met5NumberOfCOX=NumViaXY[0], _ViaMet42Met5NumberOfCOY=NumViaXY[1]))

        # Coordinates
        XCoord = self.getXYLeft('Via1ForNMDrain', '_Met2Layer')[0][0] - _DRCObj._MetalxMinSpace21 - self.getXWidth('Via1OnNMGate', '_Met2Layer') / 2
        self._DesignParameter['Via1OnNMGate']['_XYCoordinates'] = [[XCoord, self.getXY('PolyContactOnNM')[0][1]]]
        self._DesignParameter['Via1OnPMGate']['_XYCoordinates'] = [[XCoord, self.getXY('PolyContactOnPM')[0][1]]]

        self._DesignParameter['Via2OnNMGate']['_XYCoordinates'] = self.getXY('Via1OnNMGate')
        self._DesignParameter['Via3OnNMGate']['_XYCoordinates'] = self.getXY('Via1OnNMGate')
        self._DesignParameter['Via4OnNMGate']['_XYCoordinates'] = self.getXY('Via1OnNMGate')
        self._DesignParameter['Via2OnPMGate']['_XYCoordinates'] = self.getXY('Via1OnPMGate')
        self._DesignParameter['Via3OnPMGate']['_XYCoordinates'] = self.getXY('Via1OnPMGate')
        self._DesignParameter['Via4OnPMGate']['_XYCoordinates'] = self.getXY('Via1OnPMGate')


        # M1H
        rightBoundary = self.getXYRight('PolyContactOnNM', '_Met1Layer')[0][0]
        leftBoundary = self.getXYLeft('Via1OnNMGate', '_Met1Layer')[0][0]
        self._DesignParameter['M1HOnNMGate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=max(self.getYWidth('PolyContactOnNM', '_Met1Layer'), self.getYWidth('Via1OnNMGate', '_Met1Layer')),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('PolyContactOnNM')[0][1]]
            ]
        )
        rightBoundary = self.getXYRight('PolyContactOnPM', '_Met1Layer')[0][0]
        leftBoundary = self.getXYLeft('Via1OnPMGate', '_Met1Layer')[0][0]
        self._DesignParameter['M1HOnPMGate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=max(self.getYWidth('PolyContactOnPM', '_Met1Layer'), self.getYWidth('Via1OnPMGate', '_Met1Layer')),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('PolyContactOnPM')[0][1]]
            ]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        # subring
        ''' ---------------------------------------------- Subring ------------------------------------------------ '''
        rightBoundary1_ODtoOD = self.getXYRight('NMOS', '_ODLayer')[0][0] + _DRCObj._OdMinSpace
        rightBoundary2_Met1toMet1 = self.getXYRight('NMOS', '_Met1Layer')[-1][0] + _DRCObj._Metal1DefaultSpace
        rightBoundary = self.CeilMinSnapSpacing(max(rightBoundary1_ODtoOD, rightBoundary2_Met1toMet1), MinSnapSpacing*2)
        leftBoundary = self.FloorMinSnapSpacing(self.getXYLeft('M1HOnNMGate')[0][0] - _DRCObj._Metal1DefaultSpace, MinSnapSpacing*2)

        # PSubring
        _topBoundary = self.getXYTop('M1HOnNMGate')[0][1] + _DRCObj._Metal1DefaultSpace
        _botBoundary = min(self.getXYBot('NMOS', '_Met1Layer')[0][1], self.getXYBot('Via1ForNMSource', '_Met1Layer')[0][1]) - _DRCObj._Metal1DefaultSpace
        topBoundary = self.CeilMinSnapSpacing(_topBoundary, MinSnapSpacing * 2)
        botBoundary = self.FloorMinSnapSpacing(_botBoundary, MinSnapSpacing * 2)
        self._DesignParameter['PSubring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(**dict(height=1000, width=1000, contact=NumContactY_innerSubring))
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(width=rightBoundary - leftBoundary + self.getYWidth('PSubring', 'met_top'),
                   height=topBoundary - botBoundary + self.getXWidth('PSubring', 'met_right'),
                   contact=NumContactY_innerSubring))
        self._DesignParameter['PSubring']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]
        ]

        # NSubring
        _topBoundary = max(self.getXYTop('PMOS', '_Met1Layer')[0][1], self.getXYTop('Via1ForPMSource', '_Met1Layer')[0][1]) + _DRCObj._Metal1DefaultSpace
        _botBoundary = self.getXYBot('M1HOnPMGate')[0][1] - _DRCObj._Metal1DefaultSpace
        topBoundary = self.CeilMinSnapSpacing(_topBoundary, MinSnapSpacing * 2)
        botBoundary = self.FloorMinSnapSpacing(_botBoundary, MinSnapSpacing * 2)
        self._DesignParameter['NSubring'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='NSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['NSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=1000, width=1000, contact=NumContactY_innerSubring))
        self._DesignParameter['NSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(width=rightBoundary - leftBoundary + self.getYWidth('NSubring', 'met_top'),
                   height=topBoundary - botBoundary + self.getXWidth('NSubring', 'met_right'),
                   contact=NumContactY_innerSubring))
        self._DesignParameter['NSubring']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]
        ]

        ''' -------------------------------------------------------------------------------------------------------- '''
        YCoord_reCalc = self.getXYTop('PSubring', 'top', '_PPLayer')[0][1] + _DRCObj._NwMinEnclosurePactive
        YCoord_prev = self.getXYBot('NSubring', 'nw_bot')[0][1]
        YOffset = YCoord_reCalc - YCoord_prev

        ObjList_PMSide = ['PMOS', 'Via1ForPMDrain', 'Via1ForPMSource', 'Via2ForPMSource', 'PolyContactOnPM',
                          'Via1OnPMGate', 'Via2OnPMGate', 'Via3OnPMGate', 'Via4OnPMGate',
                          'POVForPM', 'M1HOnPMGate', 'NSubring']

        for DesignObj in ObjList_PMSide:
            self.YShiftUp(DesignObj, YOffset)

        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = self.getXYRight('PSubring', 'met_right')[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('Via2ForNMSource', '_Met3Layer'))[0][0]
        self._DesignParameter['M3HOnNMSource'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('Via2ForNMSource', '_Met3Layer'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('Via2ForNMSource')[0][1]]
            ]
        )
        self._DesignParameter['M3HOnPMSource'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('Via2ForPMSource', '_Met3Layer'),
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, self.getXY('Via2ForPMSource')[0][1]]
            ]
        )

        topBoundary = self.getXYTop('M3HOnPMSource')[0][1]
        botBoundary = self.getXYBot('M3HOnNMSource')[0][1]
        self._DesignParameter['M2VOnSource'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('PSubring', 'met_right'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [self.getXY('PSubring', 'met_right')[0][0], (topBoundary + botBoundary) / 2]
            ]
        )

        # via
        OverlappedBoundaryForVia2 = BoundaryCalc.getOverlappedBoundaryElement(self._DesignParameter['M3HOnNMSource'], self._DesignParameter['M2VOnSource'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=OverlappedBoundaryForVia2['_XWidth'], YWidth=OverlappedBoundaryForVia2['_YWidth'])
        self._DesignParameter['Via2ForM2VNM'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForM2VNMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForM2VNM']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForM2VNM']['_XYCoordinates'] = OverlappedBoundaryForVia2['_XYCoordinates']

        ''' -------------------------------------------------------------------------------------------------------- '''
        topBoundary = self.getXYTop('Via1ForPMDrain', '_Met2Layer')[0][1]
        botBoundary = self.getXYBot('Via1ForNMDrain', '_Met2Layer')[0][1]

        tmpXYs = []
        for XYs in self.getXY('Via1ForNMDrain'):
            tmpXYs.append([XYs[0], (topBoundary + botBoundary) / 2])
        self._DesignParameter['M2VOnDrain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('Via1ForPMDrain', '_Met2Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=tmpXYs
        )


        # M4
        topBoundary = self.getXYBot('M1HOnPMGate')[0][1]
        botBoundary = self.getXYTop('M1HOnNMGate')[0][1]
        rightBoundary = CoordCalc.getXYCoords_MaxX(self.getXYRight('M2VOnDrain'))[0][0]
        leftBoundary = CoordCalc.getXYCoords_MinX(self.getXYLeft('M2VOnDrain'))[0][0]
        self._DesignParameter['M4_VCM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, (topBoundary + botBoundary) / 2]]
        )

        # via M2 - M4
        OverlappedBoundaryForVia23 = BoundaryCalc.getOverlappedBoundaryElement(
            self._DesignParameter['M2VOnDrain'], self._DesignParameter['M4_VCM'])
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=OverlappedBoundaryForVia23['_XWidth'], YWidth=OverlappedBoundaryForVia23['_YWidth'])
        self._DesignParameter['Via2ForVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForVCM']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForVCM']['_XYCoordinates'] = OverlappedBoundaryForVia23['_XYCoordinates']

        self._DesignParameter['Via3ForVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via3ForVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['Via3ForVCM']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXYs[0], _ViaMet32Met4NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via3ForVCM']['_XYCoordinates'] = OverlappedBoundaryForVia23['_XYCoordinates']


        ''' -------------------------------------------------------------------------------------------------------- '''
        NumViaXYs = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('NSubring', 'met_top'), YWidth=self.getYWidth('NSubring', 'met_top'))
        self._DesignParameter['Via1ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForVDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXYs[0], _ViaMet12Met2NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via1ForVDD']['_XYCoordinates'] = self.getXY('NSubring', 'met_top')

        self._DesignParameter['Via2ForVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForVDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXYs[0], _ViaMet22Met3NumberOfCOY=NumViaXYs[1]))
        self._DesignParameter['Via2ForVDD']['_XYCoordinates'] = self.getXY('Via1ForVDD')

        ''' --------------------------------------------- NWELL Layer ---------------------------------------------- '''


        ''' -------------------------------------------------------------------------------------------------------- '''
        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')
        ''' -------------------------------------------------------------------------------------------------------- '''



    def YShiftUp(self, DesignObj, OffsetY):

        tmpXYs = []
        for XY in self._DesignParameter[DesignObj]['_XYCoordinates']:
            tmpXYs.append(CoordCalc.Add(XY, [0, OffsetY]))

        self._DesignParameter[DesignObj]['_XYCoordinates'] = tmpXYs

if __name__ == '__main__':
    from Private import MyInfo
    import DRCchecker
    from SthPack import PlaygroundBot

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_TransmissionGate'
    cellname = 'TransmissionGate'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        NumFinger=8,
        Width_PM=550,
        Width_NM=274,

        NumContactY_Gate=1,          # option
        NumContactY_innerSubring=2,  # option

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
        LayoutObj = TransmissionGate(_Name=cellname)
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

import StickDiagram
import DesignParameters
import DRC

import copy
import math
from SthPack import CoordCalc

from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import PbodyContact
from IksuJang.BasicArchive import NbodyContact

from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4


class SRLatchHalf(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='SRLatchHalf'):
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
        self._DesignParameter['NM1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_M1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['NM2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_M2, _NMOSChannelWidth=Width_NM2, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['NM3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM3In{}'.format(_Name)))[0]
        self._DesignParameter['NM3']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_M3, _NMOSChannelWidth=Width_NM3, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['NM4'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM4In{}'.format(_Name)))[0]
        self._DesignParameter['NM4']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_M4, _NMOSChannelWidth=Width_NM4, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))

        self._DesignParameter['PM1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM1In{}'.format(_Name)))[0]
        self._DesignParameter['PM1']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_M1, _PMOSChannelWidth=Width_PM1, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['PM2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM2In{}'.format(_Name)))[0]
        self._DesignParameter['PM2']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_M2, _PMOSChannelWidth=Width_PM2, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['PM3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM3In{}'.format(_Name)))[0]
        self._DesignParameter['PM3']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_M3, _PMOSChannelWidth=Width_PM3, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))
        self._DesignParameter['PM4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM4In{}'.format(_Name)))[0]
        self._DesignParameter['PM4']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_M4, _PMOSChannelWidth=Width_PM4, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=_GateSpacing, _XVT=XVT))


        # Supply Rail
        CellXWidth = _UnitPitch * (NumFinger_M1 + NumFinger_M2 + NumFinger_M3 + NumFinger_M4 + 7)
        NumContactX_SupplyRail = int((CellXWidth - 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)

        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfNbodyCOX=NumContactX_SupplyRail, _NumberOfNbodyCOY=NumContactY_SupplyRail))
        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=NumContactX_SupplyRail, _NumberOfPbodyCOY=NumContactY_SupplyRail))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, 0]]       # Temporal Setting, ReCalculated Later...
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]

        # M1V2M2 Vias on MOSFETs
        for mosfet in ['NM1', 'NM2', 'NM3', 'NM4', 'PM1', 'PM2', 'PM3', 'PM4']:
            try:
                NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth(mosfet, '_Met1Layer'), YWidth=self.getYWidth(mosfet, '_Met1Layer'))
                if NumViaXY[1] < 2:
                    raise NotImplementedError
            except Exception as e:
                print('Error Occurred: ', e)
                NumViaXY = (1, 2)

            ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
            ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
            self._DesignParameter[f'M1V1M2On{mosfet}Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name=f'M1V1M2On{mosfet}DrainIn{_Name}'))[0]
            self._DesignParameter[f'M1V1M2On{mosfet}Drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)


            # M2V2M3 for M1 Drain
            if mosfet in ('NM1', 'PM1'):
                self._DesignParameter[f'M2V2M3On{mosfet}Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=f'M2V2M3On{mosfet}DrainIn{_Name}'))[0]
                self._DesignParameter[f'M2V2M3On{mosfet}Drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

            # M1V1M2 for M3 Source
            if mosfet in ('NM3', 'PM3'):
                self._DesignParameter[f'M1V1M2On{mosfet}Source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name=f'M1V1M2On{mosfet}SourceIn{_Name}'))[0]
                self._DesignParameter[f'M1V1M2On{mosfet}Source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)
                self._DesignParameter[f'M2V2M3On{mosfet}Source'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=f'M2V2M3On{mosfet}SourceIn{_Name}'))[0]
                self._DesignParameter[f'M2V2M3On{mosfet}Source']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))


        ''' -------------------------------------------------------------------------------------------------------- '''
        # NMOS YCoordinates
        bot2top_Met1_NM1 = self.getYWidth('NM1', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnNM1Drain', '_Met1Layer') - self.getYWidth('NM1', '_Met1Layer')) / 2
        bot2top_Met1_NM2 = self.getYWidth('NM2', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnNM2Drain', '_Met1Layer') - self.getYWidth('NM2', '_Met1Layer')) / 2
        bot2top_Met1_NM3 = self.getYWidth('NM3', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnNM3Source', '_Met1Layer') - self.getYWidth('NM3', '_Met1Layer'))
        bot2top_Met1_NM4 = self.getYWidth('NM4', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnNM4Drain', '_Met1Layer') - self.getYWidth('NM4', '_Met1Layer')) / 2
        maxbot2top_Met1_NM1234 = max(bot2top_Met1_NM1, bot2top_Met1_NM2, bot2top_Met1_NM3, bot2top_Met1_NM4)

        _topBoundary_Met1_NM1234 = self.getYWidth('VSSRail', '_Met1Layer') / 2 + _DRCObj._Metal1DefaultSpace + maxbot2top_Met1_NM1234
        topBoundary_Met1_NM1234 = self.CeilMinSnapSpacing(_topBoundary_Met1_NM1234, MinSnapSpacing*2)

        YCoord_NM = {}
        for mosfet in ['NM1', 'NM2', 'NM3', 'NM4']:
            YCoord_NM[f'{mosfet}'] = topBoundary_Met1_NM1234 - self.getYWidth(mosfet, '_Met1Layer') / 2

        self._DesignParameter['NM1']['_XYCoordinates'] = [[-CellXWidth / 2 + _UnitPitch * (NumFinger_M1 + 1) / 2, YCoord_NM['NM1']]]
        self._DesignParameter['NM2']['_XYCoordinates'] = [[self.getXY('NM1', '_PODummyLayer')[1][0] + _UnitPitch * (NumFinger_M2 + 3) / 2, YCoord_NM['NM2']]]
        self._DesignParameter['NM3']['_XYCoordinates'] = [[self.getXY('NM2', '_PODummyLayer')[1][0] + _UnitPitch * (NumFinger_M3 + 3) / 2, YCoord_NM['NM3']]]
        self._DesignParameter['NM4']['_XYCoordinates'] = [[self.getXY('NM3', '_PODummyLayer')[1][0] + _UnitPitch * (NumFinger_M4 + 3) / 2, YCoord_NM['NM4']]]

        # PMOS YCoordinates
        bot2top_Met1_PM1 = self.getYWidth('PM1', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnPM1Drain', '_Met1Layer') - self.getYWidth('PM1', '_Met1Layer')) / 2
        bot2top_Met1_PM2 = self.getYWidth('PM2', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnPM2Drain', '_Met1Layer') - self.getYWidth('PM2', '_Met1Layer')) / 2
        bot2top_Met1_PM3 = self.getYWidth('PM3', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnPM3Source', '_Met1Layer') - self.getYWidth('PM3', '_Met1Layer'))
        bot2top_Met1_PM4 = self.getYWidth('PM4', '_Met1Layer') + max(0, self.getYWidth('M1V1M2OnPM4Drain', '_Met1Layer') - self.getYWidth('PM4', '_Met1Layer')) / 2
        maxbot2top_Met1_PM1234 = max(bot2top_Met1_PM1, bot2top_Met1_PM2, bot2top_Met1_PM3, bot2top_Met1_PM4)

        _botBoundary_Met1_PM1234 = -(self.getYWidth('VSSRail', '_Met1Layer') / 2 + _DRCObj._Metal1DefaultSpace + maxbot2top_Met1_PM1234)
        botBoundary_Met1_PM1234 = self.FloorMinSnapSpacing(_botBoundary_Met1_PM1234, MinSnapSpacing * 2)

        YCoord_PM = {}
        for mosfet in ['PM1', 'PM2', 'PM3', 'PM4']:
            YCoord_PM[f'{mosfet}'] = botBoundary_Met1_PM1234 + self.getYWidth(mosfet, '_Met1Layer') / 2

        self._DesignParameter['PM1']['_XYCoordinates'] = [[self.getXY('NM1')[0][0], YCoord_PM['PM1']]]
        self._DesignParameter['PM2']['_XYCoordinates'] = [[self.getXY('NM2')[0][0], YCoord_PM['PM2']]]
        self._DesignParameter['PM3']['_XYCoordinates'] = [[self.getXY('NM3')[0][0], YCoord_PM['PM3']]]
        self._DesignParameter['PM4']['_XYCoordinates'] = [[self.getXY('NM4')[0][0], YCoord_PM['PM4']]]


        # Via on NMOS/PMOS Drain
        for mosfet in ['NM1', 'NM2', 'NM3', 'NM4', 'PM1', 'PM2', 'PM3', 'PM4']:
            tmpXYs = []
            for i, XYs in enumerate(self.getXY(mosfet, '_Met1Layer')):
                if i % 2 == 1:
                    tmpXYs.append(XYs)
                self._DesignParameter[f'M1V1M2On{mosfet}Drain']['_XYCoordinates'] = tmpXYs

                if mosfet in ('NM1', 'PM1'):
                    self._DesignParameter[f'M2V2M3On{mosfet}Drain']['_XYCoordinates'] = tmpXYs

        # NM3 Source
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('NM3', '_Met1Layer')):
            if i % 2 == 0:
                if self.getYWidth('NM3', '_Met1Layer') < self.getYWidth('M1V1M2OnNM3Source', '_Met1Layer'):
                    tmpXYs.append([XYs[0], self.getXYTop('NM3', '_Met1Layer')[0][1] - self.getYWidth('M1V1M2OnNM3Source', '_Met1Layer') / 2])
                else:
                    tmpXYs.append([XYs[0], XYs[1]])
        self._DesignParameter['M1V1M2OnNM3Source']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M2V2M3OnNM3Source']['_XYCoordinates'] = tmpXYs

        # PM3 Source
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('PM3', '_Met1Layer')):
            if i % 2 == 0:
                if self.getYWidth('PM3', '_Met1Layer') < self.getYWidth('M1V1M2OnPM3Source', '_Met1Layer'):
                    tmpXYs.append([XYs[0], self.getXYBot('PM3', '_Met1Layer')[0][1] + self.getYWidth('M1V1M2OnPM3Source', '_Met1Layer') / 2])
                else:
                    tmpXYs.append([XYs[0], XYs[1]])
        self._DesignParameter['M1V1M2OnPM3Source']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['M2V2M3OnPM3Source']['_XYCoordinates'] = tmpXYs


        ''' -------------------------------------------------------------------------------------------------------- '''
        # PolyContact On NMOS, PMOS
        for mosfet in ['M1', 'M2', 'M3', 'M4']:
            XWidth_PCCOM1 = CoordCalc.getDistanceBtwMinMaxX(self.getXY(f'N{mosfet}', '_POLayer')) + self.getXWidth(f'N{mosfet}', '_POLayer')
            XNum_PCCOM1 = int((XWidth_PCCOM1 - 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
            if XNum_PCCOM1 < 1:
                XNum_PCCOM1 = 1

            self._DesignParameter[f'PolyContactOnN{mosfet}'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name=f'PolyContactOnN{mosfet}In{_Name}'))[0]
            self._DesignParameter[f'PolyContactOnN{mosfet}']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=XNum_PCCOM1, _ViaPoly2Met1NumberOfCOY=1))
            self._DesignParameter[f'PolyContactOnP{mosfet}'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name=f'PolyContactOnP{mosfet}In{_Name}'))[0]
            self._DesignParameter[f'PolyContactOnP{mosfet}']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=XNum_PCCOM1, _ViaPoly2Met1NumberOfCOY=1))
            if XWidth_PCCOM1 > self.getXWidth(f'PolyContactOnN{mosfet}', '_POLayer'):
                self._DesignParameter[f'PolyContactOnN{mosfet}']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PCCOM1
                self._DesignParameter[f'PolyContactOnP{mosfet}']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PCCOM1

        for mosfet in ('NM1', 'NM2', 'NM3', 'NM4'):
            # set coordinates
            YCoord_PolyContact_case1 = max(self.getXYTop(mosfet, '_Met1Layer')[0][1], self.getXYTop(f'M1V1M2On{mosfet}Drain', '_Met1Layer')[0][1]) + _DRCObj._Metal1MinSpaceAtCorner + self.getYWidth(f'PolyContactOn{mosfet}', '_Met1Layer') / 2
            YCoord_PolyContact_case2 = 0
            YCoord_PolyContact = max(YCoord_PolyContact_case1, YCoord_PolyContact_case2)
            self._DesignParameter[f'PolyContactOn{mosfet}']['_XYCoordinates'] = [[self.getXY(mosfet)[0][0], YCoord_PolyContact]]

            # POV
            topBoundary_POV = self.getXYBot(f'PolyContactOn{mosfet}', '_POLayer')[0][1]
            botBoundary_POV = self.getXYTop(mosfet, '_POLayer')[0][1]
            tmpXYs = []
            for XYs in self.getXY(mosfet, '_POLayer'):
                tmpXYs.append([XYs[0], (topBoundary_POV + botBoundary_POV) / 2])
            self._DesignParameter[f'POVFor{mosfet}'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=self.getXWidth(mosfet, '_POLayer'),
                _YWidth=topBoundary_POV-botBoundary_POV,
                _XYCoordinates=tmpXYs
            )

        for mosfet in ('PM1', 'PM2', 'PM3', 'PM4'):
            # set coordinates
            YCoord_PolyContact_case1 = min(self.getXYBot(mosfet, '_Met1Layer')[0][1], self.getXYBot(f'M1V1M2On{mosfet}Drain', '_Met1Layer')[0][1]) - _DRCObj._Metal1MinSpaceAtCorner - self.getYWidth(f'PolyContactOn{mosfet}', '_Met1Layer') / 2
            YCoord_PolyContact_case2 = 0
            YCoord_PolyContact = min(YCoord_PolyContact_case1, YCoord_PolyContact_case2)
            self._DesignParameter[f'PolyContactOn{mosfet}']['_XYCoordinates'] = [[self.getXY(mosfet)[0][0], YCoord_PolyContact]]

            # POV
            topBoundary_POV = self.getXYBot(mosfet, '_POLayer')[0][1]
            botBoundary_POV = self.getXYTop(f'PolyContactOn{mosfet}', '_POLayer')[0][1]
            tmpXYs = []
            for XYs in self.getXY(mosfet, '_POLayer'):
                tmpXYs.append([XYs[0], (topBoundary_POV + botBoundary_POV) / 2])
            self._DesignParameter[f'POVFor{mosfet}'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=self.getXWidth(mosfet, '_POLayer'),
                _YWidth=topBoundary_POV-botBoundary_POV,
                _XYCoordinates=tmpXYs
            )


        # NM3's drain to NM4's drain by M2
        rightBoundary_M2H01 = self.getXYRight('M1V1M2OnNM4Drain', '_Met2Layer')[-1][0]
        leftBoundary_M2H01 = self.getXYLeft('M1V1M2OnNM3Drain', '_Met2Layer')[0][0]
        self._DesignParameter['M2H01'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary_M2H01 - leftBoundary_M2H01,
            _YWidth=self.getXWidth('M1V1M2OnNM3Drain', '_Met2Layer'),
        )
        self._DesignParameter['M2H01']['_XYCoordinates'] = [
            [(rightBoundary_M2H01 + leftBoundary_M2H01) / 2,
             self.getXYTop('M1V1M2OnNM3Source', '_Met2Layer')[0][1] + _DRCObj._MetalxMinSpaceAtCorner + self.getYWidth('M2H01') / 2]
        ]

        topBoundary_M2V02 = self.getXYBot('M2H01')[0][1]
        botBoundary_M2V02 = self.getXYTop('M1V1M2OnNM3Drain', '_Met2Layer')[0][1]
        self._DesignParameter['M2V02'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2OnNM3Drain', '_Met2Layer'),
            _YWidth=topBoundary_M2V02-botBoundary_M2V02
        )
        tmpXYs = []
        for XYs in self.getXY('M1V1M2OnNM3Drain'):
            tmpXYs.append([XYs[0], (topBoundary_M2V02 + botBoundary_M2V02) / 2])
        self._DesignParameter['M2V02']['_XYCoordinates'] = tmpXYs

        topBoundary_M2V03 = self.getXYBot('M2H01')[0][1]
        botBoundary_M2V03 = self.getXYTop('M1V1M2OnNM4Drain', '_Met2Layer')[0][1]
        self._DesignParameter['M2V03'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2OnNM4Drain', '_Met2Layer'),
            _YWidth=topBoundary_M2V03 - botBoundary_M2V03
        )
        tmpXYs = []
        for XYs in self.getXY('M1V1M2OnNM4Drain'):
            tmpXYs.append([XYs[0], (topBoundary_M2V03 + botBoundary_M2V03) / 2])
        self._DesignParameter['M2V03']['_XYCoordinates'] = tmpXYs


        # PM3's drain to PM4's drain by M2
        rightBoundary_M2H04 = self.getXYRight('M1V1M2OnPM4Drain', '_Met2Layer')[-1][0]
        leftBoundary_M2H04 = self.getXYLeft('M1V1M2OnPM3Drain', '_Met2Layer')[0][0]
        self._DesignParameter['M2H04'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary_M2H04 - leftBoundary_M2H04,
            _YWidth=self.getXWidth('M1V1M2OnPM3Drain', '_Met2Layer'),
        )
        self._DesignParameter['M2H04']['_XYCoordinates'] = [
            [(rightBoundary_M2H04 + leftBoundary_M2H04) / 2,
             self.getXYBot('M1V1M2OnPM3Source', '_Met2Layer')[0][1] - _DRCObj._MetalxMinSpaceAtCorner - self.getYWidth('M2H04') / 2]
        ]

        topBoundary_M2V05 = self.getXYBot('M1V1M2OnPM3Drain', '_Met2Layer')[0][1]
        botBoundary_M2V05 = self.getXYTop('M2H04')[0][1]
        self._DesignParameter['M2V05'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2OnPM3Drain', '_Met2Layer'),
            _YWidth=topBoundary_M2V05-botBoundary_M2V05
        )
        tmpXYs = []
        for XYs in self.getXY('M1V1M2OnPM3Drain'):
            tmpXYs.append([XYs[0], (topBoundary_M2V05 + botBoundary_M2V05) / 2])
        self._DesignParameter['M2V05']['_XYCoordinates'] = tmpXYs

        topBoundary_M2V06 = self.getXYBot('M2H04')[0][1]
        botBoundary_M2V06 = self.getXYTop('M1V1M2OnPM4Drain', '_Met2Layer')[0][1]
        self._DesignParameter['M2V06'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2OnPM4Drain', '_Met2Layer'),
            _YWidth=topBoundary_M2V06 - botBoundary_M2V06
        )
        tmpXYs = []
        for XYs in self.getXY('M1V1M2OnPM4Drain'):
            tmpXYs.append([XYs[0], (topBoundary_M2V06 + botBoundary_M2V06) / 2])
        self._DesignParameter['M2V06']['_XYCoordinates'] = tmpXYs


        # up to M3 Via on NM3/PM3 Gate
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnNM3', '_Met1Layer'), YWidth=self.getYWidth('PolyContactOnNM3', '_Met1Layer'))
            if NumViaXY[0] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (2, 1)

        self._DesignParameter['M1V1M2OnNM3Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM3Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnNM3Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnNM3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnNM3Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

        self._DesignParameter['M1V1M2OnPM3Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM3Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnPM3Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnPM3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPM3Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

        YCoord_NM3Via_case1 = self.getXY('PolyContactOnNM3')[0][1]
        YCoord_NM3Via_case2 = self.getXYTop('M2H01')[0][1] + _DRCObj._MetalxMinSpace + self.getYWidth('M1V1M2OnNM3Gate', '_Met2Layer') / 2
        YCoord_NM3Via = max(YCoord_NM3Via_case1, YCoord_NM3Via_case2)
        self._DesignParameter['M1V1M2OnNM3Gate']['_XYCoordinates'] = [[self.getXY('NM3')[0][0], YCoord_NM3Via]]
        self._DesignParameter['M2V2M3OnNM3Gate']['_XYCoordinates'] = [[self.getXY('NM3')[0][0], YCoord_NM3Via]]

        YCoord_PM3Via_case1 = self.getXY('PolyContactOnPM3')[0][1]
        YCoord_PM3Via_case2 = self.getXYBot('M2H04')[0][1] - _DRCObj._MetalxMinSpace - self.getYWidth('M1V1M2OnPM3Gate', '_Met2Layer') / 2
        YCoord_PM3Via = min(YCoord_PM3Via_case1, YCoord_PM3Via_case2)
        self._DesignParameter['M1V1M2OnPM3Gate']['_XYCoordinates'] = [[self.getXY('PM3')[0][0], YCoord_PM3Via]]
        self._DesignParameter['M2V2M3OnPM3Gate']['_XYCoordinates'] = [[self.getXY('PM3')[0][0], YCoord_PM3Via]]

        topBoundary_M1ForNM3Gate = max(self.getXYTop('PolyContactOnNM3', '_Met1Layer')[0][1], self.getXYTop('M1V1M2OnNM3Gate', '_Met1Layer')[0][1])
        botBoundary_M1ForNM3Gate = min(self.getXYBot('PolyContactOnNM3', '_Met1Layer')[0][1], self.getXYBot('M1V1M2OnNM3Gate', '_Met1Layer')[0][1])
        self._DesignParameter['M1ForNM3Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=max(self.getXWidth('PolyContactOnNM3', '_Met1Layer'), self.getXWidth('M1V1M2OnNM3Gate', '_Met1Layer')),
            _YWidth=topBoundary_M1ForNM3Gate - botBoundary_M1ForNM3Gate,
            _XYCoordinates=[[self.getXY('NM3')[0][0], (topBoundary_M1ForNM3Gate + botBoundary_M1ForNM3Gate) / 2]]
        )

        topBoundary_M1ForPM3Gate = max(self.getXYTop('PolyContactOnPM3', '_Met1Layer')[0][1], self.getXYTop('M1V1M2OnPM3Gate', '_Met1Layer')[0][1])
        botBoundary_M1ForPM3Gate = min(self.getXYBot('PolyContactOnPM3', '_Met1Layer')[0][1], self.getXYBot('M1V1M2OnPM3Gate', '_Met1Layer')[0][1])
        self._DesignParameter['M1ForPM3Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=max(self.getXWidth('PolyContactOnPM3', '_Met1Layer'), self.getXWidth('M1V1M2OnPM3Gate', '_Met1Layer')),
            _YWidth=topBoundary_M1ForPM3Gate - botBoundary_M1ForPM3Gate,
            _XYCoordinates=[[self.getXY('PM3')[0][0], (topBoundary_M1ForPM3Gate + botBoundary_M1ForPM3Gate) / 2]]
        )

        # M1V1M2 Via for NM1/PM1 Gate
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(
                XWidth=self.getXWidth('PolyContactOnNM1', '_Met1Layer'),
                YWidth=self.getYWidth('PolyContactOnNM1', '_Met1Layer'))
            if NumViaXY[0] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (2, 1)

        self._DesignParameter['M1V1M2OnNM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM1Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnNM1Gate']['_XYCoordinates'] = self.getXY('PolyContactOnNM1')

        self._DesignParameter['M1V1M2OnPM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM1Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2OnPM1Gate']['_XYCoordinates'] = self.getXY('PolyContactOnPM1')

        if self.getXWidth('PolyContactOnNM1', '_Met1Layer') < self.getXWidth('M1V1M2OnNM1Gate', '_Met1Layer'):
            self._DesignParameter['PolyContactOnNM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('M1V1M2OnNM1Gate', '_Met1Layer')
            self._DesignParameter['PolyContactOnPM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('M1V1M2OnPM1Gate', '_Met1Layer')

        ''' -------------------------------------------------------------------------------------------------------- '''

        YCoord_M1V1M2OnPM3Gate_reCalc = self.getXYTop('M1V1M2OnNM3Gate', '_Met2Layer')[0][1] + _DRCObj._MetalxMinSpace * 2 + _DRCObj._MetalxMinWidth + self.getYWidth('M1V1M2OnPM3Gate', '_Met2Layer') / 2
        Offset_PMSide = YCoord_M1V1M2OnPM3Gate_reCalc - self.getXY('M1V1M2OnPM3Gate')[0][1]

        ObjList_PMSide = ['PM1', 'PM2', 'PM3', 'PM4', 'VDDRail',
                          'M1V1M2OnPM1Drain', 'M1V1M2OnPM2Drain', 'M1V1M2OnPM3Drain', 'M1V1M2OnPM4Drain',
                          'M1V1M2OnPM3Source', 'M2V2M3OnPM1Drain', 'M2V2M3OnPM3Source',
                          'PolyContactOnPM1', 'PolyContactOnPM2', 'PolyContactOnPM3', 'PolyContactOnPM4',
                          'POVForPM1', 'POVForPM2', 'POVForPM3', 'POVForPM4',
                          'M1V1M2OnPM1Gate', 'M1V1M2OnPM3Gate', 'M2V2M3OnPM3Gate', 'M1ForPM3Gate',
                          'M2H04', 'M2V05', 'M2V06'
                          ]
        for DesignObj in ObjList_PMSide:
            self.YShiftUp(DesignObj, Offset_PMSide)

        ''' -------------------------------------------------------------------------------------------------------- '''
        for mosfet in ('NM1', 'NM2', 'NM4'):
            topBoundary = self.getXYBot(mosfet, '_Met1Layer')[0][1]
            botBoundary = self.getXYTop('VSSRail', '_Met1Layer')[0][1]
            tmpXYs = []
            for i, XYs in enumerate(self.getXY(mosfet, '_Met1Layer')):
                if i % 2 == 0:
                    tmpXYs.append([XYs[0], (topBoundary + botBoundary) / 2])
            self._DesignParameter[f'M1VSSFor{mosfet}'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth(mosfet, '_Met1Layer'),
                _YWidth=topBoundary - botBoundary,
                _XYCoordinates=tmpXYs
            )


        ''' -------------------------------------------------------------------------------------------------------- '''
        for mosfet in ('PM1', 'PM2', 'PM4'):
            topBoundary = self.getXYBot('VDDRail', '_Met1Layer')[0][1]
            botBoundary = self.getXYTop(mosfet, '_Met1Layer')[0][1]
            tmpXYs = []
            for i, XYs in enumerate(self.getXY(mosfet, '_Met1Layer')):
                if i % 2 == 0:
                    tmpXYs.append([XYs[0], (topBoundary + botBoundary) / 2])
            self._DesignParameter[f'M1VSSFor{mosfet}'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth(mosfet, '_Met1Layer'),
                _YWidth=topBoundary - botBoundary,
                _XYCoordinates=tmpXYs
            )


        ''' -------------------------------------------------------------------------------------------------------- '''
        for mosfet in ('NM1', 'NM2', 'PM1', 'PM2'):
            rightBoundary = self.getXYLeft(f'M1V1M2On{mosfet}Drain', '_Met2Layer')[-1][0]
            leftBoundary = self.getXYRight(f'M1V1M2On{mosfet}Drain', '_Met2Layer')[0][0]
            self._DesignParameter[f'M2HFor{mosfet}Drain'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=rightBoundary-leftBoundary,
                _YWidth=self.getXWidth(f'M1V1M2On{mosfet}Drain', '_Met2Layer'),
                _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY(f'M1V1M2On{mosfet}Drain')[0][1]]]
            )

        ''' -------------------------------------------------------------------------------------------------------- '''
        topBoundary = self.getXYBot('PolyContactOnPM2', '_Met1Layer')[0][1]
        botBoundary = self.getXYTop('PolyContactOnNM2', '_Met1Layer')[0][1]
        self._DesignParameter['M1VForNM2PM2Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=_DRCObj._Metal1MinWidth,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('PolyContactOnNM2')[0][0], (topBoundary + botBoundary) / 2]]
        )

        topBoundary = self.getXYBot('PolyContactOnPM4', '_Met1Layer')[0][1]
        botBoundary = self.getXYTop('PolyContactOnNM4', '_Met1Layer')[0][1]
        self._DesignParameter['M1VForNM4PM4Gate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=_DRCObj._Metal1MinWidth,
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('PolyContactOnNM4')[0][0], (topBoundary + botBoundary) / 2]]
        )


        self._DesignParameter['M1V1M2OnNet07'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNet07In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNet07']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
        self._DesignParameter['M1V1M2OnNet07']['_XYCoordinates'] = [
            [self.getXYRight('M1V1M2OnNM4Drain', '_Met2Layer')[-1][0] + _DRCObj._MetalxMinSpace2 + _DRCObj._MetalxMinWidth,
             self.getXY('M1VForNM4PM4Gate')[0][1]]
        ]

        rightBoundary = self.getXYLeft('M1V1M2OnNet07', '_Met1Layer')[0][0]
        leftBoundary = self.getXYRight('M1VForNM4PM4Gate')[0][0]
        self._DesignParameter['M1HOnNet07'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=_DRCObj._Metal1MinWidth,
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M1V1M2OnNet07')[0][1]]]
        )


        ''' -------------------------------------------------------------------------------------------------------- '''
        topBoundary = self.getXYBot('M1V1M2OnPM2Drain', '_Met2Layer')[0][1]
        botBoundary = self.getXYTop('M1V1M2OnNM2Drain', '_Met2Layer')[0][1]
        self._DesignParameter['M2VOnNet08'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2OnNM2Drain', '_Met2Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M1V1M2OnPM2Drain')[0][0], (topBoundary + botBoundary) / 2]]
        )

        rightBoundary = self.getXYLeft('M2VOnNet08')[0][0]
        leftBoundary = self.getXYRight('M1V1M2OnNM1Gate', '_Met2Layer')[0][0]
        self._DesignParameter['M2HOnNet09'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M1V1M2OnNM1Gate', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M1V1M2OnNM1Gate')[0][1]]]
        )

        rightBoundary = self.getXYLeft('M1V1M2OnPM3Gate', '_Met2Layer')[0][0]
        leftBoundary = self.getXYRight('M2VOnNet08')[0][0]
        self._DesignParameter['M2HOnNet10'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getYWidth('M1V1M2OnPM3Gate', '_Met2Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M1V1M2OnPM3Gate')[0][1]]]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        rightBoundary = self.getXY('PM4', '_PODummyLayer')[0][0]
        leftBoundary = self.getXY('M2V2M3OnPM1Drain')[0][0]
        self._DesignParameter['M3HOnNet11'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getXWidth('M2V2M3OnPM1Drain', '_Met3Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M2V2M3OnPM1Drain')[0][1]]]
        )

        rightBoundary = self.getXY('M1V1M2OnNet07')[0][0]
        leftBoundary = self.getXY('M2V2M3OnNM1Drain')[0][0]
        self._DesignParameter['M3HOnNet12'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=self.getXWidth('M2V2M3OnNM1Drain', '_Met3Layer'),
            _XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('M2V2M3OnNM1Drain')[0][1]]]
        )

        self._DesignParameter['M3V3M4OnNet11'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNet11In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNet11']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
        self._DesignParameter['M3V3M4OnNet11']['_XYCoordinates'] = [
            [self.getXYRight('M3HOnNet11')[0][0],
             self.getXYTop('M3HOnNet11')[0][1] - self.getYWidth('M3V3M4OnNet11', '_Met3Layer') / 2]
        ]
        self._DesignParameter['M3V3M4OnNet12'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNet12In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNet12']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
        self._DesignParameter['M3V3M4OnNet12']['_XYCoordinates'] = [
            [self.getXY('M3V3M4OnNet11')[0][0],
             self.getXYBot('M3HOnNet12')[0][1] + self.getYWidth('M3V3M4OnNet12', '_Met3Layer') / 2]
        ]

        topBoundary = self.getXYBot('M3V3M4OnNet11', '_Met4Layer')[0][1]
        botBoundary = self.getXYTop('M3V3M4OnNet12', '_Met4Layer')[0][1]
        self._DesignParameter['M4VOnNet13'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M3V3M4OnNet11', '_Met4Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('M3V3M4OnNet11')[0][0], (topBoundary + botBoundary) / 2]]
        )

        # ''' -------------------------------------------------------------------------------------------------------- '''
        # # print('print all obj...')
        # # tmpObjDict_Up = copy.deepcopy(self._DesignParameter)
        # # del tmpObjDict_Up['_Name']
        # # del tmpObjDict_Up['_GDSFile']
        # #
        # # tmpObjDict_Dn = {}
        # # for i, obj in enumerate(tmpObjDict_Up):
        # #     print(f'obj{i} : {obj}')
        # #     tmpXYs = []
        # #     for XYs in self._DesignParameter[obj]['_XYCoordinates']:
        # #         tmpXYs.append(CoordCalc.FlipY(XYs))
        # #     self._DesignParameter[obj]['_XYCoordinates'].extend(tmpXYs)
        # #
        # #     tmpObjDict_Dn[obj] = tmpObjDict_Up[obj]
        # #     tmpObjDict_Dn[obj]['_XYCoordinates'] = tmpXYs
        # #
        # #
        # #
        # # topBoundary = self.getXYBot('M3V3M4OnNet11', '_Met4Layer')[0][1]
        # # botBoundary = self.getXYTop('M3V3M4OnNet12', '_Met4Layer')[0][1]
        # # self._DesignParameter['tempM4V'] = self._BoundaryElementDeclaration(
        # #     _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        # #     _XWidth=self.getXWidth('M3V3M4OnNet11', '_Met4Layer'),
        # #     _YWidth=topBoundary - botBoundary,
        # #     _XYCoordinates=[[self.getXY('M3V3M4OnNet11')[0][0], (topBoundary + botBoundary) / 2]]
        # # )
        #
        #
        # ''' -------------------------------------------------------------------------------------------------------- '''
        # print('print all obj...')
        # tmpObjDict_Up = copy.deepcopy(self._DesignParameter)
        # del tmpObjDict_Up['_Name']
        # del tmpObjDict_Up['_GDSFile']
        #
        # for i, obj in enumerate(tmpObjDict_Up):
        #     print(f'obj{i} : {obj}')
        #     tmpXYs = []
        #     for XYs in self._DesignParameter[obj]['_XYCoordinates']:
        #         tmpXYs.append(CoordCalc.FlipY(XYs))
        #     self._DesignParameter[f'{obj}_Dn'] = self._DesignParameter[obj]
        #     self._DesignParameter[f'{obj}_Dn']['_XYCoordinates'] = tmpXYs
        #
        #
        #
        #
        #
        # topBoundary = self.getXYBot('M3V3M4OnNet11', '_Met4Layer')[0][1]
        # botBoundary = self.getXYTop('M3V3M4OnNet12', '_Met4Layer')[0][1]
        # self._DesignParameter['tempM4V'] = self._BoundaryElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        #     _XWidth=self.getXWidth('M3V3M4OnNet11', '_Met4Layer'),
        #     _YWidth=topBoundary - botBoundary,
        #     _XYCoordinates=[[self.getXY('M3V3M4OnNet11')[0][0], (topBoundary + botBoundary) / 2]]
        # )



        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''

        del self._DesignParameter['M2V2M3OnPM3Gate']

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

    libname = 'TEST_SRLatch'
    cellname = 'SRLatchHalf'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_20G = dict(
        NumFinger_M1=5,         # 5 1 2 2
        NumFinger_M2=5,
        NumFinger_M3=6,
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
        LayoutObj = SRLatchHalf(_Name=cellname)
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

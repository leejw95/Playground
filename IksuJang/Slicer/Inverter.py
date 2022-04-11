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
from IksuJang.Slicer import NMOSSET
from IksuJang.Slicer import PMOSSET


class Inverter(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger=15,
                                  Width_PM=600,
                                  Width_NM=200,

                                  NumContactY_Gate=1,                   # option
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
        CellXWidth = self.getXYRight('NMOS', '_PODummyLayer')[-1][0] * 2
        NumContactX_SupplyRail = int((CellXWidth - 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)

        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfNbodyCOX=NumContactX_SupplyRail, _NumberOfNbodyCOY=NumContactY_SupplyRail))
        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=NumContactX_SupplyRail, _NumberOfPbodyCOY=NumContactY_SupplyRail))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, 0]]       # Temporal Setting, ReCalculated Later...
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]       # Temporal Setting, ReCalculated Later...

        # PolyContact
        XWidth_PolyGate = self.getXYRight('NMOS', '_POLayer')[-1][0] * 2
        NumContactX_Gate = int((XWidth_PolyGate - 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        self._DesignParameter['PolyContact'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PolyContact']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=NumContactX_Gate, _ViaPoly2Met1NumberOfCOY=NumContactY_Gate))
        self._DesignParameter['PolyContact']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PolyGate
        self._DesignParameter['PolyContact']['_XYCoordinates'] = [[0, 0]]       # Temporal Setting, ReCalculated Later...


        ''' ----------------------------------------  Drain Via (Output Node) -------------------------------------- '''
        # M1V1M2 For NMOS Drain
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('NMOS', '_Met1Layer'), YWidth=self.getYWidth('NMOS', '_Met1Layer'))
            if NumViaXY[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (1, 2)

        self._DesignParameter['M1V1M2ForNM'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2ForNMIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2ForNM']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2ForNM']['_XYCoordinates'] = [[0, 0]]       # Temporal Setting, ReCalculated Later...

        # M1V1M2 For PMOS Drain
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('PMOS', '_Met1Layer'), YWidth=self.getYWidth('PMOS', '_Met1Layer'))
            if NumViaXY[1] < 2:
                raise NotImplementedError
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (1, 2)

        self._DesignParameter['M1V1M2ForPM'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2ForPMIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2ForPM']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M1V1M2ForPM']['_XYCoordinates'] = [[0, 0]]  # Temporal Setting, ReCalculated Later...


        ''' ------------------------------------- Setting YCoordinates --------------------------------------------- '''

        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]

        YCoord_NMOS_case1 = self.getXYTop('VSSRail', '_Met1Layer')[0][1] + _DRCObj._Metal1DefaultSpace + max(self.getYWidth('NMOS', '_Met1Layer'), self.getYWidth('M1V1M2ForNM', '_Met1Layer')) / 2
        YCoord_NMOS_case2 = 0
        YCoord_NMOS = max(YCoord_NMOS_case1, YCoord_NMOS_case2)
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoord_NMOS]]

        YCoord_PolyContact_case1 = self.getXYTop('NMOS', '_Met1Layer')[0][1] + _DRCObj._Metal1MinSpaceAtCorner + self.getYWidth('PolyContact', '_Met1Layer') / 2
        YCoord_PolyContact_case2 = (self.getXY('NMOS')[0][1] + self.getYWidth('M1V1M2ForNM', '_Met1Layer') / 2) + _DRCObj._MetalxMinSpaceAtCorner + self.getYWidth('PolyContact', '_Met1Layer') / 2
        YCoord_PolyContact = max(YCoord_PolyContact_case1, YCoord_PolyContact_case2)
        self._DesignParameter['PolyContact']['_XYCoordinates'] = [[0, YCoord_PolyContact]]

        YCoord_PMOS_case1 = self.getXYTop('PolyContact', '_Met1Layer')[0][1] + _DRCObj._Metal1MinSpaceAtCorner + max(self.getYWidth('PMOS', '_Met1Layer'), self.getYWidth('M1V1M2ForPM', '_Met1Layer')) / 2
        YCoord_PMOS_case2 = 0
        YCoord_PMOS = max(YCoord_PMOS_case1, YCoord_PMOS_case2)
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoord_PMOS]]

        YCoord_VDD_case1 = self.getXYTop('PMOS', '_Met1Layer')[0][1] + _DRCObj._Metal1DefaultSpace + self.getYWidth('VDDRail', '_Met1Layer') / 2
        YCoord_VDD_case2 = (self.getXY('PMOS')[0][1] + self.getYWidth('M1V1M2ForPM', '_Met1Layer') / 2) + _DRCObj._Metal1DefaultSpace + self.getYWidth('VDDRail', '_Met1Layer') / 2
        YCoord_VDD = max(YCoord_VDD_case1, YCoord_VDD_case2)
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, YCoord_VDD]]


        ''' -------------------------------------------------------------------------------------------------------- '''
        # VSS Routing & M1V1M2 for NMOS
        topBoundary_M1VForVSS = self.getXYBot('NMOS', '_Met1Layer')[0][1]
        botBoundary_M1VForVSS = self.getXYTop('VSSRail', '_Met1Layer')[0][1]

        tmpXYs_NMSource = []
        tmpXYs_NMDrain = []
        for i, XYs in enumerate(self.getXY('NMOS', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_NMSource.append([XYs[0], (topBoundary_M1VForVSS + botBoundary_M1VForVSS) / 2])
            else:
                tmpXYs_NMDrain.append(XYs)

        self._DesignParameter['M1VForVSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('NMOS', '_Met1Layer'),
            _YWidth=topBoundary_M1VForVSS-botBoundary_M1VForVSS,
            _XYCoordinates=tmpXYs_NMSource
        )

        self._DesignParameter['M1V1M2ForNM']['_XYCoordinates'] = tmpXYs_NMDrain

        # VDD Routing & M1V1M2 for PMOS
        topBoundary_M1VForVDD = self.getXYBot('VDDRail', '_Met1Layer')[0][1]
        botBoundary_M1VForVDD = self.getXYTop('PMOS', '_Met1Layer')[0][1]

        tmpXYs_PMSource = []
        tmpXYs_PMDrain = []
        for i, XYs in enumerate(self.getXY('PMOS', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_PMSource.append([XYs[0], (topBoundary_M1VForVDD + botBoundary_M1VForVDD) / 2])
            else:
                tmpXYs_PMDrain.append(XYs)

        self._DesignParameter['M1VForVDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('PMOS', '_Met1Layer'),
            _YWidth=topBoundary_M1VForVDD - botBoundary_M1VForVDD,
            _XYCoordinates=tmpXYs_PMSource
        )

        self._DesignParameter['M1V1M2ForPM']['_XYCoordinates'] = tmpXYs_PMDrain


        # PolyGate Routing
        topBoundary_POV = self.getXYBot('PMOS', '_POLayer')[0][1]
        botBoundary_POV = self.getXYTop('NMOS', '_POLayer')[0][1]
        tmpXYs = []
        for XYs in self.getXY('PMOS', '_POLayer'):
            tmpXYs.append([XYs[0], (topBoundary_POV + botBoundary_POV) / 2])
        self._DesignParameter['POVForGate'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('PMOS', '_POLayer'),
            _YWidth=topBoundary_POV - botBoundary_POV,
            _XYCoordinates=tmpXYs
        )

        # M2H
        XWidth_M2H = self.getXYRight('M1V1M2ForPM', '_Met2Layer')[-1][0] - self.getXYLeft('M1V1M2ForPM', '_Met2Layer')[0][0]
        self._DesignParameter['M2H'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXYRight('M1V1M2ForPM', '_Met2Layer')[-1][0] - self.getXYLeft('M1V1M2ForPM', '_Met2Layer')[0][0],
            _YWidth=_DRCObj._MetalxMinWidth,
            _XYCoordinates=[
                [(self.getXYRight('M1V1M2ForPM', '_Met2Layer')[-1][0] + self.getXYLeft('M1V1M2ForPM', '_Met2Layer')[0][0]) / 2, self.getXY('M1V1M2ForPM')[0][1]],
                [(self.getXYRight('M1V1M2ForPM', '_Met2Layer')[-1][0] + self.getXYLeft('M1V1M2ForPM', '_Met2Layer')[0][0]) / 2, self.getXY('M1V1M2ForNM')[0][1]]
            ]
        )

        # M2V
        topBoundary_M2V = self.getXY('M1V1M2ForPM')[0][1]
        botBoundary_M2V = self.getXY('M1V1M2ForNM')[0][1]

        tmpXYs = []
        for i, XYs in enumerate(self.getXY('M1V1M2ForPM')):
            if i % 2 == 0:
                tmpXYs.append([XYs[0], (topBoundary_M2V + botBoundary_M2V) / 2])
            else:
                pass

        self._DesignParameter['M2V'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=self.getXWidth('M1V1M2ForPM', '_Met2Layer'),
            _YWidth=topBoundary_M2V-botBoundary_M2V,
            _XYCoordinates=tmpXYs
        )

        ''' ---------------------------------------------- Input Via ----------------------------------------------- '''
        if len(self.getXY('M2V')) >= 2:
            rightBoundary_InputVia = self.getXYLeft('M2V')[1][0] - _DRCObj._Metal1MinSpaceAtCorner
            leftBoundary_InputVia = self.getXYRight('M2V')[0][0] + _DRCObj._Metal1MinSpaceAtCorner

            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=rightBoundary_InputVia-leftBoundary_InputVia, YWidth=self.getYWidth('PolyContact', '_Met1Layer'))
            self._DesignParameter['M1V1M2ForInputVia'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2ForInputViaIn{}'.format(_Name)))[0]
            self._DesignParameter['M1V1M2ForInputVia']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
            self._DesignParameter['M2V2M3ForInputVia'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3ForInputViaIn{}'.format(_Name)))[0]
            self._DesignParameter['M2V2M3ForInputVia']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))

            XOffset = (self.getXY('M2V')[1][0] - self.getXY('M2V')[0][0]) / 2
            tmpXYs = []
            for i, XYs in enumerate(self.getXY('M2V')):
                if i != len(self.getXY('M2V')) - 1:
                    tmpXYs.append([XYs[0] + XOffset, self.getXY('PolyContact')[0][1]])
                else:
                    pass
            self._DesignParameter['M1V1M2ForInputVia']['_XYCoordinates'] = tmpXYs
            self._DesignParameter['M2V2M3ForInputVia']['_XYCoordinates'] = tmpXYs

        else:
            pass
            # rightBoundary_InputVia = self.getXYRight('PolyContact', '_Met1Layer')[0][0]
            # leftBoundary_InputVia = self.getXYRight('M2V')[0][0] + _DRCObj._Metal1MinSpaceAtCorner
            #
            # NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=rightBoundary_InputVia - leftBoundary_InputVia, YWidth=self.getYWidth('PolyContact', '_Met1Layer'))
            # self._DesignParameter['M1V1M2ForInputVia'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2ForInputViaIn{}'.format(_Name)))[0]
            # self._DesignParameter['M1V1M2ForInputVia']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1]))
            # self._DesignParameter['M1V1M2ForInputVia']['_XYCoordinates'] = [
            #     [(rightBoundary_InputVia + leftBoundary_InputVia) / 2, self.getXY('PolyContact')[0][1]]
            # ]

        # M3 Input
        rightBoundary_M3Input = self.getXYRight('M2V2M3ForInputVia', '_Met3Layer')[-1][0]
        leftBoundary_M3Input = self.getXYLeft('M2V2M3ForInputVia', '_Met3Layer')[0][0]

        self._DesignParameter['M3H_Input'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=rightBoundary_M3Input-leftBoundary_M3Input,
            _YWidth=self.getYWidth('M2V2M3ForInputVia', '_Met3Layer'),
            _XYCoordinates=[[(rightBoundary_M3Input + leftBoundary_M3Input) / 2, self.getXY('M2V2M3ForInputVia')[0][1]]]
        )


        ''' ---------------------------------------------- PIN ----------------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0,1,1], _Reflect=[0,0,0], _Angle=0,
            _XYCoordinates=self.getXY('VSSRail'), _Mag=0.04,  _TEXT='VSS')
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=self.getXY('VDDRail'), _Mag=0.04, _TEXT='VDD')

        self._DesignParameter['PIN_VIN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('M3H_Input')[0]], _Mag=0.04, _TEXT='VIN')

        self._DesignParameter['PIN_VOUT'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Angle=0,
            _XYCoordinates=[self.getXY('M2V')[0]], _Mag=0.04, _TEXT='VOUT')

        ''' ---------------------------------------------- XVT Layer ----------------------------------------------- '''
        _XVTLayer = '_' + XVT + 'Layer'
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0],
            _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXWidth('PMOS', _XVTLayer),
            _YWidth=self.getXYBot('PMOS', _XVTLayer)[0][1] - self.getXYTop('NMOS', _XVTLayer)[0][1],
            _XYCoordinates=[[0, (self.getXYBot('PMOS', _XVTLayer)[0][1] + self.getXYTop('NMOS', _XVTLayer)[0][1]) / 2]]
        )

        ''' ------------------------------------------- NWELL Layer ------------------------------------------- '''
        XWidth_NW_case1 = self.getXWidth('VDDRail', '_ODLayer') + 2 * _DRCObj._NwMinEnclosurePactive
        XWidth_NW_case2 = self.getXWidth('PMOS', '_ODLayer') + 2 * _DRCObj._NwMinEnclosurePactive2
        XWidth_NW = max(XWidth_NW_case1, XWidth_NW_case2)

        topBoundary_NW = self.getXYTop('VDDRail', '_ODLayer')[0][1] + _DRCObj._NwMinEnclosurePactive
        botBoundary_NW = self.getXYBot('PMOS', '_ODLayer')[0][1] - _DRCObj._NwMinEnclosurePactive
        YWidth_NW = topBoundary_NW - botBoundary_NW

        if (XWidth_NW * YWidth_NW) < _DRCObj._NwMinArea:
            XWidth_NW = self.CeilMinSnapSpacing(_DRCObj._NwMinArea / YWidth_NW, 2 * MinSnapSpacing)
        else:
            pass

        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=XWidth_NW,
            _YWidth=YWidth_NW,
            _XYCoordinates=[[0, (topBoundary_NW + botBoundary_NW) / 2]]
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

    libname = 'TEST_Inverter'
    cellname = 'Inverter'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams_20G = dict(
        NumFinger=16,       # 16
        Width_NM=200,
        Width_PM=600,       # 200
    )
    InputParams_16G = dict(
        NumFinger=15,
        Width_NM=200,
        Width_PM=600,
    )
    InputParams_12G = dict(
        NumFinger=15,
        Width_NM=200,
        Width_PM=600,
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
        LayoutObj = Inverter(_Name=cellname)
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

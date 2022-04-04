import StickDiagram
import DesignParameters
import copy
import DRC
from IksuJang.BasicArchive import NMOSWithDummy
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import PSubRing
from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from SthPack import CoordCalc


class NMOSSET(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='NMOSSET'):
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

                                  ChannelLength=30,
                                  XVT='SLVT',

                                  NumContactY_NM1=1,        # option
                                  NumContactY_NM23=2,       # option
                                  NumContactY_NM45=1,       # option
                                  NumContact_Subring=2,     # option

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
        self._DesignParameter['NM1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM23, _NMOSChannelWidth=Width_NM23, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM3In{}'.format(_Name)))[0]
        self._DesignParameter['NM3']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM23, _NMOSChannelWidth=Width_NM23, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM4'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM4In{}'.format(_Name)))[0]
        self._DesignParameter['NM4']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM45, _NMOSChannelWidth=Width_NM45, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['NM5'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM5In{}'.format(_Name)))[0]
        self._DesignParameter['NM5']['_DesignObj']._CalculateDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM45, _NMOSChannelWidth=Width_NM45, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))

        XCoordOfNM5 = self._DesignParameter['NM5']['_DesignObj'].CellXWidth / 2 + _UnitPitch / 2
        self._DesignParameter['NM4']['_XYCoordinates'] = [[-XCoordOfNM5, 0]]
        self._DesignParameter['NM5']['_XYCoordinates'] = [[+XCoordOfNM5, 0]]

        XCoordOfNM3 = XCoordOfNM5 + self._DesignParameter['NM5']['_DesignObj'].CellXWidth / 2 + _UnitPitch + self._DesignParameter['NM3']['_DesignObj'].CellXWidth / 2
        self._DesignParameter['NM2']['_XYCoordinates'] = [[-XCoordOfNM3, 0]]
        self._DesignParameter['NM3']['_XYCoordinates'] = [[+XCoordOfNM3, 0]]


        ''' ------------------------------ M1V1M2 on NM2~4 Source/Drain & Metal2 Route ----------------------------- '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('NM4', '_Met1Layer'), YWidth=self.getYWidth('NM4', '_Met1Layer'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnNM2345Up'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM2345UpIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM2345Up']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)
        self._DesignParameter['M1V1M2OnNM2345Dn'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM2345DnIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM2345Dn']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)

        self._DesignParameter['M1V1M2OnNM45Middle'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM45MiddleIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM45Middle']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(
            **dict(_ViaMet12Met2NumberOfCOX=NumViaXY[0], _ViaMet12Met2NumberOfCOY=NumViaXY[1] - 1))
        self._DesignParameter['M2V2M3OnNM45Middle'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnNM45MiddleIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnNM45Middle']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1] - 1))
        self._DesignParameter['M3V3M4OnNM45Middle'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNM45MiddleIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNM45Middle']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1] - 1))

        tmpXYs_Up = []
        tmpXYs_Dn = []
        tmpXYs_Middle = []
        offsetY = (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) / 4
        for i, XYs in enumerate(self.getXY('NM5', '_Met1Layer')):
            if i % 2 == 1:
                tmpXYs_Up.append(CoordCalc.Sum(XYs, [0, self.FloorMinSnapSpacing(+offsetY, MinSnapSpacing)]))
            elif i == 0:
                tmpXYs_Middle.append(CoordCalc.Sum(XYs, [0, self.FloorMinSnapSpacing(+offsetY, MinSnapSpacing)]))
            else:
                pass
        for i, XYs in enumerate(self.getXY('NM3', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_Up.append(CoordCalc.Sum(XYs, [0, self.FloorMinSnapSpacing(+offsetY, MinSnapSpacing)]))
            else:
                tmpXYs_Dn.append(CoordCalc.Sum(XYs, [0, self.FloorMinSnapSpacing(-offsetY, MinSnapSpacing)]))

        self._DesignParameter['M1V1M2OnNM2345Up']['_XYCoordinates'] = tmpXYs_Up + CoordCalc.FlipXs(tmpXYs_Up)
        self._DesignParameter['M1V1M2OnNM2345Dn']['_XYCoordinates'] = tmpXYs_Dn + CoordCalc.FlipXs(tmpXYs_Dn)

        self._DesignParameter['M1V1M2OnNM45Middle']['_XYCoordinates'] = tmpXYs_Middle + CoordCalc.FlipXs(tmpXYs_Middle)
        self._DesignParameter['M2V2M3OnNM45Middle']['_XYCoordinates'] = tmpXYs_Middle + CoordCalc.FlipXs(tmpXYs_Middle)
        self._DesignParameter['M3V3M4OnNM45Middle']['_XYCoordinates'] = tmpXYs_Middle + CoordCalc.FlipXs(tmpXYs_Middle)

        # M2H Up
        YCoord_M2HUp = max((self.getXYTop('M1V1M2OnNM2345Dn', '_Met2Layer')[0][1] + _DRCObj._MetalxMinSpaceAtCorner), self.getXYTop('M1V1M2OnNM2345Up', '_Met2Layer')[0][1]) + _DRCObj._MetalxMinWidth / 2
        XCoord_M2HUp = (CoordCalc.getXYCoords_MaxX(tmpXYs_Up)[0][0] + CoordCalc.getXYCoords_MinX(tmpXYs_Up)[0][0]) / 2
        XWidth_M2HUp = CoordCalc.getDistanceBtwMinMaxX(tmpXYs_Up) + self.getXWidth('M1V1M2OnNM2345Up', '_Met2Layer')

        self._DesignParameter['M2HUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=XWidth_M2HUp,
            _YWidth=_DRCObj._MetalxMinWidth,
            _XYCoordinates=[[+XCoord_M2HUp, YCoord_M2HUp], [-XCoord_M2HUp, YCoord_M2HUp]]
        )

        # M2H Up
        YCoord_M2HDn = min((self.getXYBot('M1V1M2OnNM2345Up', '_Met2Layer')[0][1] - _DRCObj._MetalxMinSpaceAtCorner), self.getXYBot('M1V1M2OnNM2345Dn', '_Met2Layer')[0][1]) - _DRCObj._MetalxMinWidth / 2
        XCoord_M2HDn = (CoordCalc.getXYCoords_MaxX(self.getXY('M1V1M2OnNM2345Dn'))[0][0] + CoordCalc.getXYCoords_MinX(self.getXY('M1V1M2OnNM2345Dn'))[0][0]) / 2
        XWidth_M2HDn = CoordCalc.getDistanceBtwMinMaxX(self.getXY('M1V1M2OnNM2345Dn')) + self.getXWidth('M1V1M2OnNM2345Up', '_Met2Layer')

        self._DesignParameter['M2HDn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=XWidth_M2HDn,
            _YWidth=_DRCObj._MetalxMinWidth,
            _XYCoordinates=[[XCoord_M2HDn, YCoord_M2HDn]]
        )


        ''' ------------------------------------ PolyContact On NM2,3 ---------------------------------------------- '''
        XWidth_PCCOM1_NM23 = CoordCalc.getDistanceBtwMinMaxX(self.getXY('NM3', '_POLayer')) + self.getXWidth('NM3', '_POLayer')
        XNum_PCCOM1_NM23 = int((XWidth_PCCOM1_NM23 - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = XNum_PCCOM1_NM23
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumContactY_NM23 if NumContactY_NM23 is not None else 2
        self._DesignParameter['PolyContactOnNM23'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnNM23In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnNM23']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        YCoord_PolyContactOnNM23 = self.FloorMinSnapSpacing(self.getXYBot('NM3', '_Met1Layer')[0][1] - _DRCObj._Metal1MinSpace2 - self.getYWidth('PolyContactOnNM23', '_Met1Layer') / 2, MinSnapSpacing)
        self._DesignParameter['PolyContactOnNM23']['_XYCoordinates'] = [
            [self.getXY('NM2')[0][0], YCoord_PolyContactOnNM23],
            [self.getXY('NM3')[0][0], YCoord_PolyContactOnNM23]
        ]

        self._DesignParameter['POH_NM23'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=XWidth_PCCOM1_NM23,
            _YWidth=self.getYWidth('PolyContactOnNM23', '_POLayer'),
            _XYCoordinates=self.getXY('PolyContactOnNM23')
        )

        self._DesignParameter['POV_NM23'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('NM3', '_POLayer'),
            _YWidth=self.CeilMinSnapSpacing(self.getXYBot('NM3', '_POLayer')[0][1] - self.getXYTop('POH_NM23')[0][1], MinSnapSpacing)
        )
        YCoord_POV_NM34 = (self.getXYBot('NM3', '_POLayer')[0][1] + self.getXYTop('POH_NM23')[0][1]) / 2

        tmpXYs = []
        for XYs in (self.getXY('NM2', '_POLayer') + self.getXY('NM3', '_POLayer')):
            tmpXYs.append([XYs[0], YCoord_POV_NM34])
        self._DesignParameter['POV_NM23']['_XYCoordinates'] = tmpXYs



        ''' ------------------------------------ PolyContact On NM4,5 ---------------------------------------------- '''
        XWidth_PCCOM1_NM45 = CoordCalc.getDistanceBtwMinMaxX(self.getXY('NM5', '_POLayer')) + self.getXWidth('NM5', '_POLayer')
        XNum_PCCOM1_NM45 = int((XWidth_PCCOM1_NM45 - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = XNum_PCCOM1_NM45 if XNum_PCCOM1_NM45 > 1 else 1
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumContactY_NM45 if NumContactY_NM45 is not None else 1
        self._DesignParameter['PolyContactOnNM45'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnNM45In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnNM45']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        YCoord_PolyContactOnNM45 = self.CeilMinSnapSpacing(self.getXYTop('NM5', '_Met1Layer')[0][1] + _DRCObj._Metal1MinSpace2 + self.getYWidth('PolyContactOnNM45', '_Met1Layer') / 2, MinSnapSpacing)
        self._DesignParameter['PolyContactOnNM45']['_XYCoordinates'] = [
            [self.getXY('NM4')[0][0], YCoord_PolyContactOnNM45],
            [self.getXY('NM5')[0][0], YCoord_PolyContactOnNM45]
        ]

        self._DesignParameter['POH_NM45'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=XWidth_PCCOM1_NM45,
            _YWidth=self.getYWidth('PolyContactOnNM45', '_POLayer'),
            _XYCoordinates=self.getXY('PolyContactOnNM45')
        )

        self._DesignParameter['POV_NM45'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('NM5', '_POLayer'),
            _YWidth=self.getXYBot('POH_NM45')[0][1] - self.getXYTop('NM3', '_POLayer')[0][1]
        )
        YCoord_POV_NM45 = (self.getXYBot('POH_NM45')[0][1] + self.getXYTop('NM3', '_POLayer')[0][1]) / 2

        tmpXYs = []
        for XYs in (self.getXY('NM4', '_POLayer') + self.getXY('NM5', '_POLayer')):
            tmpXYs.append([XYs[0], YCoord_POV_NM45])
        self._DesignParameter['POV_NM45']['_XYCoordinates'] = tmpXYs


        ''' ------------------------------------------ Metal1 For NM4,5 -------------------------------------------- '''
        tmpXYs = []
        for i, XYs in enumerate(self.getXYBot('NM5', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs.append(XYs)
            else:
                pass

        self._DesignParameter['Met1H_NM45'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getDistanceBtwMinMaxX(tmpXYs) + self.getXWidth('NM5', '_Met1Layer'),
            _YWidth=self.getXWidth('NM5', '_Met1Layer')
        )
        XCoord_Met1H_NM45 = (CoordCalc.getXYCoords_MaxX(tmpXYs)[0][0] + CoordCalc.getXYCoords_MinX(tmpXYs)[0][0]) / 2
        YCoord_Met1H_NM45 = min(self.getXYBot('NM5', '_Met1Layer')[0][1], self.getXYBot('M1V1M2OnNM2345Dn', '_Met1Layer')[0][1])\
                            - _DRCObj._Metal1MinSpaceAtCorner - self.getYWidth('Met1H_NM45') / 2

        self._DesignParameter['Met1H_NM45']['_XYCoordinates'] = [
            [-XCoord_Met1H_NM45, YCoord_Met1H_NM45],
            [+XCoord_Met1H_NM45, YCoord_Met1H_NM45],
        ]

        self._DesignParameter['Met1V_NM45'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('NM5', '_Met1Layer'),
            _YWidth=self.getXYBot('NM5', '_Met1Layer')[0][1] - self.getXYTop('Met1H_NM45')[0][1]
        )
        YCoord_Met1V_NM45 = (self.getXYBot('NM5', '_Met1Layer')[0][1] + self.getXYTop('Met1H_NM45')[0][1]) / 2

        tmp2XYs = []
        for XYs in tmpXYs:
            tmp2XYs.append([XYs[0], YCoord_Met1V_NM45])
        self._DesignParameter['Met1V_NM45']['_XYCoordinates'] = tmp2XYs + CoordCalc.FlipXs(tmp2XYs)


        ''' --------------------------------------- M1V1M2 On NM4,5's Gate --------------------------------------------- '''
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnNM45', '_Met1Layer'), YWidth=_DRCObj._VIAxMinWidth)
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (2,1)

        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = 1
        self._DesignParameter['M1V1M2OnNM45Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM45Gate{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM45Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**ViaParams)

        YCoord_M1V1M2OnNM45Gate = self.getXYTop('M2HUp')[0][1] + _DRCObj._MetalxMinSpace2 + self.getYWidth('M1V1M2OnNM45Gate', '_Met2Layer') / 2
        self._DesignParameter['M1V1M2OnNM45Gate']['_XYCoordinates'] = [
            [self.getXY('PolyContactOnNM45')[0][0], YCoord_M1V1M2OnNM45Gate],
            [self.getXY('PolyContactOnNM45')[1][0], YCoord_M1V1M2OnNM45Gate]
        ]

        self._DesignParameter['PolyContactOnNM45']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('M1V1M2OnNM45Gate', '_Met1Layer')


        ''' -------------------------------------------------------------------------------------------------------- '''
        self._DesignParameter['NM1']['_XYCoordinates'] = [[0, -1500]]

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('NM1', '_Met1Layer'), YWidth=self.getYWidth('NM1', '_Met1Layer'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnNM1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM1In{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)

        tmpXYs_Drain = []
        for i, XYs in enumerate(self.getXY('NM1', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_Drain.append(XYs)
            else:
                pass
        self._DesignParameter['M1V1M2OnNM1']['_XYCoordinates'] = tmpXYs_Drain

        self._DesignParameter['M2V2M3OnNM1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnNM1In{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnNM1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(
            **dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnNM1']['_XYCoordinates'] = tmpXYs_Drain
        self._DesignParameter['M3V3M4OnNM1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnNM1In{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnNM1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(
            **dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnNM1']['_XYCoordinates'] = tmpXYs_Drain


        self._DesignParameter['Met2H_NM1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=CoordCalc.getDistanceBtwMinMaxX(self.getXY('M1V1M2OnNM1')),
            _YWidth=_DRCObj._Metal1MinWidth,
            _XYCoordinates=[[(self.getXY('M1V1M2OnNM1')[-1][0] + self.getXY('M1V1M2OnNM1')[0][0]) / 2, self.getXY('NM1')[0][1]]]
        )
        self._DesignParameter['Met3H_NM1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('Met2H_NM1'),
            _YWidth=self.getYWidth('Met2H_NM1'),
            _XYCoordinates=self.getXY('Met2H_NM1')
        )
        self._DesignParameter['Met4H_NM1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0],
            _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('Met2H_NM1'),
            _YWidth=self.getYWidth('Met2H_NM1'),
            _XYCoordinates=self.getXY('Met2H_NM1')
        )

        ''' ------------------------------------ PolyContact On NM1 ---------------------------------------------- '''
        XWidth_PCCOM1_NM1 = CoordCalc.getDistanceBtwMinMaxX(self.getXY('NM1', '_POLayer')) + self.getXWidth('NM1', '_POLayer')
        XNum_PCCOM1_NM1 = int((XWidth_PCCOM1_NM1 - 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = XNum_PCCOM1_NM1 if XNum_PCCOM1_NM1 > 1 else 1
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumContactY_NM1 if NumContactY_NM1 is not None else 1
        self._DesignParameter['PolyContactOnNM1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnNM1In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnNM1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        YCoord_PolyContactOnNM1 = self.CeilMinSnapSpacing(self.getXYTop('NM1', '_Met1Layer')[0][1] + _DRCObj._Metal1MinSpace2 + self.getYWidth('PolyContactOnNM1', '_Met1Layer') / 2, MinSnapSpacing)
        self._DesignParameter['PolyContactOnNM1']['_XYCoordinates'] = [[self.getXY('NM1')[0][0], YCoord_PolyContactOnNM1]]
        self._DesignParameter['PolyContactOnNM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PCCOM1_NM1

        self._DesignParameter['POV_NM1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('NM1', '_POLayer'),
            _YWidth=self.getXYBot('PolyContactOnNM1', '_POLayer')[0][1] - self.getXYTop('NM1', '_POLayer')[0][1]
        )
        YCoord_POV_NM1 = (self.getXYBot('PolyContactOnNM1', '_POLayer')[0][1] + self.getXYTop('NM1', '_POLayer')[0][1]) / 2

        tmpXYs = []
        for XYs in self.getXY('NM1', '_POLayer'):
            tmpXYs.append([XYs[0], YCoord_POV_NM1])
        self._DesignParameter['POV_NM1']['_XYCoordinates'] = tmpXYs

        #
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnNM1', '_Met1Layer'), YWidth=self.getYWidth('PolyContactOnNM1', '_Met1Layer'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnNM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnNM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnNM1Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**ViaParams)
        self._DesignParameter['M1V1M2OnNM1Gate']['_XYCoordinates'] = self.getXY('PolyContactOnNM1')

        ViaParams = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        ViaParams['_ViaMet22Met3NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet22Met3NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M2V2M3OnNM1Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnNM1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnNM1Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**ViaParams)
        self._DesignParameter['M2V2M3OnNM1Gate']['_XYCoordinates'] = self.getXY('PolyContactOnNM1')



        #
        # 'NM1', 'M1V1M2OnNM1', 'M2V2M3OnNM1', 'M3V3M4OnNM1', 'Met2H_NM1', 'Met3H_NM1', 'Met4H_NM1', 'PolyContactOnNM1', 'POV_NM1'



        ''' ---------------------------------------------- PSubring ------------------------------------------------ '''
        _DRCtemp_metal1minspace = 165

        XWidthOfSubring1_ODtoOD = self.getXYRight('NM3', '_ODLayer')[0][0] + _DRCObj._OdMinSpace                ## ???
        XWidthOfSubring3_Met1toMet1 = self.getXYRight('NM3', '_Met1Layer')[0][0] + _DRCtemp_metal1minspace      ## ???
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring3_Met1toMet1) * 2

        YdownwardOfSubring = self.getXYBot('NM1', '_Met1Layer')[0][1] - _DRCObj._Metal1DefaultSpace     ## ???
        YupwardOfSubring = self.getXYTop('M1V1M2OnNM45Gate', '_Met1Layer')[0][1] + _DRCObj._Metal1DefaultSpace       ## ???

        YWidthOfSubring = YupwardOfSubring - YdownwardOfSubring
        YcenterOfSubring = (YupwardOfSubring + YdownwardOfSubring) / 2

        self._DesignParameter['PSubring'] = self._SrefElementDeclaration(
            _DesignObj=PSubRing.PSubRing(_Name='PSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=1000, width=1000, contact=NumContact_Subring if NumContact_Subring is not None else 2))
        self._DesignParameter['PSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=YWidthOfSubring + self.getYWidth('PSubring', 'met_top'),
                   width=XWidthOfSubring + self.getXWidth('PSubring', 'met_right'),
                   contact=NumContact_Subring if NumContact_Subring is not None else 2))
        self._DesignParameter['PSubring']['_XYCoordinates'] = [[0, YcenterOfSubring]]


        ''' --------------------------------- from NM1's source to Subring ------------------------------------------- '''
        self._DesignParameter['Met1V_NM1Source'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('NM1', '_Met1Layer'),
            _YWidth=self.getXYBot('NM1', '_Met1Layer')[0][1] - self.getXYTop('PSubring', 'met_bot')[0][1]
        )
        YCoord_Met1V_NM1Source = (self.getXYBot('NM1', '_Met1Layer')[0][1] + self.getXYTop('PSubring', 'met_bot')[0][1]) / 2
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('NM1', '_Met1Layer')):
            if i % 2 == 1:
                tmpXYs.append([XYs[0], YCoord_Met1V_NM1Source])
            else:
                pass
        self._DesignParameter['Met1V_NM1Source']['_XYCoordinates'] = tmpXYs









        ''' ---------------------------------------------- XVT Layer ----------------------------------------------- '''
        _XVTLayer = '_' + XVT + 'Layer'
        self._DesignParameter['XVTLayer1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0],
            _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXY('NM3')[0][0]-self.getXY('NM2')[0][0],
            _YWidth=self.getYWidth('NM2', _XVTLayer),
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['XVTLayer2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0],
            _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXWidth('NM1', _XVTLayer),
            _YWidth=self.getXYBot('NM4', _XVTLayer)[0][1] - self.getXYTop('NM1', _XVTLayer)[0][1],
            _XYCoordinates=[[0, self.CeilMinSnapSpacing((self.getXYBot('NM4', _XVTLayer)[0][1] + self.getXYTop('NM1', _XVTLayer)[0][1]) / 2, MinSnapSpacing)]]
        )

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
    cellname = 'NMOSSET'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams1 = dict(
        NumFinger_NM1=8,
        NumFinger_NM23=12,
        NumFinger_NM45=2,
        Width_NM1=1000,
        Width_NM23=1000,
        Width_NM45=1000,

        ChannelLength=30,
        XVT='SLVT',

        NumContactY_NM1=1,
        NumContactY_NM23=2,
        NumContactY_NM45=1,
        NumContact_Subring=2
    )

    InputParams2 = dict(
        NumFinger_NM1=20,
        NumFinger_NM23=8,
        NumFinger_NM45=1,
        Width_NM1=300,
        Width_NM23=1000,
        Width_NM45=1000,

        ChannelLength=30,
        XVT='SLVT',

        NumContactY_NM1=1,
        NumContactY_NM23=2,
        NumContactY_NM45=1,
        NumContact_Subring=2
    )
    InputParams = InputParams1

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass
        print("=============================   Last Layout Object's Input Parameters are   ===========================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("=======================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = NMOSSET(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('##################################      Sending to FTP Server...      #################################')
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
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number Of Run : {Num_DRCCheck}')
                    # elapsed time, start time, end time, main python file name
                else:
                    pass
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print('########################################      Finished       ###########################################')

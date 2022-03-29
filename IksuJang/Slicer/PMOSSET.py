import StickDiagram
import DesignParameters
import copy
import math
import DRC
from IksuJang.BasicArchive import PMOSWithDummy
from IksuJang.BasicArchive import NSubRing
from IksuJang.BasicArchive import ViaPoly2Met1
from IksuJang.BasicArchive import ViaMet12Met2
from IksuJang.BasicArchive import ViaMet22Met3
from IksuJang.BasicArchive import ViaMet32Met4
from SthPack import CoordCalc


class PMOSSET(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='PMOSSET'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger_PM12=2,
                                  NumFinger_PM34=3,
                                  NumFinger_PM56=6,
                                  Width_PM=1000,

                                  ChannelLength=30,
                                  XVT='SLVT',

                                  NumContactY_PM=1,        # option
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
        self._DesignParameter['PM1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM1In{}'.format(_Name)))[0]
        self._DesignParameter['PM1']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM12, _PMOSChannelWidth=Width_PM, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['PM2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM2In{}'.format(_Name)))[0]
        self._DesignParameter['PM2']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM12, _PMOSChannelWidth=Width_PM, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))

        self._DesignParameter['PM35'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM35In{}'.format(_Name)))[0]
        self._DesignParameter['PM35']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM34+NumFinger_PM56, _PMOSChannelWidth=Width_PM, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
        self._DesignParameter['PM46'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM46In{}'.format(_Name)))[0]
        self._DesignParameter['PM46']['_DesignObj']._CalculateDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM34 + NumFinger_PM56, _PMOSChannelWidth=Width_PM,
                   _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))


        XCoordOfPM2 = self._DesignParameter['PM2']['_DesignObj'].CellXWidth / 2 + _UnitPitch / 2
        self._DesignParameter['PM1']['_XYCoordinates'] = [[-XCoordOfPM2, 0]]
        self._DesignParameter['PM2']['_XYCoordinates'] = [[+XCoordOfPM2, 0]]

        XCoordOfPM46 = XCoordOfPM2 + self._DesignParameter['PM2']['_DesignObj'].CellXWidth / 2 + _UnitPitch + self._DesignParameter['PM46']['_DesignObj'].CellXWidth / 2
        self._DesignParameter['PM35']['_XYCoordinates'] = [[-XCoordOfPM46, 0]]
        self._DesignParameter['PM46']['_XYCoordinates'] = [[+XCoordOfPM46, 0]]


        ''' ------------------------------------ PolyContact On PM  ---------------------------------------------- '''
        # PM12
        XWidth_PCCOM1_PM12 = CoordCalc.getDistanceBtwMinMaxX(self.getXY('PM1', '_POLayer')) + self.getXWidth('PM1', '_POLayer')
        XNum_PCCOM1_PM12 = int((XWidth_PCCOM1_PM12 - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = XNum_PCCOM1_PM12
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumContactY_PM if NumContactY_PM is not None else 2
        self._DesignParameter['PolyContactOnPM12'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnPM12In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPM12']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        YCoord_PolyContactOnPM12 = self.FloorMinSnapSpacing(self.getXYBot('PM1', '_Met1Layer')[0][1] - _DRCObj._Metal1MinSpace2 - self.getYWidth('PolyContactOnPM12', '_Met1Layer') / 2, MinSnapSpacing)
        self._DesignParameter['PolyContactOnPM12']['_XYCoordinates'] = [
            [self.getXY('PM1')[0][0], YCoord_PolyContactOnPM12],
            [self.getXY('PM2')[0][0], YCoord_PolyContactOnPM12]
        ]
        self._DesignParameter['PolyContactOnPM12']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PCCOM1_PM12

        self._DesignParameter['POV_PM12'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('PM1', '_POLayer'),
            _YWidth=self.CeilMinSnapSpacing(self.getXYBot('PM1', '_POLayer')[0][1] - self.getXYTop('PolyContactOnPM12', '_POLayer')[0][1], MinSnapSpacing)
        )
        YCoord_POV_PM12 = (self.getXYBot('PM1', '_POLayer')[0][1] + self.getXYTop('PolyContactOnPM12', '_POLayer')[0][1]) / 2

        tmpXYs = []
        for XYs in (self.getXY('PM1', '_POLayer') + self.getXY('PM2', '_POLayer')):
            tmpXYs.append([XYs[0], YCoord_POV_PM12])
        self._DesignParameter['POV_PM12']['_XYCoordinates'] = tmpXYs

        # PM35, PM46
        XWidth_PCCOM1_PM46 = CoordCalc.getDistanceBtwMinMaxX(self.getXY('PM46', '_POLayer')) + self.getXWidth('PM46', '_POLayer')
        XNum_PCCOM1_PM46 = int((XWidth_PCCOM1_PM46 - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = XNum_PCCOM1_PM46
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumContactY_PM if NumContactY_PM is not None else 2
        self._DesignParameter['PolyContactOnPM35PM46'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactOnPM35PM46In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactOnPM35PM46']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        YCoord_PolyContactOnPM35PM46 = self.FloorMinSnapSpacing(self.getXYBot('PM46', '_Met1Layer')[0][1] - _DRCObj._Metal1MinSpace2 - self.getYWidth('PolyContactOnPM35PM46', '_Met1Layer') / 2, MinSnapSpacing)
        self._DesignParameter['PolyContactOnPM35PM46']['_XYCoordinates'] = [
            [self.getXY('PM35')[0][0], YCoord_PolyContactOnPM35PM46],
            [self.getXY('PM46')[0][0], YCoord_PolyContactOnPM35PM46]
        ]
        self._DesignParameter['PolyContactOnPM35PM46']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = XWidth_PCCOM1_PM46

        self._DesignParameter['POV_PM46'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('PM46', '_POLayer'),
            _YWidth=self.CeilMinSnapSpacing(self.getXYBot('PM46', '_POLayer')[0][1] - self.getXYTop('PolyContactOnPM35PM46', '_POLayer')[0][1], MinSnapSpacing)
        )
        YCoord_POV_PM46 = (self.getXYBot('PM46', '_POLayer')[0][1] + self.getXYTop('PolyContactOnPM35PM46', '_POLayer')[0][1]) / 2

        tmpXYs = []
        for XYs in (self.getXY('PM35', '_POLayer') + self.getXY('PM46', '_POLayer')):
            tmpXYs.append([XYs[0], YCoord_POV_PM46])
        self._DesignParameter['POV_PM46']['_XYCoordinates'] = tmpXYs


        ''' ------------------------------ M1V1M2 on PM12 Drain ----------------------------- '''
        tmpXYs_Source = []
        tmpXYs_Drain2 = []
        for i, XYs in enumerate(self.getXY('PM2', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs_Drain2.append(XYs)
            else:
                tmpXYs_Source.append(XYs)
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('PM2', '_Met1Layer'), YWidth=self.getYWidth('PM2', '_Met1Layer'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPM12Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM12DrainIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM12Drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)
        self._DesignParameter['M1V1M2OnPM12Drain']['_XYCoordinates'] = tmpXYs_Drain2 + CoordCalc.FlipXs(tmpXYs_Drain2)


        ''' ------------------------------ M1V1M2 on PM46,35 Drain ----------------------------- '''
        tmpXYs_D = []
        for i, XYs in enumerate(self.getXY('PM46', '_Met1Layer')):
            if NumFinger_PM34 % 2 == 0:
                if i % 2 == 0:
                    tmpXYs_Source.append(XYs)
                else:
                    tmpXYs_D.append(XYs)
            else:
                if i % 2 == 1:
                    tmpXYs_Source.append(XYs)
                else:
                    tmpXYs_D.append(XYs)

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(XWidth=self.getXWidth('PM46', '_Met1Layer'), YWidth=self.getYWidth('PM46', '_Met1Layer'))
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPM3456Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM3456DrainIn{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM3456Drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**ViaParams)
        self._DesignParameter['M1V1M2OnPM3456Drain']['_XYCoordinates'] = tmpXYs_D + CoordCalc.FlipXs(tmpXYs_D)


        # seperate PM4 and PM6
        tmpXYs_Drain4 = []
        tmpXYs_Drain6 = []
        for i, XYs in enumerate(tmpXYs_D):
            if i < math.ceil(NumFinger_PM34 / 2):
                tmpXYs_Drain4.append(XYs)
            else:
                tmpXYs_Drain6.append(XYs)

        self._DesignParameter['M2V2M3OnPM56Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnPM56DrainIn{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPM56Drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnPM56Drain']['_XYCoordinates'] = tmpXYs_Drain6 + CoordCalc.FlipXs(tmpXYs_Drain6)

        self._DesignParameter['M3V3M4OnPM56Drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4OnPM56DrainIn{}'.format(_Name)))[0]
        self._DesignParameter['M3V3M4OnPM56Drain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=NumViaXY[0], _ViaMet32Met4NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M3V3M4OnPM56Drain']['_XYCoordinates'] = tmpXYs_Drain6 + CoordCalc.FlipXs(tmpXYs_Drain6)

        # M2H, M3H, M4H
        XWidth_M2H = CoordCalc.getDistanceBtwMinMaxX(tmpXYs_Drain6) + self.getXWidth('M2V2M3OnPM56Drain', '_Met2Layer')
        XCoord_M2H = (CoordCalc.getXYCoords_MaxX(tmpXYs_Drain6)[0][0] + CoordCalc.getXYCoords_MinX(tmpXYs_Drain6)[0][0]) / 2
        YCoord_M2H = self.getXY('M2V2M3OnPM56Drain')[0][1]
        self._DesignParameter['M2H_PM56Drain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=XWidth_M2H,
            _YWidth=_DRCObj._MetalxMinWidth,
            _XYCoordinates=[[-XCoord_M2H,YCoord_M2H], [+XCoord_M2H,YCoord_M2H]]
        )
        self._DesignParameter['M3H_PM56Drain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('M2H_PM56Drain'),
            _YWidth=self.getYWidth('M2H_PM56Drain'),
            _XYCoordinates=self.getXY('M2H_PM56Drain')
        )
        self._DesignParameter['M4H_PM56Drain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
            _XWidth=self.getXWidth('M2H_PM56Drain'),
            _YWidth=self.getYWidth('M2H_PM56Drain'),
            _XYCoordinates=self.getXY('M2H_PM56Drain')
        )

        # PM2 - PM4 Drain Connection
        XWidth_M2H_PM24 = (CoordCalc.getXYCoords_MaxX(tmpXYs_Drain4)[0][0] - CoordCalc.getXYCoords_MinX(tmpXYs_Drain2)[0][0]) + self.getXWidth('M1V1M2OnPM12Drain', '_Met2Layer')
        XCoord_M2H_PM24 = (CoordCalc.getXYCoords_MaxX(tmpXYs_Drain4)[0][0] + CoordCalc.getXYCoords_MinX(tmpXYs_Drain2)[0][0]) / 2
        YCoord_M2H_PM24 = self.getXY('M1V1M2OnPM12Drain')[0][1]
        self._DesignParameter['M2H_PM2413Drain'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=XWidth_M2H_PM24,
            _YWidth=_DRCObj._MetalxMinWidth,
            _XYCoordinates=[[-XCoord_M2H_PM24, YCoord_M2H_PM24], [+XCoord_M2H_PM24, YCoord_M2H_PM24]]
        )

        ''' --------------------------------------- M1V1M2 On PM1,2's Gate --------------------------------------------- '''
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnPM12', '_Met1Layer'), YWidth=_DRCObj._VIAxMinWidth)
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (2, 1)

        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPM12Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM12Gate{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM12Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**ViaParams)
        self._DesignParameter['M1V1M2OnPM12Gate']['_XYCoordinates'] = self.getXY('PolyContactOnPM12')

        self._DesignParameter['PolyContactOnPM12']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('M1V1M2OnPM12Gate', '_Met1Layer')


        ''' ------------------------------- M1V1M2 & M2V2M3 On PM46,35's Gate -------------------------------------- '''
        try:
            NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(XWidth=self.getXWidth('PolyContactOnPM35PM46', '_Met1Layer'), YWidth=_DRCObj._VIAxMinWidth)
        except Exception as e:
            print('Error Occurred: ', e)
            NumViaXY = (2, 1)
        ViaParams = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        ViaParams['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['M1V1M2OnPM35PM46Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2OnPM35PM46Gate{}'.format(_Name)))[0]
        self._DesignParameter['M1V1M2OnPM35PM46Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**ViaParams)
        self._DesignParameter['M1V1M2OnPM35PM46Gate']['_XYCoordinates'] = self.getXY('PolyContactOnPM35PM46')

        self._DesignParameter['M2V2M3OnPM35PM46Gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3OnPM35PM46Gate{}'.format(_Name)))[0]
        self._DesignParameter['M2V2M3OnPM35PM46Gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=NumViaXY[0], _ViaMet22Met3NumberOfCOY=NumViaXY[1]))
        self._DesignParameter['M2V2M3OnPM35PM46Gate']['_XYCoordinates'] = self.getXY('PolyContactOnPM35PM46')


        ''' ---------------------------------------------- NSubring ------------------------------------------------ '''
        _DRCtemp_metal1minspace = 165

        XWidthOfSubring1_ODtoOD = self.getXYRight('PM46', '_ODLayer')[0][0] + _DRCObj._OdMinSpace                ## ???
        XWidthOfSubring3_Met1toMet1 = self.getXYRight('PM46', '_Met1Layer')[0][0] + _DRCtemp_metal1minspace      ## ???
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring3_Met1toMet1) * 2

        YdownwardOfSubring = self.getXYBot('PolyContactOnPM35PM46', '_Met1Layer')[0][1] - _DRCObj._Metal1DefaultSpace     ## ???
        YupwardOfSubring = self.getXYTop('PM1', '_Met1Layer')[0][1] + _DRCObj._Metal1DefaultSpace       ## ???

        YWidthOfSubring = YupwardOfSubring - YdownwardOfSubring
        YcenterOfSubring = (YupwardOfSubring + YdownwardOfSubring) / 2

        self._DesignParameter['NSubring'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='NSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['NSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=1000, width=1000, contact=NumContact_Subring if NumContact_Subring is not None else 2))
        self._DesignParameter['NSubring']['_DesignObj']._CalculateDesignParameter(
            **dict(height=YWidthOfSubring + self.getYWidth('NSubring', 'met_top'),
                   width=XWidthOfSubring + self.getXWidth('NSubring', 'met_right'),
                   contact=NumContact_Subring if NumContact_Subring is not None else 2))
        self._DesignParameter['NSubring']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['Nwell'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=XWidthOfSubring + self.getXWidth('NSubring', 'met_right'),
            _YWidth=YWidthOfSubring + self.getYWidth('NSubring', 'met_top'),
            _XYCoordinates=[[0, YcenterOfSubring]]
        )


        ''' --------------------------------- from NM1's source to Subring ----------------------------------------- '''
        self._DesignParameter['Met1V_Source'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('PM2', '_Met1Layer'),
            _YWidth=self.getXYBot('NSubring', 'met_top')[0][1] - self.getXYTop('PM2', '_Met1Layer')[0][1]
        )
        YCoord_Met1V_NM1Source = (self.getXYBot('NSubring', 'met_top')[0][1] + self.getXYTop('PM2', '_Met1Layer')[0][1]) / 2
        tmpXYs = []
        for XYs in tmpXYs_Source:
            tmpXYs.append([XYs[0], YCoord_Met1V_NM1Source])
        self._DesignParameter['Met1V_Source']['_XYCoordinates'] = tmpXYs + CoordCalc.FlipXs(tmpXYs)


        ''' ---------------------------------------- XVT & PP(BP) Layer -------------------------------------------- '''
        _XVTLayer = '_' + XVT + 'Layer'
        self._DesignParameter['XVTLayer1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXYLeft('PM46', _XVTLayer)[0][0]-self.getXYRight('PM35', _XVTLayer)[0][0],
            _YWidth=self.getYWidth('PM2', _XVTLayer),
            _XYCoordinates=[[0, 0]]
        )

        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=self.getXYLeft('PM46', '_PPLayer')[0][0] - self.getXYRight('PM35', '_PPLayer')[0][0],
            _YWidth=self.getYWidth('PM2', '_PPLayer'),
            _XYCoordinates=[[0, 0]]
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
    cellname = 'PMOSSET'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams1 = dict(
        NumFinger_PM12=2,
        NumFinger_PM34=3,
        NumFinger_PM56=6,
        Width_PM=1000,

        ChannelLength=30,
        XVT='SLVT',

        NumContactY_PM=1,  # option
        NumContact_Subring=2,  # option
    )

    InputParams2 = dict(
        NumFinger_PM12=2,
        NumFinger_PM34=3,
        NumFinger_PM56=3,
        Width_PM=500,

        ChannelLength=30,
        XVT='SLVT',

        NumContactY_PM=1,  # option
        NumContact_Subring=2,  # option
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
        LayoutObj = PMOSSET(_Name=cellname)
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

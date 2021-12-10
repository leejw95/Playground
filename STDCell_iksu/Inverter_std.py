import math
import copy

#
import StickDiagram
import DesignParameters
import DRC

#
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import PbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3

#
from SthPack import CoordCalc


class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=None,
                                           _ChannelWidth=None,
                                           _ChannelLength=None,
                                           _NPRatio=None,
                                           _Dummy=None,
                                           _XVT=None,
                                           _DistanceBtwFinger=None,

                                           _VDD2VSSHeight=None,
                                           _VDD2PMOSHeight=None,
                                           _VSS2NMOSHeight=None,
                                           )

    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateDesignParameter(self,
                                  _Finger=None,
                                  _ChannelWidth=None,
                                  _ChannelLength=None,
                                  _NPRatio=None,
                                  _Dummy=None,
                                  _XVT=None,
                                  _DistanceBtwFinger=None,
                                  _VDD2VSSHeight=None,
                                  _VDD2PMOSHeight=None,
                                  _VSS2NMOSHeight=None,

                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print(''.center(105, '#'))
        print('     {} Calculation Start     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))

        ''' ------------------------------------------ MOSFET Generation ------------------------------------------- '''
        # 1) _NMOS Generation ------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_XVT'] = _XVT
        NMOSparameters['_DistanceBtwFinger'] = _DistanceBtwFinger

        self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(
            _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)

        # 2) _PMOS Generation ------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)  # Need to Modify
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_XVT'] = _XVT
        PMOSparameters['_DistanceBtwFinger'] = _DistanceBtwFinger

        self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(
            _DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)

        ''' ---------------------------------------- Supply Rail Generation ---------------------------------------- '''
        self._CalculateSupplyRails(_NumSupplyCoY=1, _SupplyMet1YWidth=5)

        ''' -------------------------------------------- Via Generation -------------------------------------------- '''
        if _Finger not in (1, 2):
            NumViaYPMOS = int((self.getYWidth('_PMOS', '_Met1Layer') - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

            self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

            NumViaYNMOS = int((self.getYWidth('_NMOS', '_Met1Layer') - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

            self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIANMOSMet12)
        else:
            pass


        # 3) Input VIA Generation for Finger=1 / or calculate input poly-M1 contact YWidth     -> Need to check
        if _Finger in (1, 2):
            _VIAOnPolyGate_F1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _VIAOnPolyGate_F1['_ViaPoly2Met1NumberOfCOX'] = 1
            _VIAOnPolyGate_F1['_ViaPoly2Met1NumberOfCOY'] = 2
            self._DesignParameter['_VIAOnPolyGate_F1'] = self._SrefElementDeclaration(
                _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_F1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAOnPolyGate_F1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAOnPolyGate_F1)
            self._DesignParameter['_VIAOnPolyGate_F1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        else:
            WidthOfInputXM1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2  # how?? you have to choose / Need to Modify (by user input parameter) / ambiguous name


        ''' -------------------------------------------------------------------------------------------------------- '''
        ''' ------------------------------------------ Coordinates setting ----------------------------------------- '''
        ''' -------------------------------------------------------------------------------------------------------- '''
        # 2) Calculate Distance between 'MOSFET' and 'Input gate Contact'
        if _Finger not in (1, 2):
            if DesignParameters._Technology == '028nm':
                tmp_space = _DRCObj._Metal1MinSpaceAtCorner
            else:  # only checked when 65nm
                tmp_space = _DRCObj._Metal1MinSpace

            DistanceBtwNMOS2PolyInput = 0.5 * max(self.getYWidth('_NMOS', '_Met1Layer'),
                                                  self.getYWidth('_ViaMet12Met2OnNMOSOutput','_Met1Layer')) \
                                        + 0.5 * WidthOfInputXM1 + tmp_space
            DistanceBtwPMOS2PolyInput = 0.5 * max(self.getYWidth('_PMOS', '_Met1Layer'),
                                                  self.getYWidth('_ViaMet12Met2OnPMOSOutput', '_Met1Layer')) \
                                        + 0.5 * WidthOfInputXM1 + tmp_space
        else:
            pass

        # 5) Setting Coordinates of 'SupplyLines and MOSFETs'
        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, _VSS2NMOSHeight]]
        self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (_VDD2VSSHeight - _VDD2PMOSHeight)]]

        # 6) Setting Coordinates of 'Output Routing Via (M1V1M2)'
        if _Finger not in (1, 2):
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting')
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting')
        else:
            pass

        # Poly Boundary Generation MOS Gate -----------------------------------------------------------------------
        if _Finger not in (1, 2):
            self._DesignParameter['PolyRouteX'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
            self._DesignParameter['PolyRouteX']['_XWidth'] = CoordCalc.getDistanceBtwMinMaxX(self.getXY('_PMOS', '_POLayer')) + _ChannelLength
            self._DesignParameter['PolyRouteX']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # calculated when only one row -> should be changed
            self._DesignParameter['PolyRouteX']['_XYCoordinates'] = [
                CoordCalc.Add(self.getXY('_PMOS')[0], [0, -DistanceBtwPMOS2PolyInput]),
                CoordCalc.Add(self.getXY('_NMOS')[0], [0, +DistanceBtwNMOS2PolyInput])
            ]
        else:
            raise NotImplementedError



        # # Additional Poly Routing --------------------------------------------------------------------------------------
        # # Column Line
        # self._DesignParameter['_PolyRouteYOnPMOS'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        # self._DesignParameter['_PolyRouteYOnNMOS'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        # self._DesignParameter['_PolyRouteYOnPMOS']['_Width'] = _ChannelLength
        # self._DesignParameter['_PolyRouteYOnNMOS']['_Width'] = _ChannelLength
        #
        # tmpPolyRouteYOnPMOS, tmpPolyRouteYOnNMOS = [], []
        # for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
        #     tmpPolyRouteYOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
        #                                  self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
        #                                  self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] +
        #                                  self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
        #                                 [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
        #                                  self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
        #                                  self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] + self.getYWidth('_PolyRouteXOnPMOS') / 2]
        #                                 ])
        #     tmpPolyRouteYOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
        #                                  self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
        #                                  self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
        #                                  self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
        #                                 [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
        #                                  self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
        #                                  self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] - self.getYWidth('_PolyRouteXOnPMOS') / 2]
        #                                 ])
        #
        # self._DesignParameter['_PolyRouteYOnPMOS']['_XYCoordinates'] = tmpPolyRouteYOnPMOS
        # self._DesignParameter['_PolyRouteYOnNMOS']['_XYCoordinates'] = tmpPolyRouteYOnNMOS

        # VSS & VDD Supply Routing (Metal1) ----------------------------------------------------------------------------
        '''
        Function : Route 'VDD-PMOS(source)' and 'VSS-NMOS(source)' by 'METAL1'
                   (Set the Leftmost Metal of MOSFET as the source)
        Require  : NMOS, PMOS, NbodyContact, PbodyContact (Coordinates)
        '''

        tmpPathForSupplyRoutingOnPMOS, tmpPathForSupplyRoutingOnNMOS = [], []
        for XYs in self.getXY('_NMOS', '_XYCoordinateNMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnNMOS.append([
                [XYs[0], XYs[1] + self.getYWidth('_NMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('PbodyContact')[0][1]]
            ])
        for XYs in self.getXY('_PMOS', '_XYCoordinatePMOSSupplyRouting'):
            tmpPathForSupplyRoutingOnPMOS.append([
                [XYs[0], XYs[1] - self.getYWidth('_PMOS', '_Met1Layer') / 2],
                [XYs[0], self.getXY('NbodyContact')[0][1]]
            ])

        self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpPathForSupplyRoutingOnNMOS

        self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPathForSupplyRoutingOnPMOS

        # # Output Metal (1&2) Boundary & Routing ------------------------------------------------------------------------
        #
        # # Output M1 Routing (Column Line)
        # tmpOutputRoutingM1Y = []
        # for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2):
        #     tmpOutputRoutingM1Y.append([CoordCalc.Add(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting')[2 * i], [0, +self.getYWidth('_PMOS', '_Met1Layer')/2]),
        #                                 CoordCalc.Add(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting')[2 * i], [0, -self.getYWidth('_NMOS', '_Met1Layer')/2])
        #                                 ])  #
        #
        # if (_Finger % 4 == 2) and (_Finger != 2):  # exception case (6, 10, 14, 18, ...)
        #     del tmpOutputRoutingM1Y[-1]
        #     tmpOutputRoutingM1Y.append(
        #         [CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
        #                        self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[
        #                            '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1]),
        #          CoordCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
        #                        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[
        #                            '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])])
        # else:
        #     pass
        #
        # self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # # self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._Metal1MinWidth           # Need to Modify
        # self._DesignParameter['_OutputRouting']['_Width'] = self.getXWidth('_ViaMet12Met2OnNMOSOutput', '_Met1Layer')
        # self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRoutingM1Y
        #
        # if _Finger == 1:
        #     del self._DesignParameter['_ViaMet12Met2OnNMOSOutput']
        #     del self._DesignParameter['_ViaMet12Met2OnPMOSOutput']
        #
        # # Output M2 Routing (Row Line)
        # self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        # # self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth  # Need to Modify
        # self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._MetalxMinEnclosureVia3
        # self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = \
        #     [[CoordCalc.getXYCoords_MaxX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0],
        #       CoordCalc.getXYCoords_MinX(self.getXY('_PMOS', '_XYCoordinatePMOSOutputRouting'))[0]],
        #      [CoordCalc.getXYCoords_MaxX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0],
        #       CoordCalc.getXYCoords_MinX(self.getXY('_NMOS', '_XYCoordinateNMOSOutputRouting'))[0]]]
        #
        # # Input Contact (Poly to M1)------------------------------------------------------------------------------------
        # '''
        # Function : Make Contact(Poly to M1) for _PolyRouteXOn{}
        #            2 kind of calculation
        #            (1) surrounded by output metal(left and right)   if _Finger > 4
        #            (2) rightmost
        # Require : OutputRouting, _PolyRouteXOn{NMOS PMOS}, PMOS, NMOS
        #
        # '''
        # # (0)
        # _VIATempPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        # _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 3
        # _VIATempPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        # self._DesignParameter['_VIATempPoly2Met1'] = self._SrefElementDeclaration(
        #     _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1_TempIn{}'.format(_Name)))[0]
        # self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
        #     **_VIATempPoly2Met1)
        #
        # distance_input = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - \
        #                  self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1]
        # distance_contact = distance_input - \
        #                    self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_COLayer'][
        #                        '_YWidth']
        # distance_poly = distance_input - max(self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'],
        #                                      self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter[
        #                                          '_POLayer']['_YWidth'])
        # distance_metal1 = distance_input - \
        #                   self._DesignParameter['_VIATempPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                       '_YWidth']
        #
        # flag_poly = True if distance_poly < _DRCObj.DRCPolyMinSpace(
        #     _Width=self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth'],
        #     _ParallelLength=self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth']) else False
        # flag_metal = True if distance_metal1 < _DRCObj._Metal1MinSpace else False
        # flag_contact = True if distance_contact < _DRCObj._CoMinSpace else False
        # if (not flag_contact) and (not flag_metal) and (not flag_poly):
        #     flag_horizontal_inputvia_PCCOM1 = False
        #     Average2Up, Average2Dn = 0, 0
        # else:
        #     flag_horizontal_inputvia_PCCOM1 = True
        #     Average2Up = self.CeilMinSnapSpacing(float(distance_input) / 2.0, _DRCObj._MinSnapSpacing)
        #     Average2Dn = distance_input - Average2Up
        #
        #     self._DesignParameter['_PolyRouteXOnMOS'] = self._BoundaryElementDeclaration(
        #         _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
        #     self._DesignParameter['_PolyRouteXOnMOS']['_XWidth'] = self._DesignParameter['_PolyRouteXOnPMOS']['_XWidth']
        #     self._DesignParameter['_PolyRouteXOnMOS']['_YWidth'] = self.RounddownMinSnapSpacing(
        #         distance_input + self._DesignParameter['_PolyRouteXOnPMOS']['_YWidth'], 2 * _DRCObj._MinSnapSpacing)
        #     self._DesignParameter['_PolyRouteXOnMOS']['_XYCoordinates'] = [
        #         CoordCalc.Add(self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0],
        #                       [0, Average2Up])]
        #
        # # (1) surrounded by output metal  /  of Input Contact (Poly to M1)
        # if _Finger > 4:  # No Need else statement (when finger is 1, 2, 3, it covers on (2))
        #     ''' ************************ temporal DRC... Need 2 Modify Later ************************ '''
        #     if DesignParameters._Technology == '028nm':
        #         _tmpDRC_Metal1MinSpaceAtCorner = 70
        #         # _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner
        #     else:
        #         _tmpDRC_Metal1MinSpaceAtCorner = _DRCObj._Metal1MinSpaceAtCorner
        #
        #     # Calculate Number of Contact_X 'tmpNumCOX'
        #     lengthM1BtwOutputRouting = self._DesignParameter['_OutputRouting']['_XYCoordinates'][1][0][0] \
        #                                - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] \
        #                                - self._DesignParameter['_OutputRouting']['_Width'] \
        #                                - 2 * _tmpDRC_Metal1MinSpaceAtCorner
        #
        #     unitLengthBtwCOX = _DRCObj._CoMinWidth + _DRCObj._CoMinSpace
        #     tmpNumCOX = int((
        #                                 lengthM1BtwOutputRouting - _DRCObj._CoMinWidth - 2 * _DRCObj._Metal1MinEnclosureCO2) // unitLengthBtwCOX) + 1
        #
        #     # NMOS & PMOS
        #     _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        #     _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        #     _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
        #     _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmpNumCOX
        #     _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        #     _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        #
        #     self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(
        #         _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
        #     self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
        #         **_VIANMOSPoly2Met1)
        #     self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(
        #         _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
        #     self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
        #         **_VIAPMOSPoly2Met1)
        #
        #     tmpInputPCCOM1onNMOS, tmpInputPCCOM1onPMOS = [], []
        #     for i in range(0, len(self._DesignParameter['_OutputRouting']['_XYCoordinates']) - 1):
        #         tmpInputPCCOM1onNMOS.append(
        #             [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][2 * i + 1][0],
        #              self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up])
        #         tmpInputPCCOM1onPMOS.append(
        #             [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][2 * i + 1][0],
        #              self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn])
        #
        #     self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onNMOS
        #     self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = tmpInputPCCOM1onPMOS
        #
        #     # exception case
        #     if (_Finger % 4 == 2) and (_Finger != 2):
        #         del self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][-1]
        #         del self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][-1]
        #
        # ## (2) rightmost output metal  /  of Input Contact (Poly to M1)
        # if (_Finger % 4 == 2) and (_Finger != 2):  # exception case
        #     tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-2][0][0] \
        #                         + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
        #                         + _DRCObj._Metal1MinSpaceAtCorner
        #     tmpRightM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
        #                          - 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
        #                          - _DRCObj._Metal1MinSpaceAtCorner
        #     tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
        #     tmpRightCoBoundary = tmpRightM1Boundary - _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
        # elif _Finger != 1:
        #     tmpLeftM1Boundary = self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] \
        #                         + 0.5 * self._DesignParameter['_OutputRouting']['_Width'] \
        #                         + _DRCObj._Metal1MinSpaceAtCorner
        #     tmpRightPOBoundary = \
        #     self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] \
        #     + 0.5 * _ChannelLength
        #     tmpLeftCoBoundary = tmpLeftM1Boundary + _DRCObj._Metal1MinEnclosureCO2  # Calculate by M1-CO
        #     tmpRightCoBoundary = tmpRightPOBoundary - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide  # Calculate by PO-CO
        # elif (_Finger == 1) and (DesignParameters._Technology == '028nm'):
        #     tmpLeftCoBoundary = 0
        #     tmpRightCoBoundary = 0
        # else:
        #     raise NotImplementedError
        #
        # NumCoRightMost = int((tmpRightCoBoundary - tmpLeftCoBoundary - _DRCObj._CoMinWidth) // (
        #             _DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        #
        # if NumCoRightMost > 0:
        #     _VIAMOSPoly2Met1RightMost = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        #
        #     _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOX'] = NumCoRightMost
        #     _VIAMOSPoly2Met1RightMost['_ViaPoly2Met1NumberOfCOY'] = 1
        #
        #     self._DesignParameter['_VIAMOSPoly2Met1RightMost'] = self._SrefElementDeclaration(
        #         _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1RightMostOnNMOSGateIn{}'.format(_Name)))[0]
        #     self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
        #         **_VIAMOSPoly2Met1RightMost)
        #     self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'] = [
        #         [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
        #          self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] + Average2Up],
        #         [self.RounddownMinSnapSpacing((tmpLeftCoBoundary + tmpRightCoBoundary) / 2, MinSnapSpacing),
        #          self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] - Average2Dn]
        #     ]  # both NMOS & PMOS
        #
        # if '_VIAPMOSPoly2Met1_F1' in self._DesignParameter:
        #     self._DesignParameter['_VIANMOSPoly2Met1'] = self._DesignParameter['_VIANMOSPoly2Met1_F1']
        #     self._DesignParameter['_VIAPMOSPoly2Met1'] = self._DesignParameter['_VIAPMOSPoly2Met1_F1']
        #     del self._DesignParameter['_VIANMOSPoly2Met1_F1']
        #     del self._DesignParameter['_VIAPMOSPoly2Met1_F1']
        #
        # # Input Met1 Routing -------------------------------------------------------------------------------------------
        # '''
        # When there is a gap between (routed) poly gates, route them by Met1 (column line)
        # Strategy : Route Input M1 on the same YCoordinates as the SupplyRouting M1
        #            (Supply M1 outside the poly gate route is ignored)
        # '''
        # tmpInputRouting = []  # if list is appended twice, tmp=[ [[1,2],[3,4]], [[5,6],[7,8]] ]
        # if '_VIANMOSPoly2Met1' in self._DesignParameter:
        #     for i in range(0, len(self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'])):
        #         tmpInputRouting.append([self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][i],
        #                                 self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i]])
        # if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
        #     tmpInputRouting.append(self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'])
        #
        # self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        # # self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        # self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        # self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting
        #
        # ################################################################################################################
        # # # Input M1 Route up tp M2
        # if DesignParameters._Technology in ('028nm', '065nm'):
        #     # count input M1 segment
        #     tmpCount_GateViaLayer = 0
        #
        #     if '_VIAMOSPoly2Met1RightMost' in self._DesignParameter:
        #         tmpCount_GateViaLayer += 1
        #         flag_exception_rightmost = True
        #     else:
        #         flag_exception_rightmost = False
        #     if '_VIAPMOSPoly2Met1' in self._DesignParameter:
        #         tmpCount_GateViaLayer += len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])
        #
        #     if (DesignParameters._Technology == '028nm') and (tmpCount_GateViaLayer > 1) and flag_horizontal_inputvia_PCCOM1:
        #         # M1V1M2
        #         # (1) Normal width
        #         _LengthM1_VIAPMOSPoly2Met1 = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        #         _NumViaInputM12 = int((_LengthM1_VIAPMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
        #                               // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        #
        #         _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        #         _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12
        #         _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
        #         self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
        #             _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
        #         self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)
        #
        #         # (2) RightMost
        #         if flag_exception_rightmost:
        #             _LengthM1_VIAPMOSPoly2Met1_RightMost = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        #             _NumViaInputM12_RightMost = int((_LengthM1_VIAPMOSPoly2Met1_RightMost - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
        #                                             // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        #
        #             _ViaMet12Met2forInput2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        #             _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOX'] = _NumViaInputM12_RightMost
        #             _ViaMet12Met2forInput2['_ViaMet12Met2NumberOfCOY'] = 1
        #             self._DesignParameter['_ViaMet12Met2forInput2'] = self._SrefElementDeclaration(
        #                 _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInput2In{}'.format(_Name)))[0]
        #             self._DesignParameter['_ViaMet12Met2forInput2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput2)
        #
        #         tmpXYs = []
        #         for i in range(0, len(self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'])):
        #             tmpXYs.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
        #                            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][i][0],
        #                            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]])
        #         self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs
        #
        #         if flag_exception_rightmost:
        #             self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'] = \
        #                 [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
        #                   self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_XYCoordinates'][0][0],
        #                   self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]]]
        #
        #         self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['METAL2'][0],
        #             _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        #         self._DesignParameter['_CLKMet2InRouting']['_Width'] = self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        #         self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
        #             [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
        #              self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]]
        #         if flag_exception_rightmost:
        #             self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
        #                 [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
        #                  self._DesignParameter['_ViaMet12Met2forInput2']['_XYCoordinates'][0]]]
        #
        #     elif (DesignParameters._Technology in ('028nm', '065nm')) and (tmpCount_GateViaLayer > 1):
        #         # M1V1M2
        #         # (1) Normal width
        #         _LengthM1Y_VIAMOSPoly2Met1 = \
        #         self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
        #         + abs(self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] -
        #               self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1])
        #         _NumViaInputM12 = int((_LengthM1Y_VIAMOSPoly2Met1 - _DRCObj._VIAxMinWidth - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide)
        #                               // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        #
        #         _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        #         _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = 1
        #         _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = _NumViaInputM12 if _NumViaInputM12 < 3 else 3
        #         self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(
        #             _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='ViaMet12Met2forInputIn{}'.format(_Name)))[0]
        #         self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_ViaMet12Met2forInput)
        #
        #         tmpXYs = []
        #         for i in range(0, len(self._DesignParameter['_InputRouting']['_XYCoordinates'])):
        #             tmpXYs.append([self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][0],
        #                            (self._DesignParameter['_InputRouting']['_XYCoordinates'][i][0][1] +
        #                             self._DesignParameter['_InputRouting']['_XYCoordinates'][i][1][1]) / 2])
        #         self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmpXYs
        #
        #         self._DesignParameter['_CLKMet2InRouting'] = self._PathElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        #         # self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._MetalxMinWidth
        #         self._DesignParameter['_CLKMet2InRouting']['_Width'] = _DRCObj._VIAxMinWidth + 2 * _DRCObj._Metal1MinEnclosureVia3
        #         self._DesignParameter['_CLKMet2InRouting']['_XYCoordinates'] = [
        #             # [CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0], [0, -self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')]),
        #             #  CoordCalc.Add(self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1], [0, self.getXWidth('_ViaMet12Met2forInput', '_Met2Layer')])]]
        #             [self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][0],
        #              self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'][-1]]
        #         ]
        #
        # # end of 'if _VDD2VSSHeight == _VDD2VSSMinHeight:'
        #
        # # exception case... Need to Modify later...... Not tested in 65nm
        # if DesignParameters._Technology == '028nm':
        #     _DRC_M1MinWidth_WhenCalcMinArea = 130
        #
        #     if (_Finger == 1) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
        #         tmpX = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
        #             '_XWidth']
        #         tmpY = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
        #             '_YWidth']
        #         if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
        #             tmpY_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpX, MinSnapSpacing)
        #             if tmpY_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
        #                 tmpY_calc = _DRC_M1MinWidth_WhenCalcMinArea
        #
        #             self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                 '_YWidth'] = tmpY_calc
        #
        #     elif (_Finger == 2) and (_VDD2VSSHeight == _VDD2VSSMinHeight):
        #         tmpX = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer'][
        #             '_XWidth']
        #         tmpY = self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer'][
        #             '_YWidth']
        #         if (tmpX * tmpY) < _DRCObj._Metal1MinArea:
        #             tmpX_calc = self.CeilMinSnapSpacing(_DRCObj._Metal1MinArea / tmpY, MinSnapSpacing)
        #             if tmpX_calc < _DRC_M1MinWidth_WhenCalcMinArea:  # Rule by samsung28nm GR501aSE only for 28nm...
        #                 tmpX_calc = _DRC_M1MinWidth_WhenCalcMinArea
        #             self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                 '_XWidth'] = tmpX_calc
        #             self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                 '_XYCoordinates'][0][0] = \
        #                 self._DesignParameter['_VIAMOSPoly2Met1RightMost']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                     '_XYCoordinates'][0][0] \
        #                 + tmpX_calc / 2 - tmpX / 2
        #
        # """ Routing Finished / Next : Additional Layers """
        #
        # ''' ---------------------------------------- PP/NP Additional Layer ---------------------------------------- '''
        # if DesignParameters._Technology != '028nm':
        #     Ybot_PolyRouteXOnPMOS = self._DesignParameter['_PolyRouteXOnPMOS']['_XYCoordinates'][0][1] \
        #                             - 0.5 * self.getYWidth('_PolyRouteXOnPMOS')
        #     Ytop_PolyRouteXOnNMOS = self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][1] \
        #                             + 0.5 * self.getYWidth('_PolyRouteXOnNMOS')
        #
        #     # case 1) Enlarge each PP/NP Layers
        #     if abs(Ybot_PolyRouteXOnPMOS - Ytop_PolyRouteXOnNMOS) >= 2 * _DRCObj._PpMinEnclosureOfPo:
        #         self._DesignParameter['_PIMPforGatePoly'] = self._BoundaryElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['PIMP'][0],
        #             _Datatype=DesignParameters._LayerMapping['PIMP'][1])
        #         self._DesignParameter['_NIMPforGatePoly'] = self._BoundaryElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['NIMP'][0],
        #             _Datatype=DesignParameters._LayerMapping['NIMP'][1])
        #
        #         self._DesignParameter['_PIMPforGatePoly']['_XYCoordinates'] = self.getXY('_PolyRouteXOnPMOS')
        #         self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = self.getXY('_PolyRouteXOnNMOS')
        #         self._DesignParameter['_PIMPforGatePoly']['_XWidth'] = self.getXWidth('_PMOS', '_PPLayer')
        #         self._DesignParameter['_NIMPforGatePoly']['_XWidth'] = self.getXWidth('_NMOS', '_NPLayer')
        #         self._DesignParameter['_PIMPforGatePoly']['_YWidth'] = self.getYWidth('_PolyRouteXOnPMOS') + 2 * _DRCObj._PpMinEnclosureOfPo
        #         self._DesignParameter['_NIMPforGatePoly']['_YWidth'] = self.getYWidth('_PolyRouteXOnNMOS') + 2 * _DRCObj._PpMinEnclosureOfPo
        #
        #     # case 2) Fill the gap between PP&NP Layer with only NP Layer
        #     else:
        #         Ybot_PPLayerOnPMOS = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 0.5 * \
        #                              self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer'][
        #                                  '_YWidth']
        #         Ytop_NPLayerOnNMOS = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 0.5 * \
        #                              self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer'][
        #                                  '_YWidth']
        #
        #         self._DesignParameter['_NIMPforGatePoly'] = self._PathElementDeclaration(
        #             _Layer=DesignParameters._LayerMapping['NIMP'][0],
        #             _Datatype=DesignParameters._LayerMapping['NIMP'][1])
        #         self._DesignParameter['_NIMPforGatePoly']['_Width'] = self.getXWidth('_NMOS', '_NPLayer')
        #         self._DesignParameter['_NIMPforGatePoly']['_XYCoordinates'] = [
        #             [[self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ybot_PPLayerOnPMOS],
        #              [self._DesignParameter['_PolyRouteXOnNMOS']['_XYCoordinates'][0][0], Ytop_NPLayerOnNMOS]]
        #         ]
        # else:
        #     pass
        #
        #
        # ''' ------------------------------------------- NWELL Generation ------------------------------------------- '''
        # '''
        # Function    : Generate NWELL by PathElementDeclaration (column line)
        # Requirement : NbodyContact(ODLayer), _PMOS(ODLayer)
        # '''
        # XWidth1_NWLayer = self.getXWidth('NbodyContact', '_ODLayer') + 2 * _DRCObj._NwMinEnclosurePactive
        # XWidth2_NWLayer = self.getXWidth('_PMOS', '_ODLayer') + 2 * _DRCObj._NwMinEnclosurePactive2
        # XWidth_NWLayer = max(XWidth1_NWLayer, XWidth2_NWLayer)
        #
        # XYCoordinatesOfNW_top = CoordCalc.Add(self._DesignParameter['NbodyContact']['_XYCoordinates'][0],
        #                                       [0, self.getYWidth('NbodyContact', '_ODLayer') / 2 + _DRCObj._NwMinEnclosurePactive])
        # XYCoordinatesOfNW_bot = CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
        #                                       [0, -self.getYWidth('_PMOS', '_ODLayer') / 2 - _DRCObj._NwMinEnclosurePactive])
        # YWidth_NWLayer = abs(XYCoordinatesOfNW_top[1] - XYCoordinatesOfNW_bot[1])
        #
        # if (XWidth_NWLayer * YWidth_NWLayer) < _DRCObj._NwMinArea:
        #     XWidth_NWLayer = self.CeilMinSnapSpacing(_DRCObj._NwMinArea / YWidth_NWLayer, 2 * MinSnapSpacing)
        # else:
        #     pass
        #
        # self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
        # self._DesignParameter['_NWLayer']['_Width'] = XWidth_NWLayer
        # self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[XYCoordinatesOfNW_top, XYCoordinatesOfNW_bot]]
        #
        # ''' ----------------------------------------  XVT Layer Modification --------------------------------------- '''
        # if DesignParameters._Technology == '028nm':
        #     assert _XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
        #     _XVTLayer = '_' + _XVT + 'Layer'
        #
        #     # XVY (over NWELL) Area check
        #     Ymin_NW = XYCoordinatesOfNW_bot[1]
        #     Ymax_XVT = CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
        #                              [0, self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer][
        #                                  '_YWidth'] / 2])[1]
        #     Area_XVToverNW = abs(Ymax_XVT - Ymin_NW) * \
        #                      self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']
        #     if Area_XVToverNW < _DRCObj._XvtMinArea:
        #         XWidth_XVT = self.CeilMinSnapSpacing(_DRCObj._XvtMinArea / abs(Ymax_XVT - Ymin_NW), 2 * MinSnapSpacing)
        #     else:
        #         XWidth_XVT = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']
        #
        #     xy1 = CoordCalc.Add(self._DesignParameter['_PMOS']['_XYCoordinates'][0],
        #                         [0, self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter[_XVTLayer][
        #                             '_YWidth'] / 2])
        #     xy2 = CoordCalc.Add(self._DesignParameter['_NMOS']['_XYCoordinates'][0],
        #                         [0, -self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter[_XVTLayer][
        #                             '_YWidth'] / 2])
        #
        #     self._DesignParameter[_XVTLayer] = self._PathElementDeclaration(
        #         _Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1])
        #     self._DesignParameter[_XVTLayer]['_Width'] = XWidth_XVT
        #     self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[xy1, xy2]]
        #
        # elif DesignParameters._Technology == '065nm':
        #     pass  # No Need to Modify XVT Layer
        # else:
        #     raise NotImplementedError
        #
        # ''' -------------------------------------  Pin Generation & Coordinates ------------------------------------ '''
        # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VSS')
        #
        # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.04, _Angle=0, _TEXT='VDD')
        #
        # self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='A')
        #
        # self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.01, _Angle=0, _TEXT='Y')
        #
        # self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        # self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
        # self._DesignParameter['_Inputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] +
        #             self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2)]
        # ]
        # self._DesignParameter['_Outputpin']['_XYCoordinates'] = [
        #     [round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] +
        #             self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2),
        #      self._DesignParameter['_Inputpin']['_XYCoordinates'][0][1]]
        # ]


        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))


    def _CalculateSupplyRails(self, _NumSupplyCoY, _SupplyMet1YWidth):


        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        # 1) Calculate the Number of Contacts --------------------------------------------------------------------------
        NumCoYOnSupplyRail = _NumSupplyCoY if _NumSupplyCoY != None else 1  # default 1

        NumFinger = len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])
        XWidthOfPMOS = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFinger + 1)

        NumCoXOnSupplyRail_case1 = int(XWidthOfPMOS / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        NumCoXOnSupplyRail_case2 = int(XWidthOfPMOS / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))

        if NumCoYOnSupplyRail == 1:
            NumCoXOnSupplyRail = NumCoXOnSupplyRail_case1
        elif NumCoYOnSupplyRail == 2:
            NumCoXOnSupplyRail = NumCoXOnSupplyRail_case2 if NumCoXOnSupplyRail_case2 >= 3 else 2  # default 2
        else:
            NumCoXOnSupplyRail = NumCoXOnSupplyRail_case2

        # 2) VDD Generation --------------------------------------------------------------------------------------------
        NbodyParameters = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters.update({'_NumberOfNbodyCOX': NumCoXOnSupplyRail,
                                '_NumberOfNbodyCOY': NumCoYOnSupplyRail,
                                '_Met1XWidth': XWidthOfPMOS,
                                '_Met1YWidth': _SupplyMet1YWidth,
                                })

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(
            _DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None, _Name='NbodyContact_In{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)

        # 3) VSS Generation --------------------------------------------------------------------------------------------
        PbodyParameters = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
        PbodyParameters.update({'_NumberOfPbodyCOX': NumCoXOnSupplyRail,
                                '_NumberOfPbodyCOY': NumCoYOnSupplyRail,
                                '_Met1XWidth': XWidthOfPMOS,
                                '_Met1YWidth': _SupplyMet1YWidth
                                })

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(
            _DesignObj=PbodyContact_iksu._PbodyContact(_DesignParameter=None, _Name='PbodyContact_In{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**PbodyParameters)



if __name__ == '__main__':
    from Private import MyInfo
    from SthPack import PlaygroundBot
    import DRCchecker

    libname = 'INV_STD'
    cellname = 'INV_STD'
    _fileName = cellname + '.gds'


    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _Finger=5,
        _ChannelWidth=200,
        _ChannelLength=30,
        _NPRatio=2,
        _Dummy=True,                    # True / False
        _XVT='LVT',                    # @ 028nm, 'SLVT' 'LVT' 'RVT' 'HVT' / @ 065nm, 'LVT' 'HVT' or None
        _DistanceBtwFinger=130,        # default(None) MinimumValue by DRC | onesemicon:150

        _VDD2VSSHeight=1800,           # 1800
        _VDD2PMOSHeight=500,           # 500  |  599
        _VSS2NMOSHeight=300,           # 300  |  461

    )

    Mode_DRCCheck = False            # True | False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
            InputParams['_Finger'] = DRCchecker.RandomParam(start=2, stop=20, step=1)               # DRCchecker.RandomParam(start=2, stop=20, step=1)
            InputParams['_ChannelWidth'] = DRCchecker.RandomParam(start=400, stop=1000, step=2)     # DRCchecker.RandomParam(start=200, stop=1000, step=2)
            InputParams['_ChannelLength'] = DRCchecker.RandomParam(start=10, stop=20, step=2)
        else:
            pass

        ''' Generate Inverter Layout Object '''
        LayoutObj = _Inverter(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)

        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('###############      Sending to FTP Server...      ##################')
        My = MyInfo.USER(DesignParameters._Technology)
        Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)
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
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number Of Trial : {Num_DRCCheck}')
                    # elapsed time, start time, end time, main python file name
                else:
                    pass
            # Checker.DRCchecker_PrintInputParams(InputParams)
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print('#############################      Finished      ################################')

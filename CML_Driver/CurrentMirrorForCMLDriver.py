import copy
import time
#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from SthPack import BoundaryCalc, CoordCalc
from SthPack import PlaygroundBot
from Private import MyInfo

#
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import psubring
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu


class CurrentMirror(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
        FingerWidthOfNMOS=None,
        FingerLengthOfNMOS=None,
        NumFingerOfNMOS1=None,
        NumFingerOfNMOS2=None,
        XVTOfNMOS=None,
        NumViaPoly2Met1CoYNMOS=None,
        YWidthOfViaPoly2Met1NMOS=None,



        FingerWidthOfPMOS=None,
        FingerLengthOfPMOS=None,
        NumFingerOfPMOS=None,
        XVTOfPMOS=None,

        NumViaPoly2Met1CoYPMOS=None,
        YWidthOfViaPoly2Met1PMOS=None,

        DummyOfMOS=None,
        SubringWidth=None
    )


    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                POHForPMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1HForPMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M2HForPMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                POVForPMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1VForPMOSDrainGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                     _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                     _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1VForPMOSSupply=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                  _XYCoordinates=[], _XWidth=400, _YWidth=400),


                POHForNMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1HForNMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M2HForNMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                POVForNMOSGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1VForNMOSDrainGate=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                     _Datatype=DesignParameters._LayerMapping['METAL1'][
                                                                         1],
                                                                     _XYCoordinates=[], _XWidth=400, _YWidth=400),
                M1VForNMOSSupply=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                  _XYCoordinates=[], _XWidth=400, _YWidth=400),

                M3HForNMOSD2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                              _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400),

                Met1BoundaryOfPMOSSubring=dict(_DesignParametertype=7, _XWidth=None, _YWidth=None, _XYCoordinates=[]),
                Met1BoundaryOfNMOSSubring=dict(_DesignParametertype=7, _XWidth=None, _YWidth=None, _XYCoordinates=[]),




                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    def _CalculateDesignParameter(self, FingerWidthOfNMOS=None,
                                  FingerLengthOfNMOS=None,
                                  NumFingerOfNMOS1=None,
                                  NumFingerOfNMOS2=None,
                                  XVTOfNMOS=None,
                                  NumViaPoly2Met1CoYNMOS=None,
                                  YWidthOfViaPoly2Met1NMOS=None,

                                  FingerWidthOfPMOS=None,
                                  FingerLengthOfPMOS=None,
                                  NumFingerOfPMOS=None,
                                  XVTOfPMOS=None,
                                  NumViaPoly2Met1CoYPMOS=None,
                                  YWidthOfViaPoly2Met1PMOS=None,

                                  DummyOfMOS=None,
                                  SubringWidth=None
                                  ):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        self._CalculateDesignParameterNMOS(
            FingerWidthOfNMOS=FingerWidthOfNMOS,
            FingerLengthOfNMOS=FingerLengthOfNMOS,
            NumFingerOfNMOS1=NumFingerOfNMOS1,
            NumFingerOfNMOS2=NumFingerOfNMOS2,
            XVTOfNMOS=XVTOfNMOS,
            NumViaPoly2Met1CoYNMOS=NumViaPoly2Met1CoYNMOS,
            YWidthOfViaPoly2Met1NMOS=YWidthOfViaPoly2Met1NMOS,
            DummyOfMOS=DummyOfMOS,
            SubringWidth=SubringWidth)


        self._CalculateDesignParameterPMOS(
            FingerWidthOfPMOS=FingerWidthOfPMOS,
            FingerLengthOfPMOS=FingerLengthOfPMOS,
            NumFingerOfPMOS=NumFingerOfPMOS,
            XVTOfPMOS=XVTOfPMOS,
            NumViaPoly2Met1CoYPMOS=NumViaPoly2Met1CoYPMOS,
            YWidthOfViaPoly2Met1PMOS=YWidthOfViaPoly2Met1PMOS,
            DummyOfMOS=DummyOfMOS,
            SubringWidth=SubringWidth)


        upperYOfNMOSSubringM1 = abs(self.getXY('Met1BoundaryOfNMOSSubring')[0][1] + self.getYWidth('Met1BoundaryOfNMOSSubring') / 2)
        lowerYOfPMOSSubringM1 = abs(self.getXY('Met1BoundaryOfPMOSSubring')[0][1] - self.getYWidth('Met1BoundaryOfPMOSSubring') / 2)

        OffsetYOfPMOS = upperYOfNMOSSubringM1 + _DRCObj._Metal1MinSpace4 + lowerYOfPMOSSubringM1
        ObjListRelatedPMOS = ['PMOS', 'ViaPoly2Met1ForPMOSGate', '_Via1ForPMOSGate', 'SubringForPMOS', 'POHForPMOSGate',
                              'M1HForPMOSGate', 'M2HForPMOSGate', 'POVForPMOSGate', 'M1VForPMOSDrainGate', 'M1VForPMOSSupply']
        for DesignObj in ObjListRelatedPMOS:
            self.YShiftUp(DesignObj, OffsetYOfPMOS)


        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#') + '\n')




    def YShiftUp(self, DesignObj, OffsetY):
        tmpXYs = []
        for XY in self._DesignParameter[DesignObj]['_XYCoordinates']:
            tmpXYs.append(CoordCalc.Add(XY, [0, OffsetY]))
        self._DesignParameter[DesignObj]['_XYCoordinates'] = tmpXYs


    def _CalculateDesignParameterPMOS(self, FingerWidthOfPMOS=None, FingerLengthOfPMOS=None, NumFingerOfPMOS=None,
                                      XVTOfPMOS=None, NumViaPoly2Met1CoYPMOS=None, YWidthOfViaPoly2Met1PMOS=None,
                                      DummyOfMOS=None, SubringWidth=None):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        ''' MOSFET Calculation '''
        PMOSparams = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
        PMOSparams['_PMOSNumberofGate'] = NumFingerOfPMOS
        PMOSparams['_PMOSChannelWidth'] = FingerWidthOfPMOS
        PMOSparams['_PMOSChannellength'] = FingerLengthOfPMOS
        PMOSparams['_PMOSDummy'] = DummyOfMOS
        PMOSparams['_XVT'] = XVTOfPMOS

        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(
            _DesignObj=PMOSWithDummy_iksu._PMOS(_DesignParameter=None, _Name='PMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparams)
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, 0]]


        ''' Poly-Met1-Met2 PMOS Gate  '''
        # YWidth is calculated by two input parameters (YWidthOfViaPoly2Met1PMOS, NumViaPoly2Met1CoYPMOS)
        # calculated as the longest of the two cases.
        # If all input parameters are None, YWidth is calculated as CoY=1

        YWidthOfPMOSPolyGate_1 = YWidthOfViaPoly2Met1PMOS if YWidthOfViaPoly2Met1PMOS != None else 0
        _NumViaPoly2Met1CoYPMOS = NumViaPoly2Met1CoYPMOS if NumViaPoly2Met1CoYPMOS != None else 1
        YWidthOfPMOSPolyGate_2 = (_NumViaPoly2Met1CoYPMOS - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) \
                                 + _DRCObj._CoMinWidth \
                                 + 2 * max(_DRCObj._Metal1MinEnclosureCO2, _DRCObj._CoMinEnclosureByPOAtLeastTwoSide)

        YWidthOfPMOSPolyGate = self.CeilMinSnapSpacing(max(YWidthOfPMOSPolyGate_1, YWidthOfPMOSPolyGate_2), 2 * MinSnapSpacing)
        XWidthOfPMOSPolyGate = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfPMOS - 1) + FingerLengthOfPMOS

        DistanceBtwPMOS2PolyGate = 0.5 * (self.getYWidth('PMOS','_Met1Layer') + YWidthOfPMOSPolyGate) \
                                   + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)          # @ 28nm, SpaceAtCorner. @ other tech, MinSpace (Need2Check)

        self._DesignParameter['POHForPMOSGate']['_XWidth'] = XWidthOfPMOSPolyGate
        self._DesignParameter['POHForPMOSGate']['_YWidth'] = YWidthOfPMOSPolyGate
        self._DesignParameter['POHForPMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwPMOS2PolyGate]]

        self._DesignParameter['M1HForPMOSGate']['_XWidth'] = XWidthOfPMOSPolyGate
        self._DesignParameter['M1HForPMOSGate']['_YWidth'] = YWidthOfPMOSPolyGate
        self._DesignParameter['M1HForPMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwPMOS2PolyGate]]

        self._DesignParameter['M2HForPMOSGate']['_XWidth'] = XWidthOfPMOSPolyGate
        self._DesignParameter['M2HForPMOSGate']['_YWidth'] = YWidthOfPMOSPolyGate
        self._DesignParameter['M2HForPMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwPMOS2PolyGate]]

        ''' Vias '''
        NumViaXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=XWidthOfPMOSPolyGate, _YWidth=YWidthOfPMOSPolyGate)
        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['ViaPoly2Met1ForPMOSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1ForPMOSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['ViaPoly2Met1ForPMOSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        self._DesignParameter['ViaPoly2Met1ForPMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwPMOS2PolyGate]]

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=XWidthOfPMOSPolyGate, _YWidth=YWidthOfPMOSPolyGate)
        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['_Via1ForPMOSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPMOSGate_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['_Via1ForPMOSGate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**Via1Params)
        self._DesignParameter['_Via1ForPMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwPMOS2PolyGate]]


        ''' POV For PMOS Gate '''
        upperYCoordOfPOV = 0
        lowerYCoordOfPOV = self.getXY('POHForPMOSGate')[0][1] - self.getYWidth('POHForPMOSGate') / 2

        self._DesignParameter['POVForPMOSGate']['_XWidth'] = self.getXWidth('PMOS','_POLayer')
        self._DesignParameter['POVForPMOSGate']['_YWidth'] = upperYCoordOfPOV - lowerYCoordOfPOV
        tmpXYs = []
        for XY in self.getXY('PMOS', '_POLayer'):
            tmpXYs.append([XY[0], self.CeilMinSnapSpacing((upperYCoordOfPOV + lowerYCoordOfPOV) / 2, MinSnapSpacing)])
        self._DesignParameter['POVForPMOSGate']['_XYCoordinates'] = tmpXYs

        ''' PMOS Drain - Gate Connect '''
        upperYOfM1V_PMOSDrain2Gate = 0
        lowerYOfM1V_PMOSDrain2Gate = self.getXY('M1HForPMOSGate')[0][1] - self.getYWidth('M1HForPMOSGate') / 2

        self._DesignParameter['M1VForPMOSDrainGate']['_XWidth'] = self.getXWidth('PMOS', '_Met1Layer')
        self._DesignParameter['M1VForPMOSDrainGate']['_YWidth'] = upperYOfM1V_PMOSDrain2Gate - lowerYOfM1V_PMOSDrain2Gate
        tmpXYs = []
        for XY in self.getXY('PMOS', '_XYCoordinatePMOSOutputRouting'):
            tmpXYs.append([XY[0], self.CeilMinSnapSpacing((upperYOfM1V_PMOSDrain2Gate + lowerYOfM1V_PMOSDrain2Gate) / 2, MinSnapSpacing)])
        self._DesignParameter['M1VForPMOSDrainGate']['_XYCoordinates'] = tmpXYs


        ''' Subring '''
        _DRCtemp_metal1minspace = 210  # GR504C2 (173) GR504d(210)

        XWidthOfSubring1_ODtoOD = self.getXWidth('PMOS','_ODLayer') + 2 * _DRCObj._OdMinSpace
        XWidthOfSubring2_PolytoOD = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfPMOS + 1) \
                                    + FingerLengthOfPMOS + 2 * _DRCObj._PolygateMinSpace2OD
        XWidthOfSubring3_Met1toMet1 = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfPMOS \
                                      + self.getXWidth('PMOS','_Met1Layer') + 2 * _DRCtemp_metal1minspace
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring2_PolytoOD, XWidthOfSubring3_Met1toMet1)

        # YWidth Of Subring - by Met1 spacing
        YdownwardOfSubring = self.FloorMinSnapSpacing(self.getXY('M1HForPMOSGate')[0][1] - self.getYWidth('M1HForPMOSGate') / 2 - _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YupwardOfSubring = self.CeilMinSnapSpacing(self.getXY('PMOS', '_Met1Layer')[0][1] + self.getYWidth('PMOS', '_Met1Layer') / 2 + _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YWidthOfSubring = YupwardOfSubring - YdownwardOfSubring
        YcenterOfSubring = (YupwardOfSubring + YdownwardOfSubring) / 2.0

        PSubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PSubringInputs['_PType'] = False
        PSubringInputs['_XWidth'] = XWidthOfSubring
        PSubringInputs['_YWidth'] = YWidthOfSubring
        PSubringInputs['_Width'] = SubringWidth
        self._DesignParameter['SubringForPMOS'] = self._SrefElementDeclaration(
            _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='SubringForPMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['SubringForPMOS']['_DesignObj']._CalculatePSubring(**PSubringInputs)
        self._DesignParameter['SubringForPMOS']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['Met1BoundaryOfPMOSSubring']['_XWidth'] = XWidthOfSubring + 2 * SubringWidth
        self._DesignParameter['Met1BoundaryOfPMOSSubring']['_YWidth'] = YWidthOfSubring + 2 * SubringWidth
        self._DesignParameter['Met1BoundaryOfPMOSSubring']['_XYCoordinates'] = [[0, YcenterOfSubring]]



        ''' SupplyRouting '''
        tmpXYs = []
        for XY in self.getXY('PMOS', '_XYCoordinatePMOSSupplyRouting'):
            tmpXYs.append([XY[0], YupwardOfSubring/2])
        self._DesignParameter['M1VForPMOSSupply']['_XWidth'] = self.getXWidth('PMOS', '_Met1Layer')
        self._DesignParameter['M1VForPMOSSupply']['_YWidth'] = YupwardOfSubring - 0
        self._DesignParameter['M1VForPMOSSupply']['_XYCoordinates'] = tmpXYs




    def _CalculateDesignParameterNMOS(self, FingerWidthOfNMOS=None, FingerLengthOfNMOS=None, NumFingerOfNMOS1=None,
                                      NumFingerOfNMOS2=None,
                                      XVTOfNMOS=None, NumViaPoly2Met1CoYNMOS=None, YWidthOfViaPoly2Met1NMOS=None,
                                      DummyOfMOS=None, SubringWidth=None):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        ''' MOSFET Calculation '''
        NumFingerOfNMOS = NumFingerOfNMOS1 + NumFingerOfNMOS2

        NMOSparams = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        NMOSparams['_NMOSNumberofGate'] = NumFingerOfNMOS
        NMOSparams['_NMOSChannelWidth'] = FingerWidthOfNMOS
        NMOSparams['_NMOSChannellength'] = FingerLengthOfNMOS
        NMOSparams['_NMOSDummy'] = DummyOfMOS
        NMOSparams['_XVT'] = XVTOfNMOS

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(
            _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparams)
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, 0]]


        ''' Poly-Met1-Met2 NMOS Gate  '''
        # YWidth is calculated by two input parameters (YWidthOfViaPoly2Met1NMOS, NumViaPoly2Met1CoYNMOS)
        # calculated as the longest of the two cases.
        # If all input parameters are None, YWidth is calculated as CoY=1

        YWidthOfNMOSPolyGate_1 = YWidthOfViaPoly2Met1NMOS if YWidthOfViaPoly2Met1NMOS != None else 0
        _NumViaPoly2Met1CoYNMOS = NumViaPoly2Met1CoYNMOS if NumViaPoly2Met1CoYNMOS != None else 1
        YWidthOfNMOSPolyGate_2 = (_NumViaPoly2Met1CoYNMOS - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) \
                                 + _DRCObj._CoMinWidth \
                                 + 2 * max(_DRCObj._Metal1MinEnclosureCO2, _DRCObj._CoMinEnclosureByPOAtLeastTwoSide)

        YWidthOfNMOSPolyGate = self.CeilMinSnapSpacing(max(YWidthOfNMOSPolyGate_1, YWidthOfNMOSPolyGate_2), 2 * MinSnapSpacing)
        XWidthOfNMOSPolyGate = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfNMOS - 1) + FingerLengthOfNMOS

        DistanceBtwNMOS2PolyGate = 0.5 * (self.getYWidth('NMOS','_Met1Layer') + YWidthOfNMOSPolyGate) \
                                   + max(_DRCObj._Metal1MinSpaceAtCorner, _DRCObj._Metal1MinSpace, _DRCObj._Metal1MinSpace2)          # @ 28nm, SpaceAtCorner. @ other tech, MinSpace (Need2Check)

        self._DesignParameter['POHForNMOSGate']['_XWidth'] = XWidthOfNMOSPolyGate
        self._DesignParameter['POHForNMOSGate']['_YWidth'] = YWidthOfNMOSPolyGate
        self._DesignParameter['POHForNMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwNMOS2PolyGate]]

        self._DesignParameter['M1HForNMOSGate']['_XWidth'] = XWidthOfNMOSPolyGate
        self._DesignParameter['M1HForNMOSGate']['_YWidth'] = YWidthOfNMOSPolyGate
        self._DesignParameter['M1HForNMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwNMOS2PolyGate]]

        self._DesignParameter['M2HForNMOSGate']['_XWidth'] = XWidthOfNMOSPolyGate
        self._DesignParameter['M2HForNMOSGate']['_YWidth'] = YWidthOfNMOSPolyGate
        self._DesignParameter['M2HForNMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwNMOS2PolyGate]]

        ''' Vias '''
        NumViaXY = ViaPoly2Met1._ViaPoly2Met1.CalculateNumContact(
            _XWidth=XWidthOfNMOSPolyGate, _YWidth=YWidthOfNMOSPolyGate)
        ViaParams = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        ViaParams['_ViaPoly2Met1NumberOfCOX'] = NumViaXY[0]
        ViaParams['_ViaPoly2Met1NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['ViaPoly2Met1ForNMOSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1ForNMOSGate_In{}'.format(_Name)))[0]
        self._DesignParameter['ViaPoly2Met1ForNMOSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**ViaParams)
        self._DesignParameter['ViaPoly2Met1ForNMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwNMOS2PolyGate]]

        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaSameEnclosure(
            _XWidth=XWidthOfNMOSPolyGate, _YWidth=YWidthOfNMOSPolyGate)
        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['_Via1ForNMOSGate'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForNMOSGate_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['_Via1ForNMOSGate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**Via1Params)
        self._DesignParameter['_Via1ForNMOSGate']['_XYCoordinates'] = [[0, -DistanceBtwNMOS2PolyGate]]


        ''' POV For NMOS Gate '''
        upperYCoordOfPOV = 0
        lowerYCoordOfPOV = self.getXY('POHForNMOSGate')[0][1] - self.getYWidth('POHForNMOSGate') / 2

        self._DesignParameter['POVForNMOSGate']['_XWidth'] = self.getXWidth('NMOS','_POLayer')
        self._DesignParameter['POVForNMOSGate']['_YWidth'] = upperYCoordOfPOV - lowerYCoordOfPOV
        tmpXYs = []
        for XY in self.getXY('NMOS', '_POLayer'):
            tmpXYs.append([XY[0], self.CeilMinSnapSpacing((upperYCoordOfPOV + lowerYCoordOfPOV) / 2, MinSnapSpacing)])
        self._DesignParameter['POVForNMOSGate']['_XYCoordinates'] = tmpXYs


        ''' Subring '''
        _DRCtemp_metal1minspace = 210

        XWidthOfSubring1_ODtoOD = self.getXWidth('NMOS','_ODLayer') + 2 * _DRCObj._OdMinSpace
        XWidthOfSubring2_PolytoOD = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * (NumFingerOfNMOS + 1) \
                                    + FingerLengthOfNMOS + 2 * _DRCObj._PolygateMinSpace2OD
        XWidthOfSubring3_Met1toMet1 = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] * NumFingerOfNMOS \
                                      + self.getXWidth('NMOS','_Met1Layer') + 2 * _DRCtemp_metal1minspace
        XWidthOfSubring = max(XWidthOfSubring1_ODtoOD, XWidthOfSubring2_PolytoOD, XWidthOfSubring3_Met1toMet1)

        # YWidth Of Subring - by Met1 spacing
        YdownwardOfSubring = self.FloorMinSnapSpacing(self.getXY('M1HForNMOSGate')[0][1] - self.getYWidth('M1HForNMOSGate') / 2 - _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YupwardOfSubring = self.CeilMinSnapSpacing(self.getXY('NMOS', '_Met1Layer')[0][1] + self.getYWidth('NMOS', '_Met1Layer') / 2 + _DRCtemp_metal1minspace, 2*MinSnapSpacing)
        YWidthOfSubring = YupwardOfSubring - YdownwardOfSubring
        YcenterOfSubring = (YupwardOfSubring + YdownwardOfSubring) / 2.0

        PSubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PSubringInputs['_PType'] = True
        PSubringInputs['_XWidth'] = XWidthOfSubring
        PSubringInputs['_YWidth'] = YWidthOfSubring
        PSubringInputs['_Width'] = SubringWidth
        self._DesignParameter['SubringForNMOS'] = self._SrefElementDeclaration(
            _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='SubringForNMOS_In{}'.format(_Name)))[0]
        self._DesignParameter['SubringForNMOS']['_DesignObj']._CalculatePSubring(**PSubringInputs)
        self._DesignParameter['SubringForNMOS']['_XYCoordinates'] = [[0, YcenterOfSubring]]

        self._DesignParameter['Met1BoundaryOfNMOSSubring']['_XWidth'] = XWidthOfSubring + 2 * SubringWidth
        self._DesignParameter['Met1BoundaryOfNMOSSubring']['_YWidth'] = YWidthOfSubring + 2 * SubringWidth
        self._DesignParameter['Met1BoundaryOfNMOSSubring']['_XYCoordinates'] = [[0, YcenterOfSubring]]



        ''' SupplyRouting '''
        self._DesignParameter['text_S_NMOS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='S', _XYCoordinates=[])

        tmpXYs = []
        for XY in self.getXY('NMOS', '_XYCoordinateNMOSSupplyRouting'):
            tmpXYs.append([XY[0], YupwardOfSubring/2])
        self._DesignParameter['M1VForNMOSSupply']['_XWidth'] = self.getXWidth('NMOS', '_Met1Layer')
        self._DesignParameter['M1VForNMOSSupply']['_YWidth'] = (YupwardOfSubring - 0)
        self._DesignParameter['M1VForNMOSSupply']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['text_S_NMOS']['_XYCoordinates'] = tmpXYs


        ''' OutputRouting '''
        flag_even_finger1 = True if (NumFingerOfNMOS1 % 2 == 0) else False
        flag_even_finger2 = True if (NumFingerOfNMOS2 % 2 == 0) else False

        tmpXYs_D1, tmpXYs_D2 = [], []
        for i, X in enumerate(CoordCalc.getSortedList_ascending(self.getXY('NMOS', '_XYCoordinateNMOSOutputRouting'))[0]):
            if flag_even_finger1:               # if even finger, left side.
                if i < NumFingerOfNMOS1:
                    tmpXYs_D1.append([X,0])
                else:
                    tmpXYs_D2.append([X,0])
            else:
                if i < NumFingerOfNMOS2:
                    tmpXYs_D2.append([X,0])
                else:
                    tmpXYs_D1.append([X,0])
        self._DesignParameter['text_D1_NMOS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='D1', _XYCoordinates=tmpXYs_D1)
        self._DesignParameter['text_D2_NMOS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['text'][0], _Datatype=DesignParameters._LayerMapping['text'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT='D2', _XYCoordinates=tmpXYs_D2)


        ''' NMOS Drain - Gate Connect '''
        upperYOfM1V_NMOSDrain2Gate = 0
        lowerYOfM1V_NMOSDrain2Gate = self.getXY('M1HForNMOSGate')[0][1] - self.getYWidth('M1HForNMOSGate') / 2

        self._DesignParameter['M1VForNMOSDrainGate']['_XWidth'] = self.getXWidth('NMOS', '_Met1Layer')
        self._DesignParameter['M1VForNMOSDrainGate']['_YWidth'] = upperYOfM1V_NMOSDrain2Gate - lowerYOfM1V_NMOSDrain2Gate
        tmpXYs = []
        for XY in tmpXYs_D1:
            tmpXYs.append([XY[0], self.CeilMinSnapSpacing((upperYOfM1V_NMOSDrain2Gate + lowerYOfM1V_NMOSDrain2Gate) / 2, MinSnapSpacing)])
        self._DesignParameter['M1VForNMOSDrainGate']['_XYCoordinates'] = tmpXYs


        ''' M1V1M2 '''
        NumViaXY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureX(
            _XWidth=self.getXWidth('NMOS','_Met1Layer'),
            _YWidth=self.getYWidth('NMOS','_Met1Layer')
        )
        assert NumViaXY[1] >= 2, 'FingerWidth should be longer.'

        Via1Params = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Params['_ViaMet12Met2NumberOfCOX'] = NumViaXY[0]
        Via1Params['_ViaMet12Met2NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['Via1ForNMOSD2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForNMOSD2_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['Via1ForNMOSD2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**Via1Params)
        self._DesignParameter['Via1ForNMOSD2']['_XYCoordinates'] = tmpXYs_D2

        ''' M2V2M3 '''
        Via2Params = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        Via2Params['_ViaMet22Met3NumberOfCOX'] = NumViaXY[0]
        Via2Params['_ViaMet22Met3NumberOfCOY'] = NumViaXY[1]
        self._DesignParameter['Via2ForNMOSD2'] = self._SrefElementDeclaration(
            _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForNMOSD2_In{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['Via2ForNMOSD2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**Via2Params)
        self._DesignParameter['Via2ForNMOSD2']['_XYCoordinates'] = tmpXYs_D2

        ''' M3H For D2 '''
        XLeftOfV2 = CoordCalc.getSortedList_ascending(self.getXY('Via2ForNMOSD2'))[0][0]
        XRightOfV2 = CoordCalc.getSortedList_ascending(self.getXY('Via2ForNMOSD2'))[0][-1]
        self._DesignParameter['M3HForNMOSD2']['_XWidth'] = XRightOfV2 - XLeftOfV2 + self.getXWidth('Via2ForNMOSD2', '_Met3Layer')
        self._DesignParameter['M3HForNMOSD2']['_YWidth'] = self.getYWidth('Via2ForNMOSD2', '_Met3Layer') / 2
        self._DesignParameter['M3HForNMOSD2']['_XYCoordinates'] = [[(XLeftOfV2 + XRightOfV2) / 2, 0]]



if __name__ == '__main__':

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_CurrentMirror'
    cellname = 'CurrentMirror'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        FingerWidthOfNMOS=800,
        FingerLengthOfNMOS=30,
        NumFingerOfNMOS1=10,
        NumFingerOfNMOS2=20,
        XVTOfNMOS='SLVT',
        NumViaPoly2Met1CoYNMOS=3,
        YWidthOfViaPoly2Met1NMOS=None,

        FingerWidthOfPMOS=800,
        FingerLengthOfPMOS=30,
        NumFingerOfPMOS=50,
        XVTOfPMOS='SLVT',
        NumViaPoly2Met1CoYPMOS=3,
        YWidthOfViaPoly2Met1PMOS=None,

        DummyOfMOS=True,
        SubringWidth=1000
    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10
    start_time = time.time()

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass

        print("   Layout Object's Input Parameters are   ".center(105, '='))
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("".center(105, '='))

        ''' Generate Layout Object '''
        LayoutObj = CurrentMirror(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

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
            print(f'DRC checking... ({ii + 1}/{Num_DRCCheck})')

            try:
                Checker.DRCchecker()
            except Exception as e:
                print('Error Occurred: ', e)
                print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                print(tmpStr)
                print(''.center(105, '='))
                m, s = divmod(time.time() - start_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\nErrMsg : {e}\n'
                             f'**InputParameters:\n'
                             f'{tmpStr}\n'
                             f'****************************'
                             f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
            else:
                if (ii + 1) == Num_DRCCheck:
                    elapsed_time = time.time() - start_time
                    m, s = divmod(elapsed_time, 60)
                    h, m = divmod(m, 60)
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number of Run: {Num_DRCCheck}\n'
                                 f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
                else:
                    pass
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

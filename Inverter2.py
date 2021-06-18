import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3

class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(_Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None,_VDD2VSSHeight=None)


    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateDesignParameter(self, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None, _VDD2VSSHeight = None, _Dummy = False,
                                     _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None,
                                    _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
                                ):

            _DRCObj = DRC.DRC()

            _Name = 'Inverter'



            # NMOS Generation
            _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
            _NMOSinputs['_NMOSNumberofGate'] = _Finger
            _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
            _NMOSinputs['_NMOSChannellength'] = _ChannelLength
            _NMOSinputs['_NMOSDummy'] = _Dummy

            self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

            # PMOS Generation
            _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
            _PMOSinputs['_PMOSNumberofGate'] = _Finger
            _PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
            _PMOSinputs['_PMOSChannellength'] = _ChannelLength
            _PMOSinputs['_PMOSDummy'] = _Dummy

            self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

            # VDD Generation

            _ContactNum = ( self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
            if _ContactNum < 2:     # default number of contact column : 2
                _ContactNum = 2

            if _NumSupplyCOY is None:
                _NumSupplyCOY = 1  # default number of contact row : 1

            _Pbodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
            _Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
            _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCOY

            _tmpPbodyObj = PbodyContact._PbodyContact()
            _tmpPbodyObj._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOX=7,
                                                               _NumberOfPbodyCOY=_Pbodyinputs['_NumberOfPbodyCOY'],
                                                               _Met1YWidth=_SupplyMet1YWidth)
            _tmpPbodyObj._DesignParameter['_XYCoordinates'] = [[0, 0]]

            _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
            _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

            self._DesignParameter['_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0]
            self._DesignParameter['_PbodyContact']['_XYCoordinates'] = _tmpPbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)



            # VSS Generation
            _Nbodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
            _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum

            _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCOY

            _tmpNbodyObj = NbodyContact._NbodyContact()
            _tmpNbodyObj._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOX=7,
                                                               _NumberOfNbodyCOY=_Nbodyinputs['_NumberOfNbodyCOY'],
                                                               _Met1YWidth=_SupplyMet1YWidth)
            ############################## VDD2VSS Height Minimum value calculation ####################################

            _VDD2VSSminHeight = (_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth'] / 2) + (
                        _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth'] / 2) \
                                + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] \
                                + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _DRCObj._PolygateMinSpace2

            if _VDD2VSSHeight == None:
                _VDD2VSSHeight = _VDD2VSSminHeight

            else:
                if _VDD2VSSHeight < _VDD2VSSminHeight:
                    raise NotImplementedError

            ############################################################################################################

            _tmpNbodyObj._DesignParameter['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

            _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
            _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

            self._DesignParameter['_NbodyContact']= self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0]
            self._DesignParameter['_NbodyContact']['_XYCoordinates'] = _tmpNbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)

            # VIA Generation for PMOS Output
            _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2

            _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = 2

            self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)




            # VIA Generation for NMOS Output

            _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2

            _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = 2


            self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)

            # VIA Generation for PMOS Gate

            _LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

            _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwPMOSGates // (float)(_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1

            if _tmpNumCOX < 2:
                _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 2
            else:
                _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX

            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIAPMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)

            del _tmpNumCOX

            # VIA Generation for NMOS Gate

            _LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

            _VIANMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _tmpNumCOX = int(_LenBtwNMOSGates // (float)(_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
            if _tmpNumCOX < 2:
                _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 2
            else:
                _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX

            _VIANMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

            self._DesignParameter['_VIANMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOSPoly2Met1)

            del _tmpNumCOX


            # Coordinate Settings

            _tmpPbodyObj._DesignParameter['_XYCoordinates'] = [[0, 0]]
            _tmpNbodyObj._DesignParameter['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

            self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] * 1 / 2
                                                                 + _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']*1 / 2)]]
            self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, (float)(_VDD2VSSHeight - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] * 1 / 2
                                                                 - _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth'] * 1 / 2)]]

            tmp9 = []
            tmp10 = []
            for i in range(0,len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):

                tmp9.append([x+y for x, y in zip(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i]
                                                                                                        , self._DesignParameter['_NMOS']['_XYCoordinates'][0])])
                tmp10.append([x+y for x, y in zip(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i]
                                                                                                        , self._DesignParameter['_PMOS']['_XYCoordinates'][0])])
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmp9
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmp10

            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates']
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates']

            self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + \
                                                                           self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+ \
                                                                           self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+ \
                                                                           _DRCObj._Metal1MinSpace]]

            self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - \
                                                                           self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2- \
                                                                           self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - \
                                                                           _DRCObj._Metal1MinSpace]]

            # VSS Met1 Routing
            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tempX = \
                self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0]
                tmp.append([[tempX, 0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth'] / 2], [a + b for a, b in
                    zip(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i],
                        self._DesignParameter['_NMOS']['_XYCoordinates'][0])]])

            self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)

            self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmp
            self._DesignParameter['_NMOSSupplyRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            # VDD Met1 Routing
            tmp1 = []
            for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tempX1 = \
                self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0]
                tmp1.append([[tempX1,_VDD2VSSHeight + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth'] / 2], [a + b for a, b in
                    zip(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i],
                        self._DesignParameter['_PMOS']['_XYCoordinates'][0])]])

            self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)

            self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmp1
            self._DesignParameter['_PMOSSupplyRouting']['_Width'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']



            # Input Routing
            tmp2 = []
            tmp2.append([self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0], self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0]])

            self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=400)

            self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmp2
            self._DesignParameter['_InputRouting']['_Width'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']


            # Connection Routing

            tmp11 = []
            for i in range(0, len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tempX3 = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0]

                tmp11.append([tempX3, self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]
                              + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]])

            self._DesignParameter['_NMOSOutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_NMOSOutputRouting']['_XYCoordinates'] = [tmp11]
            self._DesignParameter['_NMOSOutputRouting']['_Width'] = self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']

            tmp8 = []
            for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tempX2 = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0]

                tmp8.append([tempX2, self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]
                              + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]])

            self._DesignParameter['_PMOSOutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_PMOSOutputRouting']['_XYCoordinates'] = [tmp8]
            self._DesignParameter['_PMOSOutputRouting']['_Width'] = self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']

            # Output Routing

            tmp3 = []

            tmp3.append([self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0], self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0]])

            self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400)

            self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmp3
            self._DesignParameter['_OutputRouting']['_Width'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

            # Additional Metal1 Layer Generation

            self._DesignParameter['_AdditionalMet1OnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalMet1OnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400)

            tmp4 = []
            for i in range(0,len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'])):
                tmp4.append([[self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],
                          self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]- self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2],
                          [self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],
                          self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]+ self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]])

            tmp5 = []
            if self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] >= (_DRCObj._Metal1MinArea) / (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']):
                for i in range(0, len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'])):
                    tmp5.append([[self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2],
                        [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2]])
            else :
                for i in range(0, len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'])):
                    tmp5.append([[self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-\
                                 ((_DRCObj._Metal1MinArea) // (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']))],
                        [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],
                        self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2]])

            self._DesignParameter['_AdditionalMet1OnNMOS']['_XYCoordinates'] = tmp5
            self._DesignParameter['_AdditionalMet1OnNMOS']['_Width'] = \
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

            self._DesignParameter['_AdditionalMet1OnPMOS']['_XYCoordinates'] = tmp4
            self._DesignParameter['_AdditionalMet1OnPMOS']['_Width'] = \
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

            # Additional Metal2 Layer Generation
            self._DesignParameter['_AdditionalMet2OnNMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],
                                                _XWidth=400, _YWidth=400)
            self._DesignParameter['_AdditionalMet2OnPMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],
                                                _XWidth=400, _YWidth=400)

            tmp12 = []
            if self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] <= _DRCObj._MetalxMinArea / (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']):
                for i in range(0, len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'])):
                    tmp12.append([self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i][0],self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1]])

            self._DesignParameter['_AdditionalMet2OnNMOS']['_XYCoordinates'] = tmp12
            self._DesignParameter['_AdditionalMet2OnNMOS']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet2OnNMOS']['_YWidth'] = _DRCObj._MetalxMinArea / (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])

            tmp13 = []
            if self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] <= _DRCObj._MetalxMinArea / (self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']):
                for i in range(0, len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'])):
                    tmp13.append([self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],
                                  self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][1]])
            self._DesignParameter['_AdditionalMet2OnPMOS']['_XYCoordinates'] = tmp13
            self._DesignParameter['_AdditionalMet2OnPMOS']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet2OnPMOS']['_YWidth'] = _DRCObj._MetalxMinArea / (self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])




            # Additional POLY Layer Generation

            self._DesignParameter['_AdditionalPolyOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)
            self._DesignParameter['_AdditionalPolyOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_Width=400)

            tmp6 = [[[self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] +
                   self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2, self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]],
                   [self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] -
                   self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2, self._DesignParameter['_VIANMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmp6
            self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = self._DesignParameter['_VIANMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            tmp7 = [[[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                      self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2,
                      self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]],
                     [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] -
                      self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2,
                      self._DesignParameter['_VIAPMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmp7
            self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = self._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

        # Additional NP Layer Generation
            self._DesignParameter['_AdditionalNPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],
                                                _XWidth=400, _YWidth=400)
            _PPBoundary = _VDD2VSSHeight - _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2 - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            _NPBoundary = _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2 + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']
            self._DesignParameter['_AdditionalNPLayer']['_XYCoordinates'] = [[0, (_PPBoundary + _NPBoundary)/2]]
            self._DesignParameter['_AdditionalNPLayer']['_XWidth'] = (float)(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'])
            self._DesignParameter['_AdditionalNPLayer']['_YWidth'] = (float)(_PPBoundary - _NPBoundary)

        # NWELL Layer Generation

            self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NWLayer']['_XWidth'] = self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._NwMinEnclosurePactive * 2
            self._DesignParameter['_NWLayer']['_YWidth'] = self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + _DRCObj._NpMinExtensiononNactive\
                                                            + _DRCObj._NwMinEnclosurePactive + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[0, _PPBoundary + self._DesignParameter['_NWLayer']['_YWidth'] / 2]]

        # LVT Layer Gnereation
#            self._DesignParameter['_NLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NLVT'][0],_Datatype=DesignParameters._LayerMapping['NLVT'][1], _XYCoordinates=[],
#                                                _XWidth=400, _YWidth=400)
#            self._DesignParameter['_PLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PLVT'][0],_Datatype=DesignParameters._LayerMapping['PLVT'][1], _XYCoordinates=[],
#                                                _XWidth=400, _YWidth=400)
#
#            self._DesignParameter['_NLVTLayer']['_XYCoordinates'] = self._DesignParameter['_NMOS']['_XYCoordinates']
#            self._DesignParameter['_NLVTLayer']['_XWidth'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PDKLayer']['_XWidth']
#            self._DesignParameter['_NLVTLayer']['_YWidth'] = \
#            self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PDKLayer']['_YWidth']


#            self._DesignParameter['_PLVTLayer']['_XYCoordinates'] = self._DesignParameter['_PMOS']['_XYCoordinates']
#            self._DesignParameter['_PLVTLayer']['_XWidth'] = \
#            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
#            self._DesignParameter['_PLVTLayer']['_YWidth'] = \
#            self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']

            # Pin Declaration

            self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],\
                                                                            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
            self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],\
                                                                            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
            self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VIN')
            self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VOUT')

            self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
            self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
            self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0]+\
                self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0])/2), round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1]+\
                self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1])/2)]]
            self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]+\
                self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0])/2), round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1]+\
                self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1])/2)]]

            del tmp, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, tmp9, tmp10, tmp11






if __name__ == '__main__':
    InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter1')
    InverterObj._CalculateDesignParameter(_Finger = 1, _ChannelWidth = 400, _ChannelLength = 60,
                                          _NPRatio = 2, _VDD2VSSHeight = None, _Dummy = False)

    InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=InverterObj._DesignParameter)
    _fileName = 'autoInverter_HeightCal.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
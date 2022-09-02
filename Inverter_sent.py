import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import PbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import math
import random
import Inverter_test
import SST_resistor
import SST_GuardRingResistor



class _Inverter_sent(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(_Finger1 = None, _Finger2 = None,_Finger3 = None,_ChannelWidth1 = None, _ChannelLength1 = None,_ChannelWidth2 = None, _ChannelLength2 = None,_ChannelWidth3 = None, _ChannelLength3 = None, _NPRatio = None,\
                                  _VDD2VSSHeight = None, _Dummy = None,_NumSupplyCoX1 = None, _NumSupplyCoY1 = None,_NumSupplyCoX2 = None, _NumSupplyCoY2 = None,_NumSupplyCoX3 = None, _NumSupplyCoY3 = None, _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, _NumViaPoly2Met1CoX = None, \
                                  _NumViaPoly2Met1CoY = None, _NumViaPMOSMet12Met2CoX = None, _NumViaPMOSMet12Met2CoY = None, _NumViaNMOSMet12Met2CoX = None, _NumViaNMOSMet12Met2CoY = None, _XVT = None, _SupplyLine = None)


    def __init__(self, _DesignParameter = None, _Name = 'Inverter') :
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name = self._NameDeclaration(_Name = _Name), _GDSFile = self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger1 = None, _Finger2 = None,_Finger3 = None, _ChannelWidth1 = None, _ChannelLength1 = None, _ChannelWidth2 = None, _ChannelLength2 = None,\
                                  _ChannelWidth3 = None, _ChannelLength3 = None,_NPRatio = None,_VDD2VSSHeight = None, _Dummy = None,_NumSupplyCoX1 = None, _NumSupplyCoY1 = None,_NumSupplyCoX2 = None, _NumSupplyCoY2 = None,_NumSupplyCoX3 = None, _NumSupplyCoY3 = None, \
                                  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, _NumViaPoly2Met1CoX = None, \
                                  _NumViaPoly2Met1CoY = None, _NumViaPMOSMet12Met2CoX = None, _NumViaPMOSMet12Met2CoY = None, _NumViaNMOSMet12Met2CoX = None, _NumViaNMOSMet12Met2CoY = None, _XVT = None, _SupplyLine = None) :

        _DRCObj=DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        _LengthPMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_ChannelWidth1,_ParallelLength=_ChannelLength1) + _ChannelLength1


        _Inv = copy.deepcopy(Inverter_test._Inverter._ParametersForDesignCalculation)
        _Inv['_Finger'] = _Finger1
        _Inv['_ChannelWidth'] = _ChannelWidth1
        _Inv['_ChannelLength'] = _ChannelLength1
        _Inv['_NPRatio'] = _NPRatio
        _Inv['_VDD2VSSHeight'] = _VDD2VSSHeight
        _Inv['_Dummy'] = _Dummy
        _Inv['_NumSupplyCoX'] =_NumSupplyCoX1
        _Inv['_NumSupplyCoY'] = _NumSupplyCoY1
        _Inv['_SupplyMet1XWidth'] = _SupplyMet1XWidth
        _Inv['_SupplyMet1YWidth'] = _SupplyMet1YWidth
        _Inv['_NumViaPoly2Met1CoX'] =  _NumViaPoly2Met1CoX
        _Inv['_NumViaPoly2Met1CoY'] =  _NumViaPoly2Met1CoY
        _Inv['_NumViaPMOSMet12Met2CoX'] = _NumViaPMOSMet12Met2CoX
        _Inv['_NumViaPMOSMet12Met2CoY'] = _NumViaPMOSMet12Met2CoY
        _Inv['_NumViaNMOSMet12Met2CoX'] = _NumViaNMOSMet12Met2CoX
        _Inv['_NumViaNMOSMet12Met2CoY'] = _NumViaNMOSMet12Met2CoY
        _Inv['_XVT'] = _XVT
        _Inv['_SupplyLine'] = _SupplyLine


        self._DesignParameter['Inverter1'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None, _Name='Inverter1In{}'.format(_Name)))[0]
        self._DesignParameter['Inverter1']['_DesignObj']._CalculateDesignParameter(**_Inv)
        self._DesignParameter['Inverter1']['_XYCoordinates'] = [[0,0]]


        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_Width']=\
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2


        #####################################Inverter2######################################

        _Inv0 = copy.deepcopy(Inverter_test._Inverter._ParametersForDesignCalculation)
        _Inv0['_Finger'] = _Finger2
        _Inv0['_ChannelWidth'] = _ChannelWidth2
        _Inv0['_ChannelLength'] = _ChannelLength2
        _Inv0['_NPRatio'] = _NPRatio
        _Inv0['_VDD2VSSHeight'] = _VDD2VSSHeight
        _Inv0['_Dummy'] = _Dummy
        _Inv0['_NumSupplyCoX'] = _NumSupplyCoX2
        _Inv0['_NumSupplyCoY'] = _NumSupplyCoY2
        _Inv0['_SupplyMet1XWidth'] = _SupplyMet1XWidth
        _Inv0['_SupplyMet1YWidth'] = _SupplyMet1YWidth
        _Inv0['_NumViaPoly2Met1CoX'] = _NumViaPoly2Met1CoX
        _Inv0['_NumViaPoly2Met1CoY'] = _NumViaPoly2Met1CoY
        _Inv0['_NumViaPMOSMet12Met2CoX'] = _NumViaPMOSMet12Met2CoX
        _Inv0['_NumViaPMOSMet12Met2CoY'] = _NumViaPMOSMet12Met2CoY
        _Inv0['_NumViaNMOSMet12Met2CoX'] = _NumViaNMOSMet12Met2CoX
        _Inv0['_NumViaNMOSMet12Met2CoY'] = _NumViaNMOSMet12Met2CoY
        _Inv0['_XVT'] = _XVT
        _Inv0['_SupplyLine'] = _SupplyLine


        self._DesignParameter['Inverter2'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None, _Name='_Inverter2In{}'.format(_Name)))[0]
        self._DesignParameter['Inverter2']['_DesignObj']._CalculateDesignParameter(**_Inv0)
        self._DesignParameter['Inverter2']['_XYCoordinates'] = [[_LengthPMOSBtwPO*((_Finger1+_Finger2)/2+1),0]]

        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] = \
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2



        #####################################Inverter3######################################
        _Inv1 = copy.deepcopy(Inverter_test._Inverter._ParametersForDesignCalculation)
        _Inv1['_Finger'] = _Finger3
        _Inv1['_ChannelWidth'] = _ChannelWidth3
        _Inv1['_ChannelLength'] = _ChannelLength3
        _Inv1['_NPRatio'] = _NPRatio
        _Inv1['_VDD2VSSHeight'] = _VDD2VSSHeight
        _Inv1['_Dummy'] = _Dummy
        _Inv1['_NumSupplyCoX'] = _NumSupplyCoX3
        _Inv1['_NumSupplyCoY'] = _NumSupplyCoY3
        _Inv1['_SupplyMet1XWidth'] = _SupplyMet1XWidth
        _Inv1['_SupplyMet1YWidth'] = _SupplyMet1YWidth
        _Inv1['_NumViaPoly2Met1CoX'] = _NumViaPoly2Met1CoX
        _Inv1['_NumViaPoly2Met1CoY'] = _NumViaPoly2Met1CoY
        _Inv1['_NumViaPMOSMet12Met2CoX'] = _NumViaPMOSMet12Met2CoX
        _Inv1['_NumViaPMOSMet12Met2CoY'] = _NumViaPMOSMet12Met2CoY
        _Inv1['_NumViaNMOSMet12Met2CoX'] = _NumViaNMOSMet12Met2CoX
        _Inv1['_NumViaNMOSMet12Met2CoY'] = _NumViaNMOSMet12Met2CoY
        _Inv1['_XVT'] = _XVT
        _Inv1['_SupplyLine'] = _SupplyLine

        self._DesignParameter['Inverter3'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None, _Name='Inverter3In{}'.format(_Name)))[0]
        self._DesignParameter['Inverter3']['_DesignObj']._CalculateDesignParameter(**_Inv1)
        self._DesignParameter['Inverter3']['_XYCoordinates'] = [[_LengthPMOSBtwPO*((_Finger1+_Finger3)/2+_Finger2+2),0]]



        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] = \
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2

        ##################################################### P,NbodyContact Delete ###########################################

        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]

        #####################################################Contact Layer Calculation###########################################

        tmpXYs = []
        _ContactNum = _NumSupplyCoX1
        if _ContactNum == None:
            _ContactNum = int(( \
                    self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + self._DesignParameter['Inverter3']['_XYCoordinates'][0][0] + \
                    self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 ) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))

        if _ContactNum < 2:
            _ContactNum = 2

        if _NumSupplyCoY1 is None:
            _NumSupplyCoY = 2

        _XYCoordinateOfNbodyContact=[[0,0]]
        _NumSupplyCoX= _ContactNum
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumSupplyCoX,NumOfCOY=_NumSupplyCoY1)
        for i in range(0, _NumSupplyCoX):
            for j in range(0, _NumSupplyCoY1):
                tmpXYs.append([_XYCoordinateOfNbodyContact[0][0] - (_NumSupplyCoX - 1) / 2.0 * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                               _XYCoordinateOfNbodyContact[0][1] - (_NumSupplyCoY1 - 1) / 2.0 * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO])


        _Nbodyinputs = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
        _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY1
        _Nbodyinputs['_Met1XWidth'] = 0
        _Nbodyinputs['_Met1YWidth'] = 0


        self._DesignParameter['_Nbodyinputs'] = self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None,_Name='_NbodyinputsIn{}'.format(_Name)))[0]
        self._DesignParameter['_Nbodyinputs']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)
        self._DesignParameter['_Nbodyinputs']['_XYCoordinates']=[[(self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 +\
                                      self._DesignParameter['Inverter3']['_XYCoordinates'][0][0]+self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 )/2\
                                         -self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2,0]]

        self._DesignParameter['_Nbodyinputs']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['_Nbodyinputs']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] = 0
        self._DesignParameter['_Nbodyinputs']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] = 0

        self._DesignParameter['_Nbodyinputs']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = 0
        self._DesignParameter['_Nbodyinputs']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 0

        _Pbodyinputs = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
        _Pbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Pbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY1
        _Pbodyinputs['_Met1XWidth'] = 0
        _Pbodyinputs['_Met1YWidth'] = 0

        self._DesignParameter['_Pbodyinputs'] = self._SrefElementDeclaration(_DesignObj=NbodyContact_iksu._NbodyContact(_DesignParameter=None, _Name='_PbodyinputsIn{}'.format(_Name)))[0]
        self._DesignParameter['_Pbodyinputs']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)
        self._DesignParameter['_Pbodyinputs']['_XYCoordinates']=[[(self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 +\
                                      self._DesignParameter['Inverter3']['_XYCoordinates'][0][0]+self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 )/2\
                                         -self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2,\
                                                                  self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_Pbodyinputs']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['_Pbodyinputs']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] = 0
        self._DesignParameter['_Pbodyinputs']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] = 0

        self._DesignParameter['_Pbodyinputs']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = 0
        self._DesignParameter['_Pbodyinputs']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 0

        ##################################################### Metal3 Delete ###########################################
        if _Finger1>4 :
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_Met3InRouting']['_Width'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'] = [[]]
        if _Finger2 > 4:
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']= 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_Met3InRouting']['_Width'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'] = [[]]
        if _Finger3 > 4:
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_Met3InRouting']['_Width'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'] = [[]]







        ##################################################### Metal2 Delete ###########################################
        if _Finger1 > 4:
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0
        if _Finger2 > 4:
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']= 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0

        if _Finger3 > 4:
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = 0



        ##################################################### Via1 Delete ###########################################
        if _Finger1 > 4:
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0
        if _Finger2 > 4:
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0
        if _Finger3 > 4:
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0

        ##################################################### ViaMet2Met3(Via2) Delete ###########################################
        if _Finger1 > 4:
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0
        if _Finger2 > 4:
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0
        if _Finger3 > 4:
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] = 0
            self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] = 0


    ##################################################### Output Met2 Boundary&Routing ###########################################

        # Horizontal Met2  inv1
        self._DesignParameter['_Met2ouput1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)

        self._DesignParameter['_Met2ouput1']['_Width'] = _DRCObj._MetalxMinWidth

        self._DesignParameter['_Met2ouput1']['_XYCoordinates'] = \
            [[[self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0]+ self._DesignParameter['Inverter1']['_XYCoordinates'][0][0], \
               self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
              [self._DesignParameter['Inverter2']['_XYCoordinates'][0][0] +self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0],
               self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]


        #Horizontal Met2  inv2
        self._DesignParameter['_Met2ouput2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)
        self._DesignParameter['_Met2ouput2']['_Width'] = _DRCObj._MetalxMinWidth

        self._DesignParameter['_Met2ouput2']['_XYCoordinates'] = \
                [[[self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0]+\
                   self._DesignParameter['Inverter2']['_XYCoordinates'][0][0], \
                   self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
                  [self._DesignParameter['Inverter3']['_XYCoordinates'][0][0] +
                   self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] \
                      , self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        # Horizontal Met2  inv3
    #    self._DesignParameter['_Met2ouput3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=None)
     #   self._DesignParameter['_Met2ouput3']['_Width'] = _DRCObj._MetalxMinWidth

     #   self._DesignParameter['_Met2ouput3']['_XYCoordinates'] = \
     #           [[[self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][0] +self._DesignParameter['Inverter3']['_XYCoordinates'][0][0], \
      #         self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
     #         [다음에 이어질 output좌표, \
      #         self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        ##################################################### Metal1 added in Vin ,Vout Contact ##########################################

        # Horizontal Met1 inv3

        self._DesignParameter['_Met1ouput2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=None)

        self._DesignParameter['_Met1ouput2']['_Width'] = _DRCObj._VIAxMinWidth  +  max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1ouput2']['_XYCoordinates'] = [[[ \
            self._DesignParameter['Inverter3']['_XYCoordinates'][0][0] + self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0],\
            self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]] , \
           [self._DesignParameter['Inverter3']['_XYCoordinates'][0][0], self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1] ]]]

        # Horizontal Met1 inv2
        self._DesignParameter['_Met1ouput3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=None)

        self._DesignParameter['_Met1ouput3']['_Width'] = _DRCObj._VIAxMinWidth  +  max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1ouput3']['_XYCoordinates'] = [[[ \
            self._DesignParameter['Inverter2']['_XYCoordinates'][0][0] +self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], \
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
            [self._DesignParameter['Inverter2']['_XYCoordinates'][0][0],self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

        ##################################################### Via1 added to Vin, Vout Contact ###########################################

        _Via1added = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _Via1added['_ViaMet12Met2NumberOfCOX'] = 1
        _Via1added['_ViaMet12Met2NumberOfCOY'] = 2
        self._DesignParameter['_Via1added'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='_Via1addedIn{}'.format(_Name)))[0]
        self._DesignParameter['_Via1added']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_Via1added)
        self._DesignParameter['_Via1added']['_XYCoordinates']=[[self._DesignParameter['Inverter2']['_XYCoordinates'][0][0]+\
                                                                self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0],\
                                                                self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]

        _Via1added2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _Via1added2['_ViaMet12Met2NumberOfCOX'] = 1
        _Via1added2['_ViaMet12Met2NumberOfCOY'] = 2
        self._DesignParameter['_Via1added2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='_Via1added2In{}'.format(_Name)))[0]
        self._DesignParameter['_Via1added2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**_Via1added)
        self._DesignParameter['_Via1added2']['_XYCoordinates'] = [[self._DesignParameter['Inverter3']['_XYCoordinates'][0][0]+\
             self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], \
             self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]

        ##################################### Inv1,Inv2,Inv3 Pin Delete#######################################

        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VDDpin'] = \
            self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = '')
        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_VSSpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_VDDpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_VSSpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VDDpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VSSpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')


        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_Inputpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter2']['_DesignObj']._DesignParameter['_Outputpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_Inputpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter3']['_DesignObj']._DesignParameter['_Outputpin'] = \
            self._TextElementDeclaration( _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_Outputpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')
        self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_Inputpin'] = \
            self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]],_Mag=0.05, _Angle=0, _TEXT='')

        ##################################### Inv1 IN, VDD, VSS pin Genteration #######################################

        _VDD2VSSMinHeight = self.CeilMinSnapSpacing(
            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
            + max(self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], \
                  self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
            + self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
            + max(self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], \
                  self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) + \
                2 * _DRCObj._Metal1DefaultSpace +self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
            2 * _DRCObj._Metal1DefaultSpace + _DRCObj._Metal1MinSpace, MinSnapSpacing)


        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='IN')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSMinHeight]]
        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['_Inputpin']['_XYCoordinates'] = [
            [self.CeilMinSnapSpacing(round((self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + \
                                            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2),MinSnapSpacing),
             self.CeilMinSnapSpacing(round((self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + \
                                            self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2),MinSnapSpacing)]]




        #print( self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'])
        #print(  self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'])

      #  if _Finger1 == 2 :
      #      self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self._DesignParameter['Inverter1']['_DesignObj']._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*2


       # if _Finger1 == 1 or _Finger2 ==1 or _Finger3==1 :
        #    raise NotImplementedError("Finger of MOS should be larger than 1!!")

if __name__ == '__main__':
    #for i in range(0,100):
        import ftplib
        import random

       # _Finger3 = random.randint(2,40)
       # _Finger2 = random.randint(2,40)
        #_Finger1 = random.randint(2,40)

        _Finger3 = 32
        _Finger2 = 8
        _Finger1 = 2

        #_ChannelWidth1 = _ChannelWidth2 = _ChannelWidth3 = random.randrange(200,500,2)
       # _ChannelLength1 = _ChannelLength2 = _ChannelLength3 = random.randrange(30,48,2)

        _ChannelWidth1 = _ChannelWidth2 = _ChannelWidth3 = 200
        _ChannelLength1 = _ChannelLength2 = _ChannelLength3 = 30

        _NPRatio = 2
        _VDD2VSSHeight = None
        _Dummy = True
        _NumSupplyCoX1= None
        _NumSupplyCoY1 = _NumSupplyCoY2=_NumSupplyCoY3=3   # The number of inverter 1,2,3 contact Y direction
        _NumSupplyCoX2 = None
        _NumSupplyCoX3 = None
        _SupplyMet1XWidth = None
        _SupplyMet1YWidth = None
        _NumViaPoly2Met1CoX = None
        _NumViaPoly2Met1CoY = None
        _NumViaPMOSMet12Met2CoX = None
        _NumViaPMOSMet12Met2CoY = None
        _NumViaNMOSMet12Met2CoX = None
        _NumViaNMOSMet12Met2CoY = None
        _XVT = 'LVT'
        _SupplyLine = False

        # from Private import MyInfo
        # import DRCchecker
        libname = 'Inverter'
        cellname = 'Inverter'
        _fileName = cellname + '.gds'

        InputParams = dict(
            _Finger1=_Finger1,
            _Finger2=_Finger2,
            _Finger3=_Finger3,
            _ChannelWidth1=_ChannelWidth1,
            _ChannelLength1=_ChannelLength1,
            _ChannelWidth2=_ChannelWidth2,
            _ChannelLength2=_ChannelLength2,
            _ChannelWidth3=_ChannelWidth3,
            _ChannelLength3=_ChannelLength3,
            _NPRatio=_NPRatio,
            _VDD2VSSHeight=_VDD2VSSHeight,
            _Dummy=_Dummy,


            _NumSupplyCoX1=_NumSupplyCoX1,
            _NumSupplyCoY1=_NumSupplyCoY1,
            _NumSupplyCoX2 = _NumSupplyCoX2,
            _NumSupplyCoY2 = _NumSupplyCoY2,
            _NumSupplyCoX3 = _NumSupplyCoX3,
            _NumSupplyCoY3 = _NumSupplyCoY3,
            _SupplyMet1XWidth=_SupplyMet1XWidth,
            _SupplyMet1YWidth=_SupplyMet1YWidth,
            _NumViaPoly2Met1CoX=_NumViaPoly2Met1CoX,
            _NumViaPoly2Met1CoY=_NumViaPoly2Met1CoY,
            _NumViaPMOSMet12Met2CoX=_NumViaPMOSMet12Met2CoX,
            _NumViaPMOSMet12Met2CoY=_NumViaPMOSMet12Met2CoY,
            _NumViaNMOSMet12Met2CoX=_NumViaNMOSMet12Met2CoX,
            _NumViaNMOSMet12Met2CoY=_NumViaNMOSMet12Met2CoY,
            _XVT=_XVT,
            _SupplyLine=_SupplyLine
        )



        LayoutObj = _Inverter_sent(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()


        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('ljw95', 'dlwodn123')
        ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
        myfile = open('Inverter.gds', 'rb')
        ftp.storbinary('STOR Inverter.gds', myfile)
        myfile.close()
        ftp.close()

       # import DRCchecker
       # a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Inverter','Inverter',None)
       # a.DRCchecker()

    #print ("DRC Clean!!!")


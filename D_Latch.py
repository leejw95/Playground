from re import S
from select import select
from tkinter import N
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
import ViaMet32Met4
import ftplib
import Inverter_test
import Transmission_Gate

class _DLatch (StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(_TGFinger=None, _TGChannelWidth=None, _TGChannelLength=None, _TGNPRatio=None, _TGVDD2VSSHeight=None, _Dummy = False, _TGXVT = None, _TGSupplyMet1YWidth=None,
                                  _INVFinger = None,  _INVChannelWidth = None, _INVChannelLength = None, _INVNPRatio = None,\
                                  _INVVDD2VSSHeight = None, _INVNumSupplyCoX = None, _INVNumSupplyCoY = None, \
                                  _INVSupplyMet1XWidth = None, _INVSupplyMet1YWidth = None, _INVNumViaPoly2Met1CoX = None, \
                                  _INVNumViaPoly2Met1CoY = None, _INVNumViaPMOSMet12Met2CoX = None, \
                                  _INVNumViaPMOSMet12Met2CoY = None, _INVNumViaNMOSMet12Met2CoX = None, INV_NumViaNMOSMet12Met2CoY = None, _INVXVT = None, _INVSupplyLine = None)

    def __init__(self, _DesignParameter = None, _Name = 'D_Latch'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None :
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDLatch (self, _TGFinger=None, _TGChannelWidth=None, _TGChannelLength=None, _TGNPRatio=None, _TGVDD2VSSHeight=None, _Dummy = False, _TGXVT = None, _TGSupplyMet1YWidth=None,
                                  _INVFinger = None,  _INVChannelWidth = None, _INVChannelLength = None, _INVNPRatio = None,\
                                  _INVVDD2VSSHeight = None, _INVNumSupplyCoX = None, _INVNumSupplyCoY = None, \
                                  _INVSupplyMet1XWidth = None, _INVSupplyMet1YWidth = None, _INVNumViaPoly2Met1CoX = None, \
                                  _INVNumViaPoly2Met1CoY = None, _INVNumViaPMOSMet12Met2CoX = None, \
                                  _INVNumViaPMOSMet12Met2CoY = None, _INVNumViaNMOSMet12Met2CoX = None, _INVNumViaNMOSMet12Met2CoY = None, _INVXVT = None, _INVSupplyLine = None) :

        print ('#########################################################################################################')
        print ('                                   {}  D_Latch Calculation Start                                         '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        if _TGVDD2VSSHeight == None and _INVVDD2VSSHeight == None :
            det = 0
        else :
            det = 1

        while det != 2 :
            _TransmissionGateInputs = copy.deepcopy(Transmission_Gate._TransmissionGate._ParametersForDesignCalculation)
            _TransmissionGateInputs['_Finger'] = _TGFinger
            _TransmissionGateInputs['_ChannelWidth'] = _TGChannelWidth
            _TransmissionGateInputs['_ChannelLength'] = _TGChannelLength
            _TransmissionGateInputs['_VDD2VSSHeight'] = _TGVDD2VSSHeight
            _TransmissionGateInputs['_Dummy'] = _Dummy
            _TransmissionGateInputs['_NPRatio'] = _TGNPRatio
            _TransmissionGateInputs['_XVT'] = _TGXVT
            _TransmissionGateInputs['_SupplyMet1YWidth'] = _TGSupplyMet1YWidth

            _InverterInputs = copy.deepcopy(Inverter_test._Inverter._ParametersForDesignCalculation)
            _InverterInputs['_Finger'] = _INVFinger
            _InverterInputs['_ChannelWidth'] = _INVChannelWidth
            _InverterInputs['_ChannelLength'] = _INVChannelLength
            _InverterInputs['_NPRatio'] = _INVNPRatio
            _InverterInputs['_VDD2VSSHeight'] = _INVVDD2VSSHeight
            _InverterInputs['_Dummy'] = _Dummy
            _InverterInputs['_NumSupplyCoX'] = _INVNumSupplyCoX
            _InverterInputs['_NumSupplyCoY'] = _INVNumSupplyCoY
            _InverterInputs['_SupplyMet1XWidth'] = _INVSupplyMet1XWidth
            _InverterInputs['_SupplyMet1YWidth'] = _INVSupplyMet1YWidth
            _InverterInputs['_NumViaPoly2Met1CoX'] = _INVNumViaPoly2Met1CoX
            _InverterInputs['_NumViaPoly2Met1CoY'] = _INVNumViaPoly2Met1CoY
            _InverterInputs['_NumViaPMOSMet12Met2CoX'] = _INVNumViaPMOSMet12Met2CoX
            _InverterInputs['_NumViaPMOSMet12Met2CoY'] = _INVNumViaPMOSMet12Met2CoY
            _InverterInputs['_NumViaNMOSMet12Met2CoX'] = _INVNumViaNMOSMet12Met2CoX
            _InverterInputs['_NumViaNMOSMet12Met2CoY'] = _INVNumViaNMOSMet12Met2CoY
            _InverterInputs['_XVT'] = _INVXVT
            _InverterInputs['_SupplyLine'] = _INVSupplyLine

            self._DesignParameter['_TransmissionGate1'] = self._SrefElementDeclaration(_DesignObj=Transmission_Gate._TransmissionGate(_DesignParameter=None,_Name='TransmissionGate1In{}'.format(_Name)))[0]
            self._DesignParameter['_TransmissionGate1']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateInputs)

            self._DesignParameter['_TransmissionGate2'] = self._SrefElementDeclaration( _DesignObj=Transmission_Gate._TransmissionGate(_DesignParameter=None,_Name='TransmissionGate2In{}'.format(_Name)), _Reflect = [1,0,0], _Angle = 0)[0]
            self._DesignParameter['_TransmissionGate2']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateInputs)

            self._DesignParameter['_Inverter1'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None,_Name='Inverter1In{}'.format(_Name)))[0]
            self._DesignParameter['_Inverter1']['_DesignObj']._CalculateDesignParameter(**_InverterInputs)

            self._DesignParameter['_Inverter2'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None,_Name='Inverter2In{}'.format(_Name)), _Reflect = [1,0,0], _Angle = 0)[0]
            self._DesignParameter['_Inverter2']['_DesignObj']._CalculateDesignParameter(**_InverterInputs)

            if _TGVDD2VSSHeight == None and _INVVDD2VSSHeight == None :
                _TGVDD2VSSHeight = max(self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_TGVDD2VSSMinHeight']['_Ignore'], 
                                        self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_INVVDD2VSSMinHeight']['_Ignore'])
                
                _INVVDD2VSSHeight = _TGVDD2VSSHeight
                det += 1
            
            else :
                det += 1

        print ('#################################       Coordinates Settings      ########################################')
        _DLatchOrigin = [[0,0]]

        self._DesignParameter['_TransmissionGate1']['_XYCoordinates'] = _DLatchOrigin

        self._DesignParameter['_TransmissionGate2']['_XYCoordinates'] = _DLatchOrigin


        if _Dummy == True :
            self._DesignParameter['_Inverter1']['_XYCoordinates'] = [[_DLatchOrigin[0][0] + 
                        abs(self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) +
                        self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] // 2 +
                        _DRCObj._PolygateMinSpace +
                        self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] // 2 +
                        abs(self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
                        _DLatchOrigin[0][1]]]

            self._DesignParameter['_Inverter2']['_XYCoordinates'] = [[_DLatchOrigin[0][0] + 
                        abs(self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) +
                        self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] // 2 +
                        _DRCObj._PolygateMinSpace +
                        self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] // 2 +
                        abs(self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
                        _DLatchOrigin[0][1]]]

    
        self._DesignParameter['_TGtoTGOutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_TGtoTGOutputRouting']['_Width'] = self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        
        tmp = []
        for i in range (0, len(self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
                        _DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]],
                        [_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                        self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
                        _DLatchOrigin[0][1] - abs(self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1])]])
        
        self._DesignParameter['_TGtoTGOutputRouting']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_TGtoINVOutputRouting1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_TGtoINVOutputRouting1']['_Width'] = self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_Width']
        self._DesignParameter['_TGtoINVOutputRouting1']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][0],
                    _DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][1]],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0][0],
                    _DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][1]]],
                    [[_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0][0],
                    _DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][1] +
                    self._DesignParameter['_TGtoINVOutputRouting1']['_Width'] // 2],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0][0],
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0][1]]]]


        _ViaNum = _INVNumViaNMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2 :
            _ViaNum = 2

        if _INVNumViaNMOSMet12Met2CoX == None:
            _INVNumViaNMOSMet12Met2CoX = 1
        
        _ViaMet22Met3OnINV2Output = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3OnINV2Output['_ViaMet22Met3NumberOfCOX'] = _INVNumViaNMOSMet12Met2CoX
        _ViaMet22Met3OnINV2Output['_ViaMet22Met3NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet22Met3OnINV2Output'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnINV2OutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnINV2Output']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnINV2Output)
        self._DesignParameter['_ViaMet22Met3OnINV2Output']['_XYCoordinates'] = [[_DLatchOrigin[0][0] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0],
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] -
                abs(self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1])]]

        del _ViaNum

        self._DesignParameter['_TGtoINVOutputRouting2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_TGtoINVOutputRouting2']['_Width'] = self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_Width']
        self._DesignParameter['_TGtoINVOutputRouting2']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][0],
                _DLatchOrigin[0][1] - abs(self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1])],
                [self._DesignParameter['_ViaMet22Met3OnINV2Output']['_XYCoordinates'][0][0],
                _DLatchOrigin[0][1] - abs(self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1])]]]


        _ViaNum = _INVNumViaNMOSMet12Met2CoY
        if _ViaNum == None:
            _ViaNum = int(abs(self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2)
                    // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _ViaNum < 2 :
            _ViaNum = 2

        _ViaMet22Met3OnINV1Output = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3OnINV1Output['_ViaMet22Met3NumberOfCOX'] = _ViaNum
        _ViaMet22Met3OnINV1Output['_ViaMet22Met3NumberOfCOY'] = 1
        self._DesignParameter['_ViaMet22Met3OnINV1Output'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnINV1OutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnINV1Output']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnINV1Output)
        self._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'] = [[self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + 
                    (self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0]) // 2,
                    self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]

        del _ViaNum

        self._DesignParameter['_INV1OuttoINV2InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_INV1OuttoINV2InRouting']['_Width'] = self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_Met2OnOutput']['_Width']
        self._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][0][0],
                            self._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][0][0],
                            _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] -
                            abs(self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0][1])]]]

        ### Additional Routings for Doping & Supply Metals
        self._DesignParameter['_UpwardVDDMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardVDDMet1Routing']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2]]]


        self._DesignParameter['_UpwardVDDODRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardVDDODRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2]]]



        self._DesignParameter['_DownwardVDDMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardVDDMet1Routing']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2]]]

        
        self._DesignParameter['_DownwardVDDODRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardVDDODRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2]]]


        self._DesignParameter['_CenterVSSMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_CenterVSSMet1Routing']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2]]]

        self._DesignParameter['_CenterVSSODRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_CenterVSSODRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] // 2)) // 2]]]

        
        self._DesignParameter['_CenterVSSPPRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_CenterVSSPPRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2]]]


        self._DesignParameter['_UpwardPMOSPPRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardPMOSPPRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2]]]

        
        self._DesignParameter['_DownwardPMOSPPRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardPMOSPPRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) -
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

        self._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2],
                [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
                -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2) +
                min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2,
                _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)) // 2]]]


        self._DesignParameter['_UpwardPMOSNWRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardPMOSNWRouting']['_Width'] = self.CeilMinSnapSpacing(max(self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2,
                self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2) -
                min(self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] - 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2,
                self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2), 2 * MinSnapSpacing)


        self._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 +
                self._DesignParameter['_UpwardPMOSNWRouting']['_Width'] // 2,
                max((self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][1]),
                (self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][1]))],
                [self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 +
                self._DesignParameter['_UpwardPMOSNWRouting']['_Width'] // 2,
                min((self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][1][1]),
                (self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][1][1]))]]]

        
        self._DesignParameter['_DownwardPMOSNWRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardPMOSNWRouting']['_Width'] = self.CeilMinSnapSpacing(max(self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2,
                self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2) -
                min(self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] - 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2,
                self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2), 2 * MinSnapSpacing)


        self._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 +
                self._DesignParameter['_DownwardPMOSNWRouting']['_Width'] // 2,
                -max((self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][1]),
                (self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][1]))],
                [self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][0][0] -
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 +
                self._DesignParameter['_DownwardPMOSNWRouting']['_Width'] // 2,
                -min((self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][1][1]),
                (self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NWLayer']['_XYCoordinates'][0][1][1]))]]]


        if _TGXVT == 'SLVT' and _INVXVT == 'SLVT' :
            self._DesignParameter['_DownwardPMOSXVTRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TGXVT][0], _Datatype=DesignParameters._LayerMapping[_TGXVT][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_DownwardPMOSXVTRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) -
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

            self._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] -
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2]]]

            self._DesignParameter['_UpwardPMOSXVTRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TGXVT][0], _Datatype=DesignParameters._LayerMapping[_TGXVT][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_UpwardPMOSXVTRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) -
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

            self._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] -
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2]]]

            self._DesignParameter['_UpwardNMOSXVTRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TGXVT][0], _Datatype=DesignParameters._LayerMapping[_TGXVT][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_UpwardNMOSXVTRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) -
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

            self._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] -
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    (max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter1']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2]]]

            self._DesignParameter['_DownwardNMOSXVTRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TGXVT][0], _Datatype=DesignParameters._LayerMapping[_TGXVT][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_DownwardNMOSXVTRouting']['_Width'] = self.CeilMinSnapSpacing(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) -
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2), 2 * MinSnapSpacing)

            self._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'] = [[[_DLatchOrigin[0][0] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] -
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2],
                    [_DLatchOrigin[0][0] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][0] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0] +
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
                    -(max(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2) +
                    min(_DLatchOrigin[0][1] + self._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] - 
                    self._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2,
                    _DLatchOrigin[0][1] + self._DesignParameter['_Inverter2']['_XYCoordinates'][0][1] + 
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1] -
                    self._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] // 2)) // 2]]]

        
        



if __name__ == '__main__' :
    import time
    start = time.time()

    _TGFinger = 3
    _TGChannelWidth = 200
    _TGChannelLength = 30
    _TGNPRatio = 2
    _TGVDD2VSSHeight = None
    _Dummy = True
    _TGXVT = 'SLVT'
    _TGSupplyMet1YWidth = None
    _INVFinger = 5
    _INVChannelWidth = 200
    _INVChannelLength = 30
    _INVNPRatio = 2
    _INVVDD2VSSHeight = None
    _INVNumSupplyCoX = None
    _INVNumSupplyCoY = None
    _INVSupplyMet1XWidth = None
    _INVSupplyMet1YWidth = None
    _INVNumViaPoly2Met1CoX = None
    _INVNumViaPoly2Met1CoY = None
    _INVNumViaPMOSMet12Met2CoX = None
    _INVNumViaPMOSMet12Met2CoY = None
    _INVNumViaNMOSMet12Met2CoX = None
    _INVNumViaNMOSMet12Met2CoY = None
    _INVXVT = 'SLVT'
    _INVSupplyLine = None
    
    DesignParameters._Technology = '028nm'

    DLatchObj = _DLatch(_DesignParameter=None, _Name='D_Latch')
    #print ("A!!")
    DLatchObj._CalculateDLatch(_TGFinger = _TGFinger, _TGChannelWidth = _TGChannelWidth, _TGChannelLength = _TGChannelLength, _TGNPRatio = _TGNPRatio, _TGVDD2VSSHeight = _TGVDD2VSSHeight, _Dummy = _Dummy, _TGXVT = _TGXVT, _TGSupplyMet1YWidth = _TGSupplyMet1YWidth,
                                  _INVFinger = _INVFinger,  _INVChannelWidth = _INVChannelWidth, _INVChannelLength = _INVChannelLength, _INVNPRatio = _INVNPRatio,
                                  _INVVDD2VSSHeight = _INVVDD2VSSHeight, _INVNumSupplyCoX = _INVNumSupplyCoX, _INVNumSupplyCoY = _INVNumSupplyCoY,
                                  _INVSupplyMet1XWidth = _INVSupplyMet1XWidth, _INVSupplyMet1YWidth = _INVSupplyMet1YWidth, _INVNumViaPoly2Met1CoX = _INVNumViaPoly2Met1CoX,
                                  _INVNumViaPoly2Met1CoY = _INVNumViaPoly2Met1CoY, _INVNumViaPMOSMet12Met2CoX = _INVNumViaPMOSMet12Met2CoX,
                                  _INVNumViaPMOSMet12Met2CoY = _INVNumViaPMOSMet12Met2CoY, _INVNumViaNMOSMet12Met2CoX = _INVNumViaNMOSMet12Met2CoX, _INVNumViaNMOSMet12Met2CoY = _INVNumViaNMOSMet12Met2CoY, _INVXVT = _INVXVT, _INVSupplyLine = _INVSupplyLine)


    DLatchObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=DLatchObj._DesignParameter)
    _fileName = 'D_Latch.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = DLatchObj._CreateGDSStream(DLatchObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    print ("time : ", time.time() - start)

    print ('###############      Sending to FTP Server...      ##################')

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('D_Latch.gds', 'rb')
    ftp.storbinary('STOR D_Latch.gds', myfile)
    myfile.close()
    ftp.close()

    import lvstest
    _LVS = lvstest.LVStest('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/LVS_run','D_Latch','D_Latch','/mnt/sdc/junung/OPUS/Samsung28n')
    _LVS.LVSchecker()
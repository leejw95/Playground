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

        _ViaMet22Met3OnINV2Output = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3OnINV2Output['_ViaMet22Met3NumberOfCOX'] = NumViaNMOSMet12Met2CoX
        _ViaMet22Met3OnINV2Output['_ViaMet22Met3NumberOfCOY'] = _ViaNum

        self._DesignParameter['_ViaMet22Met3OnINV2Output'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnINV2OutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnINV2Output']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnINV2Output)
        



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
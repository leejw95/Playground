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
        _Name = 'D_Latch'
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        _TransmissionGateInputs = copy.deepcopy(Transmission_Gate._TransmissionGate._ParametersForDesignCalculation)
        _TransmissionGateInputs['_Finger'] = _TGFinger
        _TransmissionGateInputs['_ChannelWidth'] = _TGChannelWidth
        _TransmissionGateInputs['_ChannelLength'] = _TGChannelLength
        _TransmissionGateInputs['_VDD2VSSHeight'] = _TGVDD2VSSHeight
        _TransmissionGateInputs['_Dummy'] = _Dummy
        _TransmissionGateInputs['_NPRatio'] = _TGNPRatio
        _TransmissionGateInputs['_XVT'] = _TGXVT
        _TransmissionGateInputs['_SupplyMet1YWidth'] = _TGSupplyMet1YWidth

        self._DesignParameter['_TransmissionGate'] = self._SrefElementDeclaration(_DesignObj=Transmission_Gate._TransmissionGate(_DesignParameter=None,_Name='TransmissionGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_TransmissionGate']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateInputs)

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

        self._DesignParameter['_Inverter'] = self._SrefElementDeclaration(_DesignObj=Inverter_test._Inverter(_DesignParameter=None,_Name='InverterIn{}'.format(_Name)))[0]
        self._DesignParameter['_Inverter']['_DesignObj']._CalculateInverter(**_InverterInputs)

        print ('#################################       Coordinates Settings      ########################################')
        _DLatchOrigin = [[0,0]]

        self._DesignParameter['_TransmissionGate']['_XYCoordinates'] = _DLatchOrigin

        if _Dummy == True :
            self._DesignParameter['_Inverter']['_XYCoordinates'] = [[_DLatchOrigin[0][0] + 
                                                                    self._DesignParameter['_TransmissionGate']['_DesignObj']._DesignParameter['_NMOS']]]



if __name__ == '__main__' :
    import time
    start = time.time()
    ans = [3, 200, 30, 2, None, True, '_SLVT', 4, 2, None, None, None, None, None, None]

    _Finger = ans[0]
    _ChannelWidth = ans[1]
    _ChannelLength = ans[2]
    _NPRatio = ans[3]
    _VDD2VSSHeight = ans[4]
    _Dummy = ans[5]
    _XVT = ans[6]
    _NumSupplyCOX = ans[7]
    _NumSupplyCOY = ans[8]
    _SupplyMet1XWidth = ans[9]
    _SupplyMet1YWidth = ans[10]
    _NumVIAPoly2Met1COX = ans[11]
    _NumVIAPoly2Met1COY = ans[12]
    _NumVIAMet12COX = ans[13]
    _NumVIAMet12COY = ans[14]
    #print (_NumVIAMet12COY, _NumVIAMet12COX)
    DesignParameters._Technology = '028nm'

    DLatchObj = _DLatch(_DesignParameter=None, _Name='TransmissionGate')
    #print ("A!!")
    DLatchObj._CalculateDLatch(_Finger=_Finger, _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength, _NPRatio=_NPRatio, _VDD2VSSHeight=_VDD2VSSHeight,
                                   _Dummy=_Dummy, _XVT=_XVT, _NumSupplyCOX=_NumSupplyCOX, _NumSupplyCOY = _NumSupplyCOY, _SupplyMet1XWidth= _SupplyMet1XWidth,
                                   _SupplyMet1YWidth=_SupplyMet1YWidth, _NumVIAPoly2Met1COX=_NumVIAPoly2Met1COX, _NumVIAPoly2Met1COY= _NumVIAPoly2Met1COY,
                                   _NumVIAMet12COX=_NumVIAMet12COX, _NumVIAMet12COY=_NumVIAMet12COY, _Bodycontact = True)


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
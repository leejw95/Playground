import StickDiagram
import DesignParameters
import copy
import DRC
import NMOS
import PMOS
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import ftplib
import Inverter
import Transmission_Gate
import opppcres_b
import psubring
import ResistorBank

class _FullResistorBank(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(
                                            _XRBNum = None, _YRBNum = None,
                                            # _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterVDD2VSSHeight=None,
                                           _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                                           _TransmissionGateVDD2VSSHeight = None,
                                           _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None,_ResistorMetYCO=None,
                                           _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
                                           _PMOSSubringWidth=None,
                                           _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
                                           _NMOSSubringWidth=None,
                                           _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
                                           _TotalSubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name='FullResistorBank'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateFullResistorBank(self,
                               _XRBNum = None, _YRBNum = None,
                               _TransmissionGateFinger=None, _TransmissionGateChannelWidth=None,
                               _TransmissionGateChannelLength=None, _TransmissionGateNPRatio=None,
                               _TransmissionGateDummy=False, _TransmissionGateVDD2VSSHeight=None,
                               _TransmissionGateSLVT=False,
                               _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
                               _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
                               _PMOSSubringWidth=None,
                               _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
                               _NMOSSubringWidth=None,
                               _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
                               _TotalSubringWidth=None):

        print ('#########################################################################################################')
        print ('                                {}  FullResistorBank Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'FullResistorBank'

        print ('###############################      ResistorBank Generation     #########################################')

        _ResistorBankinputs = copy.deepcopy(ResistorBank._ResistorBank._ParametersForDesignCalculation)
        _ResistorBankinputs['_TransmissionGateFinger'] = _TransmissionGateFinger
        _ResistorBankinputs['_TransmissionGateChannelWidth'] = _TransmissionGateChannelWidth
        _ResistorBankinputs['_TransmissionGateChannelLength'] = _TransmissionGateChannelLength
        _ResistorBankinputs['_TransmissionGateNPRatio'] = _TransmissionGateNPRatio
        _ResistorBankinputs['_TransmissionGateDummy'] = _TransmissionGateDummy
        _ResistorBankinputs['_TransmissionGateVDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
        _ResistorBankinputs['_TransmissionGateSLVT'] = _TransmissionGateSLVT

        _ResistorBankinputs['_ResistorWidth'] = _ResistorWidth
        _ResistorBankinputs['_ResistorLength'] = _ResistorLength
        _ResistorBankinputs['_ResistorMetXCO'] = _ResistorMetXCO
        _ResistorBankinputs['_ResistorMetYCO'] = _ResistorMetYCO

        _ResistorBankinputs['_PMOSSubringType'] = _PMOSSubringType
        _ResistorBankinputs['_PMOSSubringXWidth'] = _PMOSSubringXWidth
        _ResistorBankinputs['_PMOSSubringYWidth'] = _PMOSSubringYWidth
        _ResistorBankinputs['_PMOSSubringWidth'] = _PMOSSubringWidth

        _ResistorBankinputs['_NMOSSubringType'] = _NMOSSubringType
        _ResistorBankinputs['_NMOSSubringXWidth'] = _NMOSSubringXWidth
        _ResistorBankinputs['_NMOSSubringYWidth'] = _NMOSSubringYWidth
        _ResistorBankinputs['_NMOSSubringWidth'] = _NMOSSubringWidth

        _ResistorBankinputs['_TotalSubringType'] = _TotalSubringType
        _ResistorBankinputs['_TotalSubringXWidth'] = _TotalSubringXWidth
        _ResistorBankinputs['_TotalSubringYWidth'] = _TotalSubringYWidth
        _ResistorBankinputs['_TotalSubringWidth'] = _TotalSubringWidth

        self._DesignParameter['_ResistorBank'] = self._SrefElementDeclaration(_DesignObj=ResistorBank._ResistorBank(_DesignParameter=None,_Name='ResistorBankIn{}'.format(_Name)))[0]
        self._DesignParameter['_ResistorBank']['_DesignObj']._CalculateResistorBank(**_ResistorBankinputs)



        print '#################################       Coordinates Settings      ########################################'
        _ResistorBankOrigin = [[0,0]]
        _ResistorSpaceX = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -
                                                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'])
        _ResistorSpaceY = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] -
                                                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'])
        tmp = []
        for i in range (0, _XRBNum) :
            for j in range(0, _YRBNum) :
                tmp.append([_ResistorBankOrigin[0][0] + i * _ResistorSpaceX,
                            _ResistorBankOrigin[0][1] + j * _ResistorSpaceY])

        self._DesignParameter['_ResistorBank']['_XYCoordinates'] = tmp
        del tmp


        print '################################       Additional Path Settings      #####################################'
        self._DesignParameter['_Met4LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met4LayerVCM']['_Width'] = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
        if self._DesignParameter['_Met4LayerVCM']['_Width'] % 2 == 1 :
            self._DesignParameter['_Met4LayerVCM']['_Width'] -= 1

        tmp = []

        for i in range (0, _YRBNum) :
            tmp.append([[_ResistorBankOrigin[0][0] - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 ,
                         _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'][0][1] +
                         i * _ResistorSpaceY],
                        [_ResistorBankOrigin[0][0] - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 +
                         (_XRBNum + 1 )* _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'][0][1] +
                         i * _ResistorSpaceY]])

        self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met5LayerVRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met5LayerVRX']['_Width'] = (
                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB'][
                        '_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] -
                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB'][
                        '_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'] * 2)
        if self._DesignParameter['_Met5LayerVRX']['_Width'] % 2 == 1:
            self._DesignParameter['_Met5LayerVRX']['_Width'] -= 1

        tmp = []

        for i in range(0, _YRBNum):
            tmp.append([[_ResistorBankOrigin[0][0] -
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB'][
                             '_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2,
                         _ResistorBankOrigin[0][1] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB'][
                             '_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace9 +
                         i * _ResistorSpaceY],
                        [_ResistorBankOrigin[0][0] -
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB'][
                             '_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 +
                         (_XRBNum + 1) * _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB'][
                             '_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace9 +
                         i * _ResistorSpaceY]])

        self._DesignParameter['_Met5LayerVRX']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVDD']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XWidth']

        tmp = []
        for i in range (0, _XRBNum) :
            tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][0][0] +
                         i * _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB'][
                                  '_DesignObj']._DesignParameter['_Met1Layery']['_YWidth']],
                        [_ResistorBankOrigin[0][0] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVDD'][
                             '_XYCoordinates'][0][0] +
                         i * _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] +
                         (_YRBNum + 1) * _ResistorSpaceY]])

        self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = tmp
        
        del tmp

        self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],
            _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVSS']['_Width'] = \
        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XWidth']

        tmp = []
        for i in range(0, _XRBNum):
            tmp.append([[_ResistorBankOrigin[0][0] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVSS'][
                             '_XYCoordinates'][0][0] +
                         i * _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] -
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB'][
                             '_DesignObj']._DesignParameter['_Met1Layery']['_YWidth']],
                        [_ResistorBankOrigin[0][0] +
                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met7LayerVSS'][
                             '_XYCoordinates'][0][0] +
                         i * _ResistorSpaceX,
                         _ResistorBankOrigin[0][1] +
                         (_YRBNum + 1) * _ResistorSpaceY]])

        self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = tmp

        del tmp

        ##Path for inputs for other transmission gate
        self._DesignParameter['_Met2LayerInput'] = self._PathElementDeclaration(
            _Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XYCoordinates=[], _Width=100)
        
        self._DesignParameter['_Met2LayerInput']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        
        tmp = []
        _TotalInputnum = (_XRBNum * _YRBNum * 2) - 1
        for i in range (0, _YRBNum) :
            for j in range (0, 2) : ## for nmos and pmos
                for k in range (0, _XRBNum) :
                    if j == 0 :
                        tmp.append([[_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                     self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] + 
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum],
                                    [_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                    self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
                                    _ResistorSpaceY * i]])
                        
                        tmp.append([[_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                    self._DesignParameter['_Met2LayerInput']['_Width'] +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
                                    _ResistorSpaceY * i],
                                    [_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                     _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
                                    _ResistorSpaceY * i]
                                    ])
                        
                        tmp.append([[_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                    _ResistorBankOrigin[0][1] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                                     self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
                                    _ResistorSpaceY * i],
                                    [_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                     _ResistorBankOrigin[0][1] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                                     _ResistorSpaceY * i]
                                    ])
                        
                        
                    else :
                        tmp.append([[_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                     self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] + 
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum],
                                    [_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                    self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
                                    _ResistorSpaceY * i]
                                    ])
                        
                        tmp.append([[_ResistorBankOrigin[0][0] - 
                                    (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
                                    self._DesignParameter['_Met2LayerInput']['_Width'] +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
                                    _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
                                    _ResistorSpaceY * i],
                                    [_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                    _ResistorBankOrigin[0][1] +
                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
                                    _ResistorSpaceY * i]
                                    ])
                        
                        tmp.append([[_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                    _ResistorBankOrigin[0][1] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] + 
                                     self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
                                    (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
                                    _ResistorSpaceY * i],
                                    [_ResistorBankOrigin[0][0] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
                                     _ResistorSpaceX * k,
                                      _ResistorBankOrigin[0][1] +
                                     self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] + 
                                     _ResistorSpaceY * i]
                                    ])
                    
        self._DesignParameter['_Met2LayerInput']['_XYCoordinates'] = tmp

        





if __name__ == '__main__' :

    _XRBNum = 4
    _YRBNum = 8

    _TransmissionGateFinger = 6
    _TransmissionGateChannelWidth = 200
    _TransmissionGateChannelLength = 30
    _TransmissionGateNPRatio = 2
    _TransmissionGateDummy = True     #T/F?
    _TransmissionGateVDD2VSSHeight = 2256 ## FIXED
    _TransmissionGateSLVT = True     #T/F?

    _ResistorWidth = 1250
    _ResistorLength = 1234
    _ResistorMetXCO = None
    _ResistorMetYCO = None

    _PMOSSubringType = False ## FIXED
    _PMOSSubringXWidth = None ## FIXED
    _PMOSSubringYWidth = None ## FIXED
    _PMOSSubringWidth = 170

    _NMOSSubringType = True ## FIXED
    _NMOSSubringXWidth = None ## FIXED
    _NMOSSubringYWidth = None ## FIXED
    _NMOSSubringWidth = _PMOSSubringWidth

    _TotalSubringType = True ## FIXED
    _TotalSubringXWidth = None ## FIXED
    _TotalSubringYWidth = None ## FIXED
    _TotalSubringWidth = 170

    DesignParameters._Technology = '028nm'

    FullResistorBankObj = _FullResistorBank(_DesignParameter=None, _Name='FullResistorBank')
    #print ("A!!")
    FullResistorBankObj._CalculateFullResistorBank(
                               #  _InverterFinger=_InverterFinger, _InverterChannelWidth=_InverterChannelWidth, _InverterChannelLength=_InverterChannelLength, _InverterNPRatio=_InverterNPRatio, _InverterDummy = _InverterDummy,
                               # _InverterVDD2VSSHeight=_InverterVDD2VSSHeight, _InverterSLVT = _InverterSLVT,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                                _XRBNum=_XRBNum, _YRBNum=_YRBNum,
                               _TransmissionGateFinger =_TransmissionGateFinger, _TransmissionGateChannelWidth = _TransmissionGateChannelWidth, _TransmissionGateChannelLength = _TransmissionGateChannelLength, _TransmissionGateNPRatio =_TransmissionGateNPRatio,
                               _TransmissionGateDummy = _TransmissionGateDummy , _TransmissionGateVDD2VSSHeight = _TransmissionGateVDD2VSSHeight, _TransmissionGateSLVT = _TransmissionGateSLVT,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO = _ResistorMetXCO, _ResistorMetYCO = _ResistorMetYCO,
                                _PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth,_PMOSSubringWidth=_PMOSSubringWidth,
                                _NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth,_NMOSSubringWidth=_NMOSSubringWidth,
                                _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth)


    FullResistorBankObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=FullResistorBankObj._DesignParameter)
    _fileName = 'FullResistorBank.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = FullResistorBankObj._CreateGDSStream(FullResistorBankObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')


    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('FullResistorBank.gds', 'rb')
    ftp.storbinary('STOR FullResistorBank.gds', myfile)
    myfile.close()
    ftp.close()
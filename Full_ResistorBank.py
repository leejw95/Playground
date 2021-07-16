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
                                           _PowerLine = False,
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
                               _PowerLine = False,
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
        _ResistorBankinputs['_PowerLine'] = _PowerLine

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



        print ('#################################       Coordinates Settings      ########################################')
        _ResistorBankOrigin = [[0,0]]
        _ResistorSpaceX = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -
                                                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'])
        _ResistorSpaceY = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] -
                                                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'])

        _GapbtwOriginX = _ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0]
        _GapbtwOriginY = _ResistorBankOrigin[0][1] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + 
                                                    self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])

        tmp = []
        for i in range (0, _XRBNum) :
            for j in range(0, _YRBNum) :
                tmp.append([_ResistorBankOrigin[0][0] + i * _ResistorSpaceX,
                            _ResistorBankOrigin[0][1] + j * _ResistorSpaceY])

        self._DesignParameter['_ResistorBank']['_XYCoordinates'] = tmp
        del tmp
        

        print ('################################       Additional Path Settings      #####################################')
        self._DesignParameter['_Met4LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met4LayerVCM']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XWidth'] + \
                                                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']

        tmp = []

        for i in range (0, _XRBNum) :
            tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
                            _ResistorBankOrigin[0][1] + _GapbtwOriginY],
                            [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
                            _ResistorBankOrigin[0][1] + _GapbtwOriginY + (_YRBNum) * _ResistorSpaceY]])

        self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met5LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met5LayerVCM']['_Width'] = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + 
                                                            self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1])- \
                                                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1]
        tmp = []
        for i in range (0, _YRBNum) :
            if i % 2 == 0 :
                tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX ,
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY],
                        [_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX,
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY]])


        self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'] = tmp

        del tmp

        _ViaVCMMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] = int(self._DesignParameter['_Met4LayerVCM']['_Width'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        if _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] < 1 :
            _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
        _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOY'] = int(self._DesignParameter['_Met5LayerVCM']['_Width'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))

        self._DesignParameter['_ViaMet42Met5OnVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnVCM']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVCMMet42Met5)

        tmp = []
        for i in range (0, _XRBNum) :
            for j in range (0, len(self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0][0] + i * _ResistorSpaceX,
                            self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'][j][0][1]])
        self._DesignParameter['_ViaMet42Met5OnVCM']['_XYCoordinates'] = tmp

        del tmp
        

        self._DesignParameter['_Met6LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerVCM']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
                                                         self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

        tmp = []
        for i in range (0, _XRBNum) :
            if i % 3 == 0 :
                tmp.append([[_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] - 
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
                        _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
                        _ResistorBankOrigin[0][1] + _GapbtwOriginY],
                        [_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] - 
                        self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
                        _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
                        _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

        self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'] = tmp

        del tmp

        _ViaVCMMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Met6LayerVCM']['_Width'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] = int(self._DesignParameter['_Met5LayerVCM']['_Width'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))

        self._DesignParameter['_ViaMet52Met6OnVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVCMIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVCM']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVCMMet52Met6)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'][j][0][1]])
        self._DesignParameter['_ViaMet52Met6OnVCM']['_XYCoordinates'] = tmp

        del tmp



        self._DesignParameter['_Met6LayerVRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerVRX']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth']
        # tmp = []
        # if _YRBNum % 2 == 0 :
        #     for i in range (0, _XRBNum) :
        #         for j in range (0, _YRBNum // 2) :
        #             tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * j],
        #                     [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * j + _ResistorSpaceY]])
        
        # elif _YRBNum == 1 :
        #     tmp = []
        
        # else :
        #     for i in range (0, _XRBNum) :
        #         for j in range (0, _YRBNum // 2 - 1) :
        #             tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * j],
        #                     [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * j + _ResistorSpaceY]])

        #     for i in range (0, _XRBNum) :
        #         tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * (_YRBNum // 2 - 1)],
        #                     [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
        #                     _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + _ResistorSpaceY * 2 * (_YRBNum // 2 - 1) + 2 * _ResistorSpaceY]])

        tmp = []
        for i in range(0, _XRBNum) :
            tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
                        _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1]],
                        [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
                        _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + (_YRBNum - 1) * _ResistorSpaceY]])

        self._DesignParameter['_Met6LayerVRX']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met7LayerVRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVRX']['_Width'] = _ResistorSpaceY * (_YRBNum // 2)
        if self._DesignParameter['_Met7LayerVRX']['_Width'] > 4500 :
            self._DesignParameter['_Met7LayerVRX']['_Width'] = 4500
        self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2,
                                                                _ResistorBankOrigin[0][1] + _ResistorSpaceY * (_YRBNum // 2)],
                                                                [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] +
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 + _ResistorSpaceX * (_XRBNum - 1),
                                                                _ResistorBankOrigin[0][1] + _ResistorSpaceY * (_YRBNum // 2)]]]

        _ViaVRXMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = self._DesignParameter['_Met7LayerVRX']['_Width'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)

        self._DesignParameter['_ViaMet62Met7OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVRX']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaVRXMet62Met7)

        tmp = []
        for i in range (0, _XRBNum) :
            tmp.append([_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + _ResistorSpaceX * i,
                        _ResistorBankOrigin[0][1] + _ResistorSpaceY * (_YRBNum // 2)])
        self._DesignParameter['_ViaMet62Met7OnVRX']['_XYCoordinates'] = tmp

        del tmp



        if _PowerLine == True :
            self._DesignParameter['_Met3LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met3LayerVDD']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met2LayerVDD']['_YWidth']
            
            tmp = []

            for i in range (0, _YRBNum) :
                tmp.append([[_ResistorBankOrigin[0][0] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - 
                            self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2),
                            _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] + 
                            self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] + 
                            i * _ResistorSpaceY],
                            [_ResistorBankOrigin[0][0] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - 
                            self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2) + 
                            _XRBNum * _ResistorSpaceX,
                            _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] + 
                            self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] + 
                            i * _ResistorSpaceY]])

            self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = tmp
            
            del tmp

            self._DesignParameter['_Met4LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met4LayerVDD']['_Width'] = self._DesignParameter

            self._DesignParameter['_Met2LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met2LayerVSS']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth']
            self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] =[[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0],
                                                                _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] -
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]],
                                                                [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0],
                                                                _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1]
                                                                + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] 
                                                                + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2
                                                                + _YRBNum * _ResistorSpaceY]],
                                                                [[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] + _XRBNum * _ResistorSpaceX,
                                                                _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] -
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
                                                                self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]],
                                                                [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] + _XRBNum * _ResistorSpaceX,
                                                                _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1]
                                                                + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] 
                                                                + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2
                                                                + _YRBNum * _ResistorSpaceY]]]

            

            
            # self._DesignParameter['_Met4LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[], _Width=100)
            # self._DesignParameter['_Met4LayerVSS2']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XWidth']

            # tmp = []
            # for i in range (0, _XRBNum) :
            #     tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
            #                 _ResistorBankOrigin[0][1] - _ResistorSpaceY],
            #                 [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
            #                 _ResistorBankOrigin[0][1] + _YRBNum * _ResistorSpaceY]])

            # self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'] = tmp

            # del tmp

        ##Path for inputs for other transmission gate and pin declaration
        # self._DesignParameter['_Met2LayerInput'] = self._PathElementDeclaration(
        #     _Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        #     _XYCoordinates=[], _Width=100)
        
        # self._DesignParameter['_Met2LayerInput']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        
        # tmp = []
        # _TotalInputnum = (_XRBNum * _YRBNum * 2) - 1
        # for i in range (0, _YRBNum) :
        #     for j in range (0, 2) : ## for nmos and pmos
        #         for k in range (0, _XRBNum) :
        #             if j == 0 : ## nmos settings
        #                 tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] + 
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum],
        #                             [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                             self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
        #                             _ResistorSpaceY * i]])
                        
        #                 self._DesignParameter['_S<{0}>pin'.format((i+1) * _XRBNum - k - 1)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], 
        #                                                               _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] + 
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum]], _Mag=0.1, _Angle=90, _TEXT = 'S<{0}>'.format((i+1) * _XRBNum - k - 1))
                        
                        
        #                 tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                             self._DesignParameter['_Met2LayerInput']['_Width'] +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
        #                             _ResistorSpaceY * i],
        #                             [_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * k,
        #                              _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
        #                             _ResistorSpaceY * i]
        #                             ])
                        
        #                 tmp.append([[_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * k,
        #                             _ResistorBankOrigin[0][1] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (k) + 
        #                             _ResistorSpaceY * i],
        #                             [_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * k,
        #                              _ResistorBankOrigin[0][1] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] + 
        #                              _ResistorSpaceY * i]
        #                             ])
                        
                        
        #             else : ##pmos settings
        #                 ##1st connection
        #                 tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] + 
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum],
        #                             [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                             self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
        #                             _ResistorSpaceY * i]
        #                             ])
                        
        #                 self._DesignParameter['_SB<{0}>pin'.format(i * _XRBNum + k)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0], 
        #                                                               _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] + 
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum]], _Mag=0.1, _Angle=90, _TEXT = 'SB<{0}>'.format(i * _XRBNum + k))

                        
        #                 ##second connection
        #                 tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] - 
        #                             (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
        #                             self._DesignParameter['_Met2LayerInput']['_Width'] +
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
        #                             _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
        #                             _ResistorSpaceY * i],
        #                             [_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * (_XRBNum - k - 1),
        #                             _ResistorBankOrigin[0][1] +
        #                             self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
        #                             _ResistorSpaceY * i]
        #                             ])
                        
        #                 ##third connection
        #                 tmp.append([[_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * (_XRBNum - k - 1),
        #                             _ResistorBankOrigin[0][1] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] - 
        #                              self._DesignParameter['_Met2LayerInput']['_Width'] // 2 -
        #                             (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met2LayerInput']['_Width']) * (_XRBNum - k - 1) + 
        #                             _ResistorSpaceY * i],
        #                             [_ResistorBankOrigin[0][0] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
        #                              _ResistorSpaceX * (_XRBNum - k - 1),
        #                               _ResistorBankOrigin[0][1] +
        #                              self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] + 
        #                              _ResistorSpaceY * i]
        #                             ])
                    
        
        # self._DesignParameter['_Met2LayerInput']['_XYCoordinates'] = tmp
        # del tmp
        
        ## TransmissionGate Pin Declaration
        for i in range (0, _XRBNum) :
            for j in range (0, _YRBNum) :
                for k in range (0, 2) : ## for nmos 0 and pmos 1
                    if k == 0 :
                        self._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                        _Presentation=[0,1,2], _Reflect=[0,0,0], 
                        _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][0] +
                                        i * _ResistorSpaceX,
                                        _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][1] +
                                        j * _ResistorSpaceY]],
                        _Mag = 0.5, _Angle=0, _TEXT='S<{0}>'.format(i + _XRBNum * j))

                    else :
                        self._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                        _Presentation=[0,1,2], _Reflect=[0,0,0], 
                        _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] +
                                        i * _ResistorSpaceX,
                                        _ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][1] +
                                        j * _ResistorSpaceY]],
                        _Mag = 0.5, _Angle=0, _TEXT='SB<{0}>'.format(i + _XRBNum * j))
                    
        
        self._DesignParameter['_VRXpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
                        _Presentation=[0,1,2], _Reflect=[0,0,0], 
                        _XYCoordinates=[[_ResistorBankOrigin[0][0] + (self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][1][0] - self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][0]) // 2,
                                        _ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1]]],
                        _Mag = 0.5, _Angle=0, _TEXT='VRX')
        
        
        
        




if __name__ == '__main__' :

    _XRBNum = 4
    _YRBNum = 8

    _TransmissionGateFinger = 6
    _TransmissionGateChannelWidth = 275  ##200nm ~ 500nm range
    _TransmissionGateChannelLength = 30
    _TransmissionGateNPRatio = 2  ##Default = 2
    _TransmissionGateDummy = True     #T/F?
    _TransmissionGateVDD2VSSHeight = 2398 ## FIXED
    _TransmissionGateSLVT = True     #T/F?

    _PowerLine = True # T/F?

    _ResistorWidth = 1250
    _ResistorLength = 1234    ## minimum : 400
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
                               _PowerLine = _PowerLine,
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

    import base64
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login(base64.b64decode('anVudW5n'), base64.b64decode('Y2hsd25zZG5kMSE='))
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('FullResistorBank.gds', 'rb')
    ftp.storbinary('STOR FullResistorBank.gds', myfile)
    myfile.close()
    ftp.close()
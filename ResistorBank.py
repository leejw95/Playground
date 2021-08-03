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
import ViaMet72Met8
import ftplib
import TransmissionGate
import opppcres_b
import psubring

class _ResistorBank(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(
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

    def __init__(self, _DesignParameter=None, _Name='ResistorBank'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateResistorBank(self,
                               # _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterDummy = False,
                               # _InverterVDD2VSSHeight=None, _InverterSLVT = False,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                               _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                               _TransmissionGateDummy = False , _TransmissionGateVDD2VSSHeight = None, _TransmissionGateSLVT = False,
                               _PowerLine = False,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
                               _PMOSSubringType = True, _PMOSSubringXWidth = None, _PMOSSubringYWidth = None, _PMOSSubringWidth = None,
                               _NMOSSubringType = True, _NMOSSubringXWidth = None, _NMOSSubringYWidth = None, _NMOSSubringWidth = None,
                               _TotalSubringType = True, _TotalSubringXWidth = None, _TotalSubringYWidth = None, _TotalSubringWidth = None):

        print ('#########################################################################################################')
        print ('                                {}  ResistorBank Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'ResistorBank'


        # print '###############################     Inverter Generation    ##############################################'
        # _Inverterinputs = copy.deepcopy(Inverter._Inverter._ParametersForDesignCalculation)
        # _Inverterinputs['_Finger'] = _InverterFinger
        # _Inverterinputs['_ChannelWidth'] = _InverterChannelWidth
        # _Inverterinputs['_ChannelLength'] = _InverterChannelLength
        # _Inverterinputs['_NPRatio'] = _InverterNPRatio
        # _Inverterinputs['_Dummy'] = _InverterDummy
        # _Inverterinputs['_VDD2VSSHeight'] = _InverterVDD2VSSHeight
        # _Inverterinputs['_SLVT'] = _InverterSLVT
        # _Inverterinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth
        #
        # self._DesignParameter['_InverterRB'] = self._SrefElementDeclaration(_DesignObj=Inverter._Inverter(_DesignParameter=None, _Name='InverterIn{}'.format(_Name)))[0]
        # self._DesignParameter['_InverterRB']['_DesignObj']._CalculateInverter(**_Inverterinputs)

        print ('##############################     TransmissionGate Generation    ########################################')
        _TransmissionGateinputs = copy.deepcopy(TransmissionGate._TransmissionGate._ParametersForDesignCalculation)
        _TransmissionGateinputs['_Finger'] = _TransmissionGateFinger
        _TransmissionGateinputs['_ChannelWidth'] = _TransmissionGateChannelWidth
        _TransmissionGateinputs['_ChannelLength'] = _TransmissionGateChannelLength
        _TransmissionGateinputs['_NPRatio'] = _TransmissionGateNPRatio
        _TransmissionGateinputs['_Dummy'] = _TransmissionGateDummy
        _TransmissionGateinputs['_VDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
        _TransmissionGateinputs['_SLVT'] = _TransmissionGateSLVT
        _TransmissionGateinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth
        _TransmissionGateinputs['_Gatereverse'] = False
        _TransmissionGateinputs['_Bodycontact'] = False

        self._DesignParameter['_TransmissionGateRB'] = self._SrefElementDeclaration(_DesignObj=TransmissionGate._TransmissionGate(_DesignParameter=None, _Name = 'TransmissionGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateinputs)


        print ('############################       Via for Digital input Generation       ################################')
        _ViaInputMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet12Met2OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaInputMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'] = []

        _ViaInputMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOX'] = 2
        _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet22Met3OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaInputMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnInput']['_XYCoordinates'] = []

        _ViaInputMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOX'] = 2
        _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet32Met4OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaInputMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnInput']['_XYCoordinates'] = []

        _ViaInputMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOX'] = 2
        _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet42Met5OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnInput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaInputMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'] = []


        print ('###############################       Opppcres_b Generation      #########################################')
        _Opppcresinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
        _Opppcresinputs['_ResWidth'] = _ResistorWidth
        _Opppcresinputs['_ResLength'] = _ResistorLength
        _Opppcresinputs['_CONUMX'] = _ResistorMetXCO
        _Opppcresinputs['_CONUMY'] = _ResistorMetYCO

        self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_DesignParameter=None, _Name = 'OpppcresIn{}'.format(_Name)))[0]
        self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateOpppcresDesignParameter(**_Opppcresinputs)


        print ('#################################       PSubring Generation      #########################################')
        _PMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _PMOSSubringinputs['_PType'] = False
        #if (_TransmissionGateFinger % 2 )
        _PMOSSubringinputs['_XWidth'] = ((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 + \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace2 + _DRCObj._Metal1MinSpace3)
        if (_TransmissionGateFinger == 1) :
            _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) 
        #    _DRCObj._Metal1MinSpace3 * 3 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        else :
            _PMOSSubringinputs['_YWidth'] = (_DRCObj._Metal1MinSpace3 + _DRCObj._Metal1MinSpace2 + _DRCObj._MetalxMinSpace8 +\
                                            #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 2 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
        # elif (_TransmissionGateChannelWidth * _TransmissionGateNPRatio > 700 and _TransmissionGateFinger == 1) :
        #     _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace3 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        # else :
        #     _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace2 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        _PMOSSubringinputs['_Width'] = _PMOSSubringWidth

        self._DesignParameter['_PMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name = 'PMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOSSubringRB']['_DesignObj']._CalculatePSubring(**_PMOSSubringinputs)

        _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _NMOSSubringinputs['_PType'] = True
        _NMOSSubringinputs['_XWidth'] = ((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 + \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace2 + _DRCObj._Metal1MinSpace3)

        if (_TransmissionGateFinger == 1) :
            _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) 
        #     _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        else :
            _NMOSSubringinputs['_YWidth'] = (_DRCObj._Metal1MinSpace3 * 2 + _DRCObj._Metal1MinSpace2 +\
                                            #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 2 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
        # elif (_TransmissionGateChannelWidth  > 700 and _TransmissionGateFinger == 1) :
        #     _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace3 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        # else :
        #     _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace2 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        _NMOSSubringinputs['_Width'] = _NMOSSubringWidth
        self._DesignParameter['_NMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='NMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOSSubringRB']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

        _TotalSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _TotalSubringinputs['_PType'] = True
        _TotalSubringinputs['_XWidth'] = _NMOSSubringinputs['_XWidth'] + _NMOSSubringinputs['_Width'] * 2 + _DRCObj._PpMinExtensiononPactive2 * 2+ \
                                        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + \
                                        _DRCObj._RXMinSpacetoPRES * 2 + _DRCObj._PpMinSpace
        #if (_TransmissionGateChannelWidth * _TransmissionGateNPRatio <= 700) :
        _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width']//2 + _PMOSSubringinputs['_Width']//2 + _DRCObj._Metal1MinSpace3 + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace,
                                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + _DRCObj._RXMinSpacetoPRES * 2)

        # else :
        #     _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width']//2 + _PMOSSubringinputs['_Width']//2 + _DRCObj._MetalxMinSpace10 * 2 + 2 + (_DRCObj._MetalxMinSpace8 - _DRCObj._Metal1MinSpace3),
        #                                      self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + _DRCObj._RXMinSpacetoPRES * 2)

        _TotalSubringinputs['_Width'] = _TotalSubringWidth

        self._DesignParameter['_TotalSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='TotalSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_TotalSubringRB']['_DesignObj']._CalculatePSubring(**_TotalSubringinputs)


        print ('#################################       Coordinates Settings      ########################################')

        ## Inverter and Transmission Gate Settings

        self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'] = [[0,0]]

        _VDD2VSSMinHeight = _NMOSSubringinputs['_Width'] * 1.5 + _NMOSSubringinputs['_YWidth'] + _DRCObj._Metal1MinSpace3 + _PMOSSubringinputs['_Width'] * 1.5 + _PMOSSubringinputs['_YWidth']
        if _VDD2VSSMinHeight % 2 == 1 :
            _VDD2VSSMinHeight += 1

        print ('@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@# SET MINIMUM HEIGHT VALUE FOR RESISTOR BANK : ', _VDD2VSSMinHeight)

        if _TransmissionGateVDD2VSSHeight != _VDD2VSSMinHeight :
            raise NotImplementedError

        if _TransmissionGateVDD2VSSHeight == None :
            raise NotImplementedError


        _GapBtwRL = abs(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 - 
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpace3))
        ## MOS  SUBRING  Settings
        #if (_TransmissionGateChannelWidth * _TransmissionGateNPRatio <= 700) :
        self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] - _GapBtwRL // 2,
                                                                      self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight - (_PMOSSubringinputs['_YWidth'])//2 - (_PMOSSubringinputs['_Width']) // 2]]

        # else : 
        #     self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] ,
        #                                                               self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight - (_PMOSSubringinputs['_YWidth'])//2 - (_PMOSSubringinputs['_Width']) // 2 + (_DRCObj._MetalxMinSpace8 - _DRCObj._Metal1MinSpace3)]]


        #if (_TransmissionGateChannelWidth * _TransmissionGateNPRatio <= 700) :
        self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + int(round(_NMOSSubringinputs['_YWidth'] + 0.5)) // 2 + _NMOSSubringinputs['_Width'] // 2]]

        # else :
        #     self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + (_NMOSSubringinputs['_YWidth']) // 2 + _NMOSSubringinputs['_Width'] // 2 - (_DRCObj._MetalxMinSpace8 - _DRCObj._Metal1MinSpace3 - 1)//2 + 1]]

        ##Total Guardring Settings
        self._DesignParameter['_TotalSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + _TotalSubringinputs['_XWidth'] // 2 - _GapBtwRL // 2 -
                                                                        (_PMOSSubringinputs['_XWidth']//2 +
                                                                        # + _TotalSubringinputs['_Width'] +
                                                                        max(_PMOSSubringinputs['_Width'] + _DRCObj._NwMinEnclosurePactive ,_NMOSSubringinputs['_Width'] + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace)),
                                                                       min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2,
                                                                           self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + int(round(_TotalSubringinputs['_YWidth'] + 0.5)) // 2 -
                                                                           (_NMOSSubringinputs['_Width']//2 + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace))]]

        ## Resistor Settings
        self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
            [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
             _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 +_DRCObj._RXMinSpacetoPRES +
             int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 0.5)) // 2,
             min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]

        ##Input Via Settings

        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0] -
                                                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._Metal1MinSpace2),
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0] -
                                                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._Metal1MinSpace2),
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_ViaMet22Met3OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']
        self._DesignParameter['_ViaMet32Met4OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']
        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']


        self._DesignParameter['_Met5LayerInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met5LayerInput']['_Width'] = self._DesignParameter['_ViaMet42Met5OnInput']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']
        self._DesignParameter['_Met5LayerInput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][1]]],
                                                                        [[self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][0],
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][1]],
                                                                        [self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][1]]]]

        print ('###############################       Additional Path Settings      ######################################')
        ##Additional NWell Generation
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_NWLayer']['_Width'] = _PMOSSubringinputs['_YWidth']
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
                                                                 self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] + _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]]]]


        ##Additional SLVT Generation
        # self._DesignParameter['_SLVTLayerPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
        if _TransmissionGateFinger == 1 or _TransmissionGateFinger == 2 :
            self._DesignParameter['_SLVTLayerNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_SLVTLayerNMOS']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']
            _LengthOfSLVT = _DRCObj._SlvtMinArea2 // self._DesignParameter['_SLVTLayerNMOS']['_Width'] + 2
            
            self._DesignParameter['_SLVTLayerNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] - _LengthOfSLVT // 2 - 1,
                                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]],
                                                                            [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] + _LengthOfSLVT // 2 + 1,
                                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]]]]
        
        if (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] *
            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']) < _DRCObj._SlvtMinArea2 :
            self._DesignParameter['_SLVTLayerPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_SLVTLayerPMOS']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']
            _LengthOfSLVT = _DRCObj._SlvtMinArea2 // self._DesignParameter['_SLVTLayerPMOS']['_Width'] + 2
            self._DesignParameter['_SLVTLayerPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] - _LengthOfSLVT // 2 - 1,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] + _LengthOfSLVT // 2 + 1,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]]]]
        # _GapBtwPMOS = abs(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1])
        # _GapBtwNMOS = abs(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1])
        # if _GapBtwPMOS % 2 == 1 :
        #     _GapBtwPMOS += 1
        # if _GapBtwNMOS % 2 == 1 :
        #     _GapBtwNMOS += 1
        #
        # self._DesignParameter['_SLVTLayerPMOS']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] + _GapBtwPMOS
        # self._DesignParameter['_SLVTLayerNMOS']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] + _GapBtwNMOS
        #
        # self._DesignParameter['_SLVTLayerPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                                self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']//2,
        #                                                                max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2],
        #                                                               [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                                max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2]]]
        #
        # self._DesignParameter['_SLVTLayerNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                                 self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                             max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1],
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]) - _GapBtwNMOS // 2],
        #                                                                 [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                             max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]) - _GapBtwNMOS // 2]]]
        #

        ##Additional BP Generation
        # self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_PPLayer']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _GapBtwPMOS
        # self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                         self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']//2,
        #                                                         max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2],
        #                                                         [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
        #                                                         max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2]]]


        #Additional Metal & Via Generation for Resistor
        _LengthOfAddMet1Y = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2 +
                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) * 2

        _NumViaMet12Met2COX = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
        _NumViaMet12Met2COY = _LengthOfAddMet1Y // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)

        _CONUMXmax = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        _CONUMYmax = int((int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_OPLayer']['_YWidth'] - 2*_DRCObj._CoMinSpace2OP - 2*_DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1) / 2)

        if _ResistorMetXCO == None :
            _ResistorMetXCO = _CONUMXmax
        if _ResistorMetYCO == None :
            _ResistorMetYCO = _CONUMYmax
        _ViaResMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ResistorMetYCO

        _Resport1 = [[self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0][i] + 
                    self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][i] for i in range (len(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0]))]]
        _Resport2 = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]]]
        
        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates']
        self._DesignParameter['_ViaMet12Met2OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaResMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'] = _Resport2 + _Resport1
        
                                                                        # [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - 
                                                                        #   _TotalSubringinputs['_YWidth']//2 + 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 + _DRCObj._MetalxMinSpace9],
                                                                        #  [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + 
                                                                        #   _TotalSubringinputs['_YWidth']//2 - 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 - _DRCObj._MetalxMinSpace9]]
                                                                        ## [0] - Downward, [1] - Upward

        _ViaResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ResistorMetYCO

        self._DesignParameter['_ViaMet22Met3OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnRes']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaResMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'] = _Resport2 + _Resport1

        _ViaResMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ResistorMetYCO

        self._DesignParameter['_ViaMet32Met4OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaMet32Met4OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaResMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'] = _Resport1
        
                                                                        # [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - 
                                                                        #   _TotalSubringinputs['_YWidth']//2 + 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 + _DRCObj._MetalxMinSpace9]]

        _ViaResMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ResistorMetYCO

        self._DesignParameter['_ViaMet42Met5OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaMet42Met5OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnRes']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaResMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnRes']['_XYCoordinates'] = _Resport1

        _ViaResMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaResMet52Met6['_ViaMet52Met6NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet52Met6['_ViaMet52Met6NumberOfCOY'] = _ResistorMetYCO

        self._DesignParameter['_ViaMet52Met6OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None,_Name='ViaMet52Met6OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaResMet52Met6)
        self._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'] = _Resport1

        _ViaResMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaResMet62Met7['_ViaMet62Met7NumberOfCOX'] = _ResistorMetXCO
        _ViaResMet62Met7['_ViaMet62Met7NumberOfCOY'] = _ResistorMetYCO

        self._DesignParameter['_ViaMet62Met7OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None,_Name='ViaMet62Met7OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnRes']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaResMet62Met7)
        self._DesignParameter['_ViaMet62Met7OnRes']['_XYCoordinates'] = []


        ##Metal Generation for Input metal 1 
        self._DesignParameter['_Met1LayerInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met1LayerInput']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_Met1LayerInput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][0] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]],
                                                                    [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]]],
                                                                    [[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][0] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]],
                                                                    [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]]]]


        ## Metal Generation for VCM
        self._DesignParameter['_Met2LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met2LayerVCM']['_XWidth'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['_Met2LayerVCM']['_YWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_XYCoordinates'][0][1] -
                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][0][1]) + \
                                                            (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] +
                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) // 2
        # tmp = []
        # for i in range (0, len(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter[''])) :
        #     tmp.append([self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][i][0] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] // 2 +
        #                 self._DesignParameter['_Met2LayerVCM']['_XWidth'] // 2,
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][i][1] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 +
        #                 self._DesignParameter['_Met2LayerVCM']['_YWidth'] // 2])


        tmp1 = copy.deepcopy(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'])
        tmp2 = copy.deepcopy(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'])

        for i in tmp2 :
            if i in tmp1 : 
                tmp1.remove(i)
        
        for i in range(0, len(tmp1)) :
            tmp1[i][1] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][0][1] - \
                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + \
                         self._DesignParameter['_Met2LayerVCM']['_YWidth'] // 2
        

        self._DesignParameter['_Met2LayerVCM']['_XYCoordinates'] = tmp1
        
        
        _ViaVCMMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVCMMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
        _ViaVCMMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1])//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

        tmp = []

        self._DesignParameter['_ViaVCMMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaVCMMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaVCMMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaVCMMet22Met3)
        
        for i in range (0, len(tmp1)) :
            tmp.append([tmp1[i][0],
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]) // 2])

        self._DesignParameter['_ViaVCMMet22Met3']['_XYCoordinates'] = tmp

        del tmp

        _ViaVCMMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOX'] = 1
        _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1])//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

        tmp = []

        self._DesignParameter['_ViaVCMMet32Met4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaVCMMet32Met4In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaVCMMet32Met4)
        
        for i in range (0, len(tmp1)) :
            tmp.append([tmp1[i][0],
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]) // 2])

        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'] = tmp

        del tmp



        self._DesignParameter['_Met4LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met4LayerVCM']['_XWidth'] = self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][0]
        self._DesignParameter['_Met4LayerVCM']['_YWidth'] = self._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
        k = len(self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'])
        if k % 2 == 1 :
            self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = [[self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2][0],
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][1]]]

        else :
            self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = [[self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2 - 1][0] + 
                                                                        int(round((self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2][0] -
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2 - 1][0])+0.5)) // 2,
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][1]]]

        del k
        # self._DesignParameter['_Met6LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        # self._DesignParameter['_Met6LayerVCM']['_XWidth'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
        # self._DesignParameter['_Met6LayerVCM']['_YWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'][0][1] -
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][0][1]) + \
        #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] +
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) // 2
        
        # tmp = []
        # for i in range (0, len(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'])) :
        #     tmp.append([self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][i][0] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 +
        #                 self._DesignParameter['_Met4LayerVCM']['_XWidth'] // 2,
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][i][1] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 +
        #                 self._DesignParameter['_Met4LayerVCM']['_YWidth'] // 2])

        # self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'] = tmp

        # self._DesignParameter['_Met7LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        # self._DesignParameter['_Met7LayerVCM']['_XWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][-1][0] -
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][0][0]) + \
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
        # self._DesignParameter['_Met7LayerVCM']['_YWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'][0][1] -
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][0][1]) + \
        #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] +
        #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) // 2
        
        # self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][0][0] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 +
        #                 self._DesignParameter['_Met7LayerVCM']['_XWidth'] // 2,
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'][0][1] -
        #                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 +
        #                 self._DesignParameter['_Met7LayerVCM']['_YWidth'] // 2]]



        

        # _ViaVCMMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        # _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Met5LayerVCM']['_XWidth']//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
        # _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] = int(self._DesignParameter['_Met5LayerVCM']['_YWidth']//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 1

        # self._DesignParameter['_ViaVCMMet52Met6'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None,_Name='ViaVCMMet52Met6In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaVCMMet52Met6']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVCMMet52Met6)
        # self._DesignParameter['_ViaVCMMet52Met6']['_XYCoordinates'] = []

        # _ViaVCMMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        # _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] = int(self._DesignParameter['_Met6LayerVCM']['_XWidth']//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
        # if _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] < 1 :
        #     _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
        # _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOY'] = int(self._DesignParameter['_Met6LayerVCM']['_YWidth']//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 1

        # self._DesignParameter['_ViaVCMMet62Met7'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None,_Name='ViaVCMMet62Met7In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaVCMMet62Met7']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVCMMet62Met7)
        # self._DesignParameter['_ViaVCMMet62Met7']['_XYCoordinates'] = self._DesignParameter['_Met6LayerVCM']['_XYCoordinates']

        # _ViaVCMMet72Met8 = copy.deepcopy(ViaMet72Met8._ViaMet72Met8._ParametersForDesignCalculation)
        # _ViaVCMMet72Met8['_ViaMet72Met8NumberOfCOX'] = int(self._DesignParameter['_Met7LayerVCM']['_XWidth']//(_DRCObj._VIAzMinSpace + _DRCObj._VIAzMinWidth))
        # if _ViaVCMMet72Met8['_ViaMet72Met8NumberOfCOX'] < 1 :
        #     _ViaVCMMet72Met8['_ViaMet72Met8NumberOfCOX'] = 1
        # _ViaVCMMet72Met8['_ViaMet72Met8NumberOfCOY'] = int(self._DesignParameter['_Met7LayerVCM']['_YWidth']//(_DRCObj._VIAzMinSpace + _DRCObj._VIAzMinWidth)) + 1

        # self._DesignParameter['_ViaVCMMet72Met8'] = self._SrefElementDeclaration(_DesignObj=ViaMet72Met8._ViaMet72Met8(_DesignParameter=None,_Name='ViaVCMMet72Met8In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaVCMMet72Met8']['_DesignObj']._CalculateViaMet72Met8DesignParameterMinimumEnclosureX(**_ViaVCMMet72Met8)
        # self._DesignParameter['_ViaVCMMet72Met8']['_XYCoordinates'] = self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']

        # self._DesignParameter['_Met7LayerVCM']['_YWidth'] = self._DesignParameter['_ViaVCMMet72Met8']['_DesignObj']._DesignParameter['_Met7Layer']['_YWidth']
        # self._DesignParameter['_ViaVCMMet72Met8']['_DesignObj']._DesignParameter['_Met8Layer']['_XWidth'] = self._DesignParameter['_Met7LayerVCM']['_XWidth']

        # _ViaVCMMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        # _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOX'] = 2
        # _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1

        # self._DesignParameter['_ViaVCMMet32Met4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaVCMMet32Met4In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVCMMet32Met4)
        # self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][1][1]],
        #                                                                 [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'][0][1][1]]]

        


        ##Metal align for Resistor
        self._DesignParameter['_Met1LayerRes'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met1LayerRes']['_Width'] = self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        self._DesignParameter['_Met1LayerRes']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][1]],
                                                                    [self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 ]],
                                                                    [[self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][1][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][1][1]],
                                                                    [self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][1][0],
                                                                    self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 ]]]
                                                                    

        self._DesignParameter['_Met3LayerPMOSResAX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
        
                                                            # (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] - 
                                                            # self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][1] 
                                                            # - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + 
                                                            # (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)//4- _DRCObj._MetalxMinSpace21) - \
                                                            # (self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1] + 
                                                            # self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + _DRCObj._MetalxMinSpace11)


                                                      #   min(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1],
                                                      # (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
                                                      # self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 -
                                                      # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) -
                                                      # self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1])
        # if (_TransmissionGateFinger != 1) :
        self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] +
                                                                       self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]]]]
            
                                                                    # [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
                                                                    #    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
                                                                    #    self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1] +
                                                                    #    self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + _DRCObj._MetalxMinSpace11 + 
                                                                    #    self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2 ],
                                                                    #   [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] +
                                                                    #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                    #   self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1] +
                                                                    #   self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + _DRCObj._MetalxMinSpace11 + 
                                                                    #    self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2 ]]]

        self._DesignParameter['_Met3LayerNMOSResAX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
        self._DesignParameter['_Met3LayerNMOSResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                       self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + 
                                                                       self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]]]]

        _ViaTGPMOS2ResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int(_PMOSSubringinputs['_Width'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) 
        _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] < 1 :
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
        if _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] < 1 :
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_ViaTGPMOS2ResMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaTGPMOS2ResMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaTGPMOS2ResMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaTGPMOS2ResMet22Met3)
        self._DesignParameter['_ViaTGPMOS2ResMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                            self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'][0][0][1]]]

        _ViaTGNMOS2ResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int(_NMOSSubringinputs['_Width'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) 
        _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] < 1 :
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
        if _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] < 1 :
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_ViaTGNMOS2ResMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaTGNMOS2ResMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaTGNMOS2ResMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaTGNMOS2ResMet22Met3)
        self._DesignParameter['_ViaTGNMOS2ResMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                            self._DesignParameter['_Met3LayerNMOSResAX']['_XYCoordinates'][0][0][1]]]


        self._DesignParameter['_Met2LayerResYX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2LayerResYX']['_Width'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met2LayerResYX']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2],
                                                                    [self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_Met3LayerNMOSResAX']['_XYCoordinates'][0][0][1] - self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] // 2]]]

        
        
        # elif (_TransmissionGateFinger == 1) :
        #     self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
        #                                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'][0][0][0],
        #                                                                self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1] +
        #                                                                self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + _DRCObj._MetalxMinSpace11 + 
        #                                                                self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2 ],
        #                                                               [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] +
        #                                                               self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
        #                                                               self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1] +
        #                                                               self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 + _DRCObj._MetalxMinSpace11 + 
        #                                                                self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2 ]]]


        # self._DesignParameter['_Met3LayerResAY'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_Met3LayerResAY']['_Width'] = self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        # self._DesignParameter['_Met3LayerResAY']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][1]],
        #                                                                [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'][0][0][1]]]]

        # self._DesignParameter['_Met4LayerResBY'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_Met4LayerResBY']['_Width'] = self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
        # self._DesignParameter['_Met4LayerResBY']['_XYCoordinates'] = []
        # self._DesignParameter['_Met4LayerResBY']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][1]],
        #                                                                 [self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'][0][0],
        #                                                                 self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1]
        #                                                                 + _DRCObj._MetalxMinSpace9]]]
        _LengthYbtwGuardring = abs((abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1]) -
                                            abs(self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) - \
                                            (abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1]) -
                                            abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]))) \
                                            + _NMOSSubringinputs['_Width'] // 2 + _TotalSubringinputs['_Width'] // 2

        _LengthOfPMOSRouting = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] + 
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2) - \
                                            (self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] - (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_YWidth'] // 2))
        
        self._DesignParameter['_Met1LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met1LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met1LayerVSS']['_YWidth'] = _LengthYbtwGuardring
        self._DesignParameter['_Met1LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                                abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                                    abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                                int(round(_LengthYbtwGuardring + 0.5)) // 2 + _NMOSSubringinputs['_Width'] // 2]]


        ##VDD and VSS VIA Generation.. (Make Metals first and then via)
        if _PowerLine == True :
            self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met5LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met6LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)            
            self._DesignParameter['_Met3LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met5LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met6LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            
            
            

            self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met2LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
                                                                        # (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2) + self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        # self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                        # _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
            self._DesignParameter['_Met3LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            self._DesignParameter['_Met3LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = []
            
            
                                                                        # [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
                                                                        # (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2) + self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        # self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                        # _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
                                                                        # [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                        # self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                        # _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]

                                                                        
            # self._DesignParameter['_Met4LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2
            # self._DesignParameter['_Met4LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2) + self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
            #                                                             _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
            # self._DesignParameter['_Met4LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met4LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
            #                                                             _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
            
            
            # self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met2LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_YWidth'] - _LengthOfPMOSRouting - _DRCObj._MetalxMinSpace5
            # self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - 
            #                                                             (_PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] + (_LengthOfPMOSRouting + _DRCObj._MetalxMinSpace5) // 2]]
            # self._DesignParameter['_Met3LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met3LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_YWidth']
            # self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - 
            #                                                             (_PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]]]
            # self._DesignParameter['_Met4LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met4LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_YWidth']
            # self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - 
            #                                                             (_PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]]]


            
            # self._DesignParameter['_Met5LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met5LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
            #                                                             self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
            #                                                             _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
            # self._DesignParameter['_Met6LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met6LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            # self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
            #                                                         self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
            #                                                         _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]

            #if (_TransmissionGateChannelWidth * _TransmissionGateNPRatio <= 700) :
            
                
                # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                #                                                             abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                #                                                                 abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                #                                                             _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            self._DesignParameter['_Met2LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met2LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            self._DesignParameter['_Met3LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met3LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            self._DesignParameter['_Met4LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2 
            self._DesignParameter['_Met4LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            # self._DesignParameter['_Met2LayerVSS']['_XWidth'] = _TotalSubringinputs['_Width']
            # self._DesignParameter['_Met2LayerVSS']['_YWidth'] = (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_Width'] + _TotalSubringinputs['_YWidth'] // 2) - \
            #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 +
            #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace5)
            # self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_TotalSubringinputs['_Width'] // 2 + _TotalSubringinputs['_XWidth'] // 2),
            #                                                             (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_Width'] + _TotalSubringinputs['_YWidth'] // 2) -
            #                                                             self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2]]


            # self._DesignParameter['_Met2LayerVSS1']['_XWidth'] = _TotalSubringinputs['_Width']
            # self._DesignParameter['_Met2LayerVSS1']['_YWidth'] = abs((self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - _TotalSubringinputs['_Width'] - _TotalSubringinputs['_YWidth'] // 2) - \
            #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] - 
            #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 -
            #                                                     _DRCObj._MetalxMinSpace5))
            # self._DesignParameter['_Met2LayerVSS1']['_XYCoordinates'] = [[self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_TotalSubringinputs['_Width'] // 2 + _TotalSubringinputs['_XWidth'] // 2),
            #                                                             (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - _TotalSubringinputs['_Width'] - _TotalSubringinputs['_YWidth'] // 2) + self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // 2]]


            # self._DesignParameter['_Met3LayerVSS']['_XWidth'] = _TotalSubringinputs['_Width']
            # self._DesignParameter['_Met3LayerVSS']['_YWidth'] = (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_Width'] + _TotalSubringinputs['_YWidth'] // 2) - \
            #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 +
            #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace5)
            # self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_TotalSubringinputs['_Width'] // 2 + _TotalSubringinputs['_XWidth'] // 2),
            #                                                             (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_Width'] + _TotalSubringinputs['_YWidth'] // 2) -
            #                                                             self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2]]


            # self._DesignParameter['_Met3LayerVSS1']['_XWidth'] = _TotalSubringinputs['_Width']
            # self._DesignParameter['_Met3LayerVSS1']['_YWidth'] = abs((self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - _TotalSubringinputs['_Width'] - _TotalSubringinputs['_YWidth'] // 2) - \
            #                                                     (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] - 
            #                                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 -
            #                                                     _DRCObj._MetalxMinSpace5))
            # self._DesignParameter['_Met3LayerVSS1']['_XYCoordinates'] = [[self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_TotalSubringinputs['_Width'] // 2 + _TotalSubringinputs['_XWidth'] // 2),
            #                                                             (self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - _TotalSubringinputs['_Width'] - _TotalSubringinputs['_YWidth'] // 2) + self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // 2]]

            # self._DesignParameter['_Met4LayerVSS']['_XWidth'] = _TotalSubringinputs['_Width']
            # self._DesignParameter['_Met4LayerVSS']['_YWidth'] = _TotalSubringinputs['_Width'] * 2 + _TotalSubringinputs['_YWidth']
            # self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
            #                                                             (_TotalSubringinputs['_Width'] // 2 + _TotalSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1]]]

            
            # self._DesignParameter['_Met2LayerVSS2']['_XWidth'] = _NMOSSubringinputs['_Width']
            # self._DesignParameter['_Met2LayerVSS2']['_YWidth'] = _LengthYbtwGuardring
            # self._DesignParameter['_Met2LayerVSS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
            #                                                             (_NMOSSubringinputs['_Width'] // 2 + _NMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] -
            #                                                             (_TotalSubringinputs['_Width']+ _TotalSubringinputs['_YWidth'] // 2) + _LengthYbtwGuardring // 2]]

            # self._DesignParameter['_Met3LayerVSS2']['_XWidth'] = _NMOSSubringinputs['_Width']
            # self._DesignParameter['_Met3LayerVSS2']['_YWidth'] = _LengthYbtwGuardring
            # self._DesignParameter['_Met3LayerVSS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
            #                                                             (_NMOSSubringinputs['_Width'] // 2 + _NMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] -
            #                                                             (_TotalSubringinputs['_Width']+ _TotalSubringinputs['_YWidth'] // 2) + _LengthYbtwGuardring // 2]]

            # self._DesignParameter['_Met4LayerVSS2']['_XWidth'] = _NMOSSubringinputs['_Width']
            # self._DesignParameter['_Met4LayerVSS2']['_YWidth'] = _LengthYbtwGuardring
            # self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
            #                                                             (_NMOSSubringinputs['_Width'] // 2 + _NMOSSubringinputs['_XWidth'] // 2),
            #                                                             self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] -
            #                                                             (_TotalSubringinputs['_Width'] + _TotalSubringinputs['_YWidth'] // 2) + _LengthYbtwGuardring // 2]]

            # self._DesignParameter['_Met5LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met5LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            # self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
            #                                                                 abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
            #                                                                     abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
            #                                                                 _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            # self._DesignParameter['_Met6LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met6LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            # self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
            #                                                                 abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
            #                                                                     abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
            #                                                                 _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            

            #Via Generations
            _NumViaVDDCOX = int(self._DesignParameter['_Met2LayerVDD']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVDDCOX == 0 :
                _NumViaVDDCOX = 1
            _NumViaVDDCOY = int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVDDCOY == 0 :
                _NumViaVDDCOY = 1
            _NumViaVSSCOX = int(self._DesignParameter['_Met2LayerVSS']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSSCOX == 0 :
                _NumViaVSSCOX = 1
            _NumViaVSSCOY = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSSCOY == 0 :
                _NumViaVSSCOY = 1

            _NumViaVSS2COX = int(self._DesignParameter['_Met2LayerVSS2']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSS2COX == 0 :
                _NumViaVSS2COX = 1
            _NumViaVSS2COY = int(self._DesignParameter['_Met2LayerVSS2']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSS2COY == 0 :
                _NumViaVSS2COY = 1
            
            
            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet12Met21 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met21['_ViaMet12Met2NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet12Met21['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet22Met31 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet32Met41 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVSSCOY
            _ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVSSCOY

            _ViaVSS2Met12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSS2Met12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaVSS2COY
            _ViaVSS2Met22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSS2Met22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaVSS2COY
            _ViaVSS2Met32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSS2Met32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVSS2COY
            

            self._DesignParameter['_ViaMet12Met2OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnVDD']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2OnVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]
                                                                            + self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1]]]

            self._DesignParameter['_ViaMet22Met3OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnVDD']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3OnVDD']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnVDD']['_XYCoordinates']
            
            self._DesignParameter['_ViaMet32Met4OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVDDMet32Met4)
            self._DesignParameter['_ViaMet32Met4OnVDD']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet42Met5OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5OnVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVDDMet42Met5)
            self._DesignParameter['_ViaMet42Met5OnVDD']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet52Met6OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet52Met6OnVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVDDMet52Met6)
            self._DesignParameter['_ViaMet52Met6OnVDD']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet12Met2OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnVSS']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met2)
            self._DesignParameter['_ViaMet12Met2OnVSS']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet22Met3OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met3)
            self._DesignParameter['_ViaMet22Met3OnVSS']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet32Met4OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met4)
            self._DesignParameter['_ViaMet32Met4OnVSS']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet32Met4OnVSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met41OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnVSS1']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met41)
            self._DesignParameter['_ViaMet32Met4OnVSS1']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet12Met2OnVSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnVSS1In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnVSS1']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met21)
            self._DesignParameter['_ViaMet12Met2OnVSS1']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet22Met3OnVSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVSS1In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnVSS1']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met31)
            self._DesignParameter['_ViaMet22Met3OnVSS1']['_XYCoordinates'] = []
            self._DesignParameter['_ViaMet12Met2OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnVSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnVSS2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSS2Met12Met2)
            self._DesignParameter['_ViaMet12Met2OnVSS2']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet22Met3OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnVSS2']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSS2Met22Met3)
            self._DesignParameter['_ViaMet22Met3OnVSS2']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet32Met4OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnVSS2']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSS2Met32Met4)
            self._DesignParameter['_ViaMet32Met4OnVSS2']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet42Met5OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5OnVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met5)
            self._DesignParameter['_ViaMet42Met5OnVSS']['_XYCoordinates'] = []

            self._DesignParameter['_ViaMet52Met6OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet52Met6OnVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVSSMet52Met6)
            self._DesignParameter['_ViaMet52Met6OnVSS']['_XYCoordinates'] = []


if __name__ == '__main__' :


    # _InverterFinger = 2
    # _InverterChannelWidth = 200
    # _InverterChannelLength = 30
    # _InverterNPRatio = 2
    # _InverterDummy = True    #T/F?
    # _InverterVDD2VSSHeight = 2252 ## SHOULD BE FIXED OVER MIN VALUE
    # _InverterSLVT = True     #T/F?

    _TransmissionGateFinger = 2
    _TransmissionGateChannelWidth = 275
    _TransmissionGateChannelLength = 30
    _TransmissionGateNPRatio = 2
    _TransmissionGateDummy = True     #T/F?
    _TransmissionGateVDD2VSSHeight = 2426 ## FIXED
    _TransmissionGateSLVT = True     #T/F?

    _PowerLine = True

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

    ResistorBankObj = _ResistorBank(_DesignParameter=None, _Name='ResistorBank')
    #print ("A!!")
    ResistorBankObj._CalculateResistorBank(
                               #  _InverterFinger=_InverterFinger, _InverterChannelWidth=_InverterChannelWidth, _InverterChannelLength=_InverterChannelLength, _InverterNPRatio=_InverterNPRatio, _InverterDummy = _InverterDummy,
                               # _InverterVDD2VSSHeight=_InverterVDD2VSSHeight, _InverterSLVT = _InverterSLVT,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                               _TransmissionGateFinger =_TransmissionGateFinger, _TransmissionGateChannelWidth = _TransmissionGateChannelWidth, _TransmissionGateChannelLength = _TransmissionGateChannelLength, _TransmissionGateNPRatio =_TransmissionGateNPRatio,
                               _TransmissionGateDummy = _TransmissionGateDummy , _TransmissionGateVDD2VSSHeight = _TransmissionGateVDD2VSSHeight, _TransmissionGateSLVT = _TransmissionGateSLVT,
                               _PowerLine = _PowerLine,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO = _ResistorMetXCO, _ResistorMetYCO = _ResistorMetYCO,
                                _PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth,_PMOSSubringWidth=_PMOSSubringWidth,
                                _NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth,_NMOSSubringWidth=_NMOSSubringWidth,
                                _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth)


    ResistorBankObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ResistorBankObj._DesignParameter)
    _fileName = 'ResistorBank.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = ResistorBankObj._CreateGDSStream(ResistorBankObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')


    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('ResistorBank.gds', 'rb')
    ftp.storbinary('STOR ResistorBank.gds', myfile)
    myfile.close()
    ftp.close()

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('ResistorBank.gds', 'rb')
    ftp.storbinary('STOR ResistorBank.gds', myfile)
    myfile.close()
    ftp.close()


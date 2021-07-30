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
import Full_ResistorBank
import SlicerWithSRLatchX4
import math

class _SlicerandSRLatchwtResistor (StickDiagram._StickDiagram) :

    _ParametersForDesignCalculation = dict(
                                    _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None,
                                  _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, _SRNumViaPoly2Met1CoX = None, \
                                  _SRNumViaPoly2Met1CoY = None, _SRNumViaPMOSMet12Met2CoX = None, _SRNumViaPMOSMet12Met2CoY = None, \
                                  _SRNumViaNMOSMet12Met2CoX = None, _SRNumViaNMOSMet12Met2CoY = None, _SRNumViaPMOSMet22Met3CoX = None, _SRNumViaPMOSMet22Met3CoY = None, \
                                  _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine=None, _NumberofSlicerWithSRLatch = None, \
                                    _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
                                     _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
                                    _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                    _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                    _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                    _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None,
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

    def __init__(self, _DesignParameter=None, _Name='SlicerandSRLatchwtResistor'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateDesignParameter(self, _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                    _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None, _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                    _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                    _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, _SRNumViaPoly2Met1CoX = None, \
                                    _SRNumViaPoly2Met1CoY = None, _SRNumViaPMOSMet12Met2CoX = None, _SRNumViaPMOSMet12Met2CoY = None, \
                                    _SRNumViaNMOSMet12Met2CoX = None, _SRNumViaNMOSMet12Met2CoY = None, _SRNumViaPMOSMet22Met3CoX = None, _SRNumViaPMOSMet22Met3CoY = None, \
                                    _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                    _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False, _NumberofSlicerWithSRLatch = None, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
                                  _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
                                  _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None,
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
        print ('                           {}  SlicerandSRLatchwtResistor Calculation Start                              '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'SlicerandSRLatchwtResistor'

        print ('###############################      ResistorBank Generation     #########################################')

        _FRBinputs = copy.deepcopy(Full_ResistorBank._FullResistorBank._ParametersForDesignCalculation)
        _FRBinputs['_XRBNum'] = _XRBNum
        _FRBinputs['_YRBNum'] = _YRBNum

        _FRBinputs['_TransmissionGateFinger'] = _TransmissionGateFinger
        _FRBinputs['_TransmissionGateChannelWidth'] = _TransmissionGateChannelWidth
        _FRBinputs['_TransmissionGateChannelLength'] = _TransmissionGateChannelLength
        _FRBinputs['_TransmissionGateNPRatio'] = _TransmissionGateNPRatio
        _FRBinputs['_TransmissionGateDummy'] = _TransmissionGateDummy
        _FRBinputs['_TransmissionGateVDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
        _FRBinputs['_TransmissionGateSLVT'] = _TransmissionGateSLVT
        _FRBinputs['_PowerLine'] = _PowerLine

        _FRBinputs['_ResistorWidth'] = _ResistorWidth
        _FRBinputs['_ResistorLength'] = _ResistorLength
        _FRBinputs['_ResistorMetXCO'] = _ResistorMetXCO
        _FRBinputs['_ResistorMetYCO'] = _ResistorMetYCO

        _FRBinputs['_PMOSSubringType'] = _PMOSSubringType
        _FRBinputs['_PMOSSubringXWidth'] = _PMOSSubringXWidth
        _FRBinputs['_PMOSSubringYWidth'] = _PMOSSubringYWidth
        _FRBinputs['_PMOSSubringWidth'] = _PMOSSubringWidth

        _FRBinputs['_NMOSSubringType'] = _NMOSSubringType
        _FRBinputs['_NMOSSubringXWidth'] = _NMOSSubringXWidth
        _FRBinputs['_NMOSSubringYWidth'] = _NMOSSubringYWidth
        _FRBinputs['_NMOSSubringWidth'] = _NMOSSubringWidth

        _FRBinputs['_TotalSubringType'] = _TotalSubringType
        _FRBinputs['_TotalSubringXWidth'] = _TotalSubringXWidth
        _FRBinputs['_TotalSubringYWidth'] = _TotalSubringYWidth
        _FRBinputs['_TotalSubringWidth'] = _TotalSubringWidth

        self._DesignParameter['_FRB'] = self._SrefElementDeclaration(_DesignObj=Full_ResistorBank._FullResistorBank(_DesignParameter=None,_Name='ResistorBankIn{}'.format(_Name)))[0]
        self._DesignParameter['_FRB']['_DesignObj']._CalculateFullResistorBank(**_FRBinputs)

        
        print ('###########################      SlicerWithSRLatch Generation     ####################################')


        _SlicerWithSRLatchEdgeinputs = copy.deepcopy(SlicerWithSRLatchX4.SlicerWithSRLatchX4Obj._ParametersForDesignCalculation)
        _SlicerWithSRLatchEdgeinputs['_SRFinger1'] = _SRFinger1
        _SlicerWithSRLatchEdgeinputs['_SRFinger2'] = _SRFinger2
        _SlicerWithSRLatchEdgeinputs['_SRFinger3'] = _SRFinger3
        _SlicerWithSRLatchEdgeinputs['_SRFinger4'] = _SRFinger4
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth1'] = _SRNMOSChannelWidth1
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth1'] = _SRPMOSChannelWidth1
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth2'] = _SRNMOSChannelWidth2
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth2'] = _SRPMOSChannelWidth2
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth3'] = _SRNMOSChannelWidth3
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth3'] = _SRPMOSChannelWidth3
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth4'] = _SRNMOSChannelWidth4
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth4'] = _SRPMOSChannelWidth4
        _SlicerWithSRLatchEdgeinputs['_SRChannelLength'] = _SRChannelLength
        _SlicerWithSRLatchEdgeinputs['_SRNPRatio'] = _SRNPRatio
        _SlicerWithSRLatchEdgeinputs['_SRVDD2VSSHeightAtOneSide'] = _SRVDD2VSSHeightAtOneSide
        _SlicerWithSRLatchEdgeinputs['_SRDummy'] = _SRDummy
        _SlicerWithSRLatchEdgeinputs['_SRNumSupplyCoX'] = _SRNumSupplyCoX
        _SlicerWithSRLatchEdgeinputs['_SRNumSupplyCoY'] = _SRNumSupplyCoY
        _SlicerWithSRLatchEdgeinputs['_SRSupplyMet1XWidth'] = _SRSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_SRSupplyMet1YWidth'] = _SRSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPoly2Met1CoX'] = _SRNumViaPoly2Met1CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPoly2Met1CoY'] = _SRNumViaPoly2Met1CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet12Met2CoX'] = _SRNumViaPMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet12Met2CoY'] = _SRNumViaPMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet12Met2CoX'] = _SRNumViaNMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet12Met2CoY'] = _SRNumViaNMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet22Met3CoX'] = _SRNumViaPMOSMet22Met3CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet22Met3CoY'] = _SRNumViaPMOSMet22Met3CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet22Met3CoX'] = _SRNumViaNMOSMet22Met3CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet22Met3CoY'] = _SRNumViaNMOSMet22Met3CoY
        _SlicerWithSRLatchEdgeinputs['_SRSLVT'] = _SRSLVT
        _SlicerWithSRLatchEdgeinputs['_SRPowerLine'] = _SRPowerLine

        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2
        _SlicerWithSRLatchEdgeinputs['_SLPMOSFinger'] = _SLPMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLPMOSChannelWidth'] = _SLPMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLDATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSFinger'] = _SLNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSChannelWidth'] = _SLNMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLChannelLength'] = _SLChannelLength
        _SlicerWithSRLatchEdgeinputs['_SLDummy'] = _SLDummy
        _SlicerWithSRLatchEdgeinputs['_SLSLVT'] = _SLSLVT
        _SlicerWithSRLatchEdgeinputs['_SLGuardringWidth'] = _SLGuardringWidth
        _SlicerWithSRLatchEdgeinputs['_SLGuardring'] = _SLGuardring
        _SlicerWithSRLatchEdgeinputs['_SLSlicerGuardringWidth'] = _SLSlicerGuardringWidth
        _SlicerWithSRLatchEdgeinputs['_SLSlicerGuardring'] = _SLSlicerGuardring
        _SlicerWithSRLatchEdgeinputs['_SLNumSupplyCOX'] = _SLNumSupplyCOX
        _SlicerWithSRLatchEdgeinputs['_SLNumSupplyCOY'] = _SLNumSupplyCOY
        _SlicerWithSRLatchEdgeinputs['_SLSupplyMet1XWidth'] = _SLSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_SLSupplyMet1YWidth'] = _SLSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_SLVDD2VSSHeight'] = _SLVDD2VSSHeight
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAPoly2Met1COX'] = _SLNumVIAPoly2Met1COX
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAPoly2Met1COY'] = _SLNumVIAPoly2Met1COY
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COX
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COY
        _SlicerWithSRLatchEdgeinputs['_SLPowerLine'] = _SLPowerLine

        _SlicerWithSRLatchEdgeinputs['_NumberofSlicerWithSRLatch'] = _NumberofSlicerWithSRLatch
        _SlicerWithSRLatchEdgeinputs['_InvFinger'] = _InvFinger
        _SlicerWithSRLatchEdgeinputs['_InvChannelWidth'] = _InvChannelWidth
        _SlicerWithSRLatchEdgeinputs['_InvChannelLength'] = _InvChannelLength
        _SlicerWithSRLatchEdgeinputs['_InvNPRatio'] = _InvNPRatio
        _SlicerWithSRLatchEdgeinputs['_InvVDD2VSSHeight'] = _InvVDD2VSSHeight
        _SlicerWithSRLatchEdgeinputs['_InvDummy'] = _InvDummy
        _SlicerWithSRLatchEdgeinputs['_InvNumSupplyCoX'] = _InvNumSupplyCoX
        _SlicerWithSRLatchEdgeinputs['_InvNumSupplyCoY'] = _InvNumSupplyCoY
        _SlicerWithSRLatchEdgeinputs['_InvSupplyMet1XWidth'] = _InvSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_InvSupplyMet1YWidth'] = _InvSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPoly2Met1CoX'] = _InvNumViaPoly2Met1CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPoly2Met1CoY'] = _InvNumViaPoly2Met1CoY
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPMOSMet12Met2CoX'] = _InvNumViaPMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPMOSMet12Met2CoY'] = _InvNumViaPMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_InvNumViaNMOSMet12Met2CoX'] = _InvNumViaNMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaNMOSMet12Met2CoY'] = _InvNumViaNMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_InvSLVT'] = _InvSLVT
        _SlicerWithSRLatchEdgeinputs['_InvPowerLine'] = _InvPowerLine
        _SlicerWithSRLatchEdgeinputs['_SLSRInvSupplyLineX4'] = _SLSRInvSupplyLineX4



        self._DesignParameter['_Slicer'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatchX4.SlicerWithSRLatchX4Obj(_DesignParameter=None, _Name = "SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_Slicer']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchEdgeinputs)


        _ViaVRXMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = 2
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet52Met6OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVRXMet52Met6)


        print ('#################################       Coordinates Settings      ########################################')

        _ResistorBankOrigin  = [[0,0]]
        self._DesignParameter['_FRB']['_XYCoordinates'] = _ResistorBankOrigin

        _CenterofVRX = (self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1] +  
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1]) // 2

        self._DesignParameter['_Slicer']['_XYCoordinates'] = [[_ResistorBankOrigin[0][0] + 
                                                                self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][0][1][0] + _DRCObj._MetalxMinSpace11 + 
                                                                # self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] + _DRCObj._MetalxMinSpace11 
                                                                # + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met6LayerVRX']['_XYCoordinates'][-1][0][0] + 
                                                                # self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_XINp']['_Ignore'] + self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2,
                                                                abs(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0]) + 
                                                                _SLGuardringWidth // 2,
                                                                _ResistorBankOrigin[0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore']
                                                                + (self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] * (_NumberofSlicerWithSRLatch - 1) / 2)
                                                                + _CenterofVRX]]

        

        print ('################################       Additional Via Settings      #######################################')
        _ViaVRXMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        if _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] <= 1 :
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        self._DesignParameter['_ViaMet12Met2OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVRXMet12Met2)

        tmp = []
        for i in range (0, _NumberofSlicerWithSRLatch) :
            tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'] = tmp

        del tmp

        _ViaVRXMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        if _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] <= 1 :
            _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1
            _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        self._DesignParameter['_ViaMet22Met3OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnVRX']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVRXMet22Met3)

        tmp = []
        for i in range (0, _NumberofSlicerWithSRLatch) :
            tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        self._DesignParameter['_ViaMet22Met3OnVRX']['_XYCoordinates'] = tmp

        del tmp

        _ViaVRXMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        if _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] <= 1 :
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        self._DesignParameter['_ViaMet32Met4OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnVRX']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVRXMet32Met4)

        tmp = []
        for i in range (0, _NumberofSlicerWithSRLatch) :
            tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        self._DesignParameter['_ViaMet32Met4OnVRX']['_XYCoordinates'] = tmp

        del tmp

        _ViaVRXMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
        if _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

        self._DesignParameter['_ViaMet42Met5OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVRXMet42Met5)

        tmp = []
        for i in range (0, _NumberofSlicerWithSRLatch) :
            tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        self._DesignParameter['_ViaMet42Met5OnVRX']['_XYCoordinates'] = tmp

        del tmp

        _ViaVRXMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = 2
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet52Met6OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVRXMet52Met6)

        tmp = []
        for i in range (0, _NumberofSlicerWithSRLatch) :
            tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'] = tmp

        del tmp
        

        # _ViaVRXMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        # _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        # _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        # if _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
        #     _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = 2
        #     _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = int(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        # self._DesignParameter['_ViaMet62Met7OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVRXIn{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet62Met7OnVRX']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaVRXMet62Met7)

        # tmp = []
        # for i in range (0, _NumberofSlicerWithSRLatch) :
        #     tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
        #         self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
        #         self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
        #         self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']])
        
        
        # self._DesignParameter['_ViaMet62Met7OnVRX']['_XYCoordinates'] = tmp

        # del tmp

        # self._DesignParameter['_Met6LayerbtwSlicer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates= [], _XWidth=400, _YWidth=400)
        # self._DesignParameter['_Met6LayerbtwSlicer']['_XWidth'] = self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth']
        # self._DesignParameter['_Met6LayerbtwSlicer']['_YWidth'] = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] + self._DesignParameter['_Met6LayerbtwSlicer']['_XWidth'] // 2
        # tmp = []
        # for i in range (0, _NumberofSlicerWithSRLatch) :
        #     if i % 2 == 0 :
        #         tmp.append([self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
        #         self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
        #         self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
        #         self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] // 2
        #         - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] * i])

        # self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'] = tmp

        # del tmp

        self._DesignParameter['_Met6LayerbtwSlicer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerbtwSlicer']['_Width'] = self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth']
        self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore']],
                                                        [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] -
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] * (_NumberofSlicerWithSRLatch - 1)]]]

        self._DesignParameter['_Met6Layer4VRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6Layer4VRX']['_Width'] = self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth']
        self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                                                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1] + 
                                                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] // 2],
                                                        [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + 
                                                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                                                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1] - 
                                                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] // 2]]]


        self._DesignParameter['_Met7LayerRes2Sli'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerRes2Sli']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width']
        tmp = []
        for i in range (len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'])) :
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][0],
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][1]],
                        [self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6Layer4VRX']['_Width'] // 2,
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'] = tmp

        del tmp
        


        # self._DesignParameter['_Met7LayerSli2Res'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_Met7LayerSli2Res']['_Width'] = self._DesignParameter['_Met6LayerbtwSlicer']['_Width']
        
        # tmp = []
        # for i in range (len(self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'])) :
        #     tmp.append([[self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'][i][0] + self._DesignParameter['_Met6LayerbtwSlicer']['_Width'] // 2,
        #                 self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'][i][1]],
        #                 [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][0][0] +
        #                 self._DesignParameter['_Slicer']['_XYCoordinates'][0][0],
        #                 self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'][i][1]]])
        
        
        # self._DesignParameter['_Met7LayerSli2Res']['_XYCoordinates'] = tmp

        # del tmp

        _ViaVRXSlicerMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6Layer4VRX']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerRes2Sli']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerRes2Sli']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6Layer4VRX']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVRXSlicer'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVRXSlicerIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVRXSlicer']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVRXSlicerMet62Met7)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'][j][0][1]])
        
        self._DesignParameter['_ViaMet62Met7OnVRXSlicer']['_XYCoordinates'] = tmp

        del tmp

        # self._DesignParameter['_Met6LayerSli2ResY'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_Met6LayerSli2ResY']['_Width'] = self._DesignParameter['_Met6LayerbtwSlicer']['_XWidth']
        # self._DesignParameter['_Met6LayerSli2ResY']['_XYCoordinates'] = [[[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met6LayerVRX']['_XYCoordinates'][-1][0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met6LayerVRX']['_Width'] // 2 
        #                                             + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met6LayerSli2ResY']['_Width'] // 2,
        #                                             self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] // 2],
        #                                             [self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met6LayerVRX']['_XYCoordinates'][-1][0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met6LayerVRX']['_Width'] // 2 
        #                                             + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met6LayerSli2ResY']['_Width'] // 2,
        #                                             self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1] - self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] // 2]]]


        ## VDD / VSS Extension
        self._DesignParameter['_Met6LayerSlicerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VSSRouting']['_Width']
        self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][0][0][0] + 
                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_FRB']['_XYCoordinates'][0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_GapbtwOriginY']['_Ignore']],
                                                                        [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][0][0][0] + 
                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_FRB']['_XYCoordinates'][0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_GapbtwOriginY']['_Ignore'] +
                                                                        _YRBNum * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceY']['_Ignore']]]]

        self._DesignParameter['_Met6LayerSlicerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VDDRouting']['_Width']
        self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0] + 
                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_FRB']['_XYCoordinates'][0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_GapbtwOriginY']['_Ignore']],
                                                                        [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0] + 
                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_FRB']['_XYCoordinates'][0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_GapbtwOriginY']['_Ignore'] +
                                                                        _YRBNum * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceY']['_Ignore']]]]
        
        self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVDD']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_Width']
        tmp = []
        for i in range (0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])) :
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][0],
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][1]],
                        [self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] // 2,
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVSS']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_Width']
        tmp = []
        for i in range (0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])) :
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][0],
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][1]],
                        [self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] // 2,
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = tmp

        del tmp

        _ViaVDDMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met7)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][j][0][1]])
        
        self._DesignParameter['_ViaMet62Met7OnVDD']['_XYCoordinates'] = tmp

        del tmp

        _ViaVSSMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met7)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][j][0][1]])
        
        self._DesignParameter['_ViaMet62Met7OnVSS']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met7LayerVDD2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVDD2']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_Width']
        tmp = []
        for i in range (0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])) :
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][0],
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][1]],
                        [self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] // 2,
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met7LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerVSS2']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_Width']
        tmp = []
        for i in range (0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])) :
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][0],
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][1]],
                        [self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] // 2,
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'] = tmp

        del tmp

        _ViaVDD2Met62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVDD2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDD2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVDD2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDD2Met62Met7)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][j][0][1]])
        
        self._DesignParameter['_ViaMet62Met7OnVDD2']['_XYCoordinates'] = tmp

        del tmp

        _ViaVSS2Met62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSS2In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVSS2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSS2Met62Met7)

        tmp = []
        for i in range (0, len(self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'])) :
            for j in range (0, len(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])) :
                tmp.append([self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][j][0][1]])
        
        self._DesignParameter['_ViaMet62Met7OnVSS2']['_XYCoordinates'] = tmp

        del tmp

        




if __name__ == '__main__' :
    
    _XRBNum = 4
    _YRBNum = 100

    ## X axis M7 Length >= 25um : overall m7 density < 80%

    _TransmissionGateFinger = 10
    _TransmissionGateChannelWidth = 275  ##200nm ~ 500nm range
    _TransmissionGateChannelLength = 30
    _TransmissionGateNPRatio = 2  ##Default = 2
    _TransmissionGateDummy = True     #T/F?
    _TransmissionGateVDD2VSSHeight = 2426 ## FIXED
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
    _TotalSubringWidth = 200

    _SRFinger1 = 5
    _SRFinger2 = 1
    _SRFinger3 = 2
    _SRFinger4 = 2
    _SRNMOSChannelWidth1 = 200
    _SRPMOSChannelWidth1 = 400
    _SRNMOSChannelWidth2 = 200
    _SRPMOSChannelWidth2 = 400
    _SRNMOSChannelWidth3 = 200
    _SRPMOSChannelWidth3 = 400
    _SRNMOSChannelWidth4 = 200
    _SRPMOSChannelWidth4 = 400
    _SRChannelLength = 30
    _SRNPRatio = None
    _SRVDD2VSSHeightAtOneSide = None
    _SRDummy = True
    _SRNumSupplyCoX = None
    _SRNumSupplyCoY = 2
    _SRSupplyMet1XWidth = None
    _SRSupplyMet1YWidth = None
    _SRNumViaPoly2Met1CoX = None
    _SRNumViaPoly2Met1CoY = None
    _SRNumViaPMOSMet12Met2CoX = None
    _SRNumViaPMOSMet12Met2CoY = None
    _SRNumViaNMOSMet12Met2CoX = None
    _SRNumViaNMOSMet12Met2CoY = None
    _SRNumViaPMOSMet22Met3CoX = None
    _SRNumViaPMOSMet22Met3CoY = None
    _SRNumViaNMOSMet22Met3CoX = None
    _SRNumViaNMOSMet22Met3CoY = None
    _SRSLVT = True
    _SRPowerLine = True
    _SLCLKinputPMOSFinger1 = 6
    _SLCLKinputPMOSFinger2 = 3
    _SLPMOSFinger = 2
    _SLPMOSChannelWidth = 1000
    _SLDATAinputNMOSFinger = 12
    _SLNMOSFinger = 2
    _SLCLKinputNMOSFinger = 8
    _SLNMOSChannelWidth = 1000
    _SLChannelLength = 30
    _SLDummy = True
    _SLSLVT = True
    _SLGuardringWidth = 200
    _SLGuardring = True
    _SLSlicerGuardringWidth = 200
    _SLSlicerGuardring = None
    _SLNumSupplyCOY = None
    _SLNumSupplyCOX = None
    _SLSupplyMet1XWidth = None
    _SLSupplyMet1YWidth = None
    _SLVDD2VSSHeight = None
    _SLNumVIAPoly2Met1COX = None
    _SLNumVIAPoly2Met1COY = None
    _SLNumVIAMet12COX = None
    _SLNumVIAMet12COY = None
    _SLPowerLine = True
    _N = 4
    _InvFinger = 16
    _InvChannelWidth = 200
    _InvChannelLength = 30
    _InvNPRatio = 3
    _InvVDD2VSSHeight = None
    _InvDummy = True
    _InvNumSupplyCoX = None
    _InvNumSupplyCoY = None
    _InvSupplyMet1XWidth = None
    _InvSupplyMet1YWidth = None
    _InvNumViaPoly2Met1CoX = None
    _InvNumViaPoly2Met1CoY = None
    _InvNumViaPMOSMet12Met2CoX = None
    _InvNumViaPMOSMet12Met2CoY = None
    _InvNumViaNMOSMet12Met2CoX = None
    _InvNumViaNMOSMet12Met2CoY = None
    _InvSLVT = True
    _InvPowerLine = None
    _SLSRInvSupplyLineX4 = True


    DesignParameters._Technology = '028nm'

    SlicerandSRLatchwtResistorObj = _SlicerandSRLatchwtResistor(_DesignParameter=None, _Name='SlicerandSRLatchwtResistor')
    #print ("A!!")
    SlicerandSRLatchwtResistorObj._CalculateDesignParameter(
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
                                _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth,
                                _SRFinger1 = _SRFinger1, _SRFinger2 = _SRFinger2, _SRFinger3 = _SRFinger3, _SRFinger4 = _SRFinger4,
                                  _SRNMOSChannelWidth1 = _SRNMOSChannelWidth1, _SRPMOSChannelWidth1 = _SRPMOSChannelWidth1, _SRNMOSChannelWidth2 = _SRNMOSChannelWidth2, _SRPMOSChannelWidth2 = _SRPMOSChannelWidth2,
                                  _SRNMOSChannelWidth3 = _SRNMOSChannelWidth3, _SRPMOSChannelWidth3 = _SRPMOSChannelWidth3, _SRNMOSChannelWidth4 = _SRNMOSChannelWidth4, _SRPMOSChannelWidth4 = _SRPMOSChannelWidth4,
                                  _SRChannelLength = _SRChannelLength, _SRNPRatio = _SRNPRatio,
                                  _SRVDD2VSSHeightAtOneSide = _SRVDD2VSSHeightAtOneSide, _SRDummy = _SRDummy, _SRNumSupplyCoX = _SRNumSupplyCoX, _SRNumSupplyCoY = _SRNumSupplyCoY,
                                  _SRSupplyMet1XWidth = _SRSupplyMet1XWidth, _SRSupplyMet1YWidth = _SRSupplyMet1YWidth, _SRNumViaPoly2Met1CoX = _SRNumViaPoly2Met1CoX, \
                                  _SRNumViaPoly2Met1CoY = _SRNumViaPoly2Met1CoY, _SRNumViaPMOSMet12Met2CoX = _SRNumViaPMOSMet12Met2CoX, _SRNumViaPMOSMet12Met2CoY = _SRNumViaPMOSMet12Met2CoY,
                                  _SRNumViaNMOSMet12Met2CoX = _SRNumViaNMOSMet12Met2CoX, _SRNumViaNMOSMet12Met2CoY = _SRNumViaNMOSMet12Met2CoY, _SRNumViaPMOSMet22Met3CoX = _SRNumViaPMOSMet22Met3CoX, _SRNumViaPMOSMet22Met3CoY = _SRNumViaPMOSMet22Met3CoY,
                                  _SRNumViaNMOSMet22Met3CoX = _SRNumViaNMOSMet22Met3CoX, _SRNumViaNMOSMet22Met3CoY = _SRNumViaNMOSMet22Met3CoY, _SRSLVT = _SRSLVT, _SRPowerLine = _SRPowerLine,
                                  _SLCLKinputPMOSFinger1 = _SLCLKinputPMOSFinger1, _SLCLKinputPMOSFinger2 = _SLCLKinputPMOSFinger2, _SLPMOSFinger = _SLPMOSFinger, _SLPMOSChannelWidth = _SLPMOSChannelWidth,
                                  _SLDATAinputNMOSFinger = _SLDATAinputNMOSFinger, _SLNMOSFinger = _SLNMOSFinger, _SLCLKinputNMOSFinger = _SLCLKinputNMOSFinger, _SLNMOSChannelWidth = _SLNMOSChannelWidth,
                                  _SLChannelLength = _SLChannelLength, _SLDummy = _SLDummy, _SLSLVT = _SLSLVT, _SLGuardringWidth = _SLGuardringWidth, _SLGuardring = _SLGuardring,
                                  _SLSlicerGuardringWidth=_SLSlicerGuardringWidth, _SLSlicerGuardring=_SLSlicerGuardring,
                                  _SLNumSupplyCOY=_SLNumSupplyCOY, _SLNumSupplyCOX=_SLNumSupplyCOX, _SLSupplyMet1XWidth=_SLSupplyMet1XWidth, _SLSupplyMet1YWidth=_SLSupplyMet1YWidth, _SLVDD2VSSHeight = _SLVDD2VSSHeight,
                                  _SLNumVIAPoly2Met1COX=_SLNumVIAPoly2Met1COX, _SLNumVIAPoly2Met1COY=_SLNumVIAPoly2Met1COY, _SLNumVIAMet12COX=_SLNumVIAMet12COX, _SLNumVIAMet12COY=_SLNumVIAMet12COY, _SLPowerLine = _SLPowerLine, _NumberofSlicerWithSRLatch = _N,
                                    _InvFinger=_InvFinger, _InvChannelWidth=_InvChannelWidth,
                                    _InvChannelLength=_InvChannelLength, _InvNPRatio=_InvNPRatio,
                                    _InvVDD2VSSHeight=_InvVDD2VSSHeight, _InvDummy=_InvDummy,
                                    _InvNumSupplyCoX=_InvNumSupplyCoX,
                                    _InvNumSupplyCoY=_InvNumSupplyCoY,
                                    _InvSupplyMet1XWidth=_InvSupplyMet1XWidth,
                                    _InvSupplyMet1YWidth=_InvSupplyMet1YWidth,
                                    _InvNumViaPoly2Met1CoX=_InvNumViaPoly2Met1CoX, \
                                    _InvNumViaPoly2Met1CoY=_InvNumViaPoly2Met1CoY,
                                    _InvNumViaPMOSMet12Met2CoX=_InvNumViaPMOSMet12Met2CoX,
                                    _InvNumViaPMOSMet12Met2CoY=_InvNumViaPMOSMet12Met2CoY,
                                    _InvNumViaNMOSMet12Met2CoX=_InvNumViaNMOSMet12Met2CoX, \
                                    _InvNumViaNMOSMet12Met2CoY=_InvNumViaNMOSMet12Met2CoY,
                                    _InvSLVT=_InvSLVT, _InvPowerLine=_InvPowerLine, _SLSRInvSupplyLineX4=_SLSRInvSupplyLineX4)


    SlicerandSRLatchwtResistorObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SlicerandSRLatchwtResistorObj._DesignParameter)
    _fileName = 'SlicerandSRLatchwtResistor.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = SlicerandSRLatchwtResistorObj._CreateGDSStream(SlicerandSRLatchwtResistorObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')

    import base64
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login(base64.b64decode('anVudW5n'), base64.b64decode('Y2hsd25zZG5kMSE='))
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
    ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
    myfile.close()
    ftp.close()

    import ftplib
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
    ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
    myfile.close()
    ftp.close()

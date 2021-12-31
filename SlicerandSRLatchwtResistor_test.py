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
import FRB2
import SlicerWithSRLatchX4_test
import math
import random


class _SlicerandSRLatchwtResistor(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
        _SRFinger1=None, _SRFinger2=None, _SRFinger3=None, _SRFinger4=None, \
        _SRNMOSChannelWidth1=None, _SRPMOSChannelWidth1=None, _SRNMOSChannelWidth2=None, _SRPMOSChannelWidth2=None, _SRNMOSChannelWidth3=None,
        _SRPMOSChannelWidth3=None, _SRNMOSChannelWidth4=None, _SRPMOSChannelWidth4=None, _SRChannelLength=None, _SRNPRatio=None, \
        _SRVDD2VSSHeightAtOneSide=None, _SRDummy=None, _SRNumSupplyCoX=None, _SRNumSupplyCoY=None, \
        _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None, _SRNumViaPoly2Met1CoX=None, \
        _SRNumViaPoly2Met1CoY=None, _SRNumViaPMOSMet12Met2CoX=None, _SRNumViaPMOSMet12Met2CoY=None, \
        _SRNumViaNMOSMet12Met2CoX=None, _SRNumViaNMOSMet12Met2CoY=None, _SRNumViaPMOSMet22Met3CoX=None, _SRNumViaPMOSMet22Met3CoY=None, \
        _SRNumViaNMOSMet22Met3CoX=None, _SRNumViaNMOSMet22Met3CoY=None, _SRXVT=None, _SRPowerLine=False,
        _SLCLKinputPMOSFinger1=None, _SLCLKinputPMOSFinger2=None, _SLPMOSFinger=None, _SLPMOSChannelWidth=None,
        _SLDATAinputNMOSFinger=None, _SLNMOSFinger=None, _SLCLKinputNMOSFinger=None, _SLNMOSChannelWidth=None, _SLCLKinputNMOSChannelWidth=None,
        _SLChannelLength=None, _SLDummy=False, _SLXVT=False, _SLGuardringWidth=None, _SLGuardring=False,
        _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
        _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight=None,
        _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine=None, _NumberofSlicerWithSRLatch=None, \
        _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
        _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
        _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
        _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
        _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
        _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
        _InvNumViaNMOSMet12Met2CoY=None, _InvXVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None,
        _XRBNum=None, _YRBNum=None,
        # _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterVDD2VSSHeight=None,
        _TransmissionGateFinger=None, _TransmissionGateChannelWidth=None, _TransmissionGateChannelLength=None, _TransmissionGateNPRatio=None,
        _TransmissionGateVDD2VSSHeight=None,
        _PowerLine=False, _InputLine=False,
        _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
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
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _SRFinger1=None, _SRFinger2=None, _SRFinger3=None, _SRFinger4=None, \
                                  _SRNMOSChannelWidth1=None, _SRPMOSChannelWidth1=None, _SRNMOSChannelWidth2=None, _SRPMOSChannelWidth2=None, _SRNMOSChannelWidth3=None, _SRPMOSChannelWidth3=None, _SRNMOSChannelWidth4=None, _SRPMOSChannelWidth4=None, _SRChannelLength=None, _SRNPRatio=None, \
                                  _SRVDD2VSSHeightAtOneSide=None, _SRDummy=None, _SRNumSupplyCoX=None, _SRNumSupplyCoY=None, \
                                  _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None, _SRNumViaPoly2Met1CoX=None, \
                                  _SRNumViaPoly2Met1CoY=None, _SRNumViaPMOSMet12Met2CoX=None, _SRNumViaPMOSMet12Met2CoY=None, \
                                  _SRNumViaNMOSMet12Met2CoX=None, _SRNumViaNMOSMet12Met2CoY=None, _SRNumViaPMOSMet22Met3CoX=None, _SRNumViaPMOSMet22Met3CoY=None, \
                                  _SRNumViaNMOSMet22Met3CoX=None, _SRNumViaNMOSMet22Met3CoY=None, _SRXVT=None, _SRPowerLine=False,
                                  _SLCLKinputPMOSFinger1=None, _SLCLKinputPMOSFinger2=None, _SLPMOSFinger=None, _SLPMOSChannelWidth=None,
                                  _SLDATAinputNMOSFinger=None, _SLNMOSFinger=None, _SLCLKinputNMOSFinger=None, _SLNMOSChannelWidth=None, _SLCLKinputNMOSChannelWidth=None,
                                  _SLChannelLength=None, _SLDummy=False, _SLXVT=False, _SLGuardringWidth=None, _SLGuardring=False,
                                  _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                  _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight=None,
                                  _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine=False, _NumberofSlicerWithSRLatch=None, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
                                  _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
                                  _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvXVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None,
                                  _XRBNum=None, _YRBNum=None,
                                  _TransmissionGateFinger=None, _TransmissionGateChannelWidth=None,
                                  _TransmissionGateChannelLength=None, _TransmissionGateNPRatio=None,
                                  _TransmissionGateDummy=False, _TransmissionGateVDD2VSSHeight=None,
                                  _TransmissionGateXVT=False,
                                  _PowerLine=False, _InputLine=False,
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
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print ('###############################      ResistorBank Generation     #########################################')

        _FRBinputs = copy.deepcopy(FRB2._FullResistorBank._ParametersForDesignCalculation)
        _FRBinputs['_XRBNum'] = _XRBNum
        _FRBinputs['_YRBNum'] = _YRBNum

        _FRBinputs['_TransmissionGateFinger'] = _TransmissionGateFinger
        _FRBinputs['_TransmissionGateChannelWidth'] = _TransmissionGateChannelWidth
        _FRBinputs['_TransmissionGateChannelLength'] = _TransmissionGateChannelLength
        _FRBinputs['_TransmissionGateNPRatio'] = _TransmissionGateNPRatio
        _FRBinputs['_TransmissionGateDummy'] = _TransmissionGateDummy
        _FRBinputs['_TransmissionGateVDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
        _FRBinputs['_TransmissionGateXVT'] = _TransmissionGateXVT
        _FRBinputs['_PowerLine'] = _PowerLine
        _FRBinputs['_InputLine'] = _InputLine

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

        self._DesignParameter['_FRB'] = self._SrefElementDeclaration(_DesignObj=FRB2._FullResistorBank(_DesignParameter=None, _Name='ResistorBankIn{}'.format(_Name)))[0]
        self._DesignParameter['_FRB']['_DesignObj']._CalculateFullResistorBank(**_FRBinputs)

        print ('###########################      SlicerWithSRLatch Generation     ####################################')

        _SlicerWithSRLatchEdgeinputs = copy.deepcopy(SlicerWithSRLatchX4_test._SlicerWithSRLatchX4._ParametersForDesignCalculation)
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
        _SlicerWithSRLatchEdgeinputs['_SRXVT'] = _SRXVT
        _SlicerWithSRLatchEdgeinputs['_SRPowerLine'] = _SRPowerLine

        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2
        _SlicerWithSRLatchEdgeinputs['_SLPMOSFinger'] = _SLPMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLPMOSChannelWidth'] = _SLPMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLDATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSFinger'] = _SLNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSChannelWidth'] = _SLNMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputNMOSChannelWidth'] = _SLCLKinputNMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLChannelLength'] = _SLChannelLength
        _SlicerWithSRLatchEdgeinputs['_SLDummy'] = _SLDummy
        _SlicerWithSRLatchEdgeinputs['_SLXVT'] = _SLXVT
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
        _SlicerWithSRLatchEdgeinputs['_InvXVT'] = _InvXVT
        _SlicerWithSRLatchEdgeinputs['_InvPowerLine'] = _InvPowerLine
        _SlicerWithSRLatchEdgeinputs['_SLSRInvSupplyLineX4'] = _SLSRInvSupplyLineX4

        self._DesignParameter['_Slicer'] = self._SrefElementDeclaration(_DesignObj=SlicerWithSRLatchX4_test._SlicerWithSRLatchX4(_DesignParameter=None, _Name="SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_Slicer']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchEdgeinputs)

        _ViaVRXMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(
            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer'][
                '_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = int(
            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer'][
                '_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1:
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = 2
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int(
                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer'][
                    '_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet52Met6OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVRXMet52Met6)

        print ('#################################       Coordinates Settings      ########################################')

        _ResistorBankOrigin = [[0, 0]]
        self._DesignParameter['_FRB']['_XYCoordinates'] = _ResistorBankOrigin

        _CenterofVRX = self.CeilMinSnapSpacing((self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1] +
                        self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1]) / 2, MinSnapSpacing)

        GuardringHeight = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']

        if _PowerLine == False :
            temp = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_XYCoordinates'][-1][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] / 2
        else :
            temp = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][0][1][0]

        tempMet1space = _DRCObj._Metal1MinSpace3 #_DRCObj.DRCMETAL1MinSpace(_TotalSubringWidth, GuardringHeight + _SLSlicerGuardringWidth, _SLSlicerGuardringWidth)

        self._DesignParameter['_Slicer']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(max(_ResistorBankOrigin[0][0] + temp +
                                                               tempMet1space + abs(self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] +
                                                                   self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0]) +
                                                               _SLGuardringWidth / 2, _ResistorBankOrigin[0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_XYCoordinates'][-1][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] / 2 + _DRCObj._PpMinExtensiononPactive2 + \
                                                                self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _SLGuardringWidth / 2 + _DRCObj._PpMinExtensiononPactive2 + _DRCObj._PpMinSpace
                                                                                           ), MinSnapSpacing),
                                                               self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore']
                                                               + (GuardringHeight * (_NumberofSlicerWithSRLatch - 1) / 2)
                                                               + _CenterofVRX, MinSnapSpacing)]]

        print ('################################       Additional Via Settings      #######################################')
        _ViaVRXMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

        if _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] < 1 :
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        if _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] <= 1:
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOY'] = 2
            _ViaVRXMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        self._DesignParameter['_ViaMet12Met2OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVRXMet12Met2)

        _ViaVRXMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        if _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] < 1 :
            _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaVRXMet12Met2['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        if _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] <= 1:
            _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOY'] = 2
            _ViaVRXMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        self._DesignParameter['_ViaMet22Met3OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnVRX']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVRXMet22Met3)

        _ViaVRXMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1


        if _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] < 1 :
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        if _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] <= 1:
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOY'] = 2
            _ViaVRXMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        self._DesignParameter['_ViaMet32Met4OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnVRX']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVRXMet32Met4)

        _ViaVRXMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        if _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] < 1 :
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1


        if _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1:
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOY'] = 2
            _ViaVRXMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        self._DesignParameter['_ViaMet42Met5OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaVRXMet42Met5)

        _ViaVRXMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1


        if _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] < 1 :
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        if _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1:
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOY'] = 2
            _ViaVRXMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        self._DesignParameter['_ViaMet52Met6OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVRXIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**_ViaVRXMet52Met6)

        tmp = []

        _Met4tempSpace = _DRCObj.DRCMETALxMinSpace(self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'], self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_Width'])
        _Met2tempSpace = _DRCObj.DRCMETALxMinSpace(self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'], self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_Width'])

        for i in range(0, _NumberofSlicerWithSRLatch):
            tmp.append([self.FloorMinSnapSpacing(min(self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] +
                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                            self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0] -
                            self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 -
                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_Width'] / 2 - _Met4tempSpace), MinSnapSpacing),
                        self.CeilMinSnapSpacing(min(self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                        self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'], self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_XYCoordinates'][-1][0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_Width'] / 2 - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _Met2tempSpace\
                            ) - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'], MinSnapSpacing)])

        tmp1 = []
        for i in range(0, _NumberofSlicerWithSRLatch):
            tmp1.append([self.CeilMinSnapSpacing(max(self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] +
                             self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0],
                             self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0] +
                             self._DesignParameter['_ViaMet42Met5OnVRX']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 +
                             self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_Width'] / 2 + _Met4tempSpace), MinSnapSpacing),
                         self.CeilMinSnapSpacing(min(self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_YINp']['_Ignore'],
                                                     self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] +
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter[
                                                         '_Slicer']['_XYCoordinates'][0][1] +
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter[
                                                         '_Slicer']['_DesignObj']._DesignParameter['_NMOSSET'][
                                                         '_XYCoordinates'][0][1] +
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter[
                                                         '_Slicer']['_DesignObj']._DesignParameter['_NMOSSET'][
                                                         '_DesignObj']._DesignParameter['_Met2NMOS']['_XYCoordinates'][
                                                         -1][0][1] -
                                                     self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter[
                                                         '_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter[
                                                         '_Slicer']['_DesignObj']._DesignParameter['_NMOSSET'][
                                                         '_DesignObj']._DesignParameter['_Met2NMOS']['_Width'] / 2 -
                                                     self._DesignParameter['_ViaMet12Met2OnVRX'][
                                                         '_DesignObj']._DesignParameter['_Met2Layer'][
                                                         '_YWidth'] / 2 - _Met2tempSpace \
                                                     ) - i *
                         self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight'][
                             '_Ignore'], MinSnapSpacing)])

        self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'] = tmp + tmp1

        self._DesignParameter['_ViaMet22Met3OnVRX']['_XYCoordinates'] = tmp + tmp1

        self._DesignParameter['_ViaMet32Met4OnVRX']['_XYCoordinates'] = tmp + tmp1

        self._DesignParameter['_ViaMet42Met5OnVRX']['_XYCoordinates'] = tmp + tmp1

        self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'] = tmp + tmp1

        del tmp
        del tmp1

        _InputMaxY = max(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)
        _InputMinY = min(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)
        _InputMaxX1 = self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), MinSnapSpacing)
        _InputMinX1 = self.FloorMinSnapSpacing(min(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), MinSnapSpacing)
        _InputMaxX2 = self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][-1][0] + self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), MinSnapSpacing)
        _InputMinX2 = self.FloorMinSnapSpacing(min(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2), MinSnapSpacing)

        self._DesignParameter['_AdditionalMet1forInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_AdditionalMet1forInput']['_Width'] = _InputMaxY - _InputMinY

        _CenterofRX = self.FloorMinSnapSpacing((_InputMaxY + _InputMinY) / 2, MinSnapSpacing)
            #self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), 2 * MinSnapSpacing)

        #- i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']

        tmp = []
        for i in range(0, _NumberofSlicerWithSRLatch) :
            tmp.append([[_InputMinX1, _CenterofRX - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']], \
                        [_InputMaxX1, _CenterofRX - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']]])

            tmp.append([[_InputMinX2, _CenterofRX - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']], \
                        [_InputMaxX2, _CenterofRX - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']]])

        # tmp = []
        # for i in range(0, _NumberofSlicerWithSRLatch) :
        #     tmp.append([[self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'], MinSnapSpacing)], \
        #                 [self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'], MinSnapSpacing)]])
        #
        #     tmp.append([[self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][-1][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'], MinSnapSpacing)], \
        #                 [self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][-1][0], self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet12Met2OnVRX']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnVRX']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'], MinSnapSpacing)]])
        #

        self._DesignParameter['_AdditionalMet1forInput']['_XYCoordinates'] = tmp

        self._DesignParameter['_Met6LayerbtwSlicer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerbtwSlicer']['_Width'] = int(self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'])
        self._DesignParameter['_Met6LayerbtwSlicer']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore']],
                                                                           [self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] -
                                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] * (_NumberofSlicerWithSRLatch - 1)]]]

        self._DesignParameter['_Met6Layer4VRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6Layer4VRX']['_Width'] = int(self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'])
        self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][0][0],
                                                                       self.CeilMinSnapSpacing(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1] +
                                                                       self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] / 2, MinSnapSpacing)],
                                                                      [self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][0][0],
                                                                       self.CeilMinSnapSpacing(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1] -
                                                                       self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width'] / 2, MinSnapSpacing)]]]

        self._DesignParameter['_Met7LayerRes2Sli'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met7LayerRes2Sli']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_Width']
        tmp = []
        for i in range(len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'])):
            tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][0],
                         self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][1]],
                        [self.CeilMinSnapSpacing(self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6Layer4VRX']['_Width'] / 2, MinSnapSpacing),
                         self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][1]]])

        self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'] = tmp

        del tmp

        self._DesignParameter['_Met6LayerVref'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met6LayerVref']['_Width'] = int(self._DesignParameter['_ViaMet52Met6OnVRX']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'])
        self._DesignParameter['_Met6LayerVref']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][-1][0],
                                                                       #  self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] +
                                                                       # self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter[
                                                                       #     '_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0],
                                                                       self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                                       self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore']],
                                                                      [self._DesignParameter['_ViaMet52Met6OnVRX']['_XYCoordinates'][-1][0],
                                                                       #    self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] +
                                                                       # self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter[
                                                                       #     '_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0],
                                                                       self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] +
                                                                       self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_YINp']['_Ignore'] -
                                                                       self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore'] * (_NumberofSlicerWithSRLatch - 1)]]]

        self._DesignParameter['_Vrefpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
                                                                         _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                                                                         _XYCoordinates=[[self._DesignParameter['_Met6LayerVref']['_XYCoordinates'][0][0][0],
                                                                                          (self._DesignParameter['_Met6LayerVref']['_XYCoordinates'][0][0][1])]], ###- abs(self._DesignParameter['_Met6LayerVref']['_XYCoordinates'][0][1][1])) // 2]],
                                                                         _Mag=0.5, _Angle=0, _TEXT='Vref')


        # for i in range(0, _N):
        #     self._DesignParameter['CK<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
        #                                                    _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
        #                                                    _XYCoordinates=[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinCK0']['_XYCoordinates'][0][0],
        #                                                                     self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinCK0']['_XYCoordinates'][0][1]
        #                                                                     - i*self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']]],
        #                                                    _Mag=0.5, _Angle=0, _TEXT='CLK<{0}>'.format(i))

        # for i in range(0, _N):
        #     self._DesignParameter['OUT<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #                                                       _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
        #                                                       _XYCoordinates=[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_OUT1pin']['_XYCoordinates'][0][0],
        #                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_OUT1pin']['_XYCoordinates'][0][1]
        #                                                                        - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']]],
        #                                                       _Mag=0.5, _Angle=0, _TEXT='OUT<{0}>'.format(i))

        # for i in range(0, _N):
        #     self._DesignParameter['OUTb<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #                                                       _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
        #                                                       _XYCoordinates=[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_OUTb1pin']['_XYCoordinates'][0][0],
        #                                                                        self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_OUTb1pin']['_XYCoordinates'][0][1]
        #                                                                        - i * self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringHeight']['_Ignore']]],
        #                                                       _Mag=0.5, _Angle=0, _TEXT='OUTb<{0}>'.format(i))

        # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.5, _Angle=0, _TEXT='VDD')

        # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.5, _Angle=0, _TEXT='VSS')

        # self._DesignParameter['_VCMpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.5, _Angle=0, _TEXT='VCM')

        # self._DesignParameter['_VRXpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.5, _Angle=0, _TEXT='VRX')

        # self._DesignParameter['_VDDpin']['_XYCoordinates'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_VDDpin']['_XYCoordinates']
        # self._DesignParameter['_VSSpin']['_XYCoordinates'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_VSSpin']['_XYCoordinates']
        # self._DesignParameter['_VCMpin']['_XYCoordinates'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_VCMpin']['_XYCoordinates']
        # self._DesignParameter['_VRXpin']['_XYCoordinates'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_VRXpin']['_XYCoordinates']

        if _InputLine == True :
            for i in range(0, _XRBNum):
                for j in range(0, _YRBNum):
                    for k in range(0, 2):  ## for nmos 0 and pmos 1
                        if k == 0:
                            self._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(
                                _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
                                _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
                                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                                _XYCoordinates=self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)]['_XYCoordinates'],
                                _Mag=0.02, _Angle=0, _TEXT='S<{0}>'.format(i + _XRBNum * j))

                        else:
                            self._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(
                                _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
                                _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
                                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                                _XYCoordinates=self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)]['_XYCoordinates'],
                                _Mag=0.02, _Angle=0, _TEXT='SB<{0}>'.format(i + _XRBNum * j))

        else :
            for i in range (0, _XRBNum) :
                for j in range (0, _YRBNum) :
                    for k in range (0, 2) : ## for nmos 0 and pmos 1
                        if k == 0 :
                            self._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                            _Presentation=[0,1,2], _Reflect=[0,0,0],
                            _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][0] +
                                            i * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceX']['_Ignore'],
                                            _ResistorBankOrigin[0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][1] +
                                            j * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceY']['_Ignore']]],
                            _Mag = 0.5, _Angle=0, _TEXT='S<{0}>'.format(i + _XRBNum * j))

                        else :
                            self._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                            _Presentation=[0,1,2], _Reflect=[0,0,0],
                            _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] +
                                            i * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceX']['_Ignore'],
                                            _ResistorBankOrigin[0][1] + self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][1] +
                                            j * self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_ResistorSpaceY']['_Ignore']]],
                            _Mag = 0.5, _Angle=0, _TEXT='SB<{0}>'.format(i + _XRBNum * j))



        _ViaVRXSlicerMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6Layer4VRX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerRes2Sli']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        if _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1:
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerRes2Sli']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        if _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1:
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
            _ViaVRXSlicerMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6Layer4VRX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        self._DesignParameter['_ViaMet62Met7OnVRXSlicer'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVRXSlicerIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVRXSlicer']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVRXSlicerMet62Met7)

        tmp = []
        for i in range(0, len(self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'])):
            for j in range(0, len(self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['_Met6Layer4VRX']['_XYCoordinates'][i][0][0],
                            self._DesignParameter['_Met7LayerRes2Sli']['_XYCoordinates'][j][0][1]])

        self._DesignParameter['_ViaMet62Met7OnVRXSlicer']['_XYCoordinates'] = tmp

        del tmp


        ## VDD // VSS Extension
        if _PowerLine == True :
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
            for i in range(0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][0],
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][1]],
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] / 2, MinSnapSpacing),
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][1]]])

            self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met7LayerVSS']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_Width']
            tmp = []
            for i in range(0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][0],
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][1]],
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] / 2, MinSnapSpacing),
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][1]]])

            self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = tmp

            del tmp

            _ViaVDDMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1:
                _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
                _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1:
                _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
                _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

            self._DesignParameter['_ViaMet62Met7OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet62Met7OnVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met7)

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][i][0][0],
                                self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet62Met7OnVDD']['_XYCoordinates'] = tmp

            del tmp

            _ViaVSSMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1:
                _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
                _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1:
                _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
                _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

            self._DesignParameter['_ViaMet62Met7OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet62Met7OnVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met7)

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'][i][0][0],
                                self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet62Met7OnVSS']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_Met7LayerVDD2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met7LayerVDD2']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_Width']
            tmp = []
            for i in range(0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][0],
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][1]],
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] / 2, MinSnapSpacing),
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][1]]])

            self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_Met7LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_Met7LayerVSS2']['_Width'] = self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_Width']
            tmp = []
            for i in range(0, len(self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][0],
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][1]],
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] / 2, MinSnapSpacing),
                            self._DesignParameter['_FRB']['_DesignObj']._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][1]]])

            self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'] = tmp

            del tmp

            _ViaVDD2Met62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            if _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] <= 1:
                _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = 1
                _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] <= 1:
                _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOY'] = 1
                _ViaVDD2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

            self._DesignParameter['_ViaMet62Met7OnVDD2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVDD2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet62Met7OnVDD2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDD2Met62Met7)

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6LayerSlicerVDD']['_XYCoordinates'][i][0][0],
                                self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet62Met7OnVDD2']['_XYCoordinates'] = tmp

            del tmp

            _ViaVSS2Met62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
            if _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] <= 1:
                _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = 1
                _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
            if _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] <= 1:
                _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOY'] = 1
                _ViaVSS2Met62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerSlicerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

            self._DesignParameter['_ViaMet62Met7OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet62Met7OnVSS2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSS2Met62Met7)

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6LayerSlicerVSS']['_XYCoordinates'][i][0][0],
                                self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet62Met7OnVSS2']['_XYCoordinates'] = tmp

            del tmp



if __name__ == '__main__':
    for _ in range(0, 1) :
        _XRBNum = 4#random.randint(3,6)
        _YRBNum = 8#32//_XRBNum
        _TransmissionGateFinger = 8#random.randint(2,13)
        _TransmissionGateChannelWidth = 500#random.randrange(700,900,10)  ## 40 : random.randrange(350,500,10), 65nm : random.randrange(500,700,10), 90nm : random.randrange(700,900,10)
        _TransmissionGateChannelLength = 60  ##40 : 40, 65 : 60, 90 : 100
        _TransmissionGateNPRatio = 2  ##Default = 2
        _ResistorWidth = 2000#random.randrange(1500,2500, 100)#random.randrange(1500,2500, 100), random.randrange(1000,2000, 2)
        _ResistorLength = 2000#_ResistorWidth + random.randrange(100,2000, 100)##_ResistorWidth + random.randrange(100,1000, 100), random.randrange(400,2000, 2)  ## minimum : 400
        _TransmissionGateVDD2VSSHeight = 3850  ## 40nm : 4000, 65nm : 5000, 90nm : 6000  if DRC error occurs, set this value for minimum value

        _TransmissionGateDummy = True  # T//F? only true @ 40, 28nm process
        _TransmissionGateXVT = 'LVT'  # T//F?
        _PowerLine = False  # T//F?
        _InputLine = False
        _ResistorMetXCO = None
        _ResistorMetYCO = 2#random.randint(1,3)
        _PMOSSubringType = False  ## FIXED
        _PMOSSubringXWidth = None  ## FIXED
        _PMOSSubringYWidth = None  ## FIXED
        _PMOSSubringWidth = 170  ## 40, 65nm : 170, 90nm : 200
        _NMOSSubringType = True  ## FIXED
        _NMOSSubringXWidth = None  ## FIXED
        _NMOSSubringYWidth = None  ## FIXED
        _NMOSSubringWidth = _PMOSSubringWidth
        _TotalSubringType = True  ## FIXED
        _TotalSubringXWidth = None  ## FIXED
        _TotalSubringYWidth = None  ## FIXED
        _TotalSubringWidth = _PMOSSubringWidth

        _SRRandWidth = 500#random.randrange(700,1400,10)#(200,400,2)
        _SRNPRatio = 2##round(2 + random.random())
        _SRFinger1 = 5#random.randint(1,15)
        _SRPMOSChannelWidth1 = _SRRandWidth * _SRNPRatio
        _SRNMOSChannelWidth1 = _SRRandWidth
        _SRFinger2 = 1#random.randint(1,15)
        _SRPMOSChannelWidth2 = _SRRandWidth * _SRNPRatio
        _SRNMOSChannelWidth2 = _SRRandWidth
        _SRFinger3 = 2#random.randint(1,15)
        _SRPMOSChannelWidth3 = _SRRandWidth * _SRNPRatio
        _SRNMOSChannelWidth3 = _SRRandWidth
        _SRFinger4 = 2#random.randint(1,15)
        _SRPMOSChannelWidth4 = _SRRandWidth * _SRNPRatio
        _SRNMOSChannelWidth4 = _SRRandWidth
        _SRChannelLength = 60

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
        _SRXVT = 'LVT'
        _SRPowerLine = False

        _SLCLKinputPMOSFinger1 = 6#random.randint(1,15)
        _SLCLKinputPMOSFinger2 = 3#random.randint(1,15)
        _SLPMOSFinger = 2#random.randint(1,15)
        _SLPMOSChannelWidth = 500#random.randrange(700,3500,10)#(200,1050,2)
        _SLNMOSFinger = 2#random.randint(1,15)
        _SLDATAinputNMOSFinger = 8#random.randint(2,15)
        _SLCLKinputNMOSFinger = 10#random.randint(1,15)
        _SLNMOSChannelWidth = 500#random.randrange(700,3500,10)#(200,1050,2)
        _SLCLKinputNMOSChannelWidth = 500#random.randrange(700,3500,10)#(200,1050,2)
        _SLChannelLength = 60#30

        _SLDummy = False
        _SLXVT = 'LVT'
        _SLGuardringWidth = 200#200
        _SLGuardring = True
        _SLSlicerGuardringWidth = 200#200
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
        _SLPowerLine = False
        _N = 4#random.randint(1,8)
        _InvChannelWidth = 500#random.randrange(700,750,10)#(200,400,2)
        _InvChannelLength = 60
        _InvFinger = 15#random.randint(5,16)
        _InvNPRatio = 3##round(2+random.random())
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
        _InvXVT = 'LVT'
        _InvPowerLine = False
        _SLSRInvSupplyLineX4 = False



        from Private import MyInfo
        import DRCchecker

        libname = 'SlicerandSRLatchwtResistor'
        cellname = 'SlicerandSRLatchwtResistor'
        _fileName = cellname + '.gds'

        InputParams = dict(
        _XRBNum=_XRBNum, _YRBNum=_YRBNum,
        _TransmissionGateFinger=_TransmissionGateFinger, _TransmissionGateChannelWidth=_TransmissionGateChannelWidth, _TransmissionGateChannelLength=_TransmissionGateChannelLength, _TransmissionGateNPRatio=_TransmissionGateNPRatio,
        _TransmissionGateDummy=_TransmissionGateDummy, _TransmissionGateVDD2VSSHeight=_TransmissionGateVDD2VSSHeight, _TransmissionGateXVT=_TransmissionGateXVT,
        _PowerLine=_PowerLine, _InputLine=_InputLine,
        _ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO=_ResistorMetXCO, _ResistorMetYCO=_ResistorMetYCO,
        _PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth, _PMOSSubringWidth=_PMOSSubringWidth,
        _NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth, _NMOSSubringWidth=_NMOSSubringWidth,
        _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth, _TotalSubringWidth=_TotalSubringWidth,
        _SRFinger1=_SRFinger1, _SRFinger2=_SRFinger2, _SRFinger3=_SRFinger3, _SRFinger4=_SRFinger4,
        _SRNMOSChannelWidth1=_SRNMOSChannelWidth1, _SRPMOSChannelWidth1=_SRPMOSChannelWidth1, _SRNMOSChannelWidth2=_SRNMOSChannelWidth2, _SRPMOSChannelWidth2=_SRPMOSChannelWidth2,
        _SRNMOSChannelWidth3=_SRNMOSChannelWidth3, _SRPMOSChannelWidth3=_SRPMOSChannelWidth3, _SRNMOSChannelWidth4=_SRNMOSChannelWidth4, _SRPMOSChannelWidth4=_SRPMOSChannelWidth4,
        _SRChannelLength=_SRChannelLength, _SRNPRatio=_SRNPRatio,
        _SRVDD2VSSHeightAtOneSide=_SRVDD2VSSHeightAtOneSide, _SRDummy=_SRDummy, _SRNumSupplyCoX=_SRNumSupplyCoX, _SRNumSupplyCoY=_SRNumSupplyCoY,
        _SRSupplyMet1XWidth=_SRSupplyMet1XWidth, _SRSupplyMet1YWidth=_SRSupplyMet1YWidth, _SRNumViaPoly2Met1CoX=_SRNumViaPoly2Met1CoX, \
        _SRNumViaPoly2Met1CoY=_SRNumViaPoly2Met1CoY, _SRNumViaPMOSMet12Met2CoX=_SRNumViaPMOSMet12Met2CoX, _SRNumViaPMOSMet12Met2CoY=_SRNumViaPMOSMet12Met2CoY,
        _SRNumViaNMOSMet12Met2CoX=_SRNumViaNMOSMet12Met2CoX, _SRNumViaNMOSMet12Met2CoY=_SRNumViaNMOSMet12Met2CoY, _SRNumViaPMOSMet22Met3CoX=_SRNumViaPMOSMet22Met3CoX, _SRNumViaPMOSMet22Met3CoY=_SRNumViaPMOSMet22Met3CoY,
        _SRNumViaNMOSMet22Met3CoX=_SRNumViaNMOSMet22Met3CoX, _SRNumViaNMOSMet22Met3CoY=_SRNumViaNMOSMet22Met3CoY, _SRXVT=_SRXVT, _SRPowerLine=_SRPowerLine,
        _SLCLKinputPMOSFinger1=_SLCLKinputPMOSFinger1, _SLCLKinputPMOSFinger2=_SLCLKinputPMOSFinger2, _SLPMOSFinger=_SLPMOSFinger, _SLPMOSChannelWidth=_SLPMOSChannelWidth,
        _SLDATAinputNMOSFinger=_SLDATAinputNMOSFinger, _SLNMOSFinger=_SLNMOSFinger, _SLCLKinputNMOSFinger=_SLCLKinputNMOSFinger, _SLNMOSChannelWidth=_SLNMOSChannelWidth, _SLCLKinputNMOSChannelWidth=_SLCLKinputNMOSChannelWidth,
        _SLChannelLength=_SLChannelLength, _SLDummy=_SLDummy, _SLXVT=_SLXVT, _SLGuardringWidth=_SLGuardringWidth, _SLGuardring=_SLGuardring,
        _SLSlicerGuardringWidth=_SLSlicerGuardringWidth, _SLSlicerGuardring=_SLSlicerGuardring,
        _SLNumSupplyCOY=_SLNumSupplyCOY, _SLNumSupplyCOX=_SLNumSupplyCOX, _SLSupplyMet1XWidth=_SLSupplyMet1XWidth, _SLSupplyMet1YWidth=_SLSupplyMet1YWidth, _SLVDD2VSSHeight=_SLVDD2VSSHeight,
        _SLNumVIAPoly2Met1COX=_SLNumVIAPoly2Met1COX, _SLNumVIAPoly2Met1COY=_SLNumVIAPoly2Met1COY, _SLNumVIAMet12COX=_SLNumVIAMet12COX, _SLNumVIAMet12COY=_SLNumVIAMet12COY, _SLPowerLine=_SLPowerLine, _NumberofSlicerWithSRLatch=_N,
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
        _InvXVT=_InvXVT, _InvPowerLine=_InvPowerLine, _SLSRInvSupplyLineX4=_SLSRInvSupplyLineX4)

        LayoutObj = _SlicerandSRLatchwtResistor(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#############################      Sending to FTP Server...      #############################')
        My = MyInfo.USER(DesignParameters._Technology)
        Checker = DRCchecker.DRCchecker(
            username=My.ID,
            password=My.PW,
            WorkDir=My.Dir_Work,
            DRCrunDir=My.Dir_DRCrun,
            libname=libname,
            cellname=cellname,
            GDSDir=My.Dir_GDS
        )
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

        # import ftplib

        # ftp = ftplib.FTP('141.223.22.156')
        # ftp.login('jicho0927', 'cho89140616!!')
        # ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
        # myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
        # ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
        # myfile.close()

        import ftplib
        
        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('junung', 'chlwnsdnd1!')
        ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
        #ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
        myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
        ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
        myfile.close()
    
        import DRCchecker

        # a = DRCchecker.DRCchecker('junung', 'chlwnsdnd1!', '/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/OPUS/Samsung28n/DRC/run', 'SlicerandSRLatchwtResistor', 'SlicerandSRLatchwtResistor', None)
        # a.DRCchecker()
        
        
        # _Checker = DRCchecker.DRCchecker('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/TSMC90n','/mnt/sdc/junung/OPUS/TSMC90n/DRC/DRC_run','SlicerandSRLatchwtResistor','SlicerandSRLatchwtResistor')
        # _Checker.DRCchecker()

    print("DRC Clean!!!")

    #     import ftplib
    #
    #     ftp = ftplib.FTP('141.223.22.156')
    #     ftp.login('jicho0927', 'cho89140616!!')
    #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
    #     myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
    #     ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
    #     myfile.close()
    #
    #     import DRCchecker
    #     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','SlicerandSRLatchwtResistor','SlicerandSRLatchwtResistor',None)
    #     a.DRCchecker()
    #
    # print ("DRC Clean!!!")

    #     import ftplib
    #
    #     ftp = ftplib.FTP('141.223.22.156')
    #     ftp.login('jicho0927', 'cho89140616!!')
    #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc40n')
    #     myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
    #     ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
    #     myfile.close()
    #
    #     import DRCchecker
    #
    #     a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '/mnt/sdc/jicho0927/OPUS/tsmc40n', '/mnt/sdc/jicho0927/OPUS/tsmc40n/DRC/run', 'SlicerandSRLatchwtResistor', 'SlicerandSRLatchwtResistor', None)
    #     a.DRCchecker()
    #
    # print("DRC Clean!!!")

    #     import ftplib
    #
    #     ftp = ftplib.FTP('141.223.22.156')
    #     ftp.login('jicho0927', 'cho89140616!!')
    #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc90n')
    #     myfile = open('SlicerandSRLatchwtResistor.gds', 'rb')
    #     ftp.storbinary('STOR SlicerandSRLatchwtResistor.gds', myfile)
    #     myfile.close()
    #
    #     import DRCchecker
    #     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc90n','/mnt/sdc/jicho0927/OPUS/tsmc90n/DRC/run','SlicerandSRLatchwtResistor','SlicerandSRLatchwtResistor',None)
    #     a.DRCchecker()
    #
    #
    # print ("DRC Clean!!!")





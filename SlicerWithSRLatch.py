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
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import Slicer
import SRLatch
import Inverter
import random
import math

class _SlicerWithSRLatch (StickDiagram._StickDiagram) :

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
                                  _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None, _SLCLKinputNMOSChannelWidth=None,
                                  _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                  _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                  _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                  _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None, _InvNPRatio=None,
                                  _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None, _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLine=None
    )

    def __init__(self, _DesignParameter = None, _Name = 'SlicerWithSRLatch'):
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None, _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, _SRNumViaPoly2Met1CoX = None, \
                                  _SRNumViaPoly2Met1CoY = None, _SRNumViaPMOSMet12Met2CoX = None, _SRNumViaPMOSMet12Met2CoY = None, \
                                  _SRNumViaNMOSMet12Met2CoX = None, _SRNumViaNMOSMet12Met2CoY = None, _SRNumViaPMOSMet22Met3CoX = None, _SRNumViaPMOSMet22Met3CoY = None, \
                                  _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                  _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None, _SLCLKinputNMOSChannelWidth=None,
                                  _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                  _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                  _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                  _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None, _InvNPRatio=None,
                                  _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None, _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLine=None
                                  ) :


        print ('#########################################################################################################')
        print ('                                {}  SlicerWithSRLatch Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatch'

        print('################################        Supply Generation        #########################################')
        if _SLSRInvSupplyLine == True :
            _InvPowerLine = False
            _SLPowerLine = True
            _SRPowerLine = True

        elif _SLSRInvSupplyLine == False :
            _InvPowerLine = False
            _SLPowerLine = False
            _SRPowerLine = False



        print ('###############################        SRLatch Generation       #########################################')

        _SRLatchinputs = copy.deepcopy(SRLatch._SRLatch._ParametersForDesignCalculation)
        _SRLatchinputs['_Finger1'] = _SRFinger1
        _SRLatchinputs['_Finger2'] = _SRFinger2
        _SRLatchinputs['_Finger3'] = _SRFinger3
        _SRLatchinputs['_Finger4'] = _SRFinger4
        _SRLatchinputs['_NMOSChannelWidth1'] = _SRNMOSChannelWidth1
        _SRLatchinputs['_PMOSChannelWidth1'] = _SRPMOSChannelWidth1
        _SRLatchinputs['_NMOSChannelWidth2'] = _SRNMOSChannelWidth2
        _SRLatchinputs['_PMOSChannelWidth2'] = _SRPMOSChannelWidth2
        _SRLatchinputs['_NMOSChannelWidth3'] = _SRNMOSChannelWidth3
        _SRLatchinputs['_PMOSChannelWidth3'] = _SRPMOSChannelWidth3
        _SRLatchinputs['_NMOSChannelWidth4'] = _SRNMOSChannelWidth4
        _SRLatchinputs['_PMOSChannelWidth4'] = _SRPMOSChannelWidth4
        _SRLatchinputs['_ChannelLength'] = _SRChannelLength
        _SRLatchinputs['_NPRatio'] = _SRNPRatio
        _SRLatchinputs['_VDD2VSSHeightAtOneSide'] = _SRVDD2VSSHeightAtOneSide
        _SRLatchinputs['_Dummy'] = _SRDummy
        _SRLatchinputs['_NumSupplyCoX'] = _SRNumSupplyCoX
        _SRLatchinputs['_NumSupplyCoY'] = _SRNumSupplyCoY
        _SRLatchinputs['_SupplyMet1XWidth'] = _SRSupplyMet1XWidth
        _SRLatchinputs['_SupplyMet1YWidth'] = _SRSupplyMet1YWidth
        _SRLatchinputs['NumViaPoly2Met1CoX'] = _SRNumViaPoly2Met1CoX
        _SRLatchinputs['NumViaPoly2Met1CoY'] = _SRNumViaPoly2Met1CoY
        _SRLatchinputs['NumViaPMOSMet12Met2CoX'] = _SRNumViaPMOSMet12Met2CoX
        _SRLatchinputs['NumViaPMOSMet12Met2CoY'] = _SRNumViaPMOSMet12Met2CoY
        _SRLatchinputs['NumViaNMOSMet12Met2CoX'] = _SRNumViaNMOSMet12Met2CoX
        _SRLatchinputs['NumViaNMOSMet12Met2CoY'] = _SRNumViaNMOSMet12Met2CoY
        _SRLatchinputs['NumViaPMOSMet22Met3CoX'] = _SRNumViaPMOSMet22Met3CoX
        _SRLatchinputs['NumViaPMOSMet22Met3CoY'] = _SRNumViaPMOSMet22Met3CoY
        _SRLatchinputs['NumViaNMOSMet22Met3CoX'] = _SRNumViaNMOSMet22Met3CoX
        _SRLatchinputs['NumViaNMOSMet22Met3CoY'] = _SRNumViaNMOSMet22Met3CoY
        _SRLatchinputs['_SLVT'] = _SRSLVT
        _SRLatchinputs['_PowerLine'] = _SRPowerLine



        self._DesignParameter['_SRLatch'] = self._SrefElementDeclaration(_DesignObj = SRLatch._SRLatch(_DesignParameter=None, _Name ="SRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_SRLatch']['_DesignObj']._CalculateDesignParameter(**_SRLatchinputs)

        print ('###############################         Slicer Generation        #########################################')

        _Slicerinputs = copy.deepcopy(Slicer._Slicer._ParametersForDesignCalculation)
        _Slicerinputs['_CLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1 
        _Slicerinputs['_CLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2 
        _Slicerinputs['_PMOSFinger'] = _SLPMOSFinger
        _Slicerinputs['_PMOSChannelWidth'] = _SLPMOSChannelWidth
        _Slicerinputs['_DATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        _Slicerinputs['_NMOSFinger'] = _SLNMOSFinger
        _Slicerinputs['_CLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        _Slicerinputs['_NMOSChannelWidth'] = _SLNMOSChannelWidth
        _Slicerinputs['_CLKinputNMOSChannelWidth'] = _SLCLKinputNMOSChannelWidth
        _Slicerinputs['_ChannelLength'] = _SLChannelLength
        _Slicerinputs['_Dummy'] = _SLDummy
        _Slicerinputs['_SLVT'] = _SLSLVT
        _Slicerinputs['_GuardringWidth'] = _SLGuardringWidth
        _Slicerinputs['_Guardring'] = _SLGuardring
        _Slicerinputs['_SlicerGuardringWidth'] = _SLSlicerGuardringWidth
        _Slicerinputs['_SlicerGuardring'] = _SLSlicerGuardring
        _Slicerinputs['_NumSupplyCOX'] = _SLNumSupplyCOX
        _Slicerinputs['_NumSupplyCOY'] = _SLNumSupplyCOY
        _Slicerinputs['_SupplyMet1XWidth'] = _SLSupplyMet1XWidth
        _Slicerinputs['_SupplyMet1YWidth'] = _SLSupplyMet1YWidth
        _Slicerinputs['_VDD2VSSHeight'] = _SLVDD2VSSHeight
        _Slicerinputs['_NumVIAPoly2Met1COX'] = _SLNumVIAPoly2Met1COX
        _Slicerinputs['_NumVIAPoly2Met1COY'] = _SLNumVIAPoly2Met1COY
        _Slicerinputs['_NumVIAMet12COX'] = _SLNumVIAMet12COX
        _Slicerinputs['_NumVIAMet12COY'] = _SLNumVIAMet12COY
        _Slicerinputs['_PowerLine'] = _SLPowerLine

        self._DesignParameter['_Slicer'] = self._SrefElementDeclaration(_DesignObj = Slicer._Slicer(_DesignParameter=None, _Name = "SlicerIn{}".format(_Name)))[0]
        self._DesignParameter['_Slicer']['_DesignObj']._CalculateDesignParameter(**_Slicerinputs)

        print ('###############################         Inverter Generation        #########################################')
        # _ContactNum = _InvNumSupplyCoX
        # if _ContactNum == None:
        #     _ContactNum = int((3 * _DRCObj._PolygateMinSpace +
        #                        self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +
        #                        self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + \
        #                        self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +
        #                        self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + \
        #                        3 * _DRCObj._PolygateMinSpace) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        #
        # if _ContactNum < 2 :
        #     _ContactNum = 2
        #
        # if _InvNumSupplyCoY is None :
        #     _InvNumSupplyCoY = _SRNumSupplyCoY
        #

        _Inverterinputs = copy.deepcopy(Inverter._Inverter._ParametersForDesignCalculation)
        _Inverterinputs['_Finger']= _InvFinger
        _Inverterinputs['_ChannelWidth'] = _InvChannelWidth
        _Inverterinputs['_ChannelLength'] = _InvChannelLength
        _Inverterinputs['_NPRatio'] = _InvNPRatio
        _Inverterinputs['_VDD2VSSHeight'] = _InvVDD2VSSHeight
        _Inverterinputs['_Dummy'] = _InvDummy
        _Inverterinputs['_NumSupplyCoX'] = _InvNumSupplyCoX
        _Inverterinputs['_NumSupplyCoY'] = _InvNumSupplyCoY
        _Inverterinputs['_SupplyMet1XWidth'] = _InvSupplyMet1XWidth###self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        _Inverterinputs['_SupplyMet1YWidth'] = _InvSupplyMet1YWidth####self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        _Inverterinputs['_NumViaPoly2Met1CoX'] = _InvNumViaPoly2Met1CoX
        _Inverterinputs['_NumViaPoly2Met1CoY'] = _InvNumViaPoly2Met1CoY
        _Inverterinputs['_NumViaPMOSMet12Met2CoX'] = _InvNumViaPMOSMet12Met2CoX
        _Inverterinputs['_NumViaPMOSMet12Met2CoY'] = _InvNumViaPMOSMet12Met2CoY
        _Inverterinputs['_NumViaNMOSMet12Met2CoX'] = _InvNumViaNMOSMet12Met2CoX
        _Inverterinputs['_NumViaNMOSMet12Met2CoY'] = _InvNumViaNMOSMet12Met2CoY
        _Inverterinputs['_SLVT'] = _InvSLVT
        _Inverterinputs['_SupplyLine'] = _InvPowerLine

        self._DesignParameter['_Inverter'] = self._SrefElementDeclaration(_DesignObj = Inverter._Inverter(_DesignParameter=None, _Name = "InverterIn{}".format(_Name)))[0]
        self._DesignParameter['_Inverter']['_DesignObj']._CalculateDesignParameter(**_Inverterinputs)


        _InvVDD2VSSMinHeight = self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     2 * _DRCObj._Metal1MinSpace3 + 2 * self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 3 * _DRCObj._Metal1MinSpace2


        if _InvVDD2VSSHeight == None :
            _InvVDD2VSSHeight = _InvVDD2VSSMinHeight


        # print ('###############################         Via Met32Met4 Generation        #########################################')
        # _VIAMet32Met4forPMOSRouting = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        # _VIAMet32Met4forNMOSRouting = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        #
        # if _SLPMOSFinger == 1 :
        #     _VIAMet32Met4forPMOSRouting['_ViaMet32Met4NumberOfCOX'] = 1
        #     _VIAMet32Met4forPMOSRouting['_ViaMet32Met4NumberOfCOY'] = 4
        #
        # else :
        #     _VIAMet32Met4forPMOSRouting['_ViaMet32Met4NumberOfCOX'] = 2
        #     _VIAMet32Met4forPMOSRouting['_ViaMet32Met4NumberOfCOY'] = 2
        #
        # if _SLNMOSFinger == 1:
        #     _VIAMet32Met4forNMOSRouting['_ViaMet32Met4NumberOfCOX'] = 1
        #     _VIAMet32Met4forNMOSRouting['_ViaMet32Met4NumberOfCOY'] = 4
        #
        # else :
        #     _VIAMet32Met4forNMOSRouting['_ViaMet32Met4NumberOfCOX'] = 2
        #     _VIAMet32Met4forNMOSRouting['_ViaMet32Met4NumberOfCOY'] = 2
        #
        # self._DesignParameter['_VIAMet32Met4forSSpRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met4forSSnRoutingIn{}'.format(_Name)))[0]
        # self._DesignParameter['_VIAMet32Met4forSSpRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAMet32Met4forPMOSRouting)
        #
        # self._DesignParameter['_VIAMet32Met4forSSnRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met4forSSpRoutingIn{}'.format(_Name)))[0]
        # self._DesignParameter['_VIAMet32Met4forSSnRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAMet32Met4forNMOSRouting)


        _VIAMet42Met5forPMOSRouting = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _VIAMet42Met5forNMOSRouting = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _VIAMet52Met6forPMOSRouting = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _VIAMet52Met6forNMOSRouting = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _VIAMet62Met7forPMOSRouting = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _VIAMet62Met7forNMOSRouting = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)


        if _SLPMOSFinger == 1 :
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOX'] = 2
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOY'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOX'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOY'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOX'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOY'] = 2

        else :
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOX'] = 2
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOY'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOX'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOY'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOX'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOY'] = 2

        if _SLNMOSFinger == 1:
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOX'] = 2
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOY'] = 2
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOX'] = 2
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOY'] = 2
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOX'] = 2
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOY'] = 2

        else :
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOX'] = 2
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOY'] = 2
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOX'] = 2
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOY'] = 2
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOX'] = 2
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOY'] = 2


        self._DesignParameter['_VIAMet42Met5forSSpRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='VIAMet42Met5forSSnRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet42Met5forSSpRouting']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_VIAMet42Met5forPMOSRouting)

        self._DesignParameter['_VIAMet42Met5forSSnRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='VIAMet42Met5forSSpRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet42Met5forSSnRouting']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_VIAMet42Met5forNMOSRouting)

        self._DesignParameter['_VIAMet52Met6forSSpRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='VIAMet52Met6forSSnRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet52Met6forSSpRouting']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_VIAMet52Met6forPMOSRouting)

        self._DesignParameter['_VIAMet52Met6forSSnRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='VIAMet52Met6forSSpRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet52Met6forSSnRouting']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_VIAMet52Met6forNMOSRouting)

        self._DesignParameter['_VIAMet62Met7forSSpRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='VIAMet62Met7forSSnRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet62Met7forSSpRouting']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_VIAMet62Met7forPMOSRouting)

        self._DesignParameter['_VIAMet62Met7forSSnRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='VIAMet62Met7forSSpRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet62Met7forSSnRouting']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_VIAMet62Met7forNMOSRouting)



        _VIAMet42Met5forSRLatchInputRouting = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _VIAMet42Met5forSRLatchInputRouting['_ViaMet42Met5NumberOfCOX'] = 2
        _VIAMet42Met5forSRLatchInputRouting['_ViaMet42Met5NumberOfCOY'] = 2
        _VIAMet52Met6forSRLatchInputRouting = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _VIAMet52Met6forSRLatchInputRouting['_ViaMet52Met6NumberOfCOX'] = 2
        _VIAMet52Met6forSRLatchInputRouting['_ViaMet52Met6NumberOfCOY'] = 2
        _VIAMet62Met7forSRLatchInputRouting = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _VIAMet62Met7forSRLatchInputRouting['_ViaMet62Met7NumberOfCOX'] = 2
        _VIAMet62Met7forSRLatchInputRouting['_ViaMet62Met7NumberOfCOY'] = 2


        self._DesignParameter['_VIAMet42Met5forSRLatchInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='VIAMet42Met5forSRLatchInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_VIAMet42Met5forSRLatchInputRouting)

        self._DesignParameter['_VIAMet52Met6forSRLatchInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='VIAMet52Met6forSRLatchInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet52Met6forSRLatchInput']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_VIAMet52Met6forSRLatchInputRouting)

        self._DesignParameter['_VIAMet62Met7forSRLatchInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='VIAMet62Met7forSRLatchInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet62Met7forSRLatchInput']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_VIAMet62Met7forSRLatchInputRouting)







        print ('#################################       Coordinates Settings      #########################################')
        _XYCoordinateOfSlicer = [[0,0]]
        self._DesignParameter['_Slicer']['_XYCoordinates'] = _XYCoordinateOfSlicer
        PMOS_bottomtmp = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
        NMOS_toptmp = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']
        PMOS_Guardringbottom = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_bottomtmp
        NMOS_Guardringtop = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_toptmp
        VDD2VSSHeightofInverter = self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]


        self._DesignParameter['_SRLatch']['_XYCoordinates'] = [[_XYCoordinateOfSlicer[0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] +
                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2
                                                            +_DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace +
                                                            (self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 -
                                                            self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0]), int(round((PMOS_bottomtmp + NMOS_toptmp + 0.5) // 2))]]


        self._DesignParameter['_Inverter']['_XYCoordinates'] = [[_XYCoordinateOfSlicer[0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + \
                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2
                                                            +_DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace +
                                                            (self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 -
                                                                 self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0]), self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + \
                                                                 self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1] - VDD2VSSHeightofInverter]]


        PMOS_toptmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
        NMOS_bottomtmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
        _VDD2VSSHeightAtOneSide = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]

        #_CenterPoint = (PMOS_bottomtmp + NMOS_toptmp) // 2

        _ViaMet22Met3OnInverterOutput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMet22Met3OnInverterOutput['_ViaMet22Met3NumberOfCOX'] = 1

        PMOS2NMOSHeightofInverter= self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1]
        PMOSYofInverter = self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]

        _tmpNumY = int(self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _tmpNumY < 1 :
            _tmpNumY = 1

        _ViaMet22Met3OnInverterOutput['_ViaMet22Met3NumberOfCOY'] = _tmpNumY

        self._DesignParameter['_ViaMet22Met3OnInverterOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnInverterOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnInverterOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnInverterOutput)

        tmp = []
        for i in range(0, len(self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], \
                        self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet22Met3OnInverterOutput']['_XYCoordinates'] = tmp


        _ViaMet32Met4OnInverterOutput = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaMet32Met4OnInverterOutput['_ViaMet32Met4NumberOfCOX'] = 1
        _ViaMet32Met4OnInverterOutput['_ViaMet32Met4NumberOfCOY'] = _tmpNumY

        self._DesignParameter['_ViaMet32Met4OnInverterOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInverterOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnInverterOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnInverterOutput)

        tmp = []
        for i in range(0, len(self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], \
                        self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet32Met4OnInverterOutput']['_XYCoordinates'] = tmp

        _ViaMet42Met5OnInverterOutput = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaMet42Met5OnInverterOutput['_ViaMet42Met5NumberOfCOX'] = 1
        _ViaMet42Met5OnInverterOutput['_ViaMet42Met5NumberOfCOY'] = _tmpNumY

        self._DesignParameter['_ViaMet42Met5OnInverterOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInverterOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnInverterOutput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaMet42Met5OnInverterOutput)

        tmp = []
        for i in range(0, len(self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], \
                        self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet42Met5OnInverterOutput']['_XYCoordinates'] = tmp

        del tmp


        NMOS_righttmp = self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_righttmp']['_Ignore']
        Slicer_righttmp = self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0]
        Slicer_lefttmp = self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0]#### + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][0][0]


        # self._DesignParameter['_CLKMet3Output'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=None)
        # self._DesignParameter['_CLKMet3Output']['_Width'] = 4 * _DRCObj._MetalxMinWidth
        # self._DesignParameter['_CLKMet3Output']['_XYCoordinates'] = [[[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], PMOSYofInverter], \
        #                                                                [(NMOS_righttmp), PMOSYofInverter]]]

        self._DesignParameter['_CLKMet3Output'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=None)
        self._DesignParameter['_CLKMet3Output']['_Width'] = 4 * _DRCObj._MetalxMinWidth
        self._DesignParameter['_CLKMet3Output']['_XYCoordinates'] = [[[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], \
                                                                       self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
                                                                      [self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], \
                                                                        self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]]
                                                                     ]]


        # _ViaMet32Met4forCLKRouting = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        # _ViaMet32Met4forCLKRouting['_ViaMet32Met4NumberOfCOX'] = 2
        # _ViaMet32Met4forCLKRouting['_ViaMet32Met4NumberOfCOY'] = 2
        #
        # self._DesignParameter['_ViaMet32Met4forCLKRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forCLKRoutingIn{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet32Met4forCLKRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaMet32Met4forCLKRouting)
        # self._DesignParameter['_ViaMet32Met4forCLKRouting']['_XYCoordinates'] = [[(NMOS_righttmp), PMOSYofInverter]]
        #
        # _ViaMet42Met5forCLKRoutingOutput = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        # _ViaMet42Met5forCLKRoutingOutput['_ViaMet42Met5NumberOfCOX'] = 2
        # _ViaMet42Met5forCLKRoutingOutput['_ViaMet42Met5NumberOfCOY'] = 2
        #
        # self._DesignParameter['_ViaMet42Met5forCLKRoutingOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forCLKRoutingOutputIn{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet42Met5forCLKRoutingOutput']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaMet42Met5forCLKRoutingOutput)
        # self._DesignParameter['_ViaMet42Met5forCLKRoutingOutput']['_XYCoordinates'] = [[(NMOS_righttmp), PMOSYofInverter]]


        ############################## Metal5 Routing Version ##############################


        self._DesignParameter['_Met5RoutingforSRInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met5RoutingforSRInput']['_Width'] = 4 * _DRCObj._MetalxMinWidth



        if _SLPMOSFinger > 1 :
            self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1][0] + self._DesignParameter['_VIAMet42Met5forSSpRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4PNMOS']['_Width'] // 2, \
                                                                                      PMOS_bottomtmp]] ####_CenterPoint + self._DesignParameter['_Met5RoutingforSRInput']['_Width'] // 2 + _DRCObj._MetalxMinSpace9 // 2]]

        elif _SLPMOSFinger == 1 :
            self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1][0], \
                                                                                      PMOS_bottomtmp]] ####_CenterPoint + self._DesignParameter['_Met5RoutingforSRInput']['_Width'] // 2 + _DRCObj._MetalxMinSpace9 // 2]]

        if _SLNMOSFinger > 1:
             self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - (self._DesignParameter['_VIAMet42Met5forSSpRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4PNMOS']['_Width'] // 2), \
                                                                                       NMOS_toptmp]] ####_CenterPoint - self._DesignParameter['_Met5RoutingforSRInput']['_Width'] // 2 - _DRCObj._MetalxMinSpace9 // 2]]

        elif _SLNMOSFinger == 1 :
             self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], \
                                                                                       NMOS_toptmp]] ####_CenterPoint - self._DesignParameter['_Met5RoutingforSRInput']['_Width'] // 2 - _DRCObj._MetalxMinSpace9 // 2]]


        self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1]], \
                                                                                   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0],  self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_Met5RoutingforSRInput']['_XYCoordinates'] = [[self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0],  self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1]],\
                                                                             [self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0], self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0]]]


        self._DesignParameter['_CLKMet5Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=None)
        self._DesignParameter['_CLKMet5Routing']['_Width'] = 4 * _DRCObj._MetalxMinWidth


        CenterofCLKMOSofSlicer = (self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1]) // 2

        if (self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAMet42Met5forSSnRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] // 2) - (CenterofCLKMOSofSlicer + self._DesignParameter['_CLKMet5Routing']['_Width'] // 2) < _DRCObj._Metal1MinSpace21 :
            CenterofCLKMOSofSlicer = (self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAMet42Met5forSSnRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] // 2) - self._DesignParameter['_CLKMet5Routing']['_Width'] // 2 - _DRCObj._Metal1MinSpace21


        # self._DesignParameter['_CLKMet4Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_Width=None)
        # self._DesignParameter['_CLKMet4Routing']['_Width'] = 4 * _DRCObj._MetalxMinWidth
        # self._DesignParameter['_CLKMet4Routing']['_XYCoordinates'] = [[[(NMOS_righttmp + Slicer_righttmp) // 2, PMOSYofInverter], [(NMOS_righttmp + Slicer_righttmp) // 2, CenterofCLKMOSofSlicer]]]


        _ViaMet42Met5forCLKRouting = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaMet42Met5forCLKRouting['_ViaMet42Met5NumberOfCOX'] = 2
        _ViaMet42Met5forCLKRouting['_ViaMet42Met5NumberOfCOY'] = 2

        self._DesignParameter['_ViaMet42Met5forCLKRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forCLKRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5forCLKRouting']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaMet42Met5forCLKRouting)
        self._DesignParameter['_ViaMet42Met5forCLKRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0], CenterofCLKMOSofSlicer],\
                                                                                 [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0], CenterofCLKMOSofSlicer]]


        _ViaMet52Met6forCLKRouting = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaMet52Met6forCLKRouting['_ViaMet52Met6NumberOfCOX'] = 2
        _ViaMet52Met6forCLKRouting['_ViaMet52Met6NumberOfCOY'] = 2

        self._DesignParameter['_ViaMet52Met6forCLKRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6forCLKRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6forCLKRouting']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**_ViaMet52Met6forCLKRouting)
        self._DesignParameter['_ViaMet52Met6forCLKRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0], CenterofCLKMOSofSlicer], [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0], PMOSYofInverter]]





        self._DesignParameter['_CLKMet5Routing']['_XYCoordinates'] = [[[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], \
                                                                        self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                                                       [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet52Met6forCLKRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2, PMOSYofInverter]
                                                                     ],
                                                                    [[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0], CenterofCLKMOSofSlicer], [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0], CenterofCLKMOSofSlicer]]]
                                                                    #   [[(NMOS_righttmp + Slicer_righttmp) // 2 - self._DesignParameter['_ViaMet52Met6forCLKRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2, PMOSYofInverter], [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet52Met6forCLKRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2, PMOSYofInverter]]]

        self._DesignParameter['_CLKMet6Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[],_Width=None)
        self._DesignParameter['_CLKMet6Routing']['_Width'] = 4 * _DRCObj._MetalxMinWidth
        self._DesignParameter['_CLKMet6Routing']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0], CenterofCLKMOSofSlicer], [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0], PMOSYofInverter]]]


        _ViaMet32Met4forCLKInput = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaMet32Met4forCLKInput['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][0]) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 4
        _ViaMet32Met4forCLKInput['_ViaMet32Met4NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet32Met4forCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forCLKInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4forCLKInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4forCLKInput)
        self._DesignParameter['_ViaMet32Met4forCLKInput']['_XYCoordinates'] = [[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + (self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][1][0]) // 2, \
                                                                                self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + (self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][1][1]) // 2]]

        _ViaMet42Met5forCLKInput = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaMet42Met5forCLKInput['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][0]) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 4
        _ViaMet42Met5forCLKInput['_ViaMet42Met5NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet42Met5forCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forCLKInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaMet42Met5forCLKInput)
        self._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'] = [[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + (self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][1][0]) // 2, \
                                                                                self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + (self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Met3InRouting']['_XYCoordinates'][0][1][1]) // 2]]









        self._DesignParameter['_PinVDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_PinVSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_PinInputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp')
        self._DesignParameter['_PinInputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn')
        self._DesignParameter['_PinOutputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSp')
        self._DesignParameter['_PinOutputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSn')
        self._DesignParameter['_PinCLK'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK')
        self._DesignParameter['_OUTpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUT')
        self._DesignParameter['_OUTbpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUTb')



        self._DesignParameter['_PinVDD']['_XYCoordinates'] = [[0, PMOS_toptmp + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinVSS']['_XYCoordinates'] = [[0, NMOS_bottomtmp + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputP']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputN']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinOutputN']['_XYCoordinates'] = [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0]]
        self._DesignParameter['_PinOutputP']['_XYCoordinates'] = [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]
        self._DesignParameter['_OUTpin']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUTbpin']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][1][1]]]

        self._DesignParameter['_PinCLK']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                            ]


        SRLatch_vsstmp = self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1]
        Inverter_vsstmp = self._DesignParameter['_Inverter']['_XYCoordinates'][0][1]

        self._DesignParameter['_VSSMet1Supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_VSSMet1Supply']['_Width'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

        self._DesignParameter['_VSSMet1Supply']['_XYCoordinates'] = [[[_XYCoordinateOfSlicer[0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0], SRLatch_vsstmp], self._DesignParameter['_SRLatch']['_XYCoordinates'][0]]]


        print ('#################################       Design Constraints      #########################################')
        # if _InvChannelWidth > 250 :
        #     print("<_InvChannelWidth> should be smaller than 200nm.")
        #     raise NotImplementedError

        # if self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][1][1] - _SLSlicerGuardringWidth > self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 :
        #     raise NotImplementedError



        print ('#################################       Supply Line Routing      #########################################')
        if _SLSRInvSupplyLine == True :
            # if self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][1][1] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_YWidth'] // 2 > self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 :
            #     self._DesignParameter['_GuardringMet1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            #     self._DesignParameter['_GuardringMet1Routing']['_Width'] = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XWidth']
            #     self._DesignParameter['_GuardringMet1Routing']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][1][0], self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][1][1]], \
            #                                                                      [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][1][0], self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]]]
            #
            #toptmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['toptmp']['_Ignore']

            self._DesignParameter['_Met3VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3VDDRouting']['_Width'] = _SLGuardringWidth

            self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'] = [[[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp],
                                                                           [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp]]]

            _ViaNumSupplyX = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaNumSupplyY = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaNumSupplyX <= 1:
                _ViaNumSupplyX = 1
                _ViaNumSupplyY = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaNumSupplyY <= 1:
                _ViaNumSupplyY = 1
                _ViaNumSupplyX = int((self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet12Met2forVDDinINV = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaMet12Met2forVDDinINV['_ViaMet12Met2NumberOfCOX'] = _ViaNumSupplyX
            _ViaMet12Met2forVDDinINV['_ViaMet12Met2NumberOfCOY'] = _ViaNumSupplyY
            self._DesignParameter['_ViaMet12Met2forVDDinINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forVDDinINVIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2forVDDinINV']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forVDDinINV)
            self._DesignParameter['_ViaMet12Met2forVDDinINV']['_XYCoordinates'] = [[self._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]

            self._DesignParameter['_Met2LayerforVDDinInv'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_Met2LayerforVDDinInv']['_XWidth'] = self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met2LayerforVDDinInv']['_YWidth'] = self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            self._DesignParameter['_Met2LayerforVDDinInv']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2forVDDinINV']['_XYCoordinates']

            self._DesignParameter['_VSSMet2Supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_VSSMet2Supply']['_Width'] =  self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            self._DesignParameter['_VSSMet2Supply']['_XYCoordinates'] = [[[_XYCoordinateOfSlicer[0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0], Inverter_vsstmp], self._DesignParameter['_Inverter']['_XYCoordinates'][0]]]

            # self._DesignParameter['_Met2forVSSforInvandSlicer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met2forVSSforInvandSlicer']['_Width'] = _SLGuardringWidth
            # self._DesignParameter['_Met2forVSSforInvandSlicer']['_XYCoordinates'] = [[[Slicer_righttmp, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates'][0][1]], [Slicer_righttmp, Inverter_vsstmp - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]], \
            #                                                                          [[Slicer_lefttmp, self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates'][0][1]], [Slicer_lefttmp, Inverter_vsstmp - self._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]]]
            #

        if _InvFinger < 5 :
            print('Finger of Inverter should be larger than 4!')
            raise NotImplementedError

            # # self._DesignParameter['_Met4VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            # # self._DesignParameter['_Met4VDDRouting']['_Width'] = 6 * _DRCObj._MetalxMinWidth
            # # self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'] = [[[max(self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2) + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2 + _DRCObj._MetalxMinSpace5, self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3VDDRouting']['_Width'] // 2], \
            # #                                                                [max(self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2) + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2 + _DRCObj._MetalxMinSpace5, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1] - self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]]
            # #                                                               ]
            #
            # # [Slicer_righttmp + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2,
            # #  self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'][0][0][1] +
            # #  self._DesignParameter['_Met3VDDRouting']['_Width'] // 2], \
            # # [Slicer_righttmp + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2,
            # #  self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] +
            # #  self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1] -
            # #  self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact'][
            # #      '_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]]
            #
            # Ptoptmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][1]
            # SRtoptmp = self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]
            #
            #
            # _ViaXWidthofSR = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            # _ViaYWidthofSR = abs((self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + Ptoptmp + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_YWidth'] // 2) - (SRtoptmp - self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))
            # _ViaXCenterofSR = self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0]
            # _ViaYCenterofSR = ((self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + Ptoptmp + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_YWidth'] // 2) + (SRtoptmp - self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2
            #
            # _ViaNumVDDX12ofSRLatch = int((self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            # _ViaNumVDDY12ofSRLatch = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDX12ofSRLatch <= 1:
            #     _ViaNumVDDX12ofSRLatch = 1
            #     _ViaNumVDDY12ofSRLatch = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            # if _ViaNumVDDY12ofSRLatch <= 1:
            #     _ViaNumVDDY12ofSRLatch = 1
            #     _ViaNumVDDX12ofSRLatch = int((_ViaXWidthofSR - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12ofSRLatch
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY12ofSRLatch
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVDDMet12Met2)
            #
            # tmp = []
            # tmp.append([_ViaXCenterofSR, _ViaYCenterofSR])
            #
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], _ViaYCenterofSR]]
            #
            # _ViaNumVDDX23ofSRLatch = int((_ViaXWidthofSR - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            # _ViaNumVDDY23ofSRLatch = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDX23ofSRLatch <= 1:
            #     _ViaNumVDDX23ofSRLatch = 1
            #     _ViaNumVDDY23ofSRLatch = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDY23ofSRLatch <= 1:
            #     _ViaNumVDDY23ofSRLatch = 1
            #     _ViaNumVDDX23ofSRLatch = int((_ViaXWidthofSR - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX23ofSRLatch
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY23ofSRLatch
            # self._DesignParameter['_ViaMet22Met3VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaVDDMet22Met3)
            #
            # self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            # del tmp
            #
            #
            # self._DesignParameter['_Met1forSRVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met1forSRVDD']['_XWidth'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            # self._DesignParameter['_Met1forSRVDD']['_YWidth'] = _ViaYWidthofSR
            #
            # self._DesignParameter['_Met2forSRVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met2forSRVDD']['_XWidth'] = _ViaXWidthofSR
            # self._DesignParameter['_Met2forSRVDD']['_YWidth'] = _ViaYWidthofSR
            #
            # self._DesignParameter['_Met3forSRVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met3forSRVDD']['_XWidth'] = _ViaXWidthofSR
            # self._DesignParameter['_Met3forSRVDD']['_YWidth'] = _ViaYWidthofSR
            #
            #
            # self._DesignParameter['_Met1forSRVDD']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], _ViaYCenterofSR]]
            #
            # tmp = []
            #
            # tmp.append([_ViaXCenterofSR, _ViaYCenterofSR])
            #
            # self._DesignParameter['_Met2forSRVDD']['_XYCoordinates'] = tmp
            #
            # del tmp
            #
            # tmp = []
            #
            # tmp.append([_ViaXCenterofSR, _ViaYCenterofSR])
            #
            # self._DesignParameter['_Met3forSRVDD']['_XYCoordinates'] = tmp
            #
            #
            #
            # _ViaNumVDDX = int((_ViaXWidthofSR - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            # _ViaNumVDDY = int((self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDX <= 1:
            #     _ViaNumVDDX = 1
            #     _ViaNumVDDY = int((self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            # if _ViaNumVDDY <= 1:
            #     _ViaNumVDDY = 1
            #     _ViaNumVDDX = int((_ViaXWidthofSR - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12ofSRLatch
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY
            # self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VDDIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVDDMet12Met2)
            # self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = [[_ViaXCenterofSR, \
            #                                                                 self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]
            #
            # _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY
            # self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VDDIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVDDMet22Met3)
            # self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = [[_ViaXCenterofSR, \
            #                                                                 self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]
            #
            # self._DesignParameter['_Met1LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #
            # self._DesignParameter['_Met1LayerVDD']['_XWidth'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            # self._DesignParameter['_Met1LayerVDD']['_YWidth'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _ViaXWidthofSR
            # self._DesignParameter['_Met2LayerVDD']['_YWidth'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_Met3LayerVDD']['_XWidth'] = _ViaXWidthofSR
            # self._DesignParameter['_Met3LayerVDD']['_YWidth'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            #
            #
            # self._DesignParameter['_Met1LayerVDD']['_XYCoordinates'] = [[_ViaXCenterofSR, \
            #                                                                 self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]
            #
            # self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = [[_ViaXCenterofSR, \
            #                                                                 self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]
            #
            # self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = [[_ViaXCenterofSR, \
            #                                                                 self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]

#########################################


            # _ViaNumVDDX34ofSRLatch1 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            # _ViaNumVDDY34ofSRLatch1 = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDX34ofSRLatch1 <= 1:
            #     _ViaNumVDDX34ofSRLatch1 = 1
            #     _ViaNumVDDY34ofSRLatch1 = int((_ViaYWidthofSR - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDY34ofSRLatch1 <= 1:
            #     _ViaNumVDDY34ofSRLatch1 = 1
            #     _ViaNumVDDX34ofSRLatch1 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX34ofSRLatch1
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY34ofSRLatch1
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4VDDofSRLatch1In{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVDDMet32Met4)
            #
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch1']['_XYCoordinates'] = [[self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_XYCoordinates'][0][1]]]
            #
            # del _ViaVDDMet32Met4


            # _ViaNumVDDX34ofSRLatch2 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            # _ViaNumVDDY34ofSRLatch2 = int((self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDX34ofSRLatch2 <= 1:
            #     _ViaNumVDDX34ofSRLatch2 = 1
            #     _ViaNumVDDY34ofSRLatch2 = int((self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # if _ViaNumVDDY34ofSRLatch2 <= 1:
            #     _ViaNumVDDY34ofSRLatch2 = 1
            #     _ViaNumVDDX34ofSRLatch2 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            #
            # _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX34ofSRLatch2
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY34ofSRLatch2
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4VDDofSRLatch2In{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVDDMet32Met4)
            #
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch2']['_XYCoordinates'] = [[self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'][0][1]]]
            #
            #
            # del _ViaVDDMet32Met4

            # self._DesignParameter['_AdditionalMet3forVDD1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_AdditionalMet3forVDD1']['_Width'] = _ViaYWidthofSR
            # self._DesignParameter['_AdditionalMet3forVDD1']['_XYCoordinates'] = [[[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], _ViaYCenterofSR], \
            #                                                                      [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2, _ViaYCenterofSR]]]
            #
            #
            # self._DesignParameter['_AdditionalMet3forVDD2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_AdditionalMet3forVDD2']['_Width'] = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_AdditionalMet3forVDD2']['_XYCoordinates'] = [[[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]], \
            #                                                                      [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] + self._DesignParameter['_Met4VDDRouting']['_Width'] // 2, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]]]





if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'

    SlicerWithSRLatchObj = _SlicerWithSRLatch(_DesignParameter=None, _Name='SlicerWithSRLatch')

    for _tries in range(1, 2) :
        #####################SRLatch#######################
        _SRFinger1 = 5##random.randint(1, 16)
        _SRFinger2 = 1##random.randint(1, 16)
        _SRFinger3 = 2##random.randint(1, 16)
        _SRFinger4 = 2##random.randint(1, 16)
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
        _SRPowerLine = None
        #####################Slicer#######################
        _SLCLKinputPMOSFinger1 = 6##random.randint(1, 16)
        _SLCLKinputPMOSFinger2 = 2##random.randint(1, 16)
        _SLPMOSFinger = 2##random.randint(1, 16)
        _SLPMOSChannelWidth = 1000##random.randrange(200, 1050, 50)
        _SLDATAinputNMOSFinger = 12##random.randint(2, 16)
        _SLNMOSFinger = 2##random.randint(1, 16)
        _SLCLKinputNMOSFinger = 8##random.randint(1, 16)
        _SLNMOSChannelWidth = 1000##random.randrange(200, 1050, 50)
        _SLCLKinputNMOSChannelWidth = 1000

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
        _SLPowerLine = None
        #####################Inverter#######################
        _InvFinger = 16##random.randint(5, 16)
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
        #####################Power Line#######################
        _SLSRInvSupplyLine = True


        SlicerWithSRLatchObj._CalculateDesignParameter(_SRFinger1 = _SRFinger1, _SRFinger2 = _SRFinger2, _SRFinger3 = _SRFinger3, _SRFinger4 = _SRFinger4,
                                      _SRNMOSChannelWidth1 = _SRNMOSChannelWidth1, _SRPMOSChannelWidth1 = _SRPMOSChannelWidth1, _SRNMOSChannelWidth2 = _SRNMOSChannelWidth2, _SRPMOSChannelWidth2 = _SRPMOSChannelWidth2,
                                      _SRNMOSChannelWidth3 = _SRNMOSChannelWidth3, _SRPMOSChannelWidth3 = _SRPMOSChannelWidth3, _SRNMOSChannelWidth4 = _SRNMOSChannelWidth4, _SRPMOSChannelWidth4 = _SRPMOSChannelWidth4,
                                      _SRChannelLength = _SRChannelLength, _SRNPRatio = _SRNPRatio,
                                      _SRVDD2VSSHeightAtOneSide = _SRVDD2VSSHeightAtOneSide, _SRDummy = _SRDummy, _SRNumSupplyCoX = _SRNumSupplyCoX, _SRNumSupplyCoY = _SRNumSupplyCoY,
                                      _SRSupplyMet1XWidth = _SRSupplyMet1XWidth, _SRSupplyMet1YWidth = _SRSupplyMet1YWidth, _SRNumViaPoly2Met1CoX = _SRNumViaPoly2Met1CoX, \
                                      _SRNumViaPoly2Met1CoY = _SRNumViaPoly2Met1CoY, _SRNumViaPMOSMet12Met2CoX = _SRNumViaPMOSMet12Met2CoX, _SRNumViaPMOSMet12Met2CoY = _SRNumViaPMOSMet12Met2CoY,
                                      _SRNumViaNMOSMet12Met2CoX = _SRNumViaNMOSMet12Met2CoX, _SRNumViaNMOSMet12Met2CoY = _SRNumViaNMOSMet12Met2CoY, _SRNumViaPMOSMet22Met3CoX = _SRNumViaPMOSMet22Met3CoX, _SRNumViaPMOSMet22Met3CoY = _SRNumViaPMOSMet22Met3CoY,
                                      _SRNumViaNMOSMet22Met3CoX = _SRNumViaNMOSMet22Met3CoX, _SRNumViaNMOSMet22Met3CoY = _SRNumViaNMOSMet22Met3CoY, _SRSLVT = _SRSLVT, _SRPowerLine = _SRPowerLine,
                                      _SLCLKinputPMOSFinger1 = _SLCLKinputPMOSFinger1, _SLCLKinputPMOSFinger2 = _SLCLKinputPMOSFinger2, _SLPMOSFinger = _SLPMOSFinger, _SLPMOSChannelWidth = _SLPMOSChannelWidth,
                                      _SLDATAinputNMOSFinger = _SLDATAinputNMOSFinger, _SLNMOSFinger = _SLNMOSFinger, _SLCLKinputNMOSFinger = _SLCLKinputNMOSFinger, _SLNMOSChannelWidth = _SLNMOSChannelWidth, _SLCLKinputNMOSChannelWidth=_SLCLKinputNMOSChannelWidth,
                                      _SLChannelLength = _SLChannelLength, _SLDummy = _SLDummy, _SLSLVT = _SLSLVT, _SLGuardringWidth = _SLGuardringWidth, _SLGuardring = _SLGuardring,
                                      _SLSlicerGuardringWidth=_SLSlicerGuardringWidth, _SLSlicerGuardring=_SLSlicerGuardring,
                                      _SLNumSupplyCOY=_SLNumSupplyCOY, _SLNumSupplyCOX=_SLNumSupplyCOX, _SLSupplyMet1XWidth=_SLSupplyMet1XWidth, _SLSupplyMet1YWidth=_SLSupplyMet1YWidth, _SLVDD2VSSHeight = _SLVDD2VSSHeight,
                                      _SLNumVIAPoly2Met1COX=_SLNumVIAPoly2Met1COX, _SLNumVIAPoly2Met1COY=_SLNumVIAPoly2Met1COY, _SLNumVIAMet12COX=_SLNumVIAMet12COX, _SLNumVIAMet12COY=_SLNumVIAMet12COY, _SLPowerLine = _SLPowerLine, \
                                      _InvFinger=_InvFinger, _InvChannelWidth=_InvChannelWidth, _InvChannelLength=_InvChannelLength, _InvNPRatio=_InvNPRatio,
                                      _InvVDD2VSSHeight=_InvVDD2VSSHeight, _InvDummy=_InvDummy, _InvNumSupplyCoX=_InvNumSupplyCoX,
                                      _InvNumSupplyCoY=_InvNumSupplyCoY, _InvSupplyMet1XWidth=_InvSupplyMet1XWidth,
                                      _InvSupplyMet1YWidth=_InvSupplyMet1YWidth, _InvNumViaPoly2Met1CoX=_InvNumViaPoly2Met1CoX, \
                                      _InvNumViaPoly2Met1CoY=_InvNumViaPoly2Met1CoY, _InvNumViaPMOSMet12Met2CoX=_InvNumViaPMOSMet12Met2CoX,
                                      _InvNumViaPMOSMet12Met2CoY=_InvNumViaPMOSMet12Met2CoY, _InvNumViaNMOSMet12Met2CoX=_InvNumViaNMOSMet12Met2CoX, \
                                      _InvNumViaNMOSMet12Met2CoY=_InvNumViaNMOSMet12Met2CoY, _InvSLVT=_InvSLVT, _InvPowerLine=_InvPowerLine, _SLSRInvSupplyLine=_SLSRInvSupplyLine
                                                       )

        # SlicerwithSRLatchObj._CalculateDesignParameter(_SRFinger1=10, _SRFinger2=10, _SRFinger3=10, _SRFinger4=10,
        #                                                _SRNMOSChannelWidth1=200, _SRPMOSChannelWidth1=400,
        #                                                _SRNMOSChannelWidth2=200, _SRPMOSChannelWidth2=400,
        #                                                _SRNMOSChannelWidth3=200, _SRPMOSChannelWidth3=400,
        #                                                _SRNMOSChannelWidth4=200, _SRPMOSChannelWidth4=400,
        #                                                _SRChannelLength=30, _SRNPRatio=None,
        #                                                _SRVDD2VSSHeightAtOneSide=None, _SRDummy=True, _SRNumSupplyCoX=None,
        #                                                _SRNumSupplyCoY=2,
        #                                                _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None,
        #                                                SRNumViaPoly2Met1CoX=None, \
        #                                                SRNumViaPoly2Met1CoY=None, SRNumViaPMOSMet12Met2CoX=None,
        #                                                SRNumViaPMOSMet12Met2CoY=None,
        #                                                SRNumViaNMOSMet12Met2CoX=None, SRNumViaNMOSMet12Met2CoY=None,
        #                                                SRNumViaPMOSMet22Met3CoX=None, SRNumViaPMOSMet22Met3CoY=None,
        #                                                SRNumViaNMOSMet22Met3CoX=None, SRNumViaNMOSMet22Met3CoY=None,
        #                                                _SRSLVT=True, _SRPowerLine=True,
        #                                                _SLCLKinputPMOSFinger1=12, _SLCLKinputPMOSFinger2=12, _SLPMOSFinger=12,
        #                                                _SLPMOSChannelWidth=1000,
        #                                                _SLDATAinputNMOSFinger=12, _SLNMOSFinger=12, _SLCLKinputNMOSFinger=12,
        #                                                _SLNMOSChannelWidth=1000,
        #                                                _SLChannelLength=30, _SLDummy=True, _SLSLVT=True,
        #                                                _SLGuardringWidth=200, _SLGuardring=True,
        #                                                _SLSlicerGuardringWidth=200, _SLSlicerGuardring=None,
        #                                                _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None,
        #                                                _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight=None,
        #                                                _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None,
        #                                                _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine=True)





        SlicerWithSRLatchObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = SlicerWithSRLatchObj._DesignParameter)
        _fileName = 'SlicerWithSRLatch.gds'
        testStreamFile = open('./{}'.format(_fileName), 'wb')

        tmp = SlicerWithSRLatchObj._CreateGDSStream(SlicerWithSRLatchObj._DesignParameter['_GDSFile']['_GDSFile'])

        tmp.write_binary_gds_stream(testStreamFile)

        testStreamFile.close()

        import ftplib

        #ftp = ftplib.FTP('141.223.29.61')
        #ftp.login('jicho0927', 'cho89140616!!')
        #ftp.cwd('/mnt/sda/jicho0927/OPUS/SAMSUNG28n')
        ftp = ftplib.FTP('141.223.22.156')
        ftp.login('jicho0927', 'cho89140616!!')
        ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
        myfile = open('SlicerWithSRLatch.gds', 'rb')
        ftp.storbinary('STOR SlicerWithSRLatch.gds', myfile)
        myfile.close()
        ftp.close()

    #     import DRCchecker
    #
    #     a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '//mnt//sdc//jicho0927//OPUS//SAMSUNG28n', '//mnt//sdc//jicho0927//OPUS//SAMSUNG28n//DRC//run', 'SlicerWithSRLatch_test', 'SlicerWithSRLatch')
    #
    #     a.DRCchecker()
    #
    #
    #     print('_tries = ', _tries)
    #     print('_SRFinger1 = ', _SRFinger1)
    #     print('_SRFinger2 = ', _SRFinger2)
    #     print('_SRFinger3 = ', _SRFinger3)
    #     print('_SRFinger4 = ', _SRFinger4)
    #
    #
    #     print('_CLKinputPMOSFinger1 = ', _SLCLKinputPMOSFinger1)
    #     print('_CLKinputPMOSFinger2 = ', _SLCLKinputPMOSFinger2)
    #     print('_PMOSFinger = ', _SLPMOSFinger)
    #     print('_PMOSChannelWidth = ', _SLPMOSChannelWidth)
    #     print('_DATAinputNMOSFinger = ', _SLDATAinputNMOSFinger)
    #     print('_NMOSFinger = ', _SLNMOSFinger)
    #     print('_CLKinputNMOSFinger = ', _SLCLKinputNMOSFinger)
    #     print('_NMOSChannelWidth = ', _SLNMOSChannelWidth)
    #
    #
    #     print('_InvFinger = ', _InvFinger)
    #
    # print ("DRCclean!!")








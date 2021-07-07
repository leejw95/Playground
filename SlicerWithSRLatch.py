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
import math

class _SlicerWithSRLatch (StickDiagram._StickDiagram) :

    _ParametersForDesignCalculation = dict(
                                    _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None, 
                                  _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                  SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None, \
                                  SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None, \
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False, 
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None)

    def __init__(self, _DesignParameter = None, _Name = 'SlicerWithSRLatch'):
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None, _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                  SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None, \
                                  SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None, \
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False) :


        print ('#########################################################################################################')
        print ('                                {}  SlicerWithSRLatch Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatch'

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
        _SRLatchinputs['NumViaPoly2Met1CoX'] = SRNumViaPoly2Met1CoX
        _SRLatchinputs['NumViaPoly2Met1CoY'] = SRNumViaPoly2Met1CoY
        _SRLatchinputs['NumViaPMOSMet12Met2CoX'] = SRNumViaPMOSMet12Met2CoX
        _SRLatchinputs['NumViaPMOSMet12Met2CoY'] = SRNumViaPMOSMet12Met2CoY
        _SRLatchinputs['NumViaNMOSMet12Met2CoX'] = SRNumViaNMOSMet12Met2CoX
        _SRLatchinputs['NumViaNMOSMet12Met2CoY'] = SRNumViaNMOSMet12Met2CoY
        _SRLatchinputs['NumViaPMOSMet22Met3CoX'] = SRNumViaPMOSMet22Met3CoX
        _SRLatchinputs['NumViaPMOSMet22Met3CoY'] = SRNumViaPMOSMet22Met3CoY
        _SRLatchinputs['NumViaNMOSMet22Met3CoX'] = SRNumViaNMOSMet22Met3CoX
        _SRLatchinputs['NumViaNMOSMet22Met3CoY'] = SRNumViaNMOSMet22Met3CoY
        _SRLatchinputs['_SLVT'] = _SRSLVT
        _SRLatchinputs['_PowerLine'] = _SRPowerLine



        self._DesignParameter['_SRLatch'] = self._SrefElementDeclaration(_DesignObj = SRLatch._SRLatch(_DesignParameter=None, _Name = "SRLatchIn{}".format(_Name)))[0]
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
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOX'] = 1
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOY'] = 4
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOX'] = 1
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOY'] = 4
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOX'] = 1
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOY'] = 4

        else :
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOX'] = 2
            _VIAMet42Met5forPMOSRouting['_ViaMet42Met5NumberOfCOY'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOX'] = 2
            _VIAMet52Met6forPMOSRouting['_ViaMet52Met6NumberOfCOY'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOX'] = 2
            _VIAMet62Met7forPMOSRouting['_ViaMet62Met7NumberOfCOY'] = 2

        if _SLNMOSFinger == 1:
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOX'] = 1
            _VIAMet42Met5forNMOSRouting['_ViaMet42Met5NumberOfCOY'] = 4
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOX'] = 1
            _VIAMet52Met6forNMOSRouting['_ViaMet52Met6NumberOfCOY'] = 4
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOX'] = 1
            _VIAMet62Met7forNMOSRouting['_ViaMet62Met7NumberOfCOY'] = 4

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
        self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_VIAMet42Met5forSRLatchInputRouting)

        self._DesignParameter['_VIAMet52Met6forSRLatchInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='VIAMet52Met6forSRLatchInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet52Met6forSRLatchInput']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_VIAMet52Met6forSRLatchInputRouting)

        self._DesignParameter['_VIAMet62Met7forSRLatchInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='VIAMet62Met7forSRLatchInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet62Met7forSRLatchInput']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_VIAMet62Met7forSRLatchInputRouting)







        print ('#################################       Coordinates Settings      #########################################')
        PMOS_bottomtmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
        NMOS_toptmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']
        _XYCoordinateOfSlicer = [[0,0]]
        self._DesignParameter['_Slicer']['_XYCoordinates'] = _XYCoordinateOfSlicer
        PMOS_Guardringbottom = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_bottomtmp
        NMOS_Guardringtop = self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_toptmp
        self._DesignParameter['_SRLatch']['_XYCoordinates'] = [[_XYCoordinateOfSlicer[0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0] +
                                                            self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XWidth'] // 2 +
                                                            +_DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace +
                                                            (self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 -
                                                            self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][0]), (PMOS_Guardringbottom + NMOS_Guardringtop) / 2]]
                                                           ## _XYCoordinateOfSlicer[0][1]]]

        PMOS_toptmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
        NMOS_bottomtmp = self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
        _VDD2VSSHeightAtOneSide = self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]



        if _SLPMOSFinger > 1 :
            self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0] + 40, \
                                                                                      self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_VIAMet52Met6forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0] + 40, \
                                                                                      self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_VIAMet62Met7forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0] + 40, \
                                                                                      self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]

        elif _SLPMOSFinger == 1 :
            self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_VIAMet52Met6forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_VIAMet62Met7forSSpRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0][1]]]

        if _SLNMOSFinger > 1:
             self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - 40, \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]
             self._DesignParameter['_VIAMet52Met6forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - 40, \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]
             self._DesignParameter['_VIAMet62Met7forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - 40, \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]

        elif _SLNMOSFinger == 1 :
             self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]
             self._DesignParameter['_VIAMet52Met6forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]
             self._DesignParameter['_VIAMet62Met7forSSnRouting']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], \
                                                                                    self._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0][1]]]


        self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinSpace9], \
                                                                                   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace9]]
        self._DesignParameter['_VIAMet52Met6forSRLatchInput']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinSpace9], \
                                                                                   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace9]]
        self._DesignParameter['_VIAMet62Met7forSRLatchInput']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinSpace9], \
                                                                                   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace9]]

        self._DesignParameter['_Met7RoutingforSRInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met7RoutingforSRInput']['_Width'] = 4 * _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met7RoutingforSRInput']['_XYCoordinates'] = [[self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0],  [self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1][1]], self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1]],\
                                                                             [self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0], [self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0][1]], self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0]]]


        self._DesignParameter['_Met5forShieldingSRInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met5forShieldingSRInput']['_Width'] = 8 * _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met5forShieldingSRInput']['_XYCoordinates'] = [[[ self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_Met7RoutingforSRInput']['_Width'] / 2 + _DRCObj._MetalxMinSpace9, self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1][1]], [self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/ 2 - _DRCObj._MetalxMinSpace9, self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][1][1]]], \
                                                                               [[ self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_Met7RoutingforSRInput']['_Width'] / 2 + _DRCObj._MetalxMinSpace9, self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/ 2 - _DRCObj._MetalxMinSpace9, self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_Met5forBoundaryShieldingSRInput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)



                                                                            # [[self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0], [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0], self._DesignParameter['_VIAMet42Met5forSSpRouting']['_XYCoordinates'][0][1]],\
                                                                            #  [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1]],\
                                                                            #   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1]]], \
                                                                            #  [self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0], [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0], self._DesignParameter['_VIAMet42Met5forSSnRouting']['_XYCoordinates'][0][1]], \
                                                                            #   [self._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'][1][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]], \
                                                                            #   [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]]]]
                                                                            #


        # self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]], \
        #                                                                            [self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0] - self._DesignParameter['_VIAMet42Met5forSRLatchInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1]]]






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
        self._DesignParameter['_PinOutputP']['_XYCoordinates'] = [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2]]
        self._DesignParameter['_OUTpin']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUTbpin']['_XYCoordinates'] = [[self._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_PinCLK']['_XYCoordinates'] = [[self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                            ]




        # print ('#################################       Supply Line Routing      #########################################')
        # if _SRPowerLine == True and _SLPowerLine == True :




if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'

    SlicerWithSRLatchObj = _SlicerWithSRLatch(_DesignParameter=None, _Name='SlicerWithSRLatch')
    SlicerWithSRLatchObj._CalculateDesignParameter(_SRFinger1 = 3, _SRFinger2 = 3, _SRFinger3 = 3, _SRFinger4 = 3,
                                  _SRNMOSChannelWidth1 = 200, _SRPMOSChannelWidth1 = 400, _SRNMOSChannelWidth2 = 200, _SRPMOSChannelWidth2 = 400,
                                  _SRNMOSChannelWidth3 = 200, _SRPMOSChannelWidth3 = 400, _SRNMOSChannelWidth4 = 200, _SRPMOSChannelWidth4 = 400,
                                  _SRChannelLength = 30, _SRNPRatio = None,
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = True, _SRNumSupplyCoX = None, _SRNumSupplyCoY = 2,
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                  SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None,
                                  SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None,
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = True, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = 3, _SLCLKinputPMOSFinger2 = 3, _SLPMOSFinger = 3, _SLPMOSChannelWidth = 1000,
                                    _SLDATAinputNMOSFinger = 3, _SLNMOSFinger = 3, _SLCLKinputNMOSFinger = 3, _SLNMOSChannelWidth = 1000,
                                    _SLChannelLength = 30, _SLDummy = True, _SLSLVT = True, _SLGuardringWidth = 200, _SLGuardring = True,
                                    _SLSlicerGuardringWidth=200, _SLSlicerGuardring=None,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False)

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

    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    # myfile = open('SlicerWithSRLatch.gds', 'rb')
    # ftp.storbinary('STOR SlicerWithSRLatch.gds', myfile)
    # myfile.close()
    # ftp.close()
    #
    # ftp = ftplib.FTP('141.223.29.61')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    # myfile = open('SlicerWithSRLatch.gds', 'rb')
    # ftp.storbinary('STOR SlicerWithSRLatch.gds', myfile)
    # myfile.close()
    # ftp.close()
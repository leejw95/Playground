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
import Slicer
import SR_Latch
import math

class _SlicerwithSRLatch (StickDiagram._StickDiagram) :

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

    def __init__(self, _DesignParameter = None, _Name = 'SlicerwithSRLatch'):
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
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _PowerLine = False,
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None) :


        print ('#########################################################################################################')
        print ('                                {}  SlicerwithSRLatch Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerwithSRLatch'

        print ('###############################        SRLatch Generation       #########################################')

        _SRLatchinputs = copy.deepcopy(SR_Latch._SRLatch._ParametersForDesignCalculation)
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
        _SRLatchinputs['_PowerLine'] = _PowerLine



        self._DesignParameter['_SRLatch'] = self._SrefElementDeclaration(_DesignObj = SR_Latch._SRLatch(_DesignParameter=None, _Name = "SRLatchIn{}".format(_Name)))[0]
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

        self._DesignParameter['_Slicer'] = self._SrefElementDeclaration(_DesignObj = Slicer._Slicer(_DesignParameter=None, _Name = "SlicerIn{}".format(_Name)))[0]
        self._DesignParameter['_SRLatch']['_DesignObj']._CalculateDesignParameter(**_Slicerinputs)

        
        
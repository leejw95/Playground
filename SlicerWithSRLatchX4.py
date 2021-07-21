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
import SlicerWithSRLatch

import math

class SlicerWithSRLatchX4Obj (StickDiagram._StickDiagram) :

    _ParametersForDesignCalculation = dict(
                                    _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None,
                                  _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, _SRNumViaPoly2Met1CoX = None, \
                                  _SRNumViaPoly2Met1CoY = None, _SRNumViaPMOSMet12Met2CoX = None, _SRNumViaPMOSMet12Met2CoY = None, \
                                  _SRNumViaNMOSMet12Met2CoX = None, _SRNumViaNMOSMet12Met2CoY = None, _SRNumViaPMOSMet22Met3CoX = None, _SRNumViaPMOSMet22Met3CoY = None, \
                                  _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = None,
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
                                _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None
    )

    def __init__(self, _DesignParameter = None, _Name = 'SlicerWithSRLatchX4'):
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
                                    _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = None,
                                    _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = None, _NumberofSlicerWithSRLatch = None, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
                                  _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
                                  _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvSLVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None
                                  ) :




        print ('#########################################################################################################')
        print ('                                {}  SlicerWithSRLatchX4Obj Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatchX4'


        print ('###############################        Supply Generation       #########################################')


        if _SLSRInvSupplyLineX4 == True :
            _SRPowerLine = True
            _SLPowerLine = False
            _InvPowerLine = False

        elif _SLSRInvSupplyLineX4 == False :
            _SRPowerLine = False
            _SLPowerLine = False
            _InvPowerLine = False


        # if _SLSRInvSupplyLineX4 != None :
        #     _SRPowerLine = False
        #     _SLPowerLine = False
        #     _InvPowerLine = False
        #
        # elif _SLSRInvSupplyLineX4 == None :
        #     _SRPowerLine = False
        #     _SLPowerLine = False
        #     _InvPowerLine = False


        print ('###############################        SlicerWithSRLatch Generation       #########################################')

        _SlicerWithSRLatchEdgeinputs = copy.deepcopy(SlicerWithSRLatch._SlicerWithSRLatch._ParametersForDesignCalculation)
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



        _SlicerWithSRLatchEdgeinputs['_InvFinger']= _InvFinger
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

        _SlicerWithSRLatchEdgeinputs['_SLSRInvSupplyLine'] = None





        # _SlicerWithSRLatchXinputs = copy.deepcopy(SlicerWithSRLatch._SlicerWithSRLatch._ParametersForDesignCalculation)
        # _SlicerWithSRLatchXinputs['_SRFinger1'] = _SRFinger1
        # _SlicerWithSRLatchXinputs['_SRFinger2'] = _SRFinger2
        # _SlicerWithSRLatchXinputs['_SRFinger3'] = _SRFinger3
        # _SlicerWithSRLatchXinputs['_SRFinger4'] = _SRFinger4
        # _SlicerWithSRLatchXinputs['_SRNMOSChannelWidth1'] = _SRNMOSChannelWidth1
        # _SlicerWithSRLatchXinputs['_SRPMOSChannelWidth1'] = _SRPMOSChannelWidth1
        # _SlicerWithSRLatchXinputs['_SRNMOSChannelWidth2'] = _SRNMOSChannelWidth2
        # _SlicerWithSRLatchXinputs['_SRPMOSChannelWidth2'] = _SRPMOSChannelWidth2
        # _SlicerWithSRLatchXinputs['_SRNMOSChannelWidth3'] = _SRNMOSChannelWidth3
        # _SlicerWithSRLatchXinputs['_SRPMOSChannelWidth3'] = _SRPMOSChannelWidth3
        # _SlicerWithSRLatchXinputs['_SRNMOSChannelWidth4'] = _SRNMOSChannelWidth4
        # _SlicerWithSRLatchXinputs['_SRPMOSChannelWidth4'] = _SRPMOSChannelWidth4
        # _SlicerWithSRLatchXinputs['_SRChannelLength'] = _SRChannelLength
        # _SlicerWithSRLatchXinputs['_SRNPRatio'] = _SRNPRatio
        # _SlicerWithSRLatchXinputs['_SRVDD2VSSHeightAtOneSide'] = _SRVDD2VSSHeightAtOneSide
        # _SlicerWithSRLatchXinputs['_SRDummy'] = _SRDummy
        # _SlicerWithSRLatchXinputs['_SRNumSupplyCoX'] = _SRNumSupplyCoX
        # _SlicerWithSRLatchXinputs['_SRNumSupplyCoY'] = _SRNumSupplyCoY
        # _SlicerWithSRLatchXinputs['_SRSupplyMet1XWidth'] = _SRSupplyMet1XWidth
        # _SlicerWithSRLatchXinputs['_SRSupplyMet1YWidth'] = _SRSupplyMet1YWidth
        # _SlicerWithSRLatchXinputs['SRNumViaPoly2Met1CoX'] = SRNumViaPoly2Met1CoX
        # _SlicerWithSRLatchXinputs['SRNumViaPoly2Met1CoY'] = SRNumViaPoly2Met1CoY
        # _SlicerWithSRLatchXinputs['SRNumViaPMOSMet12Met2CoX'] = SRNumViaPMOSMet12Met2CoX
        # _SlicerWithSRLatchXinputs['SRNumViaPMOSMet12Met2CoY'] = SRNumViaPMOSMet12Met2CoY
        # _SlicerWithSRLatchXinputs['SRNumViaNMOSMet12Met2CoX'] = SRNumViaNMOSMet12Met2CoX
        # _SlicerWithSRLatchXinputs['SRNumViaNMOSMet12Met2CoY'] = SRNumViaNMOSMet12Met2CoY
        # _SlicerWithSRLatchXinputs['SRNumViaPMOSMet22Met3CoX'] = SRNumViaPMOSMet22Met3CoX
        # _SlicerWithSRLatchXinputs['SRNumViaPMOSMet22Met3CoY'] = SRNumViaPMOSMet22Met3CoY
        # _SlicerWithSRLatchXinputs['SRNumViaNMOSMet22Met3CoX'] = SRNumViaNMOSMet22Met3CoX
        # _SlicerWithSRLatchXinputs['SRNumViaNMOSMet22Met3CoY'] = SRNumViaNMOSMet22Met3CoY
        # _SlicerWithSRLatchXinputs['_SRSLVT'] = _SRSLVT
        # _SlicerWithSRLatchXinputs['_SRPowerLine'] = _SRPowerLine
        #
        # _SlicerWithSRLatchXinputs['_SLCLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1
        # _SlicerWithSRLatchXinputs['_SLCLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2
        # _SlicerWithSRLatchXinputs['_SLPMOSFinger'] = _SLPMOSFinger
        # _SlicerWithSRLatchXinputs['_SLPMOSChannelWidth'] = _SLPMOSChannelWidth
        # _SlicerWithSRLatchXinputs['_SLDATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        # _SlicerWithSRLatchXinputs['_SLNMOSFinger'] = _SLNMOSFinger
        # _SlicerWithSRLatchXinputs['_SLCLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        # _SlicerWithSRLatchXinputs['_SLNMOSChannelWidth'] = _SLNMOSChannelWidth
        # _SlicerWithSRLatchXinputs['_SLChannelLength'] = _SLChannelLength
        # _SlicerWithSRLatchXinputs['_SLDummy'] = _SLDummy
        # _SlicerWithSRLatchXinputs['_SLSLVT'] = _SLSLVT
        # _SlicerWithSRLatchXinputs['_SLGuardringWidth'] = _SLGuardringWidth
        # _SlicerWithSRLatchXinputs['_SLGuardring'] = _SLGuardring
        # _SlicerWithSRLatchXinputs['_SLSlicerGuardringWidth'] = _SLSlicerGuardringWidth
        # _SlicerWithSRLatchXinputs['_SLSlicerGuardring'] = _SLSlicerGuardring
        # _SlicerWithSRLatchXinputs['_SLNumSupplyCOX'] = _SLNumSupplyCOX
        # _SlicerWithSRLatchXinputs['_SLNumSupplyCOY'] = _SLNumSupplyCOY
        # _SlicerWithSRLatchXinputs['_SLSupplyMet1XWidth'] = _SLSupplyMet1XWidth
        # _SlicerWithSRLatchXinputs['_SLSupplyMet1YWidth'] = _SLSupplyMet1YWidth
        # _SlicerWithSRLatchXinputs['_SLVDD2VSSHeight'] = _SLVDD2VSSHeight
        # _SlicerWithSRLatchXinputs['_SLNumVIAPoly2Met1COX'] = _SLNumVIAPoly2Met1COX
        # _SlicerWithSRLatchXinputs['_SLNumVIAPoly2Met1COY'] = _SLNumVIAPoly2Met1COY
        # _SlicerWithSRLatchXinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COX
        # _SlicerWithSRLatchXinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COY
        # _SlicerWithSRLatchXinputs['_SLPowerLine'] = False



        self._DesignParameter['_SlicerWithSRLatchX4'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatch._SlicerWithSRLatch(_DesignParameter=None, _Name = "SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchEdgeinputs)

        # self._DesignParameter['_SlicerWithSRLatchX'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatch._SlicerWithSRLatch(_DesignParameter=None, _Name = "SlicerWithSRLatchXIn{}".format(_Name)))[0]
        # self._DesignParameter['_SlicerWithSRLatchX']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchXinputs)


        print ('#################################       Coordinates Settings      #########################################')
        _OriginXYCoordinateOfSlicerWithSRLatch = [[0,0]]

        _GuardRingRX2RXSpace = _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace

        PMOS_toptmp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
        NMOS_bottomtmp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
        Guardring_top = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _SLGuardringWidth/2 + _GuardRingRX2RXSpace + _SLSlicerGuardringWidth/2
        Guardring_bottom = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _SLGuardringWidth/2 - _GuardRingRX2RXSpace - _SLSlicerGuardringWidth/2
        GuardringHeight = Guardring_top - Guardring_bottom

        self._DesignParameter['_GuardringHeight']= {'_Ignore': GuardringHeight, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_PMOS_toptmp']= {'_Ignore': PMOS_toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_NMOS_bottomtmp']= {'_Ignore': NMOS_bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_Guardring_top']= {'_Ignore': Guardring_top, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_Guardring_bottom']= {'_Ignore': Guardring_bottom, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        _VDD2VSSHeightAtOneSide = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]

        tmp = []


        YINp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] +\
                self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]
        self._DesignParameter['_YINp']= {'_Ignore': YINp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        for i in range(0, _NumberofSlicerWithSRLatch) :
            tmp.append([_OriginXYCoordinateOfSlicerWithSRLatch[0][0], _OriginXYCoordinateOfSlicerWithSRLatch[0][1] - i * GuardringHeight])

        self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'] = tmp

        self._DesignParameter['_PinVDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_PinVSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_PinInputP1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp1')
        self._DesignParameter['_PinInputN1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn1')
        self._DesignParameter['_PinInputP2'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp2')
        self._DesignParameter['_PinInputN2'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn2')
        self._DesignParameter['_PinInputP3'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp3')
        self._DesignParameter['_PinInputN3'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn3')
        self._DesignParameter['_PinInputP4'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp4')
        self._DesignParameter['_PinInputN4'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn4')

        # self._DesignParameter['_PinOutputP1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSp')
        # self._DesignParameter['_PinOutputN1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],_Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSn')
        self._DesignParameter['_PinCLK0'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK0')
        self._DesignParameter['_PinCLK90'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK90')
        self._DesignParameter['_PinCLK180'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK180')
        self._DesignParameter['_PinCLK270'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK270')

        self._DesignParameter['_OUT1pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUT1')
        self._DesignParameter['_OUTb1pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUTb1')
        self._DesignParameter['_OUT2pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUT2')
        self._DesignParameter['_OUTb2pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUTb2')
        self._DesignParameter['_OUT3pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUT3')
        self._DesignParameter['_OUTb3pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUTb3')
        self._DesignParameter['_OUT4pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUT4')
        self._DesignParameter['_OUTb4pin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.1, _Angle = 0, _TEXT = 'OUTb4')



        self._DesignParameter['_PinVDD']['_XYCoordinates'] = [[0, PMOS_toptmp + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinVSS']['_XYCoordinates'] = [[0, NMOS_bottomtmp + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputP1']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputN1']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputP2']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_PinInputN2']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_PinInputP3']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_PinInputN3']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_PinInputP4']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]
        self._DesignParameter['_PinInputN4']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]

        # self._DesignParameter['_PinOutputN1']['_XYCoordinates'] = [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0]]
        # self._DesignParameter['_PinOutputP1']['_XYCoordinates'] = [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]
        self._DesignParameter['_OUT1pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUTb1pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUT2pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_OUTb2pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_OUT3pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_OUTb3pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_OUT4pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]
        self._DesignParameter['_OUTb4pin']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]

        self._DesignParameter['_PinCLK0']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                            ]

        self._DesignParameter['_PinCLK90']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]
                                                            ]

        self._DesignParameter['_PinCLK180']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]
                                                            ]

        self._DesignParameter['_PinCLK270']['_XYCoordinates'] = [[self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]- 3 * GuardringHeight],
                                                                [self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]- 3 * GuardringHeight]
                                                            ]



        print ('#################################       Supply Line Routing      #########################################')
        if _SLSRInvSupplyLineX4 == True :
            _LengthofSupplyLine = \
            self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][
                1][0] - \
            self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][
                0][0]

            self._DesignParameter['_Met3VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3VDDRouting']['_Width'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_YWidth']

            tmp = []

            for i in range(0, _NumberofSlicerWithSRLatch) :
                tmp.append([[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp],
                            [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp]])

            self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'] = tmp


            # self._DesignParameter['_Met4VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met4VDDRouting']['_Width'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            #
            # tmp = []
            # for i in range(0, _NumberofSlicerWithSRLatch) :
            #     tmp.append([[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]], \
            #                 [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])
            #
            # self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'] = tmp

            del tmp

            Ptoptmp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][1]
            Gtoptmp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][0][1]


            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], \
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + Ptoptmp])


            self._DesignParameter['_SupplyLineMet2VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet2VDD']['_XWidth'] = _LengthofSupplyLine
            self._DesignParameter['_SupplyLineMet2VDD']['_YWidth'] = _SLGuardringWidth
            self._DesignParameter['_SupplyLineMet2VDD']['_XYCoordinates'] = tmp

            self._DesignParameter['_SupplyLineMet3VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet3VDD']['_XWidth'] = _LengthofSupplyLine
            self._DesignParameter['_SupplyLineMet3VDD']['_YWidth'] = _SLGuardringWidth
            self._DesignParameter['_SupplyLineMet3VDD']['_XYCoordinates'] = tmp

            del tmp


            _ViaNumVDDX12 = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][1][0] -
                     self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][0]) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 2
            _ViaNumVDDX23 = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][1][0] -
                     self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][0]) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 2

            if _ViaNumVDDX12 < 1:
                _ViaNumVDDX12 = 1
            if _ViaNumVDDX23 < 1:
                _ViaNumVDDX23 = 1

            _ViaNumVDDY12 = int(_SLGuardringWidth // (
                    _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVDDY23 = int(_SLGuardringWidth // (
                    _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            if _ViaNumVDDY12 < 1:
                _ViaNumVDDY12 = 1
            if _ViaNumVDDY23 < 1:
                _ViaNumVDDY23 = 1


            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY12
            self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VDD']['_XYCoordinates']

            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX23
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY23
            self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VDD']['_XYCoordinates']

            tmp = []
            tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][_NumberofSlicerWithSRLatch-1][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], \
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][_NumberofSlicerWithSRLatch-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][1]])


            self._DesignParameter['_SupplyLineMet2VSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet2VSS1']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XWidth']
            self._DesignParameter['_SupplyLineMet2VSS1']['_YWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_YWidth']
            self._DesignParameter['_SupplyLineMet2VSS1']['_XYCoordinates'] = tmp

            self._DesignParameter['_SupplyLineMet3VSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet3VSS1']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XWidth']
            self._DesignParameter['_SupplyLineMet3VSS1']['_YWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_YWidth']
            self._DesignParameter['_SupplyLineMet3VSS1']['_XYCoordinates'] = tmp

            del tmp


            _ViaNumVSSX12 = int(self._DesignParameter['_SupplyLineMet2VSS1']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4
            _ViaNumVSSX23 = int(self._DesignParameter['_SupplyLineMet3VSS1']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4

            if _ViaNumVSSX12 < 1:
                _ViaNumVSSX12 = 1
            if _ViaNumVSSX23 < 1:
                _ViaNumVSSX23 = 1


            _ViaNumVSSY12 = int(self._DesignParameter['_SupplyLineMet2VSS1']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSY23 = int(self._DesignParameter['_SupplyLineMet3VSS1']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            if _ViaNumVSSY12 < 1:
                _ViaNumVSSY12 = 1
            if _ViaNumVSSY23 < 1:
                _ViaNumVSSY23 = 1


            _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVSSX12
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVSSY12
            self._DesignParameter['_ViaMet12Met2VSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VSS1In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VSS1']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met2)
            self._DesignParameter['_ViaMet12Met2VSS1']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS1']['_XYCoordinates']

            _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX23
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVSSY23
            self._DesignParameter['_ViaMet22Met3VSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VSS1In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VSS1']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met3)
            self._DesignParameter['_ViaMet22Met3VSS1']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS1']['_XYCoordinates']


            tmp = []
            tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], \
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + Gtoptmp])

            self._DesignParameter['_SupplyLineMet2VSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet2VSS2']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XWidth']
            self._DesignParameter['_SupplyLineMet2VSS2']['_YWidth'] = _SLGuardringWidth
            self._DesignParameter['_SupplyLineMet2VSS2']['_XYCoordinates'] = tmp

            self._DesignParameter['_SupplyLineMet3VSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SupplyLineMet3VSS2']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XWidth']
            self._DesignParameter['_SupplyLineMet3VSS2']['_YWidth'] = _SLGuardringWidth
            self._DesignParameter['_SupplyLineMet3VSS2']['_XYCoordinates'] = tmp

            del tmp


            _ViaNumVSSX12 = int(self._DesignParameter['_SupplyLineMet2VSS2']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4
            _ViaNumVSSX23 = int(self._DesignParameter['_SupplyLineMet3VSS2']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4

            if _ViaNumVSSX12 < 1:
                _ViaNumVSSX12 = 1
            if _ViaNumVSSX23 < 1:
                _ViaNumVSSX23 = 1


            _ViaNumVSSY12 = int(self._DesignParameter['_SupplyLineMet2VSS2']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSY23 = int(self._DesignParameter['_SupplyLineMet3VSS2']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            if _ViaNumVSSY12 < 1:
                _ViaNumVSSY12 = 1
            if _ViaNumVSSY23 < 1:
                _ViaNumVSSY23 = 1


            _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVSSX12
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVSSY12
            self._DesignParameter['_ViaMet12Met2VSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VSS2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met2)
            self._DesignParameter['_ViaMet12Met2VSS2']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS2']['_XYCoordinates']

            _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX23
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVSSY23
            self._DesignParameter['_ViaMet22Met3VSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VSS2']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met3)
            self._DesignParameter['_ViaMet22Met3VSS2']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS2']['_XYCoordinates']

            # _ViaNumVDDX12ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # _ViaNumVDDY12ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            #
            # if _ViaNumVDDX12ofSRLatch < 1:
            #     _ViaNumVDDX12ofSRLatch = 1
            #
            # if _ViaNumVDDY12ofSRLatch < 1:
            #     _ViaNumVDDY12ofSRLatch = 1
            #
            # _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12ofSRLatch
            # _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY12ofSRLatch
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
            #
            # tmp = []
            # for i in range(0, _NumberofSlicerWithSRLatch):
            #     tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]])
            #
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            #
            # _ViaNumVDDX23ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # _ViaNumVDDY23ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            #
            # if _ViaNumVDDX23ofSRLatch < 1:
            #     _ViaNumVDDX23ofSRLatch = 1
            #
            # if _ViaNumVDDY23ofSRLatch < 1:
            #     _ViaNumVDDY23ofSRLatch = 1
            #
            # _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX23ofSRLatch
            # _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY23ofSRLatch
            # self._DesignParameter['_ViaMet22Met3VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
            #
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            # del tmp
            #
            # _SupplyMetYWidth = Ptoptmp + _SLGuardringWidth / 2 - (self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)
            # _CenterMetY = (Ptoptmp + _SLGuardringWidth / 2 + (self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3VDDofSRLatch']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) / 2
            #
            #
            # _ViaNumVDDX34ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # _ViaNumVDDY34ofSRLatch = int(_SupplyMetYWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            #
            # if _ViaNumVDDX34ofSRLatch < 1:
            #     _ViaNumVDDX34ofSRLatch = 1
            #
            # if _ViaNumVDDY34ofSRLatch < 1:
            #     _ViaNumVDDY34ofSRLatch = 1
            #
            # _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX34ofSRLatch
            # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY34ofSRLatch
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet32Met4VDDofSRLatch']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVDDMet32Met4)
            #
            # tmp = []
            # for i in range(0, _NumberofSlicerWithSRLatch):
            #     tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + _CenterMetY])
            #
            # self._DesignParameter['_ViaMet12Met2VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            #
            #
            #
            #
            #
            #
            # _ViaNumVDDX45ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # _ViaNumVDDY45ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            #
            # if _ViaNumVDDX45ofSRLatch < 1 :
            #     _ViaNumVDDX45ofSRLatch = 1
            #
            # if _ViaNumVDDY45ofSRLatch < 1 :
            #     _ViaNumVDDY45ofSRLatch = 1
            #
            # _ViaNumVDDX56ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # _ViaNumVDDY56ofSRLatch = int(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            #
            # if _ViaNumVDDX56ofSRLatch < 1 :
            #     _ViaNumVDDX56ofSRLatch = 1
            #
            # if _ViaNumVDDY56ofSRLatch < 1 :
            #     _ViaNumVDDY56ofSRLatch = 1
            #
            # _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            # _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ViaNumVDDX45ofSRLatch
            # _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY45ofSRLatch
            # self._DesignParameter['_ViaMet42Met5VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet42Met5VDDofSRLatch']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVDDMet42Met5)
            #
            # tmp = []
            # for i in range(0, _NumberofSlicerWithSRLatch):
            #     tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]])
            #
            # self._DesignParameter['_ViaMet42Met5VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            # _ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            # _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = _ViaNumVDDX56ofSRLatch
            # _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = _ViaNumVDDY56ofSRLatch
            # self._DesignParameter['_ViaMet52Met6VDDofSRLatch'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6VDDofSRLatchIn{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet52Met6VDDofSRLatch']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVDDMet52Met6)
            #
            # self._DesignParameter['_ViaMet52Met6VDDofSRLatch']['_XYCoordinates'] = tmp
            #
            # del tmp
            #
            # self._DesignParameter['_Met5VDDofSRLatch'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met5VDDofSRLatch']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            # self._DesignParameter['_Met5VDDofSRLatch']['_YWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_Met5VDDofSRLatch']['_XYCoordinates'] = self._DesignParameter['_ViaMet42Met5VDDofSRLatch']['_XYCoordinates']
            #
            # self._DesignParameter['_Met6VDDofSRLatch'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met6VDDofSRLatch']['_XWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            # self._DesignParameter['_Met6VDDofSRLatch']['_YWidth'] = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_Met6VDDofSRLatch']['_XYCoordinates'] = self._DesignParameter['_ViaMet52Met6VDDofSRLatch']['_XYCoordinates']
            #



        print ('#################################       Clock Routing      #########################################')
        self._DesignParameter['_Met6RoutingCLK0'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met6RoutingCLK90'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met6RoutingCLK180'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met6RoutingCLK270'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)

        self._DesignParameter['_Met7RoutingCLK0'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met7RoutingCLK90'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met7RoutingCLK180'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_Met7RoutingCLK270'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=400)

        _CLKRoutingMetThickness = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']
        _Cen2CenBtwMet = _CLKRoutingMetThickness + _DRCObj._MetalxMinSpace11

        self._DesignParameter['_Met6RoutingCLK0']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met6RoutingCLK90']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met6RoutingCLK180']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met6RoutingCLK270']['_Width'] = _CLKRoutingMetThickness

        self._DesignParameter['_Met7RoutingCLK0']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met7RoutingCLK90']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met7RoutingCLK180']['_Width'] = _CLKRoutingMetThickness
        self._DesignParameter['_Met7RoutingCLK270']['_Width'] = _CLKRoutingMetThickness


        _MidofCLKIn0_90 = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1] + (self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][1][1]) / 2
        _MidofCLKIn180_270 = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1] + (self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][1]) / 2
        _MidofCLKIn0_270 = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1] + (self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][1]) / 2



        self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'] = [[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]], \
                                                                        [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinSpace11 + _CLKRoutingMetThickness / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'] = [[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][1][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]], \
                                                                        [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][1][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinSpace11 + _CLKRoutingMetThickness / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'] = [[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]], \
                                                                        [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinSpace11 + _CLKRoutingMetThickness / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]]]]

        self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'] = [[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]], \
                                                                        [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinSpace11 + _CLKRoutingMetThickness / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][3][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1]]]]


        self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'] = [[self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][0][1], \
                                                                       [self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][0][1][0], _MidofCLKIn0_90 + _DRCObj._MetalxMinSpace11 / 2 + _CLKRoutingMetThickness / 2]]]

        self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'] = [[self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][0][1], \
                                                                        [self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][0][1][0], _MidofCLKIn0_90 - _DRCObj._MetalxMinSpace11 / 2 - _CLKRoutingMetThickness / 2]]]

        self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'] = [[self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][0][1], \
                                                                         [self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][0][1][0], _MidofCLKIn180_270 + _DRCObj._MetalxMinSpace11 / 2 + _CLKRoutingMetThickness / 2]]]

        self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'] = [[self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][0][1], \
                                                                         [self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][0][1][0], _MidofCLKIn180_270 - _DRCObj._MetalxMinSpace11 / 2 - _CLKRoutingMetThickness / 2]]]


        self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][0][1][0], self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][0][1][1]], [self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][0][1][0] + 2 * _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][0][1][1]]])
        self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][0][1][0], self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][0][1][1]], [self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][0][1][0] + _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][0][1][1]]])
        self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][0][1][0], self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][0][1][1]], [self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][0][1][0] + _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][0][1][1]]])
        self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][0][1][0], self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][0][1][1]], [self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][0][1][0] + 2 * _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][0][1][1]]])

        self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'].append([[self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][-1][1][1] + _CLKRoutingMetThickness / 2], [self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][-1][1][0], _MidofCLKIn0_270 + _Cen2CenBtwMet / 2 + _Cen2CenBtwMet]])
        self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'].append([[self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][-1][1][1] + _CLKRoutingMetThickness / 2], [self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][-1][1][0], _MidofCLKIn0_270 + _Cen2CenBtwMet / 2]])
        self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'].append([[self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][-1][1][1] - _CLKRoutingMetThickness / 2], [self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][-1][1][0], _MidofCLKIn0_270 - _Cen2CenBtwMet / 2]])
        self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'].append([[self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][-1][1][1] - _CLKRoutingMetThickness / 2], [self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][-1][1][0], _MidofCLKIn0_270 - _Cen2CenBtwMet / 2 - _Cen2CenBtwMet]])

        self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][-1][1][1]], [self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][-1][1][0] + _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][-1][1][1]]])
        self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][-1][1][1]], [self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][-1][1][0] + 2 * _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][-1][1][1]]])
        self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][-1][1][1]], [self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][-1][1][0] + 2 * _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][-1][1][1]]])
        self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'].append([[self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][-1][1][0], self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][-1][1][1]], [self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][-1][1][0] + _Cen2CenBtwMet, self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][-1][1][1]]])

        _ViaMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaMet62Met7['_ViaMet62Met7NumberOfCOX'] = 2
        _ViaMet62Met7['_ViaMet62Met7NumberOfCOY'] = 2
        self._DesignParameter['_ViaMet62Met7'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaMet62Met7)

        tmp = []
        for i in range(0, len(self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates']) - 1) :
            tmp.append(self._DesignParameter['_Met7RoutingCLK0']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met7RoutingCLK90']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met7RoutingCLK180']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met7RoutingCLK270']['_XYCoordinates'][i][1])

        for i in range(0, len(self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'])) :
            tmp.append(self._DesignParameter['_Met6RoutingCLK0']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met6RoutingCLK90']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met6RoutingCLK180']['_XYCoordinates'][i][1])
            tmp.append(self._DesignParameter['_Met6RoutingCLK270']['_XYCoordinates'][i][1])


        self._DesignParameter['_ViaMet62Met7']['_XYCoordinates'] = tmp

        del tmp





if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'
    #####################SRLatch#######################
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
    _SRPowerLine = None
    #####################Slicer#######################
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
    _SLPowerLine = None
    _N = 4
    #####################Inverter#######################
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
    #####################Power#######################
    _SLSRInvSupplyLineX4 = True



    SlicerWithSRLatchX4Obj = SlicerWithSRLatchX4Obj(_DesignParameter=None, _Name='SlicerWithSRLatchX4')
    SlicerWithSRLatchX4Obj._CalculateDesignParameter(_SRFinger1 = _SRFinger1, _SRFinger2 = _SRFinger2, _SRFinger3 = _SRFinger3, _SRFinger4 = _SRFinger4,
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
                                                     _InvSLVT=_InvSLVT, _InvPowerLine=_InvPowerLine, _SLSRInvSupplyLineX4=_SLSRInvSupplyLineX4

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





    SlicerWithSRLatchX4Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = SlicerWithSRLatchX4Obj._DesignParameter)
    _fileName = 'SlicerWithSRLatchX4.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = SlicerWithSRLatchX4Obj._CreateGDSStream(SlicerWithSRLatchX4Obj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('SlicerWithSRLatchX4.gds', 'rb')
    ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
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
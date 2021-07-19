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

class SlicerWithSRLatchXNObj (StickDiagram._StickDiagram) :

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
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _NumberofSlicerWithSRLatch = None)

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
                                    _SRNumViaNMOSMet22Met3CoX = None, _SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                    _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False, _NumberofSlicerWithSRLatch = None) :




        print ('#########################################################################################################')
        print ('                                {}  SlicerWithSRLatchXNObj Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatchX4'

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



        self._DesignParameter['SlicerWithSRLatchX4'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatch._SlicerWithSRLatch(_DesignParameter=None, _Name = "SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchEdgeinputs)

        # self._DesignParameter['_SlicerWithSRLatchX'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatch._SlicerWithSRLatch(_DesignParameter=None, _Name = "SlicerWithSRLatchXIn{}".format(_Name)))[0]
        # self._DesignParameter['_SlicerWithSRLatchX']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchXinputs)


        print ('#################################       Coordinates Settings      #########################################')
        _OriginXYCoordinateOfSlicerWithSRLatch = [[0,0]]

        _GuardRingRX2RXSpace = _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace

        PMOS_toptmp = self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
        NMOS_bottomtmp = self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
        Guardring_top = self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _SLGuardringWidth/2 + _GuardRingRX2RXSpace + _SLSlicerGuardringWidth/2
        Guardring_bottom = self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _SLGuardringWidth/2 - _GuardRingRX2RXSpace - _SLSlicerGuardringWidth/2
        GuardringHeight = Guardring_top - Guardring_bottom

        _VDD2VSSHeightAtOneSide = self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]

        tmp = []


        for i in range(0, _NumberofSlicerWithSRLatch) :
            tmp.append([_OriginXYCoordinateOfSlicerWithSRLatch[0][0], _OriginXYCoordinateOfSlicerWithSRLatch[0][1] - i * GuardringHeight])

        self._DesignParameter['SlicerWithSRLatchX4']['_XYCoordinates'] = tmp

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



        self._DesignParameter['_PinVDD']['_XYCoordinates'] = [[0, PMOS_toptmp + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinVSS']['_XYCoordinates'] = [[0, NMOS_bottomtmp + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputP1']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputN1']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_PinInputP2']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_PinInputN2']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_PinInputP3']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_PinInputN3']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_PinInputP4']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]
        self._DesignParameter['_PinInputN4']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]

        # self._DesignParameter['_PinOutputN1']['_XYCoordinates'] = [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0]]
        # self._DesignParameter['_PinOutputP1']['_XYCoordinates'] = [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]
        self._DesignParameter['_OUT1pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUTb1pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_OUT2pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_OUTb2pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - GuardringHeight]]
        self._DesignParameter['_OUT3pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_OUTb3pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - 2 * GuardringHeight]]
        self._DesignParameter['_OUT4pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]
        self._DesignParameter['_OUTb4pin']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1] - 3 * GuardringHeight]]

        self._DesignParameter['_PinCLK0']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                            ]

        self._DesignParameter['_PinCLK90']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - GuardringHeight]
                                                            ]

        self._DesignParameter['_PinCLK180']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] - 2 * GuardringHeight]
                                                            ]

        self._DesignParameter['_PinCLK270']['_XYCoordinates'] = [[self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - 3 * GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]- 3 * GuardringHeight],
                                                                [self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]- 3 * GuardringHeight]
                                                            ]



if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'

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


    SlicerWithSRLatchXNObj = SlicerWithSRLatchXNObj(_DesignParameter=None, _Name='SlicerWithSRLatchX4')
    SlicerWithSRLatchXNObj._CalculateDesignParameter(_SRFinger1 = _SRFinger1, _SRFinger2 = _SRFinger2, _SRFinger3 = _SRFinger3, _SRFinger4 = _SRFinger4,
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
                                  _SLNumVIAPoly2Met1COX=_SLNumVIAPoly2Met1COX, _SLNumVIAPoly2Met1COY=_SLNumVIAPoly2Met1COY, _SLNumVIAMet12COX=_SLNumVIAMet12COX, _SLNumVIAMet12COY=_SLNumVIAMet12COY, _SLPowerLine = _SLPowerLine, _NumberofSlicerWithSRLatch = _N)

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





    SlicerWithSRLatchXNObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = SlicerWithSRLatchXNObj._DesignParameter)
    _fileName = 'SlicerWithSRLatchX4.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = SlicerWithSRLatchXNObj._CreateGDSStream(SlicerWithSRLatchXNObj._DesignParameter['_GDSFile']['_GDSFile'])

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
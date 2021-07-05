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
import math

class _SRLatch(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(_Finger1 = None, _Finger2 = None, _Finger3 = None, _Finger4 = None,
                                        _NMOSChannelWidth1 = None, _PMOSChannelWidth1 = None, _NMOSChannelWidth2 = None, _PMOSChannelWidth2 = None, _NMOSChannelWidth3 = None, _PMOSChannelWidth3 = None, _NMOSChannelWidth4 = None, _PMOSChannelWidth4 = None, 
                                        _ChannelLength = None, _NPRatio = None, _VDD2VSSHeightAtOneSide = None, _Dummy = None,
                                        _NumSupplyCoX = None, _NumSupplyCoY = None, _SupplyMet1XWidth = None, _SupplyMet1YWidth = None,
                                        NumViaPoly2Met1CoX = None, NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None,
                                        NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None, NumViaPMOSMet22Met3CoX = None, NumViaPMOSMet22Met3CoY = None,
                                        NumViaNMOSMet22Met3CoX = None, NumViaNMOSMet22Met3CoY = None, _SLVT = None, _PowerLine = False)

    def __init__(self, _DesignParameter = None, _Name = 'SRLatch'):
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger1 = None, _Finger2 = None, _Finger3 = None, _Finger4 = None, \
                                 # _PMOSFinger1=None, _PMOSFinger2=None, _PMOSFinger3=None, _PMOSFinger4=None, \
                                  _NMOSChannelWidth1 = None, _PMOSChannelWidth1 = None, _NMOSChannelWidth2 = None, _PMOSChannelWidth2 = None, _NMOSChannelWidth3 = None, _PMOSChannelWidth3 = None, _NMOSChannelWidth4 = None, _PMOSChannelWidth4 = None, _ChannelLength = None, _NPRatio = None,\
                                  _VDD2VSSHeightAtOneSide = None, _Dummy = None, _NumSupplyCoX = None, _NumSupplyCoY = None, \
                                  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, NumViaPoly2Met1CoX = None, \
                                  NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None, \
                                  NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None, NumViaPMOSMet22Met3CoX = None, NumViaPMOSMet22Met3CoY = None, \
                                  NumViaNMOSMet22Met3CoX = None, NumViaNMOSMet22Met3CoY = None, _SLVT = None, _PowerLine = False) :

        _DRCObj = DRC.DRC()
        _Name = 'SRLatch'



#####################################################_NMOS Generation###############################################################
        #####################################_NMOS1 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger1
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT
   #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, \
                                                                         _Name='NMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        #####################################_NMOS2 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger2
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth2
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT
   #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS2'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, \
                                                                         _Name='NMOS2In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        #####################################_NMOS3 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger3
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth3
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT
   #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS3'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, \
                                                                         _Name='NMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs

        #####################################_NMOS4 Generation######################################
        _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger4
        _NMOSinputs['_NMOSChannelWidth'] = _NMOSChannelWidth4
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT
   #     _NMOSinputs['_Flip'] = None

        self._DesignParameter['_NMOS4'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, \
                                                                         _Name='NMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        del _NMOSinputs



#####################################################_PMOS Generation###############################################################
        #####################################_PMOS1 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger1
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth1
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT
  #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS1'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, \
                                                                         _Name='PMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        #####################################_PMOS2 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger2
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth2
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT
   #     _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS2'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS2In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        #####################################_PMOS3 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger3
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth3
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT
   #     _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS3'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs

        #####################################_PMOS4 Generation######################################
        _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger4
        _PMOSinputs['_PMOSChannelWidth'] = _PMOSChannelWidth4
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT
  #      _PMOSinputs['_Flip'] = None

        self._DesignParameter['_PMOS4'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, \
                                                                        _Name='PMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        del _PMOSinputs



#####################################################VIA Generation###############################################################
        #####################################VIA Generation for Gate######################################
        _LenBtwPMOSGates1 = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
                            self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates1 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1 :
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None :
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None :
            _tmpNumCOY = 1
        else :
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

#        if ((_PMOSFinger1 == 1)&(_NMOSFinger1 == 1)) | ((_PMOSFinger1 == 2)&(_NMOSFinger1 == 2)) :
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 1
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 2

        self._DesignParameter['_VIAPMOS1Poly2Met1'] = self._SrefElementDeclaration(_DesignObj = ViaPoly2Met1._ViaPoly2Met1(_DesignParameter = None, \
                                                                                                                          _Name = 'ViaPoly2Met1OnPMOS1GateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates2 = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
                            self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates2 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1 :
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

  #      if ((_PMOSFinger2 == 1)&(_NMOSFinger2 == 1)) | ((_PMOSFinger2 == 2)&(_NMOSFinger2 == 2)) :
  #          _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 1
  #          _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 2

        self._DesignParameter['_VIAPMOS2Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                                                                        _Name='ViaPoly2Met1OnPMOS2GateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates3 = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates3 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

#        if ((_PMOSFinger3 == 1)&(_NMOSFinger3 == 1)) | ((_PMOSFinger3 == 2)&(_NMOSFinger3 == 2)) :
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 2
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

        self._DesignParameter['_VIAPMOS3Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                                                                        _Name='ViaPoly2Met1OnPMOS3GateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY

        _LenBtwPMOSGates4 = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
        self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        _VIAPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _tmpNumCOX = int(_LenBtwPMOSGates4 // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _tmpNumCOX < 1:
            _tmpNumCOX = 1

        if NumViaPoly2Met1CoX != None:
            _tmpNumCOX = NumViaPoly2Met1CoX

        if NumViaPoly2Met1CoY == None:
            _tmpNumCOY = 1
        else:
            _tmpNumCOY = NumViaPoly2Met1CoY

        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
        _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

#        if ((_PMOSFinger4 == 1)&(_NMOSFinger4 == 1)) | ((_PMOSFinger4 == 2)&(_NMOSFinger4 == 2)) :
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 1
#            _VIAPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 2

        self._DesignParameter['_VIAPMOS4Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, \
                                                                                                                        _Name='ViaPoly2Met1OnPMOS4GateIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAPMOSPoly2Met1)
        del _VIAPMOSPoly2Met1
        del _tmpNumCOX
        del _tmpNumCOY



        #####################################Met1&Met2 Contact######################################
        _PMOSViaNum = NumViaPMOSMet12Met2CoY
        if _PMOSViaNum == None:
            _PMOSViaNum = int(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _PMOSViaNum < 2:
            _PMOSViaNum = 2

        if NumViaPMOSMet12Met2CoX == None:
            NumViaPMOSMet12Met2CoX = 1

        _VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaPMOSMet12Met2CoX
        _VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _PMOSViaNum

        self._DesignParameter['_ViaMet12Met2OnPMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, \
                                                                           _Name='ViaMet12Met2OnPMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
        del _PMOSViaNum
        del _VIAPMOSMet12

        _NMOSViaNum = NumViaNMOSMet12Met2CoY
        if _NMOSViaNum == None:
            _NMOSViaNum = int(
                self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNum < 2:
            _NMOSViaNum = 2

        if NumViaNMOSMet12Met2CoX == None:
            NumViaNMOSMet12Met2CoX = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaNMOSMet12Met2CoX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNum

        self._DesignParameter['_ViaMet12Met2OnNMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, \
                                                                           _Name='ViaMet12Met2OnNMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
        del _NMOSViaNum
        del _VIANMOSMet12



#####################################################SupplyRail Generation###############################################################
        #####################################VSS Generation######################################
        _ContactNum = _NumSupplyCoX

        if _NumSupplyCoX == None :
            _ContactNum = int((3 * _DRCObj._PolygateMinSpace + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] +\
                              self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 3 * _DRCObj._PolygateMinSpace) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

        if _ContactNum < 2 :
            _ContactNum = 2

        if _NumSupplyCoY == None :
            _NumSupplyCoY = 1

        _Pbodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
        _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCoY
        _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj = PbodyContact._PbodyContact(_DesignParameter = None, \
                                                                                                                     _Name = 'PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)
        del _Pbodyinputs


        #####################################VDD Generation######################################
        _Nbodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
        _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY
        _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj = NbodyContact._NbodyContact(_DesignParameter = None, \
                                                                                                                     _Name = 'NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)
        del _Nbodyinputs



#####################################################Coordinates Setting###############################################################
        _VDD2VSSMinHeightAtOneSide = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                     2 * _DRCObj._Metal1MinSpace3 + 2 * self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 3 * _DRCObj._Metal1MinSpace2 + _DRCObj._MetalxMinSpace2

        if _VDD2VSSHeightAtOneSide == None:
            _VDD2VSSHeightAtOneSide = _VDD2VSSMinHeightAtOneSide
            print('_VDD2VSSMinHeightAtOneSide =', _VDD2VSSMinHeightAtOneSide)

        else:
            if _VDD2VSSHeightAtOneSide < _VDD2VSSMinHeightAtOneSide:
                print('_VDD2VSSMinHeightAtOneSide =', _VDD2VSSMinHeightAtOneSide)
                raise NotImplementedError

    #    self._DesignParameter['_VDD2VSSHeightAtOneSide'] = _VDD2VSSHeightAtOneSide


        #####################################################MOS Coordinates Setting###############################################################
#        LengthBtwPODummy1 = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]
#        LengthBtwPODummy2 = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]
        self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[-(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) / 2, self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
                                                                max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3],
                                                            [-(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) / 2, -(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
                                                                max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3)]]
            # [[-LengthBtwPODummy1 / 2 - LengthBtwPODummy2 - (_ChannelLength + _DRCObj._PolygateMinSpace) * 3 / 2, self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                    max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3],
            #                                                 [-LengthBtwPODummy1 / 2 - LengthBtwPODummy2 - (_ChannelLength + _DRCObj._PolygateMinSpace) * 3 / 2, -(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + \
            #                                                    max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3)]]
        self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]]]
        self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]]]
        self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + _ChannelLength + _DRCObj._PolygateMinSpace, self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]]]

        self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], _VDD2VSSHeightAtOneSide - (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3)], \
                                                             [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], -(_VDD2VSSHeightAtOneSide - (self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + _DRCObj._Metal1MinSpace3))]]
        self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]
        self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]
        self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                                             [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], -(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1])]]
#        del LengthBtwPODummy1
#        del LengthBtwPODummy2



        #####################################################Supply Rail Coordinates Setting###############################################################
        MiddleCoordinateX = (self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]) / 2 ## Center of MOSs

        self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[MiddleCoordinateX, 0]]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[MiddleCoordinateX, _VDD2VSSHeightAtOneSide], [MiddleCoordinateX, 0 - _VDD2VSSHeightAtOneSide]]

        #####################################################Via Met1&Met2 Coordinates Setting###############################################################
        _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
        tmpViaMet12Met2OnPMOS = []
        tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS = []
        for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter[ '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - _LengthbtwViaCentertoViaCenter / 4])
            tmpViaMet12Met2OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1] + _LengthbtwViaCentertoViaCenter / 4])
        for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter / 4])
            tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS.append([self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1] - _LengthbtwViaCentertoViaCenter / 4])

        self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'] = tmpViaMet12Met2OnPMOS + tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS
        del tmpViaMet12Met2OnPMOS

        tmpViaMet12Met2OnNMOS = []
        tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS = []
        for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]])
        for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter / 4])
            tmpViaMet12Met2OnNMOS.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] - _LengthbtwViaCentertoViaCenter / 4])
        for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
            tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] - _LengthbtwViaCentertoViaCenter / 4])
            tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] + _LengthbtwViaCentertoViaCenter / 4])

        self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'] = tmpViaMet12Met2OnNMOS + tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS
        del tmpViaMet12Met2OnNMOS



        #####################################################Via Poly Coordinates Setting###############################################################
        #####################################_VIAPMOS1Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1] + max(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1] - max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

        ############################
        if _Finger1 == 1 :
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            _LengthNPolyDummyEdge2OriginX = (int(_Finger1 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            _LengthPPolyDummyEdge2OriginX = (int(_Finger1 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

            _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + 1
            _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown],
                                                                             [self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthPPolyVIAtoGoDown],
                                                                             [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                             [self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp]]

        #####################################_VIAPMOS2Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1] + max(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1] - max(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

        ############################
        if _Finger2 == 1 :
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            _LengthNPolyDummyEdge2OriginX = (int(_Finger2 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            _LengthPPolyDummyEdge2OriginX = (int(_Finger2 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

            _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + 1
            _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown],
                                                                             [self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                             [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                             [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown]]

        #####################################_VIAPMOS3Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1] + max(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] - max(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + _LengthbtwViaCentertoViaCenter / 2) / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

        ############################
        if _Finger3 == 1 :
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            _LengthNPolyDummyEdge2OriginX = (int(_Finger3 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            _LengthPPolyDummyEdge2OriginX = (int(_Finger3 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

            _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + 1
            _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown],
                                                                            [self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthPPolyVIAtoGoDown],
                                                                            [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                            [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthNPolyVIAtoGoUp]]

        #####################################_VIAPMOS4Poly2Met1#####################################
        self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1] + max(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + _DRCObj._Metal1MinSpace2],
                                                                         [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1] - max(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - _DRCObj._Metal1MinSpace2]]

        ############################
        if _Finger4 == 1 :
            _LengthBtwPoly2Poly = _ChannelLength + 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
            _LengthNPolyDummyEdge2OriginX = (int(_Finger4 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2
            _LengthPPolyDummyEdge2OriginX = (int(_Finger4 / 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength / 2 - (self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2

            _LengthNPolyVIAtoGoUp = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthNPolyDummyEdge2OriginX * _LengthNPolyDummyEdge2OriginX) + 1
            _LengthPPolyVIAtoGoDown = math.sqrt(_DRCObj._PolygateMinSpaceAtCorner * _DRCObj._PolygateMinSpaceAtCorner - _LengthPPolyDummyEdge2OriginX * _LengthPPolyDummyEdge2OriginX) + 1
            self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown],
                                                                             [self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                             [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 + _LengthNPolyVIAtoGoUp],
                                                                             [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1] - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2 - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2 - _LengthPPolyVIAtoGoDown]]

#####################################################Routing###############################################################
        #####################################VSS&VDD Met1 Routing######################################
        tmpNMOSSupplyRouting = []
        tmpPMOSSupplyRouting = []

        for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) :
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        for j in range(0, len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) :
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        for k in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) :
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])
            tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]]])

        self._DesignParameter['_PMOS1SupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_PMOS1SupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting
        self._DesignParameter['_PMOS1SupplyRouting']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        for j in range(0, len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        for k in range(0, len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
            tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][k][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], \
                                          self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_NMOS1SupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_NMOS1SupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting
        self._DesignParameter['_NMOS1SupplyRouting']['_Width'] = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        del tmpNMOSSupplyRouting
        del tmpPMOSSupplyRouting



        #####################################Metal Routing######################################
        tmpMet2RoutingOnPMOS = []
        tmpMet2RoutingOnNMOS = []

        _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4 - _DRCObj._VIAxMinWidth / 2], \
                                     [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4 - _DRCObj._VIAxMinWidth / 2]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4 + _DRCObj._VIAxMinWidth / 2], \
                                     [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnPMOS']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4 + _DRCObj._VIAxMinWidth / 2]])

        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]]])
        tmpMet2RoutingOnNMOS.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1]]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4 + _DRCObj._VIAxMinWidth / 2], \
                                     [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4 + _DRCObj._VIAxMinWidth / 2]])
        tmpMet2RoutingOnPMOS.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0] - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4 - _DRCObj._VIAxMinWidth / 2], \
                                     [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_ViaMet12Met2OnNMOS']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4 - _DRCObj._VIAxMinWidth / 2]])

        self._DesignParameter['_Met2Routing1OnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2Routing1OnPMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2Routing1OnPMOS']['_XYCoordinates'] = tmpMet2RoutingOnPMOS

        self._DesignParameter['_Met2Routing1OnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2Routing1OnNMOS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2Routing1OnNMOS']['_XYCoordinates'] = tmpMet2RoutingOnNMOS

        del tmpMet2RoutingOnPMOS
        del tmpMet2RoutingOnNMOS

        tmpMet1OutputRouting = []

        tmpMet1OutputRouting.append([[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1]]])
        tmpMet1OutputRouting.append([[self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]]])
        tmpMet1OutputRouting.append([[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1]]])
        tmpMet1OutputRouting.append([[self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]]])

        self._DesignParameter['_Met1OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met1OutputRouting']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_Met1OutputRouting']['_XYCoordinates'] = tmpMet1OutputRouting

        del tmpMet1OutputRouting

        tmpMet2OutputRouting = []
        tmpMet4OutputRouting = []

        tmpMet4OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]])
        tmpMet4OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]], \
                                     [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]]])

#        tmpMet3OutputRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
#                                     [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]])

        self._DesignParameter['_Met4OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met4OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met4OutputRouting']['_XYCoordinates'] = tmpMet4OutputRouting

        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
                                     [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])

        tmpMet2OutputRouting.append([[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]],[self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]]])
        tmpMet2OutputRouting.append([[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]],[self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]]])

        for j in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _LengthbtwViaCentertoViaCenter / 4]])

            tmpMet2OutputRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]], \
                                         [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _LengthbtwViaCentertoViaCenter / 4]])

        self._DesignParameter['_Met2OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_Met2OutputRouting']['_XYCoordinates'] = tmpMet2OutputRouting

        del tmpMet2OutputRouting
        del tmpMet4OutputRouting


        #####################################################Via Met2&Met3 Generation & Coordinates Setting###############################################################
        _PMOSViaNum = NumViaPMOSMet22Met3CoY
        if _PMOSViaNum == None:
            _PMOSViaNum = int(self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        if _PMOSViaNum < 2:
            _PMOSViaNum = 2

        if NumViaPMOSMet22Met3CoX == None:
            NumViaPMOSMet22Met3CoX = 1

        _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = NumViaPMOSMet22Met3CoX
        _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _PMOSViaNum

        self._DesignParameter['_ViaMet22Met3OnPMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSIn{}'.format(_Name)))[0]
        tmp = []
        for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])
            tmp.append([self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet22Met3OnPMOS']['_XYCoordinates'] = tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS + tmp
        self._DesignParameter['_ViaMet22Met3OnPMOS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)
        del tmp
        del _PMOSViaNum
        del _VIAPMOSMet23
        del tmpViaMet12Met2OnPMOSandMet212Met3OnPMOS

        _NMOSViaNum = NumViaNMOSMet22Met3CoY
        if _NMOSViaNum == None:
            _NMOSViaNum = int(self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

        if _NMOSViaNum < 2:
            _NMOSViaNum = 2

        if NumViaNMOSMet22Met3CoX == None:
            NumViaNMOSMet22Met3CoX = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = NumViaNMOSMet22Met3CoX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNum

        self._DesignParameter['_ViaMet22Met3OnNMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSIn{}'.format(_Name)))[0]
        tmp = []
        for i in range(0, len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])) :
            tmp.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]])
            tmp.append([self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]])

        self._DesignParameter['_ViaMet22Met3OnNMOS']['_XYCoordinates'] = tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS + tmp
        self._DesignParameter['_ViaMet22Met3OnNMOS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)
        del tmp
        del _NMOSViaNum
        del _VIANMOSMet23
        del tmpViaMet12Met2OnNMOSandMet212Met3OnNMOS

        self._DesignParameter['_Met3RoutingOnPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3RoutingOnPMOS']['_Width'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_Met3RoutingOnPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]], \
                                                                         [[self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]], [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1]]]]

        self._DesignParameter['_Met3RoutingOnNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3RoutingOnNMOS']['_Width'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinWidth / 2 + _DRCObj._MetalxMinSpace, self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]]], \
                                                                         [[self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]], [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0] + _DRCObj._MetalxMinWidth / 2 + _DRCObj._MetalxMinSpace, self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1]]]]
                                                                        # [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth / 2], [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], (self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]) / 2]]]

        ViaMet22Met3forRoutingoverVSS = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        ViaMet22Met3forRoutingoverVSS['_ViaMet22Met3NumberOfCOX'] = 1
        ViaMet22Met3forRoutingoverVSS['_ViaMet22Met3NumberOfCOY'] = 2
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3forRoutingoverVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**ViaMet22Met3forRoutingoverVSS)
        self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_XYCoordinates'] = [[self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][0][1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][0][1][1]]]

        del ViaMet22Met3forRoutingoverVSS


        ViaMet32Met4forRoutingoverVSS = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        ViaMet32Met4forRoutingoverVSS['_ViaMet32Met4NumberOfCOX'] = 1
        ViaMet32Met4forRoutingoverVSS['_ViaMet32Met4NumberOfCOY'] = 2
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forRoutingoverVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**ViaMet32Met4forRoutingoverVSS)
        self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'] = [[self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][1][1][0] + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][1][1][1]]]

        del ViaMet32Met4forRoutingoverVSS




        #####################################################Additional Routing###############################################################
        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])) :
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])

        self._DesignParameter['_AdditionalPolyOnMOS1'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['POLY'][0], _Datatype = DesignParameters._LayerMapping['POLY'][1], \
                                                                                      _XYCoordinates = [], _Width = None)
        self._DesignParameter['_AdditionalPolyOnMOS1']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS1']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])) :
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][2][1] + self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])

        self._DesignParameter['_AdditionalPolyOnMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], \
                                                                                      _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS2']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS2']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])

        self._DesignParameter['_AdditionalPolyOnMOS3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], \
            _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS3']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS3']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        tmpPMOSGateRouting = []
        tmpNMOSGateRouting = []
        for i in range(0, len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpPMOSGateRouting.append([[self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]], \
                                       [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])
            tmpNMOSGateRouting.append([[self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]], \
                                       [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]])

        self._DesignParameter['_AdditionalPolyOnMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
        self._DesignParameter['_AdditionalPolyOnMOS4']['_Width'] = _ChannelLength
        self._DesignParameter['_AdditionalPolyOnMOS4']['_XYCoordinates'] = tmpPMOSGateRouting + tmpNMOSGateRouting

        del tmpPMOSGateRouting
        del tmpNMOSGateRouting

        self._DesignParameter['_AdditionalPolyOnGate1'] =  self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=None, _YWidth=None, _ElementName=None,)
        self._DesignParameter['_AdditionalPolyOnGate1']['_XWidth'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate1']['_YWidth'] = self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate1']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate2']['_XWidth'] = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

        self._DesignParameter['_AdditionalPolyOnGate2']['_YWidth'] = self._DesignParameter['_VIAPMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate2']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate3']['_XWidth'] = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate3']['_YWidth'] = self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate3']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates']

        self._DesignParameter['_AdditionalPolyOnGate4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None, )
        self._DesignParameter['_AdditionalPolyOnGate4']['_XWidth'] = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
        self._DesignParameter['_AdditionalPolyOnGate4']['_YWidth'] = self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_AdditionalPolyOnGate4']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates']


        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalViaMet12Met2OnGate1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        self._DesignParameter['_AdditionalMet12Met2OnGate1']['_XYCoordinates'] = self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates']

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12

        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditinalMet22Met3OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3OnGate1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditinalMet22Met3OnGate1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        self._DesignParameter['_AdditinalMet22Met3OnGate1']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1]], \
                                                                                 [self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet23

        # _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # if _NMOSViaNumX < 2 :
        #     _NMOSViaNumX = 2
        #
        # _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        # if _NMOSViaNumY < 1 :
        #     _NMOSViaNumY = 1
        #
        # _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        # _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        # _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY
        #
        _tmpLength = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
        #
        # self._DesignParameter['_AdditionalMet22Met3OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3OnGate3In{}'.format(_Name)))[0]
        # self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        # self._DesignParameter['_AdditionalMet22Met3OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace], \
        #                                                                          [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace]]
        #
        # del _NMOSViaNumX
        # del _NMOSViaNumY
        # del _VIANMOSMet23


        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet32Met4OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalViaMet32Met4OnGate3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet32Met4OnGate3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34)
        self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0] - (_DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace) / 2, (self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) / 2], \
                                                                                  [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace], \
                                                                                  [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0] - self._DesignParameter['_AdditionalMet32Met4OnGate3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 + _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_AdditinalMet22Met3OnGate1']['_XYCoordinates'][0][1]]]###self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1]]]###self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace]]


        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet34


        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet22Met3OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalViaMet22Met3OnGate3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet22Met3OnGate3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23)
        self._DesignParameter['_AdditionalMet22Met3OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][0], (self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) / 2], \
                                                                                  [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet23


        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalViaMet12Met2In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        self._DesignParameter['_AdditionalMet12Met2']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][0], (self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1]) / 2]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12


        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2 :
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1 :
            _NMOSViaNumY = 1

        _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditinalMet32Met4OnGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalViaMet32Met4OnMOS1In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditinalMet32Met4OnGate1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34)
        self._DesignParameter['_AdditinalMet32Met4OnGate1']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet34

        _NMOSViaNumX = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumX < 2:
            _NMOSViaNumX = 2

        _NMOSViaNumY = int(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if _NMOSViaNumY < 1:
            _NMOSViaNumY = 1

        _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NMOSViaNumX
        _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NMOSViaNumY

        self._DesignParameter['_AdditionalMet12Met2OnGate3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalViaMet12Met2OnMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIANMOSMet12)
        self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace], \
                                                                                 [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnPMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace], \
                                                                                 [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace], \
                                                                                 [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 - _tmpLength / 4 - _DRCObj._MetalxMinWidth * 3 / 2 - _DRCObj._MetalxMinSpace]]

        del _NMOSViaNumX
        del _NMOSViaNumY
        del _VIANMOSMet12


        # _ViaNumMet23X = int(self._DesignParameter['_Met1OutputRouting']['_Width'] / _DRCObj._MetalxMinWidth)
        # if _ViaNumMet23X < 1 :
        #     _ViaNumMet23X = 1
        #
        # _ViaNumMet23Y = int ((self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._MetalxMinSpace) / (_DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace)) - 2
        # if _ViaNumMet23Y < 2 :
        #     _ViaNumMet23Y = 2
        #
        # _ViaMOS4Met23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        # _ViaMOS4Met23['_ViaMet22Met3NumberOfCOX'] = _ViaNumMet23X
        # _ViaMOS4Met23['_ViaMet22Met3NumberOfCOY'] = _ViaNumMet23Y

        _ViaMOS4Met23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaMOS4Met23['_ViaMet22Met3NumberOfCOX'] = 2
        _ViaMOS4Met23['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet22Met3OnMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='AdditionalMet22Met3OnMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMOS4Met23)
        self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth /2, (self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]) / 2]]
                #[[self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_AdditionalMet22Met3OnMOS4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth /2, (self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]) / 2], \


        # _ViaNumMet12X = int(self._DesignParameter['_Met1OutputRouting']['_Width'] / _DRCObj._MetalxMinWidth)
        # if _ViaNumMet12X < 1 :
        #     _ViaNumMet12X = 1
        #
        # _ViaNumMet12Y = int ((self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._MetalxMinSpace) / (_DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace)) - 2
        # if _ViaNumMet12Y < 2 :
        #     _ViaNumMet12Y = 2
        #
        # _ViaMOS4Met12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        # _ViaMOS4Met12['_ViaMet12Met2NumberOfCOX'] = _ViaNumMet12X
        # _ViaMOS4Met12['_ViaMet12Met2NumberOfCOY'] = _ViaNumMet12Y

        _ViaMOS4Met12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaMOS4Met12['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaMOS4Met12['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet12Met2OnMOS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='AdditionalMet12Met2OnMOS4In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMOS4Met12)
        self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth /2, (self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][3][1]) / 2], \
                                                                                [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth /2, (self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]) / 2]]

        del _ViaMOS4Met23
        del _ViaMOS4Met12


        # _ViaNumMet34Y = NumViaNMOSMet22Met3CoY
        # if _ViaNumMet34Y == None:
        #     _ViaNumMet34Y = int(self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
        #
        # if _ViaNumMet34Y < 2:
        #     _ViaNumMet34Y = 2
        #
        # if NumViaNMOSMet32Met4CoX == None:
        #     NumViaNMOSMet32Met4CoX = 1
        #
        # _VIAMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        # _VIAMOSMet34['_ViaMet32Met4NumberOfCOX'] = NumViaNMOSMet32Met4CoX
        # _VIAMOSMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y
        #
        # self._DesignParameter['_AdditionalMet32Met4OnMOS3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditinalMet32Met4OnMOS3In{}'.format(_Name)))[0]
        #
        # self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAMOSMet34)
        #
        # tmp = []
        # for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
        #     tmp.append([self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]])
        #
        # self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'] = tmp
        #
        # del tmp


        self._DesignParameter['_AdditionalMet1Routing1'] = self._BoundaryElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0],_Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _XWidth=None, _YWidth=None)
        self._DesignParameter['_AdditionalMet1Routing1']['_XWidth'] = max(self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_AdditionalMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['_AdditionalMet1Routing1']['_YWidth'] = self._DesignParameter['_VIAPMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_AdditionalMet1Routing1']['_XYCoordinates'] = self._DesignParameter['_AdditionalMet12Met2OnGate1']['_XYCoordinates']


        self._DesignParameter['_AdditionalMet1Routing3'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0],_Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet1Routing3']['_Width'] = max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['_AdditionalMet1Routing3']['_XYCoordinates'] = [[[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], min(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1] - self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)]], \
                                                                              [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][0], max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][1][1] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][0], min(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][1][1] - self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)]], \
                                                                              [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][2][1] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], min(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][2][1] - self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)]], \
                                                                              [[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], max(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1] + self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][0], min(self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][3][1] - self._DesignParameter['_VIAPMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1] - self._DesignParameter['_AdditionalMet12Met2OnGate3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)]]]

            #self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'] + self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'] ################



        self._DesignParameter['_AdditionalMet1Routing'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0],_Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet1Routing']['_Width'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_AdditionalMet1Routing']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][1]]],\
                                                                             [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - _DRCObj._Metal1MinWidth / 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2], [self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2]]]

        self._DesignParameter['_AdditionalMet2Routing'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0],_Datatype = DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet2Routing']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_AdditionalMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1]], [self._DesignParameter['_PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][0][1]]], \
                                                                             [[self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][1][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][1][1]], [self._DesignParameter['_PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][1][1]]]]

        self._DesignParameter['_AdditionalMet3Routing'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL3'][0],_Datatype = DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet3Routing']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_AdditionalMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1]], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1]]],
                                                                             #[[self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth / 2], [self._DesignParameter['_VIAPMOS3Poly2Met1']['_XYCoordinates'][2][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2 + _tmpLength / 4 + _DRCObj._MetalxMinWidth * 3 / 2 + _DRCObj._MetalxMinSpace]], \
                                                                             [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - _DRCObj._Metal1MinWidth / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]], #(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) / 2], #[(self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) / 2 + _DRCObj._Metal1MinWidth / 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) / 2], \
                                                                              #[(self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) / 2 + _DRCObj._Metal1MinWidth / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]],
                                                                              [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]]]]

        _ViaNumMet34X = 2
        _ViaNumMet34Y = 1

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRouting1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met4forRouting1In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRouting1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRouting1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_VIAMet32Met4forRouting1']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth / 2, self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]]]###(self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][3][1]) / 2]]

        del _ViaNumMet34


        _ViaNumMet34X = 1
        _ViaNumMet34Y = 2

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRoutingY'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met4forRoutingYIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRoutingY']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRoutingY']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1] - self._DesignParameter['_VIAMet32Met4forRoutingY']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2], \
                                                                               [self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['_VIAMet32Met4forRoutingY']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2], \
                                                                               [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAMet32Met4forRoutingY']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2 - _DRCObj._MetalxMinWidth / 2], \
                                                                               [self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAMet32Met4forRoutingY']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2 + _DRCObj._MetalxMinWidth / 2]]

        del _ViaNumMet34




        _ViaNumMet23X = 2
        _ViaNumMet23Y = 1

        _ViaNumMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaNumMet23['_ViaMet22Met3NumberOfCOX'] = _ViaNumMet23X
        _ViaNumMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumMet23Y

        self._DesignParameter['_VIAMet22Met3forRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAMet22Met3forRoutingIn{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet22Met3forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaNumMet23)
        self._DesignParameter['_VIAMet22Met3forRouting']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][0], self._DesignParameter['_AdditionalMet12Met2OnGate3']['_XYCoordinates'][3][1]]]

        del _ViaNumMet23


        _ViaNumMet34X = 2
        _ViaNumMet34Y = 1

        _ViaNumMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaNumMet34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        _ViaNumMet34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y

        self._DesignParameter['_VIAMet32Met4forRouting2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met4forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet32Met4forRouting2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaNumMet34)
        self._DesignParameter['_VIAMet32Met4forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAMet32Met4forRouting2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2]]

        del _ViaNumMet34

        _ViaNumMet23X = 2
        _ViaNumMet23Y = 1

        _ViaNumMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaNumMet23['_ViaMet22Met3NumberOfCOX'] = _ViaNumMet23X
        _ViaNumMet23['_ViaMet22Met3NumberOfCOY'] = _ViaNumMet23Y

        self._DesignParameter['_VIAMet22Met3forRouting2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAMet22Met3forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet22Met3forRouting2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaNumMet23)
        self._DesignParameter['_VIAMet22Met3forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAMet32Met4forRouting2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2]]

        del _ViaNumMet23

        _ViaNumMet12X = 2
        _ViaNumMet12Y = 1

        _ViaNumMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaNumMet12['_ViaMet12Met2NumberOfCOX'] = _ViaNumMet12X
        _ViaNumMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNumMet12Y

        self._DesignParameter['_VIAMet12Met2forRouting2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='VIAMet12Met2forRouting2In{}'.format(_Name)))[0]
        self._DesignParameter['_VIAMet12Met2forRouting2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaNumMet12)
        self._DesignParameter['_VIAMet12Met2forRouting2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAMet32Met4forRouting2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2, (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2]]

        del _ViaNumMet12

        _ViaMOS3Met34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaMOS3Met34['_ViaMet32Met4NumberOfCOX'] = 2
        _ViaMOS3Met34['_ViaMet32Met4NumberOfCOY'] = 1

        self._DesignParameter['_AdditionalMet32Met4OnMOS3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='AdditionalMet32Met4OnMOS3In{}'.format(_Name)))[0]
        self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMOS3Met34)
        self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'] = [[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2 - _DRCObj._MetalxMinWidth /2, (self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1]) / 2]]

        del _ViaMOS3Met34


        ## Right Metal 4 routing
        self._DesignParameter['_AdditionalMet4Routing3'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL4'][0],_Datatype = DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet4Routing3']['_Width'] = _DRCObj._MetalxMinWidth
        self._DesignParameter['_AdditionalMet4Routing3']['_XYCoordinates'] = [[[self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][1]],
                                                                                [self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][1][0], (self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][0][1] + self._DesignParameter['_VIAPMOS1Poly2Met1']['_XYCoordinates'][2][1]) / 2 + _DRCObj._MetalxMinWidth / 2]]]


        self._DesignParameter['_AdditionalMet4Routing1'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL4'][0],_Datatype = DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet4Routing1']['_Width'] = _DRCObj._MetalxMinWidth #### ??????
        self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'][0], [self._DesignParameter['_ViaMet32Met4forRoutingoverVSS']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet32Met4OnMOS3']['_XYCoordinates'][0][1]]], \
                                                                            [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],  self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0],  self._DesignParameter['_AdditionalMet32Met4OnGate3']['_XYCoordinates'][2][1]]]]

        ## Right Metal 2 routing
        self._DesignParameter['_AdditionalMet2Routing1'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0],_Datatype = DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_AdditionalMet2Routing1']['_Width'] = _DRCObj._MetalxMinWidth #### ??????
        self._DesignParameter['_AdditionalMet2Routing1']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_XYCoordinates'][0], [self._DesignParameter['_ViaMet22Met3forRoutingoverVSS']['_XYCoordinates'][0][0], self._DesignParameter['_AdditionalMet12Met2OnMOS4']['_XYCoordinates'][0][1]]]]







        # _ViaNumMet34X = int(self._DesignParameter['_Met1OutputRouting']['_Width'] / _DRCObj._MetalxMinWidth)
        # if _ViaNumMet34X < 1 :
        #     _ViaNumMet34X = 1
        #
        # _ViaNumMet34Y = int ((self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][0][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_XYCoordinates'][2][1] - self._DesignParameter['_VIAPMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._MetalxMinSpace) / (_DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace)) - 2
        # if _ViaNumMet34Y < 2 :
        #     _ViaNumMet34Y = 2
        #
        # _ViaMOS3Met34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        # _ViaMOS3Met34['_ViaMet32Met4NumberOfCOX'] = _ViaNumMet34X
        # _ViaMOS3Met34['_ViaMet32Met4NumberOfCOY'] = _ViaNumMet34Y






        #####################################NWELL&SLVT&PPLayer Generation & Coordinates#######################################
        #####################################NWELL Generation & Coordinates#######################################
        _SupplyRailYwidth = _DRCObj._CoMinWidth * _NumSupplyCoY + _DRCObj._CoMinSpace * _NumSupplyCoY
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['NWELL'][0],_Datatype = DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_NWLayer']['_Width'] = max(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive, \
                                                          self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + _DRCObj._PolygateMinSpace * 3 + 2 * _DRCObj._NwMinSpacetoRX)

        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + _SupplyRailYwidth / 2 + _DRCObj._NwMinEnclosurePactive], \
                                                                [self._DesignParameter['NbodyContact']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]], \
                                                                [[self._DesignParameter['NbodyContact']['_XYCoordinates'][1][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][1][1] - _SupplyRailYwidth / 2 - _DRCObj._NwMinEnclosurePactive], \
                                                                [self._DesignParameter['NbodyContact']['_XYCoordinates'][1][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2]]]

        #####################################SLVT Generation & Coordinates#######################################
        if _SLVT == True :
            self._DesignParameter['_SLVTPMOSLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['SLVT'][0],_Datatype = DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates = [], _Width=None)
            self._DesignParameter['_SLVTPMOSLayer']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_SLVTPMOSLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]],[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]], \
                                                                     [[self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]],[self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]]]]

            self._DesignParameter['_SLVTNMOSLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['SLVT'][0],_Datatype = DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates = [], _Width=None)
            self._DesignParameter['_SLVTNMOSLayer']['_Width'] = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_SLVTNMOSLayer']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]], \
                                                                    [[self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_NMOS1']['_XYCoordinates'][1][1]], [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2, self._DesignParameter['_NMOS4']['_XYCoordinates'][1][1]]]]

        #####################################PPLayer Generation & Coordinates#######################################
        self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['PIMP'][0],_Datatype = DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates = [], _Width=None)
        self._DesignParameter['_PPLayer']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1]],[self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS4']['_XYCoordinates'][0][1]]], \
                                                                [[self._DesignParameter['_PMOS1']['_XYCoordinates'][1][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]],[self._DesignParameter['_PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2, self._DesignParameter['_PMOS4']['_XYCoordinates'][1][1]]]]



        #####################################Pin Generation & Coordinates#######################################
        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VSS')
        self._DesignParameter['_INpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'IN')
        self._DesignParameter['_INbpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'INb')
        self._DesignParameter['_OUTpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'OUT')
        self._DesignParameter['_OUTbpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'OUTb')

        self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeightAtOneSide], [0, 0 - _VDD2VSSHeightAtOneSide]]
        self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['_INbpin']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['_INpin']['_XYCoordinates'] = [[self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][0], self._DesignParameter['_VIAPMOS2Poly2Met1']['_XYCoordinates'][1][1]]]
        self._DesignParameter['_OUTpin']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1]]]
        self._DesignParameter['_OUTbpin']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][1][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], 0 - (self._DesignParameter['_PMOS1']['_XYCoordinates'][1][1])]]



        ########################### Additonal Power Line Generation (Metal First then Via) ###############################
        if _PowerLine == True :
            self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met5LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met6LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
    
            
            self._DesignParameter['_Met2LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_Met3LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)            
            self._DesignParameter['_Met5LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met6LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_Met2LayerVDD']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met2LayerVDD']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerVDD']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met3LayerVDD']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerVDD']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met4LayerVDD']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met5LayerVDD']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met5LayerVDD']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met6LayerVDD']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met6LayerVDD']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            self._DesignParameter['_Met2LayerVSS1']['_XWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met2LayerVSS2']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerVSS']['_XWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met3LayerVSS']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerVSS2']['_XWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met3LayerVSS2']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']





            self._DesignParameter['_Met4LayerVSS1']['_XWidth'] = (self._DesignParameter['_AdditionalMet4Routing3']['_XYCoordinates'][0][0][0] - _DRCObj._MetalxMinSpace21 -
                                                                self._DesignParameter['_AdditionalMet4Routing3']['_Width'] // 2)- \
                                                                (self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] - 
                                                                self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2)
            self._DesignParameter['_Met4LayerVSS1']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerVSS2']['_XWidth'] = (self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][1][0][0] - _DRCObj._MetalxMinSpace21 -
                                                                self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2) - \
                                                                (self._DesignParameter['_AdditionalMet4Routing3']['_XYCoordinates'][0][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                self._DesignParameter['_AdditionalMet4Routing3']['_Width'] // 2)
            self._DesignParameter['_Met4LayerVSS2']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerVSS3']['_XWidth'] = (self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0] - _DRCObj._MetalxMinSpace21 -
                                                                self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2) - \
                                                                (self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][1][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2)
            self._DesignParameter['_Met4LayerVSS3']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met4LayerVSS4']['_XWidth'] = (self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] + 
                                                                self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2) - \
                                                                (self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2)
            self._DesignParameter['_Met4LayerVSS4']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met5LayerVSS']['_XWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met5LayerVSS']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met6LayerVSS']['_XWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met6LayerVSS']['_YWidth'] = self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            
            self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = self._DesignParameter['PbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met3LayerVSS1']['_XYCoordinates'] = [[(self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][2][0][0] - self._DesignParameter['_Met3RoutingOnNMOS']['_Width'] / 2 - _DRCObj._MetalxMinSpace21 + self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] - self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2) / 2, self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_Met3LayerVSS2']['_XYCoordinates'] = [[(self._DesignParameter['_Met3RoutingOnNMOS']['_XYCoordinates'][2][0][0] + self._DesignParameter['_Met3RoutingOnNMOS']['_Width'] / 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2) / 2, self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]

            self._DesignParameter['_Met4LayerVSS1']['_XYCoordinates'] = [[self._DesignParameter['PbodyContact']['_XYCoordinates'][0][0] - 
                                                                        self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                                                        int(round(self._DesignParameter['_Met4LayerVSS1']['_XWidth'] + 0.5)) // 2 ,
                                                                        self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing3']['_XYCoordinates'][0][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                        self._DesignParameter['_AdditionalMet4Routing3']['_Width'] // 2 +
                                                                        self._DesignParameter['_Met4LayerVSS2']['_XWidth'] // 2 ,
                                                                        self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_Met4LayerVSS3']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][1][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                        self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2 +
                                                                        self._DesignParameter['_Met4LayerVSS3']['_XWidth'] // 2 ,
                                                                        self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_Met4LayerVSS4']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalMet4Routing1']['_XYCoordinates'][0][0][0] + _DRCObj._MetalxMinSpace21 +
                                                                        self._DesignParameter['_AdditionalMet4Routing1']['_Width'] // 2 +
                                                                        int(round(self._DesignParameter['_Met4LayerVSS4']['_XWidth'] + 0.5)) // 2 ,
                                                                        self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'] = self._DesignParameter['PbodyContact']['_XYCoordinates']
            self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'] = self._DesignParameter['PbodyContact']['_XYCoordinates']


            ############ Via Generations ##############
            _ViaNumVDDX = int(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVDDY = int(self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSX1forMet3 = int(self._DesignParameter['_Met3LayerVSS1']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSX2forMet3 = int(self._DesignParameter['_Met3LayerVSS2']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            _ViaNumVSSX1 = int(self._DesignParameter['_Met4LayerVSS1']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSX2 = int(self._DesignParameter['_Met4LayerVSS2']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSX3 = int(self._DesignParameter['_Met4LayerVSS3']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            _ViaNumVSSX4 = int(self._DesignParameter['_Met4LayerVSS4']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

            if _ViaNumVDDX < 1 :
                _ViaNumVDDX = 1
            if _ViaNumVDDY < 1 :
                _ViaNumVDDY = 1
            if _ViaNumVSSX1 < 1 :
                self._DesignParameter['_Met4LayerVSS1']['_XYCoordinates'] = []
            if _ViaNumVSSX2 < 1 :
                self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'] = []
            if _ViaNumVSSX3 < 1 :
                self._DesignParameter['_Met4LayerVSS3']['_XYCoordinates'] = []
            if _ViaNumVSSX4 < 1 :
                self._DesignParameter['_Met4LayerVSS4']['_XYCoordinates'] = []
            if _ViaNumVSSX1forMet3 < 1 :
                self._DesignParameter['_Met3LayerVSS1']['_XYCoordinates'] = []
            if _ViaNumVSSX2forMet3 < 1 :
                self._DesignParameter['_Met3LayerVSS2']['_XYCoordinates'] = []



            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VDD']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVDDMet32Met4)
            self._DesignParameter['_ViaMet32Met4VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet42Met5VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5VDD']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVDDMet42Met5)
            self._DesignParameter['_ViaMet42Met5VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            _ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = _ViaNumVDDX
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet52Met6VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6VDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet52Met6VDD']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVDDMet52Met6)
            self._DesignParameter['_ViaMet52Met6VDD']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates']

            _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet12Met2VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2VSS']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met2)
            self._DesignParameter['_ViaMet12Met2VSS']['_XYCoordinates'] = self._DesignParameter['PbodyContact']['_XYCoordinates']

            _ViaVSSMet22Met31 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX1forMet3
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet22Met3VSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3VSS1In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VSS1']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met31)
            self._DesignParameter['_ViaMet22Met3VSS1']['_XYCoordinates'] = self._DesignParameter['_Met3LayerVSS1']['_XYCoordinates']

            _ViaVSSMet22Met32 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met32['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX2forMet3
            _ViaVSSMet22Met32['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet22Met3VSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3VSS2In{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3VSS2']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met32)
            self._DesignParameter['_ViaMet22Met3VSS2']['_XYCoordinates'] = self._DesignParameter['_Met3LayerVSS2']['_XYCoordinates']



            _ViaVSSMet32Met41 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOX'] = _ViaNumVSSX1
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met41VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VSS1']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met41)
            self._DesignParameter['_ViaMet32Met4VSS1']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS1']['_XYCoordinates']

            _ViaVSSMet32Met42 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met42['_ViaMet32Met4NumberOfCOX'] = _ViaNumVSSX2
            _ViaVSSMet32Met42['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met42VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VSS2']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met42)
            self._DesignParameter['_ViaMet32Met4VSS2']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates']

            _ViaVSSMet32Met43 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met43['_ViaMet32Met4NumberOfCOX'] = _ViaNumVSSX3
            _ViaVSSMet32Met43['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VSS3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met43VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VSS3']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met43)
            self._DesignParameter['_ViaMet32Met4VSS3']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS3']['_XYCoordinates']

            _ViaVSSMet32Met44 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met44['_ViaMet32Met4NumberOfCOX'] = _ViaNumVSSX4
            _ViaVSSMet32Met44['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet32Met4VSS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met44VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4VSS4']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met44)
            self._DesignParameter['_ViaMet32Met4VSS4']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS4']['_XYCoordinates']

            _ViaVSSMet42Met51 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met51['_ViaMet42Met5NumberOfCOX'] = _ViaNumVSSX1
            _ViaVSSMet42Met51['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet42Met5VSS1'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met51VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5VSS1']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met51)
            self._DesignParameter['_ViaMet42Met5VSS1']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS1']['_XYCoordinates']

            _ViaVSSMet42Met52 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met52['_ViaMet42Met5NumberOfCOX'] = _ViaNumVSSX2
            _ViaVSSMet42Met52['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet42Met5VSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met52VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5VSS2']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met52)
            self._DesignParameter['_ViaMet42Met5VSS2']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates']

            _ViaVSSMet42Met53 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met53['_ViaMet42Met5NumberOfCOX'] = _ViaNumVSSX3
            _ViaVSSMet42Met53['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet42Met5VSS3'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met53VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5VSS3']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met53)
            self._DesignParameter['_ViaMet42Met5VSS3']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS3']['_XYCoordinates']

            _ViaVSSMet42Met54 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met54['_ViaMet42Met5NumberOfCOX'] = _ViaNumVSSX4
            _ViaVSSMet42Met54['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet42Met5VSS4'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met54VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet42Met5VSS4']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met54)
            self._DesignParameter['_ViaMet42Met5VSS4']['_XYCoordinates'] = self._DesignParameter['_Met4LayerVSS4']['_XYCoordinates']

            _ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = _ViaNumVDDX
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = _ViaNumVDDY
            self._DesignParameter['_ViaMet52Met6VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6VSSIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet52Met6VSS']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVSSMet52Met6)
            self._DesignParameter['_ViaMet52Met6VSS']['_XYCoordinates'] = self._DesignParameter['PbodyContact']['_XYCoordinates']




if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'

    SRLatchObj = _SRLatch(_DesignParameter=None, _Name='SRLatch')
    SRLatchObj._CalculateDesignParameter(_Finger1 = 5, _Finger2 = 1, _Finger3 = 2, _Finger4 = 2, \
                                  #_PMOSFinger1 = 1, _PMOSFinger2 = 3, _PMOSFinger3 = 3, _PMOSFinger4 = 3, \
                                  _NMOSChannelWidth1 = 200, _PMOSChannelWidth1 = 400, _NMOSChannelWidth2 = 200, _PMOSChannelWidth2 = 400, _NMOSChannelWidth3 = 200, _PMOSChannelWidth3 = 400, _NMOSChannelWidth4 = 200, _PMOSChannelWidth4 = 400, _ChannelLength = 30,\
                                  _VDD2VSSHeightAtOneSide = None, _Dummy = True, _NumSupplyCoX = None, _NumSupplyCoY = 2, \
                                  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, NumViaPoly2Met1CoX = None, \
                                  NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None, \
                                  NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None, NumViaPMOSMet22Met3CoX = None, NumViaPMOSMet22Met3CoY = None, \
                                  NumViaNMOSMet22Met3CoX = None, NumViaNMOSMet22Met3CoY = None, _SLVT = True,
                                  _PowerLine = False)

    # SRLatchObj._CalculateDesignParameter(_Finger1 = 1, _Finger2 = 1, _Finger3 = 1, _Finger4 = 1, \
    #                               #_PMOSFinger1 = 1, _PMOSFinger2 = 3, _PMOSFinger3 = 3, _PMOSFinger4 = 3, \
    #                               _NMOSChannelWidth1 = 200, _PMOSChannelWidth1 = 400, _NMOSChannelWidth2 = 200, _PMOSChannelWidth2 = 400, _NMOSChannelWidth3 = 200, _PMOSChannelWidth3 = 400, _NMOSChannelWidth4 = 200, _PMOSChannelWidth4 = 400, _ChannelLength = 30,\
    #                               _VDD2VSSHeightAtOneSide = None, _Dummy = True, _NumSupplyCoX = None, _NumSupplyCoY = 2, \
    #                               _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, NumViaPoly2Met1CoX = None, \
    #                               NumViaPoly2Met1CoY = None, NumViaPMOSMet12Met2CoX = None, NumViaPMOSMet12Met2CoY = None, \
    #                               NumViaNMOSMet12Met2CoX = None, NumViaNMOSMet12Met2CoY = None, NumViaPMOSMet22Met3CoX = None, NumViaPMOSMet22Met3CoY = None, \
    #                               NumViaNMOSMet22Met3CoX = None, NumViaNMOSMet22Met3CoY = None, _SLVT = True,
    #                               _PowerLine = False)
    #

    SRLatchObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = SRLatchObj._DesignParameter)
    _fileName = 'SRLatch.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = SRLatchObj._CreateGDSStream(SRLatchObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    import ftplib

    #ftp = ftplib.FTP('141.223.29.61')
    #ftp.login('jicho0927', 'cho89140616!!')
    #ftp.cwd('/mnt/sda/jicho0927/OPUS/SAMSUNG28n')
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('SRLatch.gds', 'rb')
    ftp.storbinary('STOR SRLatch.gds', myfile)
    myfile.close()
    ftp.close()

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('SRLatch.gds', 'rb')
    ftp.storbinary('STOR SRLatch.gds', myfile)
    myfile.close()
    ftp.close()

    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('SRLatch.gds', 'rb')
    ftp.storbinary('STOR SRLatch.gds', myfile)
    myfile.close()
    ftp.close()
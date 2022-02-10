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
import ftplib

## This is for Resistor Bank...

class _TransmissionGate (StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(_Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,_VDD2VSSHeight=None, _Dummy = False, _SLVT = False, _SupplyMet1YWidth=None, 
                                            _Gatereverse = False, _Bodycontact = False)

    def __init__(self, _DesignParameter = None, _Name = 'TransmissionGate'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None :
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateTransmissionGate (self, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None, _VDD2VSSHeight = None, _Dummy = False,
                            _SLVT = False, _Gatereverse = False, _NumSupplyCOX=None, _NumSupplyCOY=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None,
                                    _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None, _Bodycontact = False) :
        ## You Should Draw N-WELL Afterwards!!
        print ('#########################################################################################################')
        print ('                              {}  TransmissionGate Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'TransmissionGate'

        print ('###############################     MOSFET Generation    ################################################')
        _NMOSinputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        _NMOSinputs['_NMOSNumberofGate'] = _Finger
        _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
        _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        _NMOSinputs['_NMOSDummy'] = _Dummy
        _NMOSinputs['_SLVT'] = _SLVT

        self._DesignParameter['_NMOSTG'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle =0, _DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOSTG']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

        if _NPRatio == None:
            _NPRatio = 2
        # Default NPRatio = 2

        _PMOSinputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _PMOSinputs['_PMOSNumberofGate'] = _Finger
        _PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        _PMOSinputs['_PMOSChannellength'] = _ChannelLength
        _PMOSinputs['_PMOSDummy'] = _Dummy
        _PMOSinputs['_SLVT'] = _SLVT

        self._DesignParameter['_PMOSTG'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOSTG']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

        print ('################################     VDD VSS Generation    ##############################################')
        _NumSupplyCOX = int(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        if _NumSupplyCOX < 2:
            _NumSupplyCOX = 2
        if _NumSupplyCOY == None:
            _NumSupplyCOY = 2

        _PBodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _PBodyinputs['_NumberOfPbodyCOX'] = _NumSupplyCOX
        _PBodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCOY
        # _PBodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _PBodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['_PbodycontactTG'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='Pbodycontactin{}'.format(_Name)))[0]
        self._DesignParameter['_PbodycontactTG']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PBodyinputs)

        _NBodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _NBodyinputs['_NumberOfNbodyCOX'] = _NumSupplyCOX
        _NBodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCOY
        # _NBodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
        _NBodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['_NbodycontactTG'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='Nbodycontactin{}'.format(_Name)))[0]
        self._DesignParameter['_NbodycontactTG']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NBodyinputs)

        print ('###########################     Via Generation for PMOS Outputs     #####################################')
        _ViaPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
            _ViaPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                                                         2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] == 1 :
                _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2
        else:
            _ViaPMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumVIAMet12COX
            _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NumVIAMet12COY

        _ViaPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] = int(
                (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] == 1 :
                _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] = 2
        else:
            _ViaPMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NumVIAMet12COX
            _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NumVIAMet12COY


        _ViaPMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaPMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaPMOSMet34['_ViaMet32Met4NumberOfCOY'] = int(
                (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaPMOSMet34['_ViaMet32Met4NumberOfCOY'] == 1:
                _ViaPMOSMet34['_ViaMet32Met4NumberOfCOY'] = 2
        else:
            _ViaPMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NumVIAMet12COX
            _ViaPMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NumVIAMet12COY

        _ViaPMOSMet45 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaPMOSMet45['_ViaMet42Met5NumberOfCOX'] = 1
            _ViaPMOSMet45['_ViaMet42Met5NumberOfCOY'] = int(
                (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaPMOSMet45['_ViaMet42Met5NumberOfCOY'] == 1:
                _ViaPMOSMet45['_ViaMet42Met5NumberOfCOY'] = 2
        else:
            _ViaPMOSMet45['_ViaMet42Met5NumberOfCOX'] = _NumVIAMet12COX
            _ViaPMOSMet45['_ViaMet42Met5NumberOfCOY'] = _NumVIAMet12COY

        _ViaPMOSMet56 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaPMOSMet56['_ViaMet52Met6NumberOfCOX'] = 1
            _ViaPMOSMet56['_ViaMet52Met6NumberOfCOY'] = int(
                (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaPMOSMet56['_ViaMet52Met6NumberOfCOY'] == 1:
                _ViaPMOSMet56['_ViaMet52Met6NumberOfCOY'] = 2
        else:
            _ViaPMOSMet56['_ViaMet52Met6NumberOfCOX'] = _NumVIAMet12COX
            _ViaPMOSMet56['_ViaMet52Met6NumberOfCOY'] = _NumVIAMet12COY


        self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaPMOSMet12)

        self._DesignParameter['_ViaMet22Met3OnPMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaPMOSMet23)

        self._DesignParameter['_ViaMet32Met4OnPMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaMet32Met4OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaPMOSMet34)

        self._DesignParameter['_ViaMet42Met5OnPMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaMet42Met5OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnPMOSOutputTG']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaPMOSMet45)

        self._DesignParameter['_ViaMet52Met6OnPMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None,_Name='ViaMet52Met6OnPMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnPMOSOutputTG']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaPMOSMet56)





        print ('###########################     Via Generation for NMOS Outputs     #####################################')
        _ViaNMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
            _ViaNMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                                                         2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] == 1 :
                _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2
        else:
            _ViaNMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumVIAMet12COX
            _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NumVIAMet12COY

        _ViaNMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaNMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaNMOSMet23['_ViaMet22Met3NumberOfCOY'] = int(
                (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaNMOSMet23['_ViaMet22Met3NumberOfCOY'] == 1 :
                _ViaNMOSMet23['_ViaMet22Met3NumberOfCOY'] = 2
        else:
            _ViaNMOSMet23['_ViaMet22Met3NumberOfCOX'] = _NumVIAMet12COX
            _ViaNMOSMet23['_ViaMet22Met3NumberOfCOY'] = _NumVIAMet12COY

        _ViaNMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaNMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaNMOSMet34['_ViaMet32Met4NumberOfCOY'] = int(
                (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaNMOSMet34['_ViaMet32Met4NumberOfCOY'] == 1:
                _ViaNMOSMet34['_ViaMet32Met4NumberOfCOY'] = 2
        else:
            _ViaNMOSMet34['_ViaMet32Met4NumberOfCOX'] = _NumVIAMet12COX
            _ViaNMOSMet34['_ViaMet32Met4NumberOfCOY'] = _NumVIAMet12COY

        _ViaNMOSMet45 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaNMOSMet45['_ViaMet42Met5NumberOfCOX'] = 1
            _ViaNMOSMet45['_ViaMet42Met5NumberOfCOY'] = int(
                (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaNMOSMet45['_ViaMet42Met5NumberOfCOY'] == 1:
                _ViaNMOSMet45['_ViaMet42Met5NumberOfCOY'] = 2
        else:
            _ViaNMOSMet45['_ViaMet42Met5NumberOfCOX'] = _NumVIAMet12COX
            _ViaNMOSMet45['_ViaMet42Met5NumberOfCOY'] = _NumVIAMet12COY

        _ViaNMOSMet56 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        if (_NumVIAMet12COX==None and  _NumVIAMet12COY==None):
            _ViaNMOSMet56['_ViaMet52Met6NumberOfCOX'] = 1
            _ViaNMOSMet56['_ViaMet52Met6NumberOfCOY'] = int(
                (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            if _ViaNMOSMet56['_ViaMet52Met6NumberOfCOY'] == 1:
                _ViaNMOSMet56['_ViaMet52Met6NumberOfCOY'] = 2
        else:
            _ViaNMOSMet56['_ViaMet52Met6NumberOfCOX'] = _NumVIAMet12COX
            _ViaNMOSMet56['_ViaMet52Met6NumberOfCOY'] = _NumVIAMet12COY

        

        self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaNMOSMet12)

        self._DesignParameter['_ViaMet22Met3OnNMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaNMOSMet23)

        self._DesignParameter['_ViaMet32Met4OnNMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaMet32Met4OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaNMOSMet34)

        self._DesignParameter['_ViaMet42Met5OnNMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaMet42Met5OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnNMOSOutputTG']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaNMOSMet45)

        self._DesignParameter['_ViaMet52Met6OnNMOSOutputTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None,_Name='ViaMet52Met6OnNMOSOutputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnNMOSOutputTG']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaNMOSMet56)


        print ("###########################     Via Generation for PMOS Controls     #####################################")
        _ViaPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _TotalLenOfPMOSGate = \
        self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][
            -1][0] - \
        self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][
            0][0]
        + 2 * self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        ## [-1] means the last value of the list or key of dict

        tmp4X_P = int(round(_TotalLenOfPMOSGate // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)))
        if tmp4X_P <= 1:
            tmp4X_P = 2  ## Default value for # of contact in x axis
            _NumVIAPoly2Met1COX = tmp4X_P
        if _NumVIAPoly2Met1COX == None:
            _NumVIAPoly2Met1COX = tmp4X_P
        if _NumVIAPoly2Met1COY == None:
            _NumVIAPoly2Met1COY = 1
        
        if (_Finger == 1) :
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 1
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
        else :
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _NumVIAPoly2Met1COX
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumVIAPoly2Met1COY


        self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSControlIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPMOSPoly2Met1)


        _ViaPMOSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)

        tmp4vX_P = int(round(self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
        if tmp4vX_P <= 1:
            tmp4vX_P = 2  ## Default value for # of contact in x axis
            _NumVIAMet12Met2COX = tmp4vX_P
        else:
            _NumVIAMet12Met2COX = tmp4vX_P
        _NumVIAMet12Met2COY = 1
        _ViaPMOSMet12Met2['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaPMOSMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet12Met2OnPMOSControlTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnPMOSControlIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaPMOSMet12Met2)


        del tmp4X_P, tmp4vX_P

        print ("###########################     Via Generation for NMOS Controls      #####################################")
        _ViaNMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _TotalLenOfNMOSGate = \
            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting'][
                '_XYCoordinates'][
                -1][0] - \
            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting'][
                '_XYCoordinates'][
                0][0] + 2 * self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        ## [-1] means the last value of the list or key of dict

        tmp4X = int(round(_TotalLenOfNMOSGate // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)))
        if tmp4X <= 1:
            tmp4X = 2  ## Default value for # of contact in x axis
        if _NumVIAPoly2Met1COX == None:
            _NumVIAPoly2Met1COX = tmp4X
        if _NumVIAPoly2Met1COY == None:
            _NumVIAPoly2Met1COY = 1

        if (_Finger == 1) :
            _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = 1
            _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1

        else :
            _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _NumVIAPoly2Met1COX
            _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumVIAPoly2Met1COY


        self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSControlIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaNMOSPoly2Met1)



        _ViaNMOSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)

        tmp4vX = int(round(self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
        if tmp4vX <= 1:
            tmp4vX = 2  ## Default value for # of contact in x axis
        else:
            _NumVIAMet12Met2COX = tmp4vX
        _NumVIAMet12Met2COY = 1
        _ViaNMOSMet12Met2['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaNMOSMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1


        self._DesignParameter['_ViaMet12Met2OnNMOSControlTG'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnNMOSControlIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaNMOSMet12Met2)

        del tmp4X, tmp4vX

        print('################################     Coordinates Settings     ############################################')
        if (_Gatereverse == False) :
            #if (_ChannelWidth * _NPRatio <= 700) :
            _VDD2VSSMinHeight = (self._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
                            (self._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
                            max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +
                                (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) + \
                            max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +
                                (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) + \
                            self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                            self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 5 * _DRCObj._Metal1MinSpace3
                            # self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + \
                            # self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + \
                                
            # else :
            #     _VDD2VSSMinHeight = (self._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
            #                     (self._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
            #                     max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
            #                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +
            #                         (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) + \
            #                     max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
            #                         self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +
            #                         (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) + \
            #                     self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
            #                     self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
            #                     self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] + \
            #                     self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] + \
            #                     + 4 * _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8

            print ('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ SET MINIMUM HEIGHT VALUE TO FOR TransmissionGate : ', _VDD2VSSMinHeight)

            if _VDD2VSSHeight == None:
                _VDD2VSSHeight = _VDD2VSSMinHeight

            else:
                if _VDD2VSSHeight < _VDD2VSSMinHeight:
                    raise Exception('@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@# SET MINIMUM HEIGHT VALUE FOR TransmissionGate : ', _VDD2VSSMinHeight)

            ## BODY CONTACTS, MOS FIRST
            _PbodyObj = PbodyContact._PbodyContact()
            _PbodyObj._DesignParameter['_XYCoordinates'] = [[0, 0]]  ## This is the Origin Value of the TG!!
            _NbodyObj = NbodyContact._NbodyContact()
            _NbodyObj._DesignParameter['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

            if _Bodycontact == True : 
                self._DesignParameter['_PbodycontactTG']['_XYCoordinates'] = _PbodyObj._DesignParameter['_XYCoordinates']
                self._DesignParameter['_NbodycontactTG']['_XYCoordinates'] = _NbodyObj._DesignParameter['_XYCoordinates']

            else :
                self._DesignParameter['_PbodycontactTG']['_XYCoordinates'] = []
                self._DesignParameter['_NbodycontactTG']['_XYCoordinates'] = []

            self._DesignParameter['_NMOSTG']['_XYCoordinates'] = [[0, max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                            self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 +
                                                                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                            self._DesignParameter['_PbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
                            _DRCObj._Metal1MinSpace3]]


            #if (_ChannelWidth * _NPRatio <= 700) :
            self._DesignParameter['_PMOSTG']['_XYCoordinates'] = [[0, _VDD2VSSHeight - (max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] /2 ,
                        self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] //2 +
                                                                                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                        self._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
                        _DRCObj._MetalxMinSpace8)]]

            # else :
            #     self._DesignParameter['_PMOSTG']['_XYCoordinates'] = [[0, _VDD2VSSHeight - (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                 self._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                 _DRCObj._MetalxMinSpace8)]]

            ## control via coordinate

            if _Finger == 1 :
                self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
                                                                            max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                                                                            self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                                (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                                                                            self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                            +_DRCObj._Metal1MinSpace3]]

                self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] -
                                                                                    (max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                                                                                    self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                                        (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                                                                                    self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                                    +_DRCObj._Metal1MinSpace3)]]
            else : ## Recently editted
                self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
                                                                                max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ,
                                                                                self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 +
                                                                                    (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                                                                                self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+
                                                                            +_DRCObj._Metal1MinSpace2]]

                self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] -
                                                                                (max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                                                                                    self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                                    (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
                                                                                self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
                                                                                +_DRCObj._Metal1MinSpace2)]]


            # if _Finger == 1 :
            #     self._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #                                                                 max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
            #                                                                 self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
            #                                                                 self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                 +_DRCObj._Metal1MinSpace3]]

            #     self._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] -
            #                                                                         (max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
            #                                                                         self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                             (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                         +_DRCObj._Metal1MinSpace3)]]
            # else :
            #     self._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],
            #                                                                 self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #                                                                         max(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ,
            #                                                                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 +
            #                                                                             (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+
            #                                                                     +_DRCObj._Metal1MinSpace2]]

            #     self._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'] = [[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],
            #                                                                 self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] -
            #                                                                         (max(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
            #                                                                             self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                             (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) +
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 +
            #                                                                         +_DRCObj._Metal1MinSpace2)]]

            ##input output via coordinates
            tmp1 = []
            tmp2 = []
            for i in range(0, len(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmp1.append([self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],
                            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4]) ## inward
            for i in range(0, len(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tmp2.append([self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0],
                            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] -
                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4])  ## outward

            if _Finger % 2 == 0 :
                self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'] = tmp1 + tmp2
                self._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'] = tmp2
                self._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet42Met5OnNMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet52Met6OnNMOSOutputTG']['_XYCoordinates'] = []

            else :
                self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'] = tmp1 + tmp2
                self._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'] = tmp2
                self._DesignParameter['_ViaMet32Met4OnNMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet42Met5OnNMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet52Met6OnNMOSOutputTG']['_XYCoordinates'] = []
            del tmp1, tmp2

            tmp1 = []
            tmp2 = []
            for i in range(0, len(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmp1.append([self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],
                            self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] -
                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4])
            for i in range(0, len(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmp2.append([self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter[
                                '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0],
                            self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter[
                                '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4])

            if _Finger % 2 == 0 :
                self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_XYCoordinates'] = tmp1 + tmp2
                self._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'] = tmp2
                self._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet42Met5OnPMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet52Met6OnPMOSOutputTG']['_XYCoordinates'] = []

            
            else :
                self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_XYCoordinates'] = tmp1 + tmp2
                self._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'] = tmp2
                self._DesignParameter['_ViaMet32Met4OnPMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet42Met5OnPMOSOutputTG']['_XYCoordinates'] = []
                self._DesignParameter['_ViaMet52Met6OnPMOSOutputTG']['_XYCoordinates'] = []
            del tmp1, tmp2


            print ('################################     Additional path Settings     #########################################')
            ##Input Poly Routings (Vertical & Horizontal)

            self._DesignParameter['_ControlNMOSRoutingTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_ControlNMOSRoutingTG']['_Width'] = self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            for i in range(0, len(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
                            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                            self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
                            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                            [self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0] +
                            self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                            self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] +
                            self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2]])

            self._DesignParameter['_ControlNMOSRoutingTG']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_ControlPMOSRoutingTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_ControlPMOSRoutingTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            for i in range(0, len(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
                            self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                            self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
                            self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                            [self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0] +
                            self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                            self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                            self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2]])

            self._DesignParameter['_ControlPMOSRoutingTG']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_ControlNMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_ControlNMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_ControlNMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0],
                                                                                self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]],
                                                                            [self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0],
                                                                                self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_ControlPMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_ControlPMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_ControlPMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0],
                                                                                    self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]],
                                                                            [self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0],
                                                                                    self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]]]]

            # self._DesignParameter['_ControlNMOSRoutingMet1TG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
            # self._DesignParameter['_ControlNMOSRoutingMet1TG']['_Width'] = self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_ControlNMOSRoutingMet1TG']['_XYCoordinates'] = [[[self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0] -
            #                                                                         self._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 ,
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]],
            #                                                                         [self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 ,
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]]]]

            # self._DesignParameter['_ControlPMOSRoutingMet1TG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
            # self._DesignParameter['_ControlPMOSRoutingMet1TG']['_Width'] = self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_ControlPMOSRoutingMet1TG']['_XYCoordinates'] = [[[self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0] -
            #                                                                         self._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 ,
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]],
            #                                                                         [self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 ,
            #                                                                         self._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]]]]

            ##Supply metal 4 routing

            # if _Finger % 2 == 0 :
            #     self._DesignParameter['_OutputPMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * 2
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0] -
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
            #                                                                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] + 
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] // 2)],
            #                                                                     [self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0] + 
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2),
            #                                                                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] // 2)]]]
                

            #     self._DesignParameter['_OutputNMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] = self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * 2
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] -
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
            #                                                                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] - 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] // 2)],
            #                                                                     [self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0] + 
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2),
            #                                                                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] - 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] // 2)]]]
                
            #     self._DesignParameter['_OutputNMOSRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingYTG']['_Width'] = self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     tmp = []
            #     for i in range (0, len(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
            #         tmp.append([[self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]],
            #                     [self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])
            #     self._DesignParameter['_OutputNMOSRoutingYTG']['_XYCoordinates'] = tmp
            #     del tmp

            #     self._DesignParameter['_OutputPMOSRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingYTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     tmp = []
            #     for i in range (0, len(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
            #         tmp.append([[self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
            #                     [self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])
            #     self._DesignParameter['_OutputPMOSRoutingYTG']['_XYCoordinates'] = tmp
            #     del tmp

            #     self._DesignParameter['_OutputRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputRoutingYTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
            #                                                                         [self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]]]]

            # else :
            #     self._DesignParameter['_OutputPMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] -
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
            #                                                                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] + 
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] // 2)],
            #                                                                     [self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + 
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2),
            #                                                                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     (self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] // 2)]]]
                

            #     self._DesignParameter['_OutputNMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] = self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] -
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
            #                                                                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] - 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] // 2)],
            #                                                                     [self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0] + 
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2),
            #                                                                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] - 
            #                                                                     (self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
            #                                                                     _DRCObj._Metal1MinSpace2 + self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] // 2)]]]
                
            #     self._DesignParameter['_OutputNMOSRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingYTG']['_Width'] = self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     tmp = []
            #     for i in range (0, len(self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
            #         tmp.append([[self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]],
            #                     [self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])
            #     self._DesignParameter['_OutputNMOSRoutingYTG']['_XYCoordinates'] = tmp
            #     del tmp

            #     self._DesignParameter['_OutputPMOSRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingYTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     tmp = []
            #     for i in range (0, len(self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
            #         tmp.append([[self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
            #                     [self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0],
            #                     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])
            #     self._DesignParameter['_OutputPMOSRoutingYTG']['_XYCoordinates'] = tmp
            #     del tmp

            #     self._DesignParameter['_OutputRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputRoutingYTG']['_Width'] = self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            #     self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
            #                                                                         [self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]]]]
            
            

            # ###output metal 3 routing
            # if (_Finger != 1) :
            #     self._DesignParameter['_OutputPMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'] = []
            #                                                                     # [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     # self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],
            #                                                                     # self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     # self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1] -
            #                                                                     # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4],
            #                                                                     # [self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     # self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
            #                                                                     # self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     # self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1] -
            #                                                                     # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4]]]

            #     self._DesignParameter['_OutputNMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'] = []
            #                             # [[[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
            #                             # self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0],
            #                             # self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #                             # self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
            #                             #     '_XYCoordinates'][0][1] +
            #                             # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4],
            #                             # [self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
            #                             # self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
            #                             #     '_XYCoordinates'][-1][0],
            #                             # self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #                             # self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
            #                             #     '_XYCoordinates'][0][1] +
            #                             # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4]]]
      
            #     self._DesignParameter['_OutputRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputRoutingYTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'] = []
            #     # [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #     #     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
            #     #     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #     #     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]],
            #     #     [self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] +
            #     #     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],
            #     #     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #     #     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]]]
            
            # else :
            #     self._DesignParameter['_OutputRoutingYTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputRoutingYTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinSpace +
            #                                                                     self._DesignParameter['_OutputRoutingYTG']['_Width'] // 2 + self._DesignParameter['_SupplyRoutingYTG']['_Width'] // 2,
            #                                                                     self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]],
            #                                                                     [self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
            #                                                                     self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0] + _DRCObj._MetalxMinSpace +
            #                                                                     self._DesignParameter['_OutputRoutingYTG']['_Width'] // 2 + self._DesignParameter['_SupplyRoutingYTG']['_Width'] // 2,
            #                                                                     self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] +
            #                                                                     self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]]]

            #     self._DesignParameter['_OutputPMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputPMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                         self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] + 
            #                                                                         self._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]],
            #                                                                         [self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'][0][0][0] + self._DesignParameter['_OutputRoutingYTG']['_Width'] // 2,
            #                                                                         self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'][0][0][1]]]]

            #     self._DesignParameter['_OutputNMOSRoutingXTG'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_Width'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            #     self._DesignParameter['_OutputNMOSRoutingXTG']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] + 
            #                                                                         self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],
            #                                                                         self._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1] + 
            #                                                                         self._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]],
            #                                                                         [self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'][0][1][0] + self._DesignParameter['_OutputRoutingYTG']['_Width'] // 2,
            #                                                                         self._DesignParameter['_OutputRoutingYTG']['_XYCoordinates'][0][1][1]]]]
      


if __name__ == '__main__' :
    ans = [5, 275, 30, 2, None, True, True, 4, 2, None, None, None, None, None, None, False]
    # for i in range (17) :
    #     if i == 5 or i==6 or i==7 or i==8 :
    #         print (lst[i]+'?'+'(True/False)')
    #     else :
    #         print (lst[i]+'?')
    #     n = input()
    #     ans.append(n)
    # #print (ans)n

    _Finger = ans[0]
    _ChannelWidth = ans[1]
    _ChannelLength = ans[2]
    _NPRatio = ans[3]
    _VDD2VSSHeight = ans[4]
    _Dummy = ans[5]
    _SLVT = ans[6]
    _NumSupplyCOX = ans[7]
    _NumSupplyCOY = ans[8]
    _SupplyMet1XWidth = ans[9]
    _SupplyMet1YWidth = ans[10]
    _NumVIAPoly2Met1COX = ans[11]
    _NumVIAPoly2Met1COY = ans[12]
    _NumVIAMet12COX = ans[13]
    _NumVIAMet12COY = ans[14]
    _Gatereverse = ans[15]
    _Bodycontact = False
    #print (_NumVIAMet12COY, _NumVIAMet12COX)
    DesignParameters._Technology = '028nm'

    TransmissionGateObj = _TransmissionGate(_DesignParameter=None, _Name='TransmissionGate')
    #print ("A!!")
    TransmissionGateObj._CalculateTransmissionGate(_Finger=_Finger, _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength, _NPRatio=_NPRatio, _VDD2VSSHeight=_VDD2VSSHeight,
                                   _Dummy=_Dummy, _SLVT=_SLVT, _NumSupplyCOX=_NumSupplyCOX, _NumSupplyCOY = _NumSupplyCOY, _SupplyMet1XWidth= _SupplyMet1XWidth,
                                   _SupplyMet1YWidth=_SupplyMet1YWidth, _NumVIAPoly2Met1COX=_NumVIAPoly2Met1COX, _NumVIAPoly2Met1COY= _NumVIAPoly2Met1COY,
                                   _NumVIAMet12COX=_NumVIAMet12COX, _NumVIAMet12COY=_NumVIAMet12COY, _Gatereverse=_Gatereverse, _Bodycontact = True)


    TransmissionGateObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TransmissionGateObj._DesignParameter)
    _fileName = 'TransmissionGate.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = TransmissionGateObj._CreateGDSStream(TransmissionGateObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')

    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('TransmissionGate.gds', 'rb')
    ftp.storbinary('STOR TransmissionGate.gds', myfile)
    myfile.close()
    ftp.close()

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('TransmissionGate.gds', 'rb')
    ftp.storbinary('STOR TransmissionGate.gds', myfile)
    myfile.close()
    ftp.close()
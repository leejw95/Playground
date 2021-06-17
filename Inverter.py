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
import ftplib
import sys

class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(_Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None, _Dummy = False, _SLVT = False,
                                        _VDD2VSSHeight=None, _SupplyMet1YWidth=None)


    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


    def _CalculateInverter(self, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None, _VDD2VSSHeight = None, _Dummy = False, _SLVT = False,
                                     _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None,
                                    _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
                                ):

            _DRCObj = DRC.DRC()

            _Name = 'Inverter'



            # NMOS Generation
            _NMOSinputs = copy.deepcopy(NMOS._NMOS._ParametersForDesignCalculation)
            _NMOSinputs['_NMOSNumberofGate'] = _Finger
            _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
            _NMOSinputs['_NMOSChannellength'] = _ChannelLength
            _NMOSinputs['_NMOSDummy'] = _Dummy
            _NMOSinputs['_SLVT'] = _SLVT

            self._DesignParameter['_NMOSINV'] = self._SrefElementDeclaration(_DesignObj=NMOS._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['_NMOSINV']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)

            # PMOS Generation
            _PMOSinputs = copy.deepcopy(PMOS._PMOS._ParametersForDesignCalculation)
            _PMOSinputs['_PMOSNumberofGate'] = _Finger
            _PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
            _PMOSinputs['_PMOSChannellength'] = _ChannelLength
            _PMOSinputs['_PMOSDummy'] = _Dummy
            _PMOSinputs['_SLVT'] = _SLVT

            self._DesignParameter['_PMOSINV'] = self._SrefElementDeclaration(_DesignObj=PMOS._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['_PMOSINV']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)

            # VDD Generation

            _NumSupplyCOX = int(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // (
                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
            if _NumSupplyCOX < 2:
                _NumSupplyCOX = 2
            if _NumSupplyCOY == None:
                _NumSupplyCOY = 2

            _Pbodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
            _Pbodyinputs['_NumberOfPbodyCOX'] = _NumSupplyCOX
            _Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCOY

            # _Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
            _Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

            self._DesignParameter['_PbodycontactINV'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None,_Name='Pbodycontactin{}'.format(_Name)))[0]
            self._DesignParameter['_PbodycontactINV']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)



            # VSS Generation
            _Nbodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
            _Nbodyinputs['_NumberOfNbodyCOX'] = _NumSupplyCOX
            _Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCOY

            # _Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
            _Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

            self._DesignParameter['_NbodycontactINV'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None,_Name='Nbodycontactin{}'.format(_Name)))[0]
            self._DesignParameter['_NbodycontactINV']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)


            # VIA Generation for PMOS Output
            _ViaPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
                _ViaPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
                _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                                                             2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
                if _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] == 1 :
                    _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2
            else:
                _ViaPMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumVIAMet12COX
                _ViaPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NumVIAMet12COY

            self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaPMOSMet12)

            _ViaPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
                _ViaPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
                _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] = int(
                    (self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                     2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace)) + 1
                if _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] == 1:
                    _ViaPMOSMet23['_ViaMet22Met3NumberOfCOY'] = 2
            else:
                _ViaPMOSMet12['_ViaMet22Met3NumberOfCOX'] = _NumVIAMet12COX
                _ViaPMOSMet12['_ViaMet22Met3NumberOfCOY'] = _NumVIAMet12COY

            self._DesignParameter['_ViaMet22Met3OnPMOSOutputINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutputINV']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaPMOSMet23)



            # VIA Generation for NMOS Output

            _ViaNMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
                _ViaNMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
                _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                                                             2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
                if _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] == 1 :
                    _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2
            else:
                _ViaNMOSMet12['_ViaMet12Met2NumberOfCOX'] = _NumVIAMet12COX
                _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = _NumVIAMet12COY

            self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaNMOSMet12)

            _ViaNMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            if (_NumVIAPoly2Met1COX == None and _NumVIAPoly2Met1COY == None):
                _ViaNMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
                _ViaNMOSMet23['_ViaMet22Met3NumberOfCOY'] = int(
                    (self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] -
                     2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace)) + 1
                if _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] == 1:
                    _ViaNMOSMet12['_ViaMet12Met2NumberOfCOY'] = 2
            else:
                _ViaNMOSMet12['_ViaMet22Met3NumberOfCOX'] = _NumVIAMet12COX
                _ViaNMOSMet12['_ViaMet22Met3NumberOfCOY'] = _NumVIAMet12COY

            self._DesignParameter['_ViaMet22Met3OnNMOSOutputINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaMet22Met3OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSOutputINV']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaNMOSMet23)

            # VIA Generation for PMOS Gate

            _ViaPMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _TotalLenOfPMOSGate = self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
                                self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0] \
                                + 2 * self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            ## [-1] means the last value of the list or key of dict

            tmp4X_P = int(round(_TotalLenOfPMOSGate // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)))
            if tmp4X_P < 1:
                _NumVIAPoly2Met1COX = 1  ## Default value for # of contact in x axis
            if _NumVIAPoly2Met1COX == None:
                _NumVIAPoly2Met1COX = tmp4X_P
            if _NumVIAPoly2Met1COY == None:
                _NumVIAPoly2Met1COY = 1
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _NumVIAPoly2Met1COX
            _ViaPMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumVIAPoly2Met1COY

            self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnPMOSInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPMOSPoly2Met1)

            del tmp4X_P

            _ViaPMOSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _TotalLenOfPMOSGate = \
            self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                '_XYCoordinates'][-1][0] - \
            self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting'][
                '_XYCoordinates'][0][0] \
            + 2 * self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            ## [-1] means the last value of the list or key of dict

            tmp4X_P = int(round(_TotalLenOfPMOSGate // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
            if tmp4X_P < 1:
                _NumVIAPoly2Met1COX = 1  ## Default value for # of contact in x axis
            _ViaPMOSMet12Met2['_ViaMet12Met2NumberOfCOX'] = tmp4X_P
            _ViaPMOSMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet12Met2OnPMOSInputINV'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,_Name='ViaMet12Met2OnPMOSInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSInputINV']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
                **_ViaPMOSMet12Met2)

            del tmp4X_P

            # VIA Generation for NMOS Gate

            _ViaNMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
            _TotalLenOfNMOSGate = self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
                self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0] + 2 * self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            ## [-1] means the last value of the list or key of dict

            tmp4X = int(round(_TotalLenOfNMOSGate // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)))
            if tmp4X < 1:
                _NumVIAPoly2Met1COX = 1  ## Default value for # of contact in x axis
            if _NumVIAPoly2Met1COX == None:
                _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = tmp4X
            else :
                _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _NumVIAPoly2Met1COX
            if _NumVIAPoly2Met1COY == None:
                _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = 1
            else :
                _ViaNMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _NumVIAPoly2Met1COY

            self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None,_Name='ViaPoly2Met1OnNMOSInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaNMOSPoly2Met1)

            del tmp4X

            _ViaNMOSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _TotalLenOfNMOSGate = \
            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting'][
                '_XYCoordinates'][-1][0] - \
            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting'][
                '_XYCoordinates'][0][0] + 2 * \
            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            ## [-1] means the last value of the list or key of dict

            tmp4X = int(round(_TotalLenOfNMOSGate // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
            if tmp4X < 1:
                _NumVIAPoly2Met1COX = 1  ## Default value for # of contact in x axis

            _ViaNMOSMet12Met2['_ViaMet12Met2NumberOfCOX'] = tmp4X
            _ViaNMOSMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet12Met2OnNMOSInputINV'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                      _Name='ViaMet12Met2OnNMOSInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSInputINV']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaNMOSMet12Met2)

            del tmp4X



            # Coordinate Settings
            _VDD2VSSMinHeight = (self._DesignParameter['_NbodycontactINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
                                (self._DesignParameter['_PbodycontactINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) + \
                                max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                    self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) + \
                                max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                    self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) + \
                                self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                + 5 * _DRCObj._Metal1MinSpace3

            if _VDD2VSSHeight == None:
                _VDD2VSSHeight = _VDD2VSSMinHeight

            else:
                if _VDD2VSSHeight < _VDD2VSSMinHeight:
                    raise NotImplementedError

            _PbodyObj = PbodyContact._PbodyContact()
            _PbodyObj._DesignParameter['_XYCoordinates'] = [[0, 0]]  ## This is the Origin Value of the Inv!!
            _NbodyObj = NbodyContact._NbodyContact()
            _NbodyObj._DesignParameter['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

            self._DesignParameter['_PbodycontactINV']['_XYCoordinates'] = _PbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_NbodycontactINV']['_XYCoordinates'] = _NbodyObj._DesignParameter['_XYCoordinates']

            self._DesignParameter['_NMOSINV']['_XYCoordinates'] = [
                [0, max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                        self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                            '_YWidth']) / 2 +
                 self._DesignParameter['_PbodycontactINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +
                 _DRCObj._Metal1MinSpace3]]

            self._DesignParameter['_PMOSINV']['_XYCoordinates'] = [[0, _VDD2VSSHeight - (
                        max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                            self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter[
                                '_Met1Layer']['_YWidth']) / 2 +
                        self._DesignParameter['_NbodycontactINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                            '_YWidth'] // 2 +
                        _DRCObj._Metal1MinSpace3)]]

            ##VIAS for outputs
            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                        '_XYCoordinates'])):
                tmp.append([self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1]])

            self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_XYCoordinates'] = tmp
            self._DesignParameter['_ViaMet22Met3OnNMOSOutputINV']['_XYCoordinates'] = tmp
            del tmp

            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                        '_XYCoordinates'])):
                tmp.append([self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                            self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                            self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                            self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1]])

            self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_XYCoordinates'] = tmp
            self._DesignParameter['_ViaMet22Met3OnPMOSOutputINV']['_XYCoordinates'] = tmp
            del tmp

            ##Vias For Gate inputs
            if _Finger == 1:
                self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] +
                     max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter[
                             '_Met1Layer']['_YWidth'] / 2) +
                     self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                         '_YWidth'] / 2 +
                     +_DRCObj._Metal1MinSpace3]]

                self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] +
                     max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter[
                             '_Met1Layer']['_YWidth'] / 2) +
                     self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                         '_YWidth'] / 2 +
                     +_DRCObj._Metal1MinSpace3]]

                self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] -
                     (max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                          self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter[
                              '_Met1Layer']['_YWidth'] / 2) +
                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                          '_YWidth'] / 2 +
                      +_DRCObj._Metal1MinSpace3)]]

                self._DesignParameter['_ViaMet12Met2OnPMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] -
                     (max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                          self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter[
                              '_Met1Layer']['_YWidth'] / 2) +
                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                          '_YWidth'] / 2 +
                      +_DRCObj._Metal1MinSpace3)]]

            else:
                self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] +
                     max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter[
                             '_Met1Layer']['_YWidth'] / 2) +
                     self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                         '_YWidth'] / 2 +
                     +_DRCObj._Metal1MinSpace2]]

                self._DesignParameter['_ViaMet12Met2OnNMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] +
                     max(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                         self._DesignParameter['_ViaMet12Met2OnNMOSOutputINV']['_DesignObj']._DesignParameter[
                             '_Met1Layer']['_YWidth'] / 2) +
                     self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                         '_YWidth'] / 2 +
                     +_DRCObj._Metal1MinSpace2]]

                self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] -
                     (max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                          self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter[
                              '_Met1Layer']['_YWidth'] / 2) +
                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                          '_YWidth'] / 2 +
                      +_DRCObj._Metal1MinSpace2)]]

                self._DesignParameter['_ViaMet12Met2OnPMOSInputINV']['_XYCoordinates'] = [
                    [self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                     self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] -
                     (max(self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2,
                          self._DesignParameter['_ViaMet12Met2OnPMOSOutputINV']['_DesignObj']._DesignParameter[
                              '_Met1Layer']['_YWidth'] / 2) +
                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_Met1Layer'][
                          '_YWidth'] / 2 +
                      +_DRCObj._Metal1MinSpace2)]]


            # ########################Vias for Input Metal 1 to metal 2
            # tmp = []
            # if (_Finger) <= 4:
            #     tmp.append([self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][0],
            #                  self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1] +
            #                 self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #     tmp.append([self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][0],
            #                  self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1] -
            #                 self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #     self._DesignParameter['_ViaMet12Met2OnInputINV']['_XYCoordinates'] = tmp
            #
            # elif (_Finger % 2 == 1):
            #     for i in range(1, len(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
            #         tmp.append([self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
            #                          '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                      self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1] +
            #                     self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #         tmp.append([self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
            #                          '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1] -
            #                     self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #         self._DesignParameter['_ViaMet12Met2OnInputINV']['_XYCoordinates'] = tmp
            #
            # elif (_Finger % 2 == 0):
            #     for i in range(1, len(self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) - 1):
            #         tmp.append([self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
            #                          '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                      self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1] +
            #                     self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #         tmp.append([self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
            #                          '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
            #                      self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1] -
            #                     self._DesignParameter['_ViaMet12Met2OnInputINV']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
            #         self._DesignParameter['_ViaMet12Met2OnInputINV']['_XYCoordinates'] = tmp
            #
            # del tmp


            print ('#############      Additional Path Generation for inputs and outputs      #############')
            ## VSS and VDD Routing

            self._DesignParameter['_NMOSSupplyRoutingINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_NMOSSupplyRoutingINV']['_Width'] = \
            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                        '_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + \
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + \
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + \
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                             _PbodyObj._DesignParameter['_XYCoordinates'][0][1]]]
                           # 0 - _PbodyObj._DesignParameter['_Met1Layer']['_YWidth']//2]]
                           )
            self._DesignParameter['_NMOSSupplyRoutingINV']['_XYCoordinates'] = tmp

            self._DesignParameter['_PMOSSupplyRoutingINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_PMOSSupplyRoutingINV']['_Width'] = \
            self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            del tmp

            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'][
                        '_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + \
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + \
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + \
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                             _NbodyObj._DesignParameter['_XYCoordinates'][0][1]]]
                           # 0 - _PbodyObj._DesignParameter['_Met1Layer']['_YWidth']//2]]
                           )
            self._DesignParameter['_PMOSSupplyRoutingINV']['_XYCoordinates'] = tmp

            del tmp

            ##Output Routings

            self._DesignParameter['_OutputRoutingINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_OutputRoutingINV']['_Width'] = min(
                self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
                self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])

            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting'][
                        '_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] +
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] +
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] +
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] +
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1]]])

            self._DesignParameter['_OutputRoutingINV']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_OutputPMOSRoutingXINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_OutputPMOSRoutingXINV']['_Width'] = self._DesignParameter['_OutputRoutingINV']['_Width']
            self._DesignParameter['_OutputPMOSRoutingXINV']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSINV'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_XYCoordinatePMOSOutputRouting'][
                                                                                    '_XYCoordinates'][0][0],
                                                                                self._DesignParameter['_PMOSINV'][
                                                                                    '_XYCoordinates'][0][1]],
                                                                               [self._DesignParameter['_PMOSINV'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_XYCoordinatePMOSOutputRouting'][
                                                                                    '_XYCoordinates'][-1][0],
                                                                                self._DesignParameter['_PMOSINV'][
                                                                                    '_XYCoordinates'][-1][1]]]]

            self._DesignParameter['_OutputNMOSRoutingXINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL3'][0],
                _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_OutputNMOSRoutingXINV']['_Width'] = self._DesignParameter['_OutputRoutingINV']['_Width']
            self._DesignParameter['_OutputNMOSRoutingXINV']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSINV'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_XYCoordinateNMOSOutputRouting'][
                                                                                    '_XYCoordinates'][0][0],
                                                                                self._DesignParameter['_NMOSINV'][
                                                                                    '_XYCoordinates'][0][1]],
                                                                               [self._DesignParameter['_NMOSINV'][
                                                                                    '_DesignObj']._DesignParameter[
                                                                                    '_XYCoordinateNMOSOutputRouting'][
                                                                                    '_XYCoordinates'][-1][0],
                                                                                self._DesignParameter['_NMOSINV'][
                                                                                    '_XYCoordinates'][-1][1]]]]

            ##Input Poly Routings (Vertical & Horizontal)

            self._DesignParameter['_InputNMOSRoutingINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_InputNMOSRoutingINV']['_Width'] = \
            self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][0] +
                             self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                             self._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] +
                             self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]],
                            [self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][0] +
                             self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],
                             self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1] +
                             self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter[
                                 '_POLayer']['_YWidth'] // 2]])

            self._DesignParameter['_InputNMOSRoutingINV']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_InputPMOSRoutingINV'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XYCoordinates=[], _Width=100)
            self._DesignParameter['_InputPMOSRoutingINV']['_Width'] = \
            self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmp = []
            for i in range(0, len(
                    self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][0] +
                             self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                             self._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] +
                             self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]],
                            [self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][0] +
                             self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter[
                                 '_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],
                             self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1] -
                             self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter[
                                 '_POLayer']['_YWidth'] // 2]])

            self._DesignParameter['_InputPMOSRoutingINV']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_InputNMOSRoutingXINV'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100)
            self._DesignParameter['_InputNMOSRoutingXINV']['_Width'] = \
            self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_InputNMOSRoutingXINV']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0],
                                                                               self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1]],
                                                                              [self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0],
                                                                               self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['_InputPMOSRoutingXINV'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],_XYCoordinates=[], _Width=100)
            self._DesignParameter['_InputPMOSRoutingXINV']['_Width'] = self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
            self._DesignParameter['_InputPMOSRoutingXINV']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0],
                                                                               self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1]],
                                                                              [self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0],
                                                                               self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1]]]]


            ### Nwell Routings
            # self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            #     _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            #     _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_NWLayer']['_XWidth'] = (max(
            #     self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'],
            #     self._DesignParameter['_NbodycontactINV']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) \
            #                                                 + _DRCObj._NwMinSpacetoRX * 2) * 2
            # self._DesignParameter['_NWLayer']['_YWidth'] = \
            # self._DesignParameter['_NbodycontactINV']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + \
            # self._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] + \
            # _DRCObj._NwMinSpacetoRX + _DRCObj._NwMinEnclosurePactive * 2 + _DRCObj._Metal1MinSpace3 * 2
            # self._DesignParameter['_NWLayer']['_XYCoordinates'] = [
            #     [self._DesignParameter['_NbodycontactINV']['_XYCoordinates'][0][0],
            #      _VDD2VSSHeight + self._DesignParameter['_NbodycontactINV']['_DesignObj']._DesignParameter['_ODLayer'][
            #          '_YWidth'] / 2
            #      + _DRCObj._PpMinExtensiononPactive - (self._DesignParameter['_NWLayer']['_YWidth'] / 2)]]

            ## Gate Vias Routing
            self._DesignParameter['_InputMet2RoutingINV'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=400)
            self._DesignParameter['_InputMet2RoutingINV']['_Width'] = self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

            tmp = []
            if (_Finger) <= 4:
                tmp.append([[self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1]],
                            [self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][0],
                             self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1]]])
                self._DesignParameter['_InputMet2RoutingINV']['_XYCoordinates'] = tmp

            elif (_Finger % 2 == 1):
                for i in range(1, len(
                        self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                            '_XYCoordinates'])):
                    tmp.append([[self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                     '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                 self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1]],
                                [self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                     '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                 self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1]]])
                    self._DesignParameter['_InputMet2RoutingINV']['_XYCoordinates'] = tmp

            elif (_Finger % 2 == 0):
                for i in range(1, len(
                        self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting'][
                            '_XYCoordinates']) - 1):
                    tmp.append([[self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                     '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                 self._DesignParameter['_ViaPoly2Met1OnNMOSInputINV']['_XYCoordinates'][0][1]],
                                [self._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter[
                                     '_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0],
                                 self._DesignParameter['_ViaPoly2Met1OnPMOSInputINV']['_XYCoordinates'][0][1]]])
                    self._DesignParameter['_InputMet2RoutingINV']['_XYCoordinates'] = tmp

            del tmp

            #### PIN Declaration (Delete under if this is for standard cell)
            # self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
            #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            #     _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
            # self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
            #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            #     _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
            # self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(
            #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            #     _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VIN')
            # self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(
            #     _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            #     _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            #     _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VOUT')
            #
            # self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0, 0]]
            # self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
            # self._DesignParameter['_Inputpin']['_XYCoordinates'] = [
            #     [self._DesignParameter['_InputMet1RoutingINV']['_XYCoordinates'][0][0][0],
            #      self._DesignParameter['_InputMet1RoutingINV']['_XYCoordinates'][0][0][1]]]
            # self._DesignParameter['_Outputpin']['_XYCoordinates'] = [
            #     [self._DesignParameter['_OutputRoutingINV']['_XYCoordinates'][0][0][0],
            #      self._DesignParameter['_OutputRoutingINV']['_XYCoordinates'][0][0][1]]]






if __name__ == '__main__':
    lst = ['_Finger', '_ChannelWidth', '_ChannelLength', '_NPRatio', '_VDD2VSSHeight', '_Dummy', '_SLVT', '_LVT',
           '_HVT', '_NumSupplyCOX'
        , '_NumSupplyCOY', '_SupplyMet1XWidth', '_SupplyMet1YWidth', '_NumVIAPoly2Met1COX', '_NumVIAPoly2Met1COY',
           '_NumVIAMet12COX', '_NumVIAMet12COY']
    #ans = [6, 200, 30, 2, 2000, True, True, False, False, 4, 2, None, None, None, None, None, None]
    ans = []
    for i in range (5) :
        print (lst[i]+'?')
        n = input()
        ans.append(n)


    _Finger = ans[0]
    _ChannelWidth = ans[1]
    _ChannelLength = ans[2]
    _NPRatio = ans[3]
    _VDD2VSSHeight = ans[4]
    _Dummy = True
    _SLVT = True
    _LVT = False
    _HVT = False
    _NumSupplyCOX = None
    _NumSupplyCOY = None
    _SupplyMet1XWidth = None
    _SupplyMet1YWidth = None
    _NumVIAPoly2Met1COX = None
    _NumVIAPoly2Met1COY = None
    _NumVIAMet12COX = None
    _NumVIAMet12COY = None
    # print (_NumVIAMet12COY, _NumVIAMet12COX)
    DesignParameters._Technology = '028nm'

    InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter1')
    # print ("A!!")
    InverterObj._CalculateInverter(_Finger=_Finger, _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength,
                                   _NPRatio=_NPRatio, _VDD2VSSHeight=_VDD2VSSHeight,
                                   _Dummy=_Dummy, _SLVT=_SLVT, _NumSupplyCOX=_NumSupplyCOX,
                                   _NumSupplyCOY=_NumSupplyCOY, _SupplyMet1XWidth=_SupplyMet1XWidth,
                                   _SupplyMet1YWidth=_SupplyMet1YWidth, _NumVIAPoly2Met1COX=_NumVIAPoly2Met1COX,
                                   _NumVIAPoly2Met1COY=_NumVIAPoly2Met1COY,
                                   _NumVIAMet12COX=_NumVIAMet12COX, _NumVIAMet12COY=_NumVIAMet12COY)

    InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=InverterObj._DesignParameter)
    _fileName = 'inverter.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')

    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('inverter.gds', 'rb')
    ftp.storbinary('STOR inverter.gds', myfile)
    myfile.close()
    ftp.close()
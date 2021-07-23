import math
import copy
#
import StickDiagram
import DesignParameters
import DRC
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
from Private import FileManage


class _Inverter(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                           _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                           _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                           _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None,
                                           _NumViaPMOSMet12Met2CoY=None, _NumViaNMOSMet12Met2CoX=None,
                                           _NumViaNMOSMet12Met2CoY=None, _SLVT=None, _SupplyLine=None)

    def __init__(self, _DesignParameter=None, _Name='Inverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter

        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _Finger=None, _ChannelWidth=None, _ChannelLength=None, _NPRatio=None,
                                  _VDD2VSSHeight=None, _Dummy=None, _NumSupplyCoX=None, _NumSupplyCoY=None,
                                  _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _NumViaPoly2Met1CoX=None,
                                  _NumViaPoly2Met1CoY=None, _NumViaPMOSMet12Met2CoX=None, _NumViaPMOSMet12Met2CoY=None,
                                  _NumViaNMOSMet12Met2CoX=None, _NumViaNMOSMet12Met2CoY=None, _SLVT=None, _SupplyLine=None):

        _DRCObj = DRC.DRC()
        _Name = 'Inverter'

        # _NMOS Generation ---------------------------------------------------------------------------------------------
        NMOSparameters = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        NMOSparameters['_NMOSNumberofGate'] = _Finger
        NMOSparameters['_NMOSChannelWidth'] = _ChannelWidth
        NMOSparameters['_NMOSChannellength'] = _ChannelLength
        NMOSparameters['_NMOSDummy'] = _Dummy
        NMOSparameters['_SLVT'] = _SLVT

        self._DesignParameter['_NMOS'] = \
            self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None,
                                                                        _Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**NMOSparameters)
        del NMOSparameters

        # _PMOS Generation ---------------------------------------------------------------------------------------------
        PMOSparameters = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        PMOSparameters['_PMOSNumberofGate'] = _Finger
        PMOSparameters['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
        PMOSparameters['_PMOSChannellength'] = _ChannelLength
        PMOSparameters['_PMOSDummy'] = _Dummy
        PMOSparameters['_SLVT'] = _SLVT

        self._DesignParameter['_PMOS'] = \
            self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None,
                                                                        _Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**PMOSparameters)
        del PMOSparameters

        # VDD Generation -----------------------------------------------------------------------------------------------
        _ContactNum = _NumSupplyCoX
        if _ContactNum == None:
            xWidthOfPMOS = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            _ContactNum = int(xWidthOfPMOS // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        if _ContactNum < 2:
            _ContactNum = 2

        if _NumSupplyCoY == None:
            _NumSupplyCoY = 1

        NbodyParameters = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
        NbodyParameters['_NumberOfNbodyCOX'] = _ContactNum
        NbodyParameters['_NumberOfNbodyCOY'] = _NumSupplyCoY
        NbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        NbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None,
                                                                                                                   _Name='NbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**NbodyParameters)
        del NbodyParameters

        #####################################VSS Generation######################################
        PbodyParameters = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
        PbodyParameters['_NumberOfPbodyCOX'] = _ContactNum
        PbodyParameters['_NumberOfPbodyCOY'] = _NumSupplyCoY
        PbodyParameters['_Met1XWidth'] = _SupplyMet1XWidth
        PbodyParameters['_Met1YWidth'] = _SupplyMet1YWidth

        self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None,
                                                                                                                   _Name='PbodyContactIn{}'.format(_Name)))[0]
        self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**PbodyParameters)
        del PbodyParameters
        del _ContactNum

















    # end of 'def _CalculateDesignParameter' ---------------------------------------------------------------------------


if __name__ == '__main__':
    def main():
        # User-Defined Parameters
        _Finger = 10
        _ChannelWidth = 200
        _ChannelLength = 30
        _NPRatio = 2
        _VDD2VSSHeight = None
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
        _NumViaPMOSMet12Met2CoX = None
        _NumViaPMOSMet12Met2CoY = None
        _NumViaNMOSMet12Met2CoX = None
        _NumViaNMOSMet12Met2CoY = None
        _NumVIAMet12COX = None
        _NumVIAMet12COY = None
        _SupplyLine = True

        # Generate Inverter Layout Object
        InverterObj = _Inverter(_DesignParameter=None, _Name='Inverter')
        InverterObj._CalculateDesignParameter(_NPRatio=_NPRatio, _Dummy=_Dummy, _SLVT=_SLVT, _Finger=_Finger,
                                              _ChannelWidth=_ChannelWidth, _ChannelLength=_ChannelLength,
                                              _VDD2VSSHeight=_VDD2VSSHeight, _SupplyLine=_SupplyLine,
                                              _NumSupplyCoX=_NumSupplyCOX, _NumSupplyCoY=_NumSupplyCOY,
                                              _SupplyMet1XWidth=_SupplyMet1XWidth, _SupplyMet1YWidth=_SupplyMet1YWidth,
                                              _NumViaPoly2Met1CoX=_NumVIAPoly2Met1COX,
                                              _NumViaPoly2Met1CoY=_NumVIAPoly2Met1COY,
                                              _NumViaPMOSMet12Met2CoX=_NumViaPMOSMet12Met2CoX,
                                              _NumViaPMOSMet12Met2CoY=_NumViaPMOSMet12Met2CoY,
                                              _NumViaNMOSMet12Met2CoX=_NumViaNMOSMet12Met2CoX,
                                              _NumViaNMOSMet12Met2CoY=_NumViaNMOSMet12Met2CoY,
                                              )

        InverterObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=InverterObj._DesignParameter)
        _fileName = 'Inverter0723.gds'
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = InverterObj._CreateGDSStream(InverterObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print ('###############      Sending to FTP Server...      ##################')
        FileManage.Upload2FTP(_fileName=_fileName)

        print ('###############      Finished      ##################') # Need to get project name(inverter_iksu2.py)

    # end of 'def main():' ---------------------------------------------------------------------------------------------

    main()

import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaMet12Met2
import ViaMet22Met3
import ViaPoly2Met1

import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

##lol
class _FLIPFLOP(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
      
                                     
                                     _NumberOfGate1=None, _ChannelWidth1=None, _ChannelLength1=None, _PNChannelRatio1=None,
                                     _NumberOfGate2=None, _ChannelWidth2=None, _ChannelLength2=None, _PNChannelRatio2=None,
                                     _NumberOfGate3=None, _ChannelWidth3=None, _ChannelLength3=None, _PNChannelRatio3=None,
                                     _NumberOfGate4=None, _ChannelWidth4=None, _ChannelLength4=None, _PNChannelRatio4=None,
                                     _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                     _FFSupplyMetal1XWidth=None, _FFSupplyMetal1YWidth=None,

                                     _FFVdd2VssHeight=None,  _DistanceBtwSupplyCenter2MOSEdge=None, _FFEdgeBtwNWandPW=None, _XYadjust=None,
                                     
                                     
                                     _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfPMOSOutputViaCOY=None,
                                     _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,
                                     _NumberOfPMOSOutputLeftViaCOY=None, _NumberOfNMOSOutputLeftViaCOY=None,
                                     _NumberOfPMOSOutputRightViaCOY=None, _NumberOfNMOSOutputRightViaCOY=None,
                                     
                                     _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption=None,
                                     _MOS12MOS2spacebias=None, _MOS22MOS3spacebias=None, _MOS32MOS4spacebias=None,
                                     _YBiasOfOuputViaMet12Met2OnPMOSLeft=None, _YBiasOfOuputViaMet12Met2OnNMOSLeft=None,_YBiasOfOuputViaMet12Met2OnPMOSRight=None, _YBiasOfOuputViaMet12Met2OnNMOSRight=None,

                                     _YbiasforNMOSconnectionVia=None, _YbiasforPMOSconnectionVia=None,
                                     
                                     # _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None,
                                     # _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,
                                     # _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None,
                                     # _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None, 
                                     
                                     
                                     _BiasDictforViaPoly2Met1OnGate = {
                                     '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None, '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,
                                     '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None, '_XbiasNMOS4GateVia':None, '_YbiasNMOS4GateVia':None,
                                     '_XbiasPMOS1GateVia':None, '_YbiasPMOS1GateVia':None, '_XbiasPMOS2GateVia':None, '_YbiasPMOS2GateVia':None,
                                     '_XbiasPMOS3GateVia':None, '_YbiasPMOS3GateVia':None, '_XbiasPMOS4GateVia':None, '_YbiasPMOS4GateVia':None,
                                     },

                                     _XbiasPMOS3GateMet12Met2Via = None, _XbiasNMOS3GateMet12Met2Via = None, _NumberOfMOS3GateMetViaCOX=None,

                                    _OutputRoutingOnNMOSLeftWidth=None,_OutputRoutingOnPMOSLeftWidth=None,
                                    _OutputRoutingNEWidth=None,_OutputRoutingEWidth=None,_OutputRoutingSEWidth=None,

                                     # _YCoordinateOfViaMet12Met2OnPMOS2Gate=None,_YCoordinateOfViaMet12Met2OnPMOS3Gate=None,

                                     _NMOS1DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS2DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS3DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS4DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _PMOS1DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS2DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS3DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS4DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _NbodyDesignCalculationParameters=copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation),
                                     _PbodyDesignCalculationParameters=copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSconnectionParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSconnectionParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnPMOSconnectionParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnNMOSconnectionParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS1GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS2GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS3GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS4GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnMOS3GateParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSOutputLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSOutputRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),

                                     _Dummy=False)

    def __init__(self, _DesignParameter=None, _Name='C2FlipFlop'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(
                                                   
                                                    _NMOS1 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS1In{}'.format(_Name)))[0],
                                                    _PMOS1 = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS1In{}'.format(_Name)))[0],
                                                    _NMOS2 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS2In{}'.format(_Name)))[0],
                                                    _PMOS2 = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS2In{}'.format(_Name)))[0],
                                                    _NMOS3 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS3In{}'.format(_Name)))[0],
                                                    _PMOS3 = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS3In{}'.format(_Name)))[0],
                                                    _NMOS4 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS4In{}'.format(_Name)))[0],
                                                    _PMOS4 = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS4In{}'.format(_Name)))[0],
                                                    _PbodyContact=self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0],
                                                    _NbodyContact=self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnPMOS1connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOS1connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOS2connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOS2connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOS3connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOS3connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOS4connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOS4connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOS1connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS1connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOS2connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS2connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOS3connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS3connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOS4connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS4connectionIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnPMOS1connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOS1connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOS2connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOS2connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOS3connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOS3connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOS4connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOS4connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOS1connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOS1connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOS2connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOS2connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOS3connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOS3connectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOS4connection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOS4connectionIn{}'.format(_Name)))[0],
                                                    
                                                    
                                                    _ViaPoly2Met1OnNMOS1Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOS1GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnPMOS1Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOS1GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnNMOS2Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOS2GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnPMOS2Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOS2GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnNMOS3Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOS3GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnPMOS3Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOS3GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnNMOS4Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOS4GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnPMOS4Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOS4GateIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOS3Gate = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS3GateIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOS3Gate = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOS3GateIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnNMOSOutputLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutputRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutputLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutputRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputRightIn{}'.format(_Name)))[0],

                                                    _NMOSConnectionRoutingLeft = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _NMOSConnectionRoutingRight = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _PMOSConnectionRoutingLeft = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _PMOSConnectionRoutingRight = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingOnNMOSLeft = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingOnPMOSLeft = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingOnNMOSRight = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingOnPMOSRight = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _PMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _NMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    
                                                    # _OutputRouting2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _InputDataRouting = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingNE = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingE = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRoutingSE = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    # _DataBarRouting1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    # _DataBarRouting2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),

                                                    # _ViaPoly2Met1=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1In{}'.format(_Name)))[0],
                                                    # # _ViaMet12Met2OnNMOS=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSIn{}'.format(_Name)))[0],
                                                    # # _ViaMet12Met2OnPMOS=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSIn{}'.format(_Name)))[0],
                                                    _AdditionalMet1OnNMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnNMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnNMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnNMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnPMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnPMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnPMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnPMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    
                                                    _AdditionalMet1OnNMOS2_forOutputVia=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),                                                    
                                                    _AdditionalMet1OnPMOS2_forOutputVia=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnNMOS4_forOutputVia=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    _AdditionalMet1OnPMOS4_forOutputVia=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    
                                                    _AdditionalMet2OnNMOS_for_void=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet2OnPMOS_for_void=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
													
                                                    _AdditionalPolyOnPMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
													_AdditionalPolyOnNMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    
                                                    _AdditionalMet1PathForPMOS2Output = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1PathForNMOS2Output = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1PathForPMOS4Output = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1PathForNMOS4Output = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),



                                                    _NWell=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    
                                                    _NMOS12NMOS2Met1Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PMOS12PMOS2Met1Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _NMOS32NMOS4Met1Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PMOS32PMOS4Met1Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),

                                                    
                                                    
                                                    _GateRoutingOnNMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),

                                                    _GateRoutingOnPMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    
                                                    _AdditionalGatePolyOn_NMOS1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_NMOS2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_NMOS3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_NMOS4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_InvNMOS = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_PMOS1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_PMOS2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_PMOS3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_PMOS4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _AdditionalGatePolyOn_InvPMOS = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 
    
                                     _NumberOfGate1=None, _ChannelWidth1=None, _ChannelLength1=None, _PNChannelRatio1=None,
                                     _NumberOfGate2=None, _ChannelWidth2=None, _ChannelLength2=None, _PNChannelRatio2=None,
                                     _NumberOfGate3=None, _ChannelWidth3=None, _ChannelLength3=None, _PNChannelRatio3=None,
                                     _NumberOfGate4=None, _ChannelWidth4=None, _ChannelLength4=None, _PNChannelRatio4=None,
                                     _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                     _FFSupplyMetal1XWidth=None, _FFSupplyMetal1YWidth=None,

                                     _FFVdd2VssHeight=None,  _DistanceBtwSupplyCenter2MOSEdge=None, _FFEdgeBtwNWandPW=None,_XYadjust=None,

                                     
                                     
                                     _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfPMOSOutputViaCOY=None,
                                     _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,
                                     _NumberOfPMOSOutputLeftViaCOY=None, _NumberOfNMOSOutputLeftViaCOY=None,
                                     _NumberOfPMOSOutputRightViaCOY=None, _NumberOfNMOSOutputRightViaCOY=None,
                                     
                                     _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption=None,
                                     _MOS12MOS2spacebias=None, _MOS22MOS3spacebias=None, _MOS32MOS4spacebias=None,
                                     _YBiasOfOuputViaMet12Met2OnPMOSLeft=None, _YBiasOfOuputViaMet12Met2OnNMOSLeft=None,_YBiasOfOuputViaMet12Met2OnPMOSRight=None, _YBiasOfOuputViaMet12Met2OnNMOSRight=None,                                     
                                     # _YCoordinateOfViaMet12Met2OnPMOS2Gate=None,_YCoordinateOfViaMet12Met2OnPMOS3Gate=None,
                                     # _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None, _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None, _NumberOfPMOSConnectionCOY=None,
                                     # _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,

                                  _YbiasforNMOSconnectionVia=None, _YbiasforPMOSconnectionVia=None,
                                  _BiasDictforViaPoly2Met1OnGate={
                                      '_XbiasNMOS1GateVia': None, '_YbiasNMOS1GateVia': None,
                                      '_XbiasNMOS2GateVia': None, '_YbiasNMOS2GateVia': None,
                                      '_XbiasNMOS3GateVia': None, '_YbiasNMOS3GateVia': None,
                                      '_XbiasNMOS4GateVia': None, '_YbiasNMOS4GateVia': None,
                                      '_XbiasPMOS1GateVia': None, '_YbiasPMOS1GateVia': None,
                                      '_XbiasPMOS2GateVia': None, '_YbiasPMOS2GateVia': None,
                                      '_XbiasPMOS3GateVia': None, '_YbiasPMOS3GateVia': None,
                                      '_XbiasPMOS4GateVia': None, '_YbiasPMOS4GateVia': None,
                                  },

                                    _XbiasPMOS3GateMet12Met2Via = None, _XbiasNMOS3GateMet12Met2Via = None, _NumberOfMOS3GateMetViaCOX=None,
                                     # _MOS12MOS2spacebias=None, _MOS22InvMOSspacebias=None, _InvMOS2MOS3spacebias=None, _MOS32MOS4spacebias=None, 
                                     _OutputRoutingOnNMOSLeftWidth=None,_OutputRoutingOnPMOSLeftWidth=None,
                                    _OutputRoutingNEWidth=None,_OutputRoutingEWidth=None,_OutputRoutingSEWidth=None,


                                     
                                     _NMOS1DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS2DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS3DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS4DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _PMOS1DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS2DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS3DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _PMOS4DesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                     _NbodyDesignCalculationParameters=copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation),
                                     _PbodyDesignCalculationParameters=copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSconnectionParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSconnectionParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnPMOSconnectionParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnNMOSconnectionParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS1GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS2GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS3GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS4GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnMOS3GateParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSOutputLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnNMOSOutputRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),

                                     _Dummy=False
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  FlipFlop Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj=DRC.DRC()

        while True:
            # #####################SUBSET ELEMENTS GENERATION#########################

            # NMOS1 GENERATION
            _NMOS1DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate1
            _NMOS1DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth1
            _NMOS1DesignCalculationParameters['_NMOSChannellength']=_ChannelLength1
            _NMOS1DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS1DesignCalculationParameters)

            # PMOS1 GENERATION
            _PMOS1DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate1
            _PMOS1DesignCalculationParameters['_PMOSChannelWidth']=round(_ChannelWidth1 * _PNChannelRatio1)
            _PMOS1DesignCalculationParameters['_PMOSChannellength']=_ChannelLength1
            _PMOS1DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS1DesignCalculationParameters)

            # NMOS2 GENERATION
            _NMOS2DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate2
            _NMOS2DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth2
            _NMOS2DesignCalculationParameters['_NMOSChannellength']=_ChannelLength2
            _NMOS2DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS2DesignCalculationParameters)

            # PMOS2 GENERATION
            _PMOS2DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate2
            _PMOS2DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth2 * _PNChannelRatio2)
            _PMOS2DesignCalculationParameters['_PMOSChannellength']=_ChannelLength2
            _PMOS2DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS2DesignCalculationParameters)

            # NMOS3 GENERATION
            _NMOS3DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate3
            _NMOS3DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth3
            _NMOS3DesignCalculationParameters['_NMOSChannellength']=_ChannelLength3
            _NMOS3DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS3DesignCalculationParameters)

            # PMOS3 GENERATION
            _PMOS3DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate3
            _PMOS3DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth3 * _PNChannelRatio3)
            _PMOS3DesignCalculationParameters['_PMOSChannellength']=_ChannelLength3
            _PMOS3DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS3DesignCalculationParameters)

            # NMOS4 GENERATION
            _NMOS4DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate4
            _NMOS4DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth4
            _NMOS4DesignCalculationParameters['_NMOSChannellength']=_ChannelLength4
            _NMOS4DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS4DesignCalculationParameters)

            # PMOS4 GENERATION
            _PMOS4DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate4
            _PMOS4DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth4 * _PNChannelRatio4)
            _PMOS4DesignCalculationParameters['_PMOSChannellength']=_ChannelLength4
            _PMOS4DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS4DesignCalculationParameters)


            # VSS GENERATION
            if _NumberOfSupplyCOY == None :		# Default value is 1
                _NumberOfSupplyCOY = 1
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOY']=_NumberOfSupplyCOY
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']=_NumberOfSupplyCOY
            
            _PbodyDesignCalculationParameters['_Met1XWidth']=_FFSupplyMetal1XWidth
            _PbodyDesignCalculationParameters['_Met1YWidth']=_FFSupplyMetal1YWidth
            
            _NbodyDesignCalculationParameters['_Met1XWidth']=_FFSupplyMetal1XWidth
            _NbodyDesignCalculationParameters['_Met1YWidth']=_FFSupplyMetal1YWidth
            
            _tmpPbodyObj = PbodyContact._PbodyContact()
            _tmpPbodyObj._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOX=5, _NumberOfPbodyCOY=_PbodyDesignCalculationParameters['_NumberOfPbodyCOY'], _Met1YWidth =_FFSupplyMetal1YWidth )
            _tmpNbodyObj = NbodyContact._NbodyContact()
            _tmpNbodyObj._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOX=5, _NumberOfNbodyCOY=_NbodyDesignCalculationParameters['_NumberOfNbodyCOY'], _Met1YWidth =_FFSupplyMetal1YWidth )

            
            # if _NumberOfSupplyCOX == None :		
                # _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=int(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']+self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']+self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']+
                                                                            # self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _NbodyDesignCalculationParameters['_NumberOfNbodyCOY']==1 \
                    # else int(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2))
                # _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=int(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 \
                    # else int(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2))
            # else :
                # _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX
                # _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX

            
            # _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX
            # _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']=_NumberOfSupplyCOY
            # self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)

            # VDD GENERATION
            
            # _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX
            # _NbodyDesignCalculationParameters['_NumberOfNbodyCOY']=_NumberOfSupplyCOY
            # self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)


            # VIA GENERATION for PMOS Connection
            if _NumberOfPMOSConnectionViaCOY is None :
                _NumberOfPMOSConnectionViaCOY = 2
            if _NumberOfPMOSOutputViaCOY is None :
                _NumberOfPMOSOutputViaCOY = 2
            
            _ViaMet12Met2OnPMOSconnectionParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnPMOSconnectionParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfPMOSConnectionViaCOY
            _ViaMet22Met3OnPMOSconnectionParameters['_ViaMet22Met3NumberOfCOX']=1
            _ViaMet22Met3OnPMOSconnectionParameters['_ViaMet22Met3NumberOfCOY']=_NumberOfPMOSConnectionViaCOY
           
            self._DesignParameter['_ViaMet12Met2OnPMOS1connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOS3connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSconnectionParameters)
            
            self._DesignParameter['_ViaMet22Met3OnPMOS1connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnPMOS2connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnPMOS3connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnPMOS4connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnPMOSconnectionParameters)

            
            # # VIA GENERATION for NMOS Connection
            if _NumberOfNMOSConnectionViaCOY == None :
                _NumberOfNMOSConnectionViaCOY = 2
           
            _ViaMet12Met2OnNMOSconnectionParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnNMOSconnectionParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfNMOSConnectionViaCOY
            _ViaMet22Met3OnNMOSconnectionParameters['_ViaMet22Met3NumberOfCOX']=1
            _ViaMet22Met3OnNMOSconnectionParameters['_ViaMet22Met3NumberOfCOY']=_NumberOfNMOSConnectionViaCOY
           
            self._DesignParameter['_ViaMet12Met2OnNMOS1connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnNMOS3connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnNMOS1connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnNMOS2connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnNMOS3connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnNMOS4connection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnNMOSconnectionParameters)

            
            # # VIA GENERATION for GATE (POLY_M1)
            if _NumberOfMOS1GateViaCOX is None:
                _NumberOfMOS1GateViaCOX = 2
                if len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS1GateViaCOX= len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS1GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS1GateViaCOX
            _ViaPoly2Met1OnMOS1GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnNMOS1Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS1GateParameters)
            self._DesignParameter['_ViaPoly2Met1OnPMOS1Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS1GateParameters)
            
            if _NumberOfMOS2GateViaCOX is None:
                _NumberOfMOS2GateViaCOX = 2
                if len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS2GateViaCOX= len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS2GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS2GateViaCOX
            _ViaPoly2Met1OnMOS2GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS2GateParameters)
            self._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS2GateParameters)
            
            if _NumberOfMOS3GateViaCOX is None:
                _NumberOfMOS3GateViaCOX = 2
                if len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS3GateViaCOX= len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS3GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS3GateViaCOX
            _ViaPoly2Met1OnMOS3GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnNMOS3Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS3GateParameters)
            self._DesignParameter['_ViaPoly2Met1OnPMOS3Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS3GateParameters)
            
            if _NumberOfMOS4GateViaCOX is None:
                _NumberOfMOS4GateViaCOX = 2
                if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS4GateViaCOX= len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS4GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS4GateViaCOX
            _ViaPoly2Met1OnMOS4GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS4GateParameters)
            self._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS4GateParameters)
            
            
            # # VIA GENERATION for GATE (M1_M2)
            if _NumberOfMOS3GateMetViaCOX is None:
                _NumberOfMOS3GateMetViaCOX =2
            _ViaMet12Met2OnMOS3GateParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfMOS3GateMetViaCOX
            _ViaMet12Met2OnMOS3GateParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaMet12Met2OnMOS3GateParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaMet12Met2OnMOS3GateParameters)
            
            # # VIA GENERATION for OUTPUT Left (first stage)
            if _NumberOfPMOSOutputLeftViaCOY is None:
                _NumberOfPMOSOutputLeftViaCOY = 2
            if _NumberOfNMOSOutputLeftViaCOY is None:
                _NumberOfNMOSOutputLeftViaCOY = 2
                
            _ViaMet12Met2OnPMOSOutputLeftParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnNMOSOutputLeftParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnPMOSOutputLeftParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfPMOSOutputLeftViaCOY
            _ViaMet12Met2OnNMOSOutputLeftParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfNMOSOutputLeftViaCOY
            self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSOutputLeftParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSOutputLeftParameters)
            
            
            # # VIA GENERATION for OUTPUT Right (Final stage)
            if _NumberOfPMOSOutputRightViaCOY is None:
                _NumberOfPMOSOutputRightViaCOY = 2
            if _NumberOfNMOSOutputRightViaCOY is None:
                _NumberOfNMOSOutputRightViaCOY = 2
                
            _ViaMet12Met2OnPMOSOutputRightParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnNMOSOutputRightParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnPMOSOutputRightParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfPMOSOutputRightViaCOY
            _ViaMet12Met2OnNMOSOutputRightParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfNMOSOutputRightViaCOY
            self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSOutputRightParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSOutputRightParameters)
            

            
            # )#####################COORDINATION SETTING#########################
            if _DistanceBtwSupplyCenter2MOSEdge == None:
                _DistanceBtwSupplyCenter2MOSEdge = (float) (_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']*1/2)  
            
            
            if _YbiasforEdgeBtwNWandPW==None and _YbiasforHeight==None :        #For Height Calc
                _YbiasforEdgeBtwNWandPW = 0
                _YbiasforHeight = 0

            if _HeightCalOption == 'ON':
                min_height = 0
                min_NWPW = 0
                
                for i in range(1,5) :
                    NMOS = '_NMOS' + str(i)
                    PMOS = '_PMOS' + str(i)
                    height = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + 2 * _DistanceBtwSupplyCenter2MOSEdge
                    NWPW = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] +  _DistanceBtwSupplyCenter2MOSEdge
                    if min_height == 0 or min_height > height :
                        min_height = height
                    if min_NWPW < NWPW:
                        min_NWPW = NWPW
                _FFVdd2VssHeight = min_height + _YbiasforHeight
                _FFEdgeBtwNWandPW = min_NWPW + _YbiasforEdgeBtwNWandPW
            
            _tmpPbodyObj._DesignParameter['_XYCoordinates']=[[0,0]]
            _tmpNbodyObj._DesignParameter['_XYCoordinates']=[[0,_FFVdd2VssHeight]]

            # NMOS, PMOS Coordinate Setting
            if _MOS12MOS2spacebias is None:
                _MOS12MOS2spacebias = 0
            if _MOS22MOS3spacebias is None :
                _MOS22MOS3spacebias = 0
            if _MOS32MOS4spacebias is None :
                _MOS32MOS4spacebias = 0
            if _XYadjust is None :
                _XYadjust = 0

            # if _Dummy ==False:
            MOS1spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS2spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS3spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS4spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            
            
            if _Dummy is True:
                MOS1PODummy = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS2PODummy = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS3PODummy = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS4PODummy = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]       
            
            
            tempX1 = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + max(MOS2spaceDRC,MOS3spaceDRC) + _MOS22MOS3spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = MOS2PODummy + MOS3PODummy + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS22MOS3spacebias
            tempX = max(tempX1,tempX2)
            
            tempX_MOS2 = int(tempX/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tempX_MOS3 = round(tempX/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            
            self._DesignParameter['_NMOS2']['_XYCoordinates']=[[-tempX_MOS2+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS2']['_XYCoordinates']=[[-tempX_MOS2+_XYadjust,(float)(_FFVdd2VssHeight-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_NMOS3']['_XYCoordinates']=[[tempX_MOS3+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS3']['_XYCoordinates']=[[tempX_MOS3+_XYadjust,(float)(_FFVdd2VssHeight-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]
            
            
            tempX1 = tempX_MOS2 +  self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 +max(MOS1spaceDRC,MOS2spaceDRC) + _MOS12MOS2spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = tempX_MOS2 + MOS1PODummy + MOS2PODummy + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS12MOS2spacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS1']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS1']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_FFVdd2VssHeight-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            tempX1 = tempX_MOS3 +  self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 +max(MOS3spaceDRC,MOS4spaceDRC) +_MOS32MOS4spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = tempX_MOS3 + MOS3PODummy + MOS4PODummy + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS32MOS4spacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS4']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS4']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_FFVdd2VssHeight-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            # )################################ MOS CONNECTION ################################
            # )######PUT VIA FOR CONNECTION (M1_M2, M2_M3)		
            
            for i in range (1,5):
                tmpP = []
                tmpN = []
                PMOS = '_PMOS' + str(i)
                NMOS = '_NMOS' + str(i)
                VIAP_M12M2 = '_ViaMet12Met2OnPMOS' + str(i) + 'connection'
                VIAN_M12M2 = '_ViaMet12Met2OnNMOS' + str(i) + 'connection'
                VIAP_M22M3 = '_ViaMet22Met3OnPMOS' + str(i) + 'connection'
                VIAN_M22M3 = '_ViaMet22Met3OnNMOS' + str(i) + 'connection'
                

                if _YbiasforNMOSconnectionVia is None:
                    _YbiasforNMOSconnectionVia = 0
                if _YbiasforPMOSconnectionVia is None:
                    _YbiasforPMOSconnectionVia = 0

                YcalibP = float(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter[VIAP_M12M2]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2
                YcalibN = -float(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter[VIAN_M12M2]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2

                if i is 1 or i is 3:
                    for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                        tmpP.append( [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                        tmpP[j][1] += YcalibP + _YbiasforPMOSconnectionVia
                        tmpN.append( [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                        tmpN[j][1] += YcalibN + _YbiasforNMOSconnectionVia
                elif i is 2 or i is 4:
                    for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                        tmpP.append( [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                        tmpP[j][1] += YcalibP + _YbiasforPMOSconnectionVia
                        tmpN.append( [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                        tmpN[j][1] += YcalibN + _YbiasforNMOSconnectionVia

                self._DesignParameter[VIAP_M12M2]['_XYCoordinates'] = tmpP
                self._DesignParameter[VIAP_M22M3]['_XYCoordinates'] = tmpP

                self._DesignParameter[VIAN_M12M2]['_XYCoordinates'] = tmpN
                self._DesignParameter[VIAN_M22M3]['_XYCoordinates'] = tmpN

            # )######CONNECTION ROUTING  (Metal3)
            
            self._DesignParameter['_NMOSConnectionRoutingLeft']['_Width']= self._DesignParameter['_ViaMet22Met3OnNMOS1connection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_PMOSConnectionRoutingLeft']['_Width']= self._DesignParameter['_ViaMet22Met3OnPMOS1connection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_NMOSConnectionRoutingLeft']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnNMOS1connection']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnNMOS2connection']['_XYCoordinates'][-1]]]
            self._DesignParameter['_PMOSConnectionRoutingLeft']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnPMOS1connection']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnPMOS2connection']['_XYCoordinates'][-1]]]
            
            self._DesignParameter['_NMOSConnectionRoutingRight']['_Width']= self._DesignParameter['_ViaMet22Met3OnNMOS3connection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_PMOSConnectionRoutingRight']['_Width']= self._DesignParameter['_ViaMet22Met3OnPMOS3connection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_NMOSConnectionRoutingRight']['_XYCoordinates'] = []
            self._DesignParameter['_NMOSConnectionRoutingRight']['_XYCoordinates'].append([ self._DesignParameter['_ViaMet22Met3OnNMOS3connection']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnNMOS4connection']['_XYCoordinates'][-1]])
            self._DesignParameter['_PMOSConnectionRoutingRight']['_XYCoordinates'] = []
            self._DesignParameter['_PMOSConnectionRoutingRight']['_XYCoordinates'].append([ self._DesignParameter['_ViaMet22Met3OnPMOS3connection']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnPMOS4connection']['_XYCoordinates'][-1]])


            # )################################ Output Routing ################################
            # )######PUT VIA FOR OUTPUT left (First stage)
            if _YBiasOfOuputViaMet12Met2OnPMOSLeft == None :
                _YBiasOfOuputViaMet12Met2OnPMOSLeft = 0
            if _YBiasOfOuputViaMet12Met2OnNMOSLeft == None :
                _YBiasOfOuputViaMet12Met2OnNMOSLeft = 0   
            tmpP = []
            YbiasP = -float(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasOfOuputViaMet12Met2OnPMOSLeft
            for i in range(0,len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmpP.append( [a+b for a, b in zip(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_PMOS2']['_XYCoordinates'][0]) ])
                tmpP[i][1] += YbiasP
            
            tmpN = []
            YbiasN = float(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasOfOuputViaMet12Met2OnNMOSLeft
            for i in range(0,len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmpN.append( [a+b for a, b in zip(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_NMOS2']['_XYCoordinates'][0]) ])
                tmpN[i][1] += YbiasN
            
            self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_XYCoordinates'] = tmpP
            self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_XYCoordinates'] = tmpN


            # )###### OUTPUT ROUTING LEFT 1 (M3) - Horizontal
            if _OutputRoutingOnNMOSLeftWidth is None:
                _OutputRoutingOnNMOSLeftWidth = _DRCObj._MetalxMinWidth
            if _OutputRoutingOnPMOSLeftWidth is None:
                _OutputRoutingOnPMOSLeftWidth = _DRCObj._MetalxMinWidth
            
            tmpN = []
            tmpP = []
            self._DesignParameter['_OutputRoutingOnNMOSLeft']['_Width'] = _OutputRoutingOnNMOSLeftWidth
            self._DesignParameter['_OutputRoutingOnPMOSLeft']['_Width'] = _OutputRoutingOnPMOSLeftWidth
            
            tmpN = [[copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_XYCoordinates'][0]), copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_XYCoordinates'][-1]) ]]
            tmpN[0][0][1] += float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnNMOSLeft']['_Width'])/2
            tmpN[0][1][1] += float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnNMOSLeft']['_Width'])/2
            tmpP = [[copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_XYCoordinates'][0]), copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_XYCoordinates'][-1]) ]]
            tmpP[0][0][1] -= float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnPMOSLeft']['_Width'])/2
            tmpP[0][1][1] -= float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnPMOSLeft']['_Width'])/2
            self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'] = tmpN
            self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'] = tmpP
            
            
            # )######PUT VIA FOR OUTPUT Right (Final stage)
            if _YBiasOfOuputViaMet12Met2OnPMOSRight == None :
                _YBiasOfOuputViaMet12Met2OnPMOSRight = 0
            if _YBiasOfOuputViaMet12Met2OnNMOSRight == None :
                _YBiasOfOuputViaMet12Met2OnNMOSRight = 0   
            tmpP = []
            # if len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates']) is not 2:
            YbiasP = -float(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasOfOuputViaMet12Met2OnPMOSRight
            for i in range(0,len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmpP.append( [a+b for a, b in zip(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_PMOS4']['_XYCoordinates'][0]) ])
                tmpP[i][1] += YbiasP
            
            tmpN = []
            # if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is not 2:
            YbiasN = float(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasOfOuputViaMet12Met2OnNMOSRight
            for i in range(0,len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmpN.append( [a+b for a, b in zip(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_NMOS4']['_XYCoordinates'][0]) ])
                tmpN[i][1] += YbiasN
            
            self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'] = tmpP
            self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'] = tmpN
            # )###### OUTPUT ROUTING Right (Final stage, connection) 
            tmpN = []
            tmpP = []
            self._DesignParameter['_OutputRoutingOnNMOSRight']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_OutputRoutingOnPMOSRight']['_Width'] = _DRCObj._MetalxMinWidth
            

            # if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) is not 1:
            tmpN = [[copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][0]), copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-1]) ]]
            tmpN[0][0][1] += float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnNMOSRight']['_Width'])/2
            tmpN[0][1][1] += float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnNMOSRight']['_Width'])/2
            tmpP = [[copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][0]), copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][-1]) ]]
            tmpP[0][0][1] -= float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnPMOSRight']['_Width'])/2
            tmpP[0][1][1] -= float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']-self._DesignParameter['_OutputRoutingOnPMOSRight']['_Width'])/2
            self._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'] = tmpN
            self._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'] = tmpP

            # )################################ VSS METAL1 ROUTING )################################
            tmp = []
            for i in range(0,len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_NMOS1']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_NMOS3']['_XYCoordinates'][0])] ])

            self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates']=tmp
            self._DesignParameter['_NMOSSupplyRouting']['_Width']= self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']



            # )################################ VDD METAL1 ROUTING )################################
            tmp = []
            for i in range(0,len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,_FFVdd2VssHeight + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_PMOS1']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,_FFVdd2VssHeight + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_PMOS3']['_XYCoordinates'][0])] ])

            self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates']=tmp
            self._DesignParameter['_PMOSSupplyRouting']['_Width']= self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']





            #NEW GATE ROUTING
            for i in range (1,5):
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                Poly2Met1ViaN = '_ViaPoly2Met1OnNMOS' + str(i) + 'Gate' 
                Poly2Met1ViaP = '_ViaPoly2Met1OnPMOS' + str(i) + 'Gate' 
                NGateRouting = '_GateRoutingOnNMOS' + str(i)
                PGateRouting = '_GateRoutingOnPMOS' + str(i)
                Nbias = '_YbiasNMOS' + str(i) + 'GateVia'
                Pbias = '_YbiasPMOS' + str(i) + 'GateVia'
                VIAN = '_ViaMet12Met2OnNMOS' + str(i) + 'connection'
                VIAP = '_ViaMet12Met2OnPMOS' + str(i) + 'connection'
        
                if _BiasDictforViaPoly2Met1OnGate[Nbias] is None:
                    _BiasDictforViaPoly2Met1OnGate[Nbias] = 0
                if _BiasDictforViaPoly2Met1OnGate[Pbias] is None:
                    _BiasDictforViaPoly2Met1OnGate[Pbias] = 0
        
                N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS = _DRCObj.DRCMETAL1MinSpace(_Width=self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] , _ParallelLength=self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                N_tmpDRCMet1MinSpaceByViaPoly2Met1 = _DRCObj.DRCMETAL1MinSpace(_Width= self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength= self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                N2_tmpDRCMet2MinSpaceByViaMet12Met2 = _DRCObj.DRCMETALxMinSpace(_Width= self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength= self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])
                _tmpDRCMinSpacePoly2OD = _DRCObj._PolygateMinSpace2OD             

                P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS = _DRCObj.DRCMETAL1MinSpace(_Width=self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength=self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                P_tmpDRCMet1MinSpaceByViaPoly2Met1 = _DRCObj.DRCMETAL1MinSpace(_Width= self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength= self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                P2_tmpDRCMet2MinSpaceByViaMet12Met2 = _DRCObj.DRCMETALxMinSpace(_Width= self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength= self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])

                
                if i == 1:
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        max(self._DesignParameter[VIAN]['_XYCoordinates'][0][1] 
                                            + float(self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                            self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])  
                                        + float(self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                        + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                    ]
                                ]
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                            [
                                [
                                    self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                    min(self._DesignParameter[VIAP]['_XYCoordinates'][0][1] 
                                        - float(self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                        self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                    - float(self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                    - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                                ]
                            ]
                    print ('ssa1', self._DesignParameter[NGateRouting]['_XYCoordinates'])
                elif i == 3:
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        max(self._DesignParameter[VIAN]['_XYCoordinates'][0][1] 
                                            + float(self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                            self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])  
                                        + float(self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                        + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD,N2_tmpDRCMet2MinSpaceByViaMet12Met2 ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                    ]
                                ]
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                            [
                                [
                                    self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                    min(self._DesignParameter[VIAP]['_XYCoordinates'][0][1] 
                                        - float(self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                        self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                    - float(self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                    - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD,P2_tmpDRCMet2MinSpaceByViaMet12Met2 ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                                ]
                            ]
                elif i == 2 :
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        max(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_XYCoordinates'][0][1] \
                                            + float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2\
                                            ,self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])
                                        + float(self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                        + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                    ]
                                ]
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                        [
                            [
                                self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                min(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_XYCoordinates'][0][1] 
                                    - float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                    self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                - float(self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                            ]
                        ]
                    print ('ssa2', self._DesignParameter[NGateRouting]['_XYCoordinates'] , _BiasDictforViaPoly2Met1OnGate[Nbias])
                elif i == 4 :
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        max(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][0][1] 
                                            + float(self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                            self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])  
                                        + float(self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                        + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                    ]
                                ]
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                        [
                            [
                                self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                min(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][0][1] 
                                    - float(self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                    self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                - float(self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                            ]
                        ]
                
                self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) ):
                    self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append([ [a + b for a , b in zip( self._DesignParameter[NMOS]['_XYCoordinates'][0],self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j])]
                                                                                            , [self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0], self._DesignParameter[NGateRouting]['_XYCoordinates'][0][1]]          ])
                self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) ):
                    self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([ [a + b for a , b in zip( self._DesignParameter[PMOS]['_XYCoordinates'][0],self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j])]
                                                                                            , [self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0], self._DesignParameter[PGateRouting]['_XYCoordinates'][0][1]]          ])

                self._DesignParameter[NGateRouting]['_XWidth']=(max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                self._DesignParameter[NGateRouting]['_YWidth']=self._DesignParameter[Poly2Met1ViaN]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
                self._DesignParameter[PGateRouting]['_XWidth']=(max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                self._DesignParameter[PGateRouting]['_YWidth']=self._DesignParameter[Poly2Met1ViaP]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

                  
            # )######PUT VIA FOR Gate (PO_M1)
            
            #Bias setting
            for i in range(1,5):
                XbiasN = '_XbiasNMOS'+str(i)+ 'GateVia'
                XbiasP = '_XbiasPMOS'+str(i)+ 'GateVia'
                YbiasN = '_YbiasNMOS'+str(i)+ 'GateVia'
                YbiasP = '_YbiasPMOS'+str(i)+ 'GateVia'

                if _BiasDictforViaPoly2Met1OnGate[XbiasN] is None:
                    _BiasDictforViaPoly2Met1OnGate[XbiasN] = 0
                if _BiasDictforViaPoly2Met1OnGate[XbiasP] is None:
                    _BiasDictforViaPoly2Met1OnGate[XbiasP] = 0
  
            
            for i in range (1 , 5):
                VIAN = '_ViaPoly2Met1OnNMOS' + str(i) + 'Gate'
                VIAP = '_ViaPoly2Met1OnPMOS' + str(i) + 'Gate'
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                XBiasofN = '_XbiasNMOS' + str(i) + 'GateVia'
                YBiasofN = '_YbiasNMOS' + str(i) + 'GateVia'
                XBiasofP = '_XbiasPMOS' + str(i) + 'GateVia'
                YBiasofP = '_YbiasPMOS' + str(i) + 'GateVia'
                NGateRouting = '_GateRoutingOnNMOS' + str(i)
                PGateRouting = '_GateRoutingOnPMOS' + str(i)
                
                self._DesignParameter[VIAN]['_XYCoordinates'] = [[ self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofN]
                                                                  ,self._DesignParameter[NGateRouting]['_XYCoordinates'][0][1] ]]#+ _BiasDictforViaPoly2Met1OnGate[YBiasofN] ]]         #NMOS Gate Via
                self._DesignParameter[VIAP]['_XYCoordinates'] = [[ self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofP]
                                                                  ,self._DesignParameter[PGateRouting]['_XYCoordinates'][0][1] ]]#+ _BiasDictforViaPoly2Met1OnGate[YBiasofP] ]]         #PMOS Gate Via
                if _XbiasNMOS3GateMet12Met2Via is None:
                    _XbiasNMOS3GateMet12Met2Via = 0
                if _XbiasPMOS3GateMet12Met2Via is None:
                    _XbiasPMOS3GateMet12Met2Via = 0

                if i is 3:
                    biasN = round((self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaPoly2Met1OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    biasP = -round((self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaPoly2Met1OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'] = [[ self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofN] + _XbiasNMOS3GateMet12Met2Via
                                                                                            ,self._DesignParameter[NGateRouting]['_XYCoordinates'][0][1] + biasN ]]#+ _BiasDictforViaPoly2Met1OnGate[YBiasofN] ]]
                    self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'] = [[ self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofP] + _XbiasPMOS3GateMet12Met2Via
                                                                                            ,self._DesignParameter[PGateRouting]['_XYCoordinates'][0][1] + biasP ]] # + _BiasDictforViaPoly2Met1OnGate[YBiasofP] ]]
            
                #Additional Poly for preparing when X bias is huge.
                AdditionalPolyOnNMOS = '_AdditionalGatePolyOn' + NMOS
                AdditionalPolyOnPMOS = '_AdditionalGatePolyOn' + PMOS
                self._DesignParameter[AdditionalPolyOnNMOS]['_XWidth'] = self._DesignParameter[NGateRouting]['_YWidth']
                self._DesignParameter[AdditionalPolyOnNMOS]['_XYCoordinates'] = [[ self._DesignParameter[VIAN]['_XYCoordinates'][0],self._DesignParameter[NGateRouting]['_XYCoordinates'][0]    ]]
                self._DesignParameter[AdditionalPolyOnPMOS]['_XWidth'] = self._DesignParameter[PGateRouting]['_YWidth']
                self._DesignParameter[AdditionalPolyOnPMOS]['_XYCoordinates'] = [[ self._DesignParameter[VIAP]['_XYCoordinates'][0],self._DesignParameter[PGateRouting]['_XYCoordinates'][0]    ]]
            
            
            
            # )######Input Routing
            self._DesignParameter['_InputDataRouting']['_Width'] = _DRCObj._Metal1MinWidth
            self._DesignParameter['_InputDataRouting']['_XYCoordinates'] = [[ self._DesignParameter['_ViaPoly2Met1OnNMOS1Gate']['_XYCoordinates'][0] , self._DesignParameter['_ViaPoly2Met1OnPMOS1Gate']['_XYCoordinates'][0] ]]
           # )################################ Left Output Routing(stage1) ################################
            if _OutputRoutingSEWidth is None:
                _OutputRoutingSEWidth = _DRCObj._MetalxMinWidth
            if _OutputRoutingEWidth is None:
                _OutputRoutingEWidth = _DRCObj._MetalxMinWidth
            if _OutputRoutingNEWidth is None:
                _OutputRoutingNEWidth = _DRCObj._MetalxMinWidth
            
            
            
            self._DesignParameter['_OutputRoutingNE']['_Width'] = _OutputRoutingNEWidth
            self._DesignParameter['_OutputRoutingE']['_Width'] = _OutputRoutingEWidth
            self._DesignParameter['_OutputRoutingSE']['_Width'] = _OutputRoutingSEWidth
            
            self._DesignParameter['_OutputRoutingNE']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_XYCoordinates'][-1][0], self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'][0][0][1] ]
                                                                            ,[self._DesignParameter['_PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'][0][0][1] ]   
                                                                            ,self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0]    ]]
            self._DesignParameter['_OutputRoutingE']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0],self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0]  ]]
            self._DesignParameter['_OutputRoutingSE']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_XYCoordinates'][-1][0], self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'][0][0][1] ]
                                                                            ,[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'][0][0][1] ]   
                                                                            ,self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0]    ]]
            
            
            Right_Side = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            Left_Side = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            NMOS_NPlength = Right_Side - Left_Side
            # )################################ NWELL ################################

            # # self._DesignParameter['_NWell']['_XWidth']= self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] + _DRCObj._NwMinEnclosurePactive*2
            # self._DesignParameter['_NWell']['_XWidth']= round( (abs(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) + abs(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5 ) *2* _DRCObj._MinSnapSpacing + _DRCObj._NwMinEnclosurePactive*2
            # self._DesignParameter['_NWell']['_YWidth']= _FFVdd2VssHeight - _FFEdgeBtwNWandPW + (float (self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            # self._DesignParameter['_NWell']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _FFEdgeBtwNWandPW ]]
            self._DesignParameter['_NWell']['_XWidth']= round((NMOS_NPlength + _DRCObj._NwMinEnclosurePactive*2)/2/_DRCObj._MinSnapSpacing) * 2 * _DRCObj._MinSnapSpacing
            self._DesignParameter['_NWell']['_YWidth']= _FFVdd2VssHeight - _FFEdgeBtwNWandPW + (float (_tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            self._DesignParameter['_NWell']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _FFEdgeBtwNWandPW ]]
            # )################################ NP UnderNMOS )################################
            tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]]
            tmp[0][1] += (float)(_FFEdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2)/2 -self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            self._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'] = tmp
            # self._DesignParameter['_NIMPUnderNMOS']['_XWidth']= self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
            self._DesignParameter['_NIMPUnderNMOS']['_XWidth']= NMOS_NPlength
            self._DesignParameter['_NIMPUnderNMOS']['_YWidth']= _FFEdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2
            # )################################ PP UnderNMOS )################################
            # self._DesignParameter['_PIMPUnderPMOS']['_XWidth']= self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
            self._DesignParameter['_PIMPUnderPMOS']['_XWidth']= NMOS_NPlength
            self._DesignParameter['_PIMPUnderPMOS']['_YWidth']=  _FFVdd2VssHeight - _FFEdgeBtwNWandPW - _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2
            tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] ]]
            tmp[0][1] = tmp[0][1] - ((self._DesignParameter['_PIMPUnderPMOS']['_YWidth'])/2 - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)
            self._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'] = tmp
            # )################################ Additional Metal1 ################################
            for i in range(1,5):
                AddiM1_N = '_AdditionalMet1OnNMOS' + str(i)
                AddiM1_P = '_AdditionalMet1OnPMOS' + str(i)
                VIAN = '_ViaMet12Met2OnNMOS' + str(i) + 'connection'
                VIAP = '_ViaMet12Met2OnPMOS' + str(i) + 'connection'
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                
                
                WidthN = self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                WidthP = self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                
            # if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) is not 1:  #Delete this if case
                self._DesignParameter[AddiM1_N]['_XWidth'] = WidthN
                self._DesignParameter[AddiM1_P]['_XWidth'] = WidthP
                self._DesignParameter[AddiM1_N]['_YWidth'] = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self._DesignParameter[AddiM1_P]['_YWidth'] = self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                
                #NMOS Met1 Area DRC
                biasY = 0
                Ylength = max( self._DesignParameter[AddiM1_N]['_YWidth'],self._DesignParameter['_ViaMet12Met2OnNMOS'+str(i)+'connection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
                if WidthN * Ylength < _DRCObj._Metal1MinArea:
                    newY = round(_DRCObj._Metal1MinArea / WidthN / _DRCObj._MinSnapSpacing + 0.5 ) * _DRCObj._MinSnapSpacing
                    biasY = float(self._DesignParameter[AddiM1_N]['_YWidth'] - newY) / 2
                    self._DesignParameter[AddiM1_N]['_YWidth']  = newY
                
                if i==1 or i==3:
                    if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) is not 1:
                        for j in range(0, len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ):
                            self._DesignParameter[AddiM1_N]['_XYCoordinates'].append([a+b for a,b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                            self._DesignParameter[AddiM1_N]['_XYCoordinates'][j][1] += biasY
                            self._DesignParameter[AddiM1_P]['_XYCoordinates'].append([a+b for a,b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                else:
                    # if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) is not 1:
                    for j in range(0, len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) ):
                        self._DesignParameter[AddiM1_N]['_XYCoordinates'].append([a+b for a,b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j],self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                        self._DesignParameter[AddiM1_N]['_XYCoordinates'][j][1] += biasY
                        self._DesignParameter[AddiM1_P]['_XYCoordinates'].append([a+b for a,b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j],self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                    if i is 2:
                        for j in range(0, len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ):
                            if _YBiasOfOuputViaMet12Met2OnNMOSLeft is None:
                                _YBiasOfOuputViaMet12Met2OnNMOSLeft = 0
                            if _YBiasOfOuputViaMet12Met2OnPMOSLeft is None:
                                _YBiasOfOuputViaMet12Met2OnPMOSLeft = 0
                            self._DesignParameter['_AdditionalMet1OnNMOS2_forOutputVia']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                            self._DesignParameter['_AdditionalMet1OnPMOS2_forOutputVia']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutputLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                            self._DesignParameter['_AdditionalMet1OnNMOS2_forOutputVia']['_YWidth'] = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + abs(_YBiasOfOuputViaMet12Met2OnNMOSLeft)
                            self._DesignParameter['_AdditionalMet1OnPMOS2_forOutputVia']['_YWidth'] = self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + abs(_YBiasOfOuputViaMet12Met2OnPMOSLeft)
                            self._DesignParameter['_AdditionalMet1OnNMOS2_forOutputVia']['_XYCoordinates'].append([a+b+c for a,b,c in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[NMOS]['_XYCoordinates'][0], [0, _YBiasOfOuputViaMet12Met2OnNMOSLeft/2 ]  ) ])
                            self._DesignParameter['_AdditionalMet1OnPMOS2_forOutputVia']['_XYCoordinates'].append([a+b+c for a,b,c in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[PMOS]['_XYCoordinates'][0], [0 ,_YBiasOfOuputViaMet12Met2OnPMOSLeft/2 ]  ) ])
                    elif i is 4:
                        for j in range(0, len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ):
                            self._DesignParameter['_AdditionalMet1OnNMOS4_forOutputVia']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                            self._DesignParameter['_AdditionalMet1OnPMOS4_forOutputVia']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                            self._DesignParameter['_AdditionalMet1OnNMOS4_forOutputVia']['_YWidth'] = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + abs(_YBiasOfOuputViaMet12Met2OnNMOSRight)
                            self._DesignParameter['_AdditionalMet1OnPMOS4_forOutputVia']['_YWidth'] = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + abs(_YBiasOfOuputViaMet12Met2OnPMOSRight)
                            self._DesignParameter['_AdditionalMet1OnNMOS4_forOutputVia']['_XYCoordinates'].append([a+b+c for a,b,c in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[NMOS]['_XYCoordinates'][0], [0, _YBiasOfOuputViaMet12Met2OnNMOSRight/2 ]   ) ])
                            self._DesignParameter['_AdditionalMet1OnPMOS4_forOutputVia']['_XYCoordinates'].append([a+b+c for a,b,c in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j],self._DesignParameter[PMOS]['_XYCoordinates'][0], [0, _YBiasOfOuputViaMet12Met2OnPMOSRight/2 ]   ) ])
                # )################################ Additional Metal2 for VOID ################################
                _VoidWidthP = self._DesignParameter['_OutputRoutingNE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingNE']['_Width']/2 - self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
                _VoidWidthN = -self._DesignParameter['_OutputRoutingSE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingSE']['_Width']/2 + self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
                
                pathWidthP = round(_VoidWidthP/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                pathWidthN = round(_VoidWidthN/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                if float(int(pathWidthP/_DRCObj._MinSnapSpacing)) is not float(pathWidthP/_DRCObj._MinSnapSpacing):
                    pathWidthP += _DRCObj._MinSnapSpacing
                if float(int(pathWidthN/_DRCObj._MinSnapSpacing)) is not float(pathWidthN/_DRCObj._MinSnapSpacing):
                    pathWidthN += _DRCObj._MinSnapSpacing

                if 0 < _VoidWidthP and _VoidWidthP < _DRCObj._MetalxMinSpace:
                    _tempYforP = round( (self._DesignParameter['_OutputRoutingNE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingNE']['_Width']/2  + self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    self._DesignParameter['_AdditionalMet2OnPMOS_for_void']['_Width'] = pathWidthP
                    self._DesignParameter['_AdditionalMet2OnPMOS_for_void']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0]- self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2, _tempYforP]
                                                                                                 ,[self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0],  _tempYforP  ] ]]
                if 0 < _VoidWidthN and _VoidWidthN < _DRCObj._MetalxMinSpace:
                    _tempYforN = round( (self._DesignParameter['_OutputRoutingSE']['_XYCoordinates'][0][0][1] + self._DesignParameter['_OutputRoutingSE']['_Width']/2  + self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    self._DesignParameter['_AdditionalMet2OnNMOS_for_void']['_Width'] = pathWidthN
                    self._DesignParameter['_AdditionalMet2OnNMOS_for_void']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0]- self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2, _tempYforN]
                                                                                                 ,[self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0],  _tempYforN  ] ]]
                # _AdditionalMet2OnNMOS_for_void
            
            # )################################ DRC Verification ################################
            DRC_PASS=1
            
            
            #Additional Met2
            for i in range(1,5):
                VIAP = '_ViaMet12Met2OnPMOS' + str(i) + 'connection'
                VIAN = '_ViaMet12Met2OnNMOS' + str(i) + 'connection'
                
                
                N_XWidth = self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] 
                N_YWidth = self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                while N_XWidth * N_YWidth < _DRCObj._MetalxMinArea :
                    N_XWidth += 2*_DRCObj._MinSnapSpacing 
                
                P_XWidth = self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] 
                P_YWidth = self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                while P_XWidth * P_YWidth < _DRCObj._MetalxMinArea :
                    P_XWidth += 2*_DRCObj._MinSnapSpacing 
                    
                self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = N_XWidth
                self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = P_XWidth
            
            
            #Output Via Y-axis Calibration
            pause = 0
            LEFT_DistanceBtwOutputRouting2connectionViaN = float(self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingOnNMOSLeft']['_Width']/2 )\
                                                      -float(self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_XYCoordinates'][0][1] +  self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )
            _MET2distanceDRC = \
                                max(_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_OutputRoutingOnNMOSLeft']['_Width'], _ParallelLength=(self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'][0][-1][0]- self._DesignParameter['_OutputRoutingOnNMOSLeft']['_XYCoordinates'][0][0][0]))    \
                                   ,_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength=self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']) )

            if  (len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) != 1 ) or (len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) != 1) :
                if (LEFT_DistanceBtwOutputRouting2connectionViaN < _MET2distanceDRC):
                    temp = round((_MET2distanceDRC-LEFT_DistanceBtwOutputRouting2connectionViaN)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    _YBiasOfOuputViaMet12Met2OnNMOSLeft += temp
                    pause = 1
                    DRC_PASS = 0
                
                
                
                LEFT_DistanceBtwOutputRouting2connectionViaP = -float(self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'][0][0][1] + self._DesignParameter['_OutputRoutingOnPMOSLeft']['_Width']/2 )\
                                                           +float(self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )
                _MET2distanceDRC = \
                                    max(_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_OutputRoutingOnPMOSLeft']['_Width'], _ParallelLength=(self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'][0][-1][0]- self._DesignParameter['_OutputRoutingOnPMOSLeft']['_XYCoordinates'][0][0][0]))    \
                                       ,_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength=self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']) )

                if LEFT_DistanceBtwOutputRouting2connectionViaP < _MET2distanceDRC :
                    temp = -round((_MET2distanceDRC-LEFT_DistanceBtwOutputRouting2connectionViaP)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    _YBiasOfOuputViaMet12Met2OnPMOSLeft += temp
                    # self._DesignParameter['_AdditionalMet1OnPMOS2_forOutputVia']['_YWidth'] += abs(temp) 
                    # self._DesignParameter['_AdditionalMet1OnPMOS2_forOutputVia']['_XYCoordinates'][0][1] -= abs(temp)/2
                    pause = 1
                    DRC_PASS = 0
            
            
            if  len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) != 1 :  
                RIGHT_DistanceBtwOutputRouting2connectionViaN = float(self._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingOnNMOSRight']['_Width']/2 )\
                                                          -float(self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_XYCoordinates'][0][1] +  self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )
                _MET2distanceDRC = \
                                    max(_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_OutputRoutingOnNMOSRight']['_Width'], _ParallelLength=(self._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'][0][-1][0]- self._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'][0][0][0]))    \
                                       ,_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength=self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']) )

                if RIGHT_DistanceBtwOutputRouting2connectionViaN < _MET2distanceDRC :
                    temp = round((_MET2distanceDRC-RIGHT_DistanceBtwOutputRouting2connectionViaN)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    _YBiasOfOuputViaMet12Met2OnNMOSRight += temp
                    pause = 1
                    DRC_PASS = 0
                
                
                
                RIGHT_DistanceBtwOutputRouting2connectionViaP = -float(self._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][1] + self._DesignParameter['_OutputRoutingOnPMOSRight']['_Width']/2 )\
                                                           +float(self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )
                _MET2distanceDRC = \
                                    max(_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_OutputRoutingOnPMOSRight']['_Width'], _ParallelLength=(self._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][-1][0]- self._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][0]))    \
                                       ,_DRCObj.DRCMETALxMinSpace(_Width=self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], _ParallelLength=self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']) )

                if RIGHT_DistanceBtwOutputRouting2connectionViaP < _MET2distanceDRC :
                    temp = -round((_MET2distanceDRC-RIGHT_DistanceBtwOutputRouting2connectionViaP)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    _YBiasOfOuputViaMet12Met2OnPMOSRight += temp
                    pause = 1
                    DRC_PASS = 0

            
       
                
                
            # BodyContact Adjusting
            _LengthOfBody = self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']
            leftSideOD = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2 
            rightSideOD = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2
            _LengthOfOD = abs(rightSideOD - leftSideOD )
            
            if _NumberOfSupplyCOX is None:
                _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 \
                        else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX

            self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)
            self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)
            self._DesignParameter['_PbodyContact']['_XYCoordinates'] = _tmpPbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_NbodyContact']['_XYCoordinates'] = _tmpNbodyObj._DesignParameter['_XYCoordinates']


            del _tmpPbodyObj
            del _tmpNbodyObj
            
            
            # _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None,
            if _HeightCalOption == 'ON' :
                tempVal = 0; tempVal2 = 0; error = 0
                for i in range(1,5):
                    VIAN = '_ViaPoly2Met1OnNMOS' + str(i) + 'Gate'
                    VIAP = '_ViaPoly2Met1OnPMOS' + str(i) + 'Gate'
                    _DistanceBtwViaNEdge2NW = (_FFEdgeBtwNWandPW + tempVal) - self._DesignParameter[VIAN]['_XYCoordinates'][0][1] - self._DesignParameter[VIAN]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2

                    while _DistanceBtwViaNEdge2NW < _DRCObj._PpMinEnclosureOfPo :
                        
                        _YbiasforEdgeBtwNWandPW += _DRCObj._MinSnapSpacing
                        # _YbiasforHeight += _DRCObj._MinSnapSpacing
                        _DistanceBtwViaNEdge2NW += _DRCObj._MinSnapSpacing
                        tempVal += _DRCObj._MinSnapSpacing
                        DRC_PASS = 0
                        if _HeightCalOption != 'ON' :
                            error = 1
            
    
                if error == 1 :
                    print ('****************************** Error occured in _XOREdgeBtwNWandPW setting ******************************')
                    print ('_XOREdgeBtwNWandPW Should be same or higher than' , _FFEdgeBtwNWandPW+ tempVal)
                    return 0
                    
                for i in range(1,5):
                    VIA = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate'
                    _DistanceBtwViaPEdge2NW = -(_FFEdgeBtwNWandPW+tempVal) + self._DesignParameter[VIAP]['_XYCoordinates'][0][1] - self._DesignParameter[VIAP]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 + tempVal2

                    while _DistanceBtwViaPEdge2NW < _DRCObj._PpMinEnclosureOfPo :
                        _YbiasforHeight += _DRCObj._MinSnapSpacing
                        _DistanceBtwViaPEdge2NW += _DRCObj._MinSnapSpacing
                        tempVal2 += _DRCObj._MinSnapSpacing
                        DRC_PASS = 0
                        if _HeightCalOption != 'ON' :
                            error = 1
                if error == 1 :
                    print ('****************************** Error occured in _XORVdd2VssHeight setting ******************************')
                    print ('_XORVdd2VssHeight Should be same or higher than' , _FFVdd2VssHeight + tempVal2)
                    return 0            
             
            
            MOS12MOS2Connection = 0
            MOS32MOS4Connection = 0
            MOS12MOS2deleteMet3Connection = 0
            MOS32MOS4deleteMet3Connection = 0

            ## Delete useless VIAs (depending on number of gates)
            if len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])%2 == 1:
                if len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                    self._DesignParameter['_ViaMet12Met2OnNMOS1connection']['_XYCoordinates'] = []
                    self._DesignParameter['_ViaMet22Met3OnNMOS1connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet12Met2OnPMOS1connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet22Met3OnPMOS1connection']['_XYCoordinates'] = []
                    MOS12MOS2Connection = 1
                    MOS12MOS2deleteMet3Connection = 1
                    self._DesignParameter['_NMOSConnectionRoutingLeft']['_XYCoordinates'][0][0] = self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_XYCoordinates'][0]
                    # self._DesignParameter['_PMOSConnectionRoutingLeft']['_XYCoordinates'][0][0] = self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_XYCoordinates'][0]
                    
                if len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                    self._DesignParameter['_ViaMet12Met2OnNMOS2connection']['_XYCoordinates'] = []
                    self._DesignParameter['_ViaMet22Met3OnNMOS2connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet12Met2OnPMOS2connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet22Met3OnPMOS2connection']['_XYCoordinates'] = []
                    self._DesignParameter['_AdditionalMet1OnNMOS2']['_XYCoordinates'] = []
                    # self._DesignParameter['_AdditionalMet1OnPMOS2']['_XYCoordinates'] = []
                    MOS12MOS2Connection = 1
                    if MOS12MOS2deleteMet3Connection is 1:
                        self._DesignParameter['_NMOSConnectionRoutingLeft']['_XYCoordinates'] = []
                        # self._DesignParameter['_PMOSConnectionRoutingLeft']['_XYCoordinates'] = []
                    else :
                        self._DesignParameter['_NMOSConnectionRoutingLeft']['_XYCoordinates'][0][1] = self._DesignParameter['_ViaMet12Met2OnNMOS1connection']['_XYCoordinates'][-1]
                        # self._DesignParameter['_PMOSConnectionRoutingLeft']['_XYCoordinates'][0][1] = self._DesignParameter['_ViaMet12Met2OnPMOS1connection']['_XYCoordinates'][-1]
            if len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])%2 == 1:
                if len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                    self._DesignParameter['_ViaMet12Met2OnNMOS3connection']['_XYCoordinates'] = []
                    self._DesignParameter['_ViaMet22Met3OnNMOS3connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet12Met2OnPMOS3connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet22Met3OnPMOS3connection']['_XYCoordinates'] = []
                    MOS32MOS4Connection = 1
                    MOS32MOS4deleteMet3Connection = 1
                    self._DesignParameter['_NMOSConnectionRoutingRight']['_XYCoordinates'][0][0] = self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_XYCoordinates'][0]
                    # self._DesignParameter['_PMOSConnectionRoutingRight']['_XYCoordinates'][0][0] = self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_XYCoordinates'][0]
                    
                if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                    self._DesignParameter['_ViaMet12Met2OnNMOS4connection']['_XYCoordinates'] = []
                    self._DesignParameter['_ViaMet22Met3OnNMOS4connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet12Met2OnPMOS4connection']['_XYCoordinates'] = []
                    # self._DesignParameter['_ViaMet22Met3OnPMOS4connection']['_XYCoordinates'] = []
                    self._DesignParameter['_AdditionalMet1OnNMOS4']['_XYCoordinates'] = []
                    # self._DesignParameter['_AdditionalMet1OnPMOS4']['_XYCoordinates'] = []
                    MOS32MOS4Connection = 1
                    if MOS32MOS4deleteMet3Connection is 1:
                        self._DesignParameter['_NMOSConnectionRoutingRight']['_Ignore'] = True
                        # self._DesignParameter['_PMOSConnectionRoutingRight']['_Ignore'] = True
                    else :
                        self._DesignParameter['_NMOSConnectionRoutingRight']['_XYCoordinates'][0][1] = self._DesignParameter['_ViaMet12Met2OnNMOS3connection']['_XYCoordinates'][-1]
                        # self._DesignParameter['_PMOSConnectionRoutingRight']['_XYCoordinates'][0][1] = self._DesignParameter['_ViaMet12Met2OnPMOS3connection']['_XYCoordinates'][-1]
                        
            # if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                # self._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'] = []
                # self._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'] = []
                # self._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'] = []
                # self._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'] = []
                # self._DesignParameter['_AdditionalMet1OnNMOS4_forOutputVia']['_XYCoordinates'] = []
                # self._DesignParameter['_AdditionalMet1OnPMOS4_forOutputVia']['_XYCoordinates'] = []
                
            PMOS_MET1_DISTANCE = abs( self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0] ) - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            
            if MOS12MOS2Connection is 1:
                self._DesignParameter['_NMOS12NMOS2Met1Connection']['_Width'] = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self._DesignParameter['_NMOS12NMOS2Met1Connection']['_XYCoordinates'] =[[ [a+b for a,b in zip(self._DesignParameter['_NMOS1']['_XYCoordinates'][0] , self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])]
                                                                                         ,[a+b for a,b in zip(self._DesignParameter['_NMOS2']['_XYCoordinates'][0] , self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0] )]      ]]
                
                
                # self._DesignParameter['_PMOS12PMOS2Met1Connection']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                # self._DesignParameter['_PMOS12PMOS2Met1Connection']['_XYCoordinates'] =[[ [a+b for a,b in zip(self._DesignParameter['_PMOS1']['_XYCoordinates'][0] , self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1])]
                                                                                         # ,[a+b for a,b in zip(self._DesignParameter['_PMOS2']['_XYCoordinates'][0] , self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0] )]      ]]
                # Met1DRC = _DRCObj._Metal1MinSpace(_Width = (self._DesignParameter['_PMOS12PMOS2Met1Connection']['_XYCoordinates'][0][1][0] - self._DesignParameter['_PMOS12PMOS2Met1Connection']['_XYCoordinates'][0][0][0]), _ParallelLength = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']  )
                # if PMOS_MET1_DISTANCE < Met1DRC:
                    # self._DesignParameter['_PMOS12PMOS2Met1Connection']['_Width'] = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                                                                                         
            if MOS32MOS4Connection is 1:
                self._DesignParameter['_NMOS32NMOS4Met1Connection']['_Width'] = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self._DesignParameter['_NMOS32NMOS4Met1Connection']['_XYCoordinates'] =[[ [a+b for a,b in zip(self._DesignParameter['_NMOS3']['_XYCoordinates'][0] , self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1])]
                                                                                         ,[a+b for a,b in zip(self._DesignParameter['_NMOS4']['_XYCoordinates'][0] , self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0] )]      ]]
                # self._DesignParameter['_PMOS32PMOS4Met1Connection']['_Width'] = self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                # self._DesignParameter['_PMOS32PMOS4Met1Connection']['_XYCoordinates'] =[[ [a+b for a,b in zip(self._DesignParameter['_PMOS3']['_XYCoordinates'][0] , self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1])]
                                                                                         # ,[a+b for a,b in zip(self._DesignParameter['_PMOS4']['_XYCoordinates'][0] , self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0] )]      ]]
                
            
            
            if (_Dummy is True) and (pause is not 1):
            
                for i in range(1,5):
                    NMOS = '_NMOS' + str(i)
                    PMOS = '_PMOS' + str(i)
                    NVIA = '_ViaPoly2Met1OnNMOS' + str(i) + 'Gate'
                    PVIA = '_ViaPoly2Met1OnPMOS' + str(i) + 'Gate'
                    NViaBias = '_YbiasNMOS' + str(i)+ 'GateVia'
                    PViaBias = '_YbiasPMOS' + str(i)+ 'GateVia'
                    print ('abcd' , self._DesignParameter[NVIA]['_XYCoordinates'][0], NVIA)
                    if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                    # NMOS adjusting
                        print ('abcd' , self._DesignParameter[NVIA]['_XYCoordinates'][0], NVIA)
                        _DistanceBtwVia2GateY = \
                            float(self._DesignParameter[NVIA]['_XYCoordinates'][0][1] - self._DesignParameter[NVIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 ) \
                            -float(self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][1]+self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) 
                        if _DistanceBtwVia2GateY < _DRCObj._PolygateMinSpace:
                            temp = round(abs(_DRCObj._PolygateMinSpace- _DistanceBtwVia2GateY)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            _BiasDictforViaPoly2Met1OnGate[NViaBias] += temp
                            DRC_PASS = 0
                        print ('sungyu' , _BiasDictforViaPoly2Met1OnGate[NViaBias] ,  NViaBias)
                            
                    
                    if len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates']) is 1:
                    # PMOS adjusting
                        _DistanceBtwVia2GateY = \
                            float(self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][1]-self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) \
                            -float(self._DesignParameter[PVIA]['_XYCoordinates'][0][1] + self._DesignParameter[PVIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)
                        if _DistanceBtwVia2GateY < _DRCObj._PolygateMinSpace:
                            temp = round( abs(_DRCObj._PolygateMinSpace - _DistanceBtwVia2GateY)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            _BiasDictforViaPoly2Met1OnGate[PViaBias] -= temp
                            DRC_PASS = 0
            
                

            
            #MOSFET XY Coordinates adjusting
            MostLeft = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            MostRight = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            if abs(MostLeft + MostRight)/2 > 2*_DRCObj._MinSnapSpacing:
                _XYadjust += -round((MostLeft + MostRight)/2/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                DRC_PASS = 0
            
                        
                        
            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  FlipFlop Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


if __name__=='__main__':


    #############045nm xor #####################################################################
    # FLIPFLOPObj=_FLIPFLOP(_DesignParameter=None, _Name='FlipFlop')
    # FLIPFLOPObj._CalculateDesignParameter(
    #                      _NumberOfGate1=6, _ChannelWidth1=350, _ChannelLength1=50, _PNChannelRatio1=2, \
    #                      _NumberOfGate2=6, _ChannelWidth2=350, _ChannelLength2=50, _PNChannelRatio2=2, \
    #                      _NumberOfGate3=6, _ChannelWidth3=350, _ChannelLength3=50, _PNChannelRatio3=2, \
    #                      _NumberOfGate4=6, _ChannelWidth4=350, _ChannelLength4=50, _PNChannelRatio4=2, \
    #                      _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
    #
    #                      _FFSupplyMetal1XWidth=None, _FFSupplyMetal1YWidth=None, \
    #                      _FFVdd2VssHeight=None, _DistanceBtwSupplyCenter2MOSEdge=None, _FFEdgeBtwNWandPW=None, _XYadjust=None,
    #
    #                      _NumberOfNMOSConnectionViaCOY = 4, _NumberOfPMOSConnectionViaCOY =None, _NumberOfPMOSOutputViaCOY=None,
    #                      _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,
    #                      _NumberOfPMOSOutputLeftViaCOY=None, _NumberOfNMOSOutputLeftViaCOY=None,
    #                      _NumberOfPMOSOutputRightViaCOY=None, _NumberOfNMOSOutputRightViaCOY=None,
    #
    #
    #                      _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption= 'ON',
    #                      _MOS12MOS2spacebias=None, _MOS22MOS3spacebias=None, _MOS32MOS4spacebias=None,
    #                      _YBiasOfOuputViaMet12Met2OnPMOSLeft=None, _YBiasOfOuputViaMet12Met2OnNMOSLeft=None,_YBiasOfOuputViaMet12Met2OnPMOSRight=None, _YBiasOfOuputViaMet12Met2OnNMOSRight=None,
    #
    #                      _BiasDictforViaPoly2Met1OnGate = {
    #                      '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None,
    #                      '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
    #                      '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
    #                      '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':None,
    #                      },
    #
    #                      _OutputRoutingSEWidth=None,_OutputRoutingEWidth=None,_OutputRoutingNEWidth=None,
    #                      _OutputRoutingOnNMOSLeftWidth=None,_OutputRoutingOnPMOSLeftWidth=None,
    #                      _Dummy=True)
    ##############045nm xor #####################################################################
    # FLIPFLOPObj=_FLIPFLOP(_DesignParameter=None, _Name='FlipFlop')
    # FLIPFLOPObj._CalculateDesignParameter( _FFVdd2VssHeight=5000, _HeightCalOption='ON',\
                                      # _NumberOfGate1=4, _ChannelWidth1=350, _ChannelLength1=50, _PNChannelRatio1=2, \
                                      # _NumberOfGate2=3, _ChannelWidth2=350, _ChannelLength2=50, _PNChannelRatio2=2, \
                                      # _NumberOfGate3=4, _ChannelWidth3=350, _ChannelLength3=50, _PNChannelRatio3=2, \
                                      # _NumberOfGate4=3, _ChannelWidth4=350, _ChannelLength4=50, _PNChannelRatio4=2, \
                                         # _NumberOfNMOSConnectionViaCOY = 2, _NumberOfPMOSConnectionViaCOY =3,
                                         # _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,
                                         # _NumberOfPMOSOutputLeftViaCOY=None, _NumberOfNMOSOutputLeftViaCOY=None,
                                         # _NumberOfPMOSOutputRightViaCOY=None, _NumberOfNMOSOutputRightViaCOY=None,
                                         # _BiasDictforViaPoly2Met1OnGate = {
                                         # '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None, 
                                         # '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
                                         # '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
                                         # '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0,
                                         # },     # XBias does not consider DRC calc value
                                         
                                         # _DistanceBtwSupplyCenter2MOSEdge=None, _FFEdgeBtwNWandPW=1500,
                                         # # _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=20, _MOS32MOS4spacebias=0, \
                                         # _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         # _FFSupplyMetal1XWidth=None, _FFSupplyMetal1YWidth=None, \
                                         # _OutputRoutingSEWidth=None,_OutputRoutingEWidth=None,_OutputRoutingNEWidth=None,
                                        # _OutputRoutingOnNMOSLeftWidth=None,_OutputRoutingOnPMOSLeftWidth=None,
                                         # _Dummy=True)
    # ##################################################################################################################################################################

    ##############065nm XOR #####################################################################
    FLIPFLOPObj=_FLIPFLOP(_DesignParameter=None, _Name='FlipFlop')
    FLIPFLOPObj._CalculateDesignParameter( _FFVdd2VssHeight=5000, _HeightCalOption='ON',\
                                      _NumberOfGate1=4, _ChannelWidth1=450, _ChannelLength1=60, _PNChannelRatio1=2, \
                                      _NumberOfGate2=3, _ChannelWidth2=450, _ChannelLength2=60, _PNChannelRatio2=2, \
                                      _NumberOfGate3=4, _ChannelWidth3=450, _ChannelLength3=60, _PNChannelRatio3=2, \
                                      _NumberOfGate4=3, _ChannelWidth4=450, _ChannelLength4=60, _PNChannelRatio4=2, \
                                         _NumberOfNMOSConnectionViaCOY = 2, _NumberOfPMOSConnectionViaCOY =2,
                                         _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,
                                         _NumberOfPMOSOutputLeftViaCOY=None, _NumberOfNMOSOutputLeftViaCOY=None,
                                         _NumberOfPMOSOutputRightViaCOY=None, _NumberOfNMOSOutputRightViaCOY=None,
                                         _BiasDictforViaPoly2Met1OnGate = {
                                         '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None,
                                         '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
                                         '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
                                         '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0,
                                         },     # XBias does not consider DRC calc value
                                         
                                         _DistanceBtwSupplyCenter2MOSEdge=None, _FFEdgeBtwNWandPW=1500,
                                         # _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=20, _MOS32MOS4spacebias=0, \
                                         _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         _FFSupplyMetal1XWidth=None, _FFSupplyMetal1YWidth=None, \
                                         _OutputRoutingSEWidth=None,_OutputRoutingEWidth=None,_OutputRoutingNEWidth=None,
                                        _OutputRoutingOnNMOSLeftWidth=None,_OutputRoutingOnPMOSLeftWidth=None,
                                         _Dummy=True)

    # ##################################################################################################################################################################
    ####################180nm XOR#########################################################################
    # XORObj=_XOR(_DesignParameter=None, _Name='XOR')
    # XORObj._CalculateDesignParameter( _INVNumberOfGate=2, _INVChannelWidth=1300, _INVChannelLength=180, _INVPNChannelRatio=2, _XORVdd2VssHeight=3300, _HeightCalOption='ON',\
                                      # _NumberOfGate1=4, _ChannelWidth1=1300, _ChannelLength1=180, _PNChannelRatio1=2, \
                                      # _NumberOfGate2=4, _ChannelWidth2=1300, _ChannelLength2=180, _PNChannelRatio2=2, \
                                      # _NumberOfGate3=4, _ChannelWidth3=1300, _ChannelLength3=180, _PNChannelRatio3=2, \
                                      # _NumberOfGate4=4, _ChannelWidth4=1300, _ChannelLength4=180, _PNChannelRatio4=2, \
                                         # _NumberOfNMOSConnectionViaCOY = None, _NumberOfPMOSConnectionViaCOY =None,
                                         # _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                         # _BiasDictforViaPoly2Met1OnGate = {
                                         # '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None, 
                                         # '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
                                         # '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
                                         # '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0,
                                         # '_XbiasInvNMOSGateVia':None,    '_YbiasInvNMOSGateVia':None,   '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                         # },     # XBias does not consider DRC calc value
                                         
                                         # _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=1500,
                                         # _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=20, _MOS32MOS4spacebias=0, \
                                         # _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         # _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,\
                                         # _Dummy=False)
    ##########################################################################################################################################################################
    #INVObj=_INV(_INVDesignParameter=DesignParameters.INVDesignParameter, _INVName='INV2')
    #INVObj=_INV(_Technology=DesignParameters._Technology, _XYCoordinateINV=[0,0], _NumberOfINVCO=2, _WidthXINVOD=890, _WidthYINVOD=420, _WidthXINVNP=1250, _WidthYINVNP=780, _WidthINVCO=220, _LengthINVBtwCO=470, _WidthXINVMet1=810, _WidthYINVMet1=340, _INVName='INV')
    FLIPFLOPObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=FLIPFLOPObj._DesignParameter)
    _fileName='autoFlipFlop_45.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=FLIPFLOPObj._CreateGDSStream(FLIPFLOPObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()





# Consider output routing on PMOS DRC






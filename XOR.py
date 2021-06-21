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

class _XOR(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
                                     _INVNumberOfGate=None, _INVChannelWidth=None, _INVChannelLength=None, _INVPNChannelRatio=None,
                                     _NumberOfGate1=None, _ChannelWidth1=None, _ChannelLength1=None, _PNChannelRatio1=None,
                                     _NumberOfGate2=None, _ChannelWidth2=None, _ChannelLength2=None, _PNChannelRatio2=None,
                                     _NumberOfGate3=None, _ChannelWidth3=None, _ChannelLength3=None, _PNChannelRatio3=None,
                                     _NumberOfGate4=None, _ChannelWidth4=None, _ChannelLength4=None, _PNChannelRatio4=None,
                                     _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                     _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None, 

                                     _XORVdd2VssHeight=None,  _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=None, _InputRouting=None, _OutputMet2Width = None,
                                     
                                     _HeightCalibration = None,

                                     
                                     
                                     _YBiasForViaMet12Met2OnPMOS2Output=None,_YBiasForViaMet12Met2OnPMOS3Output=None,_YBiasForViaMet12Met2OnNMOS2Output=None,_YBiasForViaMet12Met2OnNMOS3Output=None,
                                     _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None, _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None, _NumberOfPMOSConnectionCOY=None,
                                     _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,
                                     _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption=None,
                                     _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfNMOSOutputViaCOY=None, _NumberOfPMOSOutputViaCOY=None,
                                     _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                     _BiasDictforViaPoly2Met1OnGate = {
                                     '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None, '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None, '_XbiasNMOS3GateVia':None,
                                     '_YbiasNMOS3GateVia':None, '_XbiasNMOS4GateVia':None, '_YbiasNMOS4GateVia':None, '_XbiasInvNMOSGateVia':None, '_YbiasInvNMOSGateVia':None,
                                     '_XbiasPMOS1GateVia':None, '_YbiasPMOS1GateVia':None, '_XbiasPMOS2GateVia':None, '_YbiasPMOS2GateVia':None, '_XbiasPMOS3GateVia':None,
                                     '_YbiasPMOS3GateVia':None, '_XbiasPMOS4GateVia':None, '_YbiasPMOS4GateVia':None, '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                     },
                                     _MOS12MOS2spacebias=None, _MOS22InvMOSspacebias=None, _InvMOS2MOS3spacebias=None, _MOS32MOS4spacebias=None, _XYadjust=None,

                                     
                                     _InvNMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS1DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS2DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS3DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS4DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _InvPMOSDesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
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
                                     _ViaMet12Met2OnNMOSOutputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS1GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS2GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS3GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS4GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnInvMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),

                                     _Dummy=False
                                     )

    def __init__(self, _DesignParameter=None, _Name='INV'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(
                                                    _InvNMOS = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0],
                                                    _InvPMOS = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOSIn{}'.format(_Name)))[0],
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
                                                    _ViaMet12Met2OnPMOSconnection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSconnectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSconnection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSconnectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOSconnection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSconnectionIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOSconnection = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSconnectionIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS1Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS1GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS2Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS2GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS3Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS3GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS4Gate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS4GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnInvMOSGate = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnInvMOSGateIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSGate = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSGateIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSGate = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSGateIn{}'.format(_Name)))[0],


                                                    _NMOSConnectionRouting = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _PMOSConnectionRouting = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRouting = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _OutputRouting2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _InputDataRouting1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _InputDataRouting2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _DataBarRouting1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _DataBarRouting2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),

                                                    _ViaPoly2Met1=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1In{}'.format(_Name)))[0],
                                                    # _ViaMet12Met2OnNMOS=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSIn{}'.format(_Name)))[0],
                                                    # _ViaMet12Met2OnPMOS=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSIn{}'.format(_Name)))[0],
                                                    _AdditionalMet1OnNMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnPMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    # _AdditionalMet2OnNMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
                                                    # _AdditionalMet2OnPMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400,_YWidth=400),
													_AdditionalPolyOnPMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
													_AdditionalPolyOnNMOS=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    
                                                    _AdditionalMet1OnNMOS_for_void=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnPMOS_for_void=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),



                                                    _INVOutputRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _INVOutputRouting2=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 ),
                                                    _INVInputRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _INVInputRouting2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _INVInputRouting3=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100),
                                                    _PMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _NMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _NWell=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),


                                                    
                                                    
                                                    _GateRoutingOnNMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnNMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnInvNMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    
                                                    _GateRoutingOnPMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnPMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    _GateRoutingOnInvPMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1]),
                                                    
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
                                                   
    def _CalculateDesignParameter(self, _INVNumberOfGate=None, _INVChannelWidth=None, _INVChannelLength=None, _INVPNChannelRatio=None,
                                     _NumberOfGate1=None, _ChannelWidth1=None, _ChannelLength1=None, _PNChannelRatio1=None,
                                     _NumberOfGate2=None, _ChannelWidth2=None, _ChannelLength2=None, _PNChannelRatio2=None,
                                     _NumberOfGate3=None, _ChannelWidth3=None, _ChannelLength3=None, _PNChannelRatio3=None,
                                     _NumberOfGate4=None, _ChannelWidth4=None, _ChannelLength4=None, _PNChannelRatio4=None,
                                     _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                     _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,

                                     _XORVdd2VssHeight=None,  _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=None, _InputRouting=None, _OutputMet2Width = None,

                                     _HeightCalibration = None,
                                     
                                     _YBiasForViaMet12Met2OnPMOS2Output=None,_YBiasForViaMet12Met2OnPMOS3Output=None,_YBiasForViaMet12Met2OnNMOS2Output=None,_YBiasForViaMet12Met2OnNMOS3Output=None,
                                     _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None, _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None, _NumberOfPMOSConnectionCOY=None,
                                     _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,
                                     _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption=None,
                                     _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfNMOSOutputViaCOY=None, _NumberOfPMOSOutputViaCOY=None,
                                     _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                     _BiasDictforViaPoly2Met1OnGate = {
                                     '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None, '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None, '_XbiasNMOS3GateVia':None,
                                     '_YbiasNMOS3GateVia':None, '_XbiasNMOS4GateVia':None, '_YbiasNMOS4GateVia':None, '_XbiasInvNMOSGateVia':None, '_YbiasInvNMOSGateVia':None,
                                     '_XbiasPMOS1GateVia':None, '_YbiasPMOS1GateVia':None, '_XbiasPMOS2GateVia':None, '_YbiasPMOS2GateVia':None, '_XbiasPMOS3GateVia':None,
                                     '_YbiasPMOS3GateVia':None, '_XbiasPMOS4GateVia':None, '_YbiasPMOS4GateVia':None, '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                     },
                                     _MOS12MOS2spacebias=None, _MOS22InvMOSspacebias=None, _InvMOS2MOS3spacebias=None, _MOS32MOS4spacebias=None, _XYadjust=None,

                                     
                                     _InvNMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS1DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS2DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS3DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _NMOS4DesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                     _InvPMOSDesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
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
                                     _ViaMet12Met2OnNMOSOutputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnPMOSOutputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS1GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS2GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS3GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnMOS4GateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                     _ViaPoly2Met1OnInvMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),

                                     _Dummy=False
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  INV Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj=DRC.DRC()
        
        ok=0
        while True:
            # #####################SUBSET ELEMENTS GENERATION#########################
            ok += 1
            # INV_NMOS GENERATION
            # Mandatory User Input Parameter: _INVNumberOfGate, _INVChannelWidth, _INVChannelLength
            _InvNMOSDesignCalculationParameters['_NMOSNumberofGate']=_INVNumberOfGate
            _InvNMOSDesignCalculationParameters['_NMOSChannelWidth']=_INVChannelWidth
            _InvNMOSDesignCalculationParameters['_NMOSChannellength']=_INVChannelLength
            _InvNMOSDesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_InvNMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_InvNMOSDesignCalculationParameters)

            # PMOS GENERATION
            # Mandatory User Input Parameter: _INVPNChannelRatio
            _InvPMOSDesignCalculationParameters['_PMOSNumberofGate']=_INVNumberOfGate
            _InvPMOSDesignCalculationParameters['_PMOSChannelWidth']= round(_INVChannelWidth * _INVPNChannelRatio)
            _InvPMOSDesignCalculationParameters['_PMOSChannellength']=_INVChannelLength
            _InvPMOSDesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_InvPMOS']['_DesignObj']._CalculatePMOSDesignParameter(**_InvPMOSDesignCalculationParameters)

            # NMOS1 GENERATION
            # Mandatory User Input Parameter: _INVNumberOfGate, _INVChannelWidth, _INVChannelLength
            _NMOS1DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate1
            _NMOS1DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth1
            _NMOS1DesignCalculationParameters['_NMOSChannellength']=_ChannelLength1
            _NMOS1DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS1DesignCalculationParameters)

            # PMOS1 GENERATION
            # Mandatory User Input Parameter: _INVPNChannelRatio
            _PMOS1DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate1
            _PMOS1DesignCalculationParameters['_PMOSChannelWidth']=round(_ChannelWidth1 * _PNChannelRatio1)
            _PMOS1DesignCalculationParameters['_PMOSChannellength']=_ChannelLength1
            _PMOS1DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS1DesignCalculationParameters)

            # NMOS2 GENERATION
            # Mandatory User Input Parameter: _INVNumberOfGate, _INVChannelWidth, _INVChannelLength
            _NMOS2DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate2
            _NMOS2DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth2
            _NMOS2DesignCalculationParameters['_NMOSChannellength']=_ChannelLength2
            _NMOS2DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS2DesignCalculationParameters)

            # PMOS2 GENERATION
            # Mandatory User Input Parameter: _INVPNChannelRatio
            _PMOS2DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate2
            _PMOS2DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth2 * _PNChannelRatio2)
            _PMOS2DesignCalculationParameters['_PMOSChannellength']=_ChannelLength2
            _PMOS2DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS2DesignCalculationParameters)

            # NMOS3 GENERATION
            # Mandatory User Input Parameter: _INVNumberOfGate, _INVChannelWidth, _INVChannelLength
            _NMOS3DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate3
            _NMOS3DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth3
            _NMOS3DesignCalculationParameters['_NMOSChannellength']=_ChannelLength3
            _NMOS3DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS3DesignCalculationParameters)

            # PMOS3 GENERATION
            # Mandatory User Input Parameter: _INVPNChannelRatio
            _PMOS3DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate3
            _PMOS3DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth3 * _PNChannelRatio3)
            _PMOS3DesignCalculationParameters['_PMOSChannellength']=_ChannelLength3
            _PMOS3DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS3DesignCalculationParameters)

            # NMOS4 GENERATION
            # Mandatory User Input Parameter: _INVNumberOfGate, _INVChannelWidth, _INVChannelLength
            _NMOS4DesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate4
            _NMOS4DesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth4
            _NMOS4DesignCalculationParameters['_NMOSChannellength']=_ChannelLength4
            _NMOS4DesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOS4DesignCalculationParameters)

            # PMOS4 GENERATION
            # Mandatory User Input Parameter: _INVPNChannelRatio
            _PMOS4DesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate4
            _PMOS4DesignCalculationParameters['_PMOSChannelWidth']= round(_ChannelWidth4 * _PNChannelRatio4)
            _PMOS4DesignCalculationParameters['_PMOSChannellength']=_ChannelLength4
            _PMOS4DesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOS4DesignCalculationParameters)


            # VSS GENERATION
            # Mandatory User Input Parameter:
            
            if _NumberOfSupplyCOY is None :		# Default value is 1
                _NumberOfSupplyCOY = 1
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']=_NumberOfSupplyCOY
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOY']=_NumberOfSupplyCOY

            _tmpPbodyObj = PbodyContact._PbodyContact()
            _tmpPbodyObj._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOX=5, _NumberOfPbodyCOY=_PbodyDesignCalculationParameters['_NumberOfPbodyCOY'],_Met1YWidth = _XORSupplyMetal1YWidth)
            _tmpNbodyObj = NbodyContact._NbodyContact()
            _tmpNbodyObj._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOX=5, _NumberOfNbodyCOY=_NbodyDesignCalculationParameters['_NumberOfNbodyCOY'],_Met1YWidth = _XORSupplyMetal1YWidth)

            
                
                
            
            _PbodyDesignCalculationParameters['_Met1XWidth']=_XORSupplyMetal1XWidth
            _PbodyDesignCalculationParameters['_Met1YWidth']=_XORSupplyMetal1YWidth
            # self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)

            # VDD GENERATION
            # Mandatory User Input Parameter:
            _NbodyDesignCalculationParameters['_Met1XWidth']=_XORSupplyMetal1XWidth
            _NbodyDesignCalculationParameters['_Met1YWidth']=_XORSupplyMetal1YWidth
            # self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)


            # VIA GENERATION for PMOS (M1_M2)
            if _NumberOfPMOSConnectionViaCOY == None :
                _NumberOfPMOSConnectionViaCOY = 2
            if _NumberOfPMOSOutputViaCOY is None :
                _NumberOfPMOSOutputViaCOY = 2
            
            _ViaMet12Met2OnPMOSconnectionParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnPMOSconnectionParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfPMOSConnectionViaCOY
            _ViaMet22Met3OnPMOSconnectionParameters['_ViaMet22Met3NumberOfCOX']=1
            _ViaMet22Met3OnPMOSconnectionParameters['_ViaMet22Met3NumberOfCOY']=_NumberOfPMOSConnectionViaCOY
            _ViaMet12Met2OnPMOSOutputParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnPMOSOutputParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfPMOSOutputViaCOY

            self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnPMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnPMOSOutputParameters)


            # VIA GENERATION for NMOS (M1_M2)
            if _NumberOfNMOSConnectionViaCOY == None :
                _NumberOfNMOSConnectionViaCOY = 2
            if _NumberOfNMOSOutputViaCOY is None :
                _NumberOfNMOSOutputViaCOY = 2
            _ViaMet12Met2OnNMOSconnectionParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnNMOSconnectionParameters['_ViaMet12Met2NumberOfCOY']=_NumberOfNMOSConnectionViaCOY
            _ViaMet22Met3OnNMOSconnectionParameters['_ViaMet22Met3NumberOfCOX']=1
            _ViaMet22Met3OnNMOSconnectionParameters['_ViaMet22Met3NumberOfCOY']=_NumberOfNMOSConnectionViaCOY
            _ViaMet12Met2OnNMOSOutputParameters['_ViaMet12Met2NumberOfCOX']=1
            _ViaMet12Met2OnNMOSOutputParameters['_ViaMet12Met2NumberOfCOY']= _NumberOfNMOSOutputViaCOY
            self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnNMOSconnectionParameters)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnNMOSOutputParameters)

            
            # VIA GENERATION for GATE (POLY_M1)
            if _NumberOfMOS1GateViaCOX is None:
                _NumberOfMOS1GateViaCOX = 2
                if len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS1GateViaCOX = len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS1GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS1GateViaCOX
            _ViaPoly2Met1OnMOS1GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS1GateParameters)
            
            if _NumberOfMOS2GateViaCOX is None:
                _NumberOfMOS2GateViaCOX = 2
                if len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS2GateViaCOX = len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS2GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS2GateViaCOX
            _ViaPoly2Met1OnMOS2GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnMOS2Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS2GateParameters)
            
            if _NumberOfMOS3GateViaCOX is None:
                _NumberOfMOS3GateViaCOX = 2
                if len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS3GateViaCOX = len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS3GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS3GateViaCOX
            _ViaPoly2Met1OnMOS3GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS3GateParameters)
            
            if _NumberOfMOS4GateViaCOX is None:
                _NumberOfMOS4GateViaCOX = 2
                if len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS4GateViaCOX = len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnMOS4GateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOS4GateViaCOX
            _ViaPoly2Met1OnMOS4GateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOS4GateParameters)
            
            if _NumberOfInvMOSGateViaCOX is None:
                _NumberOfInvMOSGateViaCOX = 2
                if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfInvMOSGateViaCOX = len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
            _ViaPoly2Met1OnInvMOSGateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfInvMOSGateViaCOX
            _ViaPoly2Met1OnInvMOSGateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnInvMOSGateParameters)
            
            
            # )#####################COORDINATION SETTING#########################
            if _DistanceBtwSupplyCenter2MOSEdge == None:
                _DistanceBtwSupplyCenter2MOSEdge = (float) (_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']*1/2)
            
            if _HeightCalibration is None:
                _HeightCalibration = 0
            
            if _YbiasforEdgeBtwNWandPW==None and _YbiasforHeight==None :
                _YbiasforEdgeBtwNWandPW = 0
                _YbiasforHeight = 0
                


            if _HeightCalOption == 'ON':
                min_height = 0
                min_NWPW = 0
                
                for i in range(1,6) :
                    NMOS = '_NMOS' + str(i)
                    PMOS = '_PMOS' + str(i)
                    if i == 5:
                        NMOS = '_InvNMOS'
                        PMOS = '_InvPMOS'
                    height = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + 2 * _DistanceBtwSupplyCenter2MOSEdge
                    NWPW = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] +  _DistanceBtwSupplyCenter2MOSEdge
                    if min_height == 0 or min_height > height :
                        min_height = height
                    if min_NWPW < NWPW:
                        min_NWPW = NWPW
                _XORVdd2VssHeight = min_height + _YbiasforHeight
                _XOREdgeBtwNWandPW = min_NWPW + _YbiasforEdgeBtwNWandPW
            
            
            # _XORVdd2VssHeight += _HeightCalibration
            _tmpPbodyObj._DesignParameter['_XYCoordinates']=[[0,0]]
            _tmpNbodyObj._DesignParameter['_XYCoordinates']=[[0,_XORVdd2VssHeight + _HeightCalibration]]

            # NMOS, PMOS Coordinate Setting
            if _MOS12MOS2spacebias is None:
                _MOS12MOS2spacebias = 0
            if _MOS22InvMOSspacebias is None:
                _MOS22InvMOSspacebias = 0
            if _InvMOS2MOS3spacebias is None :
                _InvMOS2MOS3spacebias = 0
            if _MOS32MOS4spacebias is None :
                _MOS32MOS4spacebias = 0
            if _XYadjust is None:
                _XYadjust = 0
            
            self._DesignParameter['_InvNMOS']['_XYCoordinates']=[[_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_InvPMOS']['_XYCoordinates']=[[_XYadjust,(float)(_XORVdd2VssHeight + _HeightCalibration-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            # if _Dummy ==False:
            InvMOSspaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS1spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS2spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS3spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            MOS4spaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            
            
            if _Dummy is True:
                InvMOSPODummy = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS1PODummy = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS2PODummy = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS3PODummy = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
                MOS4PODummy = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]       
            
            tempX1 = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + max(InvMOSspaceDRC,MOS2spaceDRC) + _MOS22InvMOSspacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = InvMOSPODummy + MOS2PODummy + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS22InvMOSspacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS2']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS2']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_XORVdd2VssHeight + _HeightCalibration-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            tempX1 = tempX +  self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 +max(MOS1spaceDRC,MOS2spaceDRC) + _MOS12MOS2spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = tempX + MOS1PODummy + MOS2PODummy + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS12MOS2spacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS1']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS1']['_XYCoordinates']=[[-tempX+_XYadjust,(float)(_XORVdd2VssHeight + _HeightCalibration-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            tempX1 = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 +max(MOS3spaceDRC,InvMOSspaceDRC) + _InvMOS2MOS3spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = InvMOSPODummy + MOS3PODummy + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 +  max(_DRCObj._PolygateMinSpace,_DRCObj._PolygateMinSpaceAtCorner) + _InvMOS2MOS3spacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS3']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS3']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_XORVdd2VssHeight + _HeightCalibration-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            
            tempX1 = tempX +  self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']*1/2 +max(MOS3spaceDRC,MOS4spaceDRC) +_MOS32MOS4spacebias
            tempX2 = 0
            if _Dummy is True:
                tempX2 = tempX + MOS3PODummy + MOS4PODummy + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*1/2 + _DRCObj._PolygateMinSpace + _MOS32MOS4spacebias
            tempX = max(tempX1,tempX2)
            self._DesignParameter['_NMOS4']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']*1/2)]]
            self._DesignParameter['_PMOS4']['_XYCoordinates']=[[tempX+_XYadjust,(float)(_XORVdd2VssHeight + _HeightCalibration-_DistanceBtwSupplyCenter2MOSEdge-self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']*1/2)]]

            # )################################ MOS CONNECTION ################################
            # )######PUT VIA FOR CONNECTION (M1_M2, M2_M3)		
            tmpP = []
            tmpN = []
            stack = 0
            for i in range (1,6):
                PMOS = '_PMOS' + str(i)
                NMOS = '_NMOS' + str(i)
                if i == 5:
                    PMOS = '_InvPMOS'
                    NMOS = '_InvNMOS'
                    if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) == 1:   # Via isn't necessary
                        break
                    
                YbiasP = float(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2
                YbiasN = float(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2

                if i == 1 or i == 4:
                    for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                        tmpP.append( [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                        tmpP[stack][1] += YbiasP
                        tmpN.append( [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                        tmpN[stack][1] -= YbiasN
                        stack += 1
                elif i == 2 or i == 3 or i == 5:
                    for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                        tmpP.append( [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ])
                        tmpP[stack][1] += YbiasP
                        tmpN.append( [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ])
                        tmpN[stack][1] -= YbiasN
                        stack += 1

            self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'] = tmpP
            self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'] = tmpP

            self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'] = tmpN
            self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'] = tmpN

            # )######CONNECTION ROUTING  (Metal3)
            tmpP = []
            tmpN = []
            for i in range(0,len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])+len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])-1):
                tmpP.append([self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i + 1]])
                # min_height = min(tmpP[i][0][1] , tmpP[i][1][1])
                tmpN.append([self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i + 1]])
                j=i
            for i in range(j+2,j+len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])+len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])+1):
                tmpP.append([self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i + 1]])
                tmpN.append([self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i + 1]])
                k=i
            for i in range(k+2,k+len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])+1):
                tmpP.append([self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][i + 1]])
                tmpN.append([self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][i + 1]])
            self._DesignParameter['_PMOSConnectionRouting']['_XYCoordinates']= tmpP
            self._DesignParameter['_PMOSConnectionRouting']['_Width']= self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
            self._DesignParameter['_NMOSConnectionRouting']['_XYCoordinates']= tmpN
            self._DesignParameter['_NMOSConnectionRouting']['_Width']= self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']


            # )################################ Output Routing ################################
            # )######PUT VIA ON PMOS FOR OUTPUT
            if _YBiasForViaMet12Met2OnPMOS2Output == None :
                _YBiasForViaMet12Met2OnPMOS2Output = 0
            if _YBiasForViaMet12Met2OnPMOS3Output == None :
                _YBiasForViaMet12Met2OnPMOS3Output = 0
            if _YBiasForViaMet12Met2OnNMOS2Output == None :
                _YBiasForViaMet12Met2OnNMOS2Output = 0
            if _YBiasForViaMet12Met2OnNMOS3Output == None :
                _YBiasForViaMet12Met2OnNMOS3Output = 0   
            tmp = []
            Yadjusting = -float(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasForViaMet12Met2OnPMOS2Output
            WidthDifference = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if WidthDifference > 0:
                Yadjusting -= int(WidthDifference/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            
            for i in range(0,len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmp.append( [a+b for a, b in zip(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_PMOS2']['_XYCoordinates'][0]) ])
                tmp[i][1] += Yadjusting
            
            tmp2 = []
            Yadjusting = -float(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 + _YBiasForViaMet12Met2OnPMOS3Output
            WidthDifference = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if WidthDifference > 0:
                Yadjusting -= int(WidthDifference/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            for i in range(0, len(self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmp2.append([a + b for a, b in zip( self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i], self._DesignParameter['_PMOS3']['_XYCoordinates'][0])])
                tmp2[i][1] += Yadjusting
                tmp.append(tmp2[i])
 
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmp

            # )######PUT VIA ON NMOS FOR OUTPUT
            tmp = []
            Yadjusting = float(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasForViaMet12Met2OnNMOS2Output
            WidthDifference = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if WidthDifference > 0:
                Yadjusting += int(WidthDifference/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            for i in range(0,len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmp.append( [a+b for a, b in zip(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i] , self._DesignParameter['_NMOS2']['_XYCoordinates'][0]) ])
                tmp[i][1] += Yadjusting
            tmp2 = []
            Yadjusting = float(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2 + _YBiasForViaMet12Met2OnNMOS2Output
            WidthDifference = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            if WidthDifference > 0:
                Yadjusting += int(WidthDifference/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            for i in range(0, len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmp2.append([a + b for a, b in zip( self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i], self._DesignParameter['_NMOS3']['_XYCoordinates'][0])])
                tmp2[i][1] += Yadjusting
                tmp.append(tmp2[i])

            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmp

            # )###### OUTPUT ROUTING1 (M2) - Horizontal
            tmp = []
            if _YBiasOfOutputRouting1 == None and _YBiasOfOutputRouting2 == None:
                _YBiasOfOutputRouting1 = 0
                _YBiasOfOutputRouting2 = 0
            if _OutputMet2Width is None:
                _OutputMet2Width = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                
            for i in range(0,len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'])-1):
                tmp.append([copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i]),copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i+1]) ])
                if i in range(0,len(self._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                    tmp[i][0][1] -= _YBiasOfOutputRouting1
                    tmp[i][1][1] -= _YBiasOfOutputRouting1
                else :
                    tmp[i][0][1] -= _YBiasOfOutputRouting2
                    tmp[i][1][1] -= _YBiasOfOutputRouting2
                minvalue = min(tmp[i][0][1],tmp[i][1][1])
                tmp[i][0][1] = minvalue
                tmp[i][1][1] = minvalue
            self._DesignParameter['_OutputRouting']['_XYCoordinates']= tmp
            self._DesignParameter['_OutputRouting']['_Width']= _OutputMet2Width#self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']


            # self._DesignParameter['_OutputRouting2']['_XYCoordinates']= tmp
            # self._DesignParameter['_OutputRouting2']['_Width']= self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            # )###### OUTPUT ROUTING1 (M2) - Vertical
            tmp = []
            # print 'eeee' , len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) , len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])
            # print len(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates']), len(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'])
            for i in range(0,len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) + len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][i],self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i]])


            self._DesignParameter['_OutputRouting2']['_XYCoordinates']= tmp
            self._DesignParameter['_OutputRouting2']['_Width']= self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']



            # )################################ VSS METAL1 ROUTING )################################
            tmp = []
            for i in range(0,len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i],self._DesignParameter['_InvNMOS']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_NMOS1']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,0 - _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_NMOS4']['_XYCoordinates'][0])] ])

            self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates']=tmp
            self._DesignParameter['_NMOSSupplyRouting']['_Width']= self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']



            # )################################ VDD METAL1 ROUTING )################################
            tmp = []
            for i in range(0,len(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,_XORVdd2VssHeight + _HeightCalibration + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,  [a+b for a , b in zip(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i],self._DesignParameter['_InvPMOS']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,_XORVdd2VssHeight + _HeightCalibration + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_PMOS1']['_XYCoordinates'][0])] ])
            for i in range(0,len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tempX = self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0]
                tmp.append([ [tempX,_XORVdd2VssHeight + _HeightCalibration + _tmpNbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2]
                          ,[ a+b for a , b in zip(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i],self._DesignParameter['_PMOS4']['_XYCoordinates'][0])] ])

            self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates']=tmp
            self._DesignParameter['_PMOSSupplyRouting']['_Width']= self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']




            # )################################ ADDITIONAL METAL1 ROUTING )################################
            tmpP = []
            tmpN = []
            
            
            k = 0
            for i in range (1 , 5): # For ith CMOS's Additional Metal1 Routing
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                YbiasP = float(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
                YbiasN = float(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
                
                addMetLen = 2 * YbiasN
                if self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * addMetLen < _DRCObj._Metal1MinArea:
                    addMetLen = round( _DRCObj._Metal1MinArea/self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                
                for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                    tmpP.append( [[a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ],
                                 [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ]])
                    tmpP[k+j][0][1] += YbiasP
                    tmpP[k+j][1][1] -= YbiasP
                    tmpN.append( [[a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ],
                                 [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ]])
                    tmpN[k + j][0][1] += (addMetLen - YbiasN)
                    tmpN[k+j][1][1] -= YbiasN
                k += j + 1
                
                if i == 2 or i == 3:    # CMOS which locates inside
                    for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                        tmpP.append( [[a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ],
                                     [a+b for a, b in zip(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[PMOS]['_XYCoordinates'][0]) ]])
                        tmpP[k+j][0][1] += YbiasP
                        tmpP[k+j][1][1] -= YbiasP
                        
                        # tmpN.append( [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0] 
                                     # ,[a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ]])
                        tmpN.append( [[a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ],
                                     [a+b for a, b in zip(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter[NMOS]['_XYCoordinates'][0]) ]])
                        tmpN[k+j][0][1] += (addMetLen - YbiasN)
                        tmpN[k+j][1][1] -= YbiasN
                    k += j + 1
            
            if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) != 1:   # Whene Vias are on Inverter, Routes additional Metal
                YbiasP = float(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
                YbiasN = float(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
                addMetLen = 2 * YbiasN
                if self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] * addMetLen < _DRCObj._Metal1MinArea:
                    addMetLen = round( _DRCObj._Metal1MinArea/self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                for j in range(0,len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                    tmpP.append( [[a+b for a, b in zip(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter['_InvPMOS']['_XYCoordinates'][0]) ],
                                 [a+b for a, b in zip(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter['_InvPMOS']['_XYCoordinates'][0]) ]])
                    tmpP[k+j][0][1] += YbiasP
                    tmpP[k+j][1][1] -= YbiasP
                    tmpN.append( [[a+b for a, b in zip(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter['_InvNMOS']['_XYCoordinates'][0]) ],
                                 [a+b for a, b in zip(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j] , self._DesignParameter['_InvNMOS']['_XYCoordinates'][0]) ]])
                    tmpN[k + j][0][1] += (addMetLen - YbiasN)
                    tmpN[k+j][1][1] -= YbiasN
            
            self._DesignParameter['_AdditionalMet1OnPMOS']['_XYCoordinates'] = tmpP
            self._DesignParameter['_AdditionalMet1OnPMOS']['_Width'] = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet1OnNMOS']['_XYCoordinates'] = tmpN
            self._DesignParameter['_AdditionalMet1OnNMOS']['_Width'] = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']    
                
             # )################################ ADDITIONAL METAL2 ROUTING )################################
            XWidth = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            
            YWidth = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
            if XWidth * YWidth < _DRCObj._MetalxMinArea :
                while XWidth * self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
                    XWidth += _DRCObj._MinSnapSpacing 
                self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = XWidth
            XWidth = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            YWidth = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
            if XWidth * YWidth < _DRCObj._MetalxMinArea :
                while XWidth * self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
                    XWidth += _DRCObj._MinSnapSpacing 
                self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = XWidth
            

            
            
            # )################################ GATE CONNECTION ################################
            # self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']=self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            # self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            tmpN=[]
            tmpP=[]
            for i in range (1 , 5):     # For ith CMOS's Gate Routing
                NMOS = '_NMOS'+ str(i)
                PMOS = '_PMOS'+ str(i)
                heightN = self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 - self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2
                heightP = self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 + self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2
                tmpN.append([ [min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter[NMOS]['_XYCoordinates'][0][0] ,heightN]
                             ,[max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter[NMOS]['_XYCoordinates'][0][0] ,heightN] ])
                tmpP.append([ [min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter[PMOS]['_XYCoordinates'][0][0] ,heightP]
                             ,[max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter[PMOS]['_XYCoordinates'][0][0] ,heightP] ])
            heightN = self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 - self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2
            heightP = self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 + self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2
            tmpN.append([ [min(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] ,heightN]
                         ,[max(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] ,heightN] ])
            tmpP.append([ [min(zip(*self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0] ,heightP]
                         ,[max(zip(*self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) +self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0] ,heightP] ])
            _AdditionalPolyOnNMOSXY = copy.deepcopy(tmpN)
            _AdditionalPolyOnPMOSXY = copy.deepcopy(tmpP)
            # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates']=tmpN
            # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates']=tmpP
                
                #Connect INV Gate and MOS3 Gate   -- when dummy is false
            # if _Dummy is not True:
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append([self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'][2][0],self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'][4][1]])
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'][2][0],self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'][4][1]])
            # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append()
                
              



            #NEW GATE ROUTING


            for i in range (1,6):
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                Poly2Met1Via = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate' 
                NGateRouting = '_GateRoutingOnNMOS' + str(i)
                PGateRouting = '_GateRoutingOnPMOS' + str(i)
                Nbias = '_YbiasNMOS' + str(i) + 'GateVia'
                Pbias = '_YbiasPMOS' + str(i) + 'GateVia'
                
                if i is 5:
                    NMOS = '_InvNMOS'
                    PMOS = '_InvPMOS'
                    Poly2Met1Via = '_ViaPoly2Met1OnInvMOSGate'
                    NGateRouting = '_GateRoutingOnInvNMOS' 
                    PGateRouting = '_GateRoutingOnInvPMOS' 
                    Nbias = '_YbiasInvNMOSGateVia'
                    Pbias = '_YbiasInvPMOSGateVia'
                
                
        
                if _BiasDictforViaPoly2Met1OnGate[Nbias] is None:
                    _BiasDictforViaPoly2Met1OnGate[Nbias] = 0
                if _BiasDictforViaPoly2Met1OnGate[Pbias] is None:
                    _BiasDictforViaPoly2Met1OnGate[Pbias] = 0
        
                N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS = _DRCObj.DRCMETAL1MinSpace(_Width=self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] , _ParallelLength=self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                N_tmpDRCMet1MinSpaceByViaPoly2Met1 = _DRCObj.DRCMETAL1MinSpace(_Width= self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength= self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                _tmpDRCMinSpacePoly2OD = _DRCObj._PolygateMinSpace2OD             

                P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS = _DRCObj.DRCMETAL1MinSpace(_Width=self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength=self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                P_tmpDRCMet1MinSpaceByViaPoly2Met1 = _DRCObj.DRCMETAL1MinSpace(_Width= self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength= self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])

                # print 'monitor for debug: ', _BiasDictforViaPoly2Met1OnGate[Nbias], Nbias
                # print _BiasDictforViaPoly2Met1OnGate
                # print 'lets' 
                # print  self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates']
                # print 'end'
                
                if i == 2 or i == 3:
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                            [
                                [
                                    self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                    max(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][0][1] 
                                        + round(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                        self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1] 
                                        + round(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                        self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])  
                                    + round(self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                                    + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                ]
                            ]
                    self._DesignParameter[NGateRouting]['_XWidth']=(max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                    self._DesignParameter[NGateRouting]['_YWidth']=self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
                    
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        min(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][0][1] 
                                            - round(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                            self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][1] 
                                            - round(self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                            self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                        - round(self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                                        - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                                    ]
                                ]
                else :
                    self._DesignParameter[NGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        max(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][0][1] 
                                            + round(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                            self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[NMOS]['_XYCoordinates'][0][1])  
                                        + round(self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                                        + max([N_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,N_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Nbias]
                                    ]
                                ]
                    self._DesignParameter[NGateRouting]['_XWidth']=(max(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                    self._DesignParameter[NGateRouting]['_YWidth']=self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
                    
                    
                    
                    self._DesignParameter[PGateRouting]['_XYCoordinates']=\
                                [
                                    [
                                        self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                        min(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][0][1] 
                                            - round(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing,
                                            self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )  
                                        - round(self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                                        - max([P_tmpDRCPolyMinSpaceByAdditionalMet1OnPMOS,P_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate[Pbias]
                                    ]
                                ]
        
                self._DesignParameter[PGateRouting]['_XWidth']=(max(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                self._DesignParameter[PGateRouting]['_YWidth']=self._DesignParameter[Poly2Met1Via]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

                self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) ):
                    self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append([ [a + b for a , b in zip( self._DesignParameter[NMOS]['_XYCoordinates'][0],self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j])]
                                                                                            , [self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0], self._DesignParameter[NGateRouting]['_XYCoordinates'][0][1]]          ])
                self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                for j in range(0,len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) ):
                    self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([ [a + b for a , b in zip( self._DesignParameter[PMOS]['_XYCoordinates'][0],self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j])]
                                                                                            , [self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0], self._DesignParameter[PGateRouting]['_XYCoordinates'][0][1]]          ])    
            
                    # if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                        # tmp=[]
                        # tmp= [self._DesignParameter[NMOS]['_XYCoordinates'][0], self._DesignParameter[VIA]['_XYCoordinates'][0] ] 
                        # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append(tmp)
             
             
             
             

             
                
            # _XbiasNMOS1GateVia=None, _YbiasNMOS1GateVia=None, _XbiasNMOS2GateVia=None, _YbiasNMOS2GateVia=None, _XbiasNMOS3GateVia=None, _YbiasNMOS3GateVia=None, _XbiasNMOS4GateVia=None, _YbiasNMOS4GateVia=None, _XbiasInvNMOSGateVia=None, _YbiasInvNMOSGateVia=None,
            # _XbiasPMOS1GateVia=None, _YbiasPMOS1GateVia=None, _XbiasPMOS2GateVia=None, _YbiasPMOS2GateVia=None, _XbiasPMOS3GateVia=None, _YbiasPMOS3GateVia=None, _XbiasPMOS4GateVia=None, _YbiasPMOS4GateVia=None, _XbiasInvPMOSGateVia=None, _YbiasInvPMOSGateVia=None,    
            # )######PUT VIA FOR Gate (PO_M1)
            
            #Bias setting
            for i in range(1,6):
                XbiasN = '_XbiasNMOS'+str(i)+ 'GateVia'
                XbiasP = '_XbiasPMOS'+str(i)+ 'GateVia'
                YbiasN = '_YbiasNMOS'+str(i)+ 'GateVia'
                YbiasP = '_YbiasPMOS'+str(i)+ 'GateVia'
                
                
                if i == 5:
                    XbiasN = '_XbiasInvNMOSGateVia'
                    XbiasP = '_XbiasInvPMOSGateVia'
                    YbiasN = '_YbiasInvNMOSGateVia'
                    YbiasP = '_YbiasInvPMOSGateVia'
                if _BiasDictforViaPoly2Met1OnGate[XbiasN] is None:
                    _BiasDictforViaPoly2Met1OnGate[XbiasN] = 0
                if _BiasDictforViaPoly2Met1OnGate[XbiasP] is None:
                    _BiasDictforViaPoly2Met1OnGate[XbiasP] = 0
                if _BiasDictforViaPoly2Met1OnGate[YbiasN] is None:
                    _BiasDictforViaPoly2Met1OnGate[YbiasN] = 0
                if _BiasDictforViaPoly2Met1OnGate[YbiasP] is None:
                    _BiasDictforViaPoly2Met1OnGate[YbiasP] = 0
            
            if _XBiasOfViaPoly2Met1OnInvMOSGateN is None:
                _XBiasOfViaPoly2Met1OnInvMOSGateN = 0
            if _XBiasOfViaPoly2Met1OnInvMOSGateP is None:
                _XBiasOfViaPoly2Met1OnInvMOSGateP = 0
            
            for i in range (1 , 6):
                VIA = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate'
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                XBiasofN = '_XbiasNMOS' + str(i) + 'GateVia'
                YBiasofN = '_YbiasNMOS' + str(i) + 'GateVia'
                XBiasofP = '_XbiasPMOS' + str(i) + 'GateVia'
                YBiasofP = '_YbiasPMOS' + str(i) + 'GateVia'
                NGateRouting = '_GateRoutingOnNMOS' + str(i)
                PGateRouting = '_GateRoutingOnPMOS' + str(i)
                if i == 5:
                    VIA = '_ViaPoly2Met1OnInvMOSGate'
                    NMOS = '_InvNMOS'
                    PMOS = '_InvPMOS'
                    XBiasofN = '_XbiasInvNMOSGateVia'
                    YBiasofN = '_YbiasInvNMOSGateVia'
                    XBiasofP = '_XbiasInvPMOSGateVia'
                    YBiasofP = '_YbiasInvPMOSGateVia'
                    NGateRouting = '_GateRoutingOnInvNMOS' 
                    PGateRouting = '_GateRoutingOnInvPMOS'
                    # self._DesignParameter[VIA]['_XYCoordinates'] = [[ (float)(tmpN[i-1][0][0]+tmpN[i-1][1][0])/2+_XBiasOfViaPoly2Met1OnInvMOSGateN,tmpN[i-1][0][1] ]]         #NMOS Gate Via
                    # self._DesignParameter[VIA]['_XYCoordinates'].append([ (float)(tmpP[i-1][0][0]+tmpP[i-1][1][0])/2+_XBiasOfViaPoly2Met1OnInvMOSGateP,tmpP[i-1][0][1]  ])     #PMOS Gate Via
                # else :
                    # self._DesignParameter[VIA]['_XYCoordinates'] = [[ (float)(tmpN[i-1][0][0]+tmpN[i-1][1][0])/2  ,tmpN[i-1][0][1]  ]]         #NMOS Gate Via
                    # self._DesignParameter[VIA]['_XYCoordinates'].append([ (float)(tmpP[i-1][0][0]+tmpP[i-1][1][0])/2 ,tmpP[i-1][0][1]  ])     #PMOS Gate Via
                self._DesignParameter[VIA]['_XYCoordinates'] = [[ self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofN]
                                                              ,self._DesignParameter[NGateRouting]['_XYCoordinates'][0][1] ]]#+ _BiasDictforViaPoly2Met1OnGate[YBiasofN] ]]         #NMOS Gate Via
                self._DesignParameter[VIA]['_XYCoordinates'].append([ self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + _BiasDictforViaPoly2Met1OnGate[XBiasofP] 
                                                              ,self._DesignParameter[PGateRouting]['_XYCoordinates'][0][1] ])#+ _BiasDictforViaPoly2Met1OnGate[YBiasofP] ])         #PMOS Gate Via

                #Additional Poly for preparing when X bias is huge.
                AdditionalPolyOnNMOS = '_AdditionalGatePolyOn' + NMOS
                AdditionalPolyOnPMOS = '_AdditionalGatePolyOn' + PMOS
                self._DesignParameter[AdditionalPolyOnNMOS]['_XWidth'] = self._DesignParameter[NGateRouting]['_YWidth']
                self._DesignParameter[AdditionalPolyOnNMOS]['_XYCoordinates'] = [[ self._DesignParameter[VIA]['_XYCoordinates'][0],self._DesignParameter[NGateRouting]['_XYCoordinates'][0]    ]]
                self._DesignParameter[AdditionalPolyOnPMOS]['_XWidth'] = self._DesignParameter[PGateRouting]['_YWidth']
                self._DesignParameter[AdditionalPolyOnPMOS]['_XYCoordinates'] = [[ self._DesignParameter[VIA]['_XYCoordinates'][1],self._DesignParameter[PGateRouting]['_XYCoordinates'][0]    ]]
                
                                                              
                                                              
                # YaxisN = self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._Metal1MinSpace 
                # YaxisP = self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - _DRCObj._Metal1MinSpace 
                # if i == 2 :
                    # YaxisP2 = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - _DRCObj._Metal1MinSpace
                    # if YaxisP > YaxisP2:
                        # YaxisP = YaxisP2
                # elif i == 3 :       
                    # YaxisP2 = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][-1][1] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - _DRCObj._Metal1MinSpace
                    # if YaxisP > YaxisP2:
                        # YaxisP = YaxisP2

                # self._DesignParameter[VIA]['_XYCoordinates'][0][1] = YaxisN
                # self._DesignParameter[VIA]['_XYCoordinates'][1][1] = YaxisP
                
                # self._DesignParameter[VIA]['_XYCoordinates'][0][0] += _BiasDictforViaPoly2Met1OnGate[XBiasofN]
                # self._DesignParameter[VIA]['_XYCoordinates'][0][1] += _BiasDictforViaPoly2Met1OnGate[YBiasofN]
                # self._DesignParameter[VIA]['_XYCoordinates'][1][0] += _BiasDictforViaPoly2Met1OnGate[XBiasofP]
                # self._DesignParameter[VIA]['_XYCoordinates'][1][1] += _BiasDictforViaPoly2Met1OnGate[YBiasofP]

            
            ###I am not sure wheter this code is necessary or not (Additional Poly btw ViaPoly2Met1OnInvMOSGateIn and INV Poly gate)### --> Gate Connection BTW INV and MOS3 with Poly is alternative
            # if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) < 3 :
                # tmpN=[]
                # tmpP=[]
                # tmpN.append([[a + b for a , b in zip(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0],self._DesignParameter['_InvNMOS']['_XYCoordinates'][0])]
                            # ,[self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0],\
                            # (float) (self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 )] ])
                # tmpP.append([[a + b for a , b in zip(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0],self._DesignParameter['_InvPMOS']['_XYCoordinates'][0])]
                            # ,[self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0],\
                            # (float) (self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 )] ])
                # _AdditionalPolyOnNMOSXY.append(tmpN[0])
                # _AdditionalPolyOnPMOSXY.append(tmpP[0])
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates']=_AdditionalPolyOnNMOSXY
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates']=_AdditionalPolyOnPMOSXY
            #
            
            
            # )######PUT VIA FOR Gate (M1_M2)
            # if _YbiasforViaMet12Met2OnNMOSGate1 == None:
                # _YbiasforViaMet12Met2OnNMOSGate1=0
                # _YbiasforViaMet12Met2OnNMOSGate4=0
                # _YbiasforViaMet12Met2OnPMOSGate1=0
                # _YbiasforViaMet12Met2OnPMOSGate4=0
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates']=[copy.deepcopy(self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0])]
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates'].append(copy.deepcopy(self._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0]))
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates'][0][0] += float(-self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates'][1][0] += float(self._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates'][0][1] += _YbiasforViaMet12Met2OnNMOSGate1
            # self._DesignParameter['_ViaMet12Met2OnNMOSGate']['_XYCoordinates'][1][1] += _YbiasforViaMet12Met2OnNMOSGate4
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates']=[copy.deepcopy(self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1])]
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates'].append(copy.deepcopy(self._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1]))
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates'][0][0] += float(self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates'][1][0] += float(-self._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates'][0][1] -= _YbiasforViaMet12Met2OnPMOSGate1
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_XYCoordinates'][1][1] -= _YbiasforViaMet12Met2OnPMOSGate4
            # self._DesignParameter['_ViaMet12Met2OnPMOSGate']['_DesignObj']
                       
            
            Right_Side = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            Left_Side = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            NMOS_NPlength = Right_Side - Left_Side
            # NMOS_NPlength = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2 - self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            
            # )################################ NWELL ################################
            # self._DesignParameter['_NWell']['_XWidth']= self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth'] + _DRCObj._NwMinEnclosurePactive*2
            # self._DesignParameter['_NWell']['_XWidth']= round( (abs(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) + abs(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 ) *2* _DRCObj._MinSnapSpacing + _DRCObj._NwMinEnclosurePactive*2
            # self._DesignParameter['_NWell']['_YWidth']= _XORVdd2VssHeight + _HeightCalibration - _XOREdgeBtwNWandPW + (float (self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            # self._DesignParameter['_NWell']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _XOREdgeBtwNWandPW ]]
            self._DesignParameter['_NWell']['_XWidth']= round((NMOS_NPlength + _DRCObj._NwMinEnclosurePactive*2)/2/_DRCObj._MinSnapSpacing) * 2 * _DRCObj._MinSnapSpacing
            self._DesignParameter['_NWell']['_YWidth']= _XORVdd2VssHeight + _HeightCalibration - _XOREdgeBtwNWandPW + (float (_tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            self._DesignParameter['_NWell']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _XOREdgeBtwNWandPW ]]
            # )################################ NP UnderNMOS )################################
            tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][1]]]
            tmp[0][1] = tmp[0][1] + (float)(_XOREdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2)/2 -self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            self._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'] = tmp
            # self._DesignParameter['_NIMPUnderNMOS']['_XWidth']= round( (abs(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) + abs(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            self._DesignParameter['_NIMPUnderNMOS']['_XWidth'] = NMOS_NPlength
            self._DesignParameter['_NIMPUnderNMOS']['_YWidth']= _XOREdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2
            # )################################ PP UnderNMOS )################################
            # self._DesignParameter['_PIMPUnderPMOS']['_XWidth']= round( (abs(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) + abs(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            self._DesignParameter['_PIMPUnderPMOS']['_XWidth'] = NMOS_NPlength
            self._DesignParameter['_PIMPUnderPMOS']['_YWidth']=  _XORVdd2VssHeight + _HeightCalibration - _XOREdgeBtwNWandPW - _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2
            tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][1]]]
            tmp[0][1] = tmp[0][1] - ((self._DesignParameter['_PIMPUnderPMOS']['_YWidth'])/2 - self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)
            self._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'] = tmp
           
           
           
            # )################################ INV METAL For DATA ################################
            if _InputRouting is None:
                _InputRouting = True
            if _InputRouting is True:
                # # checkForadditionalInputDataBarRouting2 = 0
                # # print  self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0]
                # # print       float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 )
                # # print                                                            [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 ),         self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ]
                # print         [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 ) ,self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1]  ]
                # # print                                                                      self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1]
                
                # _WidthCalibration = float(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._Metal1MinWidth/2)
                # _InputDataRoutingWidth = _DRCObj._Metal1MinWidth
                # while _WidthCalibration < _Metal1MinSpace
                    # _InputDataRoutingWidth += _DRCObj._MinSnapSpacing
                    # _WidthCalibration += _DRCObj._MinSnapSpacing
                
                self._DesignParameter['_InputDataRouting1']['_Width']= _DRCObj._Metal1MinWidth   #_InputDataRoutingWidth#

                if self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] > self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1] : #NMOS Gate Via heigth comparision
                    self._DesignParameter['_InputDataRouting1']['_XYCoordinates'] = [[ self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0] ,
                                                                                     [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 )
                                                                                     ,self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ],
                                                                                     [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 )
                                                                                     ,self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1] ]  ]]
                                                                                         
                    checkForadditionalInputDataBarRouting2 = 1
                else :
                    self._DesignParameter['_InputDataRouting1']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0],self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1]],self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0]]]
                
                if self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1] >= self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1] : #PMOS Gate Via heigth comparision
                    
                    self._DesignParameter['_InputDataRouting1']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0],self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1]],self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1]])
                         
                else :
                    # self._DesignParameter['_InputDataRouting1']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1]])
                    self._DesignParameter['_InputDataRouting1']['_XYCoordinates'].append([ self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1] ,
                                                                                     [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 )
                                                                                     ,self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1] ],
                                                                                     [float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][0]-self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+ self._DesignParameter['_InputDataRouting1']['_Width']/2 )
                                                                                     ,self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1] ]  ])
                    
                self._DesignParameter['_InputDataRouting2']['_Width']= _DRCObj._Metal1MinWidth
                self._DesignParameter['_InputDataRouting2']['_XYCoordinates'] = [[self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1]]]
                # left_end = min(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2\
                              # ,self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
                
                # self._DesignParameter['_InputDataRouting2']['_XYCoordinates'] = [[ [left_end + self._DesignParameter['_InputDataRouting2']['_Width']/2 ,self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ] \
                                                                                  # ,[left_end + self._DesignParameter['_InputDataRouting2']['_Width']/2 ,self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1] ]] ]
                
                
                # if checkForadditionalInputDataBarRouting2 == 1:
                # self._DesignParameter['_InputDataRouting2']['_XYCoordinates'].append([self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0],self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1]] )
                #DataBar Routing 2 append
                    
            
                
            # )################################ INV METAL For DATA_Bar ################################
            self._DesignParameter['_DataBarRouting1']['_Width']= _DRCObj._Metal1MinWidth
            self._DesignParameter['_DataBarRouting1']['_XYCoordinates'] = [[self._DesignParameter['_ViaPoly2Met1OnMOS2Gate']['_XYCoordinates'][0]
                                                                           ,[self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0]+ self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0],self._DesignParameter['_ViaPoly2Met1OnMOS2Gate']['_XYCoordinates'][0][1]]  ]]
            self._DesignParameter['_DataBarRouting1']['_XYCoordinates'].append([self._DesignParameter['_ViaPoly2Met1OnMOS2Gate']['_XYCoordinates'][1]
                                                                               ,[self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0]+ self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0],self._DesignParameter['_ViaPoly2Met1OnMOS2Gate']['_XYCoordinates'][1][1]]           ])
            self._DesignParameter['_DataBarRouting2']['_Width']=self._DesignParameter['_AdditionalMet1OnPMOS']['_Width'] 
            self._DesignParameter['_DataBarRouting2']['_XYCoordinates'] = [[[a + b for a, b in zip(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0] ,self._DesignParameter['_InvNMOS']['_XYCoordinates'][0])] ,
                                                                           [a + b for a ,b in zip(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0] ,self._DesignParameter['_InvPMOS']['_XYCoordinates'][0])] ]]
            # )################################ Additional Metal2 for VOID ################################
            # _VoidWidthP = self._DesignParameter['_InputDataRouting1']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingNE']['_Width']/2 - self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            # _VoidWidthN = -self._DesignParameter['_InputDataRouting1']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingSE']['_Width']/2 + self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            
            # pathWidthP = round(_VoidWidthP/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # pathWidthN = round(_VoidWidthN/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # if float(int(pathWidthP/_DRCObj._MinSnapSpacing)) is not float(pathWidthP/_DRCObj._MinSnapSpacing):
                # pathWidthP += _DRCObj._MinSnapSpacing
            # if float(int(pathWidthN/_DRCObj._MinSnapSpacing)) is not float(pathWidthN/_DRCObj._MinSnapSpacing):
                # pathWidthN += _DRCObj._MinSnapSpacing

            # if 0 < _VoidWidthP and _VoidWidthP < _DRCObj._MetalxMinSpace:
                # _tempYforP = round( (self._DesignParameter['_OutputRoutingNE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRoutingNE']['_Width']/2  + self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet2OnPMOS_for_void']['_Width'] = pathWidthP
                # self._DesignParameter['_AdditionalMet2OnPMOS_for_void']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0]- self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2, _tempYforP]
                                                                                             # ,[self._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0],  _tempYforP  ] ]]
            # if 0 < _VoidWidthN and _VoidWidthN < _DRCObj._MetalxMinSpace:
                # _tempYforN = round( (self._DesignParameter['_OutputRoutingSE']['_XYCoordinates'][0][0][1] + self._DesignParameter['_OutputRoutingSE']['_Width']/2  + self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 )/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet2OnNMOS_for_void']['_Width'] = pathWidthN
                # self._DesignParameter['_AdditionalMet2OnNMOS_for_void']['_XYCoordinates'] = [[ [self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0]- self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2, _tempYforN]
                                                                                             # ,[self._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0],  _tempYforN  ] ]]
            

            
            
            
            
            # )################################ DRC Verification ################################
            DRC_PASS=1
            
            temp_num = len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])-1
            temp_num2 = len(self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])-1
            temp_num3 = len(self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + len(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) +1
            
            _DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1Y = float(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][temp_num][1] - self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2\
                                                                    - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2)
            _DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1X = float(- self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][temp_num][0] - self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2\
                                                                    + self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2)
            _DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1 = (pow(_DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1X,2) + pow(_DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1Y,2))**0.5
            
            print (self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][-temp_num3])
            _DistanceBtwMet2ConnectionViaEdge2Met2OutputRouting1 =  float(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][temp_num][1] - self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2\
                                                                    - self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_OutputRouting']['_Width']/2)
            _DistanceBtwMet2ConnectionViaEdge2Met2OutputRouting2 =  float(self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][-temp_num3][1] - self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2\
                                                                    - self._DesignParameter['_OutputRouting']['_XYCoordinates'][-1][0][1] - self._DesignParameter['_OutputRouting']['_Width']/2)
                                                                    
            _DistanceBtwMet1DataBarEdge2Met1GateViaEdgeN = float (self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] -self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                                        - self._DesignParameter['_DataBarRouting2']['_XYCoordinates'][0][0][0] -self._DesignParameter['_DataBarRouting2']['_Width']/2  )
            _DistanceBtwMet1DataBarEdge2Met1GateViaEdgeP = float (self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0] -self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                                        - self._DesignParameter['_DataBarRouting2']['_XYCoordinates'][0][0][0] -self._DesignParameter['_DataBarRouting2']['_Width']/2  )
                                    
                                                        
            
            
            if _DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1 < _DRCObj._MetalxMinSpace : #or _DistanceBtwMet2ConnectionViaEdge2Met2OutputViaEdge1X < _DRCObj._MetalxMinSpace: 
                _YBiasForViaMet12Met2OnPMOS2Output += _DRCObj._MinSnapSpacing
                DRC_PASS = 0
            if _DistanceBtwMet2ConnectionViaEdge2Met2OutputRouting1 < _DRCObj._MetalxMinSpace :
                _YBiasOfOutputRouting1 += _DRCObj._MinSnapSpacing
                DRC_PASS = 0
            if _DistanceBtwMet2ConnectionViaEdge2Met2OutputRouting2 < _DRCObj._MetalxMinSpace:
                _YBiasOfOutputRouting2 += _DRCObj._MinSnapSpacing
                DRC_PASS = 0

            if _DistanceBtwMet1DataBarEdge2Met1GateViaEdgeN < _DRCObj._Metal1MinWidth :
                _BiasDictforViaPoly2Met1OnGate['_XbiasInvNMOSGateVia']  += _DRCObj._MinSnapSpacing
                DRC_PASS = 0
            if _DistanceBtwMet1DataBarEdge2Met1GateViaEdgeP < _DRCObj._Metal1MinWidth :
                _BiasDictforViaPoly2Met1OnGate['_XbiasInvPMOSGateVia'] += _DRCObj._MinSnapSpacing
                DRC_PASS = 0
                
                
                
                
                
            # _SpaceBTWMOS12MOS2 DRC check
            _MinSpaceBTWMOS12MOS2 = None
            _SpaceBTWMOS12MOS2OD =  self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2 - \
                                   (self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]+self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2)
                
            while _SpaceBTWMOS12MOS2OD < _DRCObj._OdMinSpace:
                _SpaceBTWMOS12MOS2OD += DRC._MinSnapSpacing
                _SpaceBiasforMOS12MOS2OD += DRC._MinSnapSpacing
                
            _MinSpaceBTWMOS12MOS2 = _SpaceBTWMOS12MOS2OD
            _SpaceBTWMOS12MOS2PO = None
            # if _Dummy is False
                # _SpaceBTWMOS12MOS2PO = 
                
                
                
                
                
            # BodyContact Adjusting

            _LengthOfBody = self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']
            leftSideOD = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2 
            rightSideOD = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2
            _LengthOfOD = abs(rightSideOD - leftSideOD )

            if _NumberOfSupplyCOX is None:
                _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 \
                        else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))
                print ('kakao' , _NumberOfSupplyCOX , _LengthOfBody ,_LengthOfOD , 'numerator', _LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2), 'denominator' , (_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2)))
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX

            self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)
            self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)
            self._DesignParameter['_PbodyContact']['_XYCoordinates'] = _tmpPbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_NbodyContact']['_XYCoordinates'] = _tmpNbodyObj._DesignParameter['_XYCoordinates']


            del _tmpPbodyObj
            del _tmpNbodyObj
            # if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 :
                # if _LengthOfBody > _LengthOfOD or _LengthOfBody < (_LengthOfOD - 2*_DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) :
                    # new_length = _LengthOfOD - 2*_DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)
                    # _NumberOfSupplyCOX = int (new_length / (_DRCObj._CoMinWidth + _DRCObj._VIAxMinWidth ) )
                    # DRC_PASS = 0
            # else:
                # if _LengthOfBody > _LengthOfOD :# or _LengthOfBody < (_LengthOfOD - 2*(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2) ) ) :
                    # new_length = _LengthOfOD - 2*_DRCObj._CoMinEnclosureByODAtLeastTwoSide
                    # _NumberOfSupplyCOX = int( new_length / (_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=2, NumOfCOX=2)) )
                    # print 'americano', _LengthOfBody, _LengthOfOD
                    # DRC_PASS = 0
                
                
                
                
                
                
                
            # _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None,
            if _HeightCalOption == 'ON' :
                tempVal = 0; tempVal2 = 0; error = 0
                for i in range(1,6):
                    VIA = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate'
                    if i == 5:
                        VIA = '_ViaPoly2Met1OnInvMOSGate'
                    _DistanceBtwViaNEdge2NW = (_XOREdgeBtwNWandPW + tempVal) - self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 

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
                    print ('_XOREdgeBtwNWandPW Should be same or higher than' , _XOREdgeBtwNWandPW+ tempVal)
                    return 0
                    
                for i in range(1,6):
                    VIA = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate'
                    if i == 5:
                        VIA = '_ViaPoly2Met1OnInvMOSGate'
                    _DistanceBtwViaPEdge2NW = -(_XOREdgeBtwNWandPW+tempVal) + self._DesignParameter[VIA]['_XYCoordinates'][1][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 + tempVal2

                    while _DistanceBtwViaPEdge2NW < _DRCObj._PpMinEnclosureOfPo :
                        _YbiasforHeight += _DRCObj._MinSnapSpacing
                        _DistanceBtwViaPEdge2NW += _DRCObj._MinSnapSpacing
                        tempVal2 += _DRCObj._MinSnapSpacing
                        DRC_PASS = 0
                        if _HeightCalOption != 'ON' :
                            error = 1
                if error == 1 :
                    print ('****************************** Error occured in _XORVdd2VssHeight + _HeightCalibration setting ******************************')
                    print ('_XORVdd2VssHeight + _HeightCalibration Should be same or higher than' , _XORVdd2VssHeight + _HeightCalibration + tempVal2)
                    return 0            
             

             
             
            # _tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS = _DRCObj.DRCMETAL1MinSpace(_Width=self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] , _ParallelLength=self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            # _tmpDRCMet1MinSpaceByViaPoly2Met1 = _DRCObj.DRCMETAL1MinSpace(_Width= self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _ParallelLength= self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            # _tmpDRCMinSpacePoly2OD = _DRCObj._PolygateMinSpace2OD            
            
            
            # #NEW GATE ROUTING
            # self._DesignParameter['_GateRoutingOnNMOS']['_XYCoordinates']=\
                        # [
                            # [
                                # self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] + float(min(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) + max(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]))/2  ,
                                # max(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][4][1] 
                                    # + float(self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2,
                                    # self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][1])  
                                # + float(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])/2
                                # + max([_tmpDRCPolyMinSpaceByAdditionalMet1OnNMOS,_tmpDRCMet1MinSpaceByViaPoly2Met1, _tmpDRCMinSpacePoly2OD ]) + _BiasDictforViaPoly2Met1OnGate['_YbiasInvNMOSGateVia']
                            # ]
                        # ]
            # self._DesignParameter['_GateRoutingOnNMOS']['_XWidth']=(max(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0]) -  min(zip(*self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])[0])) + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
            # self._DesignParameter['_GateRoutingOnNMOS']['_YWidth']=self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

            # print 'debug' ,  self._DesignParameter['_GateRoutingOnNMOS']['_XWidth'] , self._DesignParameter['_GateRoutingOnNMOS']['_YWidth']






           
            #When InvMOS and MOS3 are too close to put 2 VIAs for gate connection            
            # if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1 and len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) < 4 :
                # self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'] = []
                # self._DesignParameter['_InputDataRouting1']['_XYCoordinates'] = []
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2],\
                                                                                          # [self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'][2][0][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2],\
                                                                                          # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'][2][0] ])
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2] ,\
                                                                                          # [self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'][2][0][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2],\
                                                                                          # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'][2][0] ])
            
            
            
            
            
            

            #Space btw MOS2 and InvMOS DRC check (Metal2 - Metal2 and Metal3 - Metal3)
            if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) is not 1:
                MOS2RightEdgeViaIndex = len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) + len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) -1 
                InvMOSLeftEdgeViaIndex = -len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])
                SpaceM2 = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] - self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][MOS2RightEdgeViaIndex][0] - self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                SpaceM3 = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][MOS2RightEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                
                #NMOS check
                M2Width = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                M2Length = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                M3Width1 = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][MOS2RightEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                M3Length = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                M3Width2 = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                #PMOS check
                M2Width_P = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                M2Length_P = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                M3Width1_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][MOS2RightEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                M3Length_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                M3Width2_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                
                if SpaceM2 < max(_DRCObj.DRCMETALxMinSpace(_Width=M2Width, _ParallelLength=M2Length),_DRCObj.DRCMETALxMinSpace(_Width=M2Width_P, _ParallelLength=M2Length_P) ):
                    _MOS22InvMOSspacebias += _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                elif SpaceM3 < max(_DRCObj.DRCMETALxMinSpace(_Width=M3Width1, _ParallelLength=M3Length), _DRCObj.DRCMETALxMinSpace(_Width=M3Width2, _ParallelLength=M3Length), _DRCObj.DRCMETALxMinSpace(_Width=M3Width1_P, _ParallelLength=M3Length_P), _DRCObj.DRCMETALxMinSpace(_Width=M3Width2_P, _ParallelLength=M3Length_P)):
                    _MOS22InvMOSspacebias += _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                
                
            # # INV Input Via and INV MOS Gate connection check 
            # if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) < 3 :
                # _DistanceBtwInvInputVia2InvPolyGate =   float(
                                                        # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] -\
                                                        # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 -\
                                                        # self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] - \
                                                        # self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - \
                                                        # self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2
                                                        # )
                # if _DistanceBtwInvInputVia2InvPolyGate > 0 :
                    # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] += _DistanceBtwInvInputVia2InvPolyGate*2
                    # # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] -= float(_DistanceBtwInvInputVia2InvPolyGate/2)
            
            # # INV Input Via and MOS3 Gate Distance check
            # _DistanceBtwInvInputVia2MOS3PolyGate =  float(
                                                    # self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + \
                                                    # self._DesignParameter['_NMO3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - \
                                                    # self._DesignParameter['_NMO3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2-\
                                                    # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] -\
                                                    # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2
                                                    # )
            # if _DistanceBtwInvInputVia2MOS3PolyGate < _DRCObj._PolygateMinSpace
                
            
            
            
            #Space btw MOS3 and InvMOS DRC check (Metal2 - Metal2 and Metal3 - Metal3)
            if len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) is not 1:
                MOS3LeftEdgeViaIndex = len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) + len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])
                InvMOSRightEdgeViaIndex = -1
                MOS4RigthEdgeViaIndex = -len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])-1
                SpaceM2 = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][MOS3LeftEdgeViaIndex][0] - self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_XYCoordinates'][InvMOSRightEdgeViaIndex][0] - self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                SpaceM3 = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][MOS3LeftEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][InvMOSRightEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                M2Width = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                M2Length = self._DesignParameter['_ViaMet12Met2OnNMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                M3Width = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][MOS4RigthEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][MOS3LeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                M3Length = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                M3Width2 = self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnNMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                 #PMOS check
                M2Width_P = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                M2Length_P = self._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                M3Width1_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][MOS4RigthEdgeViaIndex][0] - self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][MOS3LeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                M3Length_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                M3Width2_P = self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_XYCoordinates'][InvMOSLeftEdgeViaIndex][0] + self._DesignParameter['_ViaMet22Met3OnPMOSconnection']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                
                print (M3Width, M3Width2, M3Length)
                if SpaceM2 < max(_DRCObj.DRCMETALxMinSpace(_Width=M2Width, _ParallelLength=M2Length),_DRCObj.DRCMETALxMinSpace(_Width=M2Width_P, _ParallelLength=M2Length_P) ):
                    _InvMOS2MOS3spacebias += _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                elif SpaceM3 < max(_DRCObj.DRCMETALxMinSpace(_Width=M3Width1, _ParallelLength=M3Length), _DRCObj.DRCMETALxMinSpace(_Width=M3Width2, _ParallelLength=M3Length), _DRCObj.DRCMETALxMinSpace(_Width=M3Width1_P, _ParallelLength=M3Length_P), _DRCObj.DRCMETALxMinSpace(_Width=M3Width2_P, _ParallelLength=M3Length_P)):
                    _InvMOS2MOS3spacebias += _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
            
            
            # When Dummy is true --> Poly2Met1 Via on INV should be replaced.
            if _Dummy is True:
            

                Px_DistanceBtwInvInputVia2InvPolyGate =  \
                    (self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0]+self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 ) \
                    -(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
                if Px_DistanceBtwInvInputVia2InvPolyGate < _DRCObj._PolygateMinSpace:
                    Py_DistanceBtwInvInputVia2InvPolyGate =  \
                        (self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][1]-self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 ) \
                        -(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)
                    if Py_DistanceBtwInvInputVia2InvPolyGate < _DRCObj._PolygateMinSpace:
                        BiasCal = (_DRCObj._PolygateMinSpace - Py_DistanceBtwInvInputVia2InvPolyGate) / _DRCObj._MinSnapSpacing
                        _BiasDictforViaPoly2Met1OnGate['_YbiasInvPMOSGateVia'] -= BiasCal * _DRCObj._MinSnapSpacing
                        DRC_PASS = 0
                    
                
                
                Nx_DistanceBtwInvInputVia2InvPolyGate =  \
                    (self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0]+self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 ) \
                    -(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
                if Nx_DistanceBtwInvInputVia2InvPolyGate < _DRCObj._PolygateMinSpace:
                    Ny_DistanceBtwInvInputVia2InvPolyGate =  \
                        (self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) \
                        -(self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][1]+self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 )
                    if Ny_DistanceBtwInvInputVia2InvPolyGate < _DRCObj._PolygateMinSpace:
                        BiasCal = (_DRCObj._PolygateMinSpace - Ny_DistanceBtwInvInputVia2InvPolyGate) / _DRCObj._MinSnapSpacing
                        _BiasDictforViaPoly2Met1OnGate['_YbiasInvNMOSGateVia'] += BiasCal * _DRCObj._MinSnapSpacing
                        DRC_PASS = 0
            
                
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                # tmp=[]
                # for i in range( 0, len(self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) ):
                    # tmp.append([ [self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][1]] \
                                # ,[self._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0],self._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1]]  ])                
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmp
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                # tmp=[]
                # for i in range( 0, len(self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates']) ):
                    # tmp.append([ [self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][1]] \
                                # ,[self._DesignParameter['_InvPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0],self._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1]]  ])                
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmp
            
            
            #When InvMOS and MOS3 are too close to put 2 VIAs for gate connection   NEW     --> change:increase space btw mosfets
            _DistanceBtwInvVia2MOS3Via = \
                float(self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0] -self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2) \
                -float(self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
            if _DistanceBtwInvVia2MOS3Via < _DRCObj._PolygateMinSpace  :
                _InvMOS2MOS3spacebias += round((_DRCObj._PolygateMinSpace-_DistanceBtwInvVia2MOS3Via)/_DRCObj._PolygateMinSpace + 0.5) * _DRCObj._MinSnapSpacing
                DRC_PASS = 0
                # # self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'] = []
                # self._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'] = []
                # self._DesignParameter['_InputDataRouting1']['_XYCoordinates'] = []
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = self._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2],\
                                                                                          # [float(self._DesignParameter['_GateRoutingOnNMOS3']['_XYCoordinates'][0][0]-self._DesignParameter['_GateRoutingOnNMOS3']['_XWidth']/2+self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2),self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2],\
                                                                                          # [float(self._DesignParameter['_GateRoutingOnNMOS3']['_XYCoordinates'][0][0]-self._DesignParameter['_GateRoutingOnNMOS3']['_XWidth']/2+self._DesignParameter['_AdditionalPolyOnNMOS']['_Width']/2),self._DesignParameter['_GateRoutingOnNMOS3']['_XYCoordinates'][0][1]] ])
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = self._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append([ [self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0],self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2],\
                                                                                          # [float(self._DesignParameter['_GateRoutingOnPMOS3']['_XYCoordinates'][0][0]-self._DesignParameter['_GateRoutingOnPMOS3']['_XWidth']/2+self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2),self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2],\
                                                                                          # [float(self._DesignParameter['_GateRoutingOnPMOS3']['_XYCoordinates'][0][0]-self._DesignParameter['_GateRoutingOnPMOS3']['_XWidth']/2+self._DesignParameter['_AdditionalPolyOnPMOS']['_Width']/2),self._DesignParameter['_GateRoutingOnPMOS3']['_XYCoordinates'][0][1]] ])
                
            # #When Dummy is True and Mos has only one gate --> via poly 2 gate poly is close
            # if _Dummy is True:
                # if _NumberOfGate1 is 1:
                    # _DistanceBtwVia2GateX = \
                        # float(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2) \
                        # -float(self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
                    # if _DistanceBtwVia2GateX < _DRCObj._PolygateMinSpace:
                        # _DistanceBtwVia2GateY = \
                            # float(self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 ) \
                            # -float(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][1]+self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) 
                        # _Distance = (_DistanceBtwVia2GateX**2) + (_DistanceBtwVia2GateY**2)
                        # if _Distance < _DRCObj._PolygateMinSpace:
                            # temp = round(    (( ((_Distance)**2 - (_DistanceBtwVia2GateX**2) ) **0.5)  - _DistanceBtwVia2GateY  )/_DRCObj._MinSnapSpacing +0.5)
                            # _XbiasNMOS1GateVia += temp * _DRCObj._MinSnapSpacing
            if _Dummy is True:
            
                for i in range(1,5):
                    NMOS = '_NMOS' + str(i)
                    PMOS = '_PMOS' + str(i)
                    VIA = '_ViaPoly2Met1OnMOS' + str(i) + 'Gate'
                    NViaBias = '_YbiasNMOS' + str(i)+ 'GateVia'
                    PViaBias = '_YbiasPMOS' + str(i)+ 'GateVia'
            
                    if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) is 1:
                        # # tmp=[]
                        # # tmp= [self._DesignParameter[NMOS]['_XYCoordinates'][0], self._DesignParameter[VIA]['_XYCoordinates'][0] ] 
                        # # self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'].append(tmp)
                    # # NMOS adjusting
                        _DistanceBtwVia2GateY = \
                            float(self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 ) \
                            -float(self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][1]+self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) 
                        if _DistanceBtwVia2GateY < _DRCObj._PolygateMinSpace:
                            temp = round(abs(_DRCObj._PolygateMinSpace- _DistanceBtwVia2GateY)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            _BiasDictforViaPoly2Met1OnGate[NViaBias] += temp
                            DRC_PASS = 0
                            
                    
                    if len(self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates']) is 1:
                        # # tmp=[]
                        # # tmp= [ self._DesignParameter[PMOS]['_XYCoordinates'][0], self._DesignParameter[VIA]['_XYCoordinates'][1] ]   
                        # # self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'].append(tmp)
                    # # PMOS adjusting
                        _DistanceBtwVia2GateY = \
                            float(self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][1]-self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2) \
                            -float(self._DesignParameter[VIA]['_XYCoordinates'][1][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)
                        if _DistanceBtwVia2GateY < _DRCObj._PolygateMinSpace:
                            temp = round( abs(_DRCObj._PolygateMinSpace - _DistanceBtwVia2GateY)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            _BiasDictforViaPoly2Met1OnGate[PViaBias] -= temp
                            DRC_PASS = 0
                    print (NViaBias, _BiasDictforViaPoly2Met1OnGate[NViaBias])
            
            
                        
                        
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
        print ('                                    {}  XOR Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        print ('ODSPACE' ,_SpaceBTWMOS12MOS2OD)


if __name__=='__main__':



    ##############045nm xor #####################################################################
    # XORObj=_XOR(_DesignParameter=None, _Name='XOR')
    # XORObj._CalculateDesignParameter(
    #                      _INVNumberOfGate=5, _INVChannelWidth=350, _INVChannelLength=50, _INVPNChannelRatio=2,
    #                      _NumberOfGate1=5, _ChannelWidth1=350, _ChannelLength1=50, _PNChannelRatio1=2,
    #                      _NumberOfGate2=5, _ChannelWidth2=350, _ChannelLength2=50, _PNChannelRatio2=2,
    #                      _NumberOfGate3=5, _ChannelWidth3=350, _ChannelLength3=50, _PNChannelRatio3=2,
    #                      _NumberOfGate4=5, _ChannelWidth4=350, _ChannelLength4=50, _PNChannelRatio4=2,
    #                      _NumberOfSupplyCOX=33,_NumberOfSupplyCOY=2,
    #                      _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None, _InputRouting = False,  _OutputMet2Width = None,
    #
    #                      _XORVdd2VssHeight=2400,  _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=1000,
    #
    #
    #
    #                      _YBiasForViaMet12Met2OnPMOS2Output=None,_YBiasForViaMet12Met2OnPMOS3Output=None,_YBiasForViaMet12Met2OnNMOS2Output=None,_YBiasForViaMet12Met2OnNMOS3Output=None,
    #                      _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None, _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None, _NumberOfPMOSConnectionCOY=None,
    #                      _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,
    #                      _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption= 'ON',
    #                      _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfNMOSOutputViaCOY=None, _NumberOfPMOSOutputViaCOY=None,
    #                      _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
    #                      _BiasDictforViaPoly2Met1OnGate = {
    #                      '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None, '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None, '_XbiasNMOS3GateVia':None,
    #                      '_YbiasNMOS3GateVia':None, '_XbiasNMOS4GateVia':None, '_YbiasNMOS4GateVia':None, '_XbiasInvNMOSGateVia':None, '_YbiasInvNMOSGateVia':None,
    #                      '_XbiasPMOS1GateVia':None, '_YbiasPMOS1GateVia':None, '_XbiasPMOS2GateVia':None, '_YbiasPMOS2GateVia':None, '_XbiasPMOS3GateVia':None,
    #                      '_YbiasPMOS3GateVia':None, '_XbiasPMOS4GateVia':None, '_YbiasPMOS4GateVia':None, '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
    #                      },
    #                      _MOS12MOS2spacebias=None, _MOS22InvMOSspacebias=None, _InvMOS2MOS3spacebias=None, _MOS32MOS4spacebias=None, _XYadjust=None,
    #
    #                      _Dummy=True           )
    # ##################################################################################################################################################################

    # ##############065nm XOR #####################################################################
    XORObj=_XOR(_DesignParameter=None, _Name='XOR')
    XORObj._CalculateDesignParameter( _INVNumberOfGate=2, _INVChannelWidth=450, _INVChannelLength=60, _INVPNChannelRatio=2, _XORVdd2VssHeight=3300, _HeightCalOption='ON',\
                                      _NumberOfGate1=3, _ChannelWidth1=450, _ChannelLength1=60, _PNChannelRatio1=2, \
                                      _NumberOfGate2=2, _ChannelWidth2=450, _ChannelLength2=60, _PNChannelRatio2=2, \
                                      _NumberOfGate3=4, _ChannelWidth3=450, _ChannelLength3=60, _PNChannelRatio3=2, \
                                      _NumberOfGate4=2, _ChannelWidth4=450, _ChannelLength4=60, _PNChannelRatio4=2, \
                                         _NumberOfNMOSConnectionViaCOY = 2, _NumberOfPMOSConnectionViaCOY =2,
                                         _NumberOfNMOSOutputViaCOY = 4, _NumberOfPMOSOutputViaCOY =6,
                                         _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                         _BiasDictforViaPoly2Met1OnGate = {
                                         '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None,
                                         '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
                                         '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
                                         '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0,
                                         '_XbiasInvNMOSGateVia':None,    '_YbiasInvNMOSGateVia':None,   '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                         },     # XBias does not consider DRC calc value
                                         
                                         _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=1500,
                                         _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=0, _MOS32MOS4spacebias=0, \
                                         _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,\
                                         _Dummy=False)

    # # ##################################################################################################################################################################
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
    XORObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=XORObj._DesignParameter)
    _fileName='autoXOR_45.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=XORObj._CreateGDSStream(XORObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()




# Consider output routing on PMOS DRC






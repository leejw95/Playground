import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaPoly2Met1


import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _ClkTreeElement(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
    
    
                                        _NumberOfGate=None, _ChannelLength=None, _ChannelWidth=None, _PNChannelRatio=None,

                                        _SupplyMetal1YWidth=None, _NumberOfSupplyCOY=None,

                                        _Vdd2VssHeight=None, _HeightCalibration=None, _DistanceBtwSupplyCenter2MOSEdge=None,
                                        
                                        _XYadjust=None, _NumberOfMOSGateViaCOX=None, _SupplyRoutingWidth=None, _NumberOfSupplyCOX=None,
                                        
                                        _MOS12MOS2spacebias=None, _MOS22MOS3spacebias=None, _MOS32MOS4spacebias=None, _MOS42MOS5spacebias=None, _MOS52MOS6spacebias=None,
                                        
                                        _NumberOfGateViaCOX=None, _NumberOfGateViaCOY=None, _NumberOfPMOSOutputViaCOY=None, _NumberOfNMOSOutputViaCOY=None,
                                        
                                        _NumberOfGate5ViaCOX = None,_NumberOfMOS5GateViaCOX = None,
                                        
                                        _XbiasforGateVia=None, _XbiasforGate6Via=None, _NumberOfParallelViaCOY=None, _EdgeBtwNWandPW = None,
                                        
                                        _NumberOfPassMet=None, _MetalxDRC= None, _ParallelMetalWidth=None, _TreeLevel = None, _TotalLevel=None,
                                        
                                        _PMOSOutputMetalWidth=None, _NMOSOutputMetalWidth=None, _ElementType = None, _MOSspacebias=None,
                                     
                                        _NMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                        _PMOSDesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                        _NbodyDesignCalculationParameters=copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation),
                                        _PbodyDesignCalculationParameters=copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation),
                                        _ViaPoly2Met1OnMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                        _ViaPoly2Met1OnCoupledMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                        _CrossCoupledNMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),

                                        InLinelocation1 = None,InLinelocation2 = None,InLinelocation3 = None,InLinelocation4 = None,InLinelocation5 = None,
                                        OutLinelocation1 = None,OutLinelocation2 = None,OutLinelocation3 = None,OutLinelocation4 = None,OutLinelocation5 = None,

                                        _NumberOfCLKInvGate = None, _CLKInvChannelWidth=None, _CLKInvPNChannelRatio=None,
                                        
                                        
                                        
                                        _NumberOfCoupledGate=None, _CoupledChannelWidth=None, _NumberOfCoupledNMOSconnectionViaCOY = None, _XbiasForCoupledMOSGateVia = None,
                                        _NumberOfCoupledMOSGateViaCOX = None, _NumberOfCoupledMOSGateViaCOY=None, CCdrainMet1Width = None,
                                        _NumberOfCCMOSDrainViaCOX = None, _NumberOfCCMOSDrainViaCOY = None, _CCconnectionMetWidht=None,
                                     

                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTreeElement'):

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
                                                    _NMOS5 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS5In{}'.format(_Name)))[0],
                                                    _PMOS5 = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_DesignParameter=None, _Name='PMOS5In{}'.format(_Name)))[0],
                                                    _NMOS6 = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_DesignParameter=None, _Name='NMOS6In{}'.format(_Name)))[0],

                                                    _PbodyContact=self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='PbodyContactIn{}'.format(_Name)))[0],
                                                    _NbodyContact=self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='NbodyContactIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaPoly2Met1OnMOS1 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS1GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS2 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS2GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS3 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS3GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS4 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS4GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS5 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS5GateIn{}'.format(_Name)))[0],
                                                    _ViaPoly2Met1OnMOS6 = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnMOS6GateIn{}'.format(_Name)))[0],

                                                    _GateRoutingOnMOS1 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _GateRoutingOnMOS2 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _GateRoutingOnMOS3 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _GateRoutingOnMOS4 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    _GateRoutingOnMOS5 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=100),
                                                    
                                                    _AdditionalPOLYRoutingOnMOS1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalPOLYRoutingOnMOS2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalPOLYRoutingOnMOS3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalPOLYRoutingOnMOS4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalPOLYRoutingOnMOS5=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalPOLYRoutingOnMOS6=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _AdditionalMet1RoutingOnMOSGate1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1RoutingOnMOSGate2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1RoutingOnMOSGate3=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1RoutingOnMOSGate4=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1RoutingOnMOSGate5=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1RoutingOnMOSGate6=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _AdditionalMet3RoutingOnOutput=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _PMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _NMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _CrossCoupledNMOSSupplyRouting=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),

                                                    
                                                    
                                                    _ViaMet12Met2OnGate1 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate1In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnGate2 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate2In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnGate3 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate3In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnGate4 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate4In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnGate5 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate5In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnGate6 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnGate6In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnGate1 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnGate1In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnGate2 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnGate2In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnGate3 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnGate3In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnGate4 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnGate4In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnGate5 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnGate5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet32Met4OnGate1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnGate1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnGate2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnGate2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnGate3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnGate3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnGate4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnGate4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnGate5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnGate5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet42Met5OnGate1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnGate1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnGate2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnGate2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnGate3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnGate3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnGate4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnGate4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnGate5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnGate5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet52Met6OnGate1 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnGate1In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnGate2 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnGate2In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnGate3 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnGate3In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnGate4 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnGate4In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnGate5 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnGate5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnPMOSOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnPMOSOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnPMOSOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnNMOSOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnNMOSOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnNMOS6Connection = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS6ConnectionIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnPMOSOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOSOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOSOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOSOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnPMOSOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnNMOSOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOSOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOSOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOSOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnNMOSOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet32Met4OnOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet42Met5OnOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutput5In{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet52Met6OnOutput1 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnOutput1In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnOutput2 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnOutput2In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnOutput3 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnOutput3In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnOutput4 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnOutput4In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnOutput5 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnOutput5In{}'.format(_Name)))[0],
                                                    
                                                    
                                                    
                                                    _ViaMet12Met2OnCCDrain = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCCDrainIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnCCDrain = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCCDrainIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnCCDrain = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnCCDrainIn{}'.format(_Name)))[0],
                                                    _CrossCoupledDrainMet1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100 ),
                                                    _CrossCoupledDrainMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 ),
                                                    _CrossCoupledConnectionMet2 =self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 ),
                                                    
                                                    # _OutputMet2Horizontal1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Horizontal2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Horizontal3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Horizontal4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Horizontal5 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    # _OutputMet2Vertical1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Vertical2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Vertical3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Vertical4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    # _OutputMet2Vertical5 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    

                                                    _AdditionalMet1OnNMOS = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnPMOS = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnNMOS5 = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnPMOS5 = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet2OnNMOS = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnNMOS6 = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _NWell=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPMOS=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderNbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderPbodyContact=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 


                                    
                                        _NumberOfGate=None, _ChannelLength=None, _ChannelWidth=None, _PNChannelRatio=None,

                                        _SupplyMetal1YWidth=None, _NumberOfSupplyCOY=None, _DistanceBtwSupplyCenter2MOSEdge=None,

                                        _Vdd2VssHeight=None, _HeightCalibration=None,
                                        
                                        _XYadjust=None, _NumberOfMOSGateViaCOX=None, _SupplyRoutingWidth=None, _NumberOfSupplyCOX=None,
                                        
                                        _MOS12MOS2spacebias=None, _MOS22MOS3spacebias=None, _MOS32MOS4spacebias=None, _MOS42MOS5spacebias=None, _MOS52MOS6spacebias=None,
                                     
                                        _NumberOfGateViaCOX=None, _NumberOfGateViaCOY=None,  _NumberOfPMOSOutputViaCOY=None, _NumberOfNMOSOutputViaCOY=None,
                                        
                                        _NumberOfGate5ViaCOX = None, _NumberOfMOS5GateViaCOX = None,
                                        
                                        _XbiasforGateVia=None,_XbiasforGate6Via=None,_NumberOfParallelViaCOY=None, _EdgeBtwNWandPW = None,
                                        
                                        _NumberOfPassMet=None, _MetalxDRC= None, _ParallelMetalWidth=None, _TreeLevel = None, _TotalLevel=None,
                                        
                                        _PMOSOutputMetalWidth=None, _NMOSOutputMetalWidth=None, _ElementType = None, _MOSspacebias=None,
                                        
                                        _NMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                        _PMOSDesignCalculationParameters=copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation),
                                        _NbodyDesignCalculationParameters=copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation),
                                        _PbodyDesignCalculationParameters=copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation),
                                        _ViaPoly2Met1OnMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                        _ViaPoly2Met1OnCoupledMOSGateParameters=copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation),
                                        _CrossCoupledNMOSDesignCalculationParameters=copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation),
                                        
                                        InLinelocation1 = None,InLinelocation2 = None,InLinelocation3 = None,InLinelocation4 = None,InLinelocation5 = None,
                                        OutLinelocation1 = None,OutLinelocation2 = None,OutLinelocation3 = None,OutLinelocation4 = None,OutLinelocation5 = None,

                                        _NumberOfCLKInvGate = None, _CLKInvChannelWidth=None, _CLKInvPNChannelRatio=None,
                                        
                                        
                                        _NumberOfCoupledGate=None, _CoupledChannelWidth=None, _NumberOfCoupledNMOSconnectionViaCOY = None, _XbiasForCoupledMOSGateVia = None,
                                        _NumberOfCoupledMOSGateViaCOX = None, _NumberOfCoupledMOSGateViaCOY=None,  CCdrainMet1Width = None,
                                        _NumberOfCCMOSDrainViaCOX = None, _NumberOfCCMOSDrainViaCOY = None, _CCconnectionMetWidht=None,


                                     _Dummy=None
                                     ):
        print '#########################################################################################################'
        print '                                    {}  CLK Tree Element Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'



        _DRCObj=DRC.DRC()
        
        while True:
            # #####################SUBSET ELEMENTS GENERATION#########################
            # MOSFET GENERATION
            _NMOSDesignCalculationParameters['_NMOSNumberofGate']=_NumberOfGate
            _NMOSDesignCalculationParameters['_NMOSChannelWidth']=_ChannelWidth
            _NMOSDesignCalculationParameters['_NMOSChannellength']=_ChannelLength
            _NMOSDesignCalculationParameters['_NMOSDummy']=_Dummy
            self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSDesignCalculationParameters)
            self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSDesignCalculationParameters)
            self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSDesignCalculationParameters)
            self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSDesignCalculationParameters)
            self._DesignParameter['_NMOS5']['_DesignObj']._CalculateNMOSDesignParameter(_NMOSNumberofGate = _NumberOfCLKInvGate, _NMOSChannelWidth = _CLKInvChannelWidth, _NMOSChannellength=_ChannelLength, _NMOSDummy =_Dummy )

            _PMOSDesignCalculationParameters['_PMOSNumberofGate']=_NumberOfGate
            _PMOSDesignCalculationParameters['_PMOSChannelWidth']=round(_ChannelWidth * _PNChannelRatio)
            _PMOSDesignCalculationParameters['_PMOSChannellength']=_ChannelLength
            _PMOSDesignCalculationParameters['_PMOSDummy']=_Dummy
            self._DesignParameter['_PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSDesignCalculationParameters)
            self._DesignParameter['_PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSDesignCalculationParameters)
            self._DesignParameter['_PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSDesignCalculationParameters)
            self._DesignParameter['_PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSDesignCalculationParameters)
            self._DesignParameter['_PMOS5']['_DesignObj']._CalculatePMOSDesignParameter(_PMOSNumberofGate = _NumberOfCLKInvGate, _PMOSChannelWidth = _CLKInvChannelWidth*_CLKInvPNChannelRatio, _PMOSChannellength=_ChannelLength,_PMOSDummy=_Dummy)

            _CrossCoupledNMOSDesignCalculationParameters['_NMOSNumberofGate']=_NumberOfCoupledGate
            _CrossCoupledNMOSDesignCalculationParameters['_NMOSChannelWidth']=_CoupledChannelWidth
            _CrossCoupledNMOSDesignCalculationParameters['_NMOSChannellength']=_ChannelLength
            _CrossCoupledNMOSDesignCalculationParameters['_NMOSDummy'] = _Dummy
            self._DesignParameter['_NMOS6']['_DesignObj']._CalculateNMOSDesignParameter(**_CrossCoupledNMOSDesignCalculationParameters)

            # GATE VIA GENERATION
            if _NumberOfMOSGateViaCOX is None:
                _NumberOfMOSGateViaCOX = 2
                if len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOSGateViaCOX = len(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
                    
            if _NumberOfMOS5GateViaCOX is None:
                _NumberOfMOS5GateViaCOX = _NumberOfMOSGateViaCOX
                if len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']) > 2:
                    _NumberOfMOS5GateViaCOX = len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])
                
                
            _ViaPoly2Met1OnMOSGateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfMOSGateViaCOX
            _ViaPoly2Met1OnMOSGateParameters['_ViaPoly2Met1NumberOfCOY'] = 1    
            self._DesignParameter['_ViaPoly2Met1OnMOS1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOSGateParameters)
            self._DesignParameter['_ViaPoly2Met1OnMOS2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOSGateParameters)
            self._DesignParameter['_ViaPoly2Met1OnMOS3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOSGateParameters)
            self._DesignParameter['_ViaPoly2Met1OnMOS4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnMOSGateParameters)
            self._DesignParameter['_ViaPoly2Met1OnMOS5']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX = _NumberOfMOS5GateViaCOX , _ViaPoly2Met1NumberOfCOY = 1)

            if _NumberOfCoupledMOSGateViaCOX is None:
                _NumberOfCoupledMOSGateViaCOX = 2
            if _NumberOfCoupledMOSGateViaCOY is None:
                _NumberOfCoupledMOSGateViaCOY = 1

            _ViaPoly2Met1OnCoupledMOSGateParameters['_ViaPoly2Met1NumberOfCOX'] = _NumberOfCoupledMOSGateViaCOX
            _ViaPoly2Met1OnCoupledMOSGateParameters['_ViaPoly2Met1NumberOfCOY'] = _NumberOfCoupledMOSGateViaCOY
            self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_ViaPoly2Met1OnCoupledMOSGateParameters)
            self._DesignParameter['_ViaMet12Met2OnGate6']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfCoupledMOSGateViaCOX, _ViaMet12Met2NumberOfCOY=1)

            
            if _NumberOfGateViaCOX is None:
                _NumberOfGateViaCOX = 2
            if _NumberOfGate5ViaCOX is None:
                _NumberOfGate5ViaCOX = 2
            if _NumberOfGateViaCOY is None:
                _NumberOfGateViaCOY = 1
                
            self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfGateViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet12Met2OnGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfGateViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet12Met2OnGate3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfGateViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet12Met2OnGate4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfGateViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet12Met2OnGate5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfGate5ViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfGateViaCOY)
            
            self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfGateViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet22Met3OnGate2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfGateViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet22Met3OnGate3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfGateViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet22Met3OnGate4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfGateViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet22Met3OnGate5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfGate5ViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfGateViaCOY)
            
            self._DesignParameter['_ViaMet32Met4OnGate1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfGateViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet32Met4OnGate2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfGateViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet32Met4OnGate3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfGateViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet32Met4OnGate4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfGateViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet32Met4OnGate5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfGate5ViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfGateViaCOY)
            
            self._DesignParameter['_ViaMet42Met5OnGate1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfGateViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet42Met5OnGate2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfGateViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet42Met5OnGate3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfGateViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet42Met5OnGate4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfGateViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet42Met5OnGate5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfGate5ViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfGateViaCOY)
            
            self._DesignParameter['_ViaMet52Met6OnGate1']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfGateViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet52Met6OnGate2']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfGateViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet52Met6OnGate3']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfGateViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet52Met6OnGate4']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfGateViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfGateViaCOY)
            self._DesignParameter['_ViaMet52Met6OnGate5']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfGate5ViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfGateViaCOY)
            
            
            #CC VIA GENERATION
            if _NumberOfCCMOSDrainViaCOX is None:
                _NumberOfCCMOSDrainViaCOX =1
            if _NumberOfCCMOSDrainViaCOY is None:
                _NumberOfCCMOSDrainViaCOY = 2
            
            self._DesignParameter['_ViaMet12Met2OnCCDrain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=_NumberOfCCMOSDrainViaCOX, _ViaMet12Met2NumberOfCOY=_NumberOfCCMOSDrainViaCOY)
            self._DesignParameter['_ViaMet22Met3OnCCDrain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=_NumberOfCCMOSDrainViaCOX, _ViaMet22Met3NumberOfCOY=_NumberOfCCMOSDrainViaCOY)
            self._DesignParameter['_ViaMet32Met4OnCCDrain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfCCMOSDrainViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfCCMOSDrainViaCOY)
            
            
            
            
            
            # OUTPUT VIA GENERATION
            if _NumberOfPMOSOutputViaCOY is None:
                _NumberOfPMOSOutputViaCOY = 2
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnPMOSOutput5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfPMOSOutputViaCOY)
            
            if _NumberOfNMOSOutputViaCOY is None:
                _NumberOfNMOSOutputViaCOY = 2
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfNMOSOutputViaCOY)
            
            if _NumberOfCoupledNMOSconnectionViaCOY is None:
                _NumberOfCoupledNMOSconnectionViaCOY = 2
            self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=_NumberOfCoupledNMOSconnectionViaCOY)
            
            
            if _NumberOfParallelViaCOY is None:
                _NumberOfParallelViaCOY = 1
            self._DesignParameter['_ViaMet22Met3OnOutput1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet22Met3OnOutput2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet22Met3OnOutput3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet22Met3OnOutput4']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet22Met3OnOutput5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
            
            self._DesignParameter['_ViaMet32Met4OnOutput1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutput2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutput3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutput4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutput5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            
            self._DesignParameter['_ViaMet42Met5OnOutput1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutput2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutput3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutput4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutput5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            
            self._DesignParameter['_ViaMet52Met6OnOutput1']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet52Met6OnOutput2']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet52Met6OnOutput3']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet52Met6OnOutput4']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet52Met6OnOutput5']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            
            #Via Metal Expand (For Minimum Area DesignRule)
            for j in range(1,6):
                    
                for i in range(1,6):
                    VIA = '_ViaMet' + str(i) + '2Met' + str(i+1) + 'OnGate' + str(j)
                    MET = '_Met' + str(i+1) + 'Layer'
                    
                    Xwidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter[MET]['_XWidth']
                    Ywidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter[MET]['_YWidth']
                    Area = Xwidth * Ywidth
                    if Area < _DRCObj._MetalxMinArea:
                        self._DesignParameter[VIA]['_DesignObj']._DesignParameter[MET]['_XWidth'] = round( (_DRCObj._MetalxMinArea/Ywidth + 0.5) /_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
                    
            
            
            
            # VSS GENERATION
            if _NumberOfSupplyCOY is None :		# Default value is 1
                _NumberOfSupplyCOY = 1
                
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']=_NumberOfSupplyCOY
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOY']=_NumberOfSupplyCOY

            _tmpPbodyObj = PbodyContact._PbodyContact()
            _tmpPbodyObj._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOX=5, _NumberOfPbodyCOY=_PbodyDesignCalculationParameters['_NumberOfPbodyCOY'] , _Met1YWidth = _SupplyMetal1YWidth)
            _tmpNbodyObj = NbodyContact._NbodyContact()
            _tmpNbodyObj._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOX=5, _NumberOfNbodyCOY=_NbodyDesignCalculationParameters['_NumberOfNbodyCOY'] , _Met1YWidth = _SupplyMetal1YWidth)


            _PbodyDesignCalculationParameters['_Met1YWidth']=_SupplyMetal1YWidth
            _NbodyDesignCalculationParameters['_Met1YWidth']=_SupplyMetal1YWidth
            
            
            
            
            # )#####################COORDINATION SETTING#########################
            # if _DistanceBtwSupplyCenter2MOSEdge is None:
                # _DistanceBtwSupplyCenter2MOSEdge = max(_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2 , _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._Metal1MinSpace - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)
                

            if _Vdd2VssHeight is None:
                if _DistanceBtwSupplyCenter2MOSEdge is None:
                    _DistanceBtwSupplyCenter2MOSEdge = max(_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2 , _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._Metal1MinSpace - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)
                _Vdd2VssHeight = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + 2*_DistanceBtwSupplyCenter2MOSEdge
            else : 
                if _DistanceBtwSupplyCenter2MOSEdge is None:
                    # _DistanceBtwSupplyCenter2MOSEdge = round( (_Vdd2VssHeight - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] )/2 / _DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                    _DistanceBtwSupplyCenter2MOSEdge = _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2
            
            # else:
                # _Vdd2VssHeight += _DistanceBtwSupplyCenter2MOSEdge
            _tmpPbodyObj._DesignParameter['_XYCoordinates']=[[0,0]]
            _tmpNbodyObj._DesignParameter['_XYCoordinates']=[[0,_Vdd2VssHeight]] #+ _HeightCalibration]]
            
            
            #MOSFET Coordinate Setting
            if _EdgeBtwNWandPW is None:
                # NMOS_Ylocation = _DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
                # PMOS_Ylocation = _tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] - _DistanceBtwSupplyCenter2MOSEdge - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
                # NMOS_YlocationforCLK = _DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
                # PMOS_YlocationforCLK = _tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] - _DistanceBtwSupplyCenter2MOSEdge - self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
                # NMOS_YlocationforCC = _DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
                _EdgeBtwNWandPW = max(_DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] , _DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'])
                
                
                
            # else:
            NMOS_Ylocation = _EdgeBtwNWandPW - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            PMOS_Ylocation = _EdgeBtwNWandPW + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
            NMOS_YlocationforCLK = _EdgeBtwNWandPW - self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            PMOS_YlocationforCLK = _EdgeBtwNWandPW + self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
            NMOS_YlocationforCC = NMOS_YlocationforCLK  - self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2 + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2
            
            
            MOSspaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            if _Dummy is True:
                MOSPODummy = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
            
            tempX1 = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + MOSspaceDRC
            tempX2 = 0
            if _Dummy is True:
                tempX2 = MOSPODummy * 2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + _DRCObj._PolygateMinSpace
            tempX = max(tempX1,tempX2)
            
            
            tempXforMOS5 = self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + MOSspaceDRC
            tempXforMOS6 = self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + MOSspaceDRC
            tempXforMOS5 =max(tempXforMOS5,tempX2)
            tempXforMOS6 =max(tempXforMOS6,tempX2)
            
            if _XYadjust is None:
                _XYadjust = 0
                
            if _MOSspacebias is not None:
                _MOS12MOS2spacebias = _MOSspacebias
                _MOS22MOS3spacebias = _MOSspacebias
                _MOS32MOS4spacebias = _MOSspacebias
                _MOS42MOS5spacebias = _MOSspacebias
            if _MOS12MOS2spacebias is None:
                _MOS12MOS2spacebias = 0
            if _MOS22MOS3spacebias is None:
                _MOS22MOS3spacebias = 0
            if _MOS32MOS4spacebias is None:
                _MOS32MOS4spacebias = 0
            if _MOS42MOS5spacebias is None:
                _MOS42MOS5spacebias = 0
            if _MOS52MOS6spacebias is None:
                _MOS52MOS6spacebias = 0
            
            
            self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[_XYadjust , NMOS_Ylocation]]
            self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[_XYadjust , PMOS_Ylocation]]
            
            self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[_XYadjust + tempX + _MOS32MOS4spacebias, NMOS_Ylocation]]
            self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[_XYadjust + tempX + _MOS32MOS4spacebias, PMOS_Ylocation]]
            
            self._DesignParameter['_NMOS5']['_XYCoordinates'] = [[_XYadjust + tempX + (tempX + tempXforMOS5)/2 + _MOS32MOS4spacebias + _MOS42MOS5spacebias, NMOS_YlocationforCLK]]
            self._DesignParameter['_PMOS5']['_XYCoordinates'] = [[_XYadjust + tempX + (tempX + tempXforMOS5)/2 + _MOS32MOS4spacebias + _MOS42MOS5spacebias, PMOS_YlocationforCLK]]
            
            self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYadjust - tempX - _MOS22MOS3spacebias, NMOS_Ylocation]]
            self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[_XYadjust - tempX - _MOS22MOS3spacebias, PMOS_Ylocation]]
            
            self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[_XYadjust - 2*tempX - _MOS12MOS2spacebias - _MOS22MOS3spacebias, NMOS_Ylocation]]
            self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[_XYadjust - 2*tempX - _MOS12MOS2spacebias - _MOS22MOS3spacebias, PMOS_Ylocation]]

            self._DesignParameter['_NMOS6']['_XYCoordinates'] = [[_XYadjust + 3*tempX/2 + tempXforMOS5 + tempXforMOS6/2 + _MOS32MOS4spacebias + _MOS42MOS5spacebias + _MOS52MOS6spacebias,NMOS_YlocationforCC ]]
            
            #Gate Via For Cross Coupled NMOS6
            self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'] = [[self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0]\
                                                                              ,self._DesignParameter['_NMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 \
                                                                              +self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 \
                                                                              +_DRCObj._Metal1MinSpace
                                                                              ]]
            
            
            

            #Gate Via Coordinate Setting and Gate Routing
            NSupplytmp=[]
            PSupplytmp=[]
            if _XbiasforGateVia is None:
                _XbiasforGateVia = 0
            if _XbiasforGate6Via is None:
                _XbiasforGate6Via = 0
            for i in range(1,6):
                VIA = '_ViaPoly2Met1OnMOS' + str(i)
                NMOS = '_NMOS' + str(i)  
                PMOS = '_PMOS' + str(i)  
                GATE = '_GateRoutingOnMOS' + str(i)
                AddiGATE = '_AdditionalPOLYRoutingOnMOS' + str(i)
                AddiMET1 = '_AdditionalMet1RoutingOnMOSGate' + str(i)
                
                DIVING_VIA1 = '_ViaMet12Met2OnGate' + str(i)
                DIVING_VIA2 = '_ViaMet22Met3OnGate' + str(i)
                DIVING_VIA3 = '_ViaMet32Met4OnGate' + str(i)
                DIVING_VIA4 = '_ViaMet42Met5OnGate' + str(i)
                DIVING_VIA5 = '_ViaMet52Met6OnGate' + str(i)
                
                
                tmp=[]
                for j in range(0, int(round(len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])/8.0)) ):
                    if len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) is 1:
                        tmp.append([ self._DesignParameter[NMOS]['_XYCoordinates'][0][0], self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2 ])
                    else:
                        tmp.append([ self._DesignParameter[NMOS]['_XYCoordinates'][0][0], self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2 ])
                self._DesignParameter[VIA]['_XYCoordinates'] = [[self._DesignParameter[NMOS]['_XYCoordinates'][0][0], self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2]]
                
                tmp=[]
                for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                    tmp.append( [ [a + b for a, b in zip(self._DesignParameter[NMOS]['_XYCoordinates'][0], self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][j]) ]
                                , [a + b for a, b in zip(self._DesignParameter[PMOS]['_XYCoordinates'][0], self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][j]) ] ] )
                
                self._DesignParameter[GATE]['_Width'] = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                self._DesignParameter[GATE]['_XYCoordinates'] = tmp
                
                Most_Rightside = max(self._DesignParameter[GATE]['_XYCoordinates'][-1][0][0] +self._DesignParameter[GATE]['_Width']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
                Most_Leftside = min(self._DesignParameter[GATE]['_XYCoordinates'][0][0][0] -self._DesignParameter[GATE]['_Width']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
                Most_Upside =self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 
                Most_Downside =self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 
            
                self._DesignParameter[AddiGATE]['_XWidth'] = Most_Rightside - Most_Leftside
                self._DesignParameter[AddiGATE]['_YWidth'] = Most_Upside - Most_Downside
                self._DesignParameter[AddiGATE]['_XYCoordinates'] = [[(Most_Rightside+Most_Leftside)/2,(Most_Downside+Most_Upside)/2]]
                
            

            
            
            
                
                                       
                ############################# WIP ##########################################
                tmp = []



                if _ElementType is '_Inverted':
                    std = len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])
                    for j in range(0, int(round(std/5.0+0.5))):     #Generate 1 Via Per 2 Output Vertical Line
                        # if 4 * j + 1 + 1 > std:
                        tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-(4*j)-1][0] \
                        +self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 - self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 + _XbiasforGateVia,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                        # else:
                            # tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-(4*j)-1-1][0] +_XbiasforGateVia ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                elif _ElementType is '_Vertical':
                    std = len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])
                    for j in range(0, int(round(std/4.0+0.5))):     #Generate 1 Via Per 2 Output Vertical Line
                        tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-(4*j)-1][0] \
                                    -self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2  +_XbiasforGateVia 
                                   ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                        # if 4 * j + 1 + 1 > std:
                            # tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-(4*j)-1][0] + _XbiasforGateVia \
                                        # + self._DesignParameter[
                                       # ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                        # else:
                            # tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-(4*j)-1-1][0] +_XbiasforGateVia ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                else:
                    std = len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])
                    for j in range(0, int(round(std/5.0+0.5))):     #Generate 1 Via Per 2 Output Vertical Line
                        if i is not 5:
                            if 4 * j + 1 + 1 > std:
                                tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-(4*j)-1][0] + _XbiasforGateVia,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                            else:
                                tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-(4*j)-1-1][0] +_XbiasforGateVia ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                        else:
                            if 4 * j + 1 + 1 > std:
                                tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-(4*j)-1][0] + _XbiasforGate6Via,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])
                            else:
                                tmp.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-(4*j)-1-1][0] +_XbiasforGate6Via ,self._DesignParameter[VIA]['_XYCoordinates'][0][1]])

                self._DesignParameter[DIVING_VIA1]['_XYCoordinates'] = tmp
                self._DesignParameter[DIVING_VIA2]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                self._DesignParameter[DIVING_VIA3]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                self._DesignParameter[DIVING_VIA4]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                self._DesignParameter[DIVING_VIA5]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                self._DesignParameter[DIVING_VIA4]['_Ignore'] = True
                self._DesignParameter[DIVING_VIA5]['_Ignore'] = True

                ############################################################################
                
                Most_Rightside = max(self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][0] +self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Most_Leftside = min(self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][0] -self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Most_Upside =max(self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ,  self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][1] +self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                Most_Downside =min(self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 , self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][1] -self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
            
                self._DesignParameter[AddiMET1]['_XWidth'] = Most_Rightside - Most_Leftside
                self._DesignParameter[AddiMET1]['_YWidth'] = Most_Upside - Most_Downside
                self._DesignParameter[AddiMET1]['_XYCoordinates'] = [[float(Most_Rightside+Most_Leftside)/2.0,float(Most_Downside+Most_Upside)/2.0]]
                

                if _ElementType is '_Inverted':
                    for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ):
                        NSupplytmp.append([ [self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                           ,[self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j][0] ,_tmpPbodyObj._DesignParameter['_XYCoordinates'][0][1] - _SupplyMetal1YWidth/2 ] ])

                        PSupplytmp.append([ [self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                           ,[self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j][0] ,_tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] + _SupplyMetal1YWidth/2 ] ])
                else:
                    for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) ):
                        NSupplytmp.append([ [self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                           ,[self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] ,_tmpPbodyObj._DesignParameter['_XYCoordinates'][0][1] - _SupplyMetal1YWidth/2 ] ])

                        PSupplytmp.append([ [self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                           ,[self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] ,_tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] + _SupplyMetal1YWidth/2 ] ])

            if _SupplyRoutingWidth is None:
                _SupplyRoutingWidth = _DRCObj._Metal1MinWidth
            self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _SupplyRoutingWidth
            self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _SupplyRoutingWidth
            self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = NSupplytmp
            self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = PSupplytmp


            #CC NMOS Supply Routing
            tmp = []
            for i in range(0,len(self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] )):
                tmp.append([
                    [self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2  ]
                   ,[self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], _tmpPbodyObj._DesignParameter['_XYCoordinates'][0][1] - _SupplyMetal1YWidth/2  ]
                ])

            self._DesignParameter['_CrossCoupledNMOSSupplyRouting']['_Width'] = _SupplyRoutingWidth
            self._DesignParameter['_CrossCoupledNMOSSupplyRouting']['_XYCoordinates'] = tmp


            
            #Output Via Coordinate Setting and ROUTING
            for i in range(1,6):
                NMOS = '_NMOS' + str(i)  
                PMOS = '_PMOS' + str(i)  
                
                VIA_P = '_ViaMet12Met2OnPMOSOutput' + str(i)
                VIA_N = '_ViaMet12Met2OnNMOSOutput' + str(i)
                VIA_P2 = '_ViaMet22Met3OnPMOSOutput' + str(i)
                VIA_N2 = '_ViaMet22Met3OnNMOSOutput' + str(i)
                    
                VIA1 = '_ViaMet22Met3OnOutput' + str(i)
                VIA2 = '_ViaMet32Met4OnOutput' + str(i)
                VIA3 = '_ViaMet42Met5OnOutput' + str(i)
                VIA4 = '_ViaMet52Met6OnOutput' + str(i)
                
                
                if _PMOSOutputMetalWidth is None:
                    _PMOSOutputMetalWidth = _DRCObj._MetalxMinWidth
                if _NMOSOutputMetalWidth is None:
                    _NMOSOutputMetalWidth = _DRCObj._MetalxMinWidth
                
                if _ElementType is '_Inverted' or _ElementType is '_Vertical':
                    HorizontalMetalOnPMOS = '_OutputMet3HorizontalOnPMOS' + str(i)
                    HorizontalMetalOnNMOS = '_OutputMet3HorizontalOnNMOS' + str(i)
                    self._DesignParameter[HorizontalMetalOnPMOS] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    self._DesignParameter[HorizontalMetalOnNMOS] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    
                    VerticalMetal = '_OutputMet3Vertical' + str(i)
                    self._DesignParameter[VerticalMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                else:
                    HorizontalMetalOnPMOS = '_OutputMet2HorizontalOnPMOS' + str(i)
                    HorizontalMetalOnNMOS = '_OutputMet2HorizontalOnNMOS' + str(i)
                    self._DesignParameter[HorizontalMetalOnPMOS] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    self._DesignParameter[HorizontalMetalOnNMOS] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    VerticalMetal = '_OutputMet2Vertical' + str(i)
                    self._DesignParameter[VerticalMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[VIA_P2]['_Ignore'] = True
                    self._DesignParameter[VIA_N2]['_Ignore'] = True
                   
                # MET2_Vertical = '_OutputMet2Vertical' + str(i)
                
                tmpN=[]
                tmpP=[]
                if _ElementType is '_Inverted':
                    for j in range(1,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])+1 ):
                        tmpN.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-j][0] 
                                   ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA_N]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                        tmpP.append([self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-j][0] 
                                   ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[VIA_P]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                else:
                    for j in range(1,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])+1 ):
                        tmpN.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-j][0] 
                                   ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA_N]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                        tmpP.append([self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-j][0] 
                                   ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[VIA_P]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                self._DesignParameter[VIA_N]['_XYCoordinates'] = tmpN
                self._DesignParameter[VIA_P]['_XYCoordinates'] = tmpP
                self._DesignParameter[VIA_N2]['_XYCoordinates'] = self._DesignParameter[VIA_N]['_XYCoordinates']
                self._DesignParameter[VIA_P2]['_XYCoordinates'] = self._DesignParameter[VIA_P]['_XYCoordinates']
                
                
                self._DesignParameter[VerticalMetal]['_Width'] = _DRCObj._MetalxMinWidth

                self._DesignParameter[HorizontalMetalOnPMOS]['_YWidth'] = _PMOSOutputMetalWidth
                self._DesignParameter[HorizontalMetalOnPMOS]['_XWidth'] = abs(self._DesignParameter[VIA_P]['_XYCoordinates'][0][0] - self._DesignParameter[VIA_P]['_XYCoordinates'][-1][0] )
                self._DesignParameter[HorizontalMetalOnPMOS]['_XYCoordinates'] = [[(a+b)/2 for a,b in zip(self._DesignParameter[VIA_P]['_XYCoordinates'][0] ,self._DesignParameter[VIA_P]['_XYCoordinates'][-1])]]
                self._DesignParameter[HorizontalMetalOnPMOS]['_XYCoordinates'][0][1] += self._DesignParameter[HorizontalMetalOnPMOS]['_YWidth']/2 - self._DesignParameter[VIA_P]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
                
                self._DesignParameter[HorizontalMetalOnNMOS]['_YWidth'] = _NMOSOutputMetalWidth
                self._DesignParameter[HorizontalMetalOnNMOS]['_XWidth'] = abs(self._DesignParameter[VIA_N]['_XYCoordinates'][0][0] - self._DesignParameter[VIA_N]['_XYCoordinates'][-1][0] )
                self._DesignParameter[HorizontalMetalOnNMOS]['_XYCoordinates'] = [[(a+b)/2 for a,b in zip(self._DesignParameter[VIA_N]['_XYCoordinates'][0] ,self._DesignParameter[VIA_N]['_XYCoordinates'][-1])]]
                self._DesignParameter[HorizontalMetalOnNMOS]['_XYCoordinates'][0][1] += -self._DesignParameter[HorizontalMetalOnNMOS]['_YWidth']/2 + self._DesignParameter[VIA_N]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
                
                # self._DesignParameter[MET2_Horizontal]['_XYCoordinates'] = [[self._DesignParameter[VIA_N]['_XYCoordinates'][0] ,self._DesignParameter[VIA_N]['_XYCoordinates'][-1] ]]
                # self._DesignParameter[MET2_Horizontal]['_XYCoordinates'].append([self._DesignParameter[VIA_P]['_XYCoordinates'][0] ,self._DesignParameter[VIA_P]['_XYCoordinates'][-1] ])
                
                tmp = []
                for j in range(0,len(self._DesignParameter[VIA_N]['_XYCoordinates'])):
                    if j % 2 is 0:
                        tmp.append([self._DesignParameter[VIA_N]['_XYCoordinates'][j] ,self._DesignParameter[VIA_P]['_XYCoordinates'][j] ])
                self._DesignParameter[VerticalMetal]['_XYCoordinates'] = tmp
                
                
                XYofVIAtmp = []
                if _ElementType is '_Inverted':
                    for j in range(0,int(round(len(self._DesignParameter[VerticalMetal]['_XYCoordinates'])/2.0)) ):
                        XYofVIAtmp.append([ self._DesignParameter[VerticalMetal]['_XYCoordinates'][2*j][0][0] - self._DesignParameter[VIA1]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[VerticalMetal]['_Width']/2
                                          , self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2 ])
                else :
                    for j in range(0,int(round(len(self._DesignParameter[VerticalMetal]['_XYCoordinates'])/2.0)) ):
                        XYofVIAtmp.append([ self._DesignParameter[VerticalMetal]['_XYCoordinates'][2*j][0][0] + self._DesignParameter[VIA1]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter[VerticalMetal]['_Width']/2
                                          , self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2 ])
                                      
                print XYofVIAtmp
                self._DesignParameter[VIA1]['_XYCoordinates'] = XYofVIAtmp
                self._DesignParameter[VIA2]['_XYCoordinates'] = self._DesignParameter[VIA1]['_XYCoordinates']
                self._DesignParameter[VIA3]['_XYCoordinates'] = self._DesignParameter[VIA1]['_XYCoordinates']
                self._DesignParameter[VIA4]['_XYCoordinates'] = self._DesignParameter[VIA1]['_XYCoordinates']
                
            ######Coupled NMOS Connection VIA ########
            tmp = []
            
            if len(self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) >= 2:
                for i in range(0,len(self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                    tmp.append([a+b for a,b in zip(
                                self._DesignParameter['_NMOS6']['_XYCoordinates'][0],
                                self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i]
                                )])
                    tmp[i][1] -= (self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
                self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_XYCoordinates'] = tmp
                # self._DesignParameter['_NMOS6']['_XYCoordinates'][0]
                # self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i]
                # self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                # self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                if _CCconnectionMetWidht is None:
                    _CCconnectionMetWidht = _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossCoupledConnectionMet2']['_Width'] = _CCconnectionMetWidht
                self._DesignParameter['_CrossCoupledConnectionMet2']['_XYCoordinates'] = [[copy.deepcopy(tmp[0]),copy.deepcopy(tmp[-1])]]
                self._DesignParameter['_CrossCoupledConnectionMet2']['_XYCoordinates'][0][0][0] += -(self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
                self._DesignParameter['_CrossCoupledConnectionMet2']['_XYCoordinates'][0][-1][0] += self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                self._DesignParameter['_CrossCoupledConnectionMet2']['_XYCoordinates'][0][0][1] += self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - float(_CCconnectionMetWidht)/2
                self._DesignParameter['_CrossCoupledConnectionMet2']['_XYCoordinates'][0][-1][1] += self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - float(_CCconnectionMetWidht)/2

                
            
            
            
            
            
            
            ### CROSS COUPLED Drain Connection With Output of INV ###
            self._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'] = [[ self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]  
                                                                                  ,self._DesignParameter['_ViaPoly2Met1OnMOS5']['_XYCoordinates'][0][1]
                                                                                ]]
            self._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'] = copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'])
            self._DesignParameter['_ViaMet32Met4OnCCDrain']['_XYCoordinates'] = copy.deepcopy(self._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'])
            
            if CCdrainMet1Width is None:
                CCdrainMet1Width = _DRCObj._Metal1MinWidth
            self._DesignParameter['_CrossCoupledDrainMet1']['_Width'] = CCdrainMet1Width
            self._DesignParameter['_CrossCoupledDrainMet1']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0],
                                                                                   [a+b for a,b in zip(self._DesignParameter['_NMOS6']['_XYCoordinates'][0], self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0] ) ]
                                                                                ]]
                                                                                
            
            self._DesignParameter['_CrossCoupledDrainMet2']['_Width'] = self._DesignParameter['_ViaMet12Met2OnCCDrain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
            self._DesignParameter['_CrossCoupledDrainMet2']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0]
                                                                                  ,self._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0]
                                                                                ]]
            
            
            # _CrossCoupledDrainMet1
            
            
            # _ViaMet12Met2OnCCDrain
            
            
            
            
            
            
            
            
            
            
            
            
            # BodyContact Adjusting
            _LengthOfBody = self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']
            leftSideOD = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2 
            rightSideOD = self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2
            rightSideODOriginal = self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2
            _LengthOfOD = abs(rightSideOD - leftSideOD )

            if _NumberOfSupplyCOX is None:
                _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 \
                        else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))
            _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX
            _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX
            _PbodyDesignCalculationParameters['_Met1YWidth'] = _SupplyMetal1YWidth
            _NbodyDesignCalculationParameters['_Met1YWidth'] = _SupplyMetal1YWidth

            self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)
            self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)
            self._DesignParameter['_PbodyContact']['_XYCoordinates'] = _tmpPbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_NbodyContact']['_XYCoordinates'] = _tmpNbodyObj._DesignParameter['_XYCoordinates']
            self._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0] = (leftSideOD+rightSideOD)/2
            self._DesignParameter['_NbodyContact']['_XYCoordinates'][0][0] = (leftSideOD+rightSideOD)/2

            del _tmpPbodyObj
            del _tmpNbodyObj
            
            


            Right_Side = self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2 + 400
            Left_Side = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            NMOS_NPlength = Right_Side - Left_Side
            if _EdgeBtwNWandPW is None:
                _EdgeBtwNWandPW = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            
            #Need To Be Fix
            # )################################ NWELL ################################
            self._DesignParameter['_NWell']['_XWidth']= round((NMOS_NPlength + _DRCObj._NwMinEnclosurePactive*2)/2/_DRCObj._MinSnapSpacing) * 2 * _DRCObj._MinSnapSpacing
            self._DesignParameter['_NWell']['_YWidth']= _Vdd2VssHeight - _EdgeBtwNWandPW + (float (self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            self._DesignParameter['_NWell']['_XYCoordinates'] = [[(Right_Side+Left_Side)/2, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _EdgeBtwNWandPW  ]]
            # )################################ NP UnderNMOS )################################
            tmp = [[(Right_Side + Left_Side)/2, 0]]
            # self._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'] = tmp
            # self._DesignParameter['_NIMPUnderNMOS']['_XWidth']= round( (abs(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) + abs(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            self._DesignParameter['_NIMPUnderNMOS']['_XWidth'] = NMOS_NPlength
            self._DesignParameter['_NIMPUnderNMOS']['_YWidth']= _EdgeBtwNWandPW - self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
            # tmp[0][1] = tmp[0][1] + (float)(_EdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2)/2 -self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            tmp[0][1] = _EdgeBtwNWandPW - self._DesignParameter['_NIMPUnderNMOS']['_YWidth']/2
            self._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'] = tmp
            # )################################ PP UnderPMOS )################################
            # self._DesignParameter['_PIMPUnderPMOS']['_XWidth']= round( (abs(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) + abs(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            self._DesignParameter['_PIMPUnderPMOS']['_XWidth'] = NMOS_NPlength
            self._DesignParameter['_PIMPUnderPMOS']['_YWidth']=  _Vdd2VssHeight - _EdgeBtwNWandPW - self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            tmp = [[(Right_Side + Left_Side)/2, 0]]
            # tmp[0][1] = tmp[0][1] - ((self._DesignParameter['_PIMPUnderPMOS']['_YWidth'])/2 - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)
            tmp[0][1] =_EdgeBtwNWandPW + self._DesignParameter['_PIMPUnderPMOS']['_YWidth']/2
            self._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'] = tmp

            

            
            
            # Parallel Metal Y Location 
            if _MetalxDRC is None:
                _MetalxDRC = _DRCObj._MetalxMinSpace
            if _ParallelMetalWidth is None:
                _ParallelMetalWidth = _DRCObj._MetalxMinWidth
            if _TreeLevel is None:
                _TreeLevel = 1
            
            # _LayerLevel = int((_TreeLevel-1)/3)     #Layer Level means: Data Path Metal layer's Level
            # RailType = (_TreeLevel-1) % 3
            _LayerLevel = 0     #Ver2. Fixed Value
            RailType = 1        #Ver2. Fixed Value
            
            # RailType = 0 #Input Is Lower Layer, Output Is Normal Layer
            # RailType = 1 #Input And Output Is Same Layer (Normal)
            # RailType = 2 #Input Is Normal Layer, Output Is Upper Layer -- >WRONG
            # RailType = 2 #Input And Output Is Same Layer (Normal)
            
            
            NP_EdgeLocationY = max(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2,
                                   self._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2,
                                   self._DesignParameter['_NMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)
            
            setting = 1
            for i in range(1,6):
                IL = 'InLinelocation'+str(i)
                OL = 'OutLinelocation' + str(i)
                if InLinelocation1 is not None:
                    setting = 0
                    self._ParametersForDesignCalculation['InLinelocation1'] = InLinelocation1
                    self._ParametersForDesignCalculation['InLinelocation2'] = InLinelocation2
                    self._ParametersForDesignCalculation['InLinelocation3'] = InLinelocation3
                    self._ParametersForDesignCalculation['InLinelocation4'] = InLinelocation4
                    self._ParametersForDesignCalculation['InLinelocation5'] = InLinelocation5
                    self._ParametersForDesignCalculation['OutLinelocation1'] = OutLinelocation1
                    self._ParametersForDesignCalculation['OutLinelocation2'] = OutLinelocation2
                    self._ParametersForDesignCalculation['OutLinelocation3'] = OutLinelocation3
                    self._ParametersForDesignCalculation['OutLinelocation4'] = OutLinelocation4
                    self._ParametersForDesignCalculation['OutLinelocation5'] = OutLinelocation5
            
            
            if setting is 1:
                if RailType is 0 or RailType is 2:   
                    if _LayerLevel is 0:
                        standardLevel = 0
                    else:
                        standardLevel = _LayerLevel - 1
                    
                    if standardLevel % 2 is 0: # Two lines on NMOS, Three lines on PMOS
                        self._ParametersForDesignCalculation['InLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+2)  - _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+1)  - _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+1)  + _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+2)  + _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation5'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+3)  + _ParallelMetalWidth * ((10*standardLevel/2 +5)/float(2))
                    else : #Two lines on PMOS, Three lines on NMOS
                        self._ParametersForDesignCalculation['InLinelocation5'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2))    - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-2)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -5)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2))    + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))
                    
                    if _LayerLevel is 0:
                        standardLevel = 0
                    else:
                        standardLevel = _LayerLevel                
                    
                    if standardLevel % 2 is 0: # Two lines on NMOS, Three lines on PMOS
                        self._ParametersForDesignCalculation['OutLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+2)  - _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+1)  - _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+1)  + _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+2)  + _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation5'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+3)  + _ParallelMetalWidth * ((10*standardLevel/2 +5)/float(2))
                    else : #Two lines on PMOS, Three lines on NMOS
                        self._ParametersForDesignCalculation['OutLinelocation5'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2))    - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-2)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -5)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2))    + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))

                elif RailType is 1:
                    standardLevel = _LayerLevel 
                    if standardLevel % 2 is 0:     # Two lines on NMOS, Three lines on PMOS

                        self._ParametersForDesignCalculation['InLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+2)  - _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*standardLevel/2+1)  - _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+1)  + _ParallelMetalWidth * ((10*standardLevel/2 +1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+2)  + _ParallelMetalWidth * ((10*standardLevel/2 +3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation5'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*standardLevel/2+3)  + _ParallelMetalWidth * ((10*standardLevel/2 +5)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation1'] = self._ParametersForDesignCalculation['InLinelocation1']
                        self._ParametersForDesignCalculation['OutLinelocation2'] = self._ParametersForDesignCalculation['InLinelocation2']
                        self._ParametersForDesignCalculation['OutLinelocation3'] = self._ParametersForDesignCalculation['InLinelocation3']
                        self._ParametersForDesignCalculation['OutLinelocation4'] = self._ParametersForDesignCalculation['InLinelocation4']
                        self._ParametersForDesignCalculation['OutLinelocation5'] = self._ParametersForDesignCalculation['InLinelocation5']
                    else : #Two lines on PMOS, Three lines on NMOS
                        self._ParametersForDesignCalculation['InLinelocation5'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2))    - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation1'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation2'] = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * (5*round((standardLevel+0.5)/2)-2)  - _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -5)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation3'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2)-1)  + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -3)/float(2))
                        self._ParametersForDesignCalculation['InLinelocation4'] = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * (5*round((standardLevel+0.5)/2))    + _ParallelMetalWidth * ((10*round((standardLevel+0.5)/2) -1)/float(2))
                        self._ParametersForDesignCalculation['OutLinelocation1'] = self._ParametersForDesignCalculation['InLinelocation1']
                        self._ParametersForDesignCalculation['OutLinelocation2'] = self._ParametersForDesignCalculation['InLinelocation2']
                        self._ParametersForDesignCalculation['OutLinelocation3'] = self._ParametersForDesignCalculation['InLinelocation3']
                        self._ParametersForDesignCalculation['OutLinelocation4'] = self._ParametersForDesignCalculation['InLinelocation4']
                        self._ParametersForDesignCalculation['OutLinelocation5'] = self._ParametersForDesignCalculation['InLinelocation5']
                
             

                if _TreeLevel is _TotalLevel:
                    self._ParametersForDesignCalculation['OutLinelocation1'] = self._ParametersForDesignCalculation['InLinelocation1']
                    self._ParametersForDesignCalculation['OutLinelocation2'] = self._ParametersForDesignCalculation['InLinelocation2']
                    self._ParametersForDesignCalculation['OutLinelocation3'] = self._ParametersForDesignCalculation['InLinelocation3']
                    self._ParametersForDesignCalculation['OutLinelocation4'] = self._ParametersForDesignCalculation['InLinelocation4']
                    self._ParametersForDesignCalculation['OutLinelocation5'] = self._ParametersForDesignCalculation['InLinelocation5']

            # # # # # # BasicLine1 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 2  - _ParallelMetalWidth * (3/2)
            # # # # # # BasicLine2 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 1  - _ParallelMetalWidth * (1/2)
            # # # # # # BasicLine3 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 1  + _ParallelMetalWidth * (1/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 2  + _ParallelMetalWidth * (3/2)
            # # # # # # BasicLine5 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 3  + _ParallelMetalWidth * (5/2)
            
            # # # # # # BasicLine1 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 5  - _ParallelMetalWidth * (9/2)
            # # # # # # BasicLine2 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 4  - _ParallelMetalWidth * (7/2)
            # # # # # # BasicLine3 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 3  - _ParallelMetalWidth * (5/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 4  + _ParallelMetalWidth * (7/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 5  + _ParallelMetalWidth * (9/2)
            
            # # # # # # BasicLine1 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 7  - _ParallelMetalWidth * (13/2)
            # # # # # # BasicLine2 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 6  - _ParallelMetalWidth * (11/2)
            # # # # # # BasicLine3 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 6  + _ParallelMetalWidth * (11/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 7  + _ParallelMetalWidth * (13/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 8  + _ParallelMetalWidth * (15/2)
            
            # # # # # # BasicLine1 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 10  - _ParallelMetalWidth * (19/2)
            # # # # # # BasicLine2 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 9  - _ParallelMetalWidth * (17/2)
            # # # # # # BasicLine3 = NP_EdgeLocationY - self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - _MetalxDRC * 8  - _ParallelMetalWidth * (15/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 9  + _ParallelMetalWidth * (17/2)
            # # # # # # BasicLine4 = NP_EdgeLocationY + self._DesignParameter['_ViaMet22Met3OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 + _MetalxDRC * 10  + _ParallelMetalWidth * (19/2)
            #
            
            #Additional OutPut Metal2 with Via and OutputConnection Metal
            if _ElementType is '_Inverted' :
                print 'not implemented yet'
            elif _ElementType is '_Vertical' :
                print 'not implemented yet'
            else:
                for i in range(1,6):
                    Output2ViaAdiMetforLowerRes = '_OutputConnectionAndOutputviaMet2OnMOS' + str(i)
                    self._DesignParameter[Output2ViaAdiMetforLowerRes] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    tmp = []
                    for j in range(0,len(self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'])):
                    # HorizontalMetalOnPMOS = '_OutputMet2HorizontalOnPMOS' + str(i)
                        hUP = self._DesignParameter['_OutputMet2HorizontalOnPMOS'+str(i)]['_XYCoordinates'][0][1] + self._DesignParameter['_OutputMet2HorizontalOnPMOS'+str(i)]['_YWidth']/2
                        hDOWN = self._DesignParameter['_OutputMet2HorizontalOnNMOS'+str(i)]['_XYCoordinates'][0][1] - self._DesignParameter['_OutputMet2HorizontalOnNMOS'+str(i)]['_YWidth']/2
                        vLeft = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
                        vRight = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
                        tmp.append([(vLeft+vRight)/2,(hUP+hDOWN)/2] )
                    self._DesignParameter[Output2ViaAdiMetforLowerRes]['_XYCoordinates'] = tmp
                    self._DesignParameter[Output2ViaAdiMetforLowerRes]['_XWidth'] = vRight - vLeft
                    self._DesignParameter[Output2ViaAdiMetforLowerRes]['_YWidth'] = hUP - hDOWN
                    
            
            
            
            
            
            # # # # )################################ DRC Verification ################################
            
            DRC_PASS=1
            
            if _ElementType is '_Inverted' :
                # VIA for GATE X location adjusting 
                viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0]
                leftIndex = 0
                RightIndex = 0
                for i in range(0, len(self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates']) ):
                    if (self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][-i][0][0] < viaXlocation):
                        leftIndex = -i-1
                    if (self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][i][0][0] > viaXlocation):
                        RightIndex = i

                leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_OutputMet3Vertical1']['_Width']/2
                if (leftSpace < _DRCObj._MetalxMinSpace): # and (leftIndex is not 0):
                    _XbiasforGateVia += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                    viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0] + _XbiasforGateVia

                rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_OutputMet3Vertical1']['_Width']/2
                if rightSpace < _DRCObj._MetalxMinSpace and (RightIndex is not 0):
                    _XbiasforGateVia -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
            elif _ElementType is '_Vertical':
                # VIA for GATE X location adjusting 
                viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0]
                # leftIndex = 0
                # RightIndex = 0
                # for i in range(0, len(self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates']) ):
                    # if (self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][-i][0][0] < viaXlocation):
                        # leftIndex = -i-1
                    # if (self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][i][0][0] > viaXlocation):
                        # RightIndex = i

                # leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_OutputMet3Vertical1']['_Width']/2
                # if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                    # _XbiasforGateVia += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    # DRC_PASS = 0
                    # viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0] + _XbiasforGateVia

                # rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_OutputMet3Vertical1']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_OutputMet3Vertical1']['_Width']/2
                # if rightSpace < _DRCObj._MetalxMinSpace :
                    # _XbiasforGateVia -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    # DRC_PASS = 0
            else:
                # VIA for GATE X location adjusting 
                viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0]
                leftIndex = 0
                RightIndex = 0
                for i in range(0, len(self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates']) ):
                    if (self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][-i][0][0] < viaXlocation):
                        leftIndex = -i
                    if (self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][i][0][0] > viaXlocation):
                        RightIndex = i

                leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_OutputMet2Vertical1']['_Width']/2
                if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                    _XbiasforGateVia += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                    viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0] + _XbiasforGateVia

                rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_OutputMet2Vertical1']['_Width']/2
                if rightSpace < _DRCObj._MetalxMinSpace:
                    _XbiasforGateVia -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0

                viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate5']['_XYCoordinates'][0][0]
                leftIndex = 0
                RightIndex = 0
                for i in range(0, len(self._DesignParameter['_OutputMet2Vertical5']['_XYCoordinates']) ):
                    if (self._DesignParameter['_OutputMet2Vertical5']['_XYCoordinates'][-i][0][0] < viaXlocation):
                        leftIndex = -i
                    if (self._DesignParameter['_OutputMet2Vertical5']['_XYCoordinates'][i][0][0] > viaXlocation):
                        RightIndex = i

                leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate5']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_OutputMet2Vertical5']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_OutputMet2Vertical5']['_Width']/2
                if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                    _XbiasforGate6Via += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
                    viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate5']['_XYCoordinates'][0][0] + _XbiasforGate6Via

                rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate5']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_OutputMet2Vertical5']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_OutputMet2Vertical5']['_Width']/2
                if rightSpace < _DRCObj._MetalxMinSpace:
                    _XbiasforGate6Via -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0


            
            
            
            # VIA for Output Met3 Area
            if _ElementType is not '_Inverted' and _ElementType is not '_Vertical':
                tmp = []
                for i in range(1,6):
                    for j in range(0,len(self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'])):
                        Xstandard = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][0] - self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2
                        Xlen = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                        Ylen = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                        if Xlen*Ylen < _DRCObj._MetalxMinArea:
                            newXwidth = round( _DRCObj._MetalxMinArea/Ylen/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            if _ElementType is not '_Inverted':
                                tmp.append([Xstandard + newXwidth/2 ,self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][1]])
                            else:
                                tmp.append([Xstandard - newXwidth/2 ,self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][1]])
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_XWidth'] = newXwidth
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_YWidth'] = Ylen
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_XYCoordinates'] = tmp
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_Ignore'] = self._DesignParameter['_ViaMet22Met3OnOutput1']['_Ignore']
            
            
            # VIA for Output Connection Met2 Area
            if _ElementType is '_Inverted' or _ElementType is '_Vertical':
                Xwidth = self._DesignParameter['_ViaMet22Met3OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                Ywidth = self._DesignParameter['_ViaMet22Met3OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
                if Xwidth * Ywidth < _DRCObj._MetalxMinArea:
                    NewYwidth = round(_DRCObj._MetalxMinArea / Xwidth / _DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    YlocationParameter = (NewYwidth - Ywidth)/2
                    tmp = []
                    for i in range(1,6):
                        for j in range(0, len(self._DesignParameter['_ViaMet22Met3OnNMOSOutput'+str(i)]['_XYCoordinates']) ):
                            tmp.append([a-b for a,b in zip(self._DesignParameter['_ViaMet22Met3OnNMOSOutput'+str(i)]['_XYCoordinates'][j], [0,YlocationParameter] ) ])
                    
                    self._DesignParameter['_AdditionalMet2OnNMOS']['_XWidth'] = Xwidth
                    self._DesignParameter['_AdditionalMet2OnNMOS']['_YWidth'] = NewYwidth
                    self._DesignParameter['_AdditionalMet2OnNMOS']['_XYCoordinates'] = tmp
            
            
            
            # VIA for Output Met3 Area
            if _ElementType is '_Inverted': 
                tmp = []
                for i in range(1,6):
                    for j in range(0,len(self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'])):
                        Xstandard = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][0] - self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2
                        Xlen = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                        Ylen = self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                        if Xlen*Ylen < _DRCObj._MetalxMinArea:
                            newXwidth = round( _DRCObj._MetalxMinArea/Ylen/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                            if _ElementType is not '_Inverted':
                                tmp.append([Xstandard + newXwidth/2 ,self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][1]])
                            else:
                                tmp.append([Xstandard - newXwidth/2 ,self._DesignParameter['_ViaMet22Met3OnOutput'+str(i)]['_XYCoordinates'][j][1]])
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_XWidth'] = newXwidth
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_YWidth'] = Ylen
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_XYCoordinates'] = tmp
                            self._DesignParameter['_AdditionalMet3RoutingOnOutput']['_Ignore'] = self._DesignParameter['_ViaMet22Met3OnOutput1']['_Ignore']
            
                
            
            
            
            
            
            # Does Parallel MetalLine locate inside of VDD2VSS Height?
            DistanceBtwPbody2OutLineBot = min(self._ParametersForDesignCalculation['OutLinelocation1'], self._ParametersForDesignCalculation['OutLinelocation2'],self._ParametersForDesignCalculation['OutLinelocation3'],self._ParametersForDesignCalculation['OutLinelocation4'],self._ParametersForDesignCalculation['OutLinelocation5']) \
                                        - _ParallelMetalWidth/2 -self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            DistanceBtwNbody2OutLineTop = self._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] \
                                        -max(self._ParametersForDesignCalculation['OutLinelocation1'], self._ParametersForDesignCalculation['OutLinelocation2'],self._ParametersForDesignCalculation['OutLinelocation3'],self._ParametersForDesignCalculation['OutLinelocation4'],self._ParametersForDesignCalculation['OutLinelocation5']) \
                                        - _ParallelMetalWidth/2 -self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            
            # if DistanceBtwPbody2OutLineBot < _DRCObj._MetalxMinSpace or DistanceBtwNbody2OutLineTop < _DRCObj._MetalxMinSpace:
            #     _DistanceBtwSupplyCenter2MOSEdge += max((_DRCObj._MetalxMinSpace-DistanceBtwPbody2OutLineBot),(_DRCObj._MetalxMinSpace-DistanceBtwNbody2OutLineTop))
            #     # _Vdd2VssHeight += 2 * max((_DRCObj._MetalxMinSpace-DistanceBtwPbody2OutLineBot),(_DRCObj._MetalxMinSpace-DistanceBtwNbody2OutLineTop))
            #     _Vdd2VssHeight = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + 2*_DistanceBtwSupplyCenter2MOSEdge
            #     DRC_PASS = 0



            # AddiMet1 For N,P Via and Channel
            tmpN = []
            tmpP = []
            for i in range(1,5):
                NMOS = '_NMOS' + str(i)
                PMOS = '_PMOS' + str(i)
                if _ElementType is '_Inverted':
                    for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                        tmpN.append([a+b for a,b in zip(self._DesignParameter[NMOS]['_XYCoordinates'][0],self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j])])
                        tmpP.append([a+b for a,b in zip(self._DesignParameter[PMOS]['_XYCoordinates'][0],self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j])])
                else :
                    for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                        tmpN.append([a+b for a,b in zip(self._DesignParameter[NMOS]['_XYCoordinates'][0],self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j])])
                        tmpP.append([a+b for a,b in zip(self._DesignParameter[PMOS]['_XYCoordinates'][0],self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j])])
                        
            self._DesignParameter['_AdditionalMet1OnNMOS']['_XYCoordinates'] =tmpN
            self._DesignParameter['_AdditionalMet1OnPMOS']['_XYCoordinates'] =tmpP
            self._DesignParameter['_AdditionalMet1OnNMOS']['_XWidth'] =self._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet1OnNMOS']['_YWidth'] =self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_AdditionalMet1OnPMOS']['_XWidth'] =self._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet1OnPMOS']['_YWidth'] =self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            ####Addi Met1 for MOS5 ####
            tmpN = []
            tmpP = []
            if _ElementType is '_Inverted':
                for j in range(0,len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                    tmpN.append([a+b for a,b in zip(self._DesignParameter['_NMOS5']['_XYCoordinates'][0],self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j])])
                    tmpP.append([a+b for a,b in zip(self._DesignParameter['_PMOS5']['_XYCoordinates'][0],self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j])])
            else :
                for j in range(0,len(self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
                    tmpN.append([a+b for a,b in zip(self._DesignParameter['_NMOS5']['_XYCoordinates'][0],self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][j])])
                    tmpP.append([a+b for a,b in zip(self._DesignParameter['_PMOS5']['_XYCoordinates'][0],self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][j])])
        
            self._DesignParameter['_AdditionalMet1OnNMOS5']['_XYCoordinates'] = tmpN
            self._DesignParameter['_AdditionalMet1OnPMOS5']['_XYCoordinates'] = tmpP
            self._DesignParameter['_AdditionalMet1OnNMOS5']['_XWidth'] =self._DesignParameter['_ViaMet12Met2OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet1OnNMOS5']['_YWidth'] =self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_AdditionalMet1OnPMOS5']['_XWidth'] =self._DesignParameter['_ViaMet12Met2OnPMOSOutput5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet1OnPMOS5']['_YWidth'] =self._DesignParameter['_PMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            ####Addi Met1 for MOS6 ####
            if len(self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) >= 2:
                tmpN = []
                tmpP = []
                for j in range(0,len(self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
                    tmpN.append([a+b for a,b in zip(self._DesignParameter['_NMOS6']['_XYCoordinates'][0],self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j])])
            
                self._DesignParameter['_AdditionalMet1OnNMOS6']['_XYCoordinates'] = tmpN
                self._DesignParameter['_AdditionalMet1OnNMOS6']['_XWidth'] =self._DesignParameter['_ViaMet12Met2OnNMOS6Connection']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                self._DesignParameter['_AdditionalMet1OnNMOS6']['_YWidth'] =self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

                if self._DesignParameter['_AdditionalMet1OnNMOS6']['_XWidth'] * self._DesignParameter['_AdditionalMet1OnNMOS6']['_YWidth'] < _DRCObj._Metal1MinArea:
                    newY =  round(_DRCObj._Metal1MinArea / self._DesignParameter['_AdditionalMet1OnNMOS6']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    Ycalibre = float(newY - self._DesignParameter['_AdditionalMet1OnNMOS6']['_YWidth']) / 2
                    for j in range(0,len(self._DesignParameter['_AdditionalMet1OnNMOS6']['_XYCoordinates'])):
                        self._DesignParameter['_AdditionalMet1OnNMOS6']['_XYCoordinates'][j][1] -= Ycalibre
                    self._DesignParameter['_AdditionalMet1OnNMOS6']['_YWidth'] = newY
            
            
            
            
            # AddiMet1 for N P output Met1 Area
            if self._DesignParameter['_AdditionalMet1OnNMOS']['_XWidth'] * self._DesignParameter['_AdditionalMet1OnNMOS']['_YWidth'] < _DRCObj._Metal1MinArea:
                newY =  round(_DRCObj._Metal1MinArea / self._DesignParameter['_AdditionalMet1OnNMOS']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                Ycalibre = float(newY - self._DesignParameter['_AdditionalMet1OnNMOS']['_YWidth']) / 2
                for j in range(0,len(self._DesignParameter['_AdditionalMet1OnNMOS']['_XYCoordinates'])):
                    self._DesignParameter['_AdditionalMet1OnNMOS']['_XYCoordinates'][j][1] -= Ycalibre
                self._DesignParameter['_AdditionalMet1OnNMOS']['_YWidth'] = newY
            
            if self._DesignParameter['_AdditionalMet1OnNMOS5']['_XWidth'] * self._DesignParameter['_AdditionalMet1OnNMOS5']['_YWidth'] < _DRCObj._Metal1MinArea:
                newY =  round(_DRCObj._Metal1MinArea / self._DesignParameter['_AdditionalMet1OnNMOS5']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                Ycalibre = float(newY - self._DesignParameter['_AdditionalMet1OnNMOS5']['_YWidth']) / 2
                for j in range(0,len(self._DesignParameter['_AdditionalMet1OnNMOS5']['_XYCoordinates'])):
                    self._DesignParameter['_AdditionalMet1OnNMOS5']['_XYCoordinates'][j][1] -= Ycalibre
                self._DesignParameter['_AdditionalMet1OnNMOS5']['_YWidth'] = newY
            
            
            # self._DesignParameter['_Node6']['_Ignore']=True

            
            
            
            
            ########### NMOS6 GateVia X coordinate Setting ##########
            if _XbiasForCoupledMOSGateVia is None:
                _XbiasForCoupledMOSGateVia = 0
            
            ViaMet1Left = self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            MOSMet1Right = self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            if (ViaMet1Left - MOSMet1Right) < _DRCObj._Metal1MinSpace:
                self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] += (_DRCObj._Metal1MinSpace - (ViaMet1Left - MOSMet1Right) )
            self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] += _XbiasForCoupledMOSGateVia
            
                
            self._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'] = copy.deepcopy(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'])
            self._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][0] += (self._DesignParameter['_ViaMet12Met2OnGate6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            
            ########### Additional Poly For NMOS6 ##############
            
            MOS6_PolyEdgeY = self._DesignParameter['_NMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2
            
            
            BotY = min( self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2
                       ,MOS6_PolyEdgeY)
            TopY = max( self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2
                       ,MOS6_PolyEdgeY)
            LeftX = min(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2
                       ,self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2  )
            RightX = max(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2
                       ,self._DesignParameter['_NMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] + self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2  )
            
            
            self._DesignParameter['_AdditionalPOLYRoutingOnMOS6']['_XYCoordinates'] = [[(LeftX+RightX)/2,(TopY+BotY)/2]]
            self._DesignParameter['_AdditionalPOLYRoutingOnMOS6']['_XWidth'] = RightX - LeftX
            self._DesignParameter['_AdditionalPOLYRoutingOnMOS6']['_YWidth'] = TopY - BotY
            
            BotY = min(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                      ,self._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnGate6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
            TopY = max(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                      ,self._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnGate6']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)
            RightX = max(self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                      ,self._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnGate6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)
            LeftX = self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            
            self._DesignParameter['_AdditionalMet1RoutingOnMOSGate6']['_XYCoordinates'] = [[(LeftX+RightX)/2,(TopY+BotY)/2]]
            self._DesignParameter['_AdditionalMet1RoutingOnMOSGate6']['_XWidth'] = RightX - LeftX
            self._DesignParameter['_AdditionalMet1RoutingOnMOSGate6']['_YWidth'] = TopY - BotY
            
            
            # min()
            # self._DesignParameter['_ViaPoly2Met1OnMOS6']['_XYCoordinates'][0][1]
            # self._DesignParameter['_ViaPoly2Met1OnMOS6']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2
            
            # self._DesignParameter['_NMOS6']['_XYCoordinates'][0][1]
            # self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]
            # self._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2
            
            ############ Additional Met1 For NMOS6 ########
            
            

            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print '#########################################################################################################'
        print '                                    {}  ClkTreeElement Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'

        


if __name__=='__main__':


                
    ##############delayUnit #####################################################################
    CLKtreeElementObj=_ClkTreeElement(_DesignParameter=None, _Name='ClkTreeElement')
    CLKtreeElementObj._CalculateDesignParameter(
    
                                        _NumberOfGate=4, _ChannelWidth=630, _ChannelLength=60, _PNChannelRatio=1500./630.,

                                        _SupplyMetal1YWidth=300, 

                                        _Vdd2VssHeight=3700, _HeightCalibration=None, _NumberOfParallelViaCOY = 2,
                                        _NumberOfCCMOSDrainViaCOX = 1, _NumberOfCCMOSDrainViaCOY = 2,
                                        _NumberOfCoupledGate=3, _CoupledChannelWidth=220,
                                        _NumberOfCoupledMOSGateViaCOX = 2,
                                     # _NWellexpandXonFF = 500, _PPexpandXonFF = 300, _NPexpandXonFF = 400,
                                     # _NWellexpandXonXOR = 500, _PPexpandXonXOR = 300, _NPexpandXonXOR = 400,
                                     # _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitDesign._DelayUnitDesign),
                                      # _INVNumberOfGate=4, _INVChannelWidth=350, _INVChannelLength=50, _INVPNChannelRatio=2, _XORVdd2VssHeight=3700, _HeightCalOption='ON',\
                                      # _NumberOfGate1=3, _ChannelWidth1=350, _ChannelLength1=50, _PNChannelRatio1=2, \
                                      # _NumberOfGate2=4, _ChannelWidth2=350, _ChannelLength2=50, _PNChannelRatio2=2, \
                                      # _NumberOfGate3=4, _ChannelWidth3=350, _ChannelLength3=50, _PNChannelRatio3=2, \
                                      # _NumberOfGate4=3, _ChannelWidth4=350, _ChannelLength4=50, _PNChannelRatio4=2, \
                                         # _NumberOfNMOSConnectionViaCOY = 2, _NumberOfPMOSConnectionViaCOY =4, _NumberOfPMOSOutputViaCOY= 4,
                                         # _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                         # _BiasDictforViaPoly2Met1OnGate = {
                                         # '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None, \
                                         # '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None, \
                                         # '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None, \
                                         # '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0, \
                                         # '_XbiasInvNMOSGateVia':None,    '_YbiasInvNMOSGateVia':None,   '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None \
                                         # },     # XBias does not consider DRC calc value
                                         
                                         # _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=1500,
                                         # _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=0, _MOS32MOS4spacebias=0, \
                                         # _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         # _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,\
                                         _Dummy=False)

                                         # )
    # ##################################################################################################################################################################

    # ##############065nm XOR #####################################################################
    # DelayUnitObj=_XOR(_DesignParameter=None, _Name='XOR')
    # DelayUnitObj._CalculateDesignParameter( _INVNumberOfGate=1, _INVChannelWidth=450, _INVChannelLength=60, _INVPNChannelRatio=2, _XORVdd2VssHeight=3300, _HeightCalOption='ON',\
                                      # _NumberOfGate1=3, _ChannelWidth1=450, _ChannelLength1=60, _PNChannelRatio1=2, \
                                      # _NumberOfGate2=2, _ChannelWidth2=450, _ChannelLength2=60, _PNChannelRatio2=2, \
                                      # _NumberOfGate3=4, _ChannelWidth3=450, _ChannelLength3=60, _PNChannelRatio3=2, \
                                      # _NumberOfGate4=2, _ChannelWidth4=450, _ChannelLength4=60, _PNChannelRatio4=2, \
                                         # _NumberOfNMOSConnectionViaCOY = 2, _NumberOfPMOSConnectionViaCOY =2,
                                         # _NumberOfNMOSOutputViaCOY = 4, _NumberOfPMOSOutputViaCOY =6,
                                         # _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                         # _BiasDictforViaPoly2Met1OnGate = {
                                         # '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None,  '_XbiasPMOS1GateVia':None,  '_YbiasPMOS1GateVia':None, 
                                         # '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None,  '_XbiasPMOS2GateVia':None,  '_YbiasPMOS2GateVia':None,
                                         # '_XbiasNMOS3GateVia':None, '_YbiasNMOS3GateVia':None,  '_XbiasPMOS3GateVia':None,  '_YbiasPMOS3GateVia':None,
                                         # '_XbiasNMOS4GateVia':None,  '_YbiasNMOS4GateVia':None,    '_XbiasPMOS4GateVia':None,   '_YbiasPMOS4GateVia':0,
                                         # '_XbiasInvNMOSGateVia':None,    '_YbiasInvNMOSGateVia':None,   '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                         # },     # XBias does not consider DRC calc value
                                         
                                         # _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=1500,
                                         # _MOS12MOS2spacebias=0, _MOS22InvMOSspacebias=0, _InvMOS2MOS3spacebias=0, _MOS32MOS4spacebias=0, \
                                         # _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                         # _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,\
                                         # _Dummy=False)

    # # ##################################################################################################################################################################
    ####################180nm XOR#########################################################################
    # DelayUnitObj=_XOR(_DesignParameter=None, _Name='XOR')
    # DelayUnitObj._CalculateDesignParameter( _INVNumberOfGate=2, _INVChannelWidth=1300, _INVChannelLength=180, _INVPNChannelRatio=2, _XORVdd2VssHeight=3300, _HeightCalOption='ON',\
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
    CLKtreeElementObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=CLKtreeElementObj._DesignParameter)
    _fileName='autoClkElement2.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=CLKtreeElementObj._CreateGDSStream(CLKtreeElementObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()


    print '###############open ftp connection & update gds file to cadence server###################'
    ftp_cadence_server = ftplib.FTP('141.223.86.109')
    ftp_cadence_server.login('sgjeong2',base64.b64decode('YWx2aDE1OTk1MQ==') )
    if DesignParameters._Technology == '065nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc65_ver3')
    elif DesignParameters._Technology == '180nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc180/workspace/workspace')
    elif DesignParameters._Technology == '130nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc130')
    elif DesignParameters._Technology == '090nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc90')
    elif DesignParameters._Technology == '045nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc45')
    print ftp_cadence_server.pwd()
    testStreamFile = open('./{}'.format(_fileName), 'rb')
    ftp_cadence_server.storbinary('STOR {}'.format(_fileName), testStreamFile)
    print 'close ftp connection'
    ftp_cadence_server.quit()
    testStreamFile.close()


    print '##########################################################################################'




# Consider output routing on PMOS DRC






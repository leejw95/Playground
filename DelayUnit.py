import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaPoly2Met1

import DelayUnitDesign
import XOR
import C2FlipFlop

import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _DELAYUNIT(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
    
                                     # _FlipFlopTopDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPtop),
                                     # _FlipFlopBotDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPbot),
                                     
                                     # _XorTopDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORtop),
                                     # _XorBotDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORbot),
                                     _FlipFlopTopDesignCalculationParameters=copy.deepcopy(C2FlipFlop._FLIPFLOP._ParametersForDesignCalculation),
                                     _FlipFlopBotDesignCalculationParameters=copy.deepcopy(C2FlipFlop._FLIPFLOP._ParametersForDesignCalculation),
                                     
                                     _XorTopDesignCalculatrionParameters=copy.deepcopy(XOR._XOR._ParametersForDesignCalculation),
                                     _XorBotDesignCalculatrionParameters=copy.deepcopy(XOR._XOR._ParametersForDesignCalculation),
                                     _FFbotOutputViaCOX=None, # Not For user
                                     

                                     _XBiasForViaMet22Met3OnCLKBotLeft = None, _YBiasForViaMet22Met3OnCLKBotLeft = None,
                                     _XBiasForViaMet12Met2OnCLKBotLeft = None, _YBiasForViaMet12Met2OnCLKBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBotRight = None, _YBiasForViaMet22Met3OnCLKBotRight = None,
                                     
                                     _XBiasForViaMet12Met2OnCLKBarBotLeft = None, _YBiasForViaMet12Met2OnCLKBarBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarBotLeft = None, _YBiasForViaMet22Met3OnCLKBarBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarBotRight = None, _YBiasForViaMet22Met3OnCLKBarBotRight = None,
                                     
                                     _XBiasForViaMet22Met3OnCLKTopLeft = None, _YBiasForViaMet22Met3OnCLKTopLeft = None,
                                     _XBiasForViaMet12Met2OnCLKTopLeft = None, _YBiasForViaMet12Met2OnCLKTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKTopRight = None, _YBiasForViaMet22Met3OnCLKTopRight = None,
                                     
                                     _XBiasForViaMet12Met2OnCLKBarTopLeft = None, _YBiasForViaMet12Met2OnCLKBarTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarTopLeft = None, _YBiasForViaMet22Met3OnCLKBarTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarTopRight = None, _YBiasForViaMet22Met3OnCLKBarTopRight = None,
                                     
                                     _NumberOfSelectionViaCOX = None,
                                     
                                     _YbiasForFFbotOutputVia = None, _FFbotOutputViaCOY =None, _FFbotOutputViaMinXorMinY = None,
                                     
                                     
                                     _XBiasForCLKverticalMet4 = None, _YBiasForViaMet32Met4OnCLKTopvertical = None,_YBiasForViaMet32Met4OnCLKBotvertical = None,
                                     _XBiasForCLKbarverticalMet4 = None, _YBiasForViaMet32Met4OnCLKBarTopvertical = None, _YBiasForViaMet32Met4OnCLKBarBotvertical = None, 
                                     
                                     _YBiasForViaMet12Met2OnXORbotInput = None, _YBiasForViaMet12Met2OnXORtopInput = None,

                                     _NumberOfXORBotInputViaCOY = None, _NumberOfXORTopInputViaCOY = None,


                                     _XBiasForViaMet12Met2OnSelectionXORtopLeft=None,_XBiasForViaMet12Met2OnSelectionXORtopRight=None,_XBiasForViaMet12Met2OnSelectionBarXORtopLeft=None,_XBiasForViaMet12Met2OnSelectionBarXORtopRight=None,
                                     _XBiasForViaMet12Met2OnSelectionXORbotLeft=None,_XBiasForViaMet12Met2OnSelectionXORbotRight=None,_XBiasForViaMet12Met2OnSelectionBarXORbotLeft=None,_XBiasForViaMet12Met2OnSelectionBarXORbotRight=None,

                                     _FFbotOutputMet4Width=None, _FFtopOutputMet2Width=None, _NumberOfCLKDivingViaOnLeftGateCOX= None, _NumberOfCLKDivingViaOnRightGateCOX= None,
                                     _CLKRoutingPathWidth=None,


                                     _ViaMet22Met3OnFFBotOutputParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnFFBotOutputParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnXORBotInputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnXORTopInputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnXORTopInputParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnXORTopInputParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                      #CLK, CLKB Via For Vertical metal
                                     _ViaMet32Met4OnCLKBotParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKTopParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKBarBotParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKBarTopParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                      #CLK Via For Horizontal metal
                                     _ViaMet12Met2OnCLKTopLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKTopRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKTopLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKTopRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnCLKBotLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBotRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBotLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBotRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet22Met3OnCLKBarTopLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBarTopRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarTopLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarTopRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),

                                     _ViaMet22Met3OnCLKBarBotLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBarBotRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarBotLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarBotRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),

                                     _ViaMet12Met2OnSelectionXORtopLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionXORtopRightParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORtopLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORtopRightParameters= copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     
                                     _ViaMet22Met3OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet32Met4OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                     
                                       
                                     
                                     _Dummy=False
                                     )

    def __init__(self, _DesignParameter=None, _Name='INV'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(

                                                    _FFtop = self._SrefElementDeclaration(_DesignObj=C2FlipFlop._FLIPFLOP(_DesignParameter=None, _Name='FFtopIn{}'.format(_Name)))[0],
                                                    _FFbot = self._SrefElementDeclaration(_DesignObj=C2FlipFlop._FLIPFLOP(_DesignParameter=None, _Name='FFbotIn{}'.format(_Name)))[0],

                                                    
                                                    _XORtop = self._SrefElementDeclaration(_DesignObj=XOR._XOR(_DesignParameter=None, _Name='XORtopIn{}'.format(_Name)))[0],
                                                    _XORbot = self._SrefElementDeclaration(_DesignObj=XOR._XOR(_DesignParameter=None, _Name='XORbotIn{}'.format(_Name)))[0],

                                                    _ViaMet22Met3OnFFBotOutput = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnFFBotOutputIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnFFBotOutput = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnFFBotOutputIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnXORBotInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnXORBotInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnXORTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnXORTopInputIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnXORTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnXORTopInputIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnXORTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnXORTopInputIn{}'.format(_Name)))[0],

                                                    #CLK, CLKB Via For Vertical metal
                                                    _ViaMet32Met4OnCLKTop = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnCLKTopIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnCLKBot = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnCLKBotIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnCLKBarTop = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnCLKBarTopIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnCLKBarBot = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnCLKBarBotIn{}'.format(_Name)))[0],
                                                    
                                                    #CLK Via For Horizontal metal
                                                    _ViaMet22Met3OnCLKTopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKTopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnCLKTopRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKTopRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKTopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKTopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKTopRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKTopRightIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnCLKBotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKBotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnCLKBotRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKRightBotIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBotRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBotRightIn{}'.format(_Name)))[0],

                                                    
                                                    
                                                    _ViaMet22Met3OnCLKBarTopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKBarTopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnCLKBarTopRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKBarTopRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBarTopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBarTopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBarTopRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBarTopRightIn{}'.format(_Name)))[0],

                                                    _ViaMet22Met3OnCLKBarBotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKBarBotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnCLKBarBotRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKBarBotRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBarBotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBarBotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnCLKBarBotRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnCLKBarBotRightIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnSelectionXORtopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionXORtopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionXORtopRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionXORtopRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionBarXORtopLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionBarXORtopLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionBarXORtopRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionBarXORtopRightIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet12Met2OnSelectionXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionXORbotRightIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionBarXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionBarXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnSelectionBarXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSelectionBarXORbotRightIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet22Met3OnSelectionXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSelectionXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnSelectionXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSelectionXORbotRightIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnSelectionBarXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSelectionBarXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet22Met3OnSelectionBarXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSelectionBarXORbotRightIn{}'.format(_Name)))[0],
                                                    
                                                    _ViaMet32Met4OnSelectionXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnSelectionXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnSelectionXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnSelectionXORbotRightIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnSelectionBarXORbotLeft = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnSelectionBarXORbotLeftIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnSelectionBarXORbotRight = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnSelectionBarXORbotRightIn{}'.format(_Name)))[0],
                                                    
                                                    
                                                    

                                                    _XORtopInputRoutingMet1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _XORtopInputRoutingMet1Horizon = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _XORbotInputRoutingMet1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _XORbotInputRoutingMet1Horizon = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _FFtopOutputRoutingMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _FFbotOutputRoutingMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _FFbotOutputRoutingMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    
                                                    _CLKRoutingMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    _CLKBarRoutingMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    
                                                    _CLKRoutingBotRightMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKRoutingBotLeftMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKRoutingBotLeftMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    
                                                    _CLKRoutingTopRightMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKRoutingTopLeftMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKRoutingTopLeftMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    
                                                    _CLKBarRoutingBotRightMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKBarRoutingBotLeftMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKBarRoutingTopRightMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    _CLKBarRoutingTopLeftMet3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1] ),
                                                    
                                                    
                                                    _SelectionRoutingXORbotLeftMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    _SelectionRoutingXORbotRightMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    _SelectionBarRoutingXORbotLeftMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    _SelectionBarRoutingXORbotRightMet4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1] ),
                                                    
                                                    _SelectionRoutingXORtopLeftMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _SelectionRoutingXORtopRightMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _SelectionBarRoutingXORtopLeftMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    _SelectionBarRoutingXORtopRightMet2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1] ),
                                                    
                                                    
                                                    _AdditionalMet1OnXORtopInputGateN = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnXORtopInputGateP = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnXORbotInputGateN = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnXORbotInputGateP = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _AdditionalMet1OnFFTopCLKRight =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnFFTopCLKBarRight =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnFFBotCLKRight =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _AdditionalMet1OnFFBotCLKBarRight =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                   
                                                   
                                                    _AdditionalMet1OnCLKBotLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnCLKBarBotLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnCLKTopLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnCLKBarTopLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    
                                                    _AdditionalMet1OnSelectionXORbotLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionXORbotRight = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionBarXORbotLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionBarXORbotRight = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _AdditionalMet1OnSelectionXORtopLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionXORtopRight = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionBarXORtopLeft = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet1OnSelectionBarXORtopRight = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 
                                     # _FlipFlopTopDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPtop),
                                     # _FlipFlopBotDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPbot),
                                     
                                     # _XorTopDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORtop),
                                     # _XorBotDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORbot),
                                     
                                     _FlipFlopTopDesignCalculationParameters=copy.deepcopy(C2FlipFlop._FLIPFLOP._ParametersForDesignCalculation),
                                     _FlipFlopBotDesignCalculationParameters=copy.deepcopy(C2FlipFlop._FLIPFLOP._ParametersForDesignCalculation),
                                     
                                     _XorTopDesignCalculatrionParameters=copy.deepcopy(XOR._XOR._ParametersForDesignCalculation),
                                     _XorBotDesignCalculatrionParameters=copy.deepcopy(XOR._XOR._ParametersForDesignCalculation),
                                     _FFbotOutputViaCOX=None, # Not For user
                                     # _INVNumberOfGate=None, _INVChannelWidth=None, _INVChannelLength=None, _INVPNChannelRatio=None,
                                     # _NumberOfGate1=None, _ChannelWidth1=None, _ChannelLength1=None, _PNChannelRatio1=None,
                                     # _NumberOfGate2=None, _ChannelWidth2=None, _ChannelLength2=None, _PNChannelRatio2=None,
                                     # _NumberOfGate3=None, _ChannelWidth3=None, _ChannelLength3=None, _PNChannelRatio3=None,
                                     # _NumberOfGate4=None, _ChannelWidth4=None, _ChannelLength4=None, _PNChannelRatio4=None,
                                     # _NumberOfSupplyCOX=None,_NumberOfSupplyCOY=None,
                                     # _XORSupplyMetal1XWidth=None, _XORSupplyMetal1YWidth=None,

                                     # _XORVdd2VssHeight=None,  _DistanceBtwSupplyCenter2MOSEdge=None, _XOREdgeBtwNWandPW=None,

                                     
                                     
                                     # _YBiasForViaMet12Met2OnPMOS2Output=None,_YBiasForViaMet12Met2OnPMOS3Output=None,_YBiasForViaMet12Met2OnNMOS2Output=None,_YBiasForViaMet12Met2OnNMOS3Output=None,
                                     # _XBiasOfViaPoly2Met1OnInvMOSGateN=None,_XBiasOfViaPoly2Met1OnInvMOSGateP=None, _YBiasOfOutputRouting1=None, _YBiasOfOutputRouting2=None, _NumberOfPMOSConnectionCOY=None,
                                     # _YbiasforViaMet12Met2OnNMOSGate1=None,_YbiasforViaMet12Met2OnNMOSGate4=None,_YbiasforViaMet12Met2OnPMOSGate1=None,_YbiasforViaMet12Met2OnPMOSGate4=None,
                                     # _YbiasforEdgeBtwNWandPW=None, _YbiasforHeight=None, _HeightCalOption=None,
                                     # _NumberOfNMOSConnectionViaCOY=None, _NumberOfPMOSConnectionViaCOY=None,_NumberOfNMOSOutputViaCOY=None, _NumberOfPMOSOutputViaCOY=None,
                                     # _NumberOfMOS1GateViaCOX=None,_NumberOfMOS2GateViaCOX=None,_NumberOfMOS3GateViaCOX=None,_NumberOfMOS4GateViaCOX=None,_NumberOfInvMOSGateViaCOX=None,
                                     # _BiasDictforViaPoly2Met1OnGate = {
                                     # '_XbiasNMOS1GateVia':None, '_YbiasNMOS1GateVia':None, '_XbiasNMOS2GateVia':None, '_YbiasNMOS2GateVia':None, '_XbiasNMOS3GateVia':None,
                                     # '_YbiasNMOS3GateVia':None, '_XbiasNMOS4GateVia':None, '_YbiasNMOS4GateVia':None, '_XbiasInvNMOSGateVia':None, '_YbiasInvNMOSGateVia':None,
                                     # '_XbiasPMOS1GateVia':None, '_YbiasPMOS1GateVia':None, '_XbiasPMOS2GateVia':None, '_YbiasPMOS2GateVia':None, '_XbiasPMOS3GateVia':None,
                                     # '_YbiasPMOS3GateVia':None, '_XbiasPMOS4GateVia':None, '_YbiasPMOS4GateVia':None, '_XbiasInvPMOSGateVia':None, '_YbiasInvPMOSGateVia':None,
                                     # },
                                     # _MOS12MOS2spacebias=None, _MOS22InvMOSspacebias=None, _InvMOS2MOS3spacebias=None, _MOS32MOS4spacebias=None, _XYadjust=None,
                                     _XBiasForViaMet22Met3OnCLKBotLeft = None, _YBiasForViaMet22Met3OnCLKBotLeft = None,
                                     _XBiasForViaMet12Met2OnCLKBotLeft = None, _YBiasForViaMet12Met2OnCLKBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBotRight = None, _YBiasForViaMet22Met3OnCLKBotRight = None,
                                     
                                     _XBiasForViaMet12Met2OnCLKBarBotLeft = None, _YBiasForViaMet12Met2OnCLKBarBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarBotLeft = None, _YBiasForViaMet22Met3OnCLKBarBotLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarBotRight = None, _YBiasForViaMet22Met3OnCLKBarBotRight = None,
                                     
                                     _XBiasForViaMet22Met3OnCLKTopLeft = None, _YBiasForViaMet22Met3OnCLKTopLeft = None,
                                     _XBiasForViaMet12Met2OnCLKTopLeft = None, _YBiasForViaMet12Met2OnCLKTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKTopRight = None, _YBiasForViaMet22Met3OnCLKTopRight = None,
                                     
                                     _XBiasForViaMet12Met2OnCLKBarTopLeft = None, _YBiasForViaMet12Met2OnCLKBarTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarTopLeft = None, _YBiasForViaMet22Met3OnCLKBarTopLeft = None,
                                     _XBiasForViaMet22Met3OnCLKBarTopRight = None, _YBiasForViaMet22Met3OnCLKBarTopRight = None,
                                     
                                     _YbiasForFFbotOutputVia = None, _FFbotOutputViaCOY =None, _FFbotOutputViaMinXorMinY = None,

                                     _NumberOfXORBotInputViaCOY=None, _NumberOfXORTopInputViaCOY=None,


                                  _XBiasForCLKverticalMet4 = None, _YBiasForViaMet32Met4OnCLKTopvertical = None,_YBiasForViaMet32Met4OnCLKBotvertical = None,
                                     _XBiasForCLKbarverticalMet4 = None, _YBiasForViaMet32Met4OnCLKBarTopvertical = None, _YBiasForViaMet32Met4OnCLKBarBotvertical = None, 
                                     
                                     _YBiasForViaMet12Met2OnXORbotInput = None, _YBiasForViaMet12Met2OnXORtopInput = None, 

                                     _NumberOfSelectionViaCOX = None,

                                     _XBiasForViaMet12Met2OnSelectionXORtopLeft=None,_XBiasForViaMet12Met2OnSelectionXORtopRight=None,_XBiasForViaMet12Met2OnSelectionBarXORtopLeft=None,_XBiasForViaMet12Met2OnSelectionBarXORtopRight=None,
                                     _XBiasForViaMet12Met2OnSelectionXORbotLeft=None,_XBiasForViaMet12Met2OnSelectionXORbotRight=None,_XBiasForViaMet12Met2OnSelectionBarXORbotLeft=None,_XBiasForViaMet12Met2OnSelectionBarXORbotRight=None,

                                     _FFbotOutputMet4Width=None, _FFtopOutputMet2Width=None, _NumberOfCLKDivingViaOnLeftGateCOX= None, _NumberOfCLKDivingViaOnRightGateCOX= None,
                                     _CLKRoutingPathWidth=None,
                                     
                                     
                                     _ViaMet22Met3OnFFBotOutputParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnFFBotOutputParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnXORBotInputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnXORTopInputParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnXORTopInputParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnXORTopInputParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                      #CLK, CLKB Via For Vertical metal
                                     _ViaMet32Met4OnCLKBotParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKTopParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKBarBotParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnCLKBarTopParameters=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                      #CLK Via For Horizontal metal
                                     _ViaMet12Met2OnCLKTopLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKTopRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKTopLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKTopRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnCLKBotLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBotRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBotLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBotRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet22Met3OnCLKBarTopLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBarTopRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarTopLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarTopRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     
                                     _ViaMet22Met3OnCLKBarBotLeftParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnCLKBarBotRightParameters=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarBotLeftParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnCLKBarBotRightParameters=copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),


                                     _ViaMet12Met2OnSelectionXORtopLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionXORtopRightParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORtopLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORtopRightParameters= copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     
                                     _ViaMet12Met2OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     _ViaMet12Met2OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation),
                                     
                                     _ViaMet22Met3OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     _ViaMet22Met3OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation),
                                     
                                     _ViaMet32Met4OnSelectionXORbotLeftParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionXORbotRightParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionBarXORbotLeftParameters = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     _ViaMet32Met4OnSelectionBarXORbotRightParameters= copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation),
                                     
                                     
                                     _Dummy=False
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  DelayUnit Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj=DRC.DRC()
        
        while True:
            # #####################SUBSET ELEMENTS GENERATION#########################
            # FF GENERATION
            self._DesignParameter['_FFtop']['_DesignObj']._CalculateDesignParameter(**_FlipFlopTopDesignCalculationParameters)
            self._DesignParameter['_FFtop']['_Reflect']=(1,0,0)
            self._DesignParameter['_FFtop']['_Angle']=0
            self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
            
            self._DesignParameter['_FFbot']['_DesignObj']._CalculateDesignParameter(**_FlipFlopBotDesignCalculationParameters)
            
            # XOR GENERATION
            self._DesignParameter['_XORtop']['_DesignObj']._CalculateDesignParameter(**_XorTopDesignCalculatrionParameters)
            self._DesignParameter['_XORtop']['_Reflect'] = (1, 0, 0)
            self._DesignParameter['_XORtop']['_Angle'] = 0

            self._DesignParameter['_XORbot']['_DesignObj']._CalculateDesignParameter(**_XorBotDesignCalculatrionParameters)
            
            # VIA GENERATION for FLIPFLOP OUTPUT
            MetLength = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][0]
            if _FFbotOutputViaCOX is None:
                # _FFbotOutputViaCOX = len(self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])
                _FFbotOutputViaCOX = int(MetLength - 2*_DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide + _DRCObj._VIAxMinSpace)/(_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
                if _FFbotOutputViaCOX < 2:
                    _FFbotOutputViaCOX = 2

            if _FFbotOutputViaCOY is None:
                _FFbotOutputViaCOY =2

            if _FFbotOutputViaMinXorMinY is None:
                _FFbotOutputViaMinXorMinY = 'MinX'


            _ViaMet22Met3OnFFBotOutputParameters['_ViaMet22Met3NumberOfCOX'] = _FFbotOutputViaCOX
            _ViaMet22Met3OnFFBotOutputParameters['_ViaMet22Met3NumberOfCOY'] = _FFbotOutputViaCOY

            _ViaMet32Met4OnFFBotOutputParameters['_ViaMet32Met4NumberOfCOX'] = _ViaMet22Met3OnFFBotOutputParameters['_ViaMet22Met3NumberOfCOX']
            _ViaMet32Met4OnFFBotOutputParameters['_ViaMet32Met4NumberOfCOY'] = _FFbotOutputViaCOY

            if _FFbotOutputViaMinXorMinY == 'MinX':
                self._DesignParameter['_ViaMet22Met3OnFFBotOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnFFBotOutputParameters)
                self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnFFBotOutputParameters)
            else:
                self._DesignParameter['_ViaMet22Met3OnFFBotOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnFFBotOutputParameters)
                self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4OnFFBotOutputParameters)
            
            # VIA GENERATION for XOR INPUT
            if _NumberOfXORTopInputViaCOY is None:
                _NumberOfXORTopInputViaCOY = 2
            if _NumberOfXORBotInputViaCOY is None:
                _NumberOfXORBotInputViaCOY = 2

            _ViaMet12Met2OnXORBotInputParameters['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaMet12Met2OnXORBotInputParameters['_ViaMet12Met2NumberOfCOY'] = _NumberOfXORBotInputViaCOY
            self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnXORBotInputParameters)


            _ViaMet12Met2OnXORTopInputParameters['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaMet12Met2OnXORTopInputParameters['_ViaMet12Met2NumberOfCOY'] = _NumberOfXORTopInputViaCOY
            self._DesignParameter['_ViaMet12Met2OnXORTopInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaMet12Met2OnXORTopInputParameters)

            _ViaMet22Met3OnXORTopInputParameters['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaMet22Met3OnXORTopInputParameters['_ViaMet22Met3NumberOfCOY'] = _NumberOfXORBotInputViaCOY
            self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaMet22Met3OnXORTopInputParameters)


            _ViaMet32Met4OnXORTopInputParameters['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet32Met4OnXORTopInputParameters['_ViaMet32Met4NumberOfCOY'] = _NumberOfXORTopInputViaCOY
            self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnXORTopInputParameters)


            # VIA GENERATION for CLK, CLKB (vertical)
            
            _ViaMet32Met4OnCLKBarTopParameters['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet32Met4OnCLKBarTopParameters['_ViaMet32Met4NumberOfCOY'] = 2
            self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnCLKBarTopParameters)
            
            _ViaMet32Met4OnCLKBarBotParameters['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet32Met4OnCLKBarBotParameters['_ViaMet32Met4NumberOfCOY'] = 2
            self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnCLKBarBotParameters)
            
            _ViaMet32Met4OnCLKTopParameters['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet32Met4OnCLKTopParameters['_ViaMet32Met4NumberOfCOY'] = 2
            self._DesignParameter['_ViaMet32Met4OnCLKTop']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnCLKTopParameters)
            
            _ViaMet32Met4OnCLKBotParameters['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet32Met4OnCLKBotParameters['_ViaMet32Met4NumberOfCOY'] = 2
            self._DesignParameter['_ViaMet32Met4OnCLKBot']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4OnCLKBotParameters)
            
            # VIA GENERATION for CLK (horizontal)

            if _NumberOfCLKDivingViaOnLeftGateCOX is None:
                _NumberOfCLKDivingViaOnLeftGateCOX = 2
            if _NumberOfCLKDivingViaOnRightGateCOX is None:
                _NumberOfCLKDivingViaOnRightGateCOX = 2
                        
            _ViaMet22Met3OnCLKTopLeftParameters['_ViaMet22Met3NumberOfCOX'] = 2
            _ViaMet22Met3OnCLKTopLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKTopLeftParameters)
            
            _ViaMet22Met3OnCLKTopRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet22Met3OnCLKTopRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKTopRightParameters)

            _ViaMet12Met2OnCLKTopLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet12Met2OnCLKTopLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKTopLeftParameters)
            
            _ViaMet12Met2OnCLKTopRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet12Met2OnCLKTopRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKTopRightParameters)
            
            
            _ViaMet12Met2OnCLKBotLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet12Met2OnCLKBotLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBotLeftParameters)
            
            _ViaMet12Met2OnCLKBotRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet12Met2OnCLKBotRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBotRightParameters)
            
            _ViaMet22Met3OnCLKBotLeftParameters['_ViaMet22Met3NumberOfCOX'] = 2
            _ViaMet22Met3OnCLKBotLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBotLeftParameters)
            
            _ViaMet22Met3OnCLKBotRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet22Met3OnCLKBotRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBotRightParameters)
            
            
            _ViaMet22Met3OnCLKBarTopLeftParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet22Met3OnCLKBarTopLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBarTopLeftParameters)
            
            _ViaMet22Met3OnCLKBarTopRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet22Met3OnCLKBarTopRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBarTopRightParameters)
            
            _ViaMet12Met2OnCLKBarTopLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet12Met2OnCLKBarTopLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBarTopLeftParameters)
            
            _ViaMet12Met2OnCLKBarTopRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet12Met2OnCLKBarTopRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBarTopRightParameters)
            
                        
            _ViaMet22Met3OnCLKBarBotLeftParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet22Met3OnCLKBarBotLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBarBotLeftParameters)
            
            _ViaMet22Met3OnCLKBarBotRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet22Met3OnCLKBarBotRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnCLKBarBotRightParameters)
            
            _ViaMet12Met2OnCLKBarBotLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnLeftGateCOX
            _ViaMet12Met2OnCLKBarBotLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBarBotLeftParameters)
            
            _ViaMet12Met2OnCLKBarBotRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfCLKDivingViaOnRightGateCOX
            _ViaMet12Met2OnCLKBarBotRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnCLKBarBotRightParameters)
            
            
            if _NumberOfSelectionViaCOX is None:
                _NumberOfSelectionViaCOX = 2
            _ViaMet12Met2OnSelectionXORtopLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionXORtopLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionXORtopLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionXORtopLeftParameters)
            
            _ViaMet12Met2OnSelectionXORtopRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionXORtopRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionXORtopRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionXORtopRightParameters)
            
            _ViaMet12Met2OnSelectionBarXORtopLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionBarXORtopLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionBarXORtopLeftParameters)
            
            _ViaMet12Met2OnSelectionBarXORtopRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionBarXORtopRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionBarXORtopRightParameters)
            
            _ViaMet12Met2OnSelectionXORbotLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionXORbotLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionXORbotLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionXORbotLeftParameters)
            
            _ViaMet12Met2OnSelectionXORbotRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionXORbotRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionXORbotRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionXORbotRightParameters)
            
            _ViaMet12Met2OnSelectionBarXORbotLeftParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionBarXORbotLeftParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotLeft']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionBarXORbotLeftParameters)
            
            _ViaMet12Met2OnSelectionBarXORbotRightParameters['_ViaMet12Met2NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet12Met2OnSelectionBarXORbotRightParameters['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotRight']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2OnSelectionBarXORbotRightParameters)
  
  
            _ViaMet22Met3OnSelectionXORbotLeftParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet22Met3OnSelectionXORbotLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnSelectionXORbotLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnSelectionXORbotLeftParameters)
            
            _ViaMet22Met3OnSelectionXORbotRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet22Met3OnSelectionXORbotRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnSelectionXORbotRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnSelectionXORbotRightParameters)
            
            _ViaMet22Met3OnSelectionBarXORbotLeftParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet22Met3OnSelectionBarXORbotLeftParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotLeft']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnSelectionBarXORbotLeftParameters)
            
            _ViaMet22Met3OnSelectionBarXORbotRightParameters['_ViaMet22Met3NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet22Met3OnSelectionBarXORbotRightParameters['_ViaMet22Met3NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotRight']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3OnSelectionBarXORbotRightParameters)
  
            
            _ViaMet32Met4OnSelectionXORbotLeftParameters['_ViaMet32Met4NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet32Met4OnSelectionXORbotLeftParameters['_ViaMet32Met4NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet32Met4OnSelectionXORbotLeft']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4OnSelectionXORbotLeftParameters)
            
            _ViaMet32Met4OnSelectionXORbotRightParameters['_ViaMet32Met4NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet32Met4OnSelectionXORbotRightParameters['_ViaMet32Met4NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet32Met4OnSelectionXORbotRight']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4OnSelectionXORbotRightParameters)
            
            _ViaMet32Met4OnSelectionBarXORbotLeftParameters['_ViaMet32Met4NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet32Met4OnSelectionBarXORbotLeftParameters['_ViaMet32Met4NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet32Met4OnSelectionBarXORbotLeft']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4OnSelectionBarXORbotLeftParameters)
            
            _ViaMet32Met4OnSelectionBarXORbotRightParameters['_ViaMet32Met4NumberOfCOX'] = _NumberOfSelectionViaCOX
            _ViaMet32Met4OnSelectionBarXORbotRightParameters['_ViaMet32Met4NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet32Met4OnSelectionBarXORbotRight']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4OnSelectionBarXORbotRightParameters)
  
            
            
            
            # # )#####################COORDINATION SETTING#########################
            self._DesignParameter['_FFbot']['_XYCoordinates']=[ [0,0] ]
            self._DesignParameter['_FFtop']['_XYCoordinates']=[ [0,self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]+self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]  ] ]

            _FFoutputXlocation = self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] +  self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0]
            _XORinputXlocation = self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0]
            _XORcenterXlocation = _FFoutputXlocation - _XORinputXlocation #- self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_InvNMOS']['_XYCoordinates'][0][0]
            self._DesignParameter['_XORbot']['_XYCoordinates']= [ [_XORcenterXlocation, self._DesignParameter['_FFtop']['_XYCoordinates'][0][1]]   ]
            self._DesignParameter['_XORtop']['_XYCoordinates']= [ [_XORcenterXlocation, self._DesignParameter['_XORbot']['_XYCoordinates'][0][1]+ self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]]  ]


            
            

            # # )################################ FF top Output CONNECTION ################################

            self._DesignParameter['_FFtopOutputRoutingMet2']['_Width'] = _DRCObj._MetalxMinWidth
            tmp = []
            for i in range(1, min( len(self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates']) , len(self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ) + 1 ):
                if i%2 is 1:
                    # print 'hmm', self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]
                    tmp.append( [ [self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][-i][0], self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][-i][1])        ]
                                ,[self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][-i][0],self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ]    ])

            self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates']=tmp
            
                # # )#############FF top Put Via #################
            
            
            
            
            # # )################################ FF bot Output CONNECTION ################################

                 # # )#############FF bot Met2 Connection #################
            self._DesignParameter['_FFbotOutputRoutingMet2']['_Width'] = _DRCObj._MetalxMinWidth
            tmp = []
            for i in range(1,len(self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'])+1 ):
                if i%2 is 1:
                    tmp.append([ [a+b for a, b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i])]
                               , [a+b for a, b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputRight']['_XYCoordinates'][-i])]    ]  )
            self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'] = tmp
                
                # # )#############FF bot Put Via #################
            tmpA=[]
            tmpB=[]
            tmpA = [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0],self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0] )]
            tmpB = [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0],self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][-1] )]
            tmpViaLoc = [[round((a+b)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing for a,b in zip(tmpA,tmpB)]]
            if _YbiasForFFbotOutputVia is None:
                _YbiasForFFbotOutputVia = 0
            tmpViaLoc[0][1] += _YbiasForFFbotOutputVia
            self._DesignParameter['_ViaMet22Met3OnFFBotOutput']['_XYCoordinates'] = tmpViaLoc
            self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_XYCoordinates'] = tmpViaLoc

            # self._DesignParameter['_FFbot']['_XYCoordinates'][0] , self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][0][0] , self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][-1][0])

            if _FFbotOutputMet4Width is None:
                _FFbotOutputMet4Width = _DRCObj._MetalxMinWidth
            self._DesignParameter['_FFbotOutputRoutingMet4']['_Width'] = _DRCObj._MetalxMinWidth
            tmp = []
            #For a now,  ==> Via12, XOR's INVGateY-Via12X
            #Later, modify ==> Via34 Coordi , Via34Y-Via12X, XOR's INVGateY-Via12X
            for i in range(1, min( len(self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates']) , len(self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_InvNMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']) ) + 1 ):
                if i%2 is 1:
                    # print 'hmm', self._DesignParameter['_FFbot']['_XYCoordinates'][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i]
                    # tmp.append( [ [a+b for a ,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0],self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i])]
                                 # ,[self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i][0],self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ]    ])
                    tmp.append( [  self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_XYCoordinates'][0]
                                 ,[self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i][0],self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_XYCoordinates'][0][1] ]
                                 ,[self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputRight']['_XYCoordinates'][-i][0],self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] ]    ])

            self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates']=tmp
            
            # # )################################ XORtop Input  ################################
            
            self._DesignParameter['_XORtopInputRoutingMet1']['_Width'] = self._DesignParameter['_ViaMet12Met2OnXORTopInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] #_DRCObj._Metal1MinWidth
            tmp=[]
            tmpYlocationUPside = self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1])  + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            tmpYlocationDOWNside = self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]) -  self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            for i in range(0 , len(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'])):
                tmp.append([ [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][i][1][0], tmpYlocationUPside  ]
                            ,[self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][i][1][0], tmpYlocationDOWNside  ]  ])      #Additional Metal consider!!!
            self._DesignParameter['_XORtopInputRoutingMet1']['_XYCoordinates'] = tmp
            
            # self._DesignParameter['_XORtopInputRoutingMet1Horizon']['_Width'] = _DRCObj._Metal1MinWidth
            self._DesignParameter['_XORtopInputRoutingMet1Horizon']['_Width'] = self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_XORtopInputRoutingMet1Horizon']['_XYCoordinates'] = [[ [self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1]) ]
                                                                                        ,  [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1]) ]  ]]
            self._DesignParameter['_XORtopInputRoutingMet1Horizon']['_XYCoordinates'].append([ [self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1]) ]
                                                                                        ,      [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1]) ]  ])

            if _YBiasForViaMet12Met2OnXORtopInput is None:
                _YBiasForViaMet12Met2OnXORtopInput = 0
            tmp = []
            for i in range(0 , len(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'])):
                tmp.append([ round((a+b)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing for a,b in zip(self._DesignParameter['_XORtopInputRoutingMet1']['_XYCoordinates'][i][0], self._DesignParameter['_XORtopInputRoutingMet1']['_XYCoordinates'][i][1] )])
                tmp[i][1] += _YBiasForViaMet12Met2OnXORtopInput
            self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_XYCoordinates'] = tmp
            self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_XYCoordinates'] = tmp
            self._DesignParameter['_ViaMet12Met2OnXORTopInput']['_XYCoordinates'] = tmp
            self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][-1][1] = tmp[0][1]
                
            self._DesignParameter['_AdditionalMet1OnXORtopInputGateN']['_Width'] = self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            MostLeft = min(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][-1][1][0] - self._DesignParameter['_FFbotOutputRoutingMet4']['_Width']/2, self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            MostRight = max(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0] + self._DesignParameter['_FFbotOutputRoutingMet4']['_Width']/2, self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            Y_location = self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1])
            self._DesignParameter['_AdditionalMet1OnXORtopInputGateN']['_XYCoordinates'] = [[ [MostLeft, Y_location ] 
                                                                                            , [MostRight, Y_location] ]] 
            
            # self._DesignParameter['_AdditionalMet1OnXORtopInputGateN']['_XYCoordinates'] = [[ [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1])  ]
                                                                                             # ,[self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1])] ]]
            # self._DesignParameter['_AdditionalMet1OnXORtopInputGateN']['_XYCoordinates'].append([ [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][-1][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (- self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1])  ] 
                                                                                             # ,[self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1])] ])
            
            self._DesignParameter['_AdditionalMet1OnXORtopInputGateP']['_Width'] = self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            MostLeft = min(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][-1][1][0] - self._DesignParameter['_FFbotOutputRoutingMet4']['_Width']/2, self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            MostRight = max(self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0] + self._DesignParameter['_FFbotOutputRoutingMet4']['_Width']/2, self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            Y_location = self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1])
            self._DesignParameter['_AdditionalMet1OnXORtopInputGateP']['_XYCoordinates'] = [[ [MostLeft, Y_location ] 
                                                                                            , [MostRight, Y_location] ]] 
            # self._DesignParameter['_AdditionalMet1OnXORtopInputGateP']['_XYCoordinates'] = [[ [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1])  ]
                                                                                             # ,[self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1])] ]]
            # self._DesignParameter['_AdditionalMet1OnXORtopInputGateP']['_XYCoordinates'].append([ [self._DesignParameter['_FFbotOutputRoutingMet4']['_XYCoordinates'][-1][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (- self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1]) ]
                                                                                                 # ,[self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0], self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1])] ])
            
            
            # # )################################ XORbot Input  ################################
            
            self._DesignParameter['_XORbotInputRoutingMet1']['_Width'] = self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] #_DRCObj._Metal1MinWidth
            tmp=[]
            tmpYlocationUPside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]  + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            tmpYlocationDOWNside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1] -  self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
            for i in range(0 , len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'])):
                tmp.append([ [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][i][0][0], tmpYlocationUPside  ]
                            ,[self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][i][0][0], tmpYlocationDOWNside  ]  ])
            self._DesignParameter['_XORbotInputRoutingMet1']['_XYCoordinates'] = tmp
            
            # self._DesignParameter['_XORbotInputRoutingMet1Horizon']['_Width'] = _DRCObj._Metal1MinWidth
            self._DesignParameter['_XORbotInputRoutingMet1Horizon']['_Width'] = self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_XORbotInputRoutingMet1Horizon']['_XYCoordinates'] = [[ [self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1] ]
                                                                                        ,  [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][0][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][1] ]  ]]
            self._DesignParameter['_XORbotInputRoutingMet1Horizon']['_XYCoordinates'].append([ [self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][0][0] , self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1] ]
                                                                                        ,      [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][0][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS3Gate']['_XYCoordinates'][1][1] ]  ])

            
            if _YBiasForViaMet12Met2OnXORbotInput is None:
                _YBiasForViaMet12Met2OnXORbotInput = 0
            tmp = []
            for i in range(0 , len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'])):
                tmp.append([ round((a+b)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing for a,b in zip(self._DesignParameter['_XORbotInputRoutingMet1']['_XYCoordinates'][i][0], self._DesignParameter['_XORbotInputRoutingMet1']['_XYCoordinates'][i][1] )])
                tmp[i][1] += _YBiasForViaMet12Met2OnXORbotInput
                self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][i][1][1] = tmp[i][1]
            self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_XYCoordinates'] = tmp
            #Routing Metal Adjusting
            
                
            self._DesignParameter['_AdditionalMet1OnXORbotInputGateN']['_Width'] = self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            MostLeft = min(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-1][1][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2, self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            MostRight = max(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][1][0] + self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2, self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            Y_location = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1]
            self._DesignParameter['_AdditionalMet1OnXORbotInputGateN']['_XYCoordinates'] = [[ [MostLeft, Y_location ] 
                                                                                            , [MostRight, Y_location] ]] 
            # self._DesignParameter['_AdditionalMet1OnXORbotInputGateN']['_XYCoordinates'] = [[ [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1]  ]
                                                                                             # ,[self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]] ]]
            # self._DesignParameter['_AdditionalMet1OnXORbotInputGateN']['_XYCoordinates'].append([ [self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][0][1]]
                                                                                                 # ,[self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-1][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] +  self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvNMOS']['_XYCoordinates'][0][1]  ]  ])
            self._DesignParameter['_AdditionalMet1OnXORbotInputGateP']['_Width'] = self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            MostLeft = min(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-1][1][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2, self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            MostRight = max(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][1][0] + self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2, self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
            Y_location = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1]
            self._DesignParameter['_AdditionalMet1OnXORbotInputGateP']['_XYCoordinates'] = [[ [MostLeft, Y_location ] 
                                                                                            , [MostRight, Y_location] ]] 
            # self._DesignParameter['_AdditionalMet1OnXORbotInputGateP']['_XYCoordinates'] = [[ [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1]  ]
                                                                                             # ,[self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]] ]]
            # self._DesignParameter['_AdditionalMet1OnXORbotInputGateP']['_XYCoordinates'].append([ [self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-1][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] +  self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_GateRoutingOnInvPMOS']['_XYCoordinates'][0][1]  ]
                                                                                                 # ,[self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][0], self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnInvMOSGate']['_XYCoordinates'][1][1]] ])

                
                
            # # )################################ CLK ROUTING ################################    (Vertical)
            if _XBiasForCLKverticalMet4 is None:
                _XBiasForCLKverticalMet4 = 0
            if _XBiasForCLKbarverticalMet4 is None:
                _XBiasForCLKbarverticalMet4 = 0
            
            _Xlocation =( self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2 \
                         +self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2 )/2
            DRCspace = max(_DRCObj._MetalxMinSpace, _DRCObj._VIAxMinSpace)/2
            
            _Xlocation1 = round((_Xlocation - DRCspace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            _Xlocation2 = round((_Xlocation + DRCspace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            if _CLKRoutingPathWidth is None:
                _CLKRoutingPathWidth = _DRCObj._MetalxMinWidth
            self._DesignParameter['_CLKRoutingMet4']['_Width'] = _CLKRoutingPathWidth
            _Xlocation1 -= round(self._DesignParameter['_CLKRoutingMet4']['_Width']/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'] = [[ [_Xlocation1 + _XBiasForCLKverticalMet4,0]
                                                                          ,[_Xlocation1 + _XBiasForCLKverticalMet4,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1]+(-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1])] ]]
            self._DesignParameter['_CLKBarRoutingMet4']['_Width'] = _CLKRoutingPathWidth
            _Xlocation2 += int(self._DesignParameter['_CLKBarRoutingMet4']['_Width']/2/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'] = [[ [_Xlocation2 + _XBiasForCLKbarverticalMet4,0]
                                                                          ,[_Xlocation2 + _XBiasForCLKbarverticalMet4,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1]+(-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1])] ]]

                                                                          
            print ('aa?' , self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'])
            # # )################################ CLK VIA ################################
            if _XBiasForViaMet22Met3OnCLKBotLeft is None:
                _XBiasForViaMet22Met3OnCLKBotLeft = 0
            if _YBiasForViaMet22Met3OnCLKBotLeft is None:
                _YBiasForViaMet22Met3OnCLKBotLeft = 0
            if _XBiasForViaMet12Met2OnCLKBotLeft is None:
                _XBiasForViaMet12Met2OnCLKBotLeft = 0
            if _YBiasForViaMet12Met2OnCLKBotLeft is None:
                _YBiasForViaMet12Met2OnCLKBotLeft = 0
            if _XBiasForViaMet22Met3OnCLKBotRight is None:
                _XBiasForViaMet22Met3OnCLKBotRight = 0
            if _YBiasForViaMet22Met3OnCLKBotRight is None:
                _YBiasForViaMet22Met3OnCLKBotRight = 0
            
            if _XBiasForViaMet12Met2OnCLKBarBotLeft is None:
                _XBiasForViaMet12Met2OnCLKBarBotLeft = 0
            if _YBiasForViaMet12Met2OnCLKBarBotLeft is None:
                _YBiasForViaMet12Met2OnCLKBarBotLeft = 0
            if _XBiasForViaMet22Met3OnCLKBarBotLeft is None:
                _XBiasForViaMet22Met3OnCLKBarBotLeft = 0
            if _YBiasForViaMet22Met3OnCLKBarBotLeft is None:
                _YBiasForViaMet22Met3OnCLKBarBotLeft = 0
            if _XBiasForViaMet22Met3OnCLKBarBotRight is None:
                _XBiasForViaMet22Met3OnCLKBarBotRight = 0
            if _YBiasForViaMet22Met3OnCLKBarBotRight is None:
                _YBiasForViaMet22Met3OnCLKBarBotRight = 0
          
            
            if _XBiasForViaMet22Met3OnCLKTopLeft is None:
                _XBiasForViaMet22Met3OnCLKTopLeft = 0
            if _YBiasForViaMet22Met3OnCLKTopLeft is None:
                _YBiasForViaMet22Met3OnCLKTopLeft = 0
            if _XBiasForViaMet12Met2OnCLKTopLeft is None:
                _XBiasForViaMet12Met2OnCLKTopLeft = 0
            if _YBiasForViaMet12Met2OnCLKTopLeft is None:
                _YBiasForViaMet12Met2OnCLKTopLeft = 0
            if _XBiasForViaMet22Met3OnCLKTopRight is None:
                _XBiasForViaMet22Met3OnCLKTopRight = 0
            if _YBiasForViaMet22Met3OnCLKTopRight is None:
                _YBiasForViaMet22Met3OnCLKTopRight = 0

            if _XBiasForViaMet12Met2OnCLKBarTopLeft is None:
                _XBiasForViaMet12Met2OnCLKBarTopLeft = 0
            if _YBiasForViaMet12Met2OnCLKBarTopLeft is None:
                _YBiasForViaMet12Met2OnCLKBarTopLeft = 0
            if _XBiasForViaMet22Met3OnCLKBarTopLeft is None:
                _XBiasForViaMet22Met3OnCLKBarTopLeft = 0
            if _YBiasForViaMet22Met3OnCLKBarTopLeft is None:
                _YBiasForViaMet22Met3OnCLKBarTopLeft = 0
            if _XBiasForViaMet22Met3OnCLKBarTopRight is None:
                _XBiasForViaMet22Met3OnCLKBarTopRight = 0
            if _YBiasForViaMet22Met3OnCLKBarTopRight is None:
                _YBiasForViaMet22Met3OnCLKBarTopRight = 0
                

            
            if _YBiasForViaMet32Met4OnCLKTopvertical is None:
                _YBiasForViaMet32Met4OnCLKTopvertical = 0
            if _YBiasForViaMet32Met4OnCLKBotvertical is None:
                _YBiasForViaMet32Met4OnCLKBotvertical = 0
            
            if _YBiasForViaMet32Met4OnCLKBarTopvertical is None:
                _YBiasForViaMet32Met4OnCLKBarTopvertical = 0
            if _YBiasForViaMet32Met4OnCLKBarBotvertical is None:
                _YBiasForViaMet32Met4OnCLKBarBotvertical = 0
            self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'] = [[self._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0][0] 
                                                                                 ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1] + _YBiasForViaMet32Met4OnCLKBotvertical ]]
            self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_XYCoordinates'] = [[self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0][0] 
                                                                                 ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1] + _YBiasForViaMet32Met4OnCLKBarBotvertical ]]

            self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'] = [[self._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0][0] 
                                                                                 ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1] ) + _YBiasForViaMet32Met4OnCLKTopvertical ]]
            self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_XYCoordinates'] = [[self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0][0] 
                                                                                 ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1] ) + _YBiasForViaMet32Met4OnCLKBarTopvertical ]]

            self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'] = [[ self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - _DRCObj._MetalxMinSpace - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + _XBiasForViaMet22Met3OnCLKBotLeft
                                                                                     ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1] + _YBiasForViaMet22Met3OnCLKBotLeft ]]


            self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'] = [[a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0])] ]
            self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][0] += _XBiasForViaMet12Met2OnCLKBotLeft
            self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][1] += _YBiasForViaMet12Met2OnCLKBotLeft
            
            
            self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'] = [[ a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0])   ]]
            self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0] += _XBiasForViaMet22Met3OnCLKBotRight
            self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][1] += _YBiasForViaMet22Met3OnCLKBotRight
            self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'] = [[ a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0])   ]]
            self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][0] += _XBiasForViaMet22Met3OnCLKBotRight
            self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][1] += _YBiasForViaMet22Met3OnCLKBotRight
            
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0]) ] ]
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][0] += _XBiasForViaMet12Met2OnCLKBarBotLeft
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][1] += _YBiasForViaMet12Met2OnCLKBarBotLeft
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0]) ] ]
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_XYCoordinates'][0][0] += _XBiasForViaMet22Met3OnCLKBarBotLeft
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_XYCoordinates'][0][1] += _YBiasForViaMet22Met3OnCLKBarBotLeft
            
            
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0]) ] ]
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0] += _XBiasForViaMet22Met3OnCLKBarBotRight
            self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][1] += _YBiasForViaMet22Met3OnCLKBarBotRight
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0]) ] ]
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][0] += _XBiasForViaMet22Met3OnCLKBarBotRight
            self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][1] += _YBiasForViaMet22Met3OnCLKBarBotRight
            
                #########CLK VIA for FFtop ##########
            self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][0] + _XBiasForViaMet12Met2OnCLKTopLeft 
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet12Met2OnCLKTopLeft   ]]
            
            self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 -_DRCObj._MetalxMinSpace - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + _XBiasForViaMet22Met3OnCLKTopLeft
                                                                                     ,self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'][0][1] + _YBiasForViaMet22Met3OnCLKTopLeft    ]]

            self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][0] +_XBiasForViaMet22Met3OnCLKTopRight
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet22Met3OnCLKTopRight    ]]
            
            self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][0] 
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet22Met3OnCLKTopRight    ]]
                                                                                     
            
            self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] + _XBiasForViaMet12Met2OnCLKBarTopLeft
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet12Met2OnCLKBarTopLeft   ]]
            
            self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_XYCoordinates'] =  [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] + _XBiasForViaMet22Met3OnCLKBarTopLeft
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet22Met3OnCLKBarTopLeft   ]]

            self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][0] + _XBiasForViaMet22Met3OnCLKBarTopRight
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet22Met3OnCLKBarTopRight    ]]
            
            self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'] = [[ self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][0] + _XBiasForViaMet22Met3OnCLKBarTopRight
                                                                                     ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1]) + _YBiasForViaMet22Met3OnCLKBarTopRight   ]]
            

           # self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'] = [[self._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0][0]
                                                                                 # ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1]  ]]
            # self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_XYCoordinates'] = [[self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0][0]
                                                                                 # ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1]  ]]

            # self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'] = [[self._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0][0]
                                                                                 # ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1] ) ]]
            # self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_XYCoordinates'] = [[self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0][0]
                                                                                 # ,self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1] ) ]]

            # self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'] = [[ self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - _DRCObj._MetalxMinSpace - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
                                                                                     # ,self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1] ]]
            
            # self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'] = [[a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0])] ]
            # self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'] = [[ a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0])   ]]
            # self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'] = [[ a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0])   ]]
            
            
            # self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0]) ] ]
            # self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0]) ] ]
            # self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0]) ] ]
            # self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'] = [ [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0]) ] ]
            
            
            
            
            
            
            
            
            # # )################################ CLK ROUTING ################################    (Horizontal)                                                            
            self._DesignParameter['_CLKRoutingBotRightMet3']['_Width'] = _DRCObj._MetalxMinWidth
            # self._DesignParameter['_CLKRoutingBotRightMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'][0] , [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0],self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0])] ]]
            self._DesignParameter['_CLKRoutingBotRightMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'][0]
                                                                                    ,[self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][1] ]
                                                                                    ,self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0] ]]
            
            self._DesignParameter['_CLKBarRoutingBotRightMet3']['_Width'] = _DRCObj._MetalxMinWidth
            # self._DesignParameter['_CLKBarRoutingBotRightMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_XYCoordinates'][0] , [a+b for a,b in zip(self._DesignParameter['_FFbot']['_XYCoordinates'][0],self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0])] ]]
            self._DesignParameter['_CLKBarRoutingBotRightMet3']['_XYCoordinates'] =  [[ [self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_XYCoordinates'][0][0] , self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][1] ]  
                                                                                       ,self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0] ]]

            self._DesignParameter['_CLKRoutingTopRightMet3']['_Width'] = _DRCObj._MetalxMinWidth
            # self._DesignParameter['_CLKRoutingTopRightMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'][0]
                                                                                   # ,[self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][0], self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][1] )] ]]
            self._DesignParameter['_CLKRoutingTopRightMet3']['_XYCoordinates'] =  [[ [self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'][0][1] ]
                                                                                    ,self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'][0] ]]
            
            self._DesignParameter['_CLKBarRoutingTopRightMet3']['_Width'] = _DRCObj._MetalxMinWidth
            # self._DesignParameter['_CLKBarRoutingTopRightMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_XYCoordinates'][0] 
                                                                                      # ,[self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][0], self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][1])] ]]
            self._DesignParameter['_CLKBarRoutingTopRightMet3']['_XYCoordinates'] =  [[ [self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_XYCoordinates'][0][0] , self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][1] ]
                                                                                       ,self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0] ]] 
            
            self._DesignParameter['_CLKRoutingBotLeftMet2']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_CLKRoutingBotLeftMet2']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0] 
                                                                                  ,[self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_CLKRoutingBotLeftMet2']['_Width']/2, self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][1]]
                                                                                  ,[self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_CLKRoutingBotLeftMet2']['_Width']/2, self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][1]]]]
            
            
            self._DesignParameter['_CLKRoutingBotLeftMet3']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_CLKRoutingBotLeftMet3']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0] \
                                                                                  ,[self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'][0][0],self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][1]] \
                                                                                  ,self._DesignParameter['_ViaMet32Met4OnCLKBot']['_XYCoordinates'][0] \
                                                                                  ]]
                                                                                  
            self._DesignParameter['_CLKBarRoutingBotLeftMet3']['_Width'] = _DRCObj._MetalxMinWidth
            tmpX = self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2 - _DRCObj._MetalxMinSpace - self._DesignParameter['_CLKBarRoutingBotLeftMet3']['_Width']/2
            self._DesignParameter['_CLKBarRoutingBotLeftMet3']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0]
                                                                                     ,[tmpX,self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][1]] 
                                                                                     ,[tmpX,self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][1]]
                                                                                     ,[self._DesignParameter['_ViaMet32Met4OnCLKBarBot']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][1] ]   ]]
            
            # #20190102 update for CLK Bot Metal3 connection
            # self._DesignParameter['_CLKRoutingBotF
            
            
            
                #########CLK Routing for FFtop ##########
            self._DesignParameter['_CLKRoutingTopLeftMet2']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_CLKRoutingTopLeftMet2']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0] 
                                                                                  ,[self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_CLKRoutingTopLeftMet2']['_Width']/2, self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0][1]]
                                                                                  ,[self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_CLKRoutingTopLeftMet2']['_Width']/2, self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][1]]]]
            
            self._DesignParameter['_CLKRoutingTopLeftMet3']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_CLKRoutingTopLeftMet3']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0]
                                                                                  ,[self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][1] ] ]]

            
            self._DesignParameter['_CLKBarRoutingTopLeftMet3']['_Width'] = _DRCObj._MetalxMinWidth
            tmpX = self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2  - _DRCObj._MetalxMinSpace - self._DesignParameter['_CLKBarRoutingTopLeftMet3']['_Width']/2
            self._DesignParameter['_CLKBarRoutingTopLeftMet3']['_XYCoordinates'] =  [[ self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_XYCoordinates'][0]
                                                                                      ,[ tmpX, self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_XYCoordinates'][0][1] ] 
                                                                                      ,[ tmpX, self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][1] ] 
                                                                                      ,[self._DesignParameter['_ViaMet32Met4OnCLKBarTop']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][1] ]
                                                                                                ]]


            
            
            
            # # )############################### Selection Via Met12Met2 #########################
            if _XBiasForViaMet12Met2OnSelectionXORtopLeft is None:
                _XBiasForViaMet12Met2OnSelectionXORtopLeft = 0
                
            if _XBiasForViaMet12Met2OnSelectionXORtopRight is None:
                _XBiasForViaMet12Met2OnSelectionXORtopRight = 0
                
            if _XBiasForViaMet12Met2OnSelectionBarXORtopLeft is None:
                _XBiasForViaMet12Met2OnSelectionBarXORtopLeft = 0
                
            if _XBiasForViaMet12Met2OnSelectionBarXORtopRight is None:
                _XBiasForViaMet12Met2OnSelectionBarXORtopRight = 0
                
            if _XBiasForViaMet12Met2OnSelectionXORbotLeft is None:
                _XBiasForViaMet12Met2OnSelectionXORbotLeft = 0
            
            if _XBiasForViaMet12Met2OnSelectionXORbotRight is None:
                _XBiasForViaMet12Met2OnSelectionXORbotRight = 0
                
            if _XBiasForViaMet12Met2OnSelectionBarXORbotLeft is None:
                _XBiasForViaMet12Met2OnSelectionBarXORbotLeft = 0
                
            if _XBiasForViaMet12Met2OnSelectionBarXORbotRight is None:
                _XBiasForViaMet12Met2OnSelectionBarXORbotRight = 0
            
            self._DesignParameter['_ViaMet12Met2OnSelectionXORbotLeft']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionXORbotLeft + self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0] + (self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionXORbotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]]]
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotLeft']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionBarXORbotLeft + self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0] - (self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_ViaMet12Met2OnSelectionXORbotRight']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionXORbotRight+ self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0] - (self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionXORbotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotRight']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionBarXORbotRight + self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0] + (self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]]]
            
            self._DesignParameter['_ViaMet22Met3OnSelectionXORbotLeft']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionXORbotLeft']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotLeft']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotLeft']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet22Met3OnSelectionXORbotRight']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionXORbotRight']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotRight']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotRight']['_XYCoordinates'][0] ]
            
            self._DesignParameter['_ViaMet32Met4OnSelectionXORbotLeft']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionXORbotLeft']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet32Met4OnSelectionBarXORbotLeft']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotLeft']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet32Met4OnSelectionXORbotRight']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionXORbotRight']['_XYCoordinates'][0] ]
            self._DesignParameter['_ViaMet32Met4OnSelectionBarXORbotRight']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet12Met2OnSelectionBarXORbotRight']['_XYCoordinates'][0] ]


            self._DesignParameter['_ViaMet12Met2OnSelectionXORtopLeft']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionXORtopLeft + self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0] - (self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionXORtopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]) ]]
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopLeft']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionBarXORtopLeft + self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0] + (self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]) ]]
            self._DesignParameter['_ViaMet12Met2OnSelectionXORtopRight']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionXORtopRight+ self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0] + (self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionXORtopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]) ]]
            self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopRight']['_XYCoordinates'] = [[_XBiasForViaMet12Met2OnSelectionBarXORtopRight + self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0] - (self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - self._DesignParameter['_ViaMet12Met2OnSelectionBarXORtopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])/2 
                                                                                             ,self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]) ]]
            

            # # )############################### Selection Metal Routing #########################
            
            self._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionRoutingXORbotRightMet4']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionBarRoutingXORbotLeftMet4']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionBarRoutingXORbotRightMet4']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionRoutingXORtopRightMet2']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionBarRoutingXORtopLeftMet2']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_SelectionBarRoutingXORtopRightMet2']['_Width'] = _DRCObj._MetalxMinWidth
           
            #Rigth-side Biased Via
            for i in range(0,4):
                if i is 0:
                    VIA = '_ViaMet12Met2OnSelectionXORbotLeft'
                    RoutingMet = '_SelectionRoutingXORbotLeftMet4'
                    TopOrBot = '_XORbot'
                    PMOS = '_PMOS1'
                elif i is 1:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotRight'
                    RoutingMet = '_SelectionBarRoutingXORbotRightMet4'
                    TopOrBot = '_XORbot'
                    PMOS = '_PMOS4'
                elif i is 2:
                    VIA = '_ViaMet12Met2OnSelectionBarXORtopLeft'
                    RoutingMet = '_SelectionBarRoutingXORtopLeftMet2'
                    TopOrBot = '_XORtop'
                    PMOS = '_PMOS1'
                elif i is 3:
                    VIA = '_ViaMet12Met2OnSelectionXORtopRight'
                    RoutingMet = '_SelectionRoutingXORtopRightMet2'
                    TopOrBot = '_XORtop'
                    PMOS = '_PMOS4'
                    
                VIA_RightSide = self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 - self._DesignParameter[RoutingMet]['_Width']/2
                MOS_RightSide = self._DesignParameter[TopOrBot]['_XYCoordinates'][0][0] + self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0]
                
                if VIA_RightSide > MOS_RightSide:
                    print ('WIP')
                    if PMOS is '_PMOS1' :
                        ConnectionIndex = len(self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) - 1
                    else :
                        ConnectionIndex = -len(self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1
                    MOSConnectionVia_RightSideXlocation = self._DesignParameter[TopOrBot]['_XYCoordinates'][0][0] +  self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][ConnectionIndex][0] + self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
                    MOS_RightSide = MOSConnectionVia_RightSideXlocation + self._DesignParameter[RoutingMet]['_Width']/2 + max(_DRCObj._MetalxMinSpace,_DRCObj._MetalxMinSpaceAtCorner)
                # else :
                self._DesignParameter[RoutingMet]['_XYCoordinates'] = [[ [VIA_RightSide , self._DesignParameter[VIA]['_XYCoordinates'][0][1]]
                                                                        ,[MOS_RightSide , self._DesignParameter[VIA]['_XYCoordinates'][0][1]]
                                                                        ,[MOS_RightSide , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1]) + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2 ]
                                                                          ]]
            
            
            #Left-side Biased Via
            for i in range(0,4):
                if i is 0:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotLeft'
                    RoutingMet = '_SelectionBarRoutingXORbotLeftMet4'
                    TopOrBot = '_XORbot'
                    PMOS = '_PMOS1'
                elif i is 1:
                    VIA = '_ViaMet12Met2OnSelectionXORbotRight'
                    RoutingMet = '_SelectionRoutingXORbotRightMet4'
                    TopOrBot = '_XORbot'
                    PMOS = '_PMOS4'
                elif i is 2:
                    VIA = '_ViaMet12Met2OnSelectionXORtopLeft'
                    RoutingMet = '_SelectionRoutingXORtopLeftMet2'
                    TopOrBot = '_XORtop'
                    PMOS = '_PMOS1'
                elif i is 3:
                    VIA = '_ViaMet12Met2OnSelectionBarXORtopRight'
                    RoutingMet = '_SelectionBarRoutingXORtopRightMet2'
                    TopOrBot = '_XORtop'
                    PMOS = '_PMOS4'
                    
                VIA_LeftSide = self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 + self._DesignParameter[RoutingMet]['_Width']/2
                MOS_LeftSide = self._DesignParameter[TopOrBot]['_XYCoordinates'][0][0] + self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                
                if VIA_LeftSide < MOS_LeftSide:
                    print ('WIP')
                    if PMOS is '_PMOS1' :
                        ConnectionIndex = 0
                    else :
                        ConnectionIndex = -len(self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_InvPMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) -len(self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])
                        
                    MOSConnectionVia_LeftSideXlocation = self._DesignParameter[TopOrBot]['_XYCoordinates'][0][0] +  self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][ConnectionIndex][0] - self._DesignParameter[TopOrBot]['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
                    MOS_LeftSide = MOSConnectionVia_LeftSideXlocation - self._DesignParameter[RoutingMet]['_Width']/2 - max(_DRCObj._MetalxMinSpace,_DRCObj._MetalxMinSpaceAtCorner)
                # else :
                self._DesignParameter[RoutingMet]['_XYCoordinates'] = [[ [VIA_LeftSide , self._DesignParameter[VIA]['_XYCoordinates'][0][1]]
                                                                        ,[MOS_LeftSide , self._DesignParameter[VIA]['_XYCoordinates'][0][1]]
                                                                        ,[MOS_LeftSide , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1]) + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2 ]
                                                                          ]]
            
            
            
            
            
            # # )################################ DRC Verification ################################
            DRC_PASS=1
            
            self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NbodyContact']['ignore'] = True

            #ViaMet32Met4OnFFBotOutput MinArea for Met3
            Area = self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] += round((_DRCObj._MetalxMinArea-Area)/self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5) * 2 * _DRCObj._MinSnapSpacing
            
                        
            # FFbot Output Via COX adjusting
            # lenOfVia = self._DesignParameter['_ViaMet22Met3OnFFBotOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            # lenOfOutputMet2 = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][0]
            # print 'Americano', lenOfVia, lenOfOutputMet2, _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide
            # if lenOfVia < 0.8 * lenOfOutputMet2: # - 4* _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide:
                # _FFbotOutputViaCOX = int( (lenOfOutputMet2 - 2*_DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide ) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth) )
                # DRC_PASS = 0
            
            # XOR Input Top Via METALx Area Check
            Area =  self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] * self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet32Met4OnXORTopInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5 ) * _DRCObj._MinSnapSpacing *2
            
            Area =  self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet22Met3OnXORTopInput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5 ) * _DRCObj._MinSnapSpacing *2

            self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['ignore'] = True

            # CLK Via MET2 Area Check
            Area = self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/_DRCObj._MinSnapSpacing/2 + 0.5 ) * _DRCObj._MinSnapSpacing *2
            
            Area = self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5 ) * _DRCObj._MinSnapSpacing *2
            
            Area = self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing *2
            
            Area = self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing *2
            
            Area = self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing *2
            
            Area = self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] * self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] += round( (_DRCObj._MetalxMinArea - Area)/self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing *2
            
            # #CLK, CLKbar Via Met1 Width Calibration
            # self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # # self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # # self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            
            # self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # # self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            # # self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            
            
            # CLKbar Bot Right Via X location adjusting and Met1 Connection
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0]
            leftIndex = 0
            RightIndex = 0
            for i in range(0, len(self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][-i][0][0] < viaXlocation):
                    leftIndex = -i
            for i in range(0, len(self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][i][0][0] > viaXlocation):
                    RightIndex = i

            leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_FFbotOutputRoutingMet2']['_Width']/2
            if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0]
            rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_FFbotOutputRoutingMet2']['_Width']/2
            if rightSpace < _DRCObj._MetalxMinSpace:
                self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                
            
                
            
            # CLK Bot Right Via X location adjusting
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0]
            leftIndex = 0
            RightIndex = 0
            for i in range(0, len(self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][-i][0][0] < viaXlocation):
                    leftIndex = -i
            for i in range(0, len(self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][i][0][0] > viaXlocation):
                    RightIndex = i

            leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_FFbotOutputRoutingMet2']['_Width']/2
            if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0]
            rightSpace = -viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_FFbotOutputRoutingMet2']['_Width']/2
            if rightSpace < _DRCObj._MetalxMinSpace:
                self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing

            
            
            # CLKbar Top Right Via X location adjusting
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0]
            leftIndex = 0
            for i in range(0, len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-i][0][0] < viaXlocation):
                    leftIndex = -i
            for i in range(0, len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][i][0][0] > viaXlocation):
                    RightIndex = i

            leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2
            if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0]
            rightSpace = -viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2
            if rightSpace < _DRCObj._MetalxMinSpace:
                self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            
            # CLK Top Right Via X location adjusting
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0]
            leftIndex = 0
            for i in range(0, len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][-i][0][0] < viaXlocation):
                    leftIndex = -i
            for i in range(0, len(self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates']) ):
                if (self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][i][0][0] > viaXlocation):
                    RightIndex = i

            leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2
            if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0] += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            viaXlocation = self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0]
            rightSpace = -viaXlocation - self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_FFtopOutputRoutingMet2']['_Width']/2
            if rightSpace < _DRCObj._MetalxMinSpace:
                self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0] -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing

                
            #CLK, CLKB Right Via and FF leftOutput Via Distance
            distanceX1 = self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            distanceX2 = self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            distanceX = min(distanceX1,distanceX2)
            if distanceX < _DRCObj._MetalxMinSpace:
                if _FlipFlopBotDesignCalculationParameters['_MOS32MOS4spacebias'] is None:
                    _FlipFlopBotDesignCalculationParameters['_MOS32MOS4spacebias'] = 0
                _FlipFlopBotDesignCalculationParameters['_MOS32MOS4spacebias'] += round((_DRCObj._MetalxMinSpace-distanceX)/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing
                DRC_PASS = 0
            
            distanceX1 = self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            distanceX2 = self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOS3Gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            distanceX = min(distanceX1,distanceX2)
            if distanceX < _DRCObj._MetalxMinSpace:
                if _FlipFlopTopDesignCalculationParameters['_MOS32MOS4spacebias'] is None:
                    _FlipFlopTopDesignCalculationParameters['_MOS32MOS4spacebias'] = 0
                _FlipFlopTopDesignCalculationParameters['_MOS32MOS4spacebias'] += round((_DRCObj._MetalxMinSpace-distanceX)/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing
                DRC_PASS = 0
                
            # ViaMet22Met3OnCLK Metal2 space ( Left) 
            upsideSpace = self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingNE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingNE']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKBotLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            upsideSpace = self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingSE']['_XYCoordinates'][0][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingSE']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKTopLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0           
            # ViaMet22Met3OnCLK Metal2 space ( Right)
            upsideSpace = self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            ViaDistanceAdjusting = (self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnCLKBotRight']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'])/2
            drc_temp = max(_DRCObj._MetalxMinSpaceAtCorner,_DRCObj._VIAxMinSpaceFor3neighboring - ViaDistanceAdjusting, _DRCObj._VIAxMinSpaceDifferentNet - ViaDistanceAdjusting)
            if upsideSpace < drc_temp:
                _YBiasForViaMet22Met3OnCLKBotRight -= round((drc_temp - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            upsideSpace = self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'][0][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingOnNMOSRight']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKTopRight -= round((_DRCObj._MetalxMinSpaceAtCorner  - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            # ViaMet22Met3OnCLKBar Metal2 space ( Right)
            upsideSpace = -self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnNMOSRight']['_XYCoordinates'][0][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingOnNMOSRight']['_Width']/2 + self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKBarBotRight += round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            upsideSpace = -self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] - (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_XYCoordinates'][0][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingOnPMOSRight']['_Width']/2 + self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKBarTopRight += round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            
            # ViaMet22Met3OnCLKBar Metal2 space ( Left) 
            upsideSpace = self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingNE']['_XYCoordinates'][0][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_OutputRoutingNE']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKBarBotLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                _YBiasForViaMet12Met2OnCLKBarBotLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0
            upsideSpace = self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingSE']['_XYCoordinates'][0][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_OutputRoutingSE']['_Width']/2 - self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet22Met3OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            if upsideSpace < _DRCObj._MetalxMinSpaceAtCorner:
                _YBiasForViaMet22Met3OnCLKBarTopLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                _YBiasForViaMet12Met2OnCLKBarTopLeft -= round((_DRCObj._MetalxMinSpaceAtCorner - upsideSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                DRC_PASS=0           
            
            
            
            # ViaMet22Met3OnCLK left and ViaMet12Met2OnCLKBar left distance for BOT
            distanceX = self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            if distanceX < _DRCObj._MetalxMinSpace:
                if _FlipFlopBotDesignCalculationParameters['_MOS22MOS3spacebias'] is None:
                    _FlipFlopBotDesignCalculationParameters['_MOS22MOS3spacebias'] = 0
                _FlipFlopBotDesignCalculationParameters['_MOS22MOS3spacebias'] += round((_DRCObj._MetalxMinSpace - distanceX)/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing*2
                DRC_PASS = 0
            
            # ViaMet22Met3OnCLK left and ViaMet12Met2OnCLKBar left distance for TOP
            distanceX = self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            if distanceX < _DRCObj._MetalxMinSpace:
                if _FlipFlopTopDesignCalculationParameters['_MOS22MOS3spacebias'] is None:
                    _FlipFlopTopDesignCalculationParameters['_MOS22MOS3spacebias'] = 0
                _FlipFlopTopDesignCalculationParameters['_MOS22MOS3spacebias'] += round((_DRCObj._MetalxMinSpace - distanceX)/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing*2
                DRC_PASS = 0
            
            
            # ViaMet32Met4OnCKTOP Vertical and Met3Connection
            if self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOSConnectionRoutingRight']['_Ignore'] is not True:
                distanceY = self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOSConnectionRoutingRight']['_XYCoordinates'][0][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOSConnectionRoutingRight']['_Width']/2 \
                            - self._DesignParameter['_ViaMet32Met4OnCLKTop']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet32Met4OnCLKTop']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
                if distanceY < _DRCObj._MetalxMinSpace:
                    _YBiasForViaMet32Met4OnCLKTopvertical -= round((_DRCObj._MetalxMinSpace - distanceY)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0

            ####XOR (bot) INPUT Metal2 DRC check (distance)
            # XORbotInputViaMet2_upSide = self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            # XORbotOutputMet2_downSide = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_Width']/2
            # distance = XORbotInputViaMet2_upSide - XORbotOutputMet2_downSide
            # if distance < _DRCObj._MetalxMinSpace:
                # _YBiasForViaMet12Met2OnXORbotInput -= round((_DRCObj._MetalxMinSpace-distance) / _DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                # # DRC_PASS = 0
                    
            # ####XOR (top) INPUT Metal2 DRC check (distance)
            # XORbotInputViaMet2_upSide = self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnXORBotInput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2
            # XORbotOutputMet2_downSide = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_Width']/2
            # distance = XORbotInputViaMet2_upSide - XORbotOutputMet2_downSide
            # if distance < _DRCObj._MetalxMinSpace:
                # _YBiasForViaMet12Met2OnXORbotInput -= round((_DRCObj._MetalxMinSpace-distance) / _DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                # DRC_PASS = 0
                    

            # CLK Right Via to FFtop CLK additional Met1
            CLK_VIA_RIGHT = self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            FF_VIA_LEFT = self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            if CLK_VIA_RIGHT < FF_VIA_LEFT:
                self.DesignParameter['_AdditionalMet1OnFFTopCLKRight']['_Width'] = self.DesignParameter['_ViaMet12Met2OnCLKTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self.DesignParameter['_AdditionalMet1OnFFTopCLKRight']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0]  
                                                                                             ,[ FF_VIA_LEFT , self._DesignParameter['_ViaMet12Met2OnCLKTopRight']['_XYCoordinates'][0][1] ]  ]]
            # CLKBar Right Via to FFtop CLK additional Met1
            CLK_VIA_RIGHT = self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            FF_VIA_LEFT = self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            if CLK_VIA_RIGHT < FF_VIA_LEFT:
                self.DesignParameter['_AdditionalMet1OnFFTopCLKBarRight']['_Width'] = self.DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self.DesignParameter['_AdditionalMet1OnFFTopCLKBarRight']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0]  
                                                                                             ,[ FF_VIA_LEFT , self._DesignParameter['_ViaMet12Met2OnCLKBarTopRight']['_XYCoordinates'][0][1] ]  ]]
            # CLK Right Via to FFbot CLK additional Met1
            CLK_VIA_RIGHT = self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            FF_VIA_LEFT = self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            if CLK_VIA_RIGHT < FF_VIA_LEFT:
                self.DesignParameter['_AdditionalMet1OnFFBotCLKRight']['_Width'] = self.DesignParameter['_ViaMet12Met2OnCLKBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self.DesignParameter['_AdditionalMet1OnFFBotCLKRight']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0]  
                                                                                             ,[ FF_VIA_LEFT , self._DesignParameter['_ViaMet12Met2OnCLKBotRight']['_XYCoordinates'][0][1] ]  ]]
            # CLK Right Via to FFtop CLK additional Met1
            CLK_VIA_RIGHT = self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            FF_VIA_LEFT = self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS4Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
            if CLK_VIA_RIGHT < FF_VIA_LEFT:
                self.DesignParameter['_AdditionalMet1OnFFTopCLKBarBotRight']['_Width'] = self.DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                self.DesignParameter['_AdditionalMet1OnFFTopCLKBarBotRight']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0]  
                                                                                             ,[ FF_VIA_LEFT , self._DesignParameter['_ViaMet12Met2OnCLKBarBotRight']['_XYCoordinates'][0][1] ]  ]]
                
            # CLK ROUTING(MET4) 2 FFbot OUTPUT M32M4Via Space
            space = self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet32Met4OnFFBotOutput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2 - self._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0][0] - self._DesignParameter['_CLKBarRoutingMet4']['_Width']/2
            if space < _DRCObj._MetalxMinSpace:
                _XBiasForCLKverticalMet4 -= round ((_DRCObj._MetalxMinSpace-space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                _XBiasForCLKbarverticalMet4 -= round ((_DRCObj._MetalxMinSpace-space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                       
                
            #CLKbar Left Additional Met1
            Met1_LeftSide = min( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_RightSide = max( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_UpSide = max( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            Met1_DownSide = min( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnCLKBarBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            
            self._DesignParameter['_AdditionalMet1OnCLKBarBotLeft']['_XWidth'] = Met1_RightSide-Met1_LeftSide
            self._DesignParameter['_AdditionalMet1OnCLKBarBotLeft']['_YWidth'] = Met1_UpSide-Met1_DownSide
            self._DesignParameter['_AdditionalMet1OnCLKBarBotLeft']['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            
            Met1_LeftSide = min( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_RightSide = max( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_UpSide = max( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1]) + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            Met1_DownSide = min( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnCLKBarTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            
            self._DesignParameter['_AdditionalMet1OnCLKBarTopLeft']['_XWidth'] = Met1_RightSide-Met1_LeftSide
            self._DesignParameter['_AdditionalMet1OnCLKBarTopLeft']['_YWidth'] = Met1_UpSide-Met1_DownSide
            self._DesignParameter['_AdditionalMet1OnCLKBarTopLeft']['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            print ('straw1' , self._DesignParameter['_AdditionalMet1OnCLKBarTopLeft']['_XYCoordinates'])
            
            #CLK Left Additional Met1
            Met1_LeftSide = min( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_RightSide = max( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][0] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_UpSide = max( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            Met1_DownSide = min( (self._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_XYCoordinates'][0][1] - self._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnCLKBotLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            
            self._DesignParameter['_AdditionalMet1OnCLKBotLeft']['_XWidth'] = Met1_RightSide-Met1_LeftSide
            self._DesignParameter['_AdditionalMet1OnCLKBotLeft']['_YWidth'] = Met1_UpSide-Met1_DownSide
            self._DesignParameter['_AdditionalMet1OnCLKBotLeft']['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            
            Met1_LeftSide = min( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][0] - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_RightSide = max( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][0] + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)    )
            Met1_UpSide = max( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1]) + self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            Met1_DownSide = min( (self._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_XYCoordinates'][0][1]) - self._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOS2Gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                               , (self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2OnCLKTopLeft']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)    )
            
            self._DesignParameter['_AdditionalMet1OnCLKTopLeft']['_XWidth'] = Met1_RightSide-Met1_LeftSide
            self._DesignParameter['_AdditionalMet1OnCLKTopLeft']['_YWidth'] = Met1_UpSide-Met1_DownSide
            self._DesignParameter['_AdditionalMet1OnCLKTopLeft']['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            

            #Selection Via Additional Met1 (Bot)
            for i in range(0 , 4):
                if i is 0:
                    VIA = '_ViaMet12Met2OnSelectionXORbotLeft'
                    AddiMet = '_AdditionalMet1OnSelectionXORbotLeft'
                    NthGateVia = '_ViaPoly2Met1OnMOS1Gate'
                    GateNorP = 1  #1 is P, 0 is N
                elif i is 1:
                    VIA = '_ViaMet12Met2OnSelectionXORbotRight'
                    AddiMet = '_AdditionalMet1OnSelectionXORbotRight'
                    NthGateVia = '_ViaPoly2Met1OnMOS4Gate'
                    GateNorP = 0
                elif i is 2:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotLeft'
                    AddiMet = '_AdditionalMet1OnSelectionBarXORbotLeft'
                    NthGateVia = '_ViaPoly2Met1OnMOS1Gate'
                    GateNorP = 0
                elif i is 3:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotRight'
                    AddiMet = '_AdditionalMet1OnSelectionBarXORbotRight'
                    NthGateVia = '_ViaPoly2Met1OnMOS4Gate'
                    GateNorP = 1
                    
                Met1_RightSide = max( self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                    , self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Met1_LeftSide = min( self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                    , self._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][0] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Met1_UpSide = max( self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                                    , self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                Met1_DownSide = min( self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                                    , self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][1] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                self._DesignParameter[AddiMet]['_XWidth'] = Met1_RightSide-Met1_LeftSide
                self._DesignParameter[AddiMet]['_YWidth'] = Met1_UpSide-Met1_DownSide
                self._DesignParameter[AddiMet]['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            
            #Selection Via Additional Met1 (Top)
            for i in range(0 , 4):
                if i is 0:
                    VIA = '_ViaMet12Met2OnSelectionXORtopLeft'
                    AddiMet = '_AdditionalMet1OnSelectionXORtopLeft'
                    NthGateVia = '_ViaPoly2Met1OnMOS1Gate'
                    GateNorP = 1  #1 is P, 0 is N
                elif i is 1:
                    VIA = '_ViaMet12Met2OnSelectionXORtopRight'
                    AddiMet = '_AdditionalMet1OnSelectionXORtopRight'
                    NthGateVia = '_ViaPoly2Met1OnMOS4Gate'
                    GateNorP = 0
                elif i is 2:
                    VIA = '_ViaMet12Met2OnSelectionBarXORtopLeft'
                    AddiMet = '_AdditionalMet1OnSelectionBarXORtopLeft'
                    NthGateVia = '_ViaPoly2Met1OnMOS1Gate'
                    GateNorP = 0
                elif i is 3:
                    VIA = '_ViaMet12Met2OnSelectionBarXORtopRight'
                    AddiMet = '_AdditionalMet1OnSelectionBarXORtopRight'
                    NthGateVia = '_ViaPoly2Met1OnMOS4Gate'
                    GateNorP = 1
                    
                Met1_RightSide = max( self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                    , self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Met1_LeftSide = min( self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                    , self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][0] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                Met1_UpSide = max( self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                                    , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][1]) + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                Met1_DownSide = min( self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                                    , self._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_XYCoordinates'][GateNorP][1]) - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter[NthGateVia]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                self._DesignParameter[AddiMet]['_XWidth'] = Met1_RightSide-Met1_LeftSide
                self._DesignParameter[AddiMet]['_YWidth'] = Met1_UpSide-Met1_DownSide
                self._DesignParameter[AddiMet]['_XYCoordinates'] =[ [(Met1_RightSide+Met1_LeftSide)/2 ,(Met1_UpSide+Met1_DownSide)/2] ]
            
            #Selection Via Additional Met2,3 (Bot)
            for i in range(0,4):
                if i is 0:
                    VIA = '_ViaMet12Met2OnSelectionXORbotLeft'
                elif i is 1:
                    VIA = '_ViaMet12Met2OnSelectionXORbotRight'
                elif i is 2:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotLeft'
                elif i is 3:
                    VIA = '_ViaMet12Met2OnSelectionBarXORbotRight'
                    
                Met_YWidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] 
                Met_XWidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] 
                Area = Met_XWidth * Met_YWidth
                if Area < _DRCObj._MetalxMinArea:
                    expand_val = round(_DRCObj._MetalxMinArea / Met_XWidth / _DRCObj._MinSnapSpacing / 2 + 0.5) * _DRCObj._MinSnapSpacing * 2
                    self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = expand_val
                
            for i in range(0,4):
                if i is 0:
                    VIA = '_ViaMet22Met3OnSelectionXORbotLeft'
                elif i is 1:
                    VIA = '_ViaMet22Met3OnSelectionXORbotRight'
                elif i is 2:
                    VIA = '_ViaMet22Met3OnSelectionBarXORbotLeft'
                elif i is 3:
                    VIA = '_ViaMet22Met3OnSelectionBarXORbotRight'
                    
                Met_YWidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] 
                Met_XWidth = self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] 
                Area = Met_XWidth * Met_YWidth
                if Area < _DRCObj._MetalxMinArea:
                    expand_val = round(_DRCObj._MetalxMinArea / Met_XWidth / _DRCObj._MinSnapSpacing / 2 + 0.5) * _DRCObj._MinSnapSpacing * 2
                    self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = expand_val
                
            
            #DRC Space BTW Selection Routing Met2 and MOS2 Connection Routing Via
            tempIndex = len(self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) 
            ConnectionVia_LeftSide = self._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_XYCoordinates'][tempIndex][0] - self._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSconnection']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2
            RoutingMet_RightSide = self._DesignParameter['_SelectionBarRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_SelectionBarRoutingXORtopLeftMet2']['_Width']/2

            Space =  ConnectionVia_LeftSide - RoutingMet_RightSide
            
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                if _XorTopDesignCalculatrionParameters['_MOS12MOS2spacebias'] is None:
                    _XorTopDesignCalculatrionParameters['_MOS12MOS2spacebias'] = 0
                if _XorBotDesignCalculatrionParameters['_MOS12MOS2spacebias'] is None:
                    _XorBotDesignCalculatrionParameters['_MOS12MOS2spacebias'] = 0
                
                _XorTopDesignCalculatrionParameters['_MOS12MOS2spacebias'] += SpaceBias
                _XorBotDesignCalculatrionParameters['_MOS12MOS2spacebias'] += SpaceBias
                DRC_PASS = 0
            
            
            
            #SelectionVia Y-location Adjusting (SelectionBarXORbotLeft)
            VIA_DownSide = self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotLeft']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotLeft']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            MOSConnectionMet3_Upside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_Width']/2
            Space = VIA_DownSide - MOSConnectionMet3_Upside
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                if _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS1GateVia'] is None:
                    _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS1GateVia'] = 0
                _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS1GateVia'] += SpaceBias
            #SelectionVia Y-location Adjusting (SelectionXORbotRight)
            VIA_DownSide = self._DesignParameter['_ViaMet22Met3OnSelectionXORbotRight']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3OnSelectionXORbotRight']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            MOSConnectionMet3_Upside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_XYCoordinates'][1][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_Width']/2
            Space = VIA_DownSide - MOSConnectionMet3_Upside
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                if _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS4GateVia'] is None:
                    _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS4GateVia'] = 0
                _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasNMOS4GateVia'] += SpaceBias
            
            #SelectionVia Y-location Adjusting (SelectionXORbotLeft)
            VIA_UpSide = self._DesignParameter['_ViaMet22Met3OnSelectionXORbotLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet22Met3OnSelectionXORbotLeft']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            MOSConnectionMet3_Downside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_Width']/2
            Space = MOSConnectionMet3_Downside - VIA_UpSide
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = -round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                if _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS1GateVia'] is None:
                    _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS1GateVia'] = 0
                _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS1GateVia'] += SpaceBias
            #SelectionVia Y-location Adjusting (SelectionBarXORbotRight)
            VIA_UpSide = self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotRight']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet22Met3OnSelectionBarXORbotRight']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            MOSConnectionMet3_Downside = self._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_XYCoordinates'][1][0][1] - self._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_Width']/2
            Space = MOSConnectionMet3_Downside - VIA_UpSide
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = -round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                if _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS4GateVia'] is None:
                    _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS4GateVia'] = 0
                _XorBotDesignCalculatrionParameters['_BiasDictforViaPoly2Met1OnGate']['_YbiasPMOS4GateVia'] += SpaceBias
            
            
            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  DelayUnit Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        


if __name__=='__main__':


                
    ##############045nm delayUnit #####################################################################
    DelayUnitObj=_DELAYUNIT(_DesignParameter=None, _Name='DelayUnit')
    DelayUnitObj._CalculateDesignParameter( 
    
                                     _FlipFlopTopDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPtop),
                                     _FlipFlopBotDesignCalculationParameters=copy.deepcopy(DelayUnitDesign._FLIPFLOPtop),
                                     
                                     _XorTopDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORtop),
                                     _XorBotDesignCalculatrionParameters=copy.deepcopy(DelayUnitDesign._XORtop),
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
                                         _Dummy=True)
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
    DelayUnitObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=DelayUnitObj._DesignParameter)
    _fileName='autoDelayUnit_45.gds'
    
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=DelayUnitObj._CreateGDSStream(DelayUnitObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()


    print ('###############open ftp connection & update gds file to cadence server###################')
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
    print (ftp_cadence_server.pwd())
    testStreamFile = open('./{}'.format(_fileName), 'rb')
    ftp_cadence_server.storbinary('STOR {}'.format(_fileName), testStreamFile)
    print ('close ftp connection')
    ftp_cadence_server.quit()
    testStreamFile.close()


    print ('##########################################################################################')




# Consider output routing on PMOS DRC






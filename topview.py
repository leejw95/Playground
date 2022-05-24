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
import ClkTreeElement
import ClkTreeUnit
import Tree
import DelayUnitX4
# import DelayUnitDesign
# import TreeDesign


import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _TopView(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
    
                                     _NumberOfParallelBufferLeftSide = None,
                                     _NumberOfParallelBufferRightSide = None, _XbiasForTreeLeft =None, _XbiasForTreeRight =None,
                                     _BufferDistance = None, _BufferConnectionMetalWidth=None, _MetalxDRCforTopBuffer = None, _TreeYlocation=None,
                                     _ParallelBufferDesignCalculationParameters = {
                                        #########################################EXAMPLE##############################################
                                        ## Default Parameter For Any Buffers ##
                                        
                                        # _Default = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Left Node(s) ##
                                        # n is from 1 to _NumberOfParallelBufferLeftSide
                                        # _DictForBufferL{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Right Node(s) ##
                                        # n is from 1 to _NumberOfParallelBufferRightSide
                                        # _DictForBufferR{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        },
                                     
                                     
                                     _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitX4._DELAYUNITX4._ParametersForDesignCalculation),
                                     _TreeDesignCalculationParameters = copy.deepcopy(Tree._CLKTree._ParametersForDesignCalculation),
                                     # _ParallelBufferDesignCalculationParameters = copy.deepcopy(ClkTreeUnit._CLKTreeUnit._ParametersForDesignCalculation),
                                     # _ParallelBufferDesignCalculationParameters = copy.deepcopy(TreeDesign._TreeDesign['_DictForCLKTreeUnitParameters']['_Default']),

                                     _DictForVDD2VSSHeightandNWPPedge = dict(
                                        # _Vdd2VssHeightForBot0 = None, for FF
                                        # _Vdd2VssHeightForBot1 = None, for XOR and Buffer
                                        # _Vdd2VssHeightForLevel1 = None, for Leveln TreeNode
                                     ),

                                     _DictForNodeOutPin = dict(
                                        # _Node1 = Name
                                        # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                         #_LR = [Left,Right]
                                         # pinText = _Node + _Output
                                     ),

                                     _DictForNodeOutUpPin = dict(
                                        # _Node2 = Name
                                        # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                     ),

                                     _DictForNodeInPin = dict(
                                        # _Node2 = Name
                                        # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                     ),

                                     _Buffer2TreeMetWidth = None,

                                     _AdditionalMet1ForSupplydict = dict(
                                         #Addi1 = [ Left = 1000, Right = 1500, Top = 200, Bot = 0 ],
                                         #Add12 = [ Left = 1000, Right = 1500, Top = 200, Bot = 0 ],

                                     ),

                                     
                                    _BufferLenDict = dict(

                                     ),
                                     
                                     _SupplyCOY = dict(
                                      # NumberOfCOYforLevel0 = 1
                                     
                                     
                                     
                                    ),
                                     
                                     
                                     
                                     
                                     

                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTree'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(

                                                    _DelayUnit = self._SrefElementDeclaration(_DesignObj=DelayUnitX4._DELAYUNITX4(_DesignParameter=None, _Name= 'DelayUnitIn{}'.format(_Name)))[0],
                                                    _TreeLeft = self._SrefElementDeclaration(_DesignObj=Tree._CLKTree(_DesignParameter=None, _Name= 'TreeLeftIn{}'.format(_Name)))[0],
                                                    _TreeRight = self._SrefElementDeclaration(_DesignObj=Tree._CLKTree(_DesignParameter=None, _Name= 'TreeRightIn{}'.format(_Name)))[0],
                                                    _VDDpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VDD' ),
                                                    _VSSpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VSS' ),
                                                    _OutL1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL0' ),
                                                    _OutL2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL1' ),
                                                    _OutL3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL1' ),
                                                    _OutL4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL0' ),
                                                    _OutL5 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKtreeL' ),
                                                    _OutL6 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL2' ),
                                                    _OutL7 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL3' ),
                                                    _OutL8 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL3' ),
                                                    _OutL9 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL2' ),
                                                    _OutL10 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKbtreeL' ),
                                                    _OutR1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER0' ),
                                                    _OutR2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER1' ),
                                                    _OutR3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR1' ),
                                                    _OutR4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR0' ),
                                                    _OutR5 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKtreeR' ),
                                                    _OutR6 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER2' ),
                                                    _OutR7 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER3' ),
                                                    _OutR8 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR3' ),
                                                    _OutR9 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR2' ),
                                                    _OutR10 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKbtreeR' ),
# _OutL1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Ol0' ),
#                                                     _OutL2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL1' ),
#                                                     _OutL3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL1' ),
#                                                     _OutL4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL0' ),
#                                                     _OutL5 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKtreeL' ),
#                                                     _OutL6 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL2' ),
#                                                     _OutL7 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL3' ),
#                                                     _OutL8 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OL3' ),
#                                                     _OutL9 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='EL2' ),
#                                                     _OutL10 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKbtreeL' ),
#                                                     _OutR1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR0' ),
#                                                     _OutR2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER1' ),
#                                                     _OutR3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR1' ),
#                                                     _OutR4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER0' ),
#                                                     _OutR5 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKtreeR' ),
#                                                     _OutR6 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR2' ),
#                                                     _OutR7 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER3' ),
#                                                     _OutR8 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OR3' ),
#                                                     _OutR9 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='ER2' ),
#                                                     _OutR10 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKbtreeR' ),

                                                    _Sel1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel1' ),
                                                    _Selb1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb1' ),
                                                    _Sel2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel2' ),
                                                    _Selb2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb2' ),
                                                    _Sel3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel3' ),
                                                    _Selb3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb3' ),
                                                    _Sel4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel4' ),
                                                    _Selb4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb4' ),

                                                    _M4Sel1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel1' ),
                                                    _M4Selb1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb1' ),
                                                    _M4Sel2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel2' ),
                                                    _M4Selb2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb2' ),
                                                    _M4Sel3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel3' ),
                                                    _M4Selb3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb3' ),
                                                    _M4Sel4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Sel4' ),
                                                    _M4Selb4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='Selb4' ),

                                                    _M4CLK = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLK' ),
                                                    _M4CLKbar = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKbar' ),

                                                    _Input1pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='D1',),
                                                    _Input2pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='D2',),


                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)

    def _CalculateDesignParameter(self,
_NumberOfParallelBufferLeftSide = None,
                                     _NumberOfParallelBufferRightSide = None, _XbiasForTreeLeft =None, _XbiasForTreeRight =None,
                                     _BufferDistance = None, _BufferConnectionMetalWidth=None, _MetalxDRCforTopBuffer = None, _TreeYlocation=None,
                                     _ParallelBufferDesignCalculationParameters = {
                                        #########################################EXAMPLE##############################################
                                        ## Default Parameter For Any Buffers ##
                                        
                                        # _Default = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Left Node(s) ##
                                        # n is from 1 to _NumberOfParallelBufferLeftSide
                                        # _DictForBufferL{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Right Node(s) ##
                                        # n is from 1 to _NumberOfParallelBufferRightSide
                                        # _DictForBufferR{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        },
                                     
                                     
                                     _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitX4._DELAYUNITX4._ParametersForDesignCalculation),
                                     _TreeDesignCalculationParameters = copy.deepcopy(Tree._CLKTree._ParametersForDesignCalculation),
                                     # _ParallelBufferDesignCalculationParameters = copy.deepcopy(ClkTreeUnit._CLKTreeUnit._ParametersForDesignCalculation),
                                     # _ParallelBufferDesignCalculationParameters = copy.deepcopy(TreeDesign._TreeDesign['_DictForCLKTreeUnitParameters']['_Default']),
                                     
                                     _Buffer2TreeMetWidth = None,

                                     _DictForVDD2VSSHeightandNWPPedge=dict(
                                       # _Vdd2VssHeightForBot0 = None, for FF
                                       # _Vdd2VssHeightForBot1 = None, for XOR and Buffer

                                       # _EdgeBtwNWandPWForBot0 = None, for FF
                                       # _EdgeBtwNWandPWForBot1 = None, for XOR and Buffer

                                     ),

                                      _DictForNodeOutPin=dict(
                                          # _Node1 = Name
                                          # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                          # pinText = _Node + _Output
                                      ),

                                      _DictForNodeOutUpPin=dict(
                                          # _Node2 = Name
                                          # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                      ),

                                      _DictForNodeInPin=dict(
                                          # _Node2 = Name
                                          # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]
                                      ),
                                      _AdditionalMet1ForSupplydict = dict(
                                         #Addi1 = [ Left = 1000, Right = 1500, Top = 200, Bot = 0 ],
                                         #Add12 = [ Left = 1000, Right = 1500, Top = 200, Bot = 0 ],

                                     ),

                                     
                                     _BufferLenDict = dict(

                                     ),
                                     
                                     _SupplyCOY = dict(
                                      # _NumberOfCOYforLevel0 = 1
                                     ),

                                  _Dummy=None
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  Top View Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')



        _DRCObj=DRC.DRC()
        while True:
            
            ##############################################################Element Generation ################################################################

            if _BufferConnectionMetalWidth is None:
                _BufferConnectionMetalWidth=_DRCObj._MetalxMinWidth

            if ('_Vdd2VssHeightForBot0' in _DictForVDD2VSSHeightandNWPPedge) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopTopDesignCalculationParameters']['_FFVdd2VssHeight'] = _DictForVDD2VSSHeightandNWPPedge['_Vdd2VssHeightForBot0']
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopBotDesignCalculationParameters']['_FFVdd2VssHeight'] = _DictForVDD2VSSHeightandNWPPedge['_Vdd2VssHeightForBot0']
            if ('_EdgeBtwNWandPWForBot0' in _DictForVDD2VSSHeightandNWPPedge) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopTopDesignCalculationParameters']['_FFEdgeBtwNWandPW'] = _DictForVDD2VSSHeightandNWPPedge['_EdgeBtwNWandPWForBot0']
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopBotDesignCalculationParameters']['_FFEdgeBtwNWandPW'] = _DictForVDD2VSSHeightandNWPPedge['_EdgeBtwNWandPWForBot0']
            if ('_Vdd2VssHeightForBot1' in _DictForVDD2VSSHeightandNWPPedge) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorTopDesignCalculatrionParameters']['_XORVdd2VssHeight'] = _DictForVDD2VSSHeightandNWPPedge['_Vdd2VssHeightForBot1']
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_XORVdd2VssHeight'] = _DictForVDD2VSSHeightandNWPPedge['_Vdd2VssHeightForBot1']
            if ('_EdgeBtwNWandPWForBot1' in _DictForVDD2VSSHeightandNWPPedge) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorTopDesignCalculatrionParameters']['_XOREdgeBtwNWandPW'] = _DictForVDD2VSSHeightandNWPPedge['_EdgeBtwNWandPWForBot1']
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_XOREdgeBtwNWandPW'] = _DictForVDD2VSSHeightandNWPPedge['_EdgeBtwNWandPWForBot1']

            if ('_NumberOfCOYforLevel0' in _SupplyCOY) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopBotDesignCalculationParameters']['_NumberOfSupplyCOY'] = _SupplyCOY['_NumberOfCOYforLevel0']
            else:
                _SupplyCOY['_NumberOfCOYforLevel0'] = _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_FlipFlopBotDesignCalculationParameters']['_NumberOfSupplyCOY']
            
            if ('_NumberOfCOYforLevel1' in _SupplyCOY) is True:
                _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_NumberOfSupplyCOY'] = _SupplyCOY['_NumberOfCOYforLevel1']
            else:
                _SupplyCOY['_NumberOfCOYforLevel1'] = _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_NumberOfSupplyCOY']
            
            if ('_NumberOfCOYforLevel2' in _SupplyCOY) is True:
                _TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']['_Default']['_NumberOfSupplyCOY'] = _SupplyCOY['_NumberOfCOYforLevel2']
            else:
                _SupplyCOY['_NumberOfCOYforLevel2'] = _TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']['_Default']['_NumberOfSupplyCOY']
            
            
            
            
            _DelayUnitDesignCalculationParameters['_OutputWidth'] = _BufferConnectionMetalWidth
            self._DesignParameter['_DelayUnit']['_DesignObj']._CalculateDesignParameter(**_DelayUnitDesignCalculationParameters)
            self._DesignParameter['_TreeLeft']['_DesignObj']._CalculateDesignParameter(**_TreeDesignCalculationParameters)
            self._DesignParameter['_TreeRight']['_DesignObj']._CalculateDesignParameter(**_TreeDesignCalculationParameters)
            
            # self._DesignParameter['_TreeRight']['_Reflect']=(1,0,0)
            # self._DesignParameter['_TreeRight']['_Angle']=180
            
            
            ################################################BUFFER NODE GENERATION#########################################################
            if _NumberOfParallelBufferLeftSide is None:
                _NumberOfParallelBufferLeftSide = 0
            if _NumberOfParallelBufferRightSide is None:
                _NumberOfParallelBufferRightSide = 0
            if _MetalxDRCforTopBuffer is None:
                _MetalxDRCforTopBuffer = _DRCObj._MetalxMinSpace
            
            #######################BufferNodeNamingRule#######################
            #BufferYZZ :   Y- Left(0) Or Right(1) ZZ- BufferNodeNaming
            for j in range(0,2):
                Y= "%01d" %(j)
                if j is 0:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferLeftSide
                    Parameterbase = '_DictForBufferL'
                else:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferRightSide
                    Parameterbase = '_DictForBufferR'

                for k in range(0,_NumberOfParallelBuffer):
                    ZZ = "%02d" %(k)
                    BufferNode = '_ParallelBufferNode'+ Y + ZZ
                    Parameter = Parameterbase + str(k+1)
                    
                    tmpParameter = 'TopBufferParameter'
                    _ParallelBufferDesignCalculationParameters[tmpParameter] = dict()
                    
                    if (Parameter in _ParallelBufferDesignCalculationParameters) is True:
                        _ParallelBufferDesignCalculationParameters[tmpParameter] = copy.deepcopy(_ParallelBufferDesignCalculationParameters[Parameter])
                    else:
                        _ParallelBufferDesignCalculationParameters[tmpParameter] = copy.deepcopy(_ParallelBufferDesignCalculationParameters['_Default'])

                    if k is 0:
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['inputRotation'] = True

                    if k is not 0:
                        for ln in range(1,6):
                            _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['InLinelocation'+str(ln)] = self._DesignParameter['_ParallelBufferNode'+Y+'00']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(ln)]['_XYCoordinates'][0][1]
                            _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['OutLinelocation'+str(ln)] = self._DesignParameter['_ParallelBufferNode'+Y+'00']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(ln)]['_XYCoordinates'][0][1]
                  
                    
                    
                    
                    ####For Normarl Buffer (Not Last Buffer)
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_OutputViaLevelForTop'] =4
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_OutputViaLevelForBot'] =4
                    
                    # # # # # # # ####For Last Buffer
                    # # # # # # # if k is _NumberOfParallelBuffer-1:
                        # # # # # # # if ('_DictForNode1' in _TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']) is True:
                            # # # # # # # _ParallelBufferDesignCalculationParameters = copy.deepcopy(_TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']['_DictForNode1'])
                        # # # # # # # else:
                            # # # # # # # _ParallelBufferDesignCalculationParameters = copy.deepcopy(_TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']['_Default'])
                        # # # # # # # _ParallelBufferDesignCalculationParameters['_MetalOutType'] = 'Metal4andMetal6'
                    
                    ####Mendatory For These Buffers####
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_Vdd2VssHeight'] = self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_SupplyMetal1YWidth'] = self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_TreeLevel'] = 2
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_OutLineIgnore'] = False
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_MetalxDRC'] = _MetalxDRCforTopBuffer
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_ParallelMetalWidth'] = _BufferConnectionMetalWidth
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_NumberOfSupplyCOY'] = _SupplyCOY['_NumberOfCOYforLevel1']
                    
                    

                    if ('_EdgeBtwNWandPWForBot1' in _DictForVDD2VSSHeightandNWPPedge) is True:
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['_CLKTreeElementParameters']['_EdgeBtwNWandPW'] = _DictForVDD2VSSHeightandNWPPedge['_EdgeBtwNWandPWForBot1']
                    
                    
                    if k % 2 is 0:
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['_MetalInType'] = 'Metal5'
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['_MetalOutType'] = 'Metal3'
                    else:
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['_MetalInType'] = 'Metal3'
                        _ParallelBufferDesignCalculationParameters[tmpParameter]['_MetalOutType'] = 'Metal5'
                    
                    _ParallelBufferDesignCalculationParameters[tmpParameter]['_Dummy'] = _Dummy
                    
                    
                    self._DesignParameter[BufferNode] = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= BufferNode + 'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[BufferNode]['_DesignObj']._CalculateDesignParameter(**_ParallelBufferDesignCalculationParameters[tmpParameter])
                # if j is 1:
                    # self._DesignParameter[BufferNode]['_Reflect']=(1,0,0)
                    # self._DesignParameter[BufferNode]['_Angle']=180
                
            ###############################################################################################################################            
        
            
            

            if _BufferDistance is None:
                _BufferDistance = 30000
            if _TreeYlocation is None:
                _TreeYlocation = 50000

            # _BufferLenDict
            
            self._DesignParameter['_DelayUnit']['_XYCoordinates'] = [[0,0]]
            
            Ystandard = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1]
            for j in range(0,2):
                Y= "%01d" %(j)

                if j is 0:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferLeftSide
                else:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferRightSide
                for k in range(0,_NumberOfParallelBuffer):
                    ZZ = "%02d" %(k)
                    ZZm1 = "%02d" %(k-1)
                    BufferNode = '_ParallelBufferNode'+ Y + ZZ
                    PiriorNode = '_ParallelBufferNode'+ Y + ZZm1

                    piriorX = 0
                    if k is not 0:
                        piriorX = self._DesignParameter[PiriorNode]['_XYCoordinates'][0][0]

                    if (BufferNode in _BufferLenDict) is True:
                        if _BufferLenDict[BufferNode] is None:
                            _Distance = _BufferDistance
                        else:
                            _Distance = _BufferLenDict[BufferNode]
                    else :
                        _Distance = _BufferDistance


                    if j is 0: #Left Side
                        self._DesignParameter[BufferNode]['_XYCoordinates'] = [[ piriorX - _Distance, Ystandard]]
                    else : #Right Side
                        self._DesignParameter[BufferNode]['_XYCoordinates'] = [[ piriorX + _Distance, Ystandard]]

            if _XbiasForTreeLeft is None:
                _XbiasForTreeLeft = 0
            if _XbiasForTreeRight is None:
                _XbiasForTreeRight = 0

            ZZforL = "%02d"%(_NumberOfParallelBufferLeftSide-1)
            ZZforR = "%02d"%(_NumberOfParallelBufferRightSide-1)
            MLbuffer = '_ParallelBufferNode0' + ZZforL
            MRbuffer = '_ParallelBufferNode1' + ZZforR


            XdistanceLeft =  _XbiasForTreeLeft + self._DesignParameter[MLbuffer]['_XYCoordinates'][0][0]
            XdistanceRight =  _XbiasForTreeRight + self._DesignParameter[MRbuffer]['_XYCoordinates'][0][0]

            Ystandard = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1]
            
            self._DesignParameter['_TreeLeft']['_XYCoordinates'] = [[XdistanceLeft,_TreeYlocation]]
            self._DesignParameter['_TreeRight']['_XYCoordinates'] = [[XdistanceRight,_TreeYlocation]]
            
            
            
            
            
            ################################################BUFFER NODE Connection#########################################################
            
            for j in range(0,2):
                Y= "%01d" %(j)
                Yn = j
                
                if j is 0:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferLeftSide
                else:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferRightSide
                
                for k in range(0,_NumberOfParallelBuffer-1):      ##LEFT SIDE 
                    tmp=[]
                    ZZ = "%02d" %(k)
                    ZZnext = "%02d" %(k+1)
                    ZZn = k
                    BufferNode = '_ParallelBufferNode' + Y + ZZ
                    NextBufferNode = '_ParallelBufferNode' + Y + ZZnext
                    BufferOutputMetal = 'OutputMetalOfBuffer'+ Y + ZZ

                    if ZZn % 2 is 1:
                        self._DesignParameter[BufferOutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                    else:
                        self._DesignParameter[BufferOutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[BufferOutputMetal]['_Width'] = _BufferConnectionMetalWidth

                    if Yn % 2 is 0: #LeftSideDirection
                        for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(LineNum)]['_XYCoordinates'][0]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][-1])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(LineNum)]['_XYCoordinates'][0]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][-1])] ])
                    else:
                        for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(LineNum)]['_XYCoordinates'][-1]) ]
                                        ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][0])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(LineNum)]['_XYCoordinates'][-1]) ]
                                        ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][0])] ])
                    
                    self._DesignParameter[BufferOutputMetal]['_XYCoordinates'] = tmp
            
            
            ################################################BUFFER NODE to DELAY UNIT Connection#########################################################
            for j in range(0,2):
                Y= "%01d" %(j)
                Yn = j
                k = 0
                tmp=[]
                ZZ = "%02d" %(k)
                ZZnext = "%02d" %(k+1)
                ZZn = k
                NextBufferNode = '_ParallelBufferNode' + Y + ZZ
                DelayUnitOutputMetal = 'OutputMetalOfDelayUnit'+ Y

                self._DesignParameter[DelayUnitOutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                self._DesignParameter[DelayUnitOutputMetal]['_Width'] = _BufferConnectionMetalWidth

                if Yn % 2 is 0: #LeftSideDirection
                    for LineNum in range(1,5):
                        tmp.append([ [a+b for a,b in zip(self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_OutputRouting' +str(LineNum) + 'up']['_XYCoordinates'][0][0]) ]
                                    ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][-1])] ])
                        tmp.append([ [a+b for a,b in zip(self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_OutputRouting' +str(5-LineNum) + 'down']['_XYCoordinates'][0][0]) ]
                                    ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][-1])] ])
                else:
                    for LineNum in range(1,5):
                        tmp.append([ [a+b for a,b in zip(self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_OutputRouting' +str(LineNum) + 'up']['_XYCoordinates'][0][1]) ]
                                    ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][0])] ])
                        tmp.append([ [a+b for a,b in zip(self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_OutputRouting' +str(5-LineNum) + 'down']['_XYCoordinates'][0][1]) ]
                                    ,[a+b for a,b in zip(self._DesignParameter[NextBufferNode]['_XYCoordinates'][0],self._DesignParameter[NextBufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][0])] ])

                self._DesignParameter[DelayUnitOutputMetal]['_XYCoordinates'] = tmp
        
            ################################################BUFFER NODE to Tree NODE Connection (VIA)#########################################################
            if _Buffer2TreeMetWidth is None:
                _Buffer2TreeMetWidth = _DRCObj._MetalxMinWidth
            
            for j in range(0,2):
                Y= "%01d" %(j)
                Yn = j
                if j is 0:
                    k = _NumberOfParallelBufferLeftSide - 1
                    Tree = '_TreeLeft'
                else:
                    k = _NumberOfParallelBufferRightSide - 1
                    Tree = '_TreeRight'
                tmp=[]
                ZZ = "%02d" %(k)
                ZZn = k
                
                BufferNode = '_ParallelBufferNode' + Y + ZZ
                
                XlocationOfVIA324and425 = None
                for upsideNum in range(1,6):
                    VIAupsideMet52Met6 = '_ViaMet52Met6OnUpsidefor'+BufferNode + 'n' + str(upsideNum)
                    VIAupsideMet32Met4 = '_ViaMet32Met4OnUpsidefor'+BufferNode + 'n' +str(upsideNum)
                    VIAupsideMet42Met5 = '_ViaMet42Met5OnUpsidefor'+BufferNode + 'n' +str(upsideNum)
                    self._DesignParameter[VIAupsideMet52Met6] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name=VIAupsideMet52Met6+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[VIAupsideMet32Met4] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name=VIAupsideMet32Met4+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[VIAupsideMet42Met5] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name=VIAupsideMet42Met5+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                
                    self._DesignParameter[VIAupsideMet52Met6]['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=2)
                    self._DesignParameter[VIAupsideMet32Met4]['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
                    self._DesignParameter[VIAupsideMet42Met5]['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
                
                    ####self._DesignParameter[VIAupsideMet42Met5]#### Metal4 Area DRC requirement
                    Xwidth = self._DesignParameter[VIAupsideMet42Met5]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
                    Ywidth = self._DesignParameter[VIAupsideMet42Met5]['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                    if Xwidth * Ywidth < _DRCObj._MetalxMinArea:
                        Xwidth = round(_DRCObj._MetalxMinArea/Ywidth/_DRCObj._MinSnapSpacing/2 + 0.5) * _DRCObj._MinSnapSpacing * 2
                        self._DesignParameter[VIAupsideMet42Met5]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = Xwidth
                
                    if upsideNum is 1:
                        TopDownLine = 'Top1'
                    elif upsideNum is 2:
                        TopDownLine = 'Top2'
                    elif upsideNum is 3:
                        TopDownLine = 'Top5'
                    elif upsideNum is 4:
                        TopDownLine = 'Bot4'
                    elif upsideNum is 5:
                        TopDownLine = 'Bot3'
                        
                    

                    tmp = []
                    ViaY = self._DesignParameter[BufferNode]['_XYCoordinates'][0][1] + self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+TopDownLine]['_XYCoordinates'][0][1]
                    for viaNum in range(0,len(self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+TopDownLine]['_XYCoordinates'])):
                        ViaX = self._DesignParameter[Tree]['_XYCoordinates'][0][0] + self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_XYCoordinates'][0][0] \
                               +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+TopDownLine]['_XYCoordinates'][viaNum][0]
                        tmp.append([ViaX,ViaY])
                    
                    if XlocationOfVIA324and425 is None:
                        ViaX2 = self._DesignParameter[BufferNode]['_XYCoordinates'][0][0] + self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+TopDownLine]['_XYCoordinates'][0][0]
                        XlocationOfVIA324and425 = round((ViaX+ViaX2)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                    
                    self._DesignParameter[VIAupsideMet52Met6]['_XYCoordinates'] = tmp
                    self._DesignParameter[VIAupsideMet32Met4]['_XYCoordinates'] = [[XlocationOfVIA324and425 , ViaY]]
                    self._DesignParameter[VIAupsideMet42Met5]['_XYCoordinates'] = self._DesignParameter[VIAupsideMet32Met4]['_XYCoordinates']
                
                for downsideNum in range(1,6):
                    VIAdownsideMet32Met4 = '_ViaMet32Met4OnDownsidefor'+BufferNode + 'n' +str(downsideNum)
                    VIAdownsideMet42Met5 = '_ViaMet42Met5OnDownsidefor'+BufferNode + 'n' +str(downsideNum)
                    self._DesignParameter[VIAdownsideMet32Met4] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name=VIAdownsideMet32Met4+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[VIAdownsideMet42Met5] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name=VIAdownsideMet42Met5+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[VIAdownsideMet32Met4]['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
                    self._DesignParameter[VIAdownsideMet42Met5]['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
                
                    if downsideNum is 1:
                        TopDownLine = 'Top3'
                    elif downsideNum is 2:
                        TopDownLine = 'Top4'
                    elif downsideNum is 3:
                        TopDownLine = 'Bot5'
                    elif downsideNum is 4:
                        TopDownLine = 'Bot2'
                    elif downsideNum is 5:
                        TopDownLine = 'Bot1'
                        
                    tmp = []
                    ViaY = self._DesignParameter[BufferNode]['_XYCoordinates'][0][1] + self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+TopDownLine]['_XYCoordinates'][0][1]
                    for viaNum in range(0,len(self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+TopDownLine]['_XYCoordinates'])):
                        ViaX = self._DesignParameter[Tree]['_XYCoordinates'][0][0] + self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_XYCoordinates'][0][0] \
                               +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+TopDownLine]['_XYCoordinates'][viaNum][0]
                        tmp.append([ViaX,ViaY])
                    
                    
                    self._DesignParameter[VIAdownsideMet32Met4]['_XYCoordinates'] = tmp
                    self._DesignParameter[VIAdownsideMet42Met5]['_XYCoordinates'] = tmp
                    

                

                
                ################################################BUFFER NODE to Tree NODE Connection (Vertical Metal)#########################################################
                for LineNum in range(1,6):
                    
                    VerticalMetalup = '_VerticalMet6ForBuffer2TreeConnectionforUPline'+ZZ+str(LineNum)
                    VerticalMetaldown = '_VerticalMet4ForBuffer2TreeConnectionforDOWNline'+ZZ+str(LineNum)
                    self._DesignParameter[VerticalMetalup] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[VerticalMetaldown] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_Width=400)
                    
                    VIAupsideMet52Met6 = '_ViaMet52Met6OnUpsidefor'+BufferNode + 'n' + str(LineNum)
                    VIAdownsideMet32Met4 = '_ViaMet32Met4OnDownsidefor'+BufferNode + 'n' + str(LineNum)
                    

                    if LineNum is 1:
                        UPviaLine = 'Top1'
                        DOWNviaLine = 'Top3'
                    elif LineNum is 2:
                        UPviaLine = 'Top2'
                        DOWNviaLine = 'Top4'
                    elif LineNum is 3:
                        UPviaLine = 'Top5'
                        DOWNviaLine = 'Bot5'
                    elif LineNum is 4:
                        UPviaLine = 'Bot4'
                        DOWNviaLine = 'Bot2'
                    elif LineNum is 5:
                        UPviaLine = 'Bot3'
                        DOWNviaLine = 'Bot1'
                    
                    YlocationForViaUpMet = self._DesignParameter[Tree]['_XYCoordinates'][0][1] \
                                          +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_XYCoordinates'][0][1]\
                                          +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] \
                                          +(-self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+UPviaLine[-1]]['_XYCoordinates'][0][1])
                    YlocationForViaDownMet = self._DesignParameter[Tree]['_XYCoordinates'][0][1] \
                                              +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_XYCoordinates'][0][1]\
                                              +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] \
                                              +self._DesignParameter[Tree]['_DesignObj']._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+DOWNviaLine[-1]]['_XYCoordinates'][0][1]

                    tmpUP =[]
                    tmpDOWN = []
                    for viaNum in range(0,len(self._DesignParameter[VIAupsideMet52Met6]['_XYCoordinates'])):
                        tmpUP.append([ [self._DesignParameter[VIAupsideMet52Met6]['_XYCoordinates'][viaNum][0],YlocationForViaUpMet]
                                      ,self._DesignParameter[VIAupsideMet52Met6]['_XYCoordinates'][viaNum]  ])
                    for viaNum in range(0,len(self._DesignParameter[VIAdownsideMet32Met4]['_XYCoordinates'])):
                        tmpDOWN.append([ [self._DesignParameter[VIAdownsideMet32Met4]['_XYCoordinates'][viaNum][0],YlocationForViaDownMet]
                                        ,self._DesignParameter[VIAdownsideMet32Met4]['_XYCoordinates'][viaNum]  ])
                    self._DesignParameter[VerticalMetalup]['_XYCoordinates'] = tmpUP
                    self._DesignParameter[VerticalMetaldown]['_XYCoordinates'] = tmpDOWN
                    self._DesignParameter[VerticalMetalup]['_Width'] = _Buffer2TreeMetWidth
                    self._DesignParameter[VerticalMetaldown]['_Width'] = _Buffer2TreeMetWidth
                    

                    

                ################################################BUFFER NODE to Tree NODE Connection (Parallel Metal)#########################################################
                for LineNum in range(1,6):
                    
                    if LineNum is 1:
                        UPviaLine = 'Top1'
                        DOWNviaLine = 'Top3'
                    elif LineNum is 2:
                        UPviaLine = 'Top2'
                        DOWNviaLine = 'Top4'
                    elif LineNum is 3:
                        UPviaLine = 'Top5'
                        DOWNviaLine = 'Bot5'
                    elif LineNum is 4:
                        UPviaLine = 'Bot4'
                        DOWNviaLine = 'Bot2'
                    elif LineNum is 5:
                        UPviaLine = 'Bot3'
                        DOWNviaLine = 'Bot1'
                    
                    ParallelMetal5up = '_ParallelMet5ForBuffer2TreeConnectionforUPline'+ Y +str(LineNum) 
                    ParallelMetaldown = '_ParallelMetForBuffer2TreeConnectionforDOWNline'+ Y +str(LineNum)
                    self._DesignParameter[ParallelMetal5up] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                    
                
                    VIAupside = '_ViaMet52Met6OnUpsidefor'+BufferNode + 'n' + str(LineNum)
                    VIAdownside = '_ViaMet42Met5OnDownsidefor'+BufferNode + 'n' + str(LineNum)
                    
                    VIAupsideforMet3 = '_ViaMet32Met4OnUpsidefor'+BufferNode + 'n' + str(LineNum)
                    VIAupsideforMet4 = '_ViaMet42Met5OnUpsidefor'+BufferNode + 'n' + str(LineNum)
                    VIAdownsideforMet3 = '_ViaMet32Met4OnDownsidefor'+BufferNode + 'n' + str(LineNum)
                    
                    if k % 2 is 1: #outputMetalis Met5
                        self._DesignParameter[ParallelMetaldown] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                        upMetal5XYlocationR = [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+UPviaLine]['_XYCoordinates'][0])]
                        upMetal5XYlocationL = [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+UPviaLine]['_XYCoordinates'][-1])]
                        self._DesignParameter[VIAupsideforMet3]['_Ignore']=True
                        self._DesignParameter[VIAupsideforMet4]['_Ignore']=True
                        self._DesignParameter[VIAdownsideforMet3]['_Ignore']=True
                        
                        
                    else:           #OutputMetal is Met3
                        ParallelMetal3up = '_ParallelMet3ForBuffer2TreeConnectionforUPline'+ Y +str(LineNum)
                        self._DesignParameter[ParallelMetal3up] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                        self._DesignParameter[ParallelMetaldown] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                        self._DesignParameter[ParallelMetal3up]['_Width'] = _BufferConnectionMetalWidth
                        upMetal5XYlocationR = self._DesignParameter[VIAupsideforMet3]['_XYCoordinates'][0]
                        upMetal3XYlocationR = [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+UPviaLine]['_XYCoordinates'][0])]
                        upMetal5XYlocationL = self._DesignParameter[VIAupsideforMet3]['_XYCoordinates'][0]
                        upMetal3XYlocationL = [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+UPviaLine]['_XYCoordinates'][-1])]
                        self._DesignParameter[VIAdownside]['_Ignore'] = True
                    

                    self._DesignParameter[ParallelMetal5up]['_Width'] = _BufferConnectionMetalWidth
                    self._DesignParameter[ParallelMetaldown]['_Width'] = _BufferConnectionMetalWidth
                    
                    if Yn is 0: #LeftSide
                        self._DesignParameter[ParallelMetal5up]['_XYCoordinates'] = [[ upMetal5XYlocationR , self._DesignParameter[VIAupside]['_XYCoordinates'][-1]  ]]
                        self._DesignParameter[ParallelMetaldown]['_XYCoordinates'] = [[ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+DOWNviaLine]['_XYCoordinates'][0])]
                                                                                     ,self._DesignParameter[VIAdownside]['_XYCoordinates'][-1]  ]]
                        if k % 2 is 0:
                            self._DesignParameter[ParallelMetal3up]['_XYCoordinates'] = [[upMetal5XYlocationR ,upMetal3XYlocationR ]]
                    else:       #Right Side
                        self._DesignParameter[ParallelMetal5up]['_XYCoordinates'] = [[ upMetal5XYlocationL , self._DesignParameter[VIAupside]['_XYCoordinates'][0]  ]]
                        self._DesignParameter[ParallelMetaldown]['_XYCoordinates'] = [[ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+DOWNviaLine]['_XYCoordinates'][-1])]
                                                                                     ,self._DesignParameter[VIAdownside]['_XYCoordinates'][0]  ]]
                        if k % 2 is 0:
                            self._DesignParameter[ParallelMetal3up]['_XYCoordinates'] = [[upMetal5XYlocationR ,upMetal3XYlocationR ]]
                    

            # ) ########################### MAKE PIN for VDD and VSS ##############################
            VDDtmp=[]
            VSStmp=[]
            totalNum = 2**(_TreeDesignCalculationParameters['_TotalLevel'])
            for i in range(1,totalNum):
            
                VDDtmp.append([a+b for a,b in zip(self._DesignParameter['_TreeLeft']['_XYCoordinates'][0],self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0])])
                VDDtmp.append([a+b+c for a,b,c in zip(self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],\
                                                      self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0],\
                                                      self._DesignParameter['_TreeLeft']['_XYCoordinates'][0] )])
                VSStmp.append([self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][0]
                              ,self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][1] \
                              +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]\
                              +self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][1] ] )
            for i in range(1,totalNum):
            
                VDDtmp.append([a+b for a,b in zip(self._DesignParameter['_TreeRight']['_XYCoordinates'][0],self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0])])
                VDDtmp.append([a+b+c for a,b,c in zip(self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],\
                                                      self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0],\
                                                      self._DesignParameter['_TreeRight']['_XYCoordinates'][0] )])
                VSStmp.append([self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_TreeRight']['_XYCoordinates'][0][0]
                              ,self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][1] \
                              +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]\
                              +self._DesignParameter['_TreeRight']['_XYCoordinates'][0][1] ] )
            
            
            for j in range(0,_NumberOfParallelBufferLeftSide ):
                ZZ = "%02d" %(j)
                VDDtmp.append(self._DesignParameter['_ParallelBufferNode0'+ZZ]['_XYCoordinates'][0])
                VDDtmp.append([a+b for a,b in zip(self._DesignParameter['_ParallelBufferNode0'+ZZ]['_XYCoordinates'][0],self._DesignParameter['_ParallelBufferNode0'+ZZ]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0] )])
                VSStmp.append([self._DesignParameter['_ParallelBufferNode0'+ZZ]['_XYCoordinates'][0][0]
                              ,self._DesignParameter['_ParallelBufferNode0'+ZZ]['_XYCoordinates'][0][1] + self._DesignParameter['_ParallelBufferNode0'+ZZ]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ] )
            
            
            for j in range(0,_NumberOfParallelBufferRightSide ):
                ZZ = "%02d" %(j)
                VDDtmp.append(self._DesignParameter['_ParallelBufferNode1'+ZZ]['_XYCoordinates'][0])
                VDDtmp.append([a+b for a,b in zip(self._DesignParameter['_ParallelBufferNode1'+ZZ]['_XYCoordinates'][0],self._DesignParameter['_ParallelBufferNode1'+ZZ]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0] )])
                VSStmp.append([self._DesignParameter['_ParallelBufferNode1'+ZZ]['_XYCoordinates'][0][0]
                              ,self._DesignParameter['_ParallelBufferNode1'+ZZ]['_XYCoordinates'][0][1] + self._DesignParameter['_ParallelBufferNode1'+ZZ]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ] )


            VDDtmp.append(self._DesignParameter['_DelayUnit']['_XYCoordinates'][0])
            VDDtmp.append([a+b for a,b in zip(
                self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0]
            )])
            VDDtmp.append([a+b for a,b in zip(
                self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0]
            )])
            VSStmp.append([self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0]
                          ,self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]])
            VSStmp.append([self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0]
                          ,self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1]
                           +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]])




            # for k in range(1,5):
                # self._DesignParameter['_DelayUnit']['_XYCoordinates'] 
                # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit3']['_XYCoordinates']
                # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates']
                # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates']
                
                              
            
            self._DesignParameter['_VDDpin']['_XYCoordinates'] = VSStmp
            self._DesignParameter['_VSSpin']['_XYCoordinates'] = VDDtmp

                
                
                
            ##############Make Pin For Output############
            startIndex = 2**(_TreeDesignCalculationParameters['_TotalLevel']-1)
            tmpUP1 = []
            tmpUP2 = []
            tmpUP3 = []
            tmpUP4 = []
            tmpUP5 = []
            tmpDOWN1 = []
            tmpDOWN2 = []
            tmpDOWN3 = []
            tmpDOWN4 = []
            tmpDOWN5 = []
            for i in range(startIndex,startIndex*2 ):
                # self._DesignParameter['_TreeLeft']['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElemenetTop']['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElemenetTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates']



                tmpUP = [a+b+c for a,b,c in zip( \
                    self._DesignParameter['_TreeLeft']['_XYCoordinates'][0],
                    self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],
                    self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0]
                    )]
                tmpDOWN = [a+b+c for a,b,c in zip( \
                    self._DesignParameter['_TreeLeft']['_XYCoordinates'][0],
                    self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],
                    self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0],
                    )]

                tmpUP1.append(copy.deepcopy(tmpUP))
                tmpUP2.append(copy.deepcopy(tmpUP))
                tmpUP3.append(copy.deepcopy(tmpUP))
                tmpUP4.append(copy.deepcopy(tmpUP))
                tmpUP5.append(copy.deepcopy(tmpUP))
                tmpDOWN1.append(copy.deepcopy(tmpDOWN))
                tmpDOWN2.append(copy.deepcopy(tmpDOWN))
                tmpDOWN3.append(copy.deepcopy(tmpDOWN))
                tmpDOWN4.append(copy.deepcopy(tmpDOWN))
                tmpDOWN5.append(copy.deepcopy(tmpDOWN))
                print(i,startIndex)

                tmpUP1[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]
                tmpUP1[i-startIndex][1] -= self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                tmpUP2[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]
                tmpUP2[i-startIndex][1] -= self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                tmpUP3[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]
                tmpUP3[i-startIndex][1] -= self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1]
                tmpUP4[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]
                tmpUP4[i-startIndex][1] -= self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1]
                tmpUP5[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]
                tmpUP5[i-startIndex][1] -= self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]

                tmpDOWN1[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]
                tmpDOWN1[i-startIndex][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                tmpDOWN2[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]
                tmpDOWN2[i-startIndex][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                tmpDOWN3[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]
                tmpDOWN3[i-startIndex][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1]
                tmpDOWN4[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]
                tmpDOWN4[i-startIndex][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1]
                tmpDOWN5[i-startIndex][0] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]
                tmpDOWN5[i-startIndex][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]

            self._DesignParameter['_OutL1']['_XYCoordinates'] = tmpUP1
            self._DesignParameter['_OutL2']['_XYCoordinates'] = tmpUP2
            self._DesignParameter['_OutL3']['_XYCoordinates'] = tmpUP3
            self._DesignParameter['_OutL4']['_XYCoordinates'] = tmpUP4
            self._DesignParameter['_OutL5']['_XYCoordinates'] = tmpUP5
            self._DesignParameter['_OutL6']['_XYCoordinates'] = tmpDOWN1
            self._DesignParameter['_OutL7']['_XYCoordinates'] = tmpDOWN2
            self._DesignParameter['_OutL8']['_XYCoordinates'] = tmpDOWN3
            self._DesignParameter['_OutL9']['_XYCoordinates'] = tmpDOWN4
            self._DesignParameter['_OutL10']['_XYCoordinates'] = tmpDOWN5

            tmpUP1 = []
            tmpUP2 = []
            tmpUP3 = []
            tmpUP4 = []
            tmpUP5 = []
            tmpDOWN1 = []
            tmpDOWN2 = []
            tmpDOWN3 = []
            tmpDOWN4 = []
            tmpDOWN5 = []
            for i in range(startIndex,startIndex*2 ):
                # self._DesignParameter['_TreeLeft']['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElemenetTop']['_XYCoordinates'][0]
                # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElemenetTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates']

                tmpUP = [a+b+c for a,b,c in zip( \
                    self._DesignParameter['_TreeRight']['_XYCoordinates'][0],
                    self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],
                    self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0]
                    )]
                tmpDOWN = [a+b+c for a,b,c in zip( \
                    self._DesignParameter['_TreeRight']['_XYCoordinates'][0],
                    self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],
                    self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0],
                    )]

                tmpUP1.append(copy.deepcopy(tmpUP))
                tmpUP2.append(copy.deepcopy(tmpUP))
                tmpUP3.append(copy.deepcopy(tmpUP))
                tmpUP4.append(copy.deepcopy(tmpUP))
                tmpUP5.append(copy.deepcopy(tmpUP))
                tmpDOWN1.append(copy.deepcopy(tmpDOWN))
                tmpDOWN2.append(copy.deepcopy(tmpDOWN))
                tmpDOWN3.append(copy.deepcopy(tmpDOWN))
                tmpDOWN4.append(copy.deepcopy(tmpDOWN))
                tmpDOWN5.append(copy.deepcopy(tmpDOWN))


                tmpUP1[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]
                tmpUP1[i-startIndex][1] -= self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                tmpUP2[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]
                tmpUP2[i-startIndex][1] -= self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                tmpUP3[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]
                tmpUP3[i-startIndex][1] -= self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1]
                tmpUP4[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]
                tmpUP4[i-startIndex][1] -= self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1]
                tmpUP5[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]
                tmpUP5[i-startIndex][1] -= self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]

                tmpDOWN1[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]
                tmpDOWN1[i-startIndex][1] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                tmpDOWN2[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]
                tmpDOWN2[i-startIndex][1] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                tmpDOWN3[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]
                tmpDOWN3[i-startIndex][1] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1]
                tmpDOWN4[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]
                tmpDOWN4[i-startIndex][1] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1]
                tmpDOWN5[i-startIndex][0] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]
                tmpDOWN5[i-startIndex][1] += self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]

            self._DesignParameter['_OutR1']['_XYCoordinates'] = tmpUP1
            self._DesignParameter['_OutR2']['_XYCoordinates'] = tmpUP2
            self._DesignParameter['_OutR3']['_XYCoordinates'] = tmpUP3
            self._DesignParameter['_OutR4']['_XYCoordinates'] = tmpUP4
            self._DesignParameter['_OutR5']['_XYCoordinates'] = tmpUP5
            self._DesignParameter['_OutR6']['_XYCoordinates'] = tmpDOWN1
            self._DesignParameter['_OutR7']['_XYCoordinates'] = tmpDOWN2
            self._DesignParameter['_OutR8']['_XYCoordinates'] = tmpDOWN3
            self._DesignParameter['_OutR9']['_XYCoordinates'] = tmpDOWN4
            self._DesignParameter['_OutR10']['_XYCoordinates'] = tmpDOWN5



            ############# Selection Pin #############
            # self._DesignParameter['_DelayUnit']['_XYCoordinates'][0]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_XYCoordinates'][0]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_XYCoordinates'][1] - 75

            for j in range(1,5):
                # Leftsel1 = []
                # Leftsel2 = []
                # Leftsel3 = []
                # Leftsel4 = []

                Leftsel1 =[ a + b + c for a,b,c in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1]
                )]
                Leftsel2 =[ a + b + c for a,b,c in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_DesignObj']._DesignParameter['_SelectionBarRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1]
                )]

                Leftsel3 =[ a + b + c for a,b,c in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_DesignObj']._DesignParameter['_SelectionBarRoutingXORtopRightMet2']['_XYCoordinates'][0][-1]
                )]
                Leftsel4 =[ a + b + c for a,b,c in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(j)]['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_XYCoordinates'][0][-1]
                )]

                tmp1 = []
                tmp1 = [Leftsel1]
                tmp1.append(Leftsel4)
                tmp2 = [Leftsel2]
                tmp2.append(Leftsel3)



                self._DesignParameter['_Sel'+str(j)]['_XYCoordinates']= tmp1
                self._DesignParameter['_Selb'+str(j)]['_XYCoordinates']= tmp2
                self._DesignParameter['_M4Sel'+str(j)]['_XYCoordinates']=tmp2
                self._DesignParameter['_M4Selb'+str(j)]['_XYCoordinates']=tmp1
                # self._DesignParameter['_Sel'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel1))
                # self._DesignParameter['_Sel'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel4))
                # self._DesignParameter['_Selb'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel2))
                # self._DesignParameter['_Selb'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel3))
                # self._DesignParameter['_M4Sel'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel2))
                # self._DesignParameter['_M4Sel'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel3))
                # self._DesignParameter['_M4Selb'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel1))
                # self._DesignParameter['_M4Selb'+str(j)]['_XYCoordinates'].append(copy.deepcopy(Leftsel4))


            ########## CLK Pin ##########
            # self._DesignParameter['_DelayUnit']['_XYCoordinates'][0]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKpin']['_XYCoordinates'][j]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKBarpin']['_XYCoordinates'][j]

            clktmp = []
            clkbartmp = []
            for j in range(0,len(self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKpin']['_XYCoordinates'])):
                clktmp.append([a+b for a,b in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKpin']['_XYCoordinates'][j]
                )])
                clkbartmp.append([a+b for a,b in zip(
                    self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                    self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKBarpin']['_XYCoordinates'][j]
                )])

            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKpin']['_Ignore'] = True
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_CLKBarpin']['_Ignore'] = True
            self._DesignParameter['_M4CLK']['_XYCoordinates'] = clktmp
            self._DesignParameter['_M4CLKbar']['_XYCoordinates'] = clkbartmp

            ####### Input Pin ######
            # self._DesignParameter['_DelayUnit']['_XYCoordinates'][0]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputApin']['_XYCoordinates'][0]
            # self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputBpin']['_XYCoordinates'][0]

            tmp1 = [a+b for a,b in zip(
                self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputApin']['_XYCoordinates'][0]
            )]
            tmp2 = [a+b for a,b in zip(
                self._DesignParameter['_DelayUnit']['_XYCoordinates'][0],
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputBpin']['_XYCoordinates'][0]
            )]

            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputApin']['_Ignore'] = True
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_InputBpin']['_Ignore'] = True
            self._DesignParameter['_Input1pin']['_XYCoordinates'] = [tmp1]
            self._DesignParameter['_Input2pin']['_XYCoordinates'] = [tmp2]

                

            ###### additional Pin for User Preference ######
            totalNum = 2 ** (_TreeDesignCalculationParameters['_TotalLevel'])
            for lr in range(0,len(_DictForNodeOutPin['_LR']) ):
                if _DictForNodeOutPin['_LR'][lr] == 'Left':
                    TreeLR = '_TreeLeft'
                else:
                    TreeLR = '_TreeRight'

                for i in range(1, totalNum):
                    Node = '_Node' + str(i)
                    OnPin = Node + 'OnPin'
                    if (Node in _DictForNodeOutPin) is True:
                        for outputIndex in range(0,len(_DictForNodeOutPin['_Output'])):
                            Pin = OnPin + _DictForNodeOutPin['_Output'][outputIndex]

                            self._DesignParameter[Pin] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT= TreeLR + _DictForNodeOutPin[Node] + _DictForNodeOutPin['_Output'][outputIndex] )
                            tmp = []
                            if _DictForNodeOutPin['_Output'][outputIndex] == 'E0':
                                VIA = 'Top1'
                                UP = True
                                MOS = '1'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'E1':
                                VIA = 'Top2'
                                UP = True
                                MOS = '2'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'E2':
                                VIA = 'Top3'
                                UP = False
                                MOS = '1'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'E3':
                                VIA = 'Top4'
                                UP = False
                                MOS = '2'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'CLK':
                                VIA = 'Top5'
                                UP = True
                                MOS = '5'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'O0':
                                VIA = 'Bot4'
                                UP = True
                                MOS = '4'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'O1':
                                VIA = 'Bot3'
                                UP = True
                                MOS = '3'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'O2':
                                VIA = 'Bot2'
                                UP = False
                                MOS = '4'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'O3':
                                VIA = 'Bot1'
                                UP = False
                                MOS = '3'
                            elif _DictForNodeOutPin['_Output'][outputIndex] == 'CLKb':
                                VIA = 'Bot5'
                                UP = False
                                MOS = '5'


                            tmp.append([a+b+c for a,b,c in zip(
                                self._DesignParameter[TreeLR]['_XYCoordinates'][0],
                                self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_XYCoordinates'][0],
                                self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLine'+VIA]['_XYCoordinates'][0]
                            )])

                            if UP is True:
                                tmp[0][1] = self._DesignParameter[TreeLR]['_XYCoordinates'][0][1] \
                                           +self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_XYCoordinates'][0][1]\
                                           +self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1]\
                                           +(-self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+MOS]['_XYCoordinates'][0][1])
                            else:
                                tmp[0][1] = self._DesignParameter[TreeLR]['_XYCoordinates'][0][1] \
                                           +self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_XYCoordinates'][0][1]\
                                           +self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1]\
                                           +self._DesignParameter[TreeLR]['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+MOS]['_XYCoordinates'][0][1]
                            self._DesignParameter[Pin]['_XYCoordinates'] = tmp
                        
            for i in range(1, totalNum):
                Node = '_Node' + str(i)
                UpPin = Node + 'UpPin'
                if (Node in _DictForNodeOutUpPin) is True:
                    for outputIndex in range(0,len(_DictForNodeOutUpPin['_Output'])):
                        Pin = UpPin + _DictForNodeOutUpPin['_Output'][outputIndex]

                        self._DesignParameter[Pin] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_DictForNodeOutUpPin[Node] +'up'+ _DictForNodeOutUpPin['_Output'][outputIndex] )
                        tmp = []
                        if _DictForNodeOutUpPin['_Output'][outputIndex] == 'E0':
                            VIA = 'Top' + str(i) + 'Line1'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'E1':
                            VIA = 'Top' + str(i) + 'Line2'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'E2':
                            VIA = 'Bot' + str(i) + 'Line1'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'E3':
                            VIA = 'Bot' + str(i) + 'Line2'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'CLK':
                            VIA = 'Top' + str(i) + 'Line5'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'O0':
                            VIA = 'Top' + str(i) + 'Line4'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'O1':
                            VIA = 'Top' + str(i) + 'Line3'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'O2':
                            VIA = 'Bot' + str(i) + 'Line4'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'O3':
                            VIA = 'Bot' + str(i) + 'Line3'
                        elif _DictForNodeOutUpPin['_Output'][outputIndex] == 'CLKb':
                            VIA = 'Bot' + str(i) + 'Line5'


                        tmp.append([a+b for a,b in zip(
                            self._DesignParameter['_TreeLeft']['_XYCoordinates'][0],
                            self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_ViaMet62Met7OnNode'+VIA]['_XYCoordinates'][0]
                        )])
                        self._DesignParameter[Pin]['_XYCoordinates'] = tmp

            for i in range(1, totalNum):
                Node = '_Node' + str(i)
                InPin = Node + 'InPin'
                if (Node in _DictForNodeInPin) is True:
                    for outputIndex in range(0,len(_DictForNodeOutPin['_Output'])):
                        Pin = InPin + _DictForNodeOutPin['_Output'][outputIndex]

                        self._DesignParameter[Pin] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_DictForNodeInPin[Node] +'In'+ _DictForNodeInPin['_Output'][outputIndex] )
                        tmp = []
                        if _DictForNodeInPin['_Output'][outputIndex] == 'E0':
                            VIA = 'Top1'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'E1':
                            VIA = 'Top2'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'E2':
                            VIA = 'Top3'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'E3':
                            VIA = 'Top4'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'CLK':
                            VIA = 'Top5'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'O0':
                            VIA = 'Bot4'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'O1':
                            VIA = 'Bot3'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'O2':
                            VIA = 'Bot2'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'O3':
                            VIA = 'Bot1'
                        elif _DictForNodeInPin['_Output'][outputIndex] == 'CLKb':
                            VIA = 'Bot5'


                        tmp.append([a+b+c for a,b,c in zip(
                            self._DesignParameter['_TreeLeft']['_XYCoordinates'][0],
                            self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[Node]['_XYCoordinates'][0],
                            self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+VIA]['_XYCoordinates'][0]
                        )])
                        self._DesignParameter[Pin]['_XYCoordinates'] = tmp

            # self._DesignParameter['_TreeLeft']['_XYCoordinates'][0]
            # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[Node]['_XYCoordinates'][0]
            # self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[Node]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineTop1']['_XYCoordinates'][0]



            # _Output = [E0,E1,E2,E3,O0,O1,O2,O3,CLK,CLKb]


            # Additional Supply Met1 #

            for i in range(1,1+len(_AdditionalMet1ForSupplydict)):
                MetalName = '_Add'+str(i)+'Metal1'
                XWidth = _AdditionalMet1ForSupplydict['_Add'+str(i)]['Right'] - _AdditionalMet1ForSupplydict['_Add'+str(i)]['Left']
                YWidth = _AdditionalMet1ForSupplydict['_Add'+str(i)]['Top'] - _AdditionalMet1ForSupplydict['_Add'+str(i)]['Bot']
                Xcoordinates = (_AdditionalMet1ForSupplydict['_Add'+str(i)]['Right'] + _AdditionalMet1ForSupplydict['_Add'+str(i)]['Left'])/2
                Ycoordinates = (_AdditionalMet1ForSupplydict['_Add'+str(i)]['Top'] + _AdditionalMet1ForSupplydict['_Add'+str(i)]['Bot'])/2
                self._DesignParameter[MetalName] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                self._DesignParameter[MetalName]['_XYCoordinates'] = [[Xcoordinates,Ycoordinates]]
                self._DesignParameter[MetalName]['_XWidth'] = XWidth
                self._DesignParameter[MetalName]['_YWidth'] = YWidth



            # # BODY Merging OPT
            # _MergingOpt = dict(
            #                     Left1 = ['_Node1','_ParallelBufferNode001'],
            #                  ),
            #
            # for



            ######################################## POWER LINE ################################
            for i in range(1,5):
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit'+str(i)]['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
            
            for i in range(1,6):
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine'+str(i)+'Met1']['_Ignore'] = True
                self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine'+str(i)+'ODLayer']['_Ignore'] = True
            
            for j in range(0,2):
                Y= "%01d" %(j)
                if j is 0:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferLeftSide
                else:
                    _NumberOfParallelBuffer = _NumberOfParallelBufferRightSide
                for k in range(0,_NumberOfParallelBuffer):
                    ZZ = "%02d" %(k)
                    BufferNode = '_ParallelBufferNode'+ Y + ZZ
                    self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                    self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                    self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                    self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                    
            totalNum = 2**(_TreeDesignCalculationParameters['_TotalLevel'])
            for i in range(1,totalNum):
                self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
            
            ##New Power Line ## for Level0
            self._DesignParameter['_PbodyContactLevel0'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='_PbodyContactLevel0In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
            self._DesignParameter['_NbodyContactLevel0'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='_NbodyContactLevel0In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
            self._DesignParameter['_PIMPLevel0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NIMPLevel0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            LeftSide = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0] \
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0]\
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0]\
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                      -self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            RightSide = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0] \
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            _XYforPbody = [[round((LeftSide+RightSide)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                           ,self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][1]]]
            _XYforNbody = copy.deepcopy(_XYforPbody)
            _XYforNbody[0][1] += self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
            _LengthOfOD = RightSide - LeftSide
            _NumberOfBodyCOY = _SupplyCOY['_NumberOfCOYforLevel0']
            _Met1YWidthForSupply = self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _NumberOfBodyCOY==1 \
                        else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))

            self._DesignParameter['_PbodyContactLevel0']['_DesignObj']._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOY =_NumberOfBodyCOY,_NumberOfPbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
            self._DesignParameter['_NbodyContactLevel0']['_DesignObj']._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOY =_NumberOfBodyCOY,_NumberOfNbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
            self._DesignParameter['_PbodyContactLevel0']['_XYCoordinates'] = _XYforPbody
            self._DesignParameter['_NbodyContactLevel0']['_XYCoordinates'] = _XYforNbody
            
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine1PIMP']['_Ignore'] = True
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine2NIMP']['_Ignore'] = True
            
            PIMPleft = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0]\
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0]\
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0]\
                      +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]\
                      -self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            PIMPright = self._DesignParameter['_DelayUnit']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]\
                       +self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            PIMPheight = self._DesignParameter['_PbodyContactLevel0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_PIMPLevel0']['_YWidth'] = PIMPheight
            self._DesignParameter['_PIMPLevel0']['_XWidth'] = PIMPright-PIMPleft
            self._DesignParameter['_PIMPLevel0']['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_PbodyContactLevel0']['_XYCoordinates'][0][1] ]]
            self._DesignParameter['_NIMPLevel0']['_YWidth'] = PIMPheight
            self._DesignParameter['_NIMPLevel0']['_XWidth'] = PIMPright-PIMPleft
            self._DesignParameter['_NIMPLevel0']['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_NbodyContactLevel0']['_XYCoordinates'][0][1] ]]
            
            
            
            ##New Power Line ## for Level1
            self._DesignParameter['_PbodyContactLevel1'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name='_PbodyContactLevel1In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
            self._DesignParameter['_NbodyContactLevel1'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='_NbodyContactLevel1In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
            self._DesignParameter['_PIMPLevel1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NIMPLevel1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            self._DesignParameter['_NwellLevel1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
            LeftBuff = '_ParallelBufferNode0' + "%02d" %(_NumberOfParallelBufferLeftSide-1)
            RightBuff = '_ParallelBufferNode1' + "%02d" %(_NumberOfParallelBufferRightSide-1)
            
            LeftSide = self._DesignParameter[LeftBuff]['_XYCoordinates'][0][0]\
                      +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                      +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                      -self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            RightSide = self._DesignParameter[RightBuff]['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            
            _XYforPbody = [[round((LeftSide+RightSide)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                           ,self._DesignParameter[LeftBuff]['_XYCoordinates'][0][1]]]
            _XYforNbody = copy.deepcopy(_XYforPbody)
            _XYforNbody[0][1] += self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
            _LengthOfOD = RightSide - LeftSide
            _NumberOfBodyCOY = _SupplyCOY['_NumberOfCOYforLevel1']
            _Met1YWidthForSupply = self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _NumberOfBodyCOY==1 \
                        else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))

            self._DesignParameter['_PbodyContactLevel1']['_DesignObj']._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOY =_NumberOfBodyCOY,_NumberOfPbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
            self._DesignParameter['_NbodyContactLevel1']['_DesignObj']._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOY =_NumberOfBodyCOY,_NumberOfNbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
            self._DesignParameter['_PbodyContactLevel1']['_XYCoordinates'] = _XYforPbody
            self._DesignParameter['_NbodyContactLevel1']['_XYCoordinates'] = _XYforNbody
            
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine3PIMP']['_Ignore'] = True
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine5PIMP']['_Ignore'] = True
            self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_PowerLine4NIMP']['_Ignore'] = True
            
            PIMPleft =  self._DesignParameter[LeftBuff]['_XYCoordinates'][0][0]\
                       +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                       +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]\
                       -self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            PIMPright = self._DesignParameter[RightBuff]['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS6']['_XYCoordinates'][0][0]\
                       +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            PIMPheight = self._DesignParameter['_PbodyContactLevel1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_PIMPLevel1']['_YWidth'] = PIMPheight
            self._DesignParameter['_PIMPLevel1']['_XWidth'] = PIMPright-PIMPleft
            self._DesignParameter['_PIMPLevel1']['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_PbodyContactLevel1']['_XYCoordinates'][0][1] ]]
            self._DesignParameter['_NIMPLevel1']['_YWidth'] = PIMPheight
            self._DesignParameter['_NIMPLevel1']['_XWidth'] = PIMPright-PIMPleft
            self._DesignParameter['_NIMPLevel1']['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_NbodyContactLevel1']['_XYCoordinates'][0][1] ]]
            
            NWleft =  self._DesignParameter[LeftBuff]['_XYCoordinates'][0][0]\
                     +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                     +self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0]\
                     -self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            NWright =  self._DesignParameter[RightBuff]['_XYCoordinates'][0][0]\
                     +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                     +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0]\
                     +self._DesignParameter[RightBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            Nwellheight = 2* ( self._DesignParameter[LeftBuff]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] \
                              -_DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_XOREdgeBtwNWandPW'] )
            self._DesignParameter['_NwellLevel1']['_YWidth'] = Nwellheight
            self._DesignParameter['_NwellLevel1']['_XWidth'] = NWright-NWleft
            self._DesignParameter['_NwellLevel1']['_XYCoordinates'] = [[(NWright+NWleft)/2,self._DesignParameter['_NbodyContactLevel1']['_XYCoordinates'][0][1] ]]
            
            
            ##New Power Line ## for Level2
            totalNum = 2**(_TreeDesignCalculationParameters['_TotalLevel'])
            for i in range(0,_TreeDesignCalculationParameters['_TotalLevel']):
                LeftNode = '_Node'+str(2**i)
                RightNode = '_Node'+str(2**(i+1)-1)
                Pbody = '_PbodyContactLevel' + str(i+2)
                Nbody = '_NbodyContactLevel' + str(i+2)
                PIMP = '_PIMPLevel' + str(i+2)
                NIMP = '_NIMPLevel' + str(i+2)
                Nwell = '_NwellLevel' + str(i+2)
                
                self._DesignParameter[Pbody] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name=Pbody+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                self._DesignParameter[Nbody] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name=Nbody+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                self._DesignParameter[PIMP] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                self._DesignParameter[NIMP] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                self._DesignParameter[Nwell] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                
                LeftSide = self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                          -self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                RightSide = self._DesignParameter['_TreeRight']['_XYCoordinates'][0][0]\
                           +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_XYCoordinates'][0][0]\
                           +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                           +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0]\
                           +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                
                _XYforPbody = [[round((LeftSide+RightSide)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                               ,self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_XYCoordinates'][0][1]]]
                _XYforNbody = copy.deepcopy(_XYforPbody)
                _XYforNbody[0][1] += self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
                _LengthOfOD = RightSide - LeftSide
                _NumberOfBodyCOY = _SupplyCOY['_NumberOfCOYforLevel2']
                _Met1YWidthForSupply = self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _NumberOfBodyCOY==1 \
                            else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))

                self._DesignParameter[Pbody]['_DesignObj']._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOY =_NumberOfBodyCOY,_NumberOfPbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
                self._DesignParameter[Nbody]['_DesignObj']._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOY =_NumberOfBodyCOY,_NumberOfNbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
                self._DesignParameter[Pbody]['_XYCoordinates'] = _XYforPbody
                self._DesignParameter[Nbody]['_XYCoordinates'] = _XYforNbody
                
                
                PIMPleft = self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]\
                          -self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
                PIMPright =self._DesignParameter['_TreeRight']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS6']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS6']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
                PIMPheight = self._DesignParameter['_PbodyContactLevel'+str(i+2)]['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
                self._DesignParameter[PIMP]['_YWidth'] = PIMPheight
                self._DesignParameter[PIMP]['_XWidth'] = PIMPright-PIMPleft
                self._DesignParameter[PIMP]['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_PbodyContactLevel'+str(i+2)]['_XYCoordinates'][0][1] ]]
                self._DesignParameter[NIMP]['_YWidth'] = PIMPheight
                self._DesignParameter[NIMP]['_XWidth'] = PIMPright-PIMPleft
                self._DesignParameter[NIMP]['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_NbodyContactLevel'+str(i+2)]['_XYCoordinates'][0][1] ]]

                
                NWleft =  self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0]\
                          -self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
                NWright =  self._DesignParameter['_TreeRight']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0]\
                          +self._DesignParameter['_TreeRight']['_DesignObj']._DesignParameter[RightNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
                Nwellheight = 2* ( self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] \
                                  -_TreeDesignCalculationParameters['_DictForCLKTreeUnitParameters']['_Default']['_EdgeBtwNWandPW'] )
                self._DesignParameter[Nwell]['_YWidth'] = Nwellheight
                self._DesignParameter[Nwell]['_XWidth'] = NWright-NWleft
                self._DesignParameter[Nwell]['_XYCoordinates'] = [[(NWright+NWleft)/2,self._DesignParameter['_NbodyContactLevel'+str(i+2)]['_XYCoordinates'][0][1] ]]
                    
                if i is 1:
                    self._DesignParameter['_PbodyContactLevel2']['_Ignore'] = True
                    self._DesignParameter['_NbodyContactLevel2']['_Ignore'] = True
                    
                if i is (_TreeDesignCalculationParameters['_TotalLevel']-1) :
                    PbodyUp='_PbodyContactLevel' + str(i+3)
                    PIMPUp = '_PIMPLevel' + str(i+3)
                    self._DesignParameter[PbodyUp] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_DesignParameter=None, _Name=PbodyUp+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[PIMPUp] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400)
                    _XYforPbodyUp = [[round((LeftSide+RightSide)/2/_DRCObj._MinSnapSpacing)*_DRCObj._MinSnapSpacing
                                    ,self._DesignParameter['_TreeLeft']['_XYCoordinates'][0][1] + self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_XYCoordinates'][0][1]\
                                    +self._DesignParameter['_TreeLeft']['_DesignObj']._DesignParameter[LeftNode]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1]  ]]
                    self._DesignParameter[PbodyUp]['_DesignObj']._CalculatePbodyContactDesignParameter(_NumberOfPbodyCOY =_NumberOfBodyCOY,_NumberOfPbodyCOX = _NumberOfSupplyCOX+1,_Met1YWidth = _Met1YWidthForSupply )
                    self._DesignParameter[PbodyUp]['_XYCoordinates'] = _XYforPbodyUp
            
                    self._DesignParameter[PIMPUp]['_YWidth'] = PIMPheight
                    self._DesignParameter[PIMPUp]['_XWidth'] = PIMPright-PIMPleft
                    self._DesignParameter[PIMPUp]['_XYCoordinates'] = [[(PIMPright+PIMPleft)/2,self._DesignParameter['_PbodyContactLevel'+str(i+3)]['_XYCoordinates'][0][1] ]]
            
            
            
            
            
            
            
            # )################################ DRC Verification ################################
            
            DRC_PASS=1
            
            ####DEBUG_MODE####
            # self._DesignParameter['_DelayUnit']['_Ignore'] = True
            # self._DesignParameter['_TreeLeft']['_Ignore'] = True
            # self._DesignParameter['_TreeRight']['_Ignore'] = True
            
            if ('_ParallelBufferNode000' in self._DesignParameter) is True or ('_ParallelBufferNode100' in self._DesignParameter) is True:
                if _DelayUnitDesignCalculationParameters['_Outline1Location'] is None:
                        _DelayUnitDesignCalculationParameters['_Outline1Location'] = self._DesignParameter['_ParallelBufferNode000']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot4']['_XYCoordinates'][0][1]
                        DRC_PASS = 0
                if _DelayUnitDesignCalculationParameters['_Outline2Location'] is None:
                        _DelayUnitDesignCalculationParameters['_Outline2Location'] = self._DesignParameter['_ParallelBufferNode000']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot3']['_XYCoordinates'][0][1]
                        DRC_PASS = 0
                if _DelayUnitDesignCalculationParameters['_Outline3Location'] is None:
                        _DelayUnitDesignCalculationParameters['_Outline3Location'] = self._DesignParameter['_ParallelBufferNode000']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot2']['_XYCoordinates'][0][1]
                        DRC_PASS = 0
                if _DelayUnitDesignCalculationParameters['_Outline4Location'] is None:
                        _DelayUnitDesignCalculationParameters['_Outline4Location'] = self._DesignParameter['_ParallelBufferNode000']['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot1']['_XYCoordinates'][0][1]
                        DRC_PASS = 0
                
                BufferHeight = self._DesignParameter['_ParallelBufferNode000']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
                DelayUnitXORHeight = self._DesignParameter['_DelayUnit']['_DesignObj']._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]
                if BufferHeight is not DelayUnitXORHeight:
                    _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorTopDesignCalculatrionParameters']['_XORVdd2VssHeight'] = max(DelayUnitXORHeight,BufferHeight)
                    _DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorBotDesignCalculatrionParameters']['_XORVdd2VssHeight'] = max(DelayUnitXORHeight,BufferHeight)
                    print (_DelayUnitDesignCalculationParameters['_DelayUnitDesignCalculationParameters']['_XorTopDesignCalculatrionParameters']['_XORVdd2VssHeight'])
                    DRC_PASS = 0
            
            
            
            
            
            
            
            
            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  TopView Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        


if __name__=='__main__':


                
    ##############delayUnit #####################################################################
    TopViewObj=_TopView(_DesignParameter=None, _Name='ATopviewDataClk')
    TopViewObj._CalculateDesignParameter(
    
                                         _NumberOfParallelBufferLeftSide = 2,_NumberOfParallelBufferRightSide = 3, _BufferDistance = 30000,
                                         _TreeDesignCalculationParameters = copy.deepcopy(TreeDesign._TreeDesign),
                                        
                                         _Dummy=True)

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
    TopViewObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopViewObj._DesignParameter)
    _fileName='auto_topview.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=TopViewObj._CreateGDSStream(TopViewObj._DesignParameter['_GDSFile']['_GDSFile'])

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






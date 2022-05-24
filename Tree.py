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
import ViaMet62Met7
import ViaPoly2Met1
import ClkTreeElement
import ClkTreeUnit



import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _CLKTree(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
                                        
                                        _DictForUnitXlocation = dict(
                                        #_XlocationOfNode1 = None, ...
                                        #_shiftXforLevelN = None

                                        
                                        
                                        ),
                                     
                                        _DictForPathLength = dict(
                                        #########################################EXAMPLE##############################################
                                        ## Default Length For any Metal Path ##
                                        
                                        # _Default = 1500
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Length For n'th Layout Level's Metal Path ##
                                        
                                        # _DictForLevel{n} = 800
                                        ##############################################################################################
                                        
                                        ),
                                        
                                        
                                        _DictForCLKTreeUnitParameters = dict(
                                        #########################################EXAMPLE##############################################
                                        ## Default Parameter For Any Nodes ##
                                        
                                        # _Default = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Node(s) ##
                                        
                                        # _DictForNode{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Vertical Level  Node(s) ##
                                        
                                        # _DictForVerticalNode{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        
                                        ),
                                       

                                        _ParallelMetalWidth=None,
                                        
                                        _TotalLevel = None, _VerticalLevel = None,

                                        _DictForNodeInformation = dict(
                                            # '_LayoutLevelOfNode1' = None
                                            # '_LevelOfNode1 = None

                                        ),

                                        _DictForBufferInformation = dict(

                                            # '_LevelOfNode1 = None
                                            # '_NumberOfNodeForLevel' = None

                                        ),

                                        _DictForVerticalNodeInformation = dict(
                                        
                                        ),
                                        
                                        _DictForLabel =dict(
                                        # _PinName1 = 'PinTEXT', _Pin1Type = 'METAL1PIN', _Pin1Node = '_Node1'
                                        ),

                                        

                                     _NumberOfParallelViaCOY = None, _VerticalDistance=None, _MOSspacebias = None,
                                     _XbiasforGateViaforVertical = None, _XbiasforGateViaforInverted = None,
                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTree'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(

                                                    # _VDDpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VDD' ),
                                                    # _VSSpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VSS' ),

                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)

    def _CalculateDesignParameter(self,


                                        _DictForUnitXlocation = dict(),
                                     
                                        _DictForPathLength = dict(
                                        #########################################EXAMPLE##############################################
                                        ## Default Length For any Metal Path ##
                                        
                                        # _Default = 1500
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Length For n'th Layout Level's Metal Path ##
                                        
                                        # _DictForLevel{n} = 800
                                        ##############################################################################################
                                        
                                        ),
                                        
                                        
                                        _DictForCLKTreeUnitParameters = dict(
                                        #########################################EXAMPLE##############################################
                                        ## Default Parameter For Any Nodes ##
                                        
                                        # _Default = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Node(s) ##
                                        
                                        # _DictForNode{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        #########################################EXAMPLE##############################################
                                        ## Specific Parameter For n'th Vertical Level  Node(s) ##
                                        
                                        # _DictForVerticalNode{n} = dict(_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                        # _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ##############################################################################################
                                        
                                        
                                        ),
                                       

                                        _ParallelMetalWidth=None,
                                        
                                        _TotalLevel = None, _VerticalLevel = None,

                                        _DictForNodeInformation = dict(
                                            # '_LayoutLevelOfNode1' = None
                                            # '_LevelOfNode1 = None

                                        ),

                                        _DictForBufferInformation = dict(

                                            # '_LevelOfNode1 = None
                                            # '_NumberOfNodeForLevel' = None

                                        ),

                                        _DictForVerticalNodeInformation = dict(
                                        
                                        ),
                                        
                                        _DictForLabel =dict(
                                        # _PinName1 = 'PinTEXT', _Pin1Type = 'METAL1PIN', _Pin1Node = '_Node1'
                                        ),

                                        

                                     _NumberOfParallelViaCOY = None, _VerticalDistance=None, _MOSspacebias = None,
                                     _XbiasforGateViaforVertical = None, _XbiasforGateViaforInverted = None,
                                     _Dummy=None
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  CLK Tree Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')



        _DRCObj=DRC.DRC()
        while True:
            # _Name='ClkTree'
            
            ##############################################################Variable Extraction and Node Unit Generation ################################################################
            if _TotalLevel is None:
                _TotalLevel = 2
            _NumberOfNode = 2**(_TotalLevel) - 1
            
            _BufferLevel = _TotalLevel - 2
            if _BufferLevel < 1:
                _NumberOfBuffer = 0
            else:
                _NumberOfBuffer = 2 * ( 2**(_BufferLevel+1) - 2 - _BufferLevel )
            
            
                        
            if _TotalLevel < 3:
                _DictForBufferInformation['_TotalBufferLevel'] = 0
            else:
                _DictForBufferInformation['_TotalBufferLevel'] =_TotalLevel - 2

            _DictForBufferInformation['_TotalNumber'] = 0
            
            
            i=1
            for i in range(1,_DictForBufferInformation['_TotalBufferLevel']+1):
                
                CurrentLevel = '_NumberOfNodeForLevel' + str(i)
                if (CurrentLevel in _DictForBufferInformation) is False or _DictForBufferInformation[CurrentLevel] is None:
                    _DictForBufferInformation[CurrentLevel] = ( 2**(_DictForBufferInformation['_TotalBufferLevel'] - i + 1) - 1 )
                _DictForBufferInformation['_TotalNumber'] += (2**i) * _DictForBufferInformation[CurrentLevel]
            if _DictForBufferInformation['_NumberOfNodeForLevel1'] is None:
                _DictForBufferInformation['_NumberOfNodeForLevel1'] = 0
            _DictForBufferInformation['_NumberOfNodeForLevel'+str(i+1)] = 0

            

            for i in range(1, _NumberOfNode+1):
                currentNode = i
                TreeUnit = '_Node' + str(currentNode)
                LevelInfo = '_LevelOfNode' + str(currentNode)
                LayoutLevelInfo = '_LayoutLevelOfNode' + str(i)
                

                #######Calculating Current Node's Tree Level##########
                NodeLevel = currentNode
                for j in range(1,1000000):
                    NodeLevel = NodeLevel / 2
                    if NodeLevel is 0:
                        break
                NodeLevel = j
                _DictForNodeInformation[LevelInfo] = NodeLevel
                ######################################################
                
                ###########Calculating Current Node's Layout Level##############
                if currentNode is 1:
                    _DictForNodeInformation[LayoutLevelInfo] = 1
                else :
                    _DictForNodeInformation[LayoutLevelInfo] = _DictForNodeInformation[LevelInfo] - 1
                ################################################################

                
                ################################# Node Parameter Matching ####################################
                Parameter = '_DictForNode' + str(currentNode)
                tmpParameter = 'ClkTreeUnitParameter'
                _DictForCLKTreeUnitParameters[tmpParameter] = dict()
                _DictForCLKTreeUnitParameters[tmpParameter]['_Dummy'] = _Dummy
                
                if (Parameter in _DictForCLKTreeUnitParameters) is False:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters['_Default'])
                else:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters[Parameter])

                if _NumberOfParallelViaCOY is None:
                    _NumberOfParallelViaCOY = 1
                _DictForCLKTreeUnitParameters[tmpParameter]['_NumberOfParallelViaCOY'] = _NumberOfParallelViaCOY
                _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters']['_MOSspacebias'] = _MOSspacebias
                    


                if ('_NumberOfNodeForLevel'+str(NodeLevel) in _DictForBufferInformation) is False:
                    a=1
                elif _DictForBufferInformation['_NumberOfNodeForLevel'+str(_DictForNodeInformation[LayoutLevelInfo])] % 2 is 0:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_MetalInType'] = 'Metal3'
                else:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_MetalInType'] = 'Metal5'
                _DictForCLKTreeUnitParameters[tmpParameter]['_MetalOutType'] = 'Metal3'
                _DictForCLKTreeUnitParameters[tmpParameter]['_TreeLevel'] = _DictForNodeInformation[LevelInfo]
                if currentNode is 1:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForTop'] = 4
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForBot'] = 4
                    _DictForCLKTreeUnitParameters[tmpParameter]['_MetalInType'] = 'Metal4andMetal6'
                    
                else:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForTop'] = 2
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForBot'] = 4
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutLineIgnore'] = True
                
                if (_DictForNodeInformation[LevelInfo] is _TotalLevel) and (currentNode is not 1):
                    _DictForCLKTreeUnitParameters[tmpParameter]['_MetalInType'] = 'Metal3'
                    _DictForCLKTreeUnitParameters[tmpParameter]['_MetalOutType'] = 'Metal2andMetal4'
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForTop'] = 2 
                    _DictForCLKTreeUnitParameters[tmpParameter]['_OutputViaLevelForBot'] = 4
                    
                    
                self._DesignParameter[TreeUnit] = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= TreeUnit + 'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                self._DesignParameter[TreeUnit]['_DesignObj']._CalculateDesignParameter(**_DictForCLKTreeUnitParameters[tmpParameter])

                ###############################################################################################
            
            ###########################################################################################################################################################################
            
            

                
            ################################################BUFFER NODE GENERATION#########################################################
            NodeNum = 1
            for i in range(1,_NumberOfNode): 
                NodeLevel = '_LevelOfNode' + str(i)
                if _DictForNodeInformation[NodeLevel] > _DictForBufferInformation['_TotalBufferLevel']:
                    break
                if _TotalLevel < 3:
                    break
                
                #######################BufferNodeNamingRule#######################
                #BufferXXYZZ :  XX- MotherNode(Standard Node), Y- Left(0) Or Right(1) ZZ- BufferNodeNaming
                XX = "%02d" %(i)
                for j in range(0,2):
                    Y= "%01d" %(j)
                    level = _DictForNodeInformation['_LevelOfNode'+str(i)]
                    UnitNum = _DictForBufferInformation['_NumberOfNodeForLevel'+str(level)] #/ (2**level)
                    # _DictForBufferInformation[Parameter]['_NumberOfParallelViaCOY'] = _NumberOfParallelViaCOY   <<?? What is this?
                    for k in range(0,UnitNum):
                        ZZ = "%02d" %(k)
                        BufferNode = '_BufferNode' + XX + Y + ZZ
                        
                        if i is 1:
                            currentBufferLevel = 1
                        else:
                            currentBufferLevel = _DictForNodeInformation[NodeLevel] + 1
                        
                        
                        tmpBufferParameter = 'ClkTreeUnitParameter'
                        _DictForCLKTreeUnitParameters[tmpBufferParameter] = dict()
                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_Dummy'] = _Dummy
                        
                        Parameter = '_DictForBufferLevel' + str(currentBufferLevel)
                        if (Parameter in _DictForCLKTreeUnitParameters) is False:
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters['_Default'])
                        else:
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters[Parameter])


                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_OutputViaLevelForTop'] = 4
                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_OutputViaLevelForBot'] = 4
                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_OutLineIgnore'] = False
                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_CLKTreeElementParameters']['_MOSspacebias'] = _MOSspacebias
                        if k % 2 is 0:
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_MetalInType'] = 'Metal3'
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_MetalOutType'] = 'Metal5'
                        else:
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_MetalInType'] = 'Metal5'
                            _DictForCLKTreeUnitParameters[tmpBufferParameter]['_MetalOutType'] = 'Metal3'
                        _DictForCLKTreeUnitParameters[tmpBufferParameter]['_TreeLevel'] = 2
                        self._DesignParameter[BufferNode] = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= BufferNode + 'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[BufferNode]['_DesignObj']._CalculateDesignParameter(**_DictForCLKTreeUnitParameters[tmpBufferParameter])
                        _DictForBufferInformation['_NameOfNode'+str(NodeNum)] = BufferNode
                        NodeNum += 1
            ###############################################################################################################################            
        
            

            ################################################Vertical NODE GENERATION#########################################################   
            _DictForVerticalNodeInformation['_NumberOfParallelNode'] = 2**(_TotalLevel-1)
            if _VerticalLevel is None:
                _VerticalLevel = 0
            
            for level in range(0,_VerticalLevel):
                Parameter = '_DictForVerticalNode' + str(level)
                
                tmpVParameter = 'ClkTreeUnitParameter'
                _DictForCLKTreeUnitParameters[tmpVParameter] = dict()
                _DictForCLKTreeUnitParameters[tmpVParameter]['_Dummy'] = _Dummy
                
                if (Parameter in _DictForCLKTreeUnitParameters) is False:
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters['_Default'])
                else:
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters[Parameter])
                    
                for parallel in range(0,_DictForVerticalNodeInformation['_NumberOfParallelNode']):
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_NumberOfParallelViaCOY'] = _NumberOfParallelViaCOY
                    TreeUnit = '_VerticalNodeLevel'+str(level)+'by'+str(parallel)
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_MetalInType'] = 'Metal2andMetal4'
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters']['_ElementType'] = '_Vertical'
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters']['_XbiasforGateVia'] = _XbiasforGateViaforVertical
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_OutputViaLevelForTop'] = 2
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_OutputViaLevelForBot'] = 4
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_OutLineIgnore'] = True
                    _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters']['_MOSspacebias'] = _MOSspacebias
                    if level % 2 is 0: #Swap Input And Output Via Location
                        _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters']['_ElementType'] = '_Inverted'
                        _DictForCLKTreeUnitParameters[tmpVParameter]['_CLKTreeElementParameters']['_XbiasforGateVia'] = _XbiasforGateViaforInverted
                        # _DictForCLKTreeUnitParameters[Parameter]['_MetalInType'] = 'Metal2andMetal4'
                    if level is _VerticalLevel-1 :
                        _DictForCLKTreeUnitParameters[tmpVParameter]['_OutputViaLevelForBot'] = 2
                    
                    self._DesignParameter[TreeUnit] = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= TreeUnit + 'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                    self._DesignParameter[TreeUnit]['_DesignObj']._CalculateDesignParameter(**_DictForCLKTreeUnitParameters[tmpVParameter])
                    
                    
                    # self._DesignParameter[TreeUnit]['_XYCoordinates'] = [ self._DesignParameter['_Node'+str(2**(_TotalLevel-1) + parallel)]['_XYCoordinates'][0] ]
                    # self._DesignParameter[TreeUnit]['_XYCoordinates'][0][1] += (level+1) * 
            ###############################################################################################################################
                
            
            
            # )#####################COORDINATION SETTING#########################
            
            for i in range(1, _NumberOfNode+1):
                currentNode = i
                _CurrentNode = '_Node' + str(currentNode)
                _MotherNode = '_Node' + str( int(currentNode/2))
                _LayoutLevelInfo = '_LayoutLevelOfNode' + str(i)

                Xlocation = '_XlocationOfNode' + str(i)
                
                _PathLength = '_DictForLevel' + str(_DictForNodeInformation[_LayoutLevelInfo])
                if (_PathLength in _DictForPathLength) is False:
                    _DictForPathLength[_PathLength] = _DictForPathLength['_Default']
                   


                Ylocation = (self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] ) * (_DictForNodeInformation[_LayoutLevelInfo] - 1)
                NodeLevel = _DictForNodeInformation['_LevelOfNode'+str(i)]

                Xshift = '_shiftXforLevel' + str(NodeLevel)
                if (Xshift in _DictForUnitXlocation) is True:
                    xshiftVal = _DictForUnitXlocation[Xshift]
                else:
                    xshiftVal = 0

                if (Xlocation in _DictForUnitXlocation) is True:
                    if _DictForUnitXlocation[Xlocation] is None:
                        print ('You Should Put X location Value of Node' + str(i))
                        return 1
                    else:
                        self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ _DictForUnitXlocation[Xlocation] , Ylocation ]]
                else :
                    if currentNode is 1:
                        self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ 0 , Ylocation ]]
                    else :
                        if currentNode % 2 is 1:
                            self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] + _DictForPathLength[_PathLength] * 2**(_TotalLevel - NodeLevel) + xshiftVal, Ylocation ]]
                            # self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] + _DictForPathLength[_PathLength] * ( 1 + _DictForBufferInformation['_NumberOfNodeForLevel'+str(_DictForNodeInformation[_LayoutLevelInfo])]  ), Ylocation ]]
                        else :
                            self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] - _DictForPathLength[_PathLength] * 2**(_TotalLevel - NodeLevel) + xshiftVal, Ylocation ]]
                            # self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] - _DictForPathLength[_PathLength] * ( 1 + _DictForBufferInformation['_NumberOfNodeForLevel'+str(_DictForNodeInformation[_LayoutLevelInfo])]  ), Ylocation ]]
            
            
            
            for i in range(1,_DictForBufferInformation['_TotalNumber']+1):
                #BufferXXYZZ :  XX- MotherNode(Standard Node), Y- Left(0) Or Right(1) ZZ- BufferNodeNaming
                BufferString = _DictForBufferInformation['_NameOfNode'+str(i)][-5:] #[11:16]
                XX = int(BufferString[0:2])
                Y = int(BufferString[2])
                ZZ = int(BufferString[3:5])
                BufferNode = _DictForBufferInformation['_NameOfNode'+str(i)]
                
                MotherNode = '_Node' + str(XX)
                ChildtrenNode = '_Node' + str(XX*2)
                Xlocation = self._DesignParameter[MotherNode]['_XYCoordinates'][0][0]
                Ylocation = self._DesignParameter[ChildtrenNode]['_XYCoordinates'][0][1]
                
                if XX is not 1:
                    _PathLength = '_DictForBuffLevel' + str(_DictForNodeInformation['_LayoutLevelOfNode'+str(XX*2)])
                else :
                    _PathLength = '_DictForBuffLevel1'
                
                if Y is 0:  #Left Side
                    Xlocation -= _DictForPathLength[_PathLength] * (ZZ+1)
                else:       #Right Side
                    Xlocation += _DictForPathLength[_PathLength] * (ZZ+1)
                
                self._DesignParameter[BufferNode]['_XYCoordinates'] = [ [Xlocation,Ylocation] ]
                self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True
                self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_Ignore'] = True
                self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_PbodyContact']['_Ignore'] = True


           

            
            
            
            if _ParallelMetalWidth is None:
                _ParallelMetalWidth = _DRCObj._MetalxMinWidth
            
            
            ########################### Output-Input Metal Connection (For Buffer) ##############################
            for i in range(1,_DictForBufferInformation['_TotalNumber']+1):
                #BufferXXYZZ :  XX- MotherNode(Standard Node), Y- Left(0) Or Right(1) ZZ- BufferNodeNaming
                BufferString = _DictForBufferInformation['_NameOfNode'+str(i)][-5:] #[11:16]
                XX = BufferString[0:2]
                Y = BufferString[2]
                ZZ = BufferString[3:5]
                
                XXn = int(BufferString[0:2])
                Yn = int(BufferString[2])
                ZZn = int(BufferString[3:5])
                
                ZZnew = "%02d"  %(ZZn+1)
                BufferNode = _DictForBufferInformation['_NameOfNode'+str(i)]
                NextBufferNode = '_BufferNode' + XX + Y + ZZnew
                
                MetalName = 'OutputMetalOfBuffer' + XX + Y + ZZ 
                if ZZn % 2 is 0:
                    self._DesignParameter[MetalName] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                else:
                    self._DesignParameter[MetalName] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                self._DesignParameter[MetalName]['_Width'] = _ParallelMetalWidth
                
                if (NextBufferNode in self._DesignParameter) is True:
                        
                    tmp =[]
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
                    
                    
                    
                
                else:
                    # self._DesignParameter[MetalName] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                    # self._DesignParameter[MetalName]['_Width'] = _ParallelMetalWidth
                    
                    tmp = []
                    if Yn % 2 is 0 :    #LeftSideDirection Buffer
                        ChildNode ='_Node' + str(XXn*2)
                        for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(LineNum)]['_XYCoordinates'][0]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[ChildNode]['_XYCoordinates'][0],self._DesignParameter[ChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][-1])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(LineNum)]['_XYCoordinates'][0]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[ChildNode]['_XYCoordinates'][0],self._DesignParameter[ChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][-1])] ])
                    else:
                        ChildNode ='_Node' + str(XXn*2+1)
                        for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(LineNum)]['_XYCoordinates'][-1]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[ChildNode]['_XYCoordinates'][0],self._DesignParameter[ChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][0])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[BufferNode]['_XYCoordinates'][0],self._DesignParameter[BufferNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(LineNum)]['_XYCoordinates'][-1]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[ChildNode]['_XYCoordinates'][0],self._DesignParameter[ChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][0])] ])
                    
                    
                
                self._DesignParameter[MetalName]['_XYCoordinates'] = tmp
                
            
            
            ########################### Output-Input Metal Connection (For Node) ############################## Parallel Metal
            for i in range(1,_NumberOfNode+1):
                print (i)
                if _DictForNodeInformation['_LevelOfNode'+str(i)] is _TotalLevel:
                    break
                MetalName = 'OutputParallelMetalOfNode' + str(i)
                XX = "%02d" %(i)
                YL = "0"
                YR = "1"
                ZZ = "00"
                LeftBuffer = '_BufferNode' + XX + YL + ZZ
                RightBuffer = '_BufferNode' + XX + YR + ZZ
                
                
                
                if (LeftBuffer in self._DesignParameter) is True:
                # if _DictForNodeInformation['_LevelOfNode'+str(i)] < _TotalLevel-1:
                    
                    # XX = "%02d" %(i)
                    # YL = "0"
                    # YR = "1"
                    # ZZ = "00"
                    # LeftBuffer = '_BufferNode' + XX + YL + ZZ
                    # RightBuffer = '_BufferNode' + XX + YR + ZZ
                    
                    self._DesignParameter[MetalName] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[MetalName]['_Width'] = _ParallelMetalWidth
                    tmp = []
                    print (LeftBuffer, RightBuffer)
                    for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[LeftBuffer]['_XYCoordinates'][0],self._DesignParameter[LeftBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][-1]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[RightBuffer]['_XYCoordinates'][0],self._DesignParameter[RightBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][0])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[LeftBuffer]['_XYCoordinates'][0],self._DesignParameter[LeftBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][-1]) ]
                                        ,[a+b for a,b in zip(self._DesignParameter[RightBuffer]['_XYCoordinates'][0],self._DesignParameter[RightBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][0])] ])

                            
                                        
                # elif _DictForNodeInformation['_LevelOfNode'+str(i)] is _TotalLevel-1:
                else:
                    LeftChildNode = '_Node'+str(2*i)
                    RightChildNode = '_Node' + str(2*i+1)
                    self._DesignParameter[MetalName] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[MetalName]['_Width'] = _ParallelMetalWidth
                    tmp = []
                    for LineNum in range(1,6):
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[LeftChildNode]['_XYCoordinates'][0],self._DesignParameter[LeftChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][-1]) ]     
                                        ,[a+b for a,b in zip(self._DesignParameter[RightChildNode]['_XYCoordinates'][0],self._DesignParameter[RightChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineTop'+str(LineNum)]['_XYCoordinates'][0])] ])
                            tmp.append([ [a+b for a,b in zip(self._DesignParameter[LeftChildNode]['_XYCoordinates'][0],self._DesignParameter[LeftChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][-1]) ]
                                        ,[a+b for a,b in zip(self._DesignParameter[RightChildNode]['_XYCoordinates'][0],self._DesignParameter[RightChildNode]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLineBot'+str(LineNum)]['_XYCoordinates'][0])] ])

                # else :
                    # break
                    
                self._DesignParameter[MetalName]['_XYCoordinates'] = tmp
                
                
                
            ########################### Output-Input Metal Connection (From Lower Level Node to Upper Level Buffer) ############################## (Vertical Metal) and VIA
            for i in range(2,_NumberOfNode+1):
                for MOSnum in range(1,6):
                    # VIA
                    # VIAdown
                    Met22Met3ViaTOP = '_ViaMet22Met3OnNode'+str(i)+'Line' + str(MOSnum)
                    Met32Met4ViaBOT = '_ViaMet32Met4OnNode'+str(i)+'Line' + str(MOSnum)
                    
                    #VIA for Every Output Connection
                    Met32Met4ViaTOP = '_ViaMet32Met4OnNodeTop'+str(i)+'Line' + str(MOSnum)
                    Met42Met5ViaTOP = '_ViaMet42Met5OnNodeTop'+str(i)+'Line' + str(MOSnum)
                    Met52Met6ViaTOP = '_ViaMet52Met6OnNodeTop'+str(i)+'Line' + str(MOSnum)
                    Met62Met7ViaTOP = '_ViaMet62Met7OnNodeTop'+str(i)+'Line' + str(MOSnum)
                    
                    Met42Met5ViaBOT = '_ViaMet42Met5OnNodeBot'+str(i)+'Line' + str(MOSnum)
                    Met52Met6ViaBOT = '_ViaMet52Met6OnNodeBot'+str(i)+'Line' + str(MOSnum)
                    Met62Met7ViaBOT = '_ViaMet62Met7OnNodeBot'+str(i)+'Line' + str(MOSnum)
                    
                    
                    
                    
                    XX = "%02d" %(i)
                    YL = "0"
                    YR = "1"
                    ZZ = "00"
                    LeftUnit = '_BufferNode' + XX + YL + ZZ

                    if (LeftUnit in self._DesignParameter) is False:
                        LeftUnit = '_Node'+str(2*i)
                    if _DictForNodeInformation['_LevelOfNode'+str(i)] is _TotalLevel:
                        break
                    
                    
                    
                    tmp2 =[]
                    tmp4 =[]
                    for j in range(0,len(self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates']) ):
                        # Xlocation = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                   # +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][0] \
                                   # -self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 \
                                   # +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Vertical'+str(MOSnum)]['_Width']/2
                        Xlocation = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                   +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][0] \
                                   # -self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 \
                                   # +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Vertical'+str(MOSnum)]['_Width']/2
                                   

                        if MOSnum is 1:
                            UPviaLine = 'Top1'
                            DOWNviaLine = 'Top3'
                        elif MOSnum is 2:
                            UPviaLine = 'Top2'
                            DOWNviaLine = 'Top4'
                        elif MOSnum is 3:
                            UPviaLine = 'Bot3'
                            DOWNviaLine = 'Bot1'
                        elif MOSnum is 4:
                            UPviaLine = 'Bot4'
                            DOWNviaLine = 'Bot2'
                        elif MOSnum is 5:
                            UPviaLine = 'Top5'
                            DOWNviaLine = 'Bot5'
                            
                        YlocationForViaBot = self._DesignParameter[LeftUnit]['_XYCoordinates'][0][1]+self._DesignParameter[LeftUnit]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+DOWNviaLine]['_XYCoordinates'][0][1]
                        YlocationForViaTop = self._DesignParameter[LeftUnit]['_XYCoordinates'][0][1]+self._DesignParameter[LeftUnit]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+UPviaLine]['_XYCoordinates'][0][1]
                        
                        
                        
                        self._DesignParameter[Met22Met3ViaTOP] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name=Met22Met3ViaTOP+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met32Met4ViaBOT] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name=Met32Met4ViaBOT+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        
                        self._DesignParameter[Met32Met4ViaTOP] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name=Met32Met4ViaTOP+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met42Met5ViaTOP] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name=Met42Met5ViaTOP+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met52Met6ViaTOP] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name=Met52Met6ViaTOP+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met62Met7ViaTOP] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name=Met62Met7ViaTOP+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        
                        self._DesignParameter[Met42Met5ViaBOT] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name=Met42Met5ViaBOT+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met52Met6ViaBOT] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name=Met52Met6ViaBOT+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        self._DesignParameter[Met62Met7ViaBOT] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name=Met62Met7ViaBOT+'In{}'.format(self._DesignParameter['_Name']['_Name'])))[0]
                        
                        
                        
                        
                        self._DesignParameter[Met22Met3ViaTOP]['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met32Met4ViaBOT]['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
                        
                        self._DesignParameter[Met32Met4ViaTOP]['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met42Met5ViaTOP]['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met52Met6ViaTOP]['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met62Met7ViaTOP]['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
                        
                        self._DesignParameter[Met42Met5ViaBOT]['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met52Met6ViaBOT]['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=2, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
                        self._DesignParameter[Met62Met7ViaBOT]['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
                        
                        
                        
                        tmp2.append([Xlocation,YlocationForViaTop])
                        tmp4.append([Xlocation,YlocationForViaBot])
                            
                    self._DesignParameter[Met22Met3ViaTOP]['_XYCoordinates'] = tmp2
                    self._DesignParameter[Met32Met4ViaBOT]['_XYCoordinates'] = tmp4
                        
                    self._DesignParameter[Met32Met4ViaTOP]['_XYCoordinates'] = self._DesignParameter[Met22Met3ViaTOP]['_XYCoordinates']
                    self._DesignParameter[Met42Met5ViaTOP]['_XYCoordinates'] = self._DesignParameter[Met22Met3ViaTOP]['_XYCoordinates']
                    self._DesignParameter[Met52Met6ViaTOP]['_XYCoordinates'] = self._DesignParameter[Met22Met3ViaTOP]['_XYCoordinates']
                    self._DesignParameter[Met62Met7ViaTOP]['_XYCoordinates'] = self._DesignParameter[Met22Met3ViaTOP]['_XYCoordinates']
                    
                    self._DesignParameter[Met42Met5ViaBOT]['_XYCoordinates'] = self._DesignParameter[Met32Met4ViaBOT]['_XYCoordinates']
                    self._DesignParameter[Met52Met6ViaBOT]['_XYCoordinates'] = self._DesignParameter[Met32Met4ViaBOT]['_XYCoordinates']
                    self._DesignParameter[Met62Met7ViaBOT]['_XYCoordinates'] = self._DesignParameter[Met32Met4ViaBOT]['_XYCoordinates']
                    
                    
            
            for i in range(2,_NumberOfNode+1):   
                Metal2Name = 'OutputVerticalMetal2OfNode' + str(i)
                Metal4Name = 'OutputVerticalMetal4OfNode' + str(i)
                if _DictForNodeInformation['_LevelOfNode'+str(i)] < _TotalLevel:
                    
                    XX = "%02d" %(i)
                    YL = "0"
                    YR = "1"
                    ZZ = "00"
                    LeftBuffer = '_BufferNode' + XX + YL + ZZ
                    # if _DictForNodeInformation['_LevelOfNode'+str(i)] is _TotalLevel-1:
                        # LeftBuffer = '_Node'+str(2*i)
                    if (LeftBuffer in self._DesignParameter) is False:
                        LeftBuffer = '_Node'+str(2*i)
                    if _DictForNodeInformation['_LevelOfNode'+str(i)] is _TotalLevel:
                        break    
                        
                        
                    
                    self._DesignParameter[Metal2Name] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[Metal2Name]['_Width'] = _ParallelMetalWidth
                    self._DesignParameter[Metal4Name] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_Width=400)
                    self._DesignParameter[Metal4Name]['_Width'] = _ParallelMetalWidth
                    tmp2 = []
                    tmp4 = []
                    for MOSnum in range(1,6):
                        
                        if MOSnum is 1:
                            UPviaLine = 'Top1'
                            DOWNviaLine = 'Top3'
                        elif MOSnum is 2:
                            UPviaLine = 'Top2'
                            DOWNviaLine = 'Top4'
                        elif MOSnum is 3:
                            UPviaLine = 'Bot3'
                            DOWNviaLine = 'Bot1'
                        elif MOSnum is 4:
                            UPviaLine = 'Bot4'
                            DOWNviaLine = 'Bot2'
                        elif MOSnum is 5:
                            UPviaLine = 'Top5'
                            DOWNviaLine = 'Bot5'
                        
                        for j in range(0,len(self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates']) ):
                            Xlocation = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                       +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][0] \
                                       -self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 \
                                       +self._DesignParameter[Metal2Name]['_Width']/2
                            # Xlocation = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] + self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                       # +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][0] \
                                       # -self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 \
                                       # +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Vertical'+str(MOSnum)]['_Width']/2

                            
                            YlocationForMet2 = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][1] \
                                              +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1]\
                                              +(-self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][1])
                            
                            YlocationForMet4 = self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][1] \
                                              +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1]\
                                              +self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(MOSnum)]['_XYCoordinates'][j][1]
                            
                            
                            tmp2.append([ [Xlocation,YlocationForMet2]     
                                         ,[Xlocation,self._DesignParameter[LeftBuffer]['_XYCoordinates'][0][1]+self._DesignParameter[LeftBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+UPviaLine]['_XYCoordinates'][0][1] ] ])
                            tmp4.append([ [Xlocation,YlocationForMet4]     
                                         ,[Xlocation,self._DesignParameter[LeftBuffer]['_XYCoordinates'][0][1]+self._DesignParameter[LeftBuffer]['_DesignObj']._DesignParameter['_ViaMet32Met4OnInLine'+DOWNviaLine]['_XYCoordinates'][0][1] ] ])
                    self._DesignParameter[Metal2Name]['_XYCoordinates'] = tmp2    
                    self._DesignParameter[Metal4Name]['_XYCoordinates'] = tmp4    
                        
                else :
                    break
                    
            

            ########################### Vertical Node Coordination ##############################
            for level in range(0,_VerticalLevel):
                for parallel in range(0,_DictForVerticalNodeInformation['_NumberOfParallelNode']):
                    TreeUnit = '_VerticalNodeLevel'+str(level)+'by'+str(parallel)
                    
                    if _VerticalDistance is None:
                        _VerticalDistance = (self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] )
                    
                    self._DesignParameter[TreeUnit]['_XYCoordinates'] = [ copy.deepcopy(self._DesignParameter['_Node'+str(2**(_TotalLevel-1) + parallel)]['_XYCoordinates'][0]) ]
                    self._DesignParameter[TreeUnit]['_XYCoordinates'][0][1] += (level+1) * _VerticalDistance
                    
            ########################### Vertical Node Connection ##############################
            for level in range(0,_VerticalLevel):
                for parallel in range(0,_DictForVerticalNodeInformation['_NumberOfParallelNode']):
                    TreeUnit = '_VerticalNodeLevel'+str(level)+'by'+str(parallel)
                    BelowUnit = '_VerticalNodeLevel'+str(level-1)+'by'+str(parallel)
                    if level is 0:
                        BelowUnit = '_Node' + str(2**(_TotalLevel-1) + parallel)
                    
                    Metal2 = '_VerticalConnectionMetal2On' + TreeUnit
                    Metal4 = '_VerticalConnectionMetal4On' + TreeUnit
                    
                    self._DesignParameter[Metal2] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 )
                    self._DesignParameter[Metal4] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )
                    
                    self._DesignParameter[Metal2]['_Width'] = _DRCObj._MetalxMinWidth
                    self._DesignParameter[Metal4]['_Width'] = _DRCObj._MetalxMinWidth
                    
                    tmp2 = []
                    tmp4 = []
                    for i in range(1,6):
                        for j in range(0,len(self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'])):
                            if level % 2 is 0:
                                standardX2 = self._DesignParameter[TreeUnit]['_XYCoordinates'][0][0] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] \
                                            -self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                            +self._DesignParameter[Metal2]['_Width']/2
                                standardX4 = self._DesignParameter[TreeUnit]['_XYCoordinates'][0][0] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] \
                                            -self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                            +self._DesignParameter[Metal4]['_Width']/2
                            else :
                                standardX2 = self._DesignParameter[TreeUnit]['_XYCoordinates'][0][0] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                            -self._DesignParameter[Metal2]['_Width']/2
                                standardX4 = self._DesignParameter[TreeUnit]['_XYCoordinates'][0][0] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] \
                                            +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 \
                                            -self._DesignParameter[Metal4]['_Width']/2
                            
                            tmp2.append([ [standardX2
                                         ,self._DesignParameter[TreeUnit]['_XYCoordinates'][0][1] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] \
                                         +self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][0][1] ]
                                        ,[standardX2
                                         ,self._DesignParameter[BelowUnit]['_XYCoordinates'][0][1] + self._DesignParameter[BelowUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] \
                                         +(-self._DesignParameter[BelowUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][0][1]) ]       ])
                            tmp4.append([ [standardX4
                                         ,self._DesignParameter[TreeUnit]['_XYCoordinates'][0][1] + self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] \
                                         +(-self._DesignParameter[TreeUnit]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][0][1]) ]
                                        ,[standardX4
                                         ,self._DesignParameter[BelowUnit]['_XYCoordinates'][0][1] + self._DesignParameter[BelowUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] \
                                         +self._DesignParameter[BelowUnit]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][0][1] ]       ])
                    
                    self._DesignParameter[Metal2]['_XYCoordinates'] = tmp2
                    self._DesignParameter[Metal4]['_XYCoordinates'] = tmp4
        


            ########################### Horizontal All Tree Node Connection ##############################
            for level in range(1,_TotalLevel-1):
                LeftIndex = pow(2,level)
                RightIndex = pow(2,level+1) - 1
                NodeLeft = '_Node' + str(LeftIndex)
                NodeRight = '_Node' + str(RightIndex)
                
                NodeOutputParallelConnectionMetal7 = NodeLeft + 'to' + NodeRight + 'parallelConnectionMet7'
                self._DesignParameter[NodeOutputParallelConnectionMetal7] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0],_Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100 )
                
                tmp = []
                for MOSnum in range(1,6):
                    TopViaLeft = '_ViaMet62Met7OnNodeTop'+str(LeftIndex)+'Line' + str(MOSnum)
                    TopViaRight = '_ViaMet62Met7OnNodeTop'+str(RightIndex)+'Line' + str(MOSnum)
                    BotViaLeft = '_ViaMet62Met7OnNodeBot'+str(LeftIndex)+'Line' + str(MOSnum)
                    BotViaRight = '_ViaMet62Met7OnNodeBot'+str(RightIndex)+'Line' + str(MOSnum)
                    tmp.append([ self._DesignParameter[TopViaLeft]['_XYCoordinates'][-1], self._DesignParameter[TopViaRight]['_XYCoordinates'][0]])
                    tmp.append([ self._DesignParameter[BotViaLeft]['_XYCoordinates'][-1], self._DesignParameter[BotViaRight]['_XYCoordinates'][0]])
                self._DesignParameter[NodeOutputParallelConnectionMetal7]['_XYCoordinates'] = tmp
                self._DesignParameter[NodeOutputParallelConnectionMetal7]['_Width'] = _DRCObj._MetalxMinWidth
                


            
            
            
            
            
            
            #################################################Additional Metal For Vertical Metal & OutputVia (MET4)###########################################
            #################################later pondering####################################
            # for gate in range(1,6):
                # gateViaXY = [ a+b+c for a,b,c in zip(self._DesignParameter[NODE]['_XYCoordinates']\
                                                    # ,self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates']\
                                                    # ,self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(gate)]['_XYCoordinates']) ]
                # viaLeft = gateViaXY[0][0] - self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(gate)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2
                # viaRight = gateViaXY[0][0] + self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(gate)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2
                # viaUp =  gateViaXY[0][1] + self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(gate)]['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2
                # viaUp =  gateViaXY[0][1] - self._DesignParameter[NODE]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(gate)]['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2
            
            
            
            
            
            
            
            
            




            
            
            # ) ############################## Put A Pin #######################################
            for i in range(1,100):
                if ('_PinName'+str(i) in _DictForLabel) is False:
                    break
                if ('_Pin'+str(i)+'Type' in _DictForLabel) is False:
                    break
                if ('_Pin'+str(i)+'Node' in _DictForLabel) is False:
                    _DictForLabel['_Pin'+str(i)+'Node'] = '_Node'+str(_TotalNumber)
                _Node = _DictForLabel['_Pin'+str(i)+'Node']
                if (_Node in self._DesignParameter) is False:
                    break
                    
                _Name = _DictForLabel['_PinName'+str(i)]
                    
                self._DesignParameter[_Name+'_ForEvenOutput1on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForEvenOutput1On'+_Node )
                self._DesignParameter[_Name+'_ForEvenOutput1on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Horizontal1']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]) ]]
                    
                self._DesignParameter[_Name+'_ForEvenOutput2on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForEvenOutput2On'+_Node )
                self._DesignParameter[_Name+'_ForEvenOutput2on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Horizontal2']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]) ]]
                    
                self._DesignParameter[_Name+'_ForEvenOutput3on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForEvenOutput3On'+_Node )
                self._DesignParameter[_Name+'_ForEvenOutput3on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet2Horizontal1']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1] ]]
                    
                self._DesignParameter[_Name+'_ForEvenOutput4on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForEvenOutput4On'+_Node )
                self._DesignParameter[_Name+'_ForEvenOutput4on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet2Horizontal2']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1] ]]
                
                self._DesignParameter[_Name+'_ForCLKon'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForCLKOn'+_Node )
                self._DesignParameter[_Name+'_ForEvenOutput1on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Horizontal1']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]) ]]
                                   
                
                self._DesignParameter[_Name+'_ForOddOutput1on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForOddOutput1On'+_Node )
                self._DesignParameter[_Name+'_ForOddOutput1on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Horizontal1']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1]) ]]
                    
                self._DesignParameter[_Name+'_ForOddOutput2on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForOddOutput2On'+_Node )
                self._DesignParameter[_Name+'_ForOddOutput2on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_OutputMet2Horizontal2']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1]) ]]
                    
                self._DesignParameter[_Name+'_ForOddOutput3on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForOddOutput3On'+_Node )
                self._DesignParameter[_Name+'_ForOddOutput3on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet2Horizontal1']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput4']['_XYCoordinates'][0][1] ]]
                    
                self._DesignParameter[_Name+'_ForOddOutput4on'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForOddOutput4On'+_Node )
                self._DesignParameter[_Name+'_ForOddOutput4on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet2Horizontal2']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput3']['_XYCoordinates'][0][1] ]]
                    
                self._DesignParameter[_Name+'_ForCLKBaron'+_Node] \
                = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][0],_Datatype=DesignParameters._LayerMapping[_DictForLabel['_Pin'+str(i)+'Type']][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT=_Name+'_ForCLKBarOn'+_Node )
                self._DesignParameter[_Name+'_ForOddOutput4on'+_Node]['_XYCoordinates']=\
                [[ self._DesignParameter[_Node]['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][0]\
                   -self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet2Horizontal2']['_Width']/2
                 ,self._DesignParameter[_Node]['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter[_Node]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1] ]]
                    
                
            # # # # # # # # # # VDDtmp=[]
            # # # # # # # # # # VSStmp=[]
            # # # # # # # # # # for i in range(1,_NumberOfNode+1):
                # # # # # # # # # # VDDtmp.append(self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0])
                # # # # # # # # # # VDDtmp.append([a+b for a,b in zip(self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0],self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0])])
                # # # # # # # # # # VSStmp.append([self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][0] ,self._DesignParameter['_Node'+str(i)]['_XYCoordinates'][0][1] + self._DesignParameter['_Node'+str(i)]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]] )
                
            # # # # # # # # # # for i in range(1,_DictForBufferInformation['_TotalNumber']+1):
                # # # # # # # # # # VDDtmp.append(self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_XYCoordinates'][0])
                # # # # # # # # # # VDDtmp.append([a+b for a,b in zip(self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_XYCoordinates'][0],self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0])])
                # # # # # # # # # # VSStmp.append([self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_XYCoordinates'][0][0] ,self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_XYCoordinates'][0][1] + self._DesignParameter[_DictForBufferInformation['_NameOfNode'+str(i)]]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]] )
                
            # # # # # # # # # # self._DesignParameter['_VDDpin']['_XYCoordinates'] = VSStmp
            # # # # # # # # # # self._DesignParameter['_VSSpin']['_XYCoordinates'] = VDDtmp
            
            # )################################ DRC Verification ################################
            
            DRC_PASS=1
            
            # # VIA for GATE X location adjusting 
            # viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0]
            # leftIndex = 0
            # RightIndex = 0
            # for i in range(0, len(self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates']) ):
                # if (self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][-i][0][0] < viaXlocation):
                    # leftIndex = -i
                # if (self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][i][0][0] > viaXlocation):
                    # RightIndex = i

            # leftSpace = viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][leftIndex][0][0] - self._DesignParameter['_OutputMet2Vertical1']['_Width']/2
            # if (leftSpace < _DRCObj._MetalxMinSpace) and (leftIndex is not 0):
                # _XbiasforGateVia += round((_DRCObj._MetalxMinSpace - leftSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                # DRC_PASS = 0

            # viaXlocation = self._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][0] + _XbiasforGateVia
            # rightSpace = - viaXlocation - self._DesignParameter['_ViaMet12Met2OnGate1']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 + self._DesignParameter['_OutputMet2Vertical1']['_XYCoordinates'][RightIndex][0][0] - self._DesignParameter['_OutputMet2Vertical1']['_Width']/2
            # if rightSpace < _DRCObj._MetalxMinSpace:
                # _XbiasforGateVia -= round((_DRCObj._MetalxMinSpace - rightSpace)/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
                # DRC_PASS = 0

            self._DesignParameter['_TmpMet4ForLVS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )
            self._DesignParameter['_TmpMet6ForLVS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100 )
            self._DesignParameter['_TmpMet4ForLVS']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_TmpMet6ForLVS']['_Width'] = _DRCObj._MetalxMinWidth
            tmp1=[]
            tmp2=[]
            for i in range(1,6):
                for j in range(0,len(self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'])):
                    tmp1.append([ [self._DesignParameter['_Node1']['_XYCoordinates'][0][0]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0]
                                                                                   ,self._DesignParameter['_Node1']['_XYCoordinates'][0][1]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][1])  ] 
                                                                                  ,[self._DesignParameter['_Node1']['_XYCoordinates'][0][0]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] 
                                                                                  , -1000] ])
                    tmp2.append([ [self._DesignParameter['_Node1']['_XYCoordinates'][0][0]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0]
                                                                                   ,self._DesignParameter['_Node1']['_XYCoordinates'][0][1]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'][0][1]  ] 
                                                                                  ,[self._DesignParameter['_Node1']['_XYCoordinates'][0][0]+self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate'+str(i)]['_XYCoordinates'][j][0] 
                                                                                  , -1000] ])
            self._DesignParameter['_TmpMet6ForLVS']['_XYCoordinates']=tmp1
            self._DesignParameter['_TmpMet4ForLVS']['_XYCoordinates']=tmp2
            self._DesignParameter['_TmpMet6ForLVS']['_Ignore']=True
            self._DesignParameter['_TmpMet4ForLVS']['_Ignore']=True


            
            
            
            #####VerticalNode Met3Via and OutputMet3 distance DRC
            if _MOSspacebias is None:
                _MOSspacebias = 0
            
            if ('_VerticalNodeLevel0by0' in self._DesignParameter) is True:
                Xlocation1 = self._DesignParameter['_VerticalNodeLevel0by0']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet32Met4OnGate1']['_XYCoordinates'][0][0] \
                            +self._DesignParameter['_VerticalNodeLevel0by0']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet32Met4OnGate1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2
                Xlocation2 = self._DesignParameter['_VerticalNodeLevel0by0']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet3Vertical2']['_XYCoordinates'][-1][0][0] \
                            -self._DesignParameter['_VerticalNodeLevel0by0']['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_OutputMet3Vertical2']['_Width']/2
                if Xlocation2 - Xlocation1 < _DRCObj._MetalxMinSpace:
                    _MOSspacebias += round((_DRCObj._MetalxMinSpace-Xlocation2+Xlocation1)/_DRCObj._MinSnapSpacing + 0.5) * _DRCObj._MinSnapSpacing
                    DRC_PASS = 0
            
            
            
            
            

            
            
            
            
            
            
            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ClkTree Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        


if __name__=='__main__':


                
    ##############delayUnit #####################################################################
    CLKTreeObj=_CLKTree(_DesignParameter=None, _Name='CLKTree')
    CLKTreeObj._CalculateDesignParameter(
    

                                        _DictForCLKTreeUnitParameters = dict(
                                            #This is for Unit Parameter, not for Element Parameter
                                            _Default = dict(
                                                _NumberOfGate=13, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2, _NumberOfGateViaCOY=2,  #_NumberOfParallelViaCOY= 2, 
                                                _PMOSOutputMetalWidth=600, _NMOSOutputMetalWidth=250,
                                                _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 300, _ParallelMetalWidth= 200,_Dummy = False
                                            )
                                            # _DictForNode1 = dict()
                                            # _DictForBufferLevel1 = dict()
                                            # _DictForVerticalNodeLevel1 = dict()

                                        ),
                                        _TotalLevel = 2,  _VerticalLevel=3,
                                        _DictForPathLength = dict(
                                        #########################################EXAMPLE##############################################
                                        ## Default Length For any Metal Path ##
                                        
                                        _Default = 22000,
                                        ##############################################################################################

                                        #########################################EXAMPLE##############################################
                                        ## Specific Length For n'th Layout Level's Metal Path ##
                                        # _DictForLevel1 = 30000,
                                        # _DictForLevel2 = 20000
                                        # _DictForLevel{n} = 800
                                        ##############################################################################################
                                        
                                        ),
                                        
                                         _DictForLabel =dict(
                                        # _PinName1 = 'TESTpin', _Pin1Type = 'METAL2PIN', _Pin1Node = '_Node4'
                                         ),

                                         _DictForBufferInformation = dict(
                                            # _NumberOfNodeForLevel1 = None,
                                            # _NumberOfodeForLevel2 = 1
                                        ),
                                         _ParallelMetalWidth= 200, _NumberOfParallelViaCOY = 2, _VerticalDistance=None,
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
    CLKTreeObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=CLKTreeObj._DesignParameter)
    _fileName='autoClkTree.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=CLKTreeObj._CreateGDSStream(CLKTreeObj._DesignParameter['_GDSFile']['_GDSFile'])

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






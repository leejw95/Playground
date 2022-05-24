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
    

                                     
                                        _DefaultXspace = None,
                                        
                                        _DictForCLKTreeUnitParameters = dict(),
                                        
                                        _DictForUnitXlocation = dict(
                                        
                                        ),

                                        _ParallelMetalWidth=None,
                                        
                                        _TotalLevel = None, _LayoutStackLevel = None,
                                        
                                        _DictForNodeInformation = dict(
                                            # '_LayoutLevelOfNode1' = None
                                            # '_LevelOfNode1 = None
                                        
                                        ),
                                        


                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTree'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(


                                                    
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 


                                        _DefaultXspace = None,
                                        
                                        _DictForCLKTreeUnitParameters = dict(),
                                        
                                        _DictForUnitXlocation = dict(
                                        
                                        ),

                                        _ParallelMetalWidth=None,
                                        
                                        _TotalLevel = None, _LayoutStackLevel = None,
                                        
                                        _DictForNodeInformation = dict(
                                            # '_LayoutLevelOfNode1' = None
                                            # '_LevelOfNode1 = None
                                        
                                        ),
                                        


                                     _Dummy=None
                                     ):
        print ('#########################################################################################################')
        print ('                                    {}  CLK Tree Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj=DRC.DRC()
        
        while True:
            _Name='ClkTree'
            #####################Variable Extraction################################
            if _TotalLevel is None:
                _TotalLevel = 2
            _NumberOfNode = 2**(_TotalLevel) - 1
            
            for i in range(0, _NumberOfNode):
                currentNode = _NumberOfNode - i
                TreeUnit = '_Node' + str(currentNode)
                TopNode = '_Node' + str(_NumberOfNode)
                LevelInfo = '_LevelOfNode' + str(currentNode)
                NodeLevel = currentNode
                for j in range(1,1000000):
                    NodeLevel = NodeLevel / 2
                    if NodeLevel is 0:
                        break
                NodeLevel = j
                _DictForNodeInformation[LevelInfo] = NodeLevel

                Parameter = '_DictForLevel' + str(NodeLevel)
                
                tmpParameter = 'ClkTreeUnitParameter'
                _DictForCLKTreeUnitParameters[tmpParameter] = dict()
                
                if (Parameter in _DictForCLKTreeUnitParameters) is False:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters['_DictForLevel1'])
                else:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters'] = copy.deepcopy(_DictForCLKTreeUnitParameters[Parameter])

                
                self._DesignParameter[TreeUnit] = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= TreeUnit + 'In{}'.format(_Name)))[0]
                _DictForCLKTreeUnitParameters[tmpParameter]['_TreeLevel'] = NodeLevel
                _DictForCLKTreeUnitParameters[tmpParameter]['_TotalLevel'] = _TotalLevel
                _DictForCLKTreeUnitParameters[tmpParameter]['_Dummy'] = _Dummy
                if i is not 0:
                    _DictForCLKTreeUnitParameters[tmpParameter]['_CLKTreeElementParameters']['_DistanceBtwSupplyCenter2MOSEdge'] = self._DesignParameter[TopNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter[TopNode]['_DesignObj']._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
                self._DesignParameter[TreeUnit]['_DesignObj']._CalculateDesignParameter(**_DictForCLKTreeUnitParameters[tmpParameter])
                
            for i in range(1, _NumberOfNode):
                _OutputMetal = '_OutputMetalOfNode' + str(i)
                LevelInfo = '_LevelOfNode' + str(i)
                
                # NodeLevel = i
                # for j in range(1,1000000):
                    # NodeLevel = NodeLevel / 2
                    # if NodeLevel is 0:
                        # break
                # NodeLevel = j
                NodeLevel =_DictForNodeInformation[LevelInfo]
                
                if NodeLevel % 3 is 1:      #OutputMetal is Met3
                    self._DesignParameter[_OutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=400)
                elif NodeLevel % 3 is 2:    #OutputMetal is Met5
                    self._DesignParameter[_OutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400)
                else :
                    self._DesignParameter[_OutputMetal] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0],_Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[],_Width=400)
            
            
            
            
            if _LayoutStackLevel is None:
                _LayoutStackLevel = 1

            
            for i in range(1,_NumberOfNode+1):
                LayoutLevelInfo = '_LayoutLevelOfNode' + str(i)
                LevelInfo = '_LevelOfNode' + str(i)
                
                # _DictForNodeInformation[LayoutLevelInfo] = _DictForNodeInformation[LevelInfo] / _LayoutStackLevel
                tmp = _TotalLevel / _LayoutStackLevel / 2.0#_DictForNodeInformation[LevelInfo]
                for j in range(1,10000):
                    tmp = tmp * 2
                    if _DictForNodeInformation[LevelInfo] < tmp:
                        _DictForNodeInformation[LayoutLevelInfo] = j
                        break


            
            # # )#####################COORDINATION SETTING#########################
            
            for i in range(1, _NumberOfNode+1):
                currentNode = i
                _CurrentNode = '_Node' + str(currentNode)
                _MotherNode = '_Node' + str( int(currentNode/2))
                LayoutLevelInfo = '_LayoutLevelOfNode' + str(i)
                
                TopNode = '_Node' + str(_NumberOfNode)
                NodeLevel = currentNode
                for j in range(1,1000000):
                    NodeLevel = NodeLevel / 2
                    if NodeLevel is 0:
                        break
                NodeLevel = j
                Parameter = '_DictForLevel' + str(NodeLevel)
                
                Xlocation = '_XlocationOfNode' + str(i)
                
                if _DefaultXspace is None:
                    _DefaultXspace = 20000


                Ylocation = (self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + self._DesignParameter['_Node1']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1]) \
                            * (_DictForNodeInformation[LayoutLevelInfo] - 1)
                
                
                
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
                            self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] + _DefaultXspace * 2**(_TotalLevel - NodeLevel), Ylocation ]]
                        else :
                            self._DesignParameter[_CurrentNode]['_XYCoordinates'] = [[ self._DesignParameter[_MotherNode]['_XYCoordinates'][0][0] - _DefaultXspace * 2**(_TotalLevel - NodeLevel), Ylocation ]]
                print ('')

           
            if _ParallelMetalWidth is None:
                _ParallelMetalWidth = _DRCObj._MetalxMinWidth
            
            for i in range(1, _NumberOfNode):
                _OutputMetal = '_OutputMetalOfNode' + str(i)
                _CurrentNode = '_Node' + str(i)
                _LeftChild = '_Node' + str(2*i)
                _RightChild = '_Node' + str(2*i+1)

                NodeLevel = i
                for j in range(1,1000000):
                    NodeLevel = NodeLevel / 2
                    if NodeLevel is 0:
                        break
                NodeLevel = j

                if NodeLevel is _TotalLevel:
                    break

                self._DesignParameter[_OutputMetal]['_Width'] = _ParallelMetalWidth
                tmp = []
                for k in range(1,6):
                    VIATop = '_ViaMet32Met4OnInLineTop' + str(k)
                    tmp.append( [[a+b for a,b in zip(self._DesignParameter[_LeftChild]['_XYCoordinates'][0],self._DesignParameter[_LeftChild]['_DesignObj']._DesignParameter[VIATop]['_XYCoordinates'][0])]
                                ,[a+b for a,b in zip(self._DesignParameter[_RightChild]['_XYCoordinates'][0],self._DesignParameter[_RightChild]['_DesignObj']._DesignParameter[VIATop]['_XYCoordinates'][0])] ])
                for k in range(1,6):
                    VIABot = '_ViaMet32Met4OnInLineBot' + str(k)
                    tmp.append( [[a+b for a,b in zip(self._DesignParameter[_LeftChild]['_XYCoordinates'][0],self._DesignParameter[_LeftChild]['_DesignObj']._DesignParameter[VIABot]['_XYCoordinates'][0])]
                                ,[a+b for a,b in zip(self._DesignParameter[_RightChild]['_XYCoordinates'][0],self._DesignParameter[_RightChild]['_DesignObj']._DesignParameter[VIABot]['_XYCoordinates'][0])] ])
                
                self._DesignParameter[_OutputMetal]['_XYCoordinates'] = tmp
            
            
            
            
            
            # self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'] = [[0,0]]
            # self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'] = [[0, self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]]

            
            # if _DistanceBtwSupplyCenter2MOSEdge is None:
                # # _DistanceBtwSupplyCenter2MOSEdge = _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2
                # # _DistanceBtwSupplyCenter2MOSMet1Edge = _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._MetalxMinSpace + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2
                
                # _DistanceBtwSupplyCenter2MOSEdge = max(_tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2 , _tmpPbodyObj._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + _DRCObj._Metal1MinSpace - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2)
                
                
            # if _HeightCalibration is None:
                # _HeightCalibration = 0
            # if _Vdd2VssHeight is None:
                # _Vdd2VssHeight = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] + self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + 2*_DistanceBtwSupplyCenter2MOSEdge
            
            # _tmpPbodyObj._DesignParameter['_XYCoordinates']=[[0,0]]
            # _tmpNbodyObj._DesignParameter['_XYCoordinates']=[[0,_Vdd2VssHeight + _HeightCalibration]]
            
            
            # #MOSFET Coordinate Setting
            # NMOS_Ylocation = _DistanceBtwSupplyCenter2MOSEdge + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            # PMOS_Ylocation = _tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] - _DistanceBtwSupplyCenter2MOSEdge - self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2
            
            # MOSspaceDRC=_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
            # if _Dummy is True:
                # MOSPODummy = self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
            
            # tempX1 = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + MOSspaceDRC
            # tempX2 = 0
            # if _Dummy is True:
                # tempX2 = MOSPODummy * 2 + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + _DRCObj._PolygateMinSpace
            # tempX = max(tempX1,tempX2)
            
            # if _XYadjust is None:
                # _XYadjust = 0
                
            # if _MOS12MOS2spacebias is None:
                # _MOS12MOS2spacebias = 0
            # if _MOS22MOS3spacebias is None:
                # _MOS22MOS3spacebias = 0
            # if _MOS32MOS4spacebias is None:
                # _MOS32MOS4spacebias = 0
            # if _MOS42MOS5spacebias is None:
                # _MOS42MOS5spacebias = 0
            
            
            # self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[_XYadjust , NMOS_Ylocation]]
            # self._DesignParameter['_PMOS3']['_XYCoordinates'] = [[_XYadjust , PMOS_Ylocation]]
            
            # self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[_XYadjust + tempX + _MOS32MOS4spacebias, NMOS_Ylocation]]
            # self._DesignParameter['_PMOS4']['_XYCoordinates'] = [[_XYadjust + tempX + _MOS32MOS4spacebias, PMOS_Ylocation]]
            
            # self._DesignParameter['_NMOS5']['_XYCoordinates'] = [[_XYadjust + 2*tempX + _MOS32MOS4spacebias + _MOS42MOS5spacebias, NMOS_Ylocation]]
            # self._DesignParameter['_PMOS5']['_XYCoordinates'] = [[_XYadjust + 2*tempX + _MOS32MOS4spacebias + _MOS42MOS5spacebias, PMOS_Ylocation]]
            
            # self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYadjust - tempX + _MOS22MOS3spacebias, NMOS_Ylocation]]
            # self._DesignParameter['_PMOS2']['_XYCoordinates'] = [[_XYadjust - tempX + _MOS22MOS3spacebias, PMOS_Ylocation]]
            
            # self._DesignParameter['_NMOS1']['_XYCoordinates'] = [[_XYadjust - 2*tempX + _MOS12MOS2spacebias + _MOS42MOS5spacebias, NMOS_Ylocation]]
            # self._DesignParameter['_PMOS1']['_XYCoordinates'] = [[_XYadjust - 2*tempX + _MOS12MOS2spacebias + _MOS42MOS5spacebias, PMOS_Ylocation]]
            
            
            # #Gate Via Coordinate Setting and Gate Routing
            # NSupplytmp=[]
            # PSupplytmp=[]
            # if _XbiasforGateVia is None:
                # _XbiasforGateVia = 0 
            # for i in range(1,6):
                # VIA = '_ViaPoly2Met1OnMOS' + str(i)
                # NMOS = '_NMOS' + str(i)  
                # PMOS = '_PMOS' + str(i)  
                # GATE = '_GateRoutingOnMOS' + str(i)
                # AddiGATE = '_AdditionalPOLYRoutingOnMOS' + str(i)
                # AddiMET1 = '_AdditionalMet1RoutingOnMOSGate' + str(i)
                
                # DIVING_VIA1 = '_ViaMet12Met2OnGate' + str(i)
                # DIVING_VIA2 = '_ViaMet22Met3OnGate' + str(i)
                # DIVING_VIA3 = '_ViaMet32Met4OnGate' + str(i)
                
                # self._DesignParameter[VIA]['_XYCoordinates'] = [[self._DesignParameter[NMOS]['_XYCoordinates'][0][0], self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2]]
                
                # tmp=[]
                # for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
                    # tmp.append( [ [a + b for a, b in zip(self._DesignParameter[NMOS]['_XYCoordinates'][0], self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][j]) ]
                                # , [a + b for a, b in zip(self._DesignParameter[PMOS]['_XYCoordinates'][0], self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][j]) ] ] )
                
                # self._DesignParameter[GATE]['_Width'] = self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
                # self._DesignParameter[GATE]['_XYCoordinates'] = tmp
                
                # Most_Rightside = max(self._DesignParameter[GATE]['_XYCoordinates'][-1][0][0] +self._DesignParameter[GATE]['_Width']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
                # Most_Leftside = min(self._DesignParameter[GATE]['_XYCoordinates'][0][0][0] -self._DesignParameter[GATE]['_Width']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2 )
                # Most_Upside =self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 
                # Most_Downside =self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2 
            
                # self._DesignParameter[AddiGATE]['_XWidth'] = Most_Rightside - Most_Leftside
                # self._DesignParameter[AddiGATE]['_YWidth'] = Most_Upside - Most_Downside
                # self._DesignParameter[AddiGATE]['_XYCoordinates'] = [[(Most_Rightside+Most_Leftside)/2,(Most_Downside+Most_Upside)/2]]
                

                # for j in range(0,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']) ):
                    # NSupplytmp.append([ [self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                       # ,[self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][j][0] ,_tmpPbodyObj._DesignParameter['_XYCoordinates'][0][1] ] ])

                    # PSupplytmp.append([ [self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]
                                       # ,[self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][j][0] ,_tmpNbodyObj._DesignParameter['_XYCoordinates'][0][1] ] ])

                # self._DesignParameter[DIVING_VIA1]['_XYCoordinates'] = [copy.deepcopy(self._DesignParameter[VIA]['_XYCoordinates'][0])]
                # self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][0] += _XbiasforGateVia
                # self._DesignParameter[DIVING_VIA2]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                # self._DesignParameter[DIVING_VIA3]['_XYCoordinates'] = self._DesignParameter[DIVING_VIA1]['_XYCoordinates']
                
                
                # Most_Rightside = max(self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][0] +self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                # Most_Leftside = min(self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][0] -self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter[VIA]['_XYCoordinates'][0][0] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2 )
                # Most_Upside =max(self._DesignParameter[VIA]['_XYCoordinates'][0][1] + self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ,  self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][1] +self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
                # Most_Downside =min(self._DesignParameter[VIA]['_XYCoordinates'][0][1] - self._DesignParameter[VIA]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 , self._DesignParameter[DIVING_VIA1]['_XYCoordinates'][0][1] -self._DesignParameter[DIVING_VIA1]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 )
            
                # self._DesignParameter[AddiMET1]['_XWidth'] = Most_Rightside - Most_Leftside
                # self._DesignParameter[AddiMET1]['_YWidth'] = Most_Upside - Most_Downside
                # self._DesignParameter[AddiMET1]['_XYCoordinates'] = [[(Most_Rightside+Most_Leftside)/2,(Most_Downside+Most_Upside)/2]]
                
                

            # if _SupplyRoutingWidth is None:
                # _SupplyRoutingWidth = _DRCObj._Metal1MinWidth
            # self._DesignParameter['_NMOSSupplyRouting']['_Width'] = _SupplyRoutingWidth
            # self._DesignParameter['_PMOSSupplyRouting']['_Width'] = _SupplyRoutingWidth
            # self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = NSupplytmp
            # self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = PSupplytmp
            
            
            # #Output Via Coordinate Setting and ROUTING
            # for i in range(1,6):
                # NMOS = '_NMOS' + str(i)  
                # PMOS = '_PMOS' + str(i)  
                
                # VIA_P = '_ViaMet12Met2OnPMOSOutput' + str(i)
                # VIA_N = '_ViaMet12Met2OnNMOSOutput' + str(i)
                
                # VIA1 = '_ViaMet22Met3OnOutput' + str(i)
                # VIA2 = '_ViaMet32Met4OnOutput' + str(i)
                # VIA3 = '_ViaMet42Met5OnOutput' + str(i)
                # VIA4 = '_ViaMet52Met6OnOutput' + str(i)
                
                # MET2_Horizontal = '_OutputMet2Horizontal' + str(i)
                # MET2_Vertical = '_OutputMet2Vertical' + str(i)
                
                # tmpN=[]
                # tmpP=[]
                # for j in range(1,len(self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])+1 ):
                    # tmpN.append([self._DesignParameter[NMOS]['_XYCoordinates'][0][0] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-j][0] 
                               # ,self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - self._DesignParameter[VIA_N]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                    # tmpP.append([self._DesignParameter[PMOS]['_XYCoordinates'][0][0] + self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-j][0] 
                               # ,self._DesignParameter[PMOS]['_XYCoordinates'][0][1] - self._DesignParameter[PMOS]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 + self._DesignParameter[VIA_P]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 ])
                
                # self._DesignParameter[VIA_N]['_XYCoordinates'] = tmpN
                # self._DesignParameter[VIA_P]['_XYCoordinates'] = tmpP
                
                # self._DesignParameter[MET2_Horizontal]['_Width'] = _DRCObj._MetalxMinWidth
                # self._DesignParameter[MET2_Vertical]['_Width'] = _DRCObj._MetalxMinWidth

                # self._DesignParameter[MET2_Horizontal]['_XYCoordinates'] = [[self._DesignParameter[VIA_N]['_XYCoordinates'][0] ,self._DesignParameter[VIA_N]['_XYCoordinates'][-1] ]]
                # self._DesignParameter[MET2_Horizontal]['_XYCoordinates'].append([self._DesignParameter[VIA_P]['_XYCoordinates'][0] ,self._DesignParameter[VIA_P]['_XYCoordinates'][-1] ])
                
                # tmp = []
                # for j in range(0,len(self._DesignParameter[VIA_N]['_XYCoordinates'])):
                    # if j % 2 is 0:
                        # tmp.append([self._DesignParameter[VIA_N]['_XYCoordinates'][j] ,self._DesignParameter[VIA_P]['_XYCoordinates'][j] ])
                # self._DesignParameter[MET2_Vertical]['_XYCoordinates'] = tmp
                
                # self._DesignParameter[VIA1]['_XYCoordinates'] =[[ self._DesignParameter[MET2_Horizontal]['_XYCoordinates'][0][0][0] + self._DesignParameter[VIA1]['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2 - self._DesignParameter[MET2_Vertical]['_Width']/2 
                                                                # , self._DesignParameter[NMOS]['_XYCoordinates'][0][1] + self._DesignParameter[NMOS]['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2 ]]
                # self._DesignParameter[VIA2]['_XYCoordinates'] = [self._DesignParameter[VIA1]['_XYCoordinates'][0]]
                # self._DesignParameter[VIA3]['_XYCoordinates'] = [self._DesignParameter[VIA1]['_XYCoordinates'][0]]
                # self._DesignParameter[VIA4]['_XYCoordinates'] = [self._DesignParameter[VIA1]['_XYCoordinates'][0]]
            
            


            # Right_Side = self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            # Left_Side = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2
            # NMOS_NPlength = Right_Side - Left_Side
            # _EdgeBtwNWandPW = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            
            # # )################################ NWELL ################################
            # self._DesignParameter['_NWell']['_XWidth']= round((NMOS_NPlength + _DRCObj._NwMinEnclosurePactive*2)/2/_DRCObj._MinSnapSpacing) * 2 * _DRCObj._MinSnapSpacing
            # self._DesignParameter['_NWell']['_YWidth']= _Vdd2VssHeight + _HeightCalibration - _EdgeBtwNWandPW + (float (_tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2)) + _DRCObj._NwMinEnclosurePactive
            # self._DesignParameter['_NWell']['_XYCoordinates'] = [[0, (float)(self._DesignParameter['_NWell']['_YWidth']/2) + _EdgeBtwNWandPW  ]]
            # # )################################ NP UnderNMOS )################################
            # tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]]]
            # tmp[0][1] = tmp[0][1] + (float)(_EdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2)/2 -self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']/2
            # self._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'] = tmp
            # # self._DesignParameter['_NIMPUnderNMOS']['_XWidth']= round( (abs(self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) + abs(self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            # self._DesignParameter['_NIMPUnderNMOS']['_XWidth'] = NMOS_NPlength
            # self._DesignParameter['_NIMPUnderNMOS']['_YWidth']= _EdgeBtwNWandPW - _tmpPbodyObj._DesignParameter['_PPLayer']['_YWidth']/2
            # # )################################ PP UnderNMOS )################################
            # # self._DesignParameter['_PIMPUnderPMOS']['_XWidth']= round( (abs(self._DesignParameter['_PMOS1']['_XYCoordinates'][0][0]-self._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) + abs(self._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2) )/_DRCObj._MinSnapSpacing/2 + 0.5) *2* _DRCObj._MinSnapSpacing 
            # self._DesignParameter['_PIMPUnderPMOS']['_XWidth'] = NMOS_NPlength
            # self._DesignParameter['_PIMPUnderPMOS']['_YWidth']=  _Vdd2VssHeight + _HeightCalibration - _EdgeBtwNWandPW - _tmpNbodyObj._DesignParameter['_NPLayer']['_YWidth']/2
            # tmp = [[(Right_Side + Left_Side)/2, self._DesignParameter['_PMOS3']['_XYCoordinates'][0][1]]]
            # tmp[0][1] = tmp[0][1] - ((self._DesignParameter['_PIMPUnderPMOS']['_YWidth'])/2 - self._DesignParameter['_PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)
            # self._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'] = tmp

            
            # # BodyContact Adjusting
            # _LengthOfBody = self._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']
            # leftSideOD = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2 
            # rightSideOD = self._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2
            # _LengthOfOD = abs(rightSideOD - leftSideOD )

            # if _NumberOfSupplyCOX is None:
                # _NumberOfSupplyCOX =int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=None, NumOfCOX=None)) if _PbodyDesignCalculationParameters['_NumberOfPbodyCOY']==1 \
                        # else int(_LengthOfOD - 2*_DRCObj._CoMinEnclosureByOD + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))/(_DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOY=3, NumOfCOX=3))
            # _PbodyDesignCalculationParameters['_NumberOfPbodyCOX']=_NumberOfSupplyCOX
            # _NbodyDesignCalculationParameters['_NumberOfNbodyCOX']=_NumberOfSupplyCOX
            # _PbodyDesignCalculationParameters['_Met1YWidth'] = _SupplyMetal1YWidth
            # _NbodyDesignCalculationParameters['_Met1YWidth'] = _SupplyMetal1YWidth

            # self._DesignParameter['_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_PbodyDesignCalculationParameters)
            # self._DesignParameter['_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_NbodyDesignCalculationParameters)
            # self._DesignParameter['_PbodyContact']['_XYCoordinates'] = _tmpPbodyObj._DesignParameter['_XYCoordinates']
            # self._DesignParameter['_NbodyContact']['_XYCoordinates'] = _tmpNbodyObj._DesignParameter['_XYCoordinates']


            # del _tmpPbodyObj
            # del _tmpNbodyObj
            
            
            
            
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
                                            _DictForLevel1 = dict
                                            (_NumberOfGate=6, _ChannelWidth=450, _ChannelLength=60, _PNChannelRatio=2,
                                            _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _Dummy = False)

                                        ),

                                        _TotalLevel = 4, _LayoutStackLevel=2,
                                        

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






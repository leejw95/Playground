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



import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _CLKTreeUnit(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(

                                        _CLKTreeElementParameters = copy.deepcopy(ClkTreeElement._ClkTreeElement._ParametersForDesignCalculation),

                                        _TreeLevel=None,_TotalLevel=None,

                                        _MetalInType=None,

                                        _MetalOutType=None, inputRotation = None,


                                        _OutputViaLevelForTop=None, _OutputViaLevelForBot=None,


                                        _OutLineIgnore=None,_NumberOfParallelViaCOY=None, _NumberOfParallelViaCOX=None,
                                        
                                        _CCRoutingMetWidth = None,


                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTreeUnit'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(



                                                    _ClkTreeElementTop = self._SrefElementDeclaration(_DesignObj=ClkTreeElement._ClkTreeElement(_DesignParameter=None, _Name='ClkTreeElementTopIn{}'.format(_Name)))[0],
                                                    _ClkTreeElementBot = self._SrefElementDeclaration(_DesignObj=ClkTreeElement._ClkTreeElement(_DesignParameter=None, _Name='ClkTreeElementBotIn{}'.format(_Name)))[0],


                                                    _ViaMet32Met4OnInLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineTop5In{}'.format(_Name)))[0],

                                                    _ViaMet42Met5OnInLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineTop5In{}'.format(_Name)))[0],

                                                    _ViaMet52Met6OnInLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineTop5In{}'.format(_Name)))[0],

                                                    _ViaMet62Met7OnInLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineTop5In{}'.format(_Name)))[0],


                                                    _ViaMet32Met4OnInLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnInLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnInLineBot5In{}'.format(_Name)))[0],

                                                    _ViaMet42Met5OnInLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnInLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnInLineBot5In{}'.format(_Name)))[0],

                                                    _ViaMet52Met6OnInLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet52Met6OnInLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnInLineBot5In{}'.format(_Name)))[0],

                                                    _ViaMet62Met7OnInLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnInLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnInLineBot5In{}'.format(_Name)))[0],



                                                    _ViaMet32Met4OnOutLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineTop5In{}'.format(_Name)))[0],

                                                    _ViaMet42Met5OnOutLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineTop5In{}'.format(_Name)))[0],

                                                    _ViaMet62Met7OnOutLineTop1 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineTop1In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineTop2 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineTop2In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineTop3 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineTop3In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineTop4 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineTop4In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineTop5 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineTop5In{}'.format(_Name)))[0],


                                                    _ViaMet32Met4OnOutLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOutLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOutLineBot5In{}'.format(_Name)))[0],

                                                    _ViaMet42Met5OnOutLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOutLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOutLineBot5In{}'.format(_Name)))[0],

                                                    _ViaMet62Met7OnOutLineBot1 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineBot1In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineBot2 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineBot2In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineBot3 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineBot3In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineBot4 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineBot4In{}'.format(_Name)))[0],
                                                    _ViaMet62Met7OnOutLineBot5 = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnOutLineBot5In{}'.format(_Name)))[0],




                                                    _CCverticalMet2Routing = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 ),
                                                    _CCverticalMet4Routing = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),


                                                    _InputDivingMet4OnInLineTop1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineTop2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineTop3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineTop4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineTop5 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),

                                                    _InputDivingMet4OnInLineBot1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineBot2 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineBot3 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineBot4 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),
                                                    _InputDivingMet4OnInLineBot5 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 ),

                                                    _CrossCoupledConnectionMet3 =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100 ),
                                                    _CrossCoupledConnectionMet2ForTop =  self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100 ),

                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)

    def _CalculateDesignParameter(self,


                                        _CLKTreeElementParameters = copy.deepcopy(ClkTreeElement._ClkTreeElement._ParametersForDesignCalculation),

                                        _TreeLevel=None,_TotalLevel=None,

                                        _MetalInType=None,

                                        _MetalOutType=None, inputRotation = None, 


                                        _OutputViaLevelForTop=None, _OutputViaLevelForBot=None,


                                        _OutLineIgnore=None,_NumberOfParallelViaCOY=None, _NumberOfParallelViaCOX=None,
                                        
                                        _CCRoutingMetWidth = None,


                                     _Dummy=None
                                     ):
        print '#########################################################################################################'
        print '                                    {}  CLK Tree Unit Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'



        _DRCObj=DRC.DRC()

        while True:
            #####################SUBSET ELEMENTS GENERATION#########################
            # CLK Tree Element GENERATION


            # Share Parameter btw Tree Unit and Tree Element
            _CLKTreeElementParameters['_TreeLevel']=_TreeLevel
            _CLKTreeElementParameters['_TotalLevel']=_TotalLevel
            # _CLKTreeElementParameters['_NumberOfParallelViaCOY']=_NumberOfParallelViaCOY
            _CLKTreeElementParameters['_Dummy']=_Dummy



            self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._CalculateDesignParameter(**_CLKTreeElementParameters)
            self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][0] = self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][0]
            self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._CalculateDesignParameter(**_CLKTreeElementParameters)

            self._DesignParameter['_ClkTreeElementTop']['_Reflect']=(1,0,0)
            self._DesignParameter['_ClkTreeElementTop']['_Angle']=0


            if _NumberOfParallelViaCOY is None:
                _NumberOfParallelViaCOY = 1
            if _NumberOfParallelViaCOX is None:
                _NumberOfParallelViaCOX = 2

            self._DesignParameter['_ViaMet32Met4OnInLineTop1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineTop2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineTop3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineTop4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineTop5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet42Met5OnInLineTop1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineTop2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineTop3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineTop4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineTop5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet52Met6OnInLineTop1']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineTop2']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineTop3']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineTop4']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineTop5']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet62Met7OnInLineTop1']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineTop2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineTop3']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineTop4']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineTop5']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet32Met4OnInLineBot1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineBot2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineBot3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineBot4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnInLineBot5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet42Met5OnInLineBot1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineBot2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineBot3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineBot4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnInLineBot5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet52Met6OnInLineBot1']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineBot2']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineBot3']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineBot4']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet52Met6OnInLineBot5']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(_ViaMet52Met6NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet52Met6NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet62Met7OnInLineBot1']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineBot2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineBot3']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineBot4']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnInLineBot5']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)


            self._DesignParameter['_ViaMet32Met4OnOutLineTop1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineTop2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineTop3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineTop4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineTop5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet42Met5OnOutLineTop1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineTop2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineTop3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineTop4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineTop5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet62Met7OnOutLineTop1']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineTop2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineTop3']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineTop4']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineTop5']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet32Met4OnOutLineBot1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineBot2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineBot3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineBot4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOutLineBot5']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet32Met4NumberOfCOY=_NumberOfParallelViaCOY)

            self._DesignParameter['_ViaMet42Met5OnOutLineBot1']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineBot2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineBot3']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineBot4']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOutLineBot5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet42Met5NumberOfCOY=_NumberOfParallelViaCOY)

            # self._DesignParameter['_ViaMet62Met7OnOutLineBot1']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=_NumberOfParallelViaCOX, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineBot2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineBot3']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineBot4']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)
            # self._DesignParameter['_ViaMet62Met7OnOutLineBot5']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(_ViaMet62Met7NumberOfCOX=2, _ViaMet62Met7NumberOfCOY=_NumberOfParallelViaCOY)


            if _TreeLevel is None:
                _TreeLevel = 1
            # MetalInType = _TreeLevel % 3           #Input Metal Type  0: Metal 5, 1 : Metal7, 2: Metal 3,
                                                   # #Output Metal Type 0: Metal 7, 1 : Metal3, 2: Metal 5 --> Delete
                                                     #Output Metal Type 0: Metal 3, 1 : XXXXXX, 2: Metal 5 --> Delete



            # OnlyMetalInType Case:
            #    In    Out
            #0 : M5    M3
            #2 : M3    M5

            # If MetalOutVia is OFF:
            #    In    Out
            #1 : M3     X



            ####Work In Progress###################################################################################################################################################################################################################
            if _MetalInType is 'Metal3':
                for i in range(1,6):
                    self._DesignParameter['_ViaMet42Met5OnInLineTop'+str(i)]['_Ignore']=True
                    self._DesignParameter['_ViaMet42Met5OnInLineBot'+str(i)]['_Ignore']=True
            elif _MetalInType is 'Metal5':
                for i in range(1,6):
                    self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_Ignore']=True
                    self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_Ignore']=True
            elif _MetalInType is 'Metal2andMetal4':
                for i in range(1,6):
                    self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet32Met4OnGate'+str(i)]['_Ignore'] =True
                    self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate'+str(i)]['_Ignore'] =True
                    for j in range(3,6):
                        self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnInLineTop'+str(i)]['_Ignore']=True
                        self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnInLineBot'+str(i)]['_Ignore']=True
            elif _MetalInType is 'Metal4andMetal6':
                for i in range(1,6):
                    self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet42Met5OnGate'+str(i)]['_Ignore'] = None
                    self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet52Met6OnGate'+str(i)]['_Ignore'] = None
                    self._DesignParameter['_InputDivingMet4OnInLineTop'+str(i)]['_Ignore'] = True
                    self._DesignParameter['_InputDivingMet4OnInLineBot'+str(i)]['_Ignore'] = True
                    for j in range(3,6):
                        self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnInLineTop'+str(i)]['_Ignore']=True
                        self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnInLineBot'+str(i)]['_Ignore']=True

            if _MetalOutType is 'Metal3':
                for i in range(1,6):
                    self._DesignParameter['_ViaMet42Met5OnOutLineTop'+str(i)]['_Ignore']=True
                    self._DesignParameter['_ViaMet42Met5OnOutLineBot'+str(i)]['_Ignore']=True
            elif _MetalOutType is 'Metal5':
                for i in range(1,6):
                    self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_Ignore'] = True
                    self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_Ignore'] = True
            elif _MetalOutType is 'Metal4andMetal6':
                for i in range(1,6):
                    self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_Ignore'] = True
                    self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_Ignore'] = True
                    self._DesignParameter['_ViaMet42Met5OnOutLineTop'+str(i)]['_Ignore']=True
                    self._DesignParameter['_ViaMet42Met5OnOutLineBot'+str(i)]['_Ignore']=True
                    # for j in range(3,6):
                        # self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnOutLineTop'+str(i)]['_Ignore']=True
                        # self._DesignParameter['_ViaMet'+str(j)+'2Met'+str(j+1)+'OnOutLineBot'+str(i)]['_Ignore']=True


            for i in range(1,6):
                _OutputDivingMetTop = '_OutputDivingMETtop' + str(i)
                _OutputDivingMetBot = '_OutputDivingMETbot' + str(i)

                # if MetalInType is 0:
                    # self._DesignParameter[_OutputDivingMetTop] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100 )
                    # self._DesignParameter[_OutputDivingMetBot] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=100 )
                # else :
                    # self._DesignParameter[_OutputDivingMetTop] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )
                    # self._DesignParameter[_OutputDivingMetBot] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )
                self._DesignParameter[_OutputDivingMetTop] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )
                self._DesignParameter[_OutputDivingMetBot] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100 )

                self._DesignParameter[_OutputDivingMetTop]['_Width'] = _DRCObj._MetalxMinWidth
                self._DesignParameter[_OutputDivingMetBot]['_Width'] = _DRCObj._MetalxMinWidth


            if _TreeLevel is 1:
                self._DesignParameter['_ViaMet32Met4OnInLineTop1']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineTop2']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineTop3']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineTop4']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineTop5']['_Ignore']= True

                self._DesignParameter['_ViaMet42Met5OnInLineTop1']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineTop2']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineTop3']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineTop4']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineTop5']['_Ignore']= True

                self._DesignParameter['_ViaMet52Met6OnInLineTop1']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineTop2']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineTop3']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineTop4']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineTop5']['_Ignore']= True

                self._DesignParameter['_ViaMet62Met7OnInLineTop1']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineTop2']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineTop3']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineTop4']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineTop5']['_Ignore']= True


                self._DesignParameter['_ViaMet32Met4OnInLineBot1']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineBot2']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineBot3']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineBot4']['_Ignore']= True
                self._DesignParameter['_ViaMet32Met4OnInLineBot5']['_Ignore']= True

                self._DesignParameter['_ViaMet42Met5OnInLineBot1']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineBot2']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineBot3']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineBot4']['_Ignore']= True
                self._DesignParameter['_ViaMet42Met5OnInLineBot5']['_Ignore']= True

                self._DesignParameter['_ViaMet52Met6OnInLineBot1']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineBot2']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineBot3']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineBot4']['_Ignore']= True
                self._DesignParameter['_ViaMet52Met6OnInLineBot5']['_Ignore']= True

                self._DesignParameter['_ViaMet62Met7OnInLineBot1']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineBot2']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineBot3']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineBot4']['_Ignore']= True
                self._DesignParameter['_ViaMet62Met7OnInLineBot5']['_Ignore']= True

                self._DesignParameter['_InputDivingMet4OnInLineTop1']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineTop2']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineTop3']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineTop4']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineTop5']['_Ignore'] = True

                self._DesignParameter['_InputDivingMet4OnInLineBot1']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineBot2']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineBot3']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineBot4']['_Ignore'] = True
                self._DesignParameter['_InputDivingMet4OnInLineBot5']['_Ignore'] = True

            # if _TreeLevel is _TotalLevel:
                # self._DesignParameter['_ViaMet32Met4OnOutLineTop1']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineTop2']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineTop3']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineTop4']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineTop5']['_Ignore']=True

                # self._DesignParameter['_ViaMet42Met5OnOutLineTop1']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineTop2']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineTop3']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineTop4']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineTop5']['_Ignore']=True

                # self._DesignParameter['_ViaMet62Met7OnOutLineTop1']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineTop2']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineTop3']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineTop4']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineTop5']['_Ignore']=True

                # self._DesignParameter['_ViaMet32Met4OnOutLineBot1']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineBot2']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineBot3']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineBot4']['_Ignore']=True
                # self._DesignParameter['_ViaMet32Met4OnOutLineBot5']['_Ignore']=True

                # self._DesignParameter['_ViaMet42Met5OnOutLineBot1']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineBot2']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineBot3']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineBot4']['_Ignore']=True
                # self._DesignParameter['_ViaMet42Met5OnOutLineBot5']['_Ignore']=True

                # self._DesignParameter['_ViaMet62Met7OnOutLineBot1']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineBot2']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineBot3']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineBot4']['_Ignore']=True
                # self._DesignParameter['_ViaMet62Met7OnOutLineBot5']['_Ignore']=True

                # for i in range(1,6):
                    # METtop = '_OutputDivingMETtop' + str(i)
                    # METbot = '_OutputDivingMETbot' + str(i)
                    # self._DesignParameter[METtop]['_Ignore'] = True
                    # self._DesignParameter[METbot]['_Ignore'] = True

            #Diving Metal Width
            for i in range(1,6):
                self._DesignParameter['_InputDivingMet4OnInLineTop'+str(i)]['_Width'] = self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
                self._DesignParameter['_InputDivingMet4OnInLineBot'+str(i)]['_Width'] = self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
                self._DesignParameter['_OutputDivingMETtop'+str(i)]['_Width'] = self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
                self._DesignParameter['_OutputDivingMETbot'+str(i)]['_Width'] = self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']



            if _OutputViaLevelForTop is None:
                print "No option for OutputVia Level(TOP)"
            else :
                for i in range(0, 6-_OutputViaLevelForTop):
                    for j in range(1,6):
                        self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet' + str(5-i) +'2Met' + str(6-i) + 'OnOutput' + str(j)]['_Ignore'] = True
                    if i is 3:
                        self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_AdditionalMet3RoutingOnOutput']['_Ignore'] = True

            if _OutputViaLevelForBot is None:
                print "No option for OutputVia Level(BOT)"
            else :
                for i in range(0, 6-_OutputViaLevelForBot):
                    for j in range(1,6):
                        self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet' + str(5-i) +'2Met' + str(6-i) + 'OnOutput' + str(j)]['_Ignore'] = True
                    if i is 3:
                        self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_AdditionalMet3RoutingOnOutput']['_Ignore'] = True

            if _OutLineIgnore is True:
                for i in range(3, 7):
                    if i is not 5:
                        for j in range(1,6):
                            self._DesignParameter['_ViaMet' + str(i) +'2Met' + str(i+1) + 'OnOutLineTop' + str(j)]['_Ignore'] = True
                            self._DesignParameter['_ViaMet' + str(i) +'2Met' + str(i+1) + 'OnOutLineBot' + str(j)]['_Ignore'] = True
                            self._DesignParameter['_OutputDivingMETtop'+str(j)]['_Ignore'] = True
                            self._DesignParameter['_OutputDivingMETbot'+str(j)]['_Ignore'] = True
            ####Work In Progress###################################################################################################################################################################################################################





            # # )#####################COORDINATION SETTING#########################



            self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'] = [[0,0]]
            self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'] = [[0, self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]]


            if inputRotation is None:
                inputRotation = False



            for i in range(1,6):   #ViaFor OutLineTop And Diving Met
                if i is 1:
                    inputN = 1
                    inLineN = 1
                    if inputRotation is True:
                        inputN = 4
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate1']['_XYCoordinates'][0][1])
                elif i is 2:
                    inputN = 2
                    inLineN = 2
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate2']['_XYCoordinates'][0][1])
                elif i is 3:
                    inputN = 1
                    inLineN = 3
                    if inputRotation is True:
                        inputN = 4
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate1']['_XYCoordinates'][0][1]
                elif i is 4:
                    inputN = 2
                    inLineN = 4
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate2']['_XYCoordinates'][0][1]
                elif i is 5:
                    inputN = 5
                    inLineN = 5
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate5']['_XYCoordinates'][0][1])
                tmp = []
                tmp2 = []
                for k in range(0,len(self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate1']['_XYCoordinates'])):
                    tmp.append([ self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate'+str(inputN)]['_XYCoordinates'][k][0] \
                                ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._ParametersForDesignCalculation['InLinelocation'+str(inLineN)]) ])
                    tmp2.append([ tmp[k]
                                , [tmp[k][0],TopOrBot ]])
                self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_XYCoordinates'] = tmp
                self._DesignParameter['_ViaMet42Met5OnInLineTop'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet52Met6OnInLineTop'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet62Met7OnInLineTop'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineTop'+str(i)]['_XYCoordinates']
                self._DesignParameter['_InputDivingMet4OnInLineTop'+str(i)]['_XYCoordinates'] = tmp2






            for i in range(1,6):   #ViaFor OutLineTop And Diving Met
                if i is 1:
                    inputN = 3
                    inLineN = 1
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate1']['_XYCoordinates'][0][1]
                elif i is 2:
                    inputN = 4
                    inLineN = 2
                    if inputRotation is True:
                        inputN = 1
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate2']['_XYCoordinates'][0][1]
                elif i is 3:
                    inputN = 3
                    inLineN = 3
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate1']['_XYCoordinates'][0][1] )
                elif i is 4:
                    inputN = 4
                    inLineN = 4
                    if inputRotation is True:
                        inputN = 1
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate2']['_XYCoordinates'][0][1] )
                elif i is 5:
                    inputN = 5
                    inLineN = 5
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate5']['_XYCoordinates'][0][1]
                tmp = []
                tmp2 = []
                for k in range(0,len(self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate3']['_XYCoordinates'])):
                    tmp.append([ self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnGate'+str(inputN)]['_XYCoordinates'][k][0] \
                                ,self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._ParametersForDesignCalculation['InLinelocation'+str(inLineN)] ])
                    tmp2.append([ tmp[k]
                                , [tmp[k][0],TopOrBot ]])
                self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_XYCoordinates'] = tmp
                self._DesignParameter['_ViaMet42Met5OnInLineBot'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet52Met6OnInLineBot'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet62Met7OnInLineBot'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnInLineBot'+str(i)]['_XYCoordinates']
                self._DesignParameter['_InputDivingMet4OnInLineBot'+str(i)]['_XYCoordinates'] = tmp2



            for i in range(1,6):   #ViaFor OutLineTop And Diving Met
                if i is 1:
                    outputN = 1
                    outLineN = 1
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1])
                elif i is 2:
                    outputN = 2
                    outLineN = 2
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1])
                elif i is 3:
                    outputN = 1
                    outLineN = 3
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                elif i is 4:
                    outputN = 2
                    outLineN = 4
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                elif i is 5:
                    outputN = 5
                    outLineN = 5
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1])
                tmp = []
                tmp2 = []
                for k in range(0,len(self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'])):
                    tmp.append([ self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(outputN)]['_XYCoordinates'][k][0] \
                                ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._ParametersForDesignCalculation['OutLinelocation'+str(outLineN)]) ])
                    Xlocation = tmp[k][0] - self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2 + self._DesignParameter['_OutputDivingMETtop'+str(outLineN)]['_Width']/2
                    tmp2.append([ [Xlocation,tmp[k][1]]
                                , [Xlocation,TopOrBot ]])
                self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_XYCoordinates'] = tmp
                self._DesignParameter['_ViaMet42Met5OnOutLineTop'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet62Met7OnOutLineTop'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnOutLineTop'+str(i)]['_XYCoordinates']
                self._DesignParameter['_OutputDivingMETtop'+str(i)]['_XYCoordinates'] = tmp2

            for i in range(1,6):   #ViaFor OutLineBot And Diving Met
                if i is 1:
                    outputN = 3
                    outLineN = 1
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1]
                elif i is 2:
                    outputN = 4
                    outLineN = 2
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1]
                elif i is 3:
                    outputN = 3
                    outLineN = 3
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'][0][1] )
                elif i is 4:
                    outputN = 4
                    outLineN = 4
                    TopOrBot = self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput2']['_XYCoordinates'][0][1] )
                elif i is 5:
                    outputN = 5
                    outLineN = 5
                    TopOrBot = self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput5']['_XYCoordinates'][0][1]
                tmp = []
                tmp2 = []
                for k in range(0,len(self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_XYCoordinates'])):
                    tmp.append([ self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput'+str(outputN)]['_XYCoordinates'][k][0] \
                                ,self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][1] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._ParametersForDesignCalculation['OutLinelocation'+str(outLineN)] ])
                    Xlocation = tmp[k][0] - self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2 + self._DesignParameter['_OutputDivingMETbot'+str(outLineN)]['_Width']/2
                    tmp2.append([ [Xlocation,tmp[k][1]]
                                , [Xlocation,TopOrBot ]])
                self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_XYCoordinates'] = tmp
                self._DesignParameter['_ViaMet42Met5OnOutLineBot'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_XYCoordinates']
                self._DesignParameter['_ViaMet62Met7OnOutLineBot'+str(i)]['_XYCoordinates'] = self._DesignParameter['_ViaMet32Met4OnOutLineBot'+str(i)]['_XYCoordinates']
                self._DesignParameter['_OutputDivingMETbot'+str(i)]['_XYCoordinates'] = tmp2




                
            ###########CrossCoupled###########
            if _CCRoutingMetWidth is None:
                _CCRoutingMetWidth = _DRCObj._MetalxMinWidth
            Met2XYmid = [a+b for a,b in zip(self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0], self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0]) ]
            Met2XYmid[1] += self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']/2 + _DRCObj._MetalxMinSpace + _CCRoutingMetWidth/2


            
            self._DesignParameter['_CCverticalMet4Routing']['_Width'] = _CCRoutingMetWidth
            self._DesignParameter['_CCverticalMet4Routing']['_XYCoordinates'] = [[ [a+b for a,b in zip(self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0], self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0]) ]
                                                                                  ,[self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0][0]
                                                                                   ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0][1]) ]
                                                                                ]]
            self._DesignParameter['_CCverticalMet2Routing']['_Width'] = _CCRoutingMetWidth
            self._DesignParameter['_CCverticalMet2Routing']['_XYCoordinates'] = [[ [self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0][0]
                                                                                   ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnCCDrain']['_XYCoordinates'][0][1]) ]
                                                                                  ,Met2XYmid
                                                                                  ,[self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][0], Met2XYmid[1]]
                                                                                  ,[a+b for a,b in zip(self._DesignParameter['_ClkTreeElementBot']['_XYCoordinates'][0],self._DesignParameter['_ClkTreeElementBot']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0] )]
                                                                                ]]
            
            self._DesignParameter['_CrossCoupledConnectionMet3']['_Width'] = self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            self._DesignParameter['_CrossCoupledConnectionMet3']['_XYCoordinates'] = [[  [self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][0] 
                                                                                         ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][1]) ]
                                                                                        ,[self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet32Met4OnCCDrain']['_XYCoordinates'][0][0]
                                                                                         ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet32Met4OnCCDrain']['_XYCoordinates'][0][1]) ]
                                                                                     ]]

            self._DesignParameter['_CrossCoupledConnectionMet2ForTop']['_Width'] = self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
            self._DesignParameter['_CrossCoupledConnectionMet2ForTop']['_XYCoordinates'] = [[ [self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][0] 
                                                                                              ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][1]) ]
                                                                                             ,[self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][0] + self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnCCDrain']['_XYCoordinates'][0][0] 
                                                                                              ,self._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet12Met2OnGate6']['_XYCoordinates'][0][1]) ]
                                                                                           ]]
            

            # )################################ DRC Verification ################################

            DRC_PASS=1


            if self._DesignParameter['_Name']['_Name'] == '_Node3InClkTree':
                print 'check'
                print self._DesignParameter['_ClkTreeElementTop']['_DesignObj']._DesignParameter['_ViaMet22Met3OnOutput1']['_Ignore']


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
    CLKTreeUnitObj=_CLKTreeUnit(_DesignParameter=None, _Name='CLKTreeUnit')
    CLKTreeUnitObj._CalculateDesignParameter(

                                    _CLKTreeElementParameters = dict(
                                            _NumberOfGate=2, _ChannelWidth=320, _ChannelLength=60, _PNChannelRatio=750./320., _NumberOfGateViaCOY=2, 
                                            _PMOSOutputMetalWidth=200, _NMOSOutputMetalWidth=200, _NumberOfParallelViaCOY = 2,
                                            _MOS12MOS2spacebias=200, _MOS22MOS3spacebias=200, _MOS32MOS4spacebias=200, _MOS42MOS5spacebias=200,
                                            _SupplyMetal1YWidth=300, _NumberOfPMOSOutputViaCOY=4, _MetalxDRC= 140, _ParallelMetalWidth= 300,
                                            _XbiasforGateVia = -620,

                                        _EdgeBtwNWandPW = 1415,
                                        _Vdd2VssHeight=3700, _HeightCalibration=None,
                                        _NumberOfCCMOSDrainViaCOX = 1, _NumberOfCCMOSDrainViaCOY = 2,
                                        _NumberOfCoupledGate=1, _CoupledChannelWidth=180,
                                        _NumberOfCoupledMOSGateViaCOX = 2, _XbiasForCoupledMOSGateVia=55,
                                        
                                        _NumberOfCLKInvGate = 2
                                        , _CLKInvChannelWidth=320., _CLKInvPNChannelRatio=750./320.,

                                        ),



                                    _TreeLevel = 1, _TotalLevel = 1,

                                    _MetalInType=None,

                                    _MetalOutType=None,


                                    _OutputViaLevelForTop=None, _OutputViaLevelForBot=None,


                                    _OutLineIgnore=None,_NumberOfParallelViaCOY=2,


                                    _Dummy=False
                                    )



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
    CLKTreeUnitObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=CLKTreeUnitObj._DesignParameter)
    _fileName='autoClkUnit2.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=CLKTreeUnitObj._CreateGDSStream(CLKTreeUnitObj._DesignParameter['_GDSFile']['_GDSFile'])

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






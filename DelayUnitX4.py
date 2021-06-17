import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaPoly2Met1

import DelayUnitDesign
import XOR
import C2FlipFlop
import DelayUnit

import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _DELAYUNITX4(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
    
                                     # _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitDesign._DelayUnitDesign),
                                     _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnit._DELAYUNIT._ParametersForDesignCalculation),
                                     _NWellexpandXonFF = None, _PPexpandXonFF = None, _NPexpandXonFF = None, 
                                     _NWellexpandXonXOR = None, _PPexpandXonXOR = None, _NPexpandXonXOR = None, 
                                     
                                     _DU12DU2spacebias = None,_DU22DU3spacebias = None,_DU32DU4spacebias = None,
                                     
                                     _Outputexpand = None, _OutputWidth = None,

                                     _MetalxDRC = None, _NumberOfOutputViaCOY = None,
                                     
                                     _Outline1Location = None,_Outline2Location = None,_Outline3Location = None,_Outline4Location = None,

                                     _YbiasForTopOutputVia=None,_YbiasForBotOutputVia = None,

                                     _Dummy=DelayUnitDesign._DelayUnitDesign['_Dummy']
                                     )

    def __init__(self, _DesignParameter=None, _Name='INV'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(

                                                    _DelayUnit1 = self._SrefElementDeclaration(_DesignObj=DelayUnit._DELAYUNIT(_DesignParameter=None, _Name='DelayUnit1In{}'.format(_Name)))[0],
                                                    _DelayUnit2 = self._SrefElementDeclaration(_DesignObj=DelayUnit._DELAYUNIT(_DesignParameter=None, _Name='DelayUnit2In{}'.format(_Name)))[0],
                                                    _DelayUnit3 = self._SrefElementDeclaration(_DesignObj=DelayUnit._DELAYUNIT(_DesignParameter=None, _Name='DelayUnit3In{}'.format(_Name)))[0],
                                                    _DelayUnit4 = self._SrefElementDeclaration(_DesignObj=DelayUnit._DELAYUNIT(_DesignParameter=None, _Name='DelayUnit4In{}'.format(_Name)))[0],
                                                    # _FFbot = self._SrefElementDeclaration(_DesignObj=C2FlipFlop._FLIPFLOP(_DesignParameter=None, _Name='FFbotIn{}'.format(_Name)))[0],

                                                    _ViaMet12Met2OnDU2FFTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU2FFTopInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnDU2FFBotInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU2FFBotInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnDU3FFTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU3FFTopInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnDU3FFBotInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU3FFBotInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnDU4FFTopInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU4FFTopInputIn{}'.format(_Name)))[0],
                                                    _ViaMet12Met2OnDU4FFBotInput = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnDU4FFBotInputIn{}'.format(_Name)))[0],

                                                    _DU1out2DU2inTopMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _DU1out2DU2inBotMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _DU2out2DU3inTopMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _DU2out2DU3inBotMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _DU3out2DU4inTopMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    _DU3out2DU4inBotMet2Connection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _PowerLine1Met1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PowerLine2Met1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PowerLine3Met1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PowerLine4Met1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    _PowerLine5Met1 = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _PowerLine1PIMP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine2NIMP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine3PIMP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine4NIMP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine5PIMP=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _PowerLine1ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine2ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine3ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine4ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PowerLine5ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    
                                                    
                                                    _NIMPUnderFFbot = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderFFbot = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderFFtop = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderFFtop = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderXORbot = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderXORbot = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NIMPUnderXORtop = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PIMPUnderXORtop = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    _NWellUnderFF = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NWellUnderXOR = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    
                                                    
                                                    
                                                    _ViaMet22Met3OnOUT1up = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT1upIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT1up = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT1upIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT1up = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT1upIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT1up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT1up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting1up = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT2up = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT2upIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT2up = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT2upIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT2up = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT2upIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT2up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT2up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting2up = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT3up = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT3upIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT3up = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT3upIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT3up = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT3upIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT3up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT3up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting3up = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT4up = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT4upIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT4up = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT4upIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT4up = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT4upIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT4up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT4up = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting4up = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    
                                                    
                                                    
                                                    _ViaMet22Met3OnOUT4down = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT1downIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT4down = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT1downIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT4down = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT1downIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT1down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT1down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting1down = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT3down = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT2downIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT3down = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT2downIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT3down = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT2downIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT2down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT2down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting2down = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT2down = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT3downIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT2down = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT3downIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT2down = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT3downIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT3down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT3down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting3down = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    
                                                    _ViaMet22Met3OnOUT1down = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnOUT4downIn{}'.format(_Name)))[0],
                                                    _ViaMet32Met4OnOUT1down = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnOUT4downIn{}'.format(_Name)))[0],
                                                    _ViaMet42Met5OnOUT1down = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnOUT4downIn{}'.format(_Name)))[0],
                                                    _AdditionalMet3OnOUT4down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _AdditionalMet4OnOUT4down = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OutputRouting4down = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_Width=400),
                                                    

                                                    _Met4OutDownForVia2ViaConnection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_Width=400),
                                                    _Met4OutTopForVia2ViaConnection = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_Width=400),

                                                    
                                                    
                                                    
                                                    
                                                    ###PINS
                                                    _InputApin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='InputA',),
                                                    _InputBpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='InputB',),
                                                    # _VDDpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VDD',),
                                                    # _VSSpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='VSS',),
                                                    
                                                    _CLKpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLK',),
                                                    _CLKBarpin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='CLKBar',),
                                                    
                                                    _OutA1pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutA1',),
                                                    _OutA2pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutA2',),
                                                    _OutA3pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutA3',),
                                                    _OutA4pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutA4',),

                                                    _OutB1pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutB1',),
                                                    _OutB2pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutB2',),
                                                    _OutB3pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutB3',),
                                                    _OutB4pin = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='OutB4',),

                                                    _SelA1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelA1',),
                                                    _SelA2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelA2',),
                                                    _SelA3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelA3',),
                                                    _SelA4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelA4',),
                                                    
                                                    _SelAbar1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelAbar1',),
                                                    _SelAbar2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelAbar2',),
                                                    _SelAbar3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelAbar3',),
                                                    _SelAbar4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelAbar4',),
                                                    
                                                    # _SelB1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelB1',),
                                                    # _SelB2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelB2',),
                                                    # _SelB3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelB3',),
                                                    # _SelB4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelB4',),
                                                    
                                                    # _SelBbar1 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelBbar1',),
                                                    # _SelBbar2 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelBbar2',),
                                                    # _SelBbar3 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelBbar3',),
                                                    # _SelBbar4 = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0],_Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]],  _Mag=0.1, _Angle=0,    _TEXT='SelBbar4',),
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 
                                    # _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitDesign._DelayUnitDesign),
                                    _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnit._DELAYUNIT._ParametersForDesignCalculation),
                                    _NWellexpandXonFF = None, _PPexpandXonFF = None, _NPexpandXonFF = None, 
                                    _NWellexpandXonXOR = None, _PPexpandXonXOR = None, _NPexpandXonXOR = None, 
                                    
                                    _DU12DU2spacebias = None,_DU22DU3spacebias = None,_DU32DU4spacebias = None,
                                    _Outputexpand = None, _OutputWidth = None, _NumberOfOutputViaCOY = None,

                                    _MetalxDRC = None,
                                    _Outline1Location = None,_Outline2Location = None,_Outline3Location = None,_Outline4Location = None,

                                     _YbiasForTopOutputVia=None, _YbiasForBotOutputVia=None,

                                     _Dummy=DelayUnitDesign._DelayUnitDesign['_Dummy']
                                     ):
        print '#########################################################################################################'
        print '                                    {}  DelayUnitX4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'

        print 'aoc1'


        _DRCObj=DRC.DRC()
        
        while True:
            # #####################SUBSET ELEMENTS GENERATION#########################
            # DELAYUNIT GENERATION
            self._DesignParameter['_DelayUnit1']['_DesignObj']._CalculateDesignParameter(**_DelayUnitDesignCalculationParameters)
            self._DesignParameter['_DelayUnit2']['_DesignObj']._CalculateDesignParameter(**_DelayUnitDesignCalculationParameters)
            self._DesignParameter['_DelayUnit3']['_DesignObj']._CalculateDesignParameter(**_DelayUnitDesignCalculationParameters)
            self._DesignParameter['_DelayUnit4']['_DesignObj']._CalculateDesignParameter(**_DelayUnitDesignCalculationParameters)
            
            # FF IN/OUT VIA GENERATION
            
            self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
            

            # OUTPUT VIA GENERATION
            if _NumberOfOutputViaCOY is None:
                _NumberOfOutputViaCOY = 2

            self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT1up']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT2up']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT3up']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT4up']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT4down']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT3down']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT2down']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet32Met4OnOUT1down']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=_NumberOfOutputViaCOY)
            self._DesignParameter['_ViaMet42Met5OnOUT1down']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2)
            
            
            # # )#####################COORDINATION SETTING#########################
            self._DesignParameter['_DelayUnit1']['_XYCoordinates']=[ [0,0] ]

            if _Dummy is True:
                PolyDRC = _DRCObj._PolygateMinSpace
            else:
                PolyDRC = 0
            
            if _DU12DU2spacebias is None:
                _DU12DU2spacebias = 0
            if _DU22DU3spacebias is None:
                _DU22DU3spacebias = 0
            if _DU32DU4spacebias is None:
                _DU32DU4spacebias = 0
            
            #DU2 COORDINATION
            DistacneDRCbot = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
                                 
            DistacneDRCtop = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
        
            
            DelayU1BotRightSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU2BotLeftSide = self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            
            DelayU1TopRightSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU2TopLeftSide = self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            

            if _Dummy is True:
                DelayU1BotRightSide += self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU2BotLeftSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU1TopRightSide += self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU2TopLeftSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
            else:
                DelayU1BotRightSide += self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU2BotLeftSide += -self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU1TopRightSide += self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU2TopLeftSide += -self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2


            XcoordishiftBot = DelayU1BotRightSide - DelayU2BotLeftSide + DistacneDRCbot
            XcoordishiftTop = DelayU1TopRightSide - DelayU2TopLeftSide + DistacneDRCtop
            Xcoordishift = max(XcoordishiftBot,XcoordishiftTop) + _DU12DU2spacebias
            DelayU2BotLeftSide += Xcoordishift
            DelayU2TopLeftSide += Xcoordishift
            
            self._DesignParameter['_DelayUnit2']['_XYCoordinates']=[ [Xcoordishift,0] ]
                
            #DU3 COORDINATION    
            DistacneDRCbot = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
                                 
            DistacneDRCtop = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
            
            DelayU2BotRightSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU3BotLeftSide = self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            
            DelayU2TopRightSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU3TopLeftSide = self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            
            if _Dummy is True:
                DelayU2BotRightSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU3BotLeftSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU2TopRightSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU3TopLeftSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
            else:
                DelayU2BotRightSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU3BotLeftSide += -self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU2TopRightSide += self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU3TopLeftSide += -self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            
            XcoordishiftBot = DelayU2BotRightSide - DelayU3BotLeftSide + DistacneDRCbot
            XcoordishiftTop = DelayU2TopRightSide - DelayU3TopLeftSide + DistacneDRCtop
            Xcoordishift = max(XcoordishiftBot,XcoordishiftTop) + _DU22DU3spacebias
            
            self._DesignParameter['_DelayUnit3']['_XYCoordinates']=[ [Xcoordishift,0] ]
                
                
            #DU4 COORDINATION    
            DistacneDRCbot = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
                                 
            DistacneDRCtop = max( _DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,_DRCObj.DRCODMinSpace(_Width=self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'], _ParallelLength=self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'])
                                 ,PolyDRC)
            
            DelayU3BotRightSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU4BotLeftSide = self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            
            DelayU3TopRightSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]
            DelayU4TopLeftSide = self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] 
            
            if _Dummy is True:
                DelayU3BotRightSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU4BotLeftSide += self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU3TopRightSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
                DelayU4TopLeftSide += self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2
            else:
                DelayU3BotRightSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU4BotLeftSide += -self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU3TopRightSide += self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                DelayU4TopLeftSide += -self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
            
            XcoordishiftBot = DelayU3BotRightSide - DelayU4BotLeftSide + DistacneDRCbot
            XcoordishiftTop = DelayU3TopRightSide - DelayU4TopLeftSide + DistacneDRCtop
            Xcoordishift = max(XcoordishiftBot,XcoordishiftTop) + _DU32DU4spacebias
            
            self._DesignParameter['_DelayUnit4']['_XYCoordinates']=[ [Xcoordishift,0] ]
            
            coordination_calibre =  round( (max(DelayU3BotRightSide,DelayU3TopRightSide) + min(DelayU2BotLeftSide,DelayU2TopLeftSide)) / 2 / _DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] -= coordination_calibre
            self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] -= coordination_calibre
            self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] -= coordination_calibre
            self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] -= coordination_calibre
            
                
                
                
            # )################################ FF OUTPUT 2 FF INPUT CONNECTION ################################
            #)Via COORDINATION SETTING
            self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'] = [[ a+b+(c+d)/2 for a,b,c,d in zip(self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0],self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'] = [[ self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][0]
                                                                                        ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-(self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/2) ]]
            self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_XYCoordinates'] = [[ a+b+(c+d)/2 for a,b,c,d in zip(self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0],self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_XYCoordinates'] = [[ self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][0]
                                                                                        ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-(self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/2) ]]
            self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_XYCoordinates'] = [[ a+b+(c+d)/2 for a,b,c,d in zip(self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0],self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_XYCoordinates'] = [[ self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][0]
                                                                                        ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-(self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/2) ]]
            self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_XYCoordinates'][0][1] = round(self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = round(abs(self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/_DRCObj._MinSnapSpacing/2) * _DRCObj._MinSnapSpacing * 2
            
            #)Met2 Connection
            self._DesignParameter['_DU1out2DU2inBotMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU1out2DU2inBotMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU2FFBotInput']['_XYCoordinates'][0] ]]
            self._DesignParameter['_DU1out2DU2inTopMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU1out2DU2inTopMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU2FFTopInput']['_XYCoordinates'][0] ]]
            
            self._DesignParameter['_DU2out2DU3inBotMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU2out2DU3inBotMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU3FFBotInput']['_XYCoordinates'][0] ]]
            self._DesignParameter['_DU2out2DU3inTopMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU2out2DU3inTopMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU3FFTopInput']['_XYCoordinates'][0] ]]
            
            self._DesignParameter['_DU3out2DU4inBotMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU3out2DU4inBotMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFbotOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU4FFBotInput']['_XYCoordinates'][0] ]]
            self._DesignParameter['_DU3out2DU4inTopMet2Connection']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_DU3out2DU4inTopMet2Connection']['_XYCoordinates'] = [[ [self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0]+self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_FFtopOutputRoutingMet2']['_XYCoordinates'][0][0][0],self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_XYCoordinates'][0][1] ]
                                                                                         , self._DesignParameter['_ViaMet12Met2OnDU4FFTopInput']['_XYCoordinates'][0] ]]
            
            
            
            # )################################ POWER LINE METAL1 ################################

            self._DesignParameter['_PowerLine1Met1']['_Width'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'] = [[  [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]
                                                                            ,[self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]]
            
            self._DesignParameter['_PowerLine2Met1']['_Width'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'] = [[  [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]
                                                                            ,[self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]  ]]
            
            self._DesignParameter['_PowerLine3Met1']['_Width'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'] = [[  [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]
                                                                            ,[self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]]
            
            self._DesignParameter['_PowerLine4Met1']['_Width'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'] = [[  [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]
                                                                            ,[self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]  ]]
            
            self._DesignParameter['_PowerLine5Met1']['_Width'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'] = [[  [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]
                                                                            ,[self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2
                                                                             ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]]

            
            # )################################ POWER LINE OD LAYER ################################

            self._DesignParameter['_PowerLine1ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][0][0]
            self._DesignParameter['_PowerLine1ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            self._DesignParameter['_PowerLine1ODLayer']['_XYCoordinates'] = [[ (self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][1][0])/2 , self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][0][1] ]]
            
            self._DesignParameter['_PowerLine2ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][0][0]
            self._DesignParameter['_PowerLine2ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            self._DesignParameter['_PowerLine2ODLayer']['_XYCoordinates'] = [[ (self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][1][0])/2 , self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][0][1] ]]
            
            self._DesignParameter['_PowerLine3ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][0][0]
            self._DesignParameter['_PowerLine3ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            self._DesignParameter['_PowerLine3ODLayer']['_XYCoordinates'] = [[ (self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][1][0])/2 , self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][0][1] ]]
            
            self._DesignParameter['_PowerLine4ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][0][0]
            self._DesignParameter['_PowerLine4ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            self._DesignParameter['_PowerLine4ODLayer']['_XYCoordinates'] = [[ (self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][1][0])/2 , self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][0][1] ]]
            
            self._DesignParameter['_PowerLine5ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][0][0]
            self._DesignParameter['_PowerLine5ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            self._DesignParameter['_PowerLine5ODLayer']['_XYCoordinates'] = [[ (self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][0][0] + self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][1][0])/2 , self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][0][1] ]]
            
            
            
            # self._DesignParameter['_PowerLine2ODLayer']['_XWidth'] = self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][0][0]
            # self._DesignParameter['_PowerLine2ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            # self._DesignParameter['_PowerLine2ODLayer']['_XYCoordinates'] = self._DesignParameter['_PowerLine2Met1']['_XYCoordinates']

            # self._DesignParameter['_PowerLine3ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            # self._DesignParameter['_PowerLine3ODLayer']['_XYCoordinates'] = self._DesignParameter['_PowerLine3Met1']['_XYCoordinates']
            
            # self._DesignParameter['_PowerLine4ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']            
            # self._DesignParameter['_PowerLine4ODLayer']['_XYCoordinates'] = self._DesignParameter['_PowerLine4Met1']['_XYCoordinates']
            
            # self._DesignParameter['_PowerLine5ODLayer']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']
            # self._DesignParameter['_PowerLine5ODLayer']['_XYCoordinates'] = self._DesignParameter['_PowerLine5Met1']['_XYCoordinates']

            # )################################ NP, PP On POWER LINE  ################################
            PP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2 + _DRCObj._PpMinExtensiononPactive
            PP_LeftSide =  self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']/2 - _DRCObj._PpMinExtensiononPactive
            self._DesignParameter['_PowerLine1PIMP']['_XWidth'] = PP_RigthSide - PP_LeftSide
            self._DesignParameter['_PowerLine1PIMP']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_PowerLine1PIMP']['_XYCoordinates'] = [ [ (PP_RigthSide + PP_LeftSide)/2 , self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]
            
            NP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2 + _DRCObj._NpMinExtensiononNactive
            NP_LeftSide =  self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']/2 - _DRCObj._NpMinExtensiononNactive
            self._DesignParameter['_PowerLine2NIMP']['_XWidth'] = NP_RigthSide - NP_LeftSide
            self._DesignParameter['_PowerLine2NIMP']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']
            self._DesignParameter['_PowerLine2NIMP']['_XYCoordinates'] = [ [ (NP_RigthSide + NP_LeftSide)/2 , self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]  ]

            PP_RigthSide = self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][-1][0] + _DRCObj._PpMinExtensiononPactive
            PP_LeftSide = self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][0][0] - _DRCObj._PpMinExtensiononPactive
            self._DesignParameter['_PowerLine3PIMP']['_XWidth'] = PP_RigthSide - PP_LeftSide
            self._DesignParameter['_PowerLine3PIMP']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_PowerLine3PIMP']['_XYCoordinates'] = [ [ (PP_RigthSide + PP_LeftSide)/2 , self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]

            NP_RigthSide = self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][-1][0] + _DRCObj._NpMinExtensiononNactive
            NP_LefthSide = self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][0][0] - _DRCObj._NpMinExtensiononNactive
            self._DesignParameter['_PowerLine4NIMP']['_XWidth'] = NP_RigthSide - NP_LefthSide
            self._DesignParameter['_PowerLine4NIMP']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth']
            self._DesignParameter['_PowerLine4NIMP']['_XYCoordinates'] = [ [ (NP_RigthSide + NP_LefthSide)/2 , self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NbodyContact']['_XYCoordinates'][0][1] ]  ]
            
            PP_RigthSide = self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][-1][0] + _DRCObj._PpMinExtensiononPactive
            PP_LeftSide = self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][0][0] - _DRCObj._PpMinExtensiononPactive
            self._DesignParameter['_PowerLine5PIMP']['_XWidth'] = PP_RigthSide - PP_LeftSide
            self._DesignParameter['_PowerLine5PIMP']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_PowerLine5PIMP']['_XYCoordinates'] = [ [ (PP_RigthSide + PP_LeftSide)/2 , self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] ]  ]

            
            
                        
            if _NWellexpandXonFF is None:
                _NWellexpandXonFF = 0
            if _PPexpandXonFF is None:
                _PPexpandXonFF = 0
            if _NPexpandXonFF is None:
                _NPexpandXonFF = 0
            
            if _NWellexpandXonXOR is None:
                _NWellexpandXonXOR = 0
            if _PPexpandXonXOR is None:
                _PPexpandXonXOR = 0
            if _NPexpandXonXOR is None:
                _NPexpandXonXOR = 0
                
            # )################################ NP, PP On MOSFET  ################################
            NP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            NP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            self._DesignParameter['_NIMPUnderFFbot']['_XWidth'] = NP_RigthSide- NP_LeftSide + _NPexpandXonFF
            self._DesignParameter['_NIMPUnderFFbot']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']
            self._DesignParameter['_NIMPUnderFFbot']['_XYCoordinates'] = [[(NP_RigthSide+ NP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1]  ]]
            
            PP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            PP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            self._DesignParameter['_PIMPUnderFFbot']['_XWidth'] = PP_RigthSide- PP_LeftSide + _PPexpandXonFF
            self._DesignParameter['_PIMPUnderFFbot']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_YWidth']
            self._DesignParameter['_PIMPUnderFFbot']['_XYCoordinates'] = [[(PP_RigthSide+ PP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][1]  ]]
            
            NP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            NP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            self._DesignParameter['_NIMPUnderFFtop']['_XWidth'] = NP_RigthSide- NP_LeftSide + _NPexpandXonXOR
            self._DesignParameter['_NIMPUnderFFtop']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']
            self._DesignParameter['_NIMPUnderFFtop']['_XYCoordinates'] = [[(NP_RigthSide+ NP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1])  ]]
            
            PP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            PP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            self._DesignParameter['_PIMPUnderFFtop']['_XWidth'] = PP_RigthSide- PP_LeftSide + _PPexpandXonFF
            self._DesignParameter['_PIMPUnderFFtop']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_YWidth']
            self._DesignParameter['_PIMPUnderFFtop']['_XYCoordinates'] = [[(PP_RigthSide+ PP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][1])  ]]
            
            NP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            NP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            self._DesignParameter['_NIMPUnderXORbot']['_XWidth'] = NP_RigthSide- NP_LeftSide + _NPexpandXonXOR
            self._DesignParameter['_NIMPUnderXORbot']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']
            self._DesignParameter['_NIMPUnderXORbot']['_XYCoordinates'] = [[(NP_RigthSide+ NP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1]  ]]
            
            PP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            PP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            self._DesignParameter['_PIMPUnderXORbot']['_XWidth'] = PP_RigthSide- PP_LeftSide + _PPexpandXonXOR
            self._DesignParameter['_PIMPUnderXORbot']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_YWidth']
            self._DesignParameter['_PIMPUnderXORbot']['_XYCoordinates'] = [[(PP_RigthSide+ PP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][1]  ]]
            
            NP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            NP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            self._DesignParameter['_NIMPUnderXORtop']['_XWidth'] = NP_RigthSide- NP_LeftSide + _NPexpandXonXOR
            self._DesignParameter['_NIMPUnderXORtop']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']
            self._DesignParameter['_NIMPUnderXORtop']['_XYCoordinates'] = [[(NP_RigthSide+ NP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1])  ]]
            
            PP_RigthSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            PP_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XWidth']/2
            self._DesignParameter['_PIMPUnderXORtop']['_XWidth'] = PP_RigthSide- PP_LeftSide + _PPexpandXonXOR
            self._DesignParameter['_PIMPUnderXORtop']['_YWidth'] = self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_YWidth']
            self._DesignParameter['_PIMPUnderXORtop']['_XYCoordinates'] = [[(PP_RigthSide+ PP_LeftSide )/2, self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PIMPUnderPMOS']['_XYCoordinates'][0][1])  ]]
            
            
            
            
            # )################################ NWell ################################    
            NWell_UpSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][1]) + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_NWell']['_YWidth']/2
            NWell_DownSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][1] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_YWidth']/2
            NWell_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            NWell_RightSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            
            
            self._DesignParameter['_NWellUnderFF']['_XWidth'] = NWell_RightSide-NWell_LeftSide + _NWellexpandXonFF
            self._DesignParameter['_NWellUnderFF']['_YWidth'] = NWell_UpSide - NWell_DownSide
            self._DesignParameter['_NWellUnderFF']['_XYCoordinates'] = [[ (NWell_RightSide + NWell_LeftSide )/2 , (NWell_UpSide + NWell_DownSide)/2 ]]
            
            
            NWell_UpSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][1]) + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NWell']['_YWidth']/2
            NWell_DownSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][1] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_YWidth']/2
            NWell_LeftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            NWell_RightSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NWell']['_XWidth']/2
            
            
            self._DesignParameter['_NWellUnderXOR']['_XWidth'] = NWell_RightSide-NWell_LeftSide + _NWellexpandXonXOR
            self._DesignParameter['_NWellUnderXOR']['_YWidth'] = NWell_UpSide - NWell_DownSide
            self._DesignParameter['_NWellUnderXOR']['_XYCoordinates'] = [[ (NWell_RightSide + NWell_LeftSide)/2 , (NWell_UpSide + NWell_DownSide)/2 ]]
            
            
            
            
            

            # )################################ OUTPUT VIA Coordination SETTING ################################               UPside                                             
            # _MidYlocationTop = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] \
                           # +(-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1]) + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']/2)
            if _YbiasForTopOutputVia is None:
                _YbiasForTopOutputVia = 0
            _MidYlocationTop = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] \
                              +(-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1]) + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']/2)
            _MidYlocationTop = round(_MidYlocationTop / _DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing + _YbiasForTopOutputVia
            tmp = []
            
            DRCforM3 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline4Location is None:
                YlocationnHorizontal = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_XYCoordinates'][0][0][1]) -self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_Width']/2 \
                                    - self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - DRCforM3
                YlocationnParallel = YlocationnHorizontal + self._DesignParameter['_ViaMet32Met4OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - _Outline4Location
                YlocationnHorizontal = _MidYlocationTop
            self._DesignParameter['_ViaMet22Met3OnOUT1up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT1up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel  ] ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT1up']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0]  ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline4Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - _Outline3Location
                YlocationnHorizontal = _MidYlocationTop
            self._DesignParameter['_ViaMet22Met3OnOUT2up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT2up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT2up']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0]  ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline4Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - _Outline2Location
                YlocationnHorizontal = _MidYlocationTop
            self._DesignParameter['_ViaMet22Met3OnOUT3up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT3up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT3up']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0]  ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline4Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] - _Outline1Location
                YlocationnHorizontal = _MidYlocationTop
            self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ] # + (self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'])/2]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT4up']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ] #+ (self._DesignParameter['_ViaMet32Met4OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'])/2]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT4up']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT4up']['_XYCoordinates'][0]  ])
            
            self._DesignParameter['_Met4OutTopForVia2ViaConnection']['_XYCoordinates'] = tmp
            self._DesignParameter['_Met4OutTopForVia2ViaConnection']['_Width'] = _DRCObj._MetalxMinWidth
            
            # )################################ OUTPUT VIA Coordination SETTING ################################               DOWNside                                             
            if _YbiasForBotOutputVia is None:
                _YbiasForBotOutputVia = 0

            _MidYlocationBot = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] \
                           +self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][1] +self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_YWidth']/2 + _YbiasForBotOutputVia
            tmp = []
            
            DRCforM3 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline1Location is None:
                YlocationnHorizontal = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_XYCoordinates'][0][0][1] -self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_Width']/2 \
                                  - self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - DRCforM3
                YlocationnParallel = YlocationnHorizontal +  self._DesignParameter['_ViaMet32Met4OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + _Outline1Location
                YlocationnHorizontal = _MidYlocationBot
            self._DesignParameter['_ViaMet22Met3OnOUT4down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal] ]
            self._DesignParameter['_ViaMet32Met4OnOUT4down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal] ]
            self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel ] ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT4down']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0]  ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline2Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] +_Outline2Location 
                YlocationnHorizontal = _MidYlocationBot
            self._DesignParameter['_ViaMet22Met3OnOUT3down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT3down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT3down']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0]  ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline3Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] +_Outline3Location 
                YlocationnHorizontal = _MidYlocationBot
            self._DesignParameter['_ViaMet22Met3OnOUT2down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT2down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT2down']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0] ])
            
            DRCforM5 = _DRCObj._MetalxMinSpace
            Xlocation = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0]
            if _Outline4Location is None:
                YlocationnHorizontal = self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
                YlocationnParallel = self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0][1] -  self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2 - DRCforM5
            else:
                YlocationnParallel = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + _Outline4Location 
                YlocationnHorizontal = _MidYlocationBot
            self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet32Met4OnOUT1down']['_XYCoordinates'] = [ [ Xlocation , YlocationnHorizontal]  ]
            self._DesignParameter['_ViaMet42Met5OnOUT1down']['_XYCoordinates'] = [ [ Xlocation , YlocationnParallel]  ]
            tmp.append([ self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'][0] , self._DesignParameter['_ViaMet42Met5OnOUT1down']['_XYCoordinates'][0] ])
            
            self._DesignParameter['_Met4OutDownForVia2ViaConnection']['_XYCoordinates'] = tmp
            self._DesignParameter['_Met4OutDownForVia2ViaConnection']['_Width'] = _DRCObj._MetalxMinWidth

            # )################################ OUTPUT Metal Routing ################################                          UPside                                  
            if _Outputexpand is None:
                _Outputexpand = 2000
            leftSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] -  self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            RightSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XYCoordinates'][0][0] +  self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_NIMPUnderNMOS']['_XWidth']/2
            

            if _OutputWidth is None:
                _OutputWidth = _DRCObj._MetalxMinWidth
            self._DesignParameter['_OutputRouting1up']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting2up']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting3up']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting4up']['_Width'] = _OutputWidth

            self._DesignParameter['_OutputRouting1up']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting2up']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting3up']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting4up']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT4up']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT4up']['_XYCoordinates'][0][1]  ]     ]]
            
            

            self._DesignParameter['_OutputRouting1down']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting2down']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting3down']['_Width'] = _OutputWidth
            self._DesignParameter['_OutputRouting4down']['_Width'] = _OutputWidth

            self._DesignParameter['_OutputRouting1down']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting2down']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting3down']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0][1]  ]     ]]
            self._DesignParameter['_OutputRouting4down']['_XYCoordinates'] = [[ [ leftSide - _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT1down']['_XYCoordinates'][0][1]     ]   
                                                                          ,[ RightSide + _Outputexpand   ,  self._DesignParameter['_ViaMet42Met5OnOUT1down']['_XYCoordinates'][0][1]  ]     ]]
            
            
            
            # )################################ Pin ################################
            self._DesignParameter['_InputApin']['_XYCoordinates'] = [ [a + b + (c + d)/2 for a , b, c, d in zip(self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0], self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_XYCoordinates'][0], self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFbot']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1] ) ]    ]
            self._DesignParameter['_InputApin']['_XYCoordinates'][0][1] = round(self._DesignParameter['_InputApin']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_InputBpin']['_XYCoordinates'] = [ [ self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][0]  
                                                                       ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][0][1] - self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_FFtop']['_DesignObj']._DesignParameter['_InputDataRouting']['_XYCoordinates'][0][1][1])/2 ]
                                                                        ]
            self._DesignParameter['_InputBpin']['_XYCoordinates'][0][1] = round(self._DesignParameter['_InputBpin']['_XYCoordinates'][0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            
            # tmp = []
            # tmp.append( [ (a + b)/2 for a , b in zip(self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PowerLine1Met1']['_XYCoordinates'][0][1] )] )
            # tmp[0][0] = round(tmp[0][0]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # tmp.append( [(a + b)/2 for a , b in zip(self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PowerLine3Met1']['_XYCoordinates'][0][1] )] )
            # tmp[1][0] = round(tmp[1][0]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # tmp.append( [(a + b)/2 for a , b in zip(self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PowerLine5Met1']['_XYCoordinates'][0][1] )] )
            # tmp[2][0] = round(tmp[2][0]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # self._DesignParameter['_VSSpin']['_XYCoordinates'] = tmp
            
            # tmp = []
            # tmp.append( [(a + b)/2 for a , b in zip(self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PowerLine2Met1']['_XYCoordinates'][0][1] )] )
            # tmp[0][0] = round(tmp[0][0]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # tmp.append( [(a + b)/2 for a , b in zip(self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][0], self._DesignParameter['_PowerLine4Met1']['_XYCoordinates'][0][1] )] )
            # tmp[1][0] = round(tmp[1][0]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            # self._DesignParameter['_VDDpin']['_XYCoordinates'] = tmp
            
            tmp = []
            tmp.append( [ a + (b + c)/2 for a, b , c in zip (self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[0][1] = round(tmp[0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tmp.append( [ a + (b + c)/2 for a, b, c in zip (self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[1][1] = round(tmp[1][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tmp.append( [ a + (b + c)/2 for a, b,c  in zip (self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[2][1] = round(tmp[2][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tmp.append( [ a + (b + c)/2 for a, b, c in zip (self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[3][1] = round(tmp[3][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            self._DesignParameter['_CLKBarpin']['_XYCoordinates'] = tmp
            # self._DesignParameter['_CLKBarpin']['_Ignore'] = True

            tmp = []
            tmp.append( [ a + (b + c)/2 for a, b, c in zip (self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[0][1] = round(tmp[0][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tmp.append( [ a + (b + c)/2 for a, b ,c in zip (self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[1][1] = round(tmp[1][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing

            tmp.append( [ a + (b + c)/2 for a, b, c in zip (self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_CLKBarRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[2][1] = round(tmp[2][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing
            tmp.append( [ a + (b + c)/2 for a, b , c in zip (self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0],self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][0] , self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_CLKRoutingMet4']['_XYCoordinates'][0][1] ) ])
            tmp[3][1] = round(tmp[3][1]/_DRCObj._MinSnapSpacing) * _DRCObj._MinSnapSpacing

            self._DesignParameter['_CLKpin']['_XYCoordinates'] = tmp
            # self._DesignParameter['_CLKpin']['_Ignore'] = True

            self._DesignParameter['_OutA1pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting1up']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting1up']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutA2pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting2up']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting2up']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutA3pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting3up']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting3up']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutA4pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting4up']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting4up']['_XYCoordinates'][0][1] )]]
            
            self._DesignParameter['_OutB1pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting1down']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting1down']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutB2pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting2down']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting2down']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutB3pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting3down']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting3down']['_XYCoordinates'][0][1] )]]
            self._DesignParameter['_OutB4pin']['_XYCoordinates'] =[[ (a+b)/2 for a, b in zip (self._DesignParameter['_OutputRouting4down']['_XYCoordinates'][0][0] ,self._DesignParameter['_OutputRouting4down']['_XYCoordinates'][0][1] )]]

            
            
            self._DesignParameter['_SelA1']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1])    ] ]
            self._DesignParameter['_SelA1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1])    ] )
            
            self._DesignParameter['_SelA2']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1])    ] ]
            self._DesignParameter['_SelA2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1])    ] )
            
            self._DesignParameter['_SelA3']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1])    ] ]
            self._DesignParameter['_SelA3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1])    ] )
            
            self._DesignParameter['_SelA4']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1])    ] ]
            self._DesignParameter['_SelA4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1])    ] )
            
            self._DesignParameter['_SelAbar1']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1])    ] ]
            self._DesignParameter['_SelAbar1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1])    ] )
            self._DesignParameter['_SelAbar2']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1])    ] ]
            self._DesignParameter['_SelAbar2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1])    ] )
            self._DesignParameter['_SelAbar3']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1])    ] ]
            self._DesignParameter['_SelAbar3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1])    ] )
            self._DesignParameter['_SelAbar4']['_XYCoordinates'] = [ [self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1])    ] ]
            self._DesignParameter['_SelAbar4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1])    ] )
            
            self._DesignParameter['_SelA1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelA1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]    ] )
            
            self._DesignParameter['_SelA2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelA2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]    ] )
            
            self._DesignParameter['_SelA3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelA3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]    ] )
            
            self._DesignParameter['_SelA4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][0]
                                                                  ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelA4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][0]
                                                                     ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][0][1]    ] )
            
            self._DesignParameter['_SelAbar1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]    ] )
            self._DesignParameter['_SelAbar1']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelAbar2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]    ] )
            self._DesignParameter['_SelAbar2']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelAbar3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]    ] )
            self._DesignParameter['_SelAbar3']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]    ] )
            self._DesignParameter['_SelAbar4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][0]
                                                                  ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS1Gate']['_XYCoordinates'][0][1]    ] )
            self._DesignParameter['_SelAbar4']['_XYCoordinates'].append([self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][0]
                                                                     ,self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnMOS4Gate']['_XYCoordinates'][1][1]    ] )
            
            
            
            
            # # # )################################ DRC Verification ################################
            
            DRC_PASS=1
            
            #OutputVia1 Additional Met3
            Area = self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT1up']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT1up']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT1up']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5 ) *  _DRCObj._MinSnapSpacing
                self._DesignParameter['_AdditionalMet3OnOUT1up']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT1up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT1up']['_YWidth'] / _DRCObj._MinSnapSpacing /2+ 0.5 ) *  _DRCObj._MinSnapSpacing * 2
                # self._DesignParameter['_AdditionalMet3OnOUT1up']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT1up']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT1up']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT1up']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT1up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT1up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT1up']['_XYCoordinates'][0] ]
                
            Area = self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT1down']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT1down']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT1down']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5 ) *  _DRCObj._MinSnapSpacing
                self._DesignParameter['_AdditionalMet3OnOUT1down']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT1down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT1down']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5 ) *  _DRCObj._MinSnapSpacing * 2
                # self._DesignParameter['_AdditionalMet3OnOUT1down']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT4down']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT4down']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT1down']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT4down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT1down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT4down']['_XYCoordinates'][0] ]
                
                
                
            #OutputVia1 Additional Met4
            Area = self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT1up']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT1up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT1up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT1up']['_YWidth'] / _DRCObj._MinSnapSpacing /2 ) *  _DRCObj._MinSnapSpacing * 2
                self._DesignParameter['_AdditionalMet4OnOUT1up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT1up']['_XYCoordinates'][0] ] 
                
            Area = self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT1down']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT4down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT1down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT1down']['_YWidth'] / _DRCObj._MinSnapSpacing /2 ) *  _DRCObj._MinSnapSpacing * 2
                self._DesignParameter['_AdditionalMet4OnOUT1down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT4down']['_XYCoordinates'][0] ] 
                
                
            #OutputVia2 Additional Met3
            Area = self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT2up']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT2up']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT2up']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT2up']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT2up']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT2up']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT2up']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT2up']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT2up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT2up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT2up']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT2up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT2up']['_XYCoordinates'][0] ]
                
            Area = self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT2down']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT2down']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT2down']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT2down']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT3down']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT3down']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT2down']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT2down']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT3down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT2down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT2down']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT2down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT3down']['_XYCoordinates'][0] ]
                
                
            #OutputVia2 Additional Met4
            Area = self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT2up']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT2up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT2up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT2up']['_YWidth'] / _DRCObj._MinSnapSpacing /2) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT2up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT2up']['_XYCoordinates'][0] ] 
                
            Area = self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT2down']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT3down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT2down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT2down']['_YWidth'] / _DRCObj._MinSnapSpacing /2) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT2down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT3down']['_XYCoordinates'][0] ] 
                
                            
            #OutputVia3 Additional Met3
            Area = self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT3up']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT3up']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT3up']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT3up']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT3up']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT3up']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT3up']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT3up']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT3up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT3up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT3up']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT3up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT3up']['_XYCoordinates'][0] ]
            
            Area = self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT3down']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT3down']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT3down']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT3down']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT2down']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT2down']['_XYCoordinates'][0][1] - (self._DesignParameter['_AdditionalMet3OnOUT3down']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT3down']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT2down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT3down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT3down']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT3down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT2down']['_XYCoordinates'][0] ]
                
                
            #OutputVia3 Additional Met4
            Area = self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT3up']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT3up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT3up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT3up']['_YWidth'] / _DRCObj._MinSnapSpacing /2) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT3up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT3up']['_XYCoordinates'][0] ] 
             
            Area = self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT3down']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT2down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT3down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT3down']['_YWidth'] / _DRCObj._MinSnapSpacing /2) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT3down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT2down']['_XYCoordinates'][0] ] 
                
                
            #OutputVia4 Additional Met3
            Area = self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT4up']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT4up']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT4up']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT4up']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'][0][1] + (self._DesignParameter['_AdditionalMet3OnOUT4up']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT4up']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT4up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT4up']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT4up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'][0] ]

            Area = self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                # self._DesignParameter['_AdditionalMet3OnOUT4down']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                # self._DesignParameter['_AdditionalMet3OnOUT4down']['_YWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT4down']['_XWidth'] / _DRCObj._MinSnapSpacing + 0.5) *  _DRCObj._MinSnapSpacing
                # self._DesignParameter['_AdditionalMet3OnOUT4down']['_XYCoordinates'] = [[ self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'][0][1] + (self._DesignParameter['_AdditionalMet3OnOUT4down']['_YWidth'] - self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2 ]]
                self._DesignParameter['_AdditionalMet3OnOUT4down']['_YWidth'] = self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet3OnOUT4down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet3OnOUT4down']['_YWidth'] / _DRCObj._MinSnapSpacing/2 + 0.5) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet3OnOUT4down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'][0] ]
                
                
            #OutputVia4 Additional Met4
            Area = self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT4up']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT4up']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT4up']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT2up']['_YWidth'] / _DRCObj._MinSnapSpacing /2) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT4up']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT4up']['_XYCoordinates'][0] ] 
                
            Area = self._DesignParameter['_ViaMet42Met5OnOUT1down']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] * self._DesignParameter['_ViaMet42Met5OnOUT1down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
            if Area < _DRCObj._MetalxMinArea:
                self._DesignParameter['_AdditionalMet4OnOUT4down']['_YWidth'] = self._DesignParameter['_ViaMet42Met5OnOUT1down']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
                self._DesignParameter['_AdditionalMet4OnOUT4down']['_XWidth'] = round(_DRCObj._MetalxMinArea / self._DesignParameter['_AdditionalMet4OnOUT2down']['_YWidth'] / _DRCObj._MinSnapSpacing/2 ) *  _DRCObj._MinSnapSpacing*2
                self._DesignParameter['_AdditionalMet4OnOUT4down']['_XYCoordinates'] = [ self._DesignParameter['_ViaMet42Met5OnOUT1down']['_XYCoordinates'][0] ] 
                
             


            ####################################################################JUST Alert To USER ############################################################
            # #OUTPUT ROUTING VIA and MET3 DRC Check
            # DRCforM3 = _DRCObj._MetalxMinSpace
            # upSide = self._DesignParameter['_ViaMet22Met3OnOUT4up']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3OnOUT4up']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            # downSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_XYCoordinates'][0][1] + (-self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_XYCoordinates'][0][0][1]) + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORtop']['_DesignObj']._DesignParameter['_PMOSConnectionRouting']['_Width']/2
            # space = upSide - downSide
            # if space < DRCforM3:
            #     if _DelayUnitDesignCalculationParameters['_XorTopDesignCalculatrionParameters']['_HeightCalibration'] is None:
            #         _DelayUnitDesignCalculationParameters['_XorTopDesignCalculatrionParameters']['_HeightCalibration'] = 0
            #     _DelayUnitDesignCalculationParameters['_XorTopDesignCalculatrionParameters']['_HeightCalibration'] += round((DRCforM3 - space)/_DRCObj._MinSnapSpacing)* _DRCObj._MinSnapSpacing
            #     print 'DEBUG MONITOR : Your OUTPUT ROUTING VIA location Of DelayUnitX4 is not reasonable'
            #     # return 0
            #     # DRC_PASS = 0
            #
            #
            # upSide = self._DesignParameter['_ViaMet22Met3OnOUT1down']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3OnOUT1down']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']/2
            # downSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_XYCoordinates'][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_XYCoordinates'][0][0][1] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_XORbot']['_DesignObj']._DesignParameter['_NMOSConnectionRouting']['_Width']/2
            # space = upSide - downSide
            # if space < DRCforM3:
            #     if _DelayUnitDesignCalculationParameters['_XorBotDesignCalculatrionParameters']['_HeightCalibration'] is None:
            #         _DelayUnitDesignCalculationParameters['_XorBotDesignCalculatrionParameters']['_HeightCalibration'] = 0
            #     print  _DelayUnitDesignCalculationParameters['_XorBotDesignCalculatrionParameters']['_HeightCalibration']
            #     _DelayUnitDesignCalculationParameters['_XorBotDesignCalculatrionParameters']['_HeightCalibration'] += round((DRCforM3 - space)/_DRCObj._MinSnapSpacing)* _DRCObj._MinSnapSpacing
            #     print 'DEBUG MONITOR : Your OUTPUT ROUTING VIA location Of DelayUnitX4 is not reasonable'
            #     # return 0
            #     # DRC_PASS = 0
            # ##################################################################################################################################################



            #DRC Space BTW Selection Routing Met2 and Selection Routing Met2 (BTW DU1~DU )
            RoutingMet_RightSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_Width']/2
            RoutingMet_LeftSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_Width']/2
            print ' carhatt' ,RoutingMet_LeftSide , RoutingMet_RightSide
            
            RoutingMet4_RightSide = self._DesignParameter['_DelayUnit1']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_Width']/2
            RoutingMet4_LeftSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_Width']/2

            Space =  RoutingMet_LeftSide - RoutingMet_RightSide
            Space4 = RoutingMet4_LeftSide - RoutingMet4_RightSide
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU12DU2spacebias += SpaceBias
                DRC_PASS = 0
            elif Space4 < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space4)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU12DU2spacebias += SpaceBias
                DRC_PASS = 0
            
            
            #DRC Space BTW Selection Routing Met2 and Selection Routing Met2 (BTW  DU2~DU3 ) 
            RoutingMet_RightSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_Width']/2
            RoutingMet_LeftSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_Width']/2
            
            RoutingMet4_RightSide = self._DesignParameter['_DelayUnit2']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_Width']/2
            RoutingMet4_LeftSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit2']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_Width']/2

            Space =  RoutingMet_LeftSide - RoutingMet_RightSide
            Space4 = RoutingMet4_LeftSide - RoutingMet4_RightSide
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU22DU3spacebias += SpaceBias
                DRC_PASS = 0
            elif Space4 < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space4)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU22DU3spacebias += SpaceBias
                DRC_PASS = 0

            
            #DRC Space BTW Selection Routing Met2 and Selection Routing Met2 (BTW  DU3~DU4 ) 
            RoutingMet_RightSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopRightMet2']['_Width']/2
            RoutingMet_LeftSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORtopLeftMet2']['_Width']/2
            
            RoutingMet4_RightSide = self._DesignParameter['_DelayUnit3']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_XYCoordinates'][0][-1][0] + self._DesignParameter['_DelayUnit1']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotRightMet4']['_Width']/2
            RoutingMet4_LeftSide = self._DesignParameter['_DelayUnit4']['_XYCoordinates'][0][0] + self._DesignParameter['_DelayUnit4']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_XYCoordinates'][0][-1][0] - self._DesignParameter['_DelayUnit3']['_DesignObj']._DesignParameter['_SelectionRoutingXORbotLeftMet4']['_Width']/2

            Space =  RoutingMet_LeftSide - RoutingMet_RightSide
            Space4 = RoutingMet4_LeftSide - RoutingMet4_RightSide
            if Space < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU32DU4spacebias += SpaceBias
                DRC_PASS = 0
            elif Space4 < _DRCObj._MetalxMinSpace:
                SpaceBias = round((_DRCObj._MetalxMinSpace - Space4)/_DRCObj._MinSnapSpacing ) * _DRCObj._MinSnapSpacing
                
                _DU32DU4spacebias += SpaceBias
                DRC_PASS = 0
                       
                       
            if DRC_PASS==1 :
                break
            else :
                self._ResetSrefElement()
            
        
        del _DRCObj
        print '#########################################################################################################'
        print '                                    {}  DelayUnit Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'

        


if __name__=='__main__':


                
    ##############delayUnit #####################################################################
    DelayUnitX4Obj=_DELAYUNITX4(_DesignParameter=None, _Name='DelayUnitX4')
    DelayUnitX4Obj._CalculateDesignParameter(
                                     _NWellexpandXonFF = 500, _PPexpandXonFF = 300, _NPexpandXonFF = 400,
                                     _NWellexpandXonXOR = 500, _PPexpandXonXOR = 300, _NPexpandXonXOR = 400,
                                     _DelayUnitDesignCalculationParameters = copy.deepcopy(DelayUnitDesign._DelayUnitDesign),
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
                                         _Dummy=copy.deepcopy(DelayUnitDesign._DelayUnitDesign['_Dummy'])
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
    DelayUnitX4Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=DelayUnitX4Obj._DesignParameter)
    _fileName='autoDelayUnitX4_65.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=DelayUnitX4Obj._CreateGDSStream(DelayUnitX4Obj._DesignParameter['_GDSFile']['_GDSFile'])

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






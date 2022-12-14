import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import ContGeneration
import warnings
import PMOSSetofSlicer
import NMOSSetofSlicer

import DesignParameters
import user_define_exceptions

import copy
import DRC
import psubring
import random

import ftplib
import os

from ftplib import FTP
import base64


class _Slicer(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
                                        _CLKinputPMOSFinger1=None, _CLKinputPMOSFinger2=None, _PMOSFinger=None, _PMOSChannelWidth=None,
                                        _DATAinputNMOSFinger=None, _NMOSFinger=None, _CLKinputNMOSFinger=None, _NMOSChannelWidth=None, _CLKinputNMOSChannelWidth=None,
                                        _ChannelLength=None, _Dummy=False, _SLVT=False, _GuardringWidth=None, _Guardring=False,
                                        _SlicerGuardringWidth=None, _SlicerGuardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight=None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None, _PowerLine=None)


    def __init__(self, _DesignParameter=None, _Name='Slicer'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _CLKinputPMOSFinger1 = None, _CLKinputPMOSFinger2 = None, _PMOSFinger = None, _PMOSChannelWidth = None,
                                        _DATAinputNMOSFinger = None, _NMOSFinger = None, _CLKinputNMOSFinger = None, _NMOSChannelWidth = None, _CLKinputNMOSChannelWidth=None,
                                        _ChannelLength = None, _Dummy = False, _SLVT = False, _GuardringWidth = None, _Guardring = False,
                                        _SlicerGuardringWidth=None, _SlicerGuardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None, _PowerLine = None
                                 ):

            _DRCObj = DRC.DRC()
            _XYCoordinateOfPMOSSET = [[0, 0]]
            _XYCoordinateOfNMOSSET = [[0, 0]]
            _PODummyWidth = 30
            _Name = 'Slicer'
            _CLKinputPMOSFinger = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2





            ##############################################################################################################################################################
            ################################################################### PMOS SET Generation  #########################################################################
            ##############################################################################################################################################################
            # PMOS SET Generation
            _PMOSSETinputs = copy.deepcopy(PMOSSetofSlicer._PMOSWithDummyOfSlicer._ParametersForDesignCalculation)
            _PMOSSETinputs['_CLKinputPMOSFinger1'] = _CLKinputPMOSFinger1
            _PMOSSETinputs['_CLKinputPMOSFinger2'] = _CLKinputPMOSFinger2
            _PMOSSETinputs['_PMOSFinger'] = _PMOSFinger
            _PMOSSETinputs['_PMOSChannelWidth'] = _PMOSChannelWidth
            _PMOSSETinputs['_ChannelLength'] = _ChannelLength
            _PMOSSETinputs['_Dummy'] = _Dummy
            _PMOSSETinputs['_SLVT'] = _SLVT
            _PMOSSETinputs['_GuardringWidth'] = _GuardringWidth
            _PMOSSETinputs['_Guardring'] = _Guardring
            self._DesignParameter['_PMOSSET'] = self._SrefElementDeclaration(_DesignObj=PMOSSetofSlicer._PMOSWithDummyOfSlicer(_DesignParameter=None, _Name='PMOSSETIn{}'.format(_Name)))[0]
            self._DesignParameter['_PMOSSET']['_DesignObj']._CalculateDesignParameter(**_PMOSSETinputs)
            self._DesignParameter['_PMOSSET']['_XYCoordinates'] = [[0, 0+abs(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']) + \
                                                                       _GuardringWidth +_DRCObj._NwMinSpacetoNactive ]]#### + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_Width'] +_DRCObj._NwMinSpacetoNactive]]

            ##############################################################################################################################################################
            ################################################################### NMOS SET Generation  #########################################################################
            ##############################################################################################################################################################
            # NMOS SET Generation
            _NMOSSETinputs = copy.deepcopy(NMOSSetofSlicer._NMOSWithDummyOfSlicer._ParametersForDesignCalculation)
            _NMOSSETinputs['_DATAinputNMOSFinger'] = _DATAinputNMOSFinger
            _NMOSSETinputs['_NMOSFinger'] = _NMOSFinger
            _NMOSSETinputs['_CLKinputNMOSFinger'] = _CLKinputNMOSFinger
            _NMOSSETinputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOSSETinputs['_CLKinputNMOSChannelWidth'] = _CLKinputNMOSChannelWidth
            _NMOSSETinputs['_ChannelLength'] = _ChannelLength
            _NMOSSETinputs['_Dummy'] = _Dummy
            _NMOSSETinputs['_SLVT'] = _SLVT
            _NMOSSETinputs['_GuardringWidth'] = _GuardringWidth
            _NMOSSETinputs['_Guardring'] = _Guardring

            self._DesignParameter['_NMOSSET'] = self._SrefElementDeclaration(_DesignObj=NMOSSetofSlicer._NMOSWithDummyOfSlicer(_DesignParameter=None, _Name='NMOSSETIn{}'.format(_Name)))[0]
            self._DesignParameter['_NMOSSET']['_DesignObj']._CalculateDesignParameter(**_NMOSSETinputs)

            PMOS_toptmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
            PMOS_bottomtmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
            PMOS_righttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_righttmp']['_Ignore']
            PMOS_lefttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_lefttmp']['_Ignore']
            NMOS_toptmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']
            NMOS_bottomtmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
            NMOS_righttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_righttmp']['_Ignore']
            NMOS_lefttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_lefttmp']['_Ignore']
            _NMOSGuardringY=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_GuardringY']['_Ignore']

            NMOS_GuardringHeight = NMOS_toptmp - NMOS_bottomtmp
            tmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_bottomtmp
            self._DesignParameter['_NMOSSET']['_XYCoordinates'] = [[0, tmp - (int(round(NMOS_GuardringHeight + 0.5)) // 2 + _NMOSGuardringY) - _DRCObj._Metal1MinSpace3 - _GuardringWidth]]###0-abs(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']) \
                                                                        ###-_DRCObj._PpMinWidth//2]]

            #########################################################################################################################################
            ############################################### Guardring Generation for Slicer #########################################################
            #########################################################################################################################################
            print('x')
            _GuardRingRX2RXSpace = _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace

            # Horizontal Met1
            # self._DesignParameter['_SlicerGuardringMet1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # tmp=[]
            # GuardringMet1Coordinate= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
            #                            self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth//2 \
            #                            + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2]]
            # GuardringMet1Coordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
            #                             self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth//2 \
            #                            - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2]]
            # print('x')

            toptmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth//2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2
            bottomtmp = self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth//2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2

            # Vertical Met1
            # self._DesignParameter['_SlicerGuardringMet2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_SlicerGuardringMet2']['_XWidth'] = _SlicerGuardringWidth
            # self._DesignParameter['_SlicerGuardringMet2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth
            # GuardringMet1Coordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth//2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2, \
            #                             (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])//2
            #                           ]]
            # GuardringMet1Coordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth//2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2, \
            #                              (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) // 2
            #                              ]]

            lefttmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth//2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2
            righttmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth//2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2

            _GuardringCetPointX = int(round(lefttmp + righttmp + 0.5)) // 2
            _GuardringCetPointY = int(round(toptmp + bottomtmp + 0.5)) // 2
            _GuardringXWidth = int(righttmp - lefttmp - _SlicerGuardringWidth) + 2
            _GuardringYWidth = int(toptmp - bottomtmp - _SlicerGuardringWidth) + 2
            if _GuardringXWidth % 2 == 1:
                _GuardringXWidth = _GuardringXWidth + 1
            if _GuardringYWidth % 2 == 1:
                _GuardringYWidth = _GuardringYWidth + 1
            if _GuardringCetPointX % 2 == 1 :
                _GuardringCetPointX = _GuardringCetPointX
            if _GuardringCetPointY % 2 == 1 :
                _GuardringCetPointY = _GuardringCetPointY



            _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
            _NMOSSubringinputs['_PType'] = True
            _NMOSSubringinputs['_XWidth'] = _GuardringXWidth
            _NMOSSubringinputs['_YWidth'] = _GuardringYWidth
            _NMOSSubringinputs['_Width'] = _SlicerGuardringWidth

            self._DesignParameter['_Guardring'] = self._SrefElementDeclaration(
                _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='GuardringIn{}'.format(_Name)))[0]
            self._DesignParameter['_Guardring']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

            self._DesignParameter['_Guardring']['_XYCoordinates'] = [[_GuardringCetPointX, _GuardringCetPointY]]

            # self._DesignParameter['_SlicerGuardringMet1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth
            # self._DesignParameter['_SlicerGuardringMet1']['_YWidth'] = _SlicerGuardringWidth
            #
            # tmp=GuardringMet1Coordinate + GuardringMet1Coordinate1
            # tmp2=GuardringMet1Coordinate2 + GuardringMet1Coordinate3
            # self._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'] = tmp
            # self._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'] = tmp2
            # del tmp

            # Guardring OD Layer
            tmp=[]
            # Horizontal OD
            # self._DesignParameter['_SlicerGuardringOD1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # GuardringODCoordinate = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
            #                           self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth//2 \
            #                           + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2]]
            # GuardringODCoordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
            #                            self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth//2 \
            #                            - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2]]
            # tmp=GuardringODCoordinate + GuardringODCoordinate1
            # self._DesignParameter['_SlicerGuardringOD1']['_XYCoordinates'] = tmp
            #
            # # Vertical OD
            # self._DesignParameter['_SlicerGuardringOD2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_SlicerGuardringOD2']['_XWidth'] = _SlicerGuardringWidth
            # self._DesignParameter['_SlicerGuardringOD2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth
            # GuardringMet1Coordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth//2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2, \
            #                             (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])//2
            #                           ]]
            # GuardringMet1Coordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth//2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2, \
            #                              (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) // 2
            #                              ]]
            # tmp2=GuardringMet1Coordinate2 + GuardringMet1Coordinate3
            # self._DesignParameter['_SlicerGuardringOD2']['_XYCoordinates'] = tmp2
            # del tmp
            #
            # self._DesignParameter['_SlicerGuardringOD1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth
            # self._DesignParameter['_SlicerGuardringOD1']['_YWidth'] = _SlicerGuardringWidth
            #
            # # Guardring Pp Layer
            # # Horizontal Pp Layer
            # self._DesignParameter['_SlicerGuardringBP1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # GuardringPpCoordinate = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
            #                           self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth//2 \
            #                           + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2]]
            # GuardringPpCoordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
            #                            self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth//2 \
            #                            - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2]]
            # tmp = GuardringPpCoordinate + GuardringPpCoordinate1
            #
            # self._DesignParameter['_SlicerGuardringBP1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            # self._DesignParameter['_SlicerGuardringBP1']['_YWidth'] = _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            # self._DesignParameter['_SlicerGuardringBP1']['_XYCoordinates'] = tmp
            #
            # # Vertical Pp Layer
            # self._DesignParameter['_SlicerGuardringBP2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # GuardringPpCoordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth//2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth//2, \
            #                             (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])//2
            #                           ]]
            # GuardringPpCoordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth//2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth//2, \
            #                              (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) // 2
            #                              ]]
            # tmp2 = GuardringPpCoordinate2 + GuardringPpCoordinate3
            #
            # self._DesignParameter['_SlicerGuardringBP2']['_XWidth'] = _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            # self._DesignParameter['_SlicerGuardringBP2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            # self._DesignParameter['_SlicerGuardringBP2']['_XYCoordinates'] = tmp2
            #
            # # CONT Generation for Guardring
            # self._DesignParameter['_CONT1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_CONT2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #
            # self._DesignParameter['_CONT1']['_XWidth'] = _DRCObj._CoMinWidth
            # self._DesignParameter['_CONT1']['_YWidth'] = _DRCObj._CoMinWidth
            # self._DesignParameter['_CONT2']['_XWidth'] = _DRCObj._CoMinWidth
            # self._DesignParameter['_CONT2']['_YWidth'] = _DRCObj._CoMinWidth
            #
            # _XNumberOfCO1 = int((self._DesignParameter['_SlicerGuardringMet1']['_XWidth'] - 2*_SlicerGuardringWidth - 2 * _DRCObj._Metal1MinEnclosureCO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) # Horizontal Ring
            # _YNumberOfCO1 = int((_SlicerGuardringWidth- 2 * _DRCObj._Metal1MinEnclosureCO) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            # _XNumberOfCO2 = int((_SlicerGuardringWidth- 2 * _DRCObj._Metal1MinEnclosureCO) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
            # _YNumberOfCO2 = int((self._DesignParameter['_SlicerGuardringMet2']['_YWidth'] - 2*_SlicerGuardringWidth - 2 * _DRCObj._Metal1MinEnclosureCO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))  # Verical Ring
            #
            # # CONT Coordinate Setting
            # _LengthRingBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
            # tmp = []
            # tmp2=[GuardringMet1Coordinate[0][1], GuardringMet1Coordinate1[0][1]]
            # tmp3=GuardringMet1Coordinate3[0][0]+GuardringMet1Coordinate2[0][0]
            #
            # for i in range(0, _XNumberOfCO1):
            #     for j in range(0, _YNumberOfCO1):
            #         for k in tmp2:
            #             if (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 0:
            #                 _xycoordinatetmp = [(tmp3)//2 - (_XNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 1:
            #                 _xycoordinatetmp = [(tmp3)//2 - (_XNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 0:
            #                 _xycoordinatetmp = [(tmp3)//2 - (_XNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 1:
            #                 _xycoordinatetmp = [(tmp3)//2 - (_XNumberOfCO1 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
            #                                     k - (_YNumberOfCO1 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             tmp.append(_xycoordinatetmp)
            # self._DesignParameter['_CONT1']['_XYCoordinates'] = tmp
            #
            # tmp = []
            # tmp2 = [-1, 1]
            # tmp3 = GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1]
            # print('x')
            #
            # for i in range(0, _XNumberOfCO2):
            #     for j in range(0, _YNumberOfCO2):
            #         for k in tmp2:
            #             if (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 0:
            #                 _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO, \
            #                                     tmp3//2 - (_YNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #
            #             elif (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 1:
            #                 _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + i * _LengthRingBtwCO, \
            #                                     tmp3//2 - (_YNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #
            #             elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 0:
            #                 _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO, \
            #                                     tmp3//2 - (_YNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #
            #             elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 1:
            #                 _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 // 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO, \
            #                                     tmp3//2 - (_YNumberOfCO2 - 1) // 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
            #             tmp.append(_xycoordinatetmp)
            # self._DesignParameter['_CONT2']['_XYCoordinates'] = tmp

            ################################################################ Guadring VSS Generation ########################################################################################
            self._DesignParameter['_GuardringVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_GuardringVSS']['_XWidth'] = _GuardringXWidth + 2 * _SlicerGuardringWidth ####self._DesignParameter['_SlicerGuardringMet1']['_XWidth'] ###NMOS_righttmp - NMOS_lefttmp + _GuardringWidth
            self._DesignParameter['_GuardringVSS']['_YWidth'] = (self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]) - (self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]) + _GuardringWidth // 2 + _SlicerGuardringWidth // 2####(NMOS_bottomtmp+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]) - GuardringMet1Coordinate1[0][1] + _GuardringWidth
            self._DesignParameter['_GuardringVSS']['_XYCoordinates'] = [[0, ((self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] + _GuardringWidth // 2) + (self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - _SlicerGuardringWidth // 2)) // 2]]###GuardringMet1Coordinate1[0][1] + self._DesignParameter['_GuardringVSS']['_YWidth']//2 - _GuardringWidth // 2]]
            print('x')

            _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

            ##################################################################################################################################################################################
            ################################################################# NMOS VIA1 Generation ###########################################################################################
            ##################################################################################################################################################################################
            ## VIA1 Generation for Gate of Inner NMOS
            _VIAInnerNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
            if _tmpNumViaX < 2:
                _tmpNumViaX = 2
            _VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
            _VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1

            # if _NMOSChannelWidth < 400 :
            #     a = _LengthbtwViaCentertoViaCenter // 4
            # else :
            #     a = 0

            self._DesignParameter['_ViaMet12Met2OnNMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnInnerNMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerNMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][0],
                                                                                    max(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_XYCoordinates'][0][1][1] + _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace,
                                                                                   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]\
                                                                                   + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4)],
                                                                                   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][0],
                                                                                    max(self._DesignParameter[
                                                                                            '_NMOSSET'][
                                                                                            '_XYCoordinates'][0][1] +
                                                                                        self._DesignParameter[
                                                                                            '_NMOSSET'][
                                                                                            '_DesignObj']._DesignParameter[
                                                                                            '_Met2NMOS'][
                                                                                            '_XYCoordinates'][0][1][
                                                                                            1] + _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace,

                                                                                    self._DesignParameter['_NMOSSET'][
                                                                                        '_DesignObj']._DesignParameter[
                                                                                        '_VIANMOSPoly2Met1NMOS3'][
                                                                                        '_XYCoordinates'][0][1] \
                                                                                    + self._DesignParameter['_NMOSSET'][
                                                                                        '_XYCoordinates'][0][
                                                                                        1] + _LengthbtwViaCentertoViaCenter // 4)]
                                                                                  ]
            del _tmpNumViaX
            #del a

            if _NMOSChannelWidth < 400 :
                self._DesignParameter['_Metal1forGate2&3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_Metal1forGate2&3']['_XWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
                self._DesignParameter['_Metal1forGate2&3']['_YWidth'] = abs(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]\
                                                                                    + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))
                self._DesignParameter['_Metal1forGate2&3']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][0],
                                                                                 (self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] \
                                                                                + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2 - 1],
                                                                                   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][0],
                                                                                    (self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] \
                                                                                + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2 - 1]
                                                                                  ]




            # VIA1 Generation for Gate of Outer NMOS
            _VIAOuterNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
            if _tmpNumViaX < 2:
                _tmpNumViaX = 2
            _VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
            _VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnOuterNMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterNMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] ,
                                                                                    self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]
            del _tmpNumViaX
            print('x')

            ## VIA1 Generation for Gate of Outer PMOS CLK
            _VIAOuterPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
            if _tmpNumViaX < 2:
                _tmpNumViaX = 2

            _VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
            _VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnOuterPMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterPMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0],  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
                                                                                    + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                                   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
                                                                                    + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
            del _tmpNumViaX






            ## VIA1 Generation for Gate of Inner PMOS
            _VIAInnerPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) - 1
            if _tmpNumViaX < 2 :
                _tmpNumViaX = 2
            _VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
            _VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnInnerPMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerPMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                                   [self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]
            del _tmpNumViaX


            self._DesignParameter['_Met1ForGates'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met1ForGates']['_Width'] = max(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            if _NMOSFinger != 1:
                self._DesignParameter['_Met1ForGates']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]], \
                                                                            [[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2]]]
            else :
                self._DesignParameter['_Met1ForGates']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - 1]], \
                                                                            [[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - 1]]]



            self._DesignParameter['_Met1ForNMOSGates5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met1ForNMOSGates5']['_XWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            self._DesignParameter['_Met1ForNMOSGates5']['_YWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
            self._DesignParameter['_Met1ForNMOSGates5']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates']
            print('x')

            self._DesignParameter['_Met1ForPMOSGates1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met1ForPMOSGates1']['_XWidth'] = max(0, self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])###max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            self._DesignParameter['_Met1ForPMOSGates1']['_YWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
            self._DesignParameter['_Met1ForPMOSGates1']['_XYCoordinates'] =  [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                              [self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                                ]
            print('x')

            self._DesignParameter['_Met1ForPMOSGates3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met1ForPMOSGates3']['_XWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
            self._DesignParameter['_Met1ForPMOSGates3']['_YWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
            self._DesignParameter['_Met1ForPMOSGates3']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates']
            print('x')


            ## VIA2 Generation of Inner PMOS Drain and Inner NMOS Drain for PMOSSET, NMOSSET Connection
            _VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)

            _VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1

            _tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _tmpNumY < 1:
                _tmpNumY = 1
            # if 400 <= _NMOSChannelWidth < 800:
            #     _tmpNumY = _tmpNumY - 1
            #     if _tmpNumY < 1:
            #         _tmpNumY = 1
            _VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _tmpNumY

            self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
            self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4],
                                                                                    [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4]]








            _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

            _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1

            _tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _tmpNumY < 1 :
                _tmpNumY = 1
            # if 400 <= _NMOSChannelWidth < 800:
            #     _tmpNumY = _tmpNumY - 1
            #     if _tmpNumY < 1 :
            #         _tmpNumY = 1
            _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumY


            self._DesignParameter['_ViaMet22Met3OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates']=[
                                                                                  # [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
                                                                                  # self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
                                                                                  # + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0],
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],

                                                                                  # [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
                                                                                  #  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
                                                                                  #  + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), \
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
                                                                                  ]]
            print('x')

            _VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
            _tmpNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 1
            if _tmpNumY < 1 :
                _tmpNumY = 1
            _VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumY
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)
            self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
                                                                                  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
                                                                                  + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
                                                                                     [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]




            if self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] :
                self._DesignParameter['_AdditionalMet3forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_AdditionalMet3forArea']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
                self._DesignParameter['_AdditionalMet3forArea']['_YWidth'] = _DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] + 1
                self._DesignParameter['_AdditionalMet3forArea']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]



            ## VIA3 Generation of Inner PMOS Drain and Inner NMOS Drain for PMOSSET, NMOSSET Connection
            _VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)

            _VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1

            _tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            if _tmpNumY < 1 :
                _tmpNumY = 1
            # if 400 <= _NMOSChannelWidth < 800:
            #     _tmpNumY = _tmpNumY - 1
            #     if _tmpNumY < 1 :
            #         _tmpNumY = 1
            _VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _tmpNumY


            self._DesignParameter['_ViaMet32Met4OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIANMOSMet34)
            self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates']=[
                                                                                  # [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
                                                                                  # self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
                                                                                  # + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0],
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],

                                                                                  # [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
                                                                                  #  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
                                                                                  #  + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), \
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
                                                                                  ]]
            print('x')



            if (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea) :

                _LengthNMOSSpaceBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength - _DRCObj._Metal1MinWidth
                _SpaceMet12Met1 = 2 * _LengthNMOSSpaceBtwMet1 + _DRCObj._Metal1MinWidth

                self._DesignParameter['_Met2OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'] = _SpaceMet12Met1 - 2 * _DRCObj._MetalxMinSpace2
                self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] = _DRCObj._MetalxMinArea // self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'] + 1
                self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] // 2 + self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2], \
                                                                                  [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] // 2 + self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2]]

                self._DesignParameter['_Met3OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_Met3OnNMOS4forArea']['_XWidth'] = _SpaceMet12Met1 - 2 * _DRCObj._MetalxMinSpace2
                self._DesignParameter['_Met3OnNMOS4forArea']['_YWidth'] = _DRCObj._MetalxMinArea // self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'] + 1
                self._DesignParameter['_Met3OnNMOS4forArea']['_XYCoordinates'] = self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates']

                # self._DesignParameter['_Met4OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                # self._DesignParameter['_Met4OnNMOS4forArea']['_XWidth'] = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                # self._DesignParameter['_Met4OnNMOS4forArea']['_YWidth'] = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
                # self._DesignParameter['_Met4OnNMOS4forArea']['_XYCoordinates'] = self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates']











            _VIAPMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _VIAPMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
            _tmpNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 1
            if _tmpNumY < 1 :
                _tmpNumY = 1
            _VIAPMOSMet34['_ViaMet32Met4NumberOfCOY'] = _tmpNumY
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnPMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAPMOSMet34)
            self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \

                                                                                   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
                                                                                    + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                                   ]








            ## VIA2 Generation of Outer PMOS and NMOS for CLK routing Connection
            _VIAPMOSMet23CLKinput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
            if _tmpNumViaX < 2 :
                _tmpNumViaX = 2

            _VIAPMOSMet23CLKinput['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
            _VIAPMOSMet23CLKinput['_ViaMet22Met3NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnPMOSCLKInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23CLKinput)
            self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0]
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0]
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
            del _tmpNumViaX
            print('x')

            _VIANMOSMet23CLKinput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)
            if _tmpNumViaX < 2:
                _tmpNumViaX = 2

            _VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
            _VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSCLKInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23CLKinput)
            self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'] = [self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates'][0]

                                                                                  # [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0]
                                                                                  #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],
                                                                                  #  self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] \
                                                                                  #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]] # NMOS CLK input
                                                                                 ]
            del _tmpNumViaX

            _LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
            _VIANMOSMet23input = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

            if _DATAinputNMOSFinger > 1:
                _tmpNumViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
                if _tmpNumViaX < 2:
                    _tmpNumViaX = 2

                _VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
                _VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23input)
                self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 // 2, \
                                                                                    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
                                                                                    [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinSpace3 // 2, \
                                                                                     self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
                                                                                   # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
                                                                                   #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2],
                                                                                   # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
                                                                                   #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]
                                                                                    ]
                del _tmpNumViaX

            elif _DATAinputNMOSFinger == 1 :
                _VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = 2
                _VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23input)
                self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, \
                                                                                    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
                                                                                    [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, \
                                                                                     self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
                                                                                   # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
                                                                                   #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2],
                                                                                   # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
                                                                                   #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]
                                                                                    ]





            del _VIANMOSMet23input


            # _VIANMOSMet23input = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            # if _DATAinputNMOSFinger > 1 :
            #     _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1
            #     if _tmpNumViaX < 2 :
            #         _tmpNumViaX = 2
            #
            #     _VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
            #     _VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='LowerViaMet22Met3OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23input)
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [
            # #                                                                        [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            # #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
            # #                                                                         [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            # #                                                                          self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
            #                                                                         [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2],
            #                                                                        [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinSpace3, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]
            #                                                                        ]
            #
            #
            #     del _tmpNumViaX
            #                                                                       # [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0]
            #                                                                       #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],
                                                                                  #  self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] \
                                                                                  #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]] # NMOS CLK input
            # if _DATAinputNMOSFinger == 1:
            #     _VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = 1
            #     _VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='LowerViaMet22Met3OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23input)
            #     self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [
            #                                                                                 [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            #                                                                                  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
            #                                                                                 [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            #                                                                                  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_LowerViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]
            #     ]

#            del _VIANMOSMet23input




            # _VIANMOSMet34input = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # if _DATAinputNMOSFinger > 1 :
            #     _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1
            #     if _tmpNumViaX < 2:
            #         _tmpNumViaX = 2
            #
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOX'] = _tmpNumViaX
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34input)
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
            #                                                                         [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinSpace3, \
            #                                                                          self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
            #                                                                        # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            #                                                                        #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2],
            #                                                                        # [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            #                                                                        #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]
            #                                                                         ]
            #     del _tmpNumViaX
            #
            # elif _DATAinputNMOSFinger == 1 :
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOX'] = 2
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34input)
            #     self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0]- self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
            #                                                                         [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, \
            #                                                                          self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
            #                                                                                 ]
            #
            #
            #
            # del _VIANMOSMet34input



            # _VIANMOSMet34input = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # if _DATAinputNMOSFinger > 1 :
            #     _tmpNumViaX = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1
            #     if _tmpNumViaX < 1 :
            #         _tmpNumViaX = 1
            #
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOX'] = _tmpNumViaX
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='LowerViaMet32Met4OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34input)
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_XYCoordinates'] = [
            #                                                                        #  [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            #                                                                        #  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2],
            #                                                                        #  [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            #                                                                        #   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2], \
            #                                                                         [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2],
            #                                                                        [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]
            #                                                                        ]
            #     del _tmpNumViaX

            # if _DATAinputNMOSFinger == 1 :
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOX'] = 1
            #     _VIANMOSMet34input['_ViaMet32Met4NumberOfCOY'] = 2
            #
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='LowerViaMet32Met4OnNMOSInputIn{}'.format(_Name)))[0]
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIANMOSMet34input)
            #     self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_XYCoordinates'] = [
            #                                                                                 [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0], \
            #                                                                                  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
            #                                                                                 [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0], \
            #                                                                                  self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_LowerViaMet32Met4OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]
            #                                                                                 ]







                                                                                  # [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0]
                                                                                  #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],
                                                                                  #  self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] \
                                                                                  #  + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]] # NMOS CLK input
       #     del _VIANMOSMet34input






            ########################################################################################################################################################
            ########################################################## Routing Generation ##########################################################################
            ########################################################################################################################################################

            ############################################# CLK input PMOS1 Drain + Data intput NMOS Drain Met2 Routing ###############################################
            #PMOSxycoordinate=[]
            #NMOSxycoordinate=[]
            # self._DesignParameter['_Met2Slicer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met2Slicer']['_Width'] = _DRCObj._MetalxMinWidth
            # # k = len(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'])

            # self._DesignParameter['_Met2Slicer']['_XYCoordinates'] =[
            #                                                          [
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1]+(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])//2-_DRCObj._MetalxMinWidth//2+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1]+(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])//2-_DRCObj._MetalxMinWidth//2+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
            #                                                          ],
            #                                                          [
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][-1][1] + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) // 2 - _DRCObj._MetalxMinWidth // 2 + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][-1][1] + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) // 2 - _DRCObj._MetalxMinWidth // 2 + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
            #                                                           ],
            #                                                         ]

            print('x')

            #####################################################################################################################################################
            ########################################################### PMOS Met2 Routing #######################################################################
            #####################################################################################################################################################

            ########################################### CLK input PMOS1 Btw Drains Connection ############################################
            self._DesignParameter['_Met2PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

            if (_CLKinputPMOSFinger1 % 2) == 0:
                k = int(_CLKinputPMOSFinger1//2)
            elif (_CLKinputPMOSFinger1 % 2) == 1:
                k = int((float(_CLKinputPMOSFinger1)//float(2)) + 0.5)

            if (_CLKinputPMOSFinger1 % 2) == 1:
                self._DesignParameter['_Met2PMOS1']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
                                                                         ]
                                                                        ]
            elif (_CLKinputPMOSFinger1 % 2) == 0:
                self._DesignParameter['_Met2PMOS1']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1) - _LengthPMOSBtwMet1,
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Right PMOS Drain Connection
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1)+ _LengthPMOSBtwMet1,
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Left PMOS Drain Connection
                                                                         ]
                                                                        ]
            print('x')

            self._DesignParameter['_Met3PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

            if (_CLKinputPMOSFinger1 % 2) == 0:
                k = int(_CLKinputPMOSFinger1//2)
            elif (_CLKinputPMOSFinger1 % 2) == 1:
                k = int((float(_CLKinputPMOSFinger1)//float(2)) + 0.5)

            if (_CLKinputPMOSFinger1 % 2) == 1:
                self._DesignParameter['_Met3PMOS1']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
                                                                         ]
                                                                        ]
            elif (_CLKinputPMOSFinger1 % 2) == 0:
                self._DesignParameter['_Met3PMOS1']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1) - _LengthPMOSBtwMet1,
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Right PMOS Drain Connection
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1)+ _LengthPMOSBtwMet1,
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Left PMOS Drain Connection
                                                                         ]
                                                                        ]
            print('x')

            self._DesignParameter['_Met4PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
            _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

            if (_CLKinputPMOSFinger1 % 2) == 0:
                k = int(_CLKinputPMOSFinger1 // 2)
            elif (_CLKinputPMOSFinger1 % 2) == 1:
                k = int((float(_CLKinputPMOSFinger1) // float(2)) + 0.5)

            if (_CLKinputPMOSFinger1 % 2) == 1:
                self._DesignParameter['_Met4PMOS1']['_XYCoordinates'] = [
                    [
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][0][0],
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][k - 1][0],
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                        # Right
                    ],
                    [
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][-1][0],
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
                             '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                        # Right
                    ]
                ]
            elif (_CLKinputPMOSFinger1 % 2) == 0:
                self._DesignParameter['_Met4PMOS1']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1) - _LengthPMOSBtwMet1,
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                        # CLK input Right PMOS Drain Connection
                    ],
                    [
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                        [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1) + _LengthPMOSBtwMet1,
                         self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                        # CLK input Left PMOS Drain Connection
                    ]
                ]
            print('x')


            ################################################# Inner CLK input PMOS2 Drain --- Inner PMOS Drain Connection ###############################################
            self._DesignParameter['_Met2PMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2PMOS2']['_Width'] = _DRCObj._MetalxMinWidth
            k = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'])
            j = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'])

            print('x')

            if (_CLKinputPMOSFinger2 % 2) == 1:
                self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2)-1)][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j // 2) - 1)][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k // 2))][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j // 2))][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ]
                                                                        ]
            elif (_CLKinputPMOSFinger2 % 2) == 0:
                self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2)-1)][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j//2)-1)][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2))][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j//2))][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ]
                                                                        ]


            ######################################################################################################################################################################
            ########################################################################### Met3 Routing #############################################################################
            ######################################################################################################################################################################
            ################################################ Met3 Routing Generation for CLK input PMOS2 --- Inner PMOS Connection ###############################################
            PMOS_bottomtmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
            NMOS_toptmp = self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']

            self._DesignParameter['_Met4PNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4PNMOS']['_Width'] = 2 * _DRCObj._MetalxMinWidth

            self._DesignParameter['_Met4PNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], (PMOS_bottomtmp + NMOS_toptmp) // 2], ###### (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], (PMOS_bottomtmp + NMOS_toptmp) // 2], ##### (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]],
                                                                    [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1][0], (PMOS_bottomtmp + NMOS_toptmp) // 2],##### (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], (PMOS_bottomtmp + NMOS_toptmp) // 2], ##### (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2],
                                                                      [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]]]
            ################################################ Met3 Routing Generation for CLK input // Outer PMOS1---PMOS2---NMOS5 ###############################################
            self._DesignParameter['_Met3CLKinput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3CLKinput']['_Width'] = 2 * _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met3CLKinput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
                                                                         [min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]],



                                                                        [[-(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2), self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],###self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1]],
                                                                         [-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]###self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1]],

                                                                         ],
                                                                        [[min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2],
                                                                         [-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]]]

                                                                        # [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth, self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1]],
                                                                        # [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth), self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1]]]]



            self._DesignParameter['_Met4CLKinput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4CLKinput']['_Width'] = 2 * _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met4CLKinput']['_XYCoordinates'] = [[[min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2], [min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2]],###self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
                                                                        [[-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2], [-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2]]] ###self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]]]

                                                                       #  [[[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth], \
                                                                       #   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
                                                                       #  [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth],
                                                                       #   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
                                                                       #  [[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]), self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth], \
                                                                       #   [-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
                                                                       #  [[-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth],
                                                                       #   [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
                                                                       # ]



            # if (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) > _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace4 :
            #     self._DesignParameter['_Met3CLKinput']['_XYCoordinates'].append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                                      [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]])
            #
            #     _VIAOnNMOS12Met34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            #
            #     _VIAOnNMOS12Met34['_ViaMet32Met4NumberOfCOX'] = 2
            #     _VIAOnNMOS12Met34['_ViaMet32Met4NumberOfCOY'] = 1
            #
            #     self._DesignParameter['_ViaMet32Met4OnNMOS12'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAOnNMOS12Met34In{}'.format(_Name)))[0]
            #     self._DesignParameter['_ViaMet32Met4OnNMOS12']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAOnNMOS12Met34)
            #     self._DesignParameter['_ViaMet32Met4OnNMOS12']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_ViaMet32Met4OnNMOS12']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]],\
            #                                                                         [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_ViaMet32Met4OnNMOS12']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                                         [-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] + self._DesignParameter['_ViaMet32Met4OnNMOS12']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                                         [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_ViaMet32Met4OnNMOS12']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]
            #                                                                         ]
            #
            #
            # else :
            #     self._DesignParameter['_Met4CLKinput']['_XYCoordinates'].append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                                      [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]]])



            # self._DesignParameter['_Met4CLKinput']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][int((_CLKinputPMOSFinger1 - 1) // 2)][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2, self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth], \
            #                                                              [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][int((_CLKinputPMOSFinger1 - 1) // 2)][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                              [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]],
            #                                                              [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
            #                                                             [[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][int((_CLKinputPMOSFinger1 - 1) // 2)][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2), self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinWidth], \
            #                                                              [-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][int((_CLKinputPMOSFinger1 - 1) // 2)][0] + _DRCObj._MetalxMinWidth // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]], \
            #                                                              [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]],
            #                                                              [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace21 + self._DesignParameter['_Met4CLKinput']['_Width'] // 2), self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
            #
            #                                                             ]



            _VIANMOSMet34inner = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _tmpNumViaX = int(abs((self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0] - self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0] - self._DesignParameter['_Met4CLKinput']['_Width'] - 2 * _DRCObj._MetalxMinSpace21) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))

            ### int(abs((self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][3][0] - self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][3][0] - self._DesignParameter['_Met4CLKinput']['_Width'] - 2 * _DRCObj._MetalxMinSpace21) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))

            _VIANMOSMet34inner['_ViaMet32Met4NumberOfCOX'] = _tmpNumViaX
            _VIANMOSMet34inner['_ViaMet32Met4NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet32Met4OnNMOSInner'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnNMOSInnerIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34inner)
            self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_XYCoordinates'] = [[0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]]

            del _tmpNumViaX

            _VIANMOSMet23inner = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _tmpNumViaX = int(abs((self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0] - self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0] - self._DesignParameter['_Met4CLKinput']['_Width'] - 2 * _DRCObj._MetalxMinSpace21) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))

            _VIANMOSMet23inner['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
            _VIANMOSMet23inner['_ViaMet22Met3NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet22Met3OnNMOSInner'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSInnerIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSInner']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23inner)
            self._DesignParameter['_ViaMet22Met3OnNMOSInner']['_XYCoordinates'] = [[0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2]]

            #                                                               [[[(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth), self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Met4CLKinput']['_Width'] // 2],\
            #                                                             [(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth), self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth]], \
            #                                                             [[-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth), self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - _DRCObj._MetalxMinWidth], \
            #                                                             [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 - 2 * _DRCObj._MetalxMinWidth), self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Met4CLKinput']['_Width'] // 2]]]


            _VIAMet32Met4OnforCLKRouting = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _VIAMet32Met4OnforCLKRouting['_ViaMet32Met4NumberOfCOX'] = 1
            _VIAMet32Met4OnforCLKRouting['_ViaMet32Met4NumberOfCOY'] = 2

            self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAMet32Met3OnforPNRouting{}'.format(_Name)))[0]
            self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAMet32Met4OnforCLKRouting)
            self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_XYCoordinates'] =  [[self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                         [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                         [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                         [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]]




                                                                                        # [[self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                        #  [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][3][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][3][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                        #  [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2], \
                                                                                        #  [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][3][0], self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][3][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]]

            print('x')

            ########################################### Met2 Routing Generation for Inner PMOS Gate --- Inner NMOS Gate Connection (Cross-coupled) ##########################################
            self._DesignParameter['_ThickMet2PNMOSGate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_ThickMet2PNMOSGate']['_Width'] = 2 * _DRCObj._MetalxMinWidth
            if (_PMOSFinger < _NMOSFinger):
                self._DesignParameter['_ThickMet2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0],
                                                                                  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2], \
                                                                                  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2], \
                                                                                   self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0]],

                                                                                  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1],
                                                                                  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2], \
                                                                                  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2], \
                                                                                   self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1]]]


            elif (_PMOSFinger >= _NMOSFinger):
                self._DesignParameter['_ThickMet2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0],
                                                                                  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2], \
                                                                                  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2], \
                                                                                   self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0]],


                                                                             [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1],
                                                                             [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2],\
                                                                             [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2],\
                                                                              self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1]]

                                                                            ]


            ########################################### Met4 Routing Generation for CLK PMOS//NMOS Drain --- Inner PMOS//NMOS Drain Connection ##########################################
            self._DesignParameter['_Met4PNMOSDrain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4PNMOSDrain']['_Width'] = _DRCObj._MetalxMinWidth
            tmp = []
            for i in range(0, int(_CLKinputPMOSFinger1 + 1) // 2) :
                # if (self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][0] < self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2) :
                #     continue

                # else :
                # tmp.append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
                #             [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][1]], \
                #             [self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][1]]])
                # tmp.append([[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
                #             [-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]),  self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][1]], \
                #             [-(self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][0]), self._DesignParameter['_ViaMet32Met4OnNMOSInput']['_XYCoordinates'][0][1]]])


                tmp.append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
                            [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])

                tmp.append([[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
                            [-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]),  self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])


            self._DesignParameter['_Met4PNMOSDrain']['_XYCoordinates'] = tmp
            del tmp

            self._DesignParameter['_Met3PNMOSDrainRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] = _DRCObj._MetalxMinWidth
            tmp = []
            tmp.append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], [self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])
            tmp.append([[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][0][0]), self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], [-(self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][0]), self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])

            self._DesignParameter['_Met3PNMOSDrainRouting']['_XYCoordinates'] = tmp

            del tmp

            _ViaMet324PNMOSDrain = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaMet324PNMOSDrain['_ViaMet32Met4NumberOfCOX'] = 1
            _ViaMet324PNMOSDrain['_ViaMet32Met4NumberOfCOY'] = 2

            self._DesignParameter['_ViaMet324PNMOSDrain'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet324PNMOSDrainIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet324PNMOSDrain)

            tmp = []

            for i in range(0, int(_CLKinputPMOSFinger1 + 1) // 2) :
                tmp.append([self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 - self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] // 2])
                tmp.append([-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]), self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 - self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] // 2])


            self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'] = tmp

            del tmp


            self._DesignParameter['_Met4NMOS5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)

            if _DATAinputNMOSFinger > 1 :
                # if _CLKinputNMOSFinger % 2 == 1 :
                #     self._DesignParameter['_Met4NMOS5']['_Width'] = 7 // 2 * _DRCObj._MetalxMinWidth
                #     self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [#[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                #                                                             #[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                #                                                             [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]]]


                if _CLKinputNMOSFinger % 4 != 2 :
                    self._DesignParameter['_Met4NMOS5']['_Width'] = 3 * _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinWidth // 2 + 2
                    self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [#[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                                                                            #[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                                                                            [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]]]
                elif _CLKinputNMOSFinger % 4 == 2 :
                    self._DesignParameter['_Met4NMOS5']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                    self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [#[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                                                                            #[[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                                                                            [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] - _DRCObj._PolygateMinWidth - _DRCObj._PolygateMinSpace - _DRCObj._MetalxMinWidth // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] - _DRCObj._PolygateMinWidth - _DRCObj._PolygateMinSpace - _DRCObj._MetalxMinWidth // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]], \
                                                                             [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + _DRCObj._PolygateMinWidth + _DRCObj._PolygateMinSpace + _DRCObj._MetalxMinWidth // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + _DRCObj._PolygateMinWidth + _DRCObj._PolygateMinSpace + _DRCObj._MetalxMinWidth // 2, self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]]]





            elif _DATAinputNMOSFinger == 1:
                self._DesignParameter['_Met4NMOS5']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]], \
                                                                         [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2]]]


            #####################################################################################################################################################
            ############################################################# Pin Declaration #######################################################################
            #####################################################################################################################################################
            self._DesignParameter['_PinVDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
            self._DesignParameter['_PinVSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
            self._DesignParameter['_PinInputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp')
            self._DesignParameter['_PinInputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn')
            self._DesignParameter['_PinOutputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSp')
            self._DesignParameter['_PinOutputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSn')
            self._DesignParameter['_PinCLK'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK')

            self._DesignParameter['_PinVDD']['_XYCoordinates'] = [[0, PMOS_toptmp+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_PinVSS']['_XYCoordinates'] = [[0, NMOS_bottomtmp+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_PinInputP']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
                                                                      self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
            self._DesignParameter['_PinInputN']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0],
                                                                      self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]

            self._DesignParameter['_PinOutputN']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0]]
            self._DesignParameter['_PinOutputP']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]
            self._DesignParameter['_PinCLK']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0],
                                                                   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                 ]

            print('x221')
            pass


            # self._DesignParameter['_AdditionalMet3OnPMOSCLKinputGate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_AdditionalMet3OnPMOSCLKinputGate']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
            # self._DesignParameter['_AdditionalMet3OnPMOSCLKinputGate']['_YWidth'] = 2 * _DRCObj._MetalxMinWidth
            # self._DesignParameter['_AdditionalMet3OnPMOSCLKinputGate']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0]
            #                                                                        + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]],
            #                                                                        # self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
            #                                                                        # + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
            #
            #                                                                       [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0]
            #                                                                        + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]]
            #                                                                        # self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
            #                                                                        # + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]

            # self._DesignParameter['_AdditionalMet3OnNMOSCLKinputGate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_AdditionalMet3OnNMOSCLKinputGate']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
            # self._DesignParameter['_AdditionalMet3OnNMOSCLKinputGate']['_YWidth'] = 2 * _DRCObj._MetalxMinWidth
            # self._DesignParameter['_AdditionalMet3OnNMOSCLKinputGate']['_XYCoordinates'] = self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates']


            if _PMOSFinger % 2 == 1 :
                _VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAPMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
                self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]

                self._DesignParameter['_CrossPMOSMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossPMOSMet3Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossPMOSMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]



                _VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAPMOSMet34forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_VIAPMOSMet34Routing)
                self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] - self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinWidth, (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]



                self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIAPMOSMet23Routing


            elif _PMOSFinger == 2 :
                _VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAPMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
                self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]

                _VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAPMOSMet34forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIAPMOSMet34Routing)
                self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]





                self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIAPMOSMet23Routing


            else :
                _VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIAPMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
                self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]

                _VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIAPMOSMet34forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIAPMOSMet34Routing)
                self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]




                self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], (3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIAPMOSMet23Routing




            if _NMOSFinger % 2 == 1 :
                _VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIANMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
                self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]

                self._DesignParameter['_CrossNMOSMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossNMOSMet3Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossNMOSMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]


                _VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIANMOSMet34orRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_VIANMOSMet34Routing)
                self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] + self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 - _DRCObj._MetalxMinWidth, (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]



                self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIANMOSMet23Routing


            elif _NMOSFinger == 2 :
                _VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIANMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
                self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]


                _VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIANMOSMet34orRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34Routing)
                self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]


                self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIANMOSMet23Routing


                self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]





            else :
                _VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
                _VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='VIANMOSMet23forRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
                self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]

                _VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
                _VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
                self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='VIANMOSMet34orRoutingIn{}'.format(_Name)))[0]
                self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34Routing)
                self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4]]



                self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
                self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
                self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], (self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4], \
                                                             self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]

                del _VIANMOSMet23Routing


            self._DesignParameter['_AdditionalMet3Layer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_AdditionalMet3Layer']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_AdditionalMet3Layer']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], \
                                                                                [self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][-2][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]], \
                                                                               [[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], \
                                                                                [self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][-1][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]]
                                                                               ]

            self._DesignParameter['_AdditionalMet3Layer2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_AdditionalMet3Layer2']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
            self._DesignParameter['_AdditionalMet3Layer2']['_YWidth'] = self._DesignParameter['_Met3CLKinput']['_Width']
            self._DesignParameter['_AdditionalMet3Layer2']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_AdditionalMet3Layer2']['_YWidth'] // 2 - self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2]]




            if _PowerLine == True :
                Ptoptmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1]
                Gtoptmp = self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] ### self._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'][0][1]

                self._DesignParameter['_SupplyLineMet2VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
                self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
                self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates'] ###[[0, GuardringMet1Coordinate1[0][1] + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                self._DesignParameter['_SupplyLineMet3VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_SupplyLineMet3VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
                self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
                self._DesignParameter['_SupplyLineMet3VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates'] # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                # self._DesignParameter['_SupplyLineMet4VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                # self._DesignParameter['_SupplyLineMet4VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
                # self._DesignParameter['_SupplyLineMet4VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
                # self._DesignParameter['_SupplyLineMet4VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates'] # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]
                #
                # self._DesignParameter['_SupplyLineMet5VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                # self._DesignParameter['_SupplyLineMet5VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
                # self._DesignParameter['_SupplyLineMet5VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
                # self._DesignParameter['_SupplyLineMet5VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates'] # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                _ViaNumVSSX12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                _ViaNumVSSY12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                _ViaNumVSSX23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                _ViaNumVSSY23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

                # _ViaNumVSSX12 = int(self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4
                # _ViaNumVSSX23 = int(self._DesignParameter['_SupplyLineMet3VSS']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4
                # # _ViaNumVSSX34 = int(self._DesignParameter['_SupplyLineMet4VSS']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4
                # _ViaNumVSSX45 = int(self._DesignParameter['_SupplyLineMet5VSS']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 4

                if _ViaNumVSSX12 <= 1 :
                    _ViaNumVSSX12 = 1
                    _ViaNumVSSY12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                if _ViaNumVSSY12 <= 1:
                    _ViaNumVSSY12 = 1
                    _ViaNumVSSX12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                if _ViaNumVSSX23 <= 1 :
                    _ViaNumVSSX23 = 1
                    _ViaNumVSSY23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                if _ViaNumVSSY23 <= 1:
                    _ViaNumVSSY23 = 1
                    _ViaNumVSSX23 = int((self._DesignParameter['_SupplyLineMet3VSS'][ '_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                # if _ViaNumVSSX34 < 1 :
                #     _ViaNumVSSX34 = 1
                # if _ViaNumVSSX45 < 1 :
                #     _ViaNumVSSX45 = 1


                # _ViaNumVSSY12 = int(self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
                # _ViaNumVSSY23 = int(self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
                # _ViaNumVSSY34 = int(self._DesignParameter['_SupplyLineMet4VSS']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
                # _ViaNumVSSY45 = int(self._DesignParameter['_SupplyLineMet5VSS']['_YWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))


                # if _ViaNumVSSY34 < 1 :
                #     _ViaNumVSSY34 = 1
                # if _ViaNumVSSY45 < 1 :
                #     _ViaNumVSSY45 = 1


                _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVSSX12
                _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVSSY12
                self._DesignParameter['_ViaMet12Met2VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2VSSIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2VSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVSSMet12Met2)
                self._DesignParameter['_ViaMet12Met2VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']

                _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX23
                _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVSSY23
                self._DesignParameter['_ViaMet22Met3VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3VSSIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet22Met3VSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVSSMet22Met3)
                self._DesignParameter['_ViaMet22Met3VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']

                # _ViaVSSMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                # _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVSSX34
                # _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVSSY34
                # self._DesignParameter['_ViaMet32Met4VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4VSSIn{}'.format(_Name)))[0]
                # self._DesignParameter['_ViaMet32Met4VSS']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met4)
                # self._DesignParameter['_ViaMet32Met4VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']
                #
                # _ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
                # _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ViaNumVSSX45
                # _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ViaNumVSSY45
                # self._DesignParameter['_ViaMet42Met5VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5VSSIn{}'.format(_Name)))[0]
                # self._DesignParameter['_ViaMet42Met5VSS']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met5)
                # self._DesignParameter['_ViaMet42Met5VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']





                _LengthofSupplyLine = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth']


                self._DesignParameter['_SupplyLineMet2VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_SupplyLineMet2VDD']['_XWidth'] = _LengthofSupplyLine
                self._DesignParameter['_SupplyLineMet2VDD']['_YWidth'] = _GuardringWidth
                self._DesignParameter['_SupplyLineMet2VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]] ###[[0, GuardringMet1Coordinate1[0][1] + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                self._DesignParameter['_SupplyLineMet3VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                self._DesignParameter['_SupplyLineMet3VDD']['_XWidth'] = _LengthofSupplyLine
                self._DesignParameter['_SupplyLineMet3VDD']['_YWidth'] = _GuardringWidth
                self._DesignParameter['_SupplyLineMet3VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]]  # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                # self._DesignParameter['_SupplyLineMet4VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                # self._DesignParameter['_SupplyLineMet4VDD']['_XWidth'] = _LengthofSupplyLine
                # self._DesignParameter['_SupplyLineMet4VDD']['_YWidth'] = _GuardringWidth
                # self._DesignParameter['_SupplyLineMet4VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]]  # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]
                #
                # self._DesignParameter['_SupplyLineMet5VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
                # self._DesignParameter['_SupplyLineMet5VDD']['_XWidth'] = _LengthofSupplyLine
                # self._DesignParameter['_SupplyLineMet5VDD']['_YWidth'] = _GuardringWidth
                # self._DesignParameter['_SupplyLineMet5VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]]  # + self._DesignParameter['_GuardringVSS']['_YWidth'] // 2]]

                _ViaNumVDDX12 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (
                        _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                _ViaNumVDDX23 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (
                        _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                # _ViaNumVDDX34 = int((self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][1][0] - self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][0]) // (
                #         _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 2
                # _ViaNumVDDX45 = int((self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][1][0] - self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_XYCoordinates'][0][0][0]) // (
                #         _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) - 2


                # if _ViaNumVDDX34 < 1:
                #     _ViaNumVDDX34 = 1
                # if _ViaNumVDDX45 < 1:
                #     _ViaNumVDDX45 = 1

                _ViaNumVDDY12 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) // (
                        _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                _ViaNumVDDY23 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) // (
                        _DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
                # _ViaNumVDDY34 = int(_GuardringWidth // (
                #         _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
                # _ViaNumVDDY45 = int(_GuardringWidth // (
                #         _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

                if _ViaNumVDDX12 <= 1:
                    _ViaNumVDDX12 = 1
                    _ViaNumVDDY12 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) // (
                                                _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                if _ViaNumVDDX23 <= 1:
                    _ViaNumVDDX23 = 1
                    _ViaNumVDDY23 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) // (
                                                _DRCObj._VIAxMinSpace+ _DRCObj._VIAxMinWidth)) + 1


                if _ViaNumVDDY12 <= 1:
                    _ViaNumVDDY12 = 1
                    _ViaNumVDDX12 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (
                            _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                if _ViaNumVDDY23 <= 1:
                    _ViaNumVDDY23 = 1
                    _ViaNumVDDX23 = int((_LengthofSupplyLine  - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) // (
                            _DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

                # if _ViaNumVDDY34 < 1:
                #     _ViaNumVDDY34 = 1
                # if _ViaNumVDDY45 < 1:
                #     _ViaNumVDDY45 = 1

                _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12
                _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY12
                self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None,
                                                      _Name='ViaMet12Met2VDDIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(
                **_ViaVDDMet12Met2)
                self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]

                _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX23
                _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY23
                self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(
                _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,
                                                      _Name='ViaMet22Met3VDDIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(
                **_ViaVDDMet22Met3)
                self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]

                # _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaNumVDDX34
                # _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaNumVDDY34
                # self._DesignParameter['_ViaMet32Met4VDD'] = self._SrefElementDeclaration(
                # _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,
                #                                       _Name='ViaMet32Met4VDDIn{}'.format(_Name)))[0]
                # self._DesignParameter['_ViaMet32Met4VDD']['_DesignObj']._CalculateViaMet32Met4DesignParameter(
                # **_ViaVDDMet32Met4)
                # self._DesignParameter['_ViaMet32Met4VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]
                #
                # _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
                # _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ViaNumVDDX45
                # _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ViaNumVDDY45
                # self._DesignParameter['_ViaMet42Met5VDD'] = self._SrefElementDeclaration(
                #     _DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,
                #                                       _Name='ViaMet42Met5VDDIn{}'.format(_Name)))[0]
                # self._DesignParameter['_ViaMet42Met5VDD']['_DesignObj']._CalculateViaMet42Met5DesignParameter(
                #     **_ViaVDDMet42Met5)
                # self._DesignParameter['_ViaMet42Met5VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]

            ########################################### Setting for Input Metal ##########################################
            # _ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = _tmpViaX
            # _ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 2
            #
            # self._DesignParameter['_ViaMet12Met2forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet12Met2forInSignal']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)
            # self._DesignParameter['_ViaMet12Met2forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            # _ViaMet22Met3forInput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOX'] = _tmpViaX
            # _ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOY'] = 2
            #
            # self._DesignParameter['_ViaMet22Met3forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet22Met3forInSignal']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3forInput)
            # self._DesignParameter['_ViaMet22Met3forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            #
            # _ViaMet32Met4forInput = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet32Met4forInput['_ViaMet32Met4NumberOfCOX'] = _tmpViaX
            # _ViaMet32Met4forInput['_ViaMet32Met4NumberOfCOY'] = 2
            #
            # self._DesignParameter['_ViaMet32Met4forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet32Met4forInSignal']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4forInput)
            # self._DesignParameter['_ViaMet32Met4forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            #
            # _ViaMet42Met5forInput = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet42Met5forInput['_ViaMet42Met5NumberOfCOX'] = _tmpViaX
            # _ViaMet42Met5forInput['_ViaMet42Met5NumberOfCOY'] = 2
            #
            # self._DesignParameter['_ViaMet42Met5forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet42Met5forInSignal']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaMet42Met5forInput)
            # self._DesignParameter['_ViaMet42Met5forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            #
            # _ViaMet52Met6forInput = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet52Met6forInput['_ViaMet52Met6NumberOfCOX'] = _tmpViaX
            # _ViaMet52Met6forInput['_ViaMet52Met6NumberOfCOY'] = 5
            #
            # self._DesignParameter['_ViaMet52Met6forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet52Met6forInSignal']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**_ViaMet52Met6forInput)
            # self._DesignParameter['_ViaMet52Met6forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            # _ViaMet62Met7forInput = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
            # _tmpViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
            # if _tmpViaX < 1 :
            #     _tmpViaX = 1
            # _ViaMet62Met7forInput['_ViaMet62Met7NumberOfCOX'] = _tmpViaX
            # _ViaMet62Met7forInput['_ViaMet62Met7NumberOfCOY'] = 5
            #
            # self._DesignParameter['_ViaMet62Met7forInSignal'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7forInSignal{}'.format(_Name)))[0]
            # self._DesignParameter['_ViaMet62Met7forInSignal']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(**_ViaMet62Met7forInput)
            # self._DesignParameter['_ViaMet62Met7forInSignal']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace, \
            #                                                                         self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] - 30], \
            #                                                                        [-(self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][0] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][
            #                                                                             0] - _DRCObj._MetalxMinSpace), \
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_XYCoordinates'][0][1] +
            #                                                                         self._DesignParameter['_NMOSSET'][
            #                                                                             '_DesignObj']._DesignParameter[
            #                                                                             '_VIANMOSPoly2Met1NMOS1'][
            #                                                                             '_XYCoordinates'][0][1] - 30]
            #                                                                        ]
            #
            # del _tmpViaX
            #
            #
            #
            #
            #
            # self._DesignParameter['_Met1forInSignal'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            # self._DesignParameter['_Met1forInSignal']['_XWidth'] = self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 - \
            #                                             (self._DesignParameter['_ViaMet12Met2forInSignal']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2forInSignal']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2)
            # self._DesignParameter['_Met1forInSignal']['_YWidth'] = self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - \
            #                                             (self._DesignParameter['_ViaMet12Met2forInSignal']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2forInSignal']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)
            # self._DesignParameter['_Met1forInSignal']['_XYCoordinates'] = [[(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 + \
            #                                             (self._DesignParameter['_ViaMet12Met2forInSignal']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet12Met2forInSignal']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2)) // 2, \
            #                                                                 (self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + \
            #                                              (self._DesignParameter['_ViaMet12Met2forInSignal']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet12Met2forInSignal']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2
            #                                                                 ], \
            #                                                                [- (self._DesignParameter['_NMOSSET'][
            #                                                                      '_XYCoordinates'][0][0] +
            #                                                                  self._DesignParameter['_NMOSSET'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_VIANMOSPoly2Met1NMOS1'][
            #                                                                      '_XYCoordinates'][0][0] +
            #                                                                  self._DesignParameter['_NMOSSET'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_VIANMOSPoly2Met1NMOS1'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_Met1Layer']['_XWidth'] // 2 + \
            #                                                                  (self._DesignParameter[
            #                                                                       '_ViaMet12Met2forInSignal'][
            #                                                                       '_XYCoordinates'][0][0] -
            #                                                                   self._DesignParameter[
            #                                                                       '_ViaMet12Met2forInSignal'][
            #                                                                       '_DesignObj']._DesignParameter[
            #                                                                       '_Met1Layer']['_XWidth'] // 2)) // 2, \
            #                                                                 (self._DesignParameter['_NMOSSET'][
            #                                                                      '_XYCoordinates'][0][1] +
            #                                                                  self._DesignParameter['_NMOSSET'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_VIANMOSPoly2Met1NMOS1'][
            #                                                                      '_XYCoordinates'][0][1] +
            #                                                                  self._DesignParameter['_NMOSSET'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_VIANMOSPoly2Met1NMOS1'][
            #                                                                      '_DesignObj']._DesignParameter[
            #                                                                      '_Met1Layer']['_YWidth'] // 2 + \
            #                                                                  (self._DesignParameter[
            #                                                                       '_ViaMet12Met2forInSignal'][
            #                                                                       '_XYCoordinates'][0][1] -
            #                                                                   self._DesignParameter[
            #                                                                       '_ViaMet12Met2forInSignal'][
            #                                                                       '_DesignObj']._DesignParameter[
            #                                                                       '_Met1Layer']['_YWidth'] // 2)) // 2
            #                                                                 ]
            #                                                                ]
            #


            # if _NMOSChannelWidth < 400 :
            #     print("<_NMOSChannelWidth> should be over 400nm.")
            #     raise NotImplementedError

            if _DATAinputNMOSFinger == 1 and _NMOSFinger == 1 :
                warnings.warn("The input signal can be disturbed.")





if __name__ == '__main__':
    # SlicerObj._CalculateDesignParameter(_CLKinputPMOSFinger1 = 6, _CLKinputPMOSFinger2 = 3, _PMOSFinger = 2, _PMOSChannelWidth = 1000,
    #                                     _DATAinputNMOSFinger = 12, _NMOSFinger = 2, _CLKinputNMOSFinger = 8, _NMOSChannelWidth = 1000,
    #                                     _ChannelLength = 30, _Dummy = True, _SLVT = True, _GuardringWidth = 200, _Guardring = True,
    #                                     _SlicerGuardringWidth=200, _SlicerGuardring= None,
    #                                     _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
    #                                     _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None, _PowerLine=True)

    # SlicerObj._CalculateDesignParameter(_CLKinputPMOSFinger1 =3, _CLKinputPMOSFinger2 =2, _PMOSFinger = 1, _PMOSChannelWidth =1000,
    #                                     _DATAinputNMOSFinger =11, _NMOSFinger =1, _CLKinputNMOSFinger = 7, _NMOSChannelWidth = 1000,
    #                                     _ChannelLength = 30, _Dummy = True, _SLVT = True, _GuardringWidth = 200, _Guardring = True,
    #                                     _SlicerGuardringWidth=200, _SlicerGuardring= None,
    #                                     _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
    #                                     _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None, _PowerLine=True)

    for _tries in range(1, 2) :


        _CLKinputPMOSFinger1 = 6###random.randint(1, 16)
        _CLKinputPMOSFinger2 = 3###random.randint(1, 16)
        _PMOSFinger = 2###random.randint(1, 16)
        _PMOSChannelWidth = 600###random.randrange(200, 1050, 50)
        _DATAinputNMOSFinger = 10###random.randint(2, 16)
        _NMOSFinger = 2###random.randint(1, 16)
        _CLKinputNMOSFinger = 7##random.randint(1, 16)
        _NMOSChannelWidth = 600###random.randrange(200, 1050, 50)
        _CLKinputNMOSChannelWidth = 1000
        _ChannelLength = 30
        _Dummy = True
        _SLVT = True
        _GuardringWidth = 200
        _Guardring = True
        _SlicerGuardringWidth = 200
        _SlicerGuardring = None
        _NumSupplyCOY = None
        _NumSupplyCOX = None
        _SupplyMet1XWidth = None
        _SupplyMet1YWidth = None
        _VDD2VSSHeight = None
        _NumVIAPoly2Met1COX = None
        _NumVIAPoly2Met1COY = None
        _NumVIAMet12COX = None
        _NumVIAMet12COY = None
        _PowerLine = True




        DesignParameters._Technology = '028nm'

        SlicerObj = _Slicer(_DesignParameter=None, _Name='Slicer')

        SlicerObj._CalculateDesignParameter(_CLKinputPMOSFinger1=_CLKinputPMOSFinger1, _CLKinputPMOSFinger2=_CLKinputPMOSFinger2, _PMOSFinger=_PMOSFinger,
                                            _PMOSChannelWidth=_PMOSChannelWidth,
                                            _DATAinputNMOSFinger=_DATAinputNMOSFinger, _NMOSFinger=_NMOSFinger, _CLKinputNMOSFinger=_CLKinputNMOSFinger,
                                            _NMOSChannelWidth=_NMOSChannelWidth, _CLKinputNMOSChannelWidth = _CLKinputNMOSChannelWidth ,
                                            _ChannelLength=_ChannelLength, _Dummy=_Dummy, _SLVT=_SLVT, _GuardringWidth=_GuardringWidth,
                                            _Guardring=_Guardring,
                                            _SlicerGuardringWidth=_SlicerGuardringWidth, _SlicerGuardring=_SlicerGuardring,
                                            _NumSupplyCOY=_NumSupplyCOY, _NumSupplyCOX=_NumSupplyCOX, _SupplyMet1XWidth=_SupplyMet1XWidth,
                                            _SupplyMet1YWidth=_SupplyMet1YWidth, _VDD2VSSHeight=_VDD2VSSHeight,
                                            _NumVIAPoly2Met1COX=_NumVIAPoly2Met1COX, _NumVIAPoly2Met1COY=_NumVIAPoly2Met1COY, _NumVIAMet12COX=_NumVIAMet12COX,
                                            _NumVIAMet12COY=_NumVIAMet12COY, _PowerLine=_PowerLine)


        SlicerObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SlicerObj._DesignParameter)
        _fileName = 'Slicer.gds'
        testStreamFile = open('.//{}'.format(_fileName), 'wb')
        tmp = SlicerObj._CreateGDSStream(SlicerObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()





        import ftplib
        ftp = ftplib.FTP('141.223.22.156')
        ftp.login('jicho0927', 'cho89140616!!')
        ftp.cwd('//mnt//sdc//jicho0927//OPUS//SAMSUNG28n')
        myfile = open('Slicer.gds', 'rb')
        ftp.storbinary('STOR Slicer.gds', myfile)
        myfile.close()
        ftp.close()

        ftp = ftplib.FTP('141.223.22.156')
        ftp.login('junung', 'chlwnsdnd1!')
        ftp.cwd('//mnt//sdc//junung//OPUS//Samsung28n')
        myfile = open('Slicer.gds', 'rb')
        ftp.storbinary('STOR Slicer.gds', myfile)
        myfile.close()
        ftp.close()

    ################################## DRC Checker #################################
    #     import DRCchecker
    #
    #
    #
    #     a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '//mnt//sdc//jicho0927//OPUS//SAMSUNG28n', '//mnt//sdc//jicho0927//OPUS//SAMSUNG28n//DRC//run', 'Slicer_test', 'Slicer')
    #     print('_tries = ', _tries)
    #     print('_CLKinputPMOSFinger1 = ', _CLKinputPMOSFinger1)
    #     print('_CLKinputPMOSFinger2 = ', _CLKinputPMOSFinger2)
    #     print('_PMOSFinger = ', _PMOSFinger)
    #     print('_PMOSChannelWidth = ', _PMOSChannelWidth)
    #     print('_DATAinputNMOSFinger = ', _DATAinputNMOSFinger)
    #     print('_NMOSFinger = ', _NMOSFinger)
    #     print('_CLKinputNMOSFinger = ', _CLKinputNMOSFinger)
    #     print('_NMOSChannelWidth = ', _NMOSChannelWidth)
    #
    #     a.DRCchecker()
    #
    #
    #
    #
    #
    #
    # print ("DRCclean!!")





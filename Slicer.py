import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ContGeneration

import PMOSSetofSlicer
import NMOSSetofSlicer

import DesignParameters
import user_define_exceptions

import copy
import DRC

import ftplib
import os

from ftplib import FTP
import base64


class _Slicer(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
                                        _CLKinputPMOSFinger1=None, _CLKinputPMOSFinger2=None, _PMOSFinger=None, _PMOSChannelWidth=None,
                                        _DATAinputNMOSFinger=None, _NMOSFinger=None, _CLKinputNMOSFinger=None, _NMOSChannelWidth=None,
                                        _ChannelLength=None, _Dummy=False, _SLVT=False, _GuardringWidth=None, _Guardring=False,
                                        _SlicerGuardringWidth=None, _SlicerGuardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight=None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None)


    def __init__(self, _DesignParameter=None, _Name='Slicer'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _CLKinputPMOSFinger1 = None, _CLKinputPMOSFinger2 = None, _PMOSFinger = None, _PMOSChannelWidth = None,
                                        _DATAinputNMOSFinger = None, _NMOSFinger = None, _CLKinputNMOSFinger = None, _NMOSChannelWidth = None,
                                        _ChannelLength = None, _Dummy = False, _SLVT = False, _GuardringWidth = None, _Guardring = False,
                                        _SlicerGuardringWidth=None, _SlicerGuardring=False,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None
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
            self._DesignParameter['_PMOSSET']['_XYCoordinates'] = [[0, 0+abs(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']) \
                                                                       + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_RingMetal1Layer1']['_Width'] +_DRCObj._NwMinSpacetoNactive]]

            ##############################################################################################################################################################
            ################################################################### NMOS SET Generation  #########################################################################
            ##############################################################################################################################################################
            # NMOS SET Generation
            _NMOSSETinputs = copy.deepcopy(NMOSSetofSlicer._NMOSWithDummyOfSlicer._ParametersForDesignCalculation)
            _NMOSSETinputs['_DATAinputNMOSFinger'] = _DATAinputNMOSFinger
            _NMOSSETinputs['_NMOSFinger'] = _NMOSFinger
            _NMOSSETinputs['_CLKinputNMOSFinger'] = _CLKinputNMOSFinger
            _NMOSSETinputs['_NMOSChannelWidth'] = _NMOSChannelWidth
            _NMOSSETinputs['_ChannelLength'] = _ChannelLength
            _NMOSSETinputs['_Dummy'] = _Dummy
            _NMOSSETinputs['_SLVT'] = _SLVT
            _NMOSSETinputs['_GuardringWidth'] = _GuardringWidth
            _NMOSSETinputs['_Guardring'] = _Guardring

            self._DesignParameter['_NMOSSET'] = self._SrefElementDeclaration(_DesignObj=NMOSSetofSlicer._NMOSWithDummyOfSlicer(_DesignParameter=None, _Name='NMOSSETIn{}'.format(_Name)))[0]
            self._DesignParameter['_NMOSSET']['_DesignObj']._CalculateDesignParameter(**_NMOSSETinputs)
            self._DesignParameter['_NMOSSET']['_XYCoordinates'] = [[0, 0-abs(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']) \
                                                                        -_DRCObj._PpMinWidth/2]]

            #########################################################################################################################################
            ############################################### Guardring Generation for Slicer #########################################################
            #########################################################################################################################################
            PMOS_toptmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
            PMOS_bottomtmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
            PMOS_righttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_righttmp']['_Ignore']
            PMOS_lefttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_lefttmp']['_Ignore']
            NMOS_toptmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']
            NMOS_bottomtmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
            NMOS_righttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_righttmp']['_Ignore']
            NMOS_lefttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_lefttmp']['_Ignore']
            print('x')
            _GuardRingRX2RXSpace=212

            # Horizontal Met1
            self._DesignParameter['_SlicerGuardringMet1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            tmp=[]
            GuardringMet1Coordinate= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
                                       self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth/2 \
                                       + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2]]
            GuardringMet1Coordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
                                        self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth/2 \
                                       - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2]]
            print('x')

            # Vertical Met1
            self._DesignParameter['_SlicerGuardringMet2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SlicerGuardringMet2']['_XWidth'] = _SlicerGuardringWidth
            self._DesignParameter['_SlicerGuardringMet2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth
            GuardringMet1Coordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth/2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2, \
                                        (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])/2
                                      ]]
            GuardringMet1Coordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth/2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2, \
                                         (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) / 2
                                         ]]

            self._DesignParameter['_SlicerGuardringMet1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth
            self._DesignParameter['_SlicerGuardringMet1']['_YWidth'] = _SlicerGuardringWidth

            tmp=GuardringMet1Coordinate + GuardringMet1Coordinate1
            tmp2=GuardringMet1Coordinate2 + GuardringMet1Coordinate3
            self._DesignParameter['_SlicerGuardringMet1']['_XYCoordinates'] = tmp
            self._DesignParameter['_SlicerGuardringMet2']['_XYCoordinates'] = tmp2
            del tmp

            # Guardring OD Layer
            tmp=[]
            # Horizontal OD
            self._DesignParameter['_SlicerGuardringOD1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            GuardringODCoordinate = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
                                      self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth/2 \
                                      + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2]]
            GuardringODCoordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
                                       self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth/2 \
                                       - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2]]
            tmp=GuardringODCoordinate + GuardringODCoordinate1
            self._DesignParameter['_SlicerGuardringOD1']['_XYCoordinates'] = tmp

            # Vertical OD
            self._DesignParameter['_SlicerGuardringOD2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_SlicerGuardringOD2']['_XWidth'] = _SlicerGuardringWidth
            self._DesignParameter['_SlicerGuardringOD2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth
            GuardringMet1Coordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth/2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2, \
                                        (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])/2
                                      ]]
            GuardringMet1Coordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth/2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2, \
                                         (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) / 2
                                         ]]
            tmp2=GuardringMet1Coordinate2 + GuardringMet1Coordinate3
            self._DesignParameter['_SlicerGuardringOD2']['_XYCoordinates'] = tmp2
            del tmp

            self._DesignParameter['_SlicerGuardringOD1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth
            self._DesignParameter['_SlicerGuardringOD1']['_YWidth'] = _SlicerGuardringWidth

            # Guardring Pp Layer
            # Horizontal Pp Layer
            self._DesignParameter['_SlicerGuardringBP1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            GuardringPpCoordinate = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],\
                                      self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth/2 \
                                      + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2]]
            GuardringPpCoordinate1 = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0],\
                                       self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _GuardringWidth/2 \
                                       - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2]]
            tmp = GuardringPpCoordinate + GuardringPpCoordinate1

            self._DesignParameter['_SlicerGuardringBP1']['_XWidth'] = GuardringMet1Coordinate3[0][0] - GuardringMet1Coordinate2[0][0] + _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            self._DesignParameter['_SlicerGuardringBP1']['_YWidth'] = _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            self._DesignParameter['_SlicerGuardringBP1']['_XYCoordinates'] = tmp

            # Vertical Pp Layer
            self._DesignParameter['_SlicerGuardringBP2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            GuardringPpCoordinate2= [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth/2 - _GuardRingRX2RXSpace - _SlicerGuardringWidth/2, \
                                        (GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1])/2
                                      ]]
            GuardringPpCoordinate3 = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth/2 + _GuardRingRX2RXSpace + _SlicerGuardringWidth/2, \
                                         (GuardringMet1Coordinate[0][1] + GuardringMet1Coordinate1[0][1]) / 2
                                         ]]
            tmp2 = GuardringPpCoordinate2 + GuardringPpCoordinate3

            self._DesignParameter['_SlicerGuardringBP2']['_XWidth'] = _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            self._DesignParameter['_SlicerGuardringBP2']['_YWidth'] = GuardringMet1Coordinate[0][1] - GuardringMet1Coordinate1[0][1] + _SlicerGuardringWidth + 2*_DRCObj._PpMinExtensiononPactive2
            self._DesignParameter['_SlicerGuardringBP2']['_XYCoordinates'] = tmp2

            # CONT Generation for Guardring
            self._DesignParameter['_CONT1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_CONT2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            self._DesignParameter['_CONT1']['_XWidth'] = _DRCObj._CoMinWidth
            self._DesignParameter['_CONT1']['_YWidth'] = _DRCObj._CoMinWidth
            self._DesignParameter['_CONT2']['_XWidth'] = _DRCObj._CoMinWidth
            self._DesignParameter['_CONT2']['_YWidth'] = _DRCObj._CoMinWidth

            _XNumberOfCO1 = int((self._DesignParameter['_SlicerGuardringMet1']['_XWidth'] - 2*_SlicerGuardringWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) # Horizontal Ring
            _YNumberOfCO1 = _SlicerGuardringWidth // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
            _XNumberOfCO2 = _SlicerGuardringWidth // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
            _YNumberOfCO2 = int(self._DesignParameter['_SlicerGuardringMet2']['_YWidth'] - 2*_SlicerGuardringWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)  # Verical Ring

            # CONT Coordinate Setting
            _LengthRingBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
            tmp = []
            tmp2=[GuardringMet1Coordinate[0][1], GuardringMet1Coordinate1[0][1]]
            tmp3=GuardringMet1Coordinate3[0][0]+GuardringMet1Coordinate2[0][0]

            for i in range(0, _XNumberOfCO1):
                for j in range(0, _YNumberOfCO1):
                    for k in tmp2:
                        if (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 0:
                            _xycoordinatetmp = [(tmp3)/2 - (_XNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 1 and (_YNumberOfCO1 % 2) == 1:
                            _xycoordinatetmp = [(tmp3)/2 - (_XNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 0:
                            _xycoordinatetmp = [(tmp3)/2 - (_XNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        elif (_XNumberOfCO1 % 2) == 0 and (_YNumberOfCO1 % 2) == 1:
                            _xycoordinatetmp = [(tmp3)/2 - (_XNumberOfCO1 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO,
                                                k - (_YNumberOfCO1 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        tmp.append(_xycoordinatetmp)
            self._DesignParameter['_CONT1']['_XYCoordinates'] = tmp

            tmp = []
            tmp2 = [-1, 1]
            tmp3 = GuardringMet1Coordinate[0][1]+GuardringMet1Coordinate1[0][1]
            print('x')

            for i in range(0, _XNumberOfCO2):
                for j in range(0, _YNumberOfCO2):
                    for k in tmp2:
                        if (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 0:
                            _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO, \
                                                tmp3/2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]

                        elif (_XNumberOfCO2 % 2) == 1 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + i * _LengthRingBtwCO, \
                                                tmp3/2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]

                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 0:
                            _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO, \
                                                tmp3/2 - (_YNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + j * _LengthRingBtwCO]

                        elif (_XNumberOfCO2 % 2) == 0 and (_YNumberOfCO2 % 2) == 1:
                            _xycoordinatetmp = [GuardringMet1Coordinate2[0][0] * k - (_XNumberOfCO2 / 2 - 0.5) * _LengthRingBtwCO + i * _LengthRingBtwCO, \
                                                tmp3/2 - (_YNumberOfCO2 - 1) / 2 * _LengthRingBtwCO + j * _LengthRingBtwCO]
                        tmp.append(_xycoordinatetmp)
            self._DesignParameter['_CONT2']['_XYCoordinates'] = tmp

            ################################################################ Guadring VSS Generation ########################################################################################
            self._DesignParameter['_GuardringVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_GuardringVSS']['_XWidth'] = NMOS_righttmp - NMOS_lefttmp + _GuardringWidth
            self._DesignParameter['_GuardringVSS']['_YWidth'] = (NMOS_bottomtmp+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]) - GuardringMet1Coordinate1[0][1]
            self._DesignParameter['_GuardringVSS']['_XYCoordinates'] = [[0, GuardringMet1Coordinate1[0][1] + self._DesignParameter['_GuardringVSS']['_YWidth']/2]]
            print('x')


            ##################################################################################################################################################################################
            ################################################################# NMOS VIA1 Generation ###########################################################################################
            ##################################################################################################################################################################################
            ## VIA1 Generation for Gate of Inner NMOS
            _VIAInnerNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = 2
            _VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnNMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnInnerNMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerNMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][0]-_DRCObj._Metal1MinEnclosureVia12,
                                                                                    self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]\
                                                                                    +self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                                   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][0]+_DRCObj._Metal1MinEnclosureVia12,
                                                                                    self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] \
                                                                                    +self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]
            ## VIA1 Generation for Gate of Outer NMOS
            _VIAOuterNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = 2
            _VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnOuterNMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterNMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0]+self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2*_DRCObj._MetalxMinSpace,
                                                                                    self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]\
                                                                                    +self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]

            print('x')

            ## VIA1 Generation for Gate of Inner PMOS
            _VIAInnerPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = 2
            _VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnInnerPMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerPMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][0]-_DRCObj._Metal1MinEnclosureVia12,
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1]\
                                                                                    +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                                   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][0]+_DRCObj._Metal1MinEnclosureVia12,
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1] \
                                                                                    +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]

            self._DesignParameter['_Met1ForGates'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met1ForGates']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_Met1ForGates']['_YWidth'] = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met1ForGates']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'] + self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates']
            print('x')

            ## VIA1 Generation for Gate of Outer PMOS CLK
            _VIAOuterPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = 2
            _VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnOuterPMOSGateIn1{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterPMOSGateMet12)
            self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0] +
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*3/4 + _DRCObj._MetalxMinSpace,
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1]\
                                                                                    +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                                   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0] -
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*3/4 - _DRCObj._MetalxMinSpace,
                                                                                    self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
                                                                                    + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                                  ]


            ## VIA2 Generation of Inner PMOS Drain and Inner NMOS Drain for PMOSSET, NMOSSET Connection
            _VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

            _VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1

            _tmpNumY = _NMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth) - 1
            if _tmpNumY < 1 :
                _tmpNumY = 1
            _VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumY

            self._DesignParameter['_ViaMet22Met3OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSOutputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)
            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates']=[[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][0],
                                                                                  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
                                                                                  + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][0],
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                                   # self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1] \
                                                                                   # + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][-1][0],
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

                                                                                  [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][-1][0], \
                                                                                   self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
                                                                                   # self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput3']['_XYCoordinates'][0][1] \
                                                                                   # + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
                                                                                  ]]
            print('x')

            ## VIA2 Generation of Outer PMOS and NMOS for CLK routing Connection
            _VIANMOSMet23CLKinput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOX'] = 2
            _VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOY'] = 1

            self._DesignParameter['_ViaMet22Met3OnCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnCLKInputIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnCLKInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23CLKinput)
            self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0] +
                                                                                   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2*_DRCObj._MetalxMinSpace,
                                                                                   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1]\
                                                                                    +self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]], #NMOS CLK input

                                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0] +
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*3/4 + _DRCObj._MetalxMinSpace,
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], #PMOS1 CLK input

                                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0] -
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*3/4 - _DRCObj._MetalxMinSpace,
                                                                                   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
                                                                                   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] #PMOS1 CLK input
                                                                                 ]

            print('x')
            ########################################################################################################################################################
            ########################################################## Routing Generation ##########################################################################
            ########################################################################################################################################################

            ############################################# CLK input PMOS1 Drain + Data intput NMOS Drain Met2 Routing ###############################################
            PMOSxycoordinate=[]
            NMOSxycoordinate=[]
            # self._DesignParameter['_Met2Slicer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            # self._DesignParameter['_Met2Slicer']['_Width'] = _DRCObj._MetalxMinWidth
            # # k = len(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'])

            # self._DesignParameter['_Met2Slicer']['_XYCoordinates'] =[
            #                                                          [
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1]+(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2-_DRCObj._MetalxMinWidth/2+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][0][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][0][1]+(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])/2-_DRCObj._MetalxMinWidth/2+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
            #                                                          ],
            #                                                          [
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][-1][1] + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 - _DRCObj._MetalxMinWidth / 2 + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
            #                                                           [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_XYCoordinates'][-1][0],
            #                                                            self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_XYCoordinates'][-1][1] + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput4']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2 - _DRCObj._MetalxMinWidth / 2 + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
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
                k = int(_CLKinputPMOSFinger1/2)
            elif (_CLKinputPMOSFinger1 % 2) == 1:
                k = int((float(_CLKinputPMOSFinger1)/float(2)) + 0.5)

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
            ################################################# Inner CLK input PMOS2 Drain --- Inner PMOS Drain Connection ###############################################
            self._DesignParameter['_Met2PMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2PMOS2']['_Width'] = _DRCObj._MetalxMinWidth
            k = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'])
            j = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'])

            print('x')

            if (_CLKinputPMOSFinger2 % 2) == 1:
                self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][(k/2)-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][(j / 2) - 1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][(k / 2)][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][(j / 2)][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ]
                                                                        ]
            elif (_CLKinputPMOSFinger2 % 2) == 0:
                self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][(k/2)-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][(j/2)-1][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ],
                                                                         [
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][(k/2)][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                          [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][(j/2)][0],
                                                                           self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
                                                                         ]
                                                                        ]


            ######################################################################################################################################################################
            ########################################################################### Met3 Routing #############################################################################
            ######################################################################################################################################################################
            ################################################ Met3 Routing Generation for CLK input PMOS2 --- Inner PMOS Connection ###############################################
            self._DesignParameter['_Met3PNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3PNMOS']['_Width'] = _DRCObj._MetalxMinWidth
            if (_PMOSFinger < _NMOSFinger):
                self._DesignParameter['_Met3PNMOS']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][1]],
                                                                          self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1]],

                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][3][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][1]],
                                                                          self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][3]]
                                                                         ]
            elif (_PMOSFinger >= _NMOSFinger):
                self._DesignParameter['_Met3PNMOS']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][1]],
                                                                          self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1]],

                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][3][1]],
                                                                          self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][3]]
                                                                         ]

            ################################################ Met3 Routing Generation for CLK input / Outer PMOS1---PMOS2---NMOS5 ###############################################
            self._DesignParameter['_Met3CLKinput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3CLKinput']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met3CLKinput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][1][1]],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - 3*_DRCObj._MetalxMinWidth,
                                                                          self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][1][1]],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0] - 3*_DRCObj._MetalxMinWidth,
                                                                          self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][0][1]],
                                                                         [self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][0][1]],

                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0] + 3*_DRCObj._MetalxMinWidth,
                                                                          self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][0][1]],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][0] + 3*_DRCObj._MetalxMinWidth,
                                                                          self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][2][1]],
                                                                         [self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][2][0], self._DesignParameter['_ViaMet22Met3OnCLKInput']['_XYCoordinates'][2][1]]
                                                                        ]]
            print('x')

            ########################################### Met2 Routing Generation for Inner PMOS Gate --- Inner NMOS Gate Connection (Cross-coupled) ##########################################
            self._DesignParameter['_Met2PNMOSGate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2PNMOSGate']['_Width'] = _DRCObj._MetalxMinWidth
            if (_PMOSFinger < _NMOSFinger):
                self._DesignParameter['_Met2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0],
                                                                             [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]],
                                                                              self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0]],

                                                                             [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1],
                                                                             [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]],
                                                                              self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1]]
                                                                         ]

            elif (_PMOSFinger >= _NMOSFinger):
                self._DesignParameter['_Met2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0],
                                                                             [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1]],
                                                                              self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0]],

                                                                             [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1],
                                                                             [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1]],
                                                                              self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1]]
                                                                            ]

            ########################################### Met2 Routing Generation for Inner PMOS/NMOS Gate --- Inner PMOS/NMOS Drain Connection (Cross-coupled) ##########################################
            self._DesignParameter['_Met2PNMOSCross'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met2PNMOSCross']['_Width'] = _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met2PNMOSCross']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0],
                                                                         [(self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0])/2,
                                                                           self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1]],
                                                                         [(self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0])/2,
                                                                           self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2][1]],
                                                                         self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2]
                                                                         ],
                                                                         [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1],
                                                                          [(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0])/2,
                                                                            self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][1]],
                                                                          [(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0])/2,
                                                                            self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]],
                                                                          self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1]
                                                                         ]]
            print('x')
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

            self._DesignParameter['_PinOutputN']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0]]
            self._DesignParameter['_PinOutputP']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][2]]
            self._DesignParameter['_PinCLK']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0],
                                                                   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
                                                                 ]

            print('x')
            pass
            #########################################################################################################################################
if __name__ == '__main__':
    SlicerObj = _Slicer(_DesignParameter=None, _Name='Slicer')
    SlicerObj._CalculateDesignParameter(_CLKinputPMOSFinger1 = 6, _CLKinputPMOSFinger2 = 3, _PMOSFinger = 2, _PMOSChannelWidth = 1000,
                                        _DATAinputNMOSFinger = 12, _NMOSFinger = 2, _CLKinputNMOSFinger = 8, _NMOSChannelWidth = 1000,
                                        _ChannelLength = 30, _Dummy = True, _SLVT = True, _GuardringWidth = 200, _Guardring = True,
                                        _SlicerGuardringWidth=200, _SlicerGuardring= None,
                                        _NumSupplyCOY=None, _NumSupplyCOX=None, _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, _VDD2VSSHeight = None,
                                        _NumVIAPoly2Met1COX=None, _NumVIAPoly2Met1COY=None, _NumVIAMet12COX=None, _NumVIAMet12COY=None)

    SlicerObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SlicerObj._DesignParameter)
    _fileName = 'Slicer.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = SlicerObj._CreateGDSStream(SlicerObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()



    import ftplib
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('Slicer.gds', 'rb')
    ftp.storbinary('STOR Slicer.gds', myfile)
    myfile.close()
    ftp.close()
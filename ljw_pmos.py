
import StickDiagram
import DesignParameters
import DRC


class _Pmos(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False, _SLVT=False, _LVT=False, _HVT=False)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #RXlayer red
                # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['RXPIN'][
                                                                        1], _XYCoordinates=[], _XWidth=400,
                                                                    _YWidth=400),
                _SLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],
                                                            _Datatype=DesignParameters._LayerMapping['SLVT'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #SLVTlayer
                _LVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVT'][0],
                                                           _Datatype=DesignParameters._LayerMapping['LVT'][1],
                                                           _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _HVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['HVT'][0],
                                                           _Datatype=DesignParameters._LayerMapping['HVT'][1],
                                                           _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                               _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #BP layer에 같이 나옴
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #Poly(Gate)layer green
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['PCPIN'][
                                                                        1], _XYCoordinates=[], _XWidth=400,
                                                                    _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #Metal1 layer blue
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                   _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                   _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #Metal1 layer와 동일 blue
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #BP layer(pmos에만 존재)brown
                _NWLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                          _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                # NWELL layer yellow
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #Contact layer yellow
                _PCCRITLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                              _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400),
                #PC crit layer(green)
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

                _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),


            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateDesignParameter(self, _PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False, _SLVT=False, _LVT=False, _HVT=False):
        global _xycoordinatetmp_dummy

        print( '{}  PMOSContact Calculation Start'.format(
                self._DesignParameter['_Name']['_Name']))
        _DRCObj = DRC.DRC()
        if _PMOSChannelWidth % 2 == 0:
            _XYCoordinateOfPMOS = [[0, 0]]#게이트 짝수개 일때 y좌표 0
        else:
            _XYCoordinateOfPMOS = [[0, 0.5]]#게이트 홀수개 일때 y좌표 0.5



        print('#############################     POLY Layer Calculation    ##############################################')
        # POLY Layer XWidth and YWidth Setting
        self._DesignParameter['_POLayer']['_XWidth'] = _PMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_PMOSChannellength)

        print("DRCPolygateMinExtensionOnOD:",_DRCObj.DRCPolygateMinExtensionOnOD(_PMOSChannellength))

        _LengthPMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth,_ParallelLength=_PMOSChannellength) + _PMOSChannellength\

        tmp=[]

        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:  # 게이트수가 짝수면
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) \
                                    * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO, _XYCoordinateOfPMOS[0][1]]
            elif (_PMOSNumberofGate % 2) == 1:  # 게이트수가 홀수면
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 \
                                    * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO, _XYCoordinateOfPMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmp


        print(tmp)
        print('#############################     DIFF(OD/RX) Layer Calculation    ##############################################')
        self._DesignParameter['_ODLayer']['_XWidth'] = _LengthPMOSBtwPO * _PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_YWidth'] = _PMOSChannelWidth
        # DIFF Layer Coordinate Setting
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS



        if _PMOSDummy == True:
            print('#############################     POLY Dummy Layer Calculation    ##############################################')
            # POLY Dummy Layer XWidth and YWidth Setting
            self._DesignParameter['_PODummyLayer']['_XWidth'] = _PMOSChannellength
            self._DesignParameter['_PODummyLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD #여기까지는 Poly와 동일

            # POLY Dummy Layer Coordinate Setting
            # _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
            if (_PMOSNumberofGate % 2) == 0:  # When the number of finger is even
                _xycoordinatetmp_dummy = [[_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) - (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(
                    self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]],[_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2, _XYCoordinateOfPMOS[0][1]]]
            elif (_PMOSNumberofGate % 2) == 1:  # When the number of finger is odd
                _xycoordinatetmp_dummy = [[_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) - (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]],
                    [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]]]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp_dummy

            if int(self._DesignParameter['_PODummyLayer']['_XWidth']) * int(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:
                self._DesignParameter['_PODummyLayer']['_YWidth'] = int((_DRCObj._PODummyMinArea) // (self._DesignParameter['_PODummyLayer']['_XWidth'])) + 2 # +2는 왜??


        else:

            self._DesignParameter['_PODummyLayer']['_XWidth'] = 0
            self._DesignParameter['_PODummyLayer']['_YWidth'] = 0

            # _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
            # self._DesignParameter['_POLayer']['_XWidth']
            if (_PMOSNumberofGate % 2) == 0:  # When the number of finger is even
                _xycoordinatetmp_dummy = [[_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolyMinSpace(
                    _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) - (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]],
                    [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2, _XYCoordinateOfPMOS[0][1]]]
            elif (_PMOSNumberofGate % 2) == 1:  # When the number of finger is odd
                _xycoordinatetmp_dummy = [[_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) - (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]],
                    [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolyMinSpace(
                        _Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfPMOS[0][1]]]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp_dummy


        print('#############################     METAL1 Layer Calcuation    ##############################################')
        # METAL1 Layer XWidth and YWidth Setting
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        # METAL1 Layer Coordinate Setting
        _LengthPMOSBtwMet1 = _LengthPMOSBtwPO  ##_DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        tmp = []

        for i in range(0, _PMOSNumberofGate + 1):  # the number of the metal = the number of the gate + 1
            if (_PMOSNumberofGate % 2) == 0: #게이트 짝수
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,_XYCoordinateOfPMOS[0][1]]
            elif (_PMOSNumberofGate % 2) == 1: #게이트 홀수
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,_XYCoordinateOfPMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmp


        print('#############################     METAL1 PINDrawing    ##############################################')   # METAL1 Layer와 완전히 동일
        self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = tmp


        print('############################# CONT (Source/Drain) Layer Calculation    ##############################################')
        # CONT XNum/YNum Calculation
        _XNumberOfCOInPMOS = _PMOSNumberofGate + 1
        _YNumberOfCOInPMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2]) + _DRCObj._CoMinSpace) / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))

        # CONT Layer XWidth and YWidth Settingk
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        # CONT Coordinate Setting
        _LengthPMOSBtwCO = _DRCObj._CoMinSpace + self._DesignParameter['_COLayer']['_YWidth']
        # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        tmp = []
        ###############################################Check the number of CO On PMOS TR##############################################################################################
        if _XNumberOfCOInPMOS == 0 or _YNumberOfCOInPMOS == 0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ##############################################################################################################################################################################

        if _PMOSChannelWidth % 2 == 0:
            for i in range(0, _XNumberOfCOInPMOS):
                for j in range(0, _YNumberOfCOInPMOS):
                    if (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                    tmp.append(_xycoordinatetmp)

        else:
            for i in range(0, _XNumberOfCOInPMOS):
                for j in range(0, _YNumberOfCOInPMOS):
                    if (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] + 0.5 - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] + 0.5 - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] + 0.5 - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                    elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                            _XYCoordinateOfPMOS[0][1] + 0.5 - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                    tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        _CoArrXWidth = (_XNumberOfCOInPMOS - 1) * _LengthPMOSBtwMet1 + self._DesignParameter['_COLayer']['_XWidth']
        _CoArrYWidth = (_YNumberOfCOInPMOS - 1) * _LengthPMOSBtwCO + self._DesignParameter['_COLayer']['_YWidth']

        if min(_CoArrXWidth, _CoArrYWidth) > _DRCObj._CoArrayMaxWidth:
            print('CA Array Maximum Width should be smaller than 1211n.')
            raise NotImplementedError


        print('#############################     PIMP Layer Calculation    ####################')

        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS
        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive if _PMOSDummy == False else \
                self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] -self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._PpMinEnclosureOfPo + _DRCObj._PpMinExtensiononPactive3
        else:
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive if _PMOSDummy == False else \
                self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] -self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._PpMinEnclosureOfPo

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo2
        else:
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo



        print('##################################################### NWLayer Calculation ####################################################')
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_NWLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * max(_DRCObj._NwMinSpacetoRX,_DRCObj._NwMinSpacetoPactive+_DRCObj._PpMinExtensiononPactive)

        else:
            self._DesignParameter['_NWLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoRX

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_NWLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']
        else:
            self._DesignParameter['_NWLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']



        if _SLVT == True:
            print ('#############################     SLVT Layer Calculation    ##############################################')
            # SLVT Dummy Layer XWidth and YWidth Setting
            self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._SlvtMinExtensionOnOD
            self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            # SLVT Layer Coordinate Setting
            self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = self._DesignParameter['_PPLayer']['_XYCoordinates']

        else:
            self._DesignParameter['_SLVTLayer']['_XWidth'] = 0
            self._DesignParameter['_SLVTLayer']['_YWidth'] = 0

            self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = self._DesignParameter['_PPLayer']['_XYCoordinates']

        if _LVT == True: ### ????
            self._DesignParameter['_LVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._SlvtMinExtensionOnOD
            self._DesignParameter['_LVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_LVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        else : ### ????
            self._DesignParameter['_LVTLayer']['_XWidth'] = 0
            self._DesignParameter['_LVTLayer']['_YWidth'] = 0

            self._DesignParameter['_LVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']


        if _HVT == True: ### ????
            self._DesignParameter['_HVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._SlvtMinExtensionOnOD
            self._DesignParameter['_HVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_HVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        else: ### ????
            self._DesignParameter['_HVTLayer']['_XWidth'] = 0
            self._DesignParameter['_HVTLayer']['_YWidth'] = 0

            self._DesignParameter['_HVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']



        if DesignParameters._Technology == '028nm':
            print(
                '#############################     PCCRIT Layer Calculation    ##############################################')
            if self._DesignParameter['_POLayer']['_XWidth'] == 30 or self._DesignParameter['_POLayer']['_XWidth'] == 34:
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = _PMOSNumberofGate * _LengthPMOSBtwMet1 + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS

            else:
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = []



        print('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmp = []
        # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, int(_PMOSNumberofGate / 2 + 1)):
                # _XYCenter=[self._XYCoordinatePMOS[0] -  self._NumberOfPMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 \
                            * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2) == 1:
            for i in range(0, int((_PMOSNumberofGate - 1) / 2 + 1)):
                # _XYCenter=[self._XYCoordinatePMOS[0] - (  (self._NumberOfPMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) \
                            * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmp

        print('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmp = []
        # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, int(_PMOSNumberofGate / 2 + 1)):
                # _XYCenter=[self._XYCoordinatePMOS[0] -  self._NumberOfPMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 \
                            * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2) == 1:
            for i in range(0, int((_PMOSNumberofGate - 1) / 2 + 1)):
                # _XYCenter=[self._XYCoordinatePMOS[0] - (  (self._NumberOfPMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) \
                            * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmp

        print('#########################     Output Routing Coordinates Calculation    ##################################')
        tmp = []
        # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, int(_PMOSNumberofGate / 2)):
                # _XYCenter=[self._XYCoordinatePMOS[0] -  self._NumberOfPMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 \
                            * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2) == 1:
            for i in range(0, int((_PMOSNumberofGate - 1) / 2 + 1)):
                # _XYCenter=[self._XYCoordinatePMOS[0] - (  (self._NumberOfPMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) \
                            * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = tmp

        print('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmp = []
        # _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:  # Even
                tmp.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) \
                            * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
                # _xycoordinatetmp = self.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[self._XYCoordinatePMOS[0] - (self._NumberOfPMOSGate / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]], _WidthX=self._LengthPMOSPO, _WidthY=self._WidthPMOSPO)
            elif (_PMOSNumberofGate % 2) == 1:  # Odd
                tmp.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 \
                            * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'] = tmp

        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  PMOSContact Calculation End                                   '.format(
                self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        print('##################################################### Diff Pin Generation & Coordinates ####################################################')

        self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (
                    self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                    self._DesignParameter['_POLayer']['_XWidth'] / 2)
        self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [[(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +
                                                                                                 self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,_XYCoordinateOfPMOS[0][1]], \
                                                                         [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] +self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                                                                          _XYCoordinateOfPMOS[0][1]]]

        print('##################################################### POLayer Pin Generation & Coordinates ####################################################')
        self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_SLVTLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2
        tmp1 = []
        tmp2 = []
        for i in range(0, len(self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmp1.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], - (
                        self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
            tmp2.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], (
                        self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

        if _PMOSNumberofGate == 1:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
        else:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1



if __name__ == '__main__':
    _PMOSFinger = 5
    _PMOSWidth = 200
    _PMOSChannelLength = 30
    # _GuardringWidth = 1000
    _PMOSDummy = True
    _SLVT = True
    _LVT = False
    _HVT = False


    DesignParameters._Technology = '028nm'
    #    print 'Technology Process', DesignParameters._Technology
    TestObj=_Pmos(_DesignParameter=None, _Name='Test')
    TestObj._CalculateDesignParameter(_PMOSNumberofGate=_PMOSFinger, _PMOSChannelWidth=_PMOSWidth, _PMOSChannellength=_PMOSChannelLength ,_PMOSDummy=_PMOSDummy, _SLVT=_SLVT ,_LVT=False, _HVT=False)
    #_PMOSNumberofGate=_PMOSFinger, _PMOSChannelWidth=_PMOSWidth, _PMOSChannellength=_PMOSChannelLength ,_PMOSDummy=_PMOSDummy, _SLVT=_SLVT ,_LVT=False, _HVT=False

    TestObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TestObj._DesignParameter)
    testStreamFile = open('./test.gds', 'wb')
    tmp = TestObj._CreateGDSStream(TestObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('##########################################################################################')
    import ftplib

    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('myungguk', 'vmfl!225')
    # ftp.cwd('/mnt/sdd/myungguk/OPUS/ss28nm_workspace')
    # myfile = open('NMOSWithDummy_test.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy_test.gds', myfile)
    # myfile.close()
    # ftp.close()


    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('//mnt//sdc//junung//OPUS//Samsung28n')
    # myfile = open('NMOSWithDummy.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy.gds', myfile)
    # myfile.close()
    # ftp.close()


    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('ljw95', 'dlwodn123')
    ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
    myfile = open('test.gds', 'rb')
    ftp.storbinary('STOR test.gds', myfile)
    myfile.close()
    ftp.close()
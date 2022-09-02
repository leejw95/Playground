import StickDiagram
import DesignParameters
import DRC

import ftplib


class _SSTresistor(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _OPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['OP'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PRESLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0],
                                                            _Datatype=DesignParameters._LayerMapping['PRES'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePort1Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePort2Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateSSTresistorDesignParameter(self, _RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None):
        print('#########################################################################################################')
        print('                                    {}  SSTresistor Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        # systematically modify
        # _XYCoordinateOfOPRES = [[RLength, RWidth]]
        if _RLength % 2 == 0 and _RWidth % 2 == 0:
            _XYCoordinateOfOPRES = [[0, 0]]
        elif _RLength % 2 == 0 and _RWidth % 2 == 1:
            _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
        elif _RLength % 2 == 1 and _RWidth % 2 == 0:
            _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
        elif _RLength % 2 == 1 and _RWidth % 2 == 1:
            _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]

        if _RLength % (2 * MinSnapSpacing) != 0 or _RWidth % (2 * MinSnapSpacing) != 0:
            raise Exception("Only even number can be generated")


        print('#############################     OP Layer Calculation    ################################################')
        # OP minimum area >= 370
        # PRES minimum space to (PC not touching OP) >= 240
        self._DesignParameter['_OPLayer']['_XWidth'] = _RLength - _DRCObj._PRESlayeroverPoly * 2 + _DRCObj._OPlayeroverPoly * 2 # _OPlayeroverPoly = 200 (checked DRC rule)
        self._DesignParameter['_OPLayer']['_YWidth'] = _RWidth - _DRCObj._PolyoverOPlayer * 2 - _DRCObj._PRESlayeroverPoly * 2 # _PRESlayeroverPoly = 240
        if self._DesignParameter['_OPLayer']['_YWidth'] < _DRCObj._PolyoverOPlayer: #_PolyoverOPlayer = 400
            raise NotImplementedError
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print('#############################     POLY Layer Calculation    ##############################################')
        self._DesignParameter['_POLayer']['_XWidth'] = _RLength - _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_POLayer']['_YWidth'] = _RWidth - _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print('#############################     PRES Layer Calculation    ##############################################')
        self._DesignParameter['_PRESLayer']['_XWidth'] = _RLength
        self._DesignParameter['_PRESLayer']['_YWidth'] = _RWidth
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print('#############################     PIMP Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PRESLayer']['_XWidth']
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PRESLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print('#############################     CONT Layer Calculation    ##############################################')
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        _NumofCOXmax = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth * 2 - _DRCObj._CoMinSpace) # _CoMinEnclosureByPO2 = 12
                           // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 2 # _CoMinSpace = 60
        _NumofCOYmax = int(((self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OPLayer']['_YWidth']) // 2 - _DRCObj._CoMinWidth * 2 - _DRCObj._CoMinSpace
                            - _DRCObj._CoMinSpace2OP - _DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 2 # _CoMinSpace2OP = 200

        if _NumofCOX == None:
            _NumofCOX = _NumofCOXmax
        if _NumofCOY == None:
            if DesignParameters._Technology != '028nm':
                _NumofCOY = 1
            else:
                _NumofCOY = _NumofCOYmax

        if _NumofCOY > 1:
            _NumofCOX = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth * 2 - _DRCObj._CoMinSpace)  # _CoMinEnclosureByPO2 = 12
                            // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 2

        if _NumofCOX > _NumofCOXmax or _NumofCOY > _NumofCOYmax:
            raise NotImplementedError

        tmp_cont = []
        if _NumofCOY == 1: # DRC CoMinSpace
            for i in range(_NumofCOX):
                for j in range(_NumofCOY):
                    if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                    elif _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]] -> consider Y coordinate by add/sub MinSnapSpacing / 2.0
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                        _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                        + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                    elif _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]] -> consider X coordinate by add/sub MinSnapSpacing / 2.0
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                    elif _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]] -> consider X&Y coordinates by add/sub MinSnapSpacing / 2.0
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[0][1] +  MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                             _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                             _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

        else: # DRC CoMinSpace2
            for i in range(_NumofCOX):
                for j in range(_NumofCOY):
                    if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                    elif _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                    elif _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 +
                                            _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                    elif _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]
                        if (_NumofCOX % 2 == 0):
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                             + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                        else:
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            tmp_cont.append([_XYCoordinateOfOPRES[0][0] + MinSnapSpacing / 2.0 - (_NumofCOX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)
                                            + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                            + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp_cont

        print('#########################     Port1 Routing Coordinates Calculation    ####################################')
        tmp_p1_route = []
        if _NumofCOY == 1:
            if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + _DRCObj._CoMinWidth // 2)])

        else:
            if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]
                tmp_p1_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = tmp_p1_route

        print('#########################     Port2 Routing Coordinates Calculation    ####################################')
        tmp_p2_route = []
        if _NumofCOY == 1:
            if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

        else:
            if _RLength % 2 == 0 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[0, 0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 0 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 0: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

            if _RLength % 2 == 1 and _RWidth % 2 == 1: # _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]
                tmp_p2_route.append([_XYCoordinateOfOPRES[0][0],
                                     _XYCoordinateOfOPRES[0][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2
                                     + _DRCObj._CoMinSpace2OP + (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = tmp_p2_route

        print(
            '#############################     Metal1 Layer Calculation    #############################################')
        if _NumofCOY == 1:
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_NumofCOX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)\
                                                             + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)\
                                                             + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO4 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0],
                                                                     self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0]]

        else:
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_NumofCOX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)\
                                                             + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_NumofCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)\
                                                             + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO4 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0],
                                                                     self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0]]




if __name__ == '__main__':
    _RWidth = 1680
    _RLength = 7372
    _NumofCOX = None
    _NumofCOY = 2

    DesignParameters._Technology = '028nm'
    SSTresistorObj = _SSTresistor(_DesignParameter=None, _Name='_SSTresistor')
    SSTresistorObj._CalculateSSTresistorDesignParameter(_RWidth=_RWidth, _RLength=_RLength, _NumofCOX=_NumofCOX,_NumofCOY=_NumofCOY)
    SSTresistorObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SSTresistorObj._DesignParameter)
    testStreamFile = open('./_SSTresistor.gds', 'wb')
    tmp = SSTresistorObj._CreateGDSStream(SSTresistorObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############################    Transporting to FTP server    ########################################')
    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_SSTresistor.gds', 'rb')
    ftp.storbinary('STOR _SSTresistor.gds', myfile)
    myfile.close()
    ftp.close()


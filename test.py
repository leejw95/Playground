import StickDiagram
import DesignParameters
import DRC


class _test(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _SLVT=False, _LVT=False, _HVT=False)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                          _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                               _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _SLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],
                                                            _Datatype=DesignParameters._LayerMapping['SLVT'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _LVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVT'][0],
                                                            _Datatype=DesignParameters._LayerMapping['LVT'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _HVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['HVT'][0],
                                                            _Datatype=DesignParameters._LayerMapping['HVT'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),

                _PDKLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PDK'][0],
                                                           _Datatype=DesignParameters._LayerMapping['PDK'][1],
                                                           _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                            _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _NPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _WELLBodyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['WELLBODY'][0],
                                                                _Datatype=DesignParameters._LayerMapping['WELLBODY'][1],
                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PCCRITLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                              _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                      _NMOSDummy=None, _SLVT=None, _LVT=None, _HVT=None):

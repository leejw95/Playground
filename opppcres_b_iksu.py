import math
import copy

#
import StickDiagram
import DesignParameters
import DRC

from Private import MyInfo


class Resistor_OPPPC(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None, _RoutingWidth=None, _Series=False, _Parallel=False, _Dummy=False)
    '''
    # Input Variables
        _ResWidth         : Stripe Width, <number>
        _ResLength        : Stripe Length, <number>
        _NumCOY           : Contact Rows, <number>             | default 1 (if None)
        _NumStripes       : Number of Parallel/Series Stripes  | default 1 (if None)
        _RoutingWidth     : gap between poly <number>          | default 114(_PolygateMinSpace2) if None
        _Series/_Parallel : True or False                      | 'All True<T,T>' is not available
        _Dummy            : True or False
    '''

    def __init__(self, _DesignParameter=None, _Name='Resistor_OPPPC'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1]),
                _OPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1]),
                _PRESLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1]),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1]),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None, _RoutingWidth=None, _Series=False, _Parallel=False, _Dummy=False):
        _DRCObj = DRC.DRC()
        _Name = 'Resistor_OPPPC'
        _XYCoordinateOfOPRES = [[0, 0]]
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print('#########################################################################################################')
        print('                                    {}  Opppcres Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        # _DistanceBtwPC = max(_DRCObj._PolygateMinSpace2, _RoutingWidth)  # edge-to-edge
        _DistanceBtwPC = _DRCObj._PolygateMinSpace2 if _RoutingWidth == None else _RoutingWidth     # edge-to-edge
        _DistanceBtwCO = (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)                                # center-to-center
        _NumRes = _NumStripes if (_NumStripes is not None) else 1                                   # # of Resistor Set
        _NumPC = _NumRes + 2 if _Dummy else _NumRes
        _NumCOX = int((_ResWidth - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // _DistanceBtwCO) + 1
        _NumCOY = _NumCOY if (_NumCOY is not None) else 1


        print('#############################     OP Layer Calculation    ################################################')
        self._DesignParameter['_OPLayer']['_XWidth'] = _ResWidth * _NumPC + _DistanceBtwPC * (_NumPC-1) + _DRCObj._OPlayeroverPoly * 2
        self._DesignParameter['_OPLayer']['_YWidth'] = _ResLength
        if _ResLength < _DRCObj._PolyoverOPlayer:
            raise NotImplementedError
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES


        print('#############################     POLY Layer Calculation    ##############################################')
        PC_YWidth_1 = _ResLength + _DRCObj._PolyoverOPlayer * 2
        PC_YWidth_2 = _ResLength + (_DRCObj._CoMinSpace2OP + (_NumCOY-1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2  # when with many contact rows

        self._DesignParameter['_POLayer']['_XWidth'] = _ResWidth
        self._DesignParameter['_POLayer']['_YWidth'] = max(PC_YWidth_1, PC_YWidth_2)
        tmpXYs = []
        for i in range(0, _NumPC):
            if (_NumPC % 2) == 0:
                tmpXYs.append([_XYCoordinateOfOPRES[0][0] - (_NumPC/2 - 0.5) * (_DistanceBtwPC + _ResWidth) + i * (_DistanceBtwPC + _ResWidth),
                               _XYCoordinateOfOPRES[0][1]])
            else:
                tmpXYs.append([_XYCoordinateOfOPRES[0][0] - (_NumPC - 1)/2 * (_DistanceBtwPC + _ResWidth) + i * (_DistanceBtwPC + _ResWidth),
                               _XYCoordinateOfOPRES[0][1]])
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs


        print('#############################     CONT Layer Calculation    ##############################################')
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmpXYs = []
        for k in range(0,_NumPC):
            for i in range(0, _NumCOX):
                for j in range(0, _NumCOY):
                    if _NumCOX % 2 == 0:
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2 - 0.5) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] - (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * _DistanceBtwCO])
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2 - 0.5) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] + (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * _DistanceBtwCO])
                    else:
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - ((_NumCOX-1)/2) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] - (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * _DistanceBtwCO])
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - ((_NumCOX-1)/2) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] + (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * _DistanceBtwCO])


        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        print('#############################     Metal1 Layer Calculation    #############################################')
        self._DesignParameter['_Met1Layer']['_XWidth'] = (_NumCOX - 1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        self._DesignParameter['_Met1Layer']['_YWidth'] = (_NumCOY - 1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        tmpXYs = []
        for i in range(0, _NumPC):
            tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                           self._DesignParameter['_POLayer']['_XYCoordinates'][i][1] - (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + (_NumCOY-1) * _DistanceBtwCO/2 + _DRCObj._CoMinWidth/2)])
            tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                           self._DesignParameter['_POLayer']['_XYCoordinates'][i][1] + (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + (_NumCOY-1) * _DistanceBtwCO/2 + _DRCObj._CoMinWidth/2)])
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs


        print('#############################     PRES Layer Calculation    ##############################################')
        self._DesignParameter['_PRESLayer']['_XWidth'] = _ResWidth * _NumPC + _DistanceBtwPC * (_NumPC-1) + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print('#############################     PIMP Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PRESLayer']['_XWidth']
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PRESLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES


        print('#############################     ETC. Options Calculation    ##############################################')
        if _Parallel:
            self._DesignParameter['_Met1Port'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1])
            self._DesignParameter['_Met1Port']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth'] + (_NumRes-1) * (_DistanceBtwPC + _ResWidth)
            self._DesignParameter['_Met1Port']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_Met1Port']['_XYCoordinates'] = [[_XYCoordinateOfOPRES[0][0], -self._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]],
                                                                    [_XYCoordinateOfOPRES[0][0], +self._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]]]
        elif _Series:
            print('Series')

        if _Dummy:
            self._DesignParameter['_Met1DummyRoute'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1])
            self._DesignParameter['_Met1DummyRoute']['_XWidth'] = _DRCObj._Metal1MinWidth
            self._DesignParameter['_Met1DummyRoute']['_YWidth'] = 2 * abs(self._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            self._DesignParameter['_Met1DummyRoute']['_XYCoordinates'] = [self._DesignParameter['_POLayer']['_XYCoordinates'][0],
                                                                          self._DesignParameter['_POLayer']['_XYCoordinates'][-1]]


if __name__ == '__main__':

    _ResWidth = 3000
    _ResLength = 2300
    _NumCOY = 4
    _NumStripes = 5
    _RoutingWidth = None
    _Series = False
    _Parallel = True
    _Dummy = True

    _fileName = 'Resistor_OPPPC.gds'
    libname = 'TEST_OPPPCRES'

    # Generate Layout Object
    OpppcresObj = Resistor_OPPPC(_DesignParameter=None, _Name='Resistor_OPPPC')
    OpppcresObj._CalculateDesignParameter(_ResWidth=_ResWidth, _ResLength=_ResLength,
                                          _NumCOY=_NumCOY, _NumStripes=_NumStripes, _RoutingWidth=_RoutingWidth,
                                          _Series=_Series, _Parallel=_Parallel, _Dummy=_Dummy)
    OpppcresObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=OpppcresObj._DesignParameter)

    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = OpppcresObj._CreateGDSStream(OpppcresObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

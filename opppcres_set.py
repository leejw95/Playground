import math
import copy

#
import StickDiagram
import DesignParameters
import DRC

from Private import FileManage
from Private import MyInfo


class ResistorSet(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None)
    '''
    # Input Variables
        _ResWidth   : Stripe Width, <number>
        _ResLength  : Stripe Length, <number>
        _NumCOY     : Contact Rows, <number>            | default 1 (if None)
        _NumStripes : Number of Parallel/Series Stripes | default 1 (if None)
    
    '''


    def __init__(self, _DesignParameter=None, _Name='ResistorSet'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _OPLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0],_Datatype=DesignParameters._LayerMapping['OP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _PRESLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0],_Datatype=DesignParameters._LayerMapping['PRES'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePort1Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePort2Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
           )

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None):
        _DRCObj = DRC.DRC()
        _Name = 'ResistorSet'

        print ('#########################################################################################################')
        print ('                                    {}  Opppcres Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')
        _DistanceBtwPC = _DRCObj._PolygateMinSpace2                   # edge-to-edge
        _DistanceBtwCO = (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)  # center-to-center
        _NumRes = _NumStripes if (_NumStripes is not None) else 1     # Number of Resistor Set
        _NumCOX = int((_ResWidth - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // _DistanceBtwCO) + 1
        _NumCOY = _NumCOY if (_NumCOY is not None) else 1

        _XYCoordinateOfOPRES = [[0,0]]

        print ('#############################     OP Layer Calculation    ################################################')
        self._DesignParameter['_OPLayer']['_XWidth'] = _ResWidth * _NumRes + _DistanceBtwPC * (_NumRes-1) + _DRCObj._OPlayeroverPoly * 2
        self._DesignParameter['_OPLayer']['_YWidth'] = _ResLength
        if _ResLength < _DRCObj._PolyoverOPlayer:
            raise NotImplementedError
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES


        print ('#############################     POLY Layer Calculation    ##############################################')
        PC_YWidth_1 = _ResLength + _DRCObj._PolyoverOPlayer * 2
        PC_YWidth_2 = _ResLength + (_DRCObj._CoMinSpace2OP + (_NumCOY-1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2  # when with many contact rows

        self._DesignParameter['_POLayer']['_XWidth'] = _ResWidth
        self._DesignParameter['_POLayer']['_YWidth'] = max(PC_YWidth_1, PC_YWidth_2)
        tmpXYs = []
        for i in range(0, _NumRes):
            if (_NumRes % 2) == 0:
                tmpXYs.append([_XYCoordinateOfOPRES[0][0] - (_NumRes/2 - 0.5) * (_DistanceBtwPC + _ResWidth) + i * (_DistanceBtwPC + _ResWidth),
                               _XYCoordinateOfOPRES[0][1]])
            else:
                tmpXYs.append([_XYCoordinateOfOPRES[0][0] - (_NumRes - 1)/2 * (_DistanceBtwPC + _ResWidth) + i * (_DistanceBtwPC + _ResWidth),
                               _XYCoordinateOfOPRES[0][1]])
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs


        print ('#############################     CONT Layer Calculation    ##############################################')
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmpXYs = []
        for k in range(0,_NumRes):
            for i in range(0, _NumCOX):
                for j in range(0, _NumCOY):
                    if _NumCOX % 2 == 0:
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2 - 0.5) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] - (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * _DistanceBtwCO])
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2 - 0.5) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] + (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * _DistanceBtwCO])
                    else:
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] - (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * _DistanceBtwCO])
                        tmpXYs.append([self._DesignParameter['_POLayer']['_XYCoordinates'][k][0] - (_NumCOX/2) * _DistanceBtwCO + i * _DistanceBtwCO,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][k][1] + (self._DesignParameter['_OPLayer']['_YWidth']/2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * _DistanceBtwCO])

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        print ('#########################     Port1 Routing Coordinates Calculation    ####################################')
        tmpXYs = []
        tmpXYs.append([_XYCoordinateOfOPRES[0][0],
                       _XYCoordinateOfOPRES[0][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP + (_NumCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])
        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = tmpXYs

        # Downward

        print ('#########################     Port2 Routing Coordinates Calculation    ####################################')
        tmpXYs = []
        tmpXYs.append([_XYCoordinateOfOPRES[0][0],
                       _XYCoordinateOfOPRES[0][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + (_NumCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])
        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = tmpXYs

        #Upward

        print ('#############################     Metal1 Layer Calculation    #############################################')
        self._DesignParameter['_Met1Layer']['_XWidth'] = (_NumCOX - 1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        self._DesignParameter['_Met1Layer']['_YWidth'] = (_NumCOY - 1) * _DistanceBtwCO + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0], self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0]]


        print ('#############################     PRES Layer Calculation    ##############################################')
        self._DesignParameter['_PRESLayer']['_XWidth'] = _ResWidth * _NumRes + _DistanceBtwPC * (_NumRes-1) + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES

        print ('#############################     PIMP Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PRESLayer']['_XWidth']
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PRESLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES


if __name__ == '__main__':

    _ResWidth = 500
    _ResLength = 1000
    _NumCOY = 3
    _NumStripes = 4

    _fileName = 'Opppcres_set.gds'
    libname = 'TEST_OPPPCRES'

    # Generate Layout Object
    OpppcresObj = ResistorSet(_DesignParameter=None, _Name='Opppcres_set')
    OpppcresObj._CalculateDesignParameter(_ResWidth=_ResWidth, _ResLength=_ResLength, _NumCOY=_NumCOY, _NumStripes=_NumStripes)
    OpppcresObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=OpppcresObj._DesignParameter)

    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = OpppcresObj._CreateGDSStream(OpppcresObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)

    FileManage.Upload2FTP(
        server=My.server,
        user=My.ID,
        password=My.PW,
        directory=My.Dir_GDS,
        filename=_fileName
    )

    FileManage.StreamIn(
        server=My.server,
        port=22,
        ID=My.ID,
        PW=My.PW,
        Dir_Work=My.Dir_Work,
        Dir_GDS=My.Dir_GDS,
        libname=libname,
        filename=_fileName,
        tech=DesignParameters._Technology
    )

    print ('###############      Finished      ##################')
# end of 'main():' ---------------------------------------------------------------------------------------------

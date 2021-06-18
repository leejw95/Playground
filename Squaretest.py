import StickDiagram
import DesignParameters
import user_define_exceptions
import DRC

import ftplib
from ftplib import FTP
import base64

import sys


class _Square(StickDiagram._StickDiagram):

    #_ParametersForDesignCalculation= dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False, _SLVT=False)
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(

                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                              _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                              _XYCoordinates=[],_XWidth=400, _YWidth=400),
                #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?

                                                    _SLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['SLVT'][1],
                                                                                                _XYCoordinates=[], _XWidth=400, _YWidth=400),

                                                    _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                   _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                   _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                              _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                              _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                              _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                              _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                              _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                              _XYCoordinates=[],_XWidth=400, _YWidth=400),

                                                    _PCCRITLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                                                                  _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                                                                  _XYCoordinates=[], _XWidth=400, _YWidth=400),

                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

                                                    _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                    _XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                    _XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                   )


        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _sqfunction(self, _XWidth = None, _YWidth = None):
        self._DesignParameter['_POLayer']['_XWidth'] = _XWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _YWidth
        self._DesignParameter['_POLayer']['_XYCoordinates'] =[[0 , 0]]
        self._DesignParameter['_Met1Layer']['_XWidth'] = _X1Width
        self._DesignParameter['_Met1Layer']['_YWidth'] = _Y1Width
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [[0,400]]
        self._DesignParameter['_COLayer']['_XWidth'] = _X2Width
        self._DesignParameter['_COLayer']['_YWidth'] = _Y2Width
        self._DesignParameter['_COLayer']['_XYCoordinates'] = [[100, 100]]

        #print('x')

        #print('x')

if __name__=='__main__':
    _a = 1000
    _b = 300
    _X1Width = 30
    _Y1Width = 800
    _X2Width = 100
    _Y2Width = 800
    # _GuardringWidth = 1000
    # _PMOSDummy = True
    # _SLVT = True
    # _Guardring = True
    DesignParameters._Technology='028nm'
    print ('Technology Process', DesignParameters._Technology)
    SquareObj=_Square(_DesignParameter=None, _Name='Square')
    #SquareObj._CalculatePMOSDesignParameter(_PMOSNumberofGate=_PMOSFinger, _PMOSChannelWidth=_PMOSWidth, _PMOSChannellength=_PMOSChannelLength ,_PMOSDummy=_PMOSDummy, _SLVT=_SLVT)
    SquareObj._sqfunction(_a,_b)
    #SquareObj._sqfunction(_X1Width, _Y1Width)
    #SquareObj._sqfunction(_X2Width, _Y2Width)
    SquareObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SquareObj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')
    tmp=SquareObj._CreateGDSStream(SquareObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('##########################################################################################')
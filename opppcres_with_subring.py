import math
import copy

#
import StickDiagram
import DesignParameters
import DRC
from Private import FileManage
from Private import MyInfo

#
import opppcres_b_iksu
import psubring


class OpppcresWithSubring(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None, _RoutingWidth=None, _Dummy=False, _SubringWidth=None)


    def __init__(self, _DesignParameter=None, _Name='Resistor_OPPPC_wSubRing'):
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


    def _CalculateDesignParameter(self, _ResWidth=None, _ResLength=None, _NumCOY=None, _NumRows=None, _NumStripes=None, _RoutingWidth=None, _Dummy=False, _SubringWidth=None):
        _DRCObj = DRC.DRC()
        _Name = 'OpppcresWithSubring'
        _XYCoordinateOfOPRES = [[0, 0]]
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print('##############################     Resistor_OPPPCRES Generation    ########################################')
        _OPPPCRES_inputs = copy.deepcopy(opppcres_b_iksu.Resistor_OPPPC._ParametersForDesignCalculation)
        _OPPPCRES_inputs['_ResWidth'] = _ResWidth
        _OPPPCRES_inputs['_ResLength'] = _ResLength
        _OPPPCRES_inputs['_NumCOY'] = _NumCOY
        _OPPPCRES_inputs['_NumStripes'] = _NumStripes
        _OPPPCRES_inputs['_RoutingWidth'] = _RoutingWidth
        _OPPPCRES_inputs['_Series'] = False
        _OPPPCRES_inputs['_Parallel'] = True
        _OPPPCRES_inputs['_Dummy'] = _Dummy
        self._DesignParameter['OPPCRES'] = self._SrefElementDeclaration(_DesignObj=opppcres_b_iksu.Resistor_OPPPC(_DesignParameter=None, _Name='OpppcresIn{}'.format(_Name)))[0]
        self._DesignParameter['OPPCRES']['_DesignObj']._CalculateDesignParameter(**_OPPPCRES_inputs)

        distanceBtwM1Port = abs(self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][0][1]
                                - self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][1][1])


        print('##############################     SubRing Generation    ########################################')
        XWidthOfSubring1 = self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoPRES
        XWidthOfSubring2 = self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_OPLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoOP
        XWidthOfSubring = max(XWidthOfSubring1, XWidthOfSubring2)
        YWidthOfSubring = self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] * _NumRows \
                          - (self._DesignParameter['OPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] - distanceBtwM1Port) * (_NumRows-1) \
                          + 2*_DRCObj._RXMinSpacetoPRES

        _PMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _PMOSSubringinputs['_PType'] = True
        _PMOSSubringinputs['_XWidth'] = XWidthOfSubring
        _PMOSSubringinputs['_YWidth'] = YWidthOfSubring
        _PMOSSubringinputs['_Width'] = _SubringWidth
        self._DesignParameter['_Subring'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='SubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_Subring']['_DesignObj']._CalculatePSubring(**_PMOSSubringinputs)


        ''' Coordinates Settings '''
        tmpXYs = []
        for i in range(0, _NumRows):
            if (_NumRows % 2) == 0:
                tmpXYs.append([+(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows / 2 - 0.5))])
                tmpXYs.append([-(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows / 2 - 0.5))])
            else:
                tmpXYs.append([+(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows - 1) / 2)])
                tmpXYs.append([-(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows - 1) / 2)])

        self._DesignParameter['OPPCRES']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['_Subring']['_XYCoordinates'] = [[-(XWidthOfSubring + _SubringWidth)/2, 0],
                                                               [+(XWidthOfSubring + _SubringWidth)/2, 0]]


        '''    
        Next Work...
        Connect VSS
        Connect Port when multiple rows
        Outline coordinates or XYWidth
        
        '''


if __name__ == '__main__':

    _ResWidth = 3000
    _ResLength = 2300
    _NumCOY = 3
    _NumRows = 2
    _NumStripes = 5
    _RoutingWidth = None
    _Dummy = True
    _SubringWidth = 1000

    _fileName = 'OpppcresWithSubring.gds'
    libname = 'TEST_OPPPCRES'

    # Generate Layout Object
    OpppcresObj = OpppcresWithSubring(_DesignParameter=None, _Name='OpppcresWithSubring')
    OpppcresObj._CalculateDesignParameter(_ResWidth=_ResWidth, _ResLength=_ResLength,
                                          _NumCOY=_NumCOY, _NumRows=_NumRows, _NumStripes=_NumStripes,
                                          _RoutingWidth=_RoutingWidth,
                                          _Dummy=_Dummy, _SubringWidth=_SubringWidth)
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

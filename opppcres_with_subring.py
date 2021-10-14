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
        self._DesignParameter['OPPPCRES'] = self._SrefElementDeclaration(_DesignObj=opppcres_b_iksu.Resistor_OPPPC(_DesignParameter=None, _Name='OpppcresIn{}'.format(_Name)))[0]
        self._DesignParameter['OPPPCRES']['_DesignObj']._CalculateDesignParameter(**_OPPPCRES_inputs)

        distanceBtwM1Port = abs(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][0][1]
                                - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][1][1])


        print('##############################     SubRing Generation    ########################################')
        XWidthOfSubring1 = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoPRES, MinSnapSpacing*2)
        XWidthOfSubring2 = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_OPLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoOP, MinSnapSpacing*2)
        XWidthOfSubring = max(XWidthOfSubring1, XWidthOfSubring2)
        YWidthOfSubring = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] * _NumRows
                                                  - (self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] - distanceBtwM1Port) * (_NumRows-1)
                                                  + 2*_DRCObj._RXMinSpacetoPRES, MinSnapSpacing*2)

        PSubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PSubringInputs['_PType'] = True
        PSubringInputs['_XWidth'] = XWidthOfSubring
        PSubringInputs['_YWidth'] = YWidthOfSubring
        PSubringInputs['_Width'] = _SubringWidth
        self._DesignParameter['_Subring'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='SubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_Subring']['_DesignObj']._CalculatePSubring(**PSubringInputs)


        ''' Coordinates Settings '''
        tmpXYs = []
        for i in range(0, _NumRows):
            if (_NumRows % 2) == 0:
                tmpXYs.append([+(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows / 2 - 0.5))])
                tmpXYs.append([-(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows / 2 - 0.5))])
            else:
                tmpXYs.append([+(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows - 1) / 2)])
                tmpXYs.append([-(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - (_NumRows - 1) / 2)])

        self._DesignParameter['OPPPCRES']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['_Subring']['_XYCoordinates'] = [[-(XWidthOfSubring + _SubringWidth)/2, 0],
                                                               [+(XWidthOfSubring + _SubringWidth)/2, 0]]



        M1PortXYs = []  # For internal calculation
        for i in range(0, _NumRows+1):
            M1PortXYs.append([+(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - _NumRows/2.0)])
            M1PortXYs.append([-(XWidthOfSubring + _SubringWidth)/2, distanceBtwM1Port * (i - _NumRows/2.0)])

        '''    
        Next Work...
        Connect VSS
        Connect Port when multiple rows
        Outline coordinates or XYWidth
        
        '''

        ''' Connect VSS - horizontal '''
        tmpXYs = []
        for i in range(0, (_NumRows//2 + 1)):
            tmpXYs.append([0, distanceBtwM1Port * (_NumRows/2.0 - i*2)])

        self._DesignParameter['_VSSRoutingH'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['_VSSRoutingH']['_XWidth'] = _SubringWidth + XWidthOfSubring * 2
        self._DesignParameter['_VSSRoutingH']['_YWidth'] = self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_YWidth']
        self._DesignParameter['_VSSRoutingH']['_XYCoordinates'] = tmpXYs


        self._DesignParameter['_VSSRoutingH2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['_VSSRoutingH2']['_XWidth'] = _SubringWidth + XWidthOfSubring * 2
        self._DesignParameter['_VSSRoutingH2']['_YWidth'] = (YWidthOfSubring + _SubringWidth - distanceBtwM1Port * _NumRows)/2
        self._DesignParameter['_VSSRoutingH2']['_XYCoordinates'] = [[0, ((YWidthOfSubring + _SubringWidth)/2 + abs(M1PortXYs[0][1]))/2]]   # Need MinSnapSpacing and lower one when even odd




if __name__ == '__main__':

    _ResWidth = 3000
    _ResLength = 1000
    _NumCOY = 3
    _NumRows = 4
    _NumStripes = 4
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

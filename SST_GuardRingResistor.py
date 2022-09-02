import StickDiagram
import DesignParameters
import copy
import DRC
import SST_resistor
import psubring


class _SST_GuardRingResistor(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NumofRes=None, _PType = True, _XWidth = None, _YWidth = None, _Width = None,
                                           _RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateSSTGuardRingResistorParameter(self, _NumofRes=None, _PType = True, _XWidth = None, _YWidth = None, _Width = None,
                                                _RWidth=None, _RLength=None, _NumofCOX=None, _NumofCOY=None):

        print ('#########################################################################################################')
        print ('                                  {}  GuardRing Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        PContinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PContinputs['_PType'] = _PType
        PContinputs['_XWidth'] = _XWidth
        PContinputs['_YWidth'] = _YWidth
        PContinputs['_Width'] = _Width

        Resinputs = copy.deepcopy(SST_resistor._SSTresistor._ParametersForDesignCalculation)
        Resinputs['_RWidth'] = _RWidth
        Resinputs['_RLength'] = _RLength
        Resinputs['_NumofCOX'] = _NumofCOX
        Resinputs['_NumofCOY'] = _NumofCOY

        self._DesignParameter['_SSTGuardRing'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='_SSTGuardRingIn{}'.format(_Name)))[0]
        self._DesignParameter['_SSTGuardRing']['_DesignObj']._CalculatePSubring(**dict(_PType = True, _XWidth = 2000.0, _YWidth = 2000.0, _Width = _Width))

        self._DesignParameter['SSTresistor'] = self._SrefElementDeclaration(_DesignObj=SST_resistor._SSTresistor(_DesignParameter=None, _Name='_SSTResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['SSTresistor']['_DesignObj']._CalculateSSTresistorDesignParameter(**Resinputs)


        _XYCoordinateOfGuardring = [[0, 0]]

        print('#############################     GR Space Calculation    ##############################################')

        _PRESMinSpace = 400     # There's no DRC value in DRC.py
        _PRESMinEnclosureOfPP = 200     # There's no DRC value in DRC.py
        _PpMinExtensiononPactive = 80
        _GR_XWidth = _NumofRes * (_RLength + _PRESMinSpace) - _PRESMinSpace
        _GR_YWidth = _RWidth

        print('#############################     SST_resistor Calculation    ##############################################')

        tmp_res = []
        if _NumofRes % 2 == 0:
            for i in range(_NumofRes):
                tmp_res.append([_XYCoordinateOfGuardring[0][0] - (_NumofRes // 2 - 0.5) * (_RLength + _PRESMinSpace)
                            + i * (_RLength + _PRESMinSpace), _XYCoordinateOfGuardring[0][1]])
        else:
            for i in range(_NumofRes):
                tmp_res.append([_XYCoordinateOfGuardring[0][0] - (_NumofRes // 2) * (_RLength + _PRESMinSpace)
                            + i * (_RLength + _PRESMinSpace), _XYCoordinateOfGuardring[0][1]])
        self._DesignParameter['SSTresistor']['_XYCoordinates'] = tmp_res

        print('#############################     GuardRing Calculation    ##############################################')

        # PRES to RX = 230
        # XWidth, YWidth = metal to metal
        if _XWidth == None :
            _XWidth_Min = float(_GR_XWidth + _DRCObj._RXMinSpacetoPRES * 2)
            _XWidth=_XWidth_Min
        if _YWidth == None:
            _YWidth_Min = float(_GR_YWidth + _DRCObj._RXMinSpacetoPRES * 2)
            _YWidth = _YWidth_Min
        self._DesignParameter['_SSTGuardRing']['_XYCoordinates'] = _XYCoordinateOfGuardring

        self._DesignParameter['_SSTGuardRing']['_DesignObj']._CalculatePSubring(**dict(_XWidth=_XWidth, _YWidth=_YWidth, _Width=_Width))

if __name__ == '__main__':
    _NumofRes = 2
    _PType = True
    _XWidth = None
    _YWidth = None
    _Width = 600 # metal1 width
    _RWidth = 1680
    _RLength = 7372
    _NumofCOX = None
    _NumofCOY = 1


    DesignParameters._Technology = '028nm'
    TopObj = _SST_GuardRingResistor(_DesignParameter=None, _Name='_SST_GuardRingResistor')
    TopObj._CalculateSSTGuardRingResistorParameter(_NumofRes=_NumofRes, _PType = _PType, _XWidth = _XWidth, _YWidth = _YWidth, _Width = _Width, _RWidth=_RWidth, _RLength=_RLength, _NumofCOX=_NumofCOX, _NumofCOY=_NumofCOY)
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_SST_GuardRingResistor.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('##########################################################################################')
    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_SST_GuardRingResistor.gds', 'rb')
    ftp.storbinary('STOR _SST_GuardRingResistor.gds', myfile)
    myfile.close()
    ftp.close()
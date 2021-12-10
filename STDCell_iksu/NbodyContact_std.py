import StickDiagram
import DesignParameters
import DRC

from Private import MyInfo
import DRCchecker


class _NbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(NumCOX=None,
                                           Pitch=None,

                                           Met1YWidth=None,
                                           Met2YWidth=None,
                                           )

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _NPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )
        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateDesignParameter(self,
                                  NumCOX=None,
                                  Pitch=None,
                                  Met2YWidth=None,
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _XYCoord = [[0, 0]]

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        if Pitch == None:
            LengthBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=NumCOX, NumOfCOY=1)
        else:
            LengthBtwCO = Pitch


        print('#############################     DIFF Layer Calculation    ##############################################')
        self._DesignParameter['_ODLayer']['_XWidth'] = NumCOX * Pitch
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoord


        if DesignParameters._Technology != '028nm':  # @ Samsung 28nm, There is No 'NPLayer(NIMP)'
            print('#############################     NIMP  Layer Calculation    ##############################################')
            self._DesignParameter['_NPLayer']['_XWidth'] = max(self.getXWidth('_ODLayer') + 2 * _DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth)
            self._DesignParameter['_NPLayer']['_YWidth'] = max(self.getYWidth('_ODLayer') + 2 * _DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth)
            self._DesignParameter['_NPLayer']['_XYCoordinates'] = self.getXY('_ODLayer')


        print('###########################     Metal1  Layer Calculation    ##############################################')
        self._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('_ODLayer')
        self._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('_ODLayer')
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self.getXY('_ODLayer')


        print('#############################     CONT Layer Calculation    ##############################################')
        tmpXYs = []
        for i in range(0, NumCOX):
            tmpXYs.append([_XYCoord[0][0] - (NumCOX - 1) / 2.0 * LengthBtwCO + i * LengthBtwCO,
                           _XYCoord[0][1]])

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')


if __name__ == '__main__':

    libname = 'TEST_MOS'
    cellname = 'NbodyContact'
    _fileName = cellname + '.gds'

    ''' Generate Layout Object '''
    LayoutObj = _NbodyContact(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateNbodyContactDesignParameter(_NumberOfNbodyCOX=30, _NumberOfNbodyCOY=1)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      #############################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
    )
    Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    print('#############################      Finished      ################################')

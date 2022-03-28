import StickDiagram
import DesignParameters
import DRC


class _PbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict( _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400), #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    # _PDKLayer=dict(_DesignParametertype=1,_Layer=DesignParameters._LayerMapping['PDK'][0], _Datatype=DesignParameters._LayerMapping['PDK'][1],_XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


        
    def _CalculateDesignParameter(self,  _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None ):
        print ('#########################################################################################################')
        print(('                                  {}  PbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')
        _DRCObj=DRC.DRC()
        _XYCoordinateOfPbodyContact = [[0,0]]





        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX,NumOfCOY=_NumberOfPbodyCOY )

        print ('#############################     DIFF Layer Calculation    ##############################################')

        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfPbodyContact

        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOX - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOY - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        print ('#############################     PIMP  Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XYCoordinates']=_XYCoordinateOfPbodyContact

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

            if self._DesignParameter['_PPLayer']['_YWidth'] < 170:
                self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
        else:
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive



        print ('###########################     Metal1  Layer Calculation    ##############################################')

        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfPbodyContact

        if _Met1XWidth==None and _Met1YWidth == None:
            self._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        elif _Met1XWidth!=None and _Met1YWidth == None:
            self._DesignParameter['_Met1Layer']['_XWidth'] = _Met1XWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        elif _Met1XWidth==None and _Met1YWidth != None:
            self._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_Met1Layer']['_YWidth'] = _Met1YWidth

        else:
            self._DesignParameter['_Met1Layer']['_XWidth'] =_Met1XWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] =_Met1YWidth


        print ('#############################     CONT Layer Caculation    ##############################################')

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmp=[]
        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX,NumOfCOY=_NumberOfPbodyCOY )


        for i in range(0, _NumberOfPbodyCOX):
            for j in range(0, _NumberOfPbodyCOY):

                if (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX // 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY // 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]
                elif (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX // 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY-1)//2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 1 and (_NumberOfPbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX -1) // 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY // 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 1 and (_NumberOfPbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX -1) // 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY-1)//2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp






        del _DRCObj
        print ('#########################################################################################################')
        print(('                                  {}  PbodyContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')
        



if __name__ == '__main__':
    from Private import MyInfo
    import DRCchecker
    from SthPack import PlaygroundBot

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_BasicArchive'
    cellname = 'PbodyContact'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NumberOfPbodyCOX=3, _NumberOfPbodyCOY=2,
        # _Met1XWidth=1000, _Met1YWidth=500
    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass
        print(
            "=============================   Last Layout Object's Input Parameters are   =============================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print(
            "=========================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = _PbodyContact(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('##################################      Sending to FTP Server...      ##################################')
        Checker = DRCchecker.DRCchecker(
            username=My.ID,
            password=My.PW,
            WorkDir=My.Dir_Work,
            DRCrunDir=My.Dir_DRCrun,
            GDSDir=My.Dir_GDS,
            libname=libname,
            cellname=cellname,
        )
        Checker.Upload2FTP()

        if Mode_DRCCheck:
            print('###############      DRC checking... {0}/{1}      ##################'.format(ii + 1, Num_DRCCheck))
            # Bot.send2Bot(f'Start DRCChecker...\nTotal Number Of Run : {Num_DRCCheck}')
            try:
                Checker.DRCchecker()
            except Exception as e:
                print('Error Occurred: ', e)
                print("=============================   Last Layout Object's Input Parameters are   =============================")
                tmpStr = '\n'.join(f'{k} : {v}' for k,v in InputParams.items())
                print(tmpStr)
                print("=========================================================================================================")

                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\n'
                             f'ErrMsg : {e}\n'
                             f'============================='
                             f'{tmpStr}\n'
                             f'=============================')
            else:
                if (ii + 1) == Num_DRCCheck:
                    Bot.send2Bot(f'Checking DRC Finished.\nTotal Number Of Run : {Num_DRCCheck}')
                    # elapsed time, start time, end time, main python file name
                else:
                    pass
        else:
            Checker.StreamIn(tech=DesignParameters._Technology)

    print('########################################      Finished       ###########################################')
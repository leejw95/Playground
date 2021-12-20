import StickDiagram
import DesignParameters
import DRC
import NMOSWithDummy_iksu
import copy
import ftplib


class _Square(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))


        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _sqfunction(self, _XWidth = None, _YWidth = None, _Width = None, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _Dummy = False, _XVT = None):

        _Name = 'TEST'
        _DRCObj = DRC.DRC()
        self._DesignParameter['_ODLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                              _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                              _XYCoordinates=[],_XWidth=400, _YWidth=400)

        self._DesignParameter['_ODLayer']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter['_ODLayer']['_XWidth'] = _XWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _YWidth

        self._DesignParameter['_Met1Layer']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                _XYCoordinates = [], _Width=100)

        self._DesignParameter['_Met1Layer']['_Width'] = _Width
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [[[200,200],[200,1000]]]

        # _NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
        # _NMOSinputs['_NMOSNumberofGate'] = _Finger
        # _NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
        # _NMOSinputs['_NMOSChannellength'] = _ChannelLength
        # _NMOSinputs['_NMOSDummy'] = _Dummy
        # _NMOSinputs['_XVT'] = _XVT
        # self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle =0, _DesignObj=NMOSWithDummy_iksu._NMOS(_DesignParameter=None, _Name='NMOSIn{}'.format(_Name)))[0]
        # self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)
        # self._DesignParameter['_NMOS']['_XYCoordinates'] =[[300,0]]

        



        print('x')

        #print('x')

if __name__=='__main__':
    _a = 400
    _b = 400
    _c = 300
    _Finger = 5
    _ChannelWidth = 500
    _ChannelLength = 30
    _Dummy = True
    _XVT = 'SLVT'
    SquareObj=_Square(_DesignParameter=None, _Name='Square')
    SquareObj._sqfunction(_a,_b,_c, _Finger, _ChannelWidth, _ChannelLength, _Dummy, _XVT)
    SquareObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SquareObj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')
    tmp=SquareObj._CreateGDSStream(SquareObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    #ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
    myfile = open('testStreamFile.gds', 'rb')
    ftp.storbinary('STOR testStreamFile.gds', myfile)
    myfile.close()
    ftp.close()
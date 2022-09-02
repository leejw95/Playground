import StickDiagram
import DesignParameters
import DRC
import copy
import ljw_test




class _test(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict( Width=None, XWidth=None, YWidth=None,x0=None,y=None,x1=None,x2=None,xp=None,yp=None,xp1=None,yp1=None)
#,x2=None,x3=None,x4=None,x5=None
    # XWidth = None, YWidth = None
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(


                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),

            )



    def _CalculateDesignParameter(self  ,Width=None,XWidth=None, YWidth=None,x0=None,y=None,x1=None,x2=None,xp=None,yp=None,xp1=None,yp1=None):
        # , Width = None x2=None,x3=None,x4=None,x5=None
        DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _Inv = copy.deepcopy(ljw_test._TEST._ParametersForDesignCalculation)
        _Inv['XWidth'] = XWidth
        _Inv['YWidth']= YWidth
        _Inv['Width'] = Width
        _Inv['x0'] = x0
        _Inv['x1'] = x1
        _Inv['y'] = y

        #Width = 2 * (y - DRCObj._Metal1MinSpace3 - YWidth / 2)
        x2 = x1 - x0
        print(Width)
        xp=x2+DRCObj._Metal1MinSpace3
        xp1=xp*2
        yp=1000
        yp1=yp*2

        self._DesignParameter['_test'] = self._SrefElementDeclaration(_DesignObj=ljw_test._TEST(_DesignParameter=None, _Name = '_testIn{}'.format(_Name)))[0]
        self._DesignParameter['_test']['_DesignObj']._CalculateDesignParameter(**_Inv)
        #self._DesignParameter['_test']['_DesignObj']._CalculateDesignParameter(XWidth=None, YWidth=None,Width=None, x0=None,x1=None,y=None)

        self._DesignParameter['_test']['_XYCoordinates'] = [[0,0],[xp,yp],[xp1,yp1]]




           # print(x0)
           # print(x1)
            #print(xp)
            #print(DRCObj._Metal1MinSpace3)

if __name__ == '__main__':

    XWidth = 2000
    YWidth = 1000
    x0 = -2000
    x1 = 2000
    x2=0
    y = 2000
    xp=0
    yp=0
    xp1 = 0
    yp1 = 0



   # for i in range(3):
    #    XCoordinates = XCoordinates + DRCObj._Metal1MinSpace3



    DesignParameters._Technology = '028nm'
    #    print 'Technology Process', DesignParameters._Technology
    TestObj = _test(_DesignParameter=None, _Name='Test')
    TestObj._CalculateDesignParameter( XWidth=XWidth, YWidth=YWidth,x0=x0,y=y,x1=x1,x2=x2,xp=xp,yp=yp,xp1=xp1,yp1=yp1)
    # ,,x2=x2,x3=x3,x4=x4,x5=x5
    TestObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TestObj._DesignParameter)
    testStreamFile = open('./_test.gds', 'wb')
    tmp = TestObj._CreateGDSStream(TestObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('##########################################################################################')
    import ftplib

    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('myungguk', 'vmfl!225')
    # ftp.cwd('/mnt/sdd/myungguk/OPUS/ss28nm_workspace')
    # myfile = open('NMOSWithDummy_test.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy_test.gds', myfile)
    # myfile.close()
    # ftp.close()

    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('//mnt//sdc//junung//OPUS//Samsung28n')
    # myfile = open('NMOSWithDummy.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy.gds', myfile)
    # myfile.close()
    # ftp.close()


    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('ljw95', 'dlwodn123')
    ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')
    myfile = open('_test.gds', 'rb')
    ftp.storbinary('STOR _test.gds', myfile)
    myfile.close()
    ftp.close()
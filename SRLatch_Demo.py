import SRLatch
import DesignParameters
import random

if __name__ == '__main__':
    for _tries in range(1, 51) :
        _Finger1 = random.randint(1, 10)
        _Finger2 = random.randint(1, 10)
        _Finger3 = random.randint(1, 10)
        _Finger4 = random.randint(1, 10)

        _NMOSChannelWidth = random.randrange(200, 400, 2)
        _NPRatio = 2.7
        _PMOSChannelWidth = _NPRatio * _NMOSChannelWidth
        _ChannelLength = 30

        _VDD2VSSHeightAtOneSide = None
        _NumSupplyCoX = None
        _NumSupplyCoY = None

        _FileName = 'SR_Latch_Demo1'
        _STOR_FileName = 'STOR SR_Latch_Demo1.gds'
        # _LibraryName = 'SR_Latch_Demo1'


        _Dummy = True
        _SLVT = True
        _PowerLine = False

        DesignParameters._Technology = '028nm'

        SRLatchObj = SRLatch._SRLatch(_DesignParameter=None, _Name='SR_Latch')
        SRLatchObj._CalculateDesignParameter(_Finger1=_Finger1, _Finger2=_Finger2, _Finger3=_Finger3, _Finger4=_Finger4, \
                                             _NMOSChannelWidth1=_NMOSChannelWidth, _PMOSChannelWidth1=_PMOSChannelWidth,
                                             _NMOSChannelWidth2=_NMOSChannelWidth,
                                             _PMOSChannelWidth2=_PMOSChannelWidth, _NMOSChannelWidth3=_NMOSChannelWidth,
                                             _PMOSChannelWidth3=_PMOSChannelWidth,
                                             _NMOSChannelWidth4=_NMOSChannelWidth, _PMOSChannelWidth4=_PMOSChannelWidth,
                                             _ChannelLength=_ChannelLength, \
                                             _VDD2VSSHeightAtOneSide=_VDD2VSSHeightAtOneSide, _Dummy=_Dummy,
                                             _NumSupplyCoX=_NumSupplyCoX, _NumSupplyCoY=_NumSupplyCoY, \
                                             _SupplyMet1XWidth=None, _SupplyMet1YWidth=None, NumViaPoly2Met1CoX=None, \
                                             NumViaPoly2Met1CoY=None, NumViaPMOSMet12Met2CoX=None,
                                             NumViaPMOSMet12Met2CoY=None, \
                                             NumViaNMOSMet12Met2CoX=None, NumViaNMOSMet12Met2CoY=None,
                                             NumViaPMOSMet22Met3CoX=None, NumViaPMOSMet22Met3CoY=None, \
                                             NumViaNMOSMet22Met3CoX=None, NumViaNMOSMet22Met3CoY=None, _SLVT=_SLVT,
                                             _PowerLine=_PowerLine)

        SRLatchObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SRLatchObj._DesignParameter)
        _fileName = _FileName
        testStreamFile = open('./{}'.format(_fileName), 'wb')

        tmp = SRLatchObj._CreateGDSStream(SRLatchObj._DesignParameter['_GDSFile']['_GDSFile'])

        tmp.write_binary_gds_stream(testStreamFile)

        testStreamFile.close()

        import ftplib

        import base64

        ftp = ftplib.FTP('141.223.22.156')
        ftp.login(base64.b64decode('amljaG8wOTI3'), base64.b64decode('Y2hvODkxNDA2MTYhIQ=='))
        ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
        myfile = open(_FileName, 'rb')
        ftp.storbinary(_STOR_FileName, myfile)
        myfile.close()
        ftp.close()


        import DRCchecker

        a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '/mnt/sdc/jicho0927/OPUS/SAMSUNG28n', '/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run', 'SR_Latch_test', 'SR_Latch_Demo1')

        a.DRCchecker()


        print('_tries = ', _tries)
        print('_SRFinger1 = ', _Finger1)
        print('_SRFinger2 = ', _Finger2)
        print('_SRFinger3 = ', _Finger3)
        print('_SRFinger4 = ', _Finger4)
        print('_NMOSChannelWidth = ', _NMOSChannelWidth)
        print('_PMOSChannelWidth = ', _PMOSChannelWidth)
        print('_Channellength = ', _ChannelLength)

    print ("DRCclean!!")

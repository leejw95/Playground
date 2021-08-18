import SRLatch
import DesignParameters


if __name__ == '__main__':
    _Finger1 = 4
    _Finger2 = 8
    _Finger3 = 8
    _Finger4 = 5

    _NMOSChannelWidth = 300
    _NPRatio = 3
    _PMOSChannelWidth = _NPRatio * _NMOSChannelWidth
    _ChannelLength = 60

    _VDD2VSSHeightAtOneSide = None
    _NumSupplyCoX = 80
    _NumSupplyCoY = 5

    _FileName = 'SR_Latch_DemoX'
    _STOR_FileName = 'STOR SR_Latch_DemoX.gds'
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
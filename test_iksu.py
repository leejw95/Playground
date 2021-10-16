
#
import StickDiagram
import DesignParameters
import DRC
from Private import FileManage
from Private import MyInfo

#
import ViaMet12Met2


if __name__ == '__main__':

    NumCOX = 3
    NumCOY = 2

    _fileName = 'ViaMet12Met2.gds'
    libname = 'TEST_VIA'

    # Generate Layout Object

    ViaMet12Met2Obj = ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test1')
    ViaMet12Met2Obj._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=NumCOX, _ViaMet12Met2NumberOfCOY=NumCOY)
    # ViaMet12Met2Obj._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=NumCOX, _ViaMet12Met2NumberOfCOY=NumCOY)
    # ViaMet12Met2Obj._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=NumCOX, _ViaMet12Met2NumberOfCOY=NumCOY)
    ViaMet12Met2Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet12Met2Obj._DesignParameter)

    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = ViaMet12Met2Obj._CreateGDSStream(ViaMet12Met2Obj._DesignParameter['_GDSFile']['_GDSFile'])
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

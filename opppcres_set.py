import math
import copy

#
import StickDiagram
import DesignParameters
import DRC

from Private import FileManage
from Private import MyInfo
import opppcres_b

class ResistorSet(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ResistorWidth=None, _ResistorLength=None, _NumX=None, _NumY=None)

    def __init__(self, _DesignParameter=None, _Name='ResistorSet'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _ResistorWidth=None, _ResistorLength=None, _NumX=None, _NumY=None):

        _DRCObj = DRC.DRC()
        _Name = 'ResistorSet'




        print ('###############################       Opppcres_b Generation      #########################################')
        _Opppcresinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
        _Opppcresinputs['_ResWidth'] = _ResistorWidth
        _Opppcresinputs['_ResLength'] = _ResistorLength
        _Opppcresinputs['_CONUMX'] = None
        _Opppcresinputs['_CONUMY'] = None

        self._DesignParameter['_Opppcres1'] = self._SrefElementDeclaration(
            _DesignObj=opppcres_b._Opppcres(_DesignParameter=None, _Name='OpppcresIn{}'.format(_Name)))[0]
        self._DesignParameter['_Opppcres1']['_DesignObj']._CalculateOpppcresDesignParameter(**_Opppcresinputs)
        self._DesignParameter['_Opppcres1']['_XYCoordinates'] = [[0, 0]]

if __name__ == '__main__':

    _ResistorWidth = 150
    _ResistorLength = 400
    _NumX = None
    _NumY = None

    _fileName = 'Opppcres_b.gds'
    libname = 'TEST_OPPPRES'

    # Generate Layout Object
    print ('Technology Process', DesignParameters._Technology)

    OpppcresObj = ResistorSet(_DesignParameter=None, _Name='Opppcres_set')
    OpppcresObj._CalculateDesignParameter(_ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _NumX=_NumX, _NumY=_NumX)
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
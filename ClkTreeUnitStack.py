import StickDiagram
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaPoly2Met1
import ClkTreeElement
import ClkTreeUnit



import DesignParameters
import user_define_exceptions

import copy


import DRC

import ftplib
from ftplib import FTP
import base64



import sys

class _CLKTreeUnitStack(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(
    

                                     _CLKTreeElementCalculationParameters = copy.deepcopy(ClkTreeElement._ClkTreeElement._ParametersForDesignCalculation),
                                     
                                       


                                     _Dummy=None
                                     )

    def __init__(self, _DesignParameter=None, _Name='ClkTree'):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else : #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
            self._DesignParameter = dict(


                                                    _TopUnit = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= 'TopUnitIn{}'.format(_Name)))[0],
                                                    _BotUnit = self._SrefElementDeclaration(_DesignObj=ClkTreeUnit._CLKTreeUnit(_DesignParameter=None, _Name= 'BotUnitIn{}'.format(_Name)))[0],
                                                    
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)

                                                   )

    def _ResetSrefElement(self):
        tmpDesignName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_DesignParameter=None, _Name=tmpDesignName)                                              
                                                   
    def _CalculateDesignParameter(self, 


  
                                        _CLKTreeElementCalculationParameters = copy.deepcopy(ClkTreeElement._ClkTreeElement._ParametersForDesignCalculation),
                                        


                                     _Dummy=None
                                     ):
        print '#########################################################################################################'
        print '                                    {}  CLK Tree Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'



        _DRCObj=DRC.DRC()

            
        self._DesignParameter['_TopUnit']['_DesignObj']._CalculateDesignParameter(_CLKTreeElementParameters = _CLKTreeElementCalculationParameters,_Dummy=False, _TreeLevel=1, _TotalLevel=1)
        self._DesignParameter['_BotUnit']['_DesignObj']._CalculateDesignParameter(_CLKTreeElementParameters = _CLKTreeElementCalculationParameters,_Dummy=False, _TreeLevel=1, _TotalLevel=1)

        self._DesignParameter['_BotUnit']['_XYCoordinates'] = [[0,0]]
        Ycoord = self._DesignParameter['_BotUnit']['_XYCoordinates'][0][1] + self._DesignParameter['_BotUnit']['_DesignObj']._DesignParameter['_ClkTreeElementTop']['_XYCoordinates'][0][1]
        self._DesignParameter['_TopUnit']['_XYCoordinates'] = [[0,Ycoord]]


        
        del _DRCObj
        
        print '#########################################################################################################'
        print '                                    {}  ClkTree Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'

        


if __name__=='__main__':


                
    ##############TreeStack #####################################################################
    CLKTreeObj=_CLKTreeUnitStack(_DesignParameter=None, _Name='CLKtreeStack')
    CLKTreeObj._CalculateDesignParameter(
    


                                         )

                                         # )

    CLKTreeObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=CLKTreeObj._DesignParameter)
    _fileName='autoClkTree.gds'
    testStreamFile=open('./{}'.format(_fileName),'wb')

    tmp=CLKTreeObj._CreateGDSStream(CLKTreeObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()


    print '###############open ftp connection & update gds file to cadence server###################'
    ftp_cadence_server = ftplib.FTP('141.223.86.109')
    ftp_cadence_server.login('sgjeong2',base64.b64decode('YWx2aDE1OTk1MQ==') )
    if DesignParameters._Technology == '065nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc65_ver3')
    elif DesignParameters._Technology == '180nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc180/workspace/workspace')
    elif DesignParameters._Technology == '130nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc130')
    elif DesignParameters._Technology == '090nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc90')
    elif DesignParameters._Technology == '045nm':
        ftp_cadence_server.cwd('/home/home18/sgjeong2/OPUS/tsmc45')
    print ftp_cadence_server.pwd()
    testStreamFile = open('./{}'.format(_fileName), 'rb')
    ftp_cadence_server.storbinary('STOR {}'.format(_fileName), testStreamFile)
    print 'close ftp connection'
    ftp_cadence_server.quit()
    testStreamFile.close()


    print '##########################################################################################'




# Consider output routing on PMOS DRC






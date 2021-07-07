import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import SlicerWithSRLatch

import math

class _SlicerWithSRLatchX4 (StickDiagram._StickDiagram) :

    _ParametersForDesignCalculation = dict(
                                    _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                  _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None,
                                  _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                  SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None, \
                                  SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None, \
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _NumberofSlicerWithSRLatch = None)

    def __init__(self, _DesignParameter = None, _Name = 'SlicerWithSRLatchX4'):
        if _DesignParameter != None :
            self._DesignParameter = _DesignParameter

        else :
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _SRFinger1 = None, _SRFinger2 = None, _SRFinger3 = None, _SRFinger4 = None, \
                                    _SRNMOSChannelWidth1 = None, _SRPMOSChannelWidth1 = None, _SRNMOSChannelWidth2 = None, _SRPMOSChannelWidth2 = None, _SRNMOSChannelWidth3 = None, _SRPMOSChannelWidth3 = None, _SRNMOSChannelWidth4 = None, _SRPMOSChannelWidth4 = None, _SRChannelLength = None, _SRNPRatio = None,\
                                    _SRVDD2VSSHeightAtOneSide = None, _SRDummy = None, _SRNumSupplyCoX = None, _SRNumSupplyCoY = None, \
                                    _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                    SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None, \
                                    SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None, \
                                    SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = None, _SRPowerLine = False,
                                    _SLCLKinputPMOSFinger1 = None, _SLCLKinputPMOSFinger2 = None, _SLPMOSFinger = None, _SLPMOSChannelWidth = None,
                                    _SLDATAinputNMOSFinger = None, _SLNMOSFinger = None, _SLCLKinputNMOSFinger = None, _SLNMOSChannelWidth = None,
                                    _SLChannelLength = None, _SLDummy = False, _SLSLVT = False, _SLGuardringWidth = None, _SLGuardring = False,
                                    _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False, _NumberofSlicerWithSRLatch = None) :




        print ('#########################################################################################################')
        print ('                                {}  SlicerWithSRLatchX4 Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatchX4'

        print ('###############################        SlicerWithSRLatch Generation       #########################################')

        _SlicerWithSRLatchinputs = copy.deepcopy(SlicerWithSRLatch._SlicerWithSRLatch._ParametersForDesignCalculation)
        _SlicerWithSRLatchinputs['_SRFinger1'] = _SRFinger1
        _SlicerWithSRLatchinputs['_SRFinger2'] = _SRFinger2
        _SlicerWithSRLatchinputs['_SRFinger3'] = _SRFinger3
        _SlicerWithSRLatchinputs['_SRFinger4'] = _SRFinger4
        _SlicerWithSRLatchinputs['_SRNMOSChannelWidth1'] = _SRNMOSChannelWidth1
        _SlicerWithSRLatchinputs['_SRPMOSChannelWidth1'] = _SRPMOSChannelWidth1
        _SlicerWithSRLatchinputs['_SRNMOSChannelWidth2'] = _SRNMOSChannelWidth2
        _SlicerWithSRLatchinputs['_SRPMOSChannelWidth2'] = _SRPMOSChannelWidth2
        _SlicerWithSRLatchinputs['_SRNMOSChannelWidth3'] = _SRNMOSChannelWidth3
        _SlicerWithSRLatchinputs['_SRPMOSChannelWidth3'] = _SRPMOSChannelWidth3
        _SlicerWithSRLatchinputs['_SRNMOSChannelWidth4'] = _SRNMOSChannelWidth4
        _SlicerWithSRLatchinputs['_SRPMOSChannelWidth4'] = _SRPMOSChannelWidth4
        _SlicerWithSRLatchinputs['_SRChannelLength'] = _SRChannelLength
        _SlicerWithSRLatchinputs['_SRNPRatio'] = _SRNPRatio
        _SlicerWithSRLatchinputs['_SRVDD2VSSHeightAtOneSide'] = _SRVDD2VSSHeightAtOneSide
        _SlicerWithSRLatchinputs['_SRDummy'] = _SRDummy
        _SlicerWithSRLatchinputs['_SRNumSupplyCoX'] = _SRNumSupplyCoX
        _SlicerWithSRLatchinputs['_SRNumSupplyCoY'] = _SRNumSupplyCoY
        _SlicerWithSRLatchinputs['_SRSupplyMet1XWidth'] = _SRSupplyMet1XWidth
        _SlicerWithSRLatchinputs['_SRSupplyMet1YWidth'] = _SRSupplyMet1YWidth
        _SlicerWithSRLatchinputs['SRNumViaPoly2Met1CoX'] = SRNumViaPoly2Met1CoX
        _SlicerWithSRLatchinputs['SRNumViaPoly2Met1CoY'] = SRNumViaPoly2Met1CoY
        _SlicerWithSRLatchinputs['SRNumViaPMOSMet12Met2CoX'] = SRNumViaPMOSMet12Met2CoX
        _SlicerWithSRLatchinputs['SRNumViaPMOSMet12Met2CoY'] = SRNumViaPMOSMet12Met2CoY
        _SlicerWithSRLatchinputs['SRNumViaNMOSMet12Met2CoX'] = SRNumViaNMOSMet12Met2CoX
        _SlicerWithSRLatchinputs['SRNumViaNMOSMet12Met2CoY'] = SRNumViaNMOSMet12Met2CoY
        _SlicerWithSRLatchinputs['SRNumViaPMOSMet22Met3CoX'] = SRNumViaPMOSMet22Met3CoX
        _SlicerWithSRLatchinputs['SRNumViaPMOSMet22Met3CoY'] = SRNumViaPMOSMet22Met3CoY
        _SlicerWithSRLatchinputs['SRNumViaNMOSMet22Met3CoX'] = SRNumViaNMOSMet22Met3CoX
        _SlicerWithSRLatchinputs['SRNumViaNMOSMet22Met3CoY'] = SRNumViaNMOSMet22Met3CoY
        _SlicerWithSRLatchinputs['_SRSLVT'] = _SRSLVT
        _SlicerWithSRLatchinputs['_SRPowerLine'] = _SRPowerLine

        _SlicerWithSRLatchinputs['_SLCLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1
        _SlicerWithSRLatchinputs['_SLCLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2
        _SlicerWithSRLatchinputs['_SLPMOSFinger'] = _SLPMOSFinger
        _SlicerWithSRLatchinputs['_SLPMOSChannelWidth'] = _SLPMOSChannelWidth
        _SlicerWithSRLatchinputs['_SLDATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        _SlicerWithSRLatchinputs['_SLNMOSFinger'] = _SLNMOSFinger
        _SlicerWithSRLatchinputs['_SLCLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        _SlicerWithSRLatchinputs['_SLNMOSChannelWidth'] = _SLNMOSChannelWidth
        _SlicerWithSRLatchinputs['_SLChannelLength'] = _SLChannelLength
        _SlicerWithSRLatchinputs['_SLDummy'] = _SLDummy
        _SlicerWithSRLatchinputs['_SLSLVT'] = _SLSLVT
        _SlicerWithSRLatchinputs['_SLGuardringWidth'] = _SLGuardringWidth
        _SlicerWithSRLatchinputs['_SLGuardring'] = _SLGuardring
        _SlicerWithSRLatchinputs['_SLSlicerGuardringWidth'] = _SLSlicerGuardringWidth
        _SlicerWithSRLatchinputs['_SLSlicerGuardring'] = _SLSlicerGuardring
        _SlicerWithSRLatchinputs['_SLNumSupplyCOX'] = _SLNumSupplyCOX
        _SlicerWithSRLatchinputs['_SLNumSupplyCOY'] = _SLNumSupplyCOY
        _SlicerWithSRLatchinputs['_SLSupplyMet1XWidth'] = _SLSupplyMet1XWidth
        _SlicerWithSRLatchinputs['_SLSupplyMet1YWidth'] = _SLSupplyMet1YWidth
        _SlicerWithSRLatchinputs['_SLVDD2VSSHeight'] = _SLVDD2VSSHeight
        _SlicerWithSRLatchinputs['_SLNumVIAPoly2Met1COX'] = _SLNumVIAPoly2Met1COX
        _SlicerWithSRLatchinputs['_SLNumVIAPoly2Met1COY'] = _SLNumVIAPoly2Met1COY
        _SlicerWithSRLatchinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COX
        _SlicerWithSRLatchinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COY
        _SlicerWithSRLatchinputs['_SLPowerLine'] = _SLPowerLine


        self._DesignParameter['_SlicerWithSRLatch'] = self._SrefElementDeclaration(_DesignObj = SlicerWithSRLatch._SlicerWithSRLatch(_DesignParameter=None, _Name = "SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchinputs)


        print ('#################################       Coordinates Settings      #########################################')
        _OriginXYCoordinateOfSlicerWithSRLatch = [[0,0]]

        _GuardRingRX2RXSpace = _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace

        PMOS_toptmp = self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
        NMOS_bottomtmp = self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
        Guardring_top = self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _SLGuardringWidth/2 + _GuardRingRX2RXSpace + _SLSlicerGuardringWidth/2
        Guardring_bottom = self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - _SLGuardringWidth/2 - _GuardRingRX2RXSpace - _SLSlicerGuardringWidth/2
        GuardringHeight = Guardring_top - Guardring_bottom

        _VDD2VSSHeightAtOneSide = self._DesignParameter['_SlicerWithSRLatch']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]

        tmp = []
        for i in range(0, _NumberofSlicerWithSRLatch) :
            tmp.append([_OriginXYCoordinateOfSlicerWithSRLatch[0][0], _OriginXYCoordinateOfSlicerWithSRLatch[0][1] - i * GuardringHeight])

        self._DesignParameter['_SlicerWithSRLatch']['_XYCoordinates'] = tmp


if __name__ == '__main__' :
    DesignParameters._Technology = '028nm'

    SlicerWithSRLatchX4Obj = _SlicerWithSRLatchX4(_DesignParameter=None, _Name='SlicerWithSRLatchX4')
    SlicerWithSRLatchX4Obj._CalculateDesignParameter(_SRFinger1 = 5, _SRFinger2 = 1, _SRFinger3 = 2, _SRFinger4 = 2,
                                  _SRNMOSChannelWidth1 = 200, _SRPMOSChannelWidth1 = 400, _SRNMOSChannelWidth2 = 200, _SRPMOSChannelWidth2 = 400,
                                  _SRNMOSChannelWidth3 = 200, _SRPMOSChannelWidth3 = 400, _SRNMOSChannelWidth4 = 200, _SRPMOSChannelWidth4 = 400,
                                  _SRChannelLength = 30, _SRNPRatio = None,
                                  _SRVDD2VSSHeightAtOneSide = None, _SRDummy = True, _SRNumSupplyCoX = None, _SRNumSupplyCoY = 2,
                                  _SRSupplyMet1XWidth = None, _SRSupplyMet1YWidth = None, SRNumViaPoly2Met1CoX = None, \
                                  SRNumViaPoly2Met1CoY = None, SRNumViaPMOSMet12Met2CoX = None, SRNumViaPMOSMet12Met2CoY = None,
                                  SRNumViaNMOSMet12Met2CoX = None, SRNumViaNMOSMet12Met2CoY = None, SRNumViaPMOSMet22Met3CoX = None, SRNumViaPMOSMet22Met3CoY = None,
                                  SRNumViaNMOSMet22Met3CoX = None, SRNumViaNMOSMet22Met3CoY = None, _SRSLVT = True, _SRPowerLine = False,
                                  _SLCLKinputPMOSFinger1 = 6, _SLCLKinputPMOSFinger2 = 3, _SLPMOSFinger = 2, _SLPMOSChannelWidth = 1000,
                                    _SLDATAinputNMOSFinger = 12, _SLNMOSFinger = 2, _SLCLKinputNMOSFinger = 8, _SLNMOSChannelWidth = 1000,
                                    _SLChannelLength = 30, _SLDummy = True, _SLSLVT = True, _SLGuardringWidth = 200, _SLGuardring = True,
                                    _SLSlicerGuardringWidth=200, _SLSlicerGuardring=None,
                                    _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight = None,
                                    _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine = False, _NumberofSlicerWithSRLatch = 4)

    # SlicerwithSRLatchObj._CalculateDesignParameter(_SRFinger1=10, _SRFinger2=10, _SRFinger3=10, _SRFinger4=10,
    #                                                _SRNMOSChannelWidth1=200, _SRPMOSChannelWidth1=400,
    #                                                _SRNMOSChannelWidth2=200, _SRPMOSChannelWidth2=400,
    #                                                _SRNMOSChannelWidth3=200, _SRPMOSChannelWidth3=400,
    #                                                _SRNMOSChannelWidth4=200, _SRPMOSChannelWidth4=400,
    #                                                _SRChannelLength=30, _SRNPRatio=None,
    #                                                _SRVDD2VSSHeightAtOneSide=None, _SRDummy=True, _SRNumSupplyCoX=None,
    #                                                _SRNumSupplyCoY=2,
    #                                                _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None,
    #                                                SRNumViaPoly2Met1CoX=None, \
    #                                                SRNumViaPoly2Met1CoY=None, SRNumViaPMOSMet12Met2CoX=None,
    #                                                SRNumViaPMOSMet12Met2CoY=None,
    #                                                SRNumViaNMOSMet12Met2CoX=None, SRNumViaNMOSMet12Met2CoY=None,
    #                                                SRNumViaPMOSMet22Met3CoX=None, SRNumViaPMOSMet22Met3CoY=None,
    #                                                SRNumViaNMOSMet22Met3CoX=None, SRNumViaNMOSMet22Met3CoY=None,
    #                                                _SRSLVT=True, _SRPowerLine=True,
    #                                                _SLCLKinputPMOSFinger1=12, _SLCLKinputPMOSFinger2=12, _SLPMOSFinger=12,
    #                                                _SLPMOSChannelWidth=1000,
    #                                                _SLDATAinputNMOSFinger=12, _SLNMOSFinger=12, _SLCLKinputNMOSFinger=12,
    #                                                _SLNMOSChannelWidth=1000,
    #                                                _SLChannelLength=30, _SLDummy=True, _SLSLVT=True,
    #                                                _SLGuardringWidth=200, _SLGuardring=True,
    #                                                _SLSlicerGuardringWidth=200, _SLSlicerGuardring=None,
    #                                                _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None,
    #                                                _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight=None,
    #                                                _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None,
    #                                                _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None, _SLPowerLine=True)

    SlicerWithSRLatchX4Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary = SlicerWithSRLatchX4Obj._DesignParameter)
    _fileName = 'SlicerWithSRLatchX4.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = SlicerWithSRLatchX4Obj._CreateGDSStream(SlicerWithSRLatchX4Obj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('SlicerWithSRLatchX4.gds', 'rb')
    ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
    myfile.close()
    ftp.close()

    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    # myfile = open('SlicerWithSRLatch.gds', 'rb')
    # ftp.storbinary('STOR SlicerWithSRLatch.gds', myfile)
    # myfile.close()
    # ftp.close()
    #
    # ftp = ftplib.FTP('141.223.29.61')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    # myfile = open('SlicerWithSRLatch.gds', 'rb')
    # ftp.storbinary('STOR SlicerWithSRLatch.gds', myfile)
    # myfile.close()
    # ftp.close()
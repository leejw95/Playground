import StickDiagram
import DesignParameters
import copy
import DRC
import NMOS
import PMOS
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import ftplib
import Transmission_Gate
import opppcres_b
import psubring

class _ResistorBank(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(
                                           _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                                           _TransmissionGateVDD2VSSHeight = None,
                                           _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None,_ResistorMetYCO=None,
                                           _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
                                           _PMOSSubringWidth=None,
                                           _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
                                           _NMOSSubringWidth=None,
                                           _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
                                           _TotalSubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name='ResistorBank'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateResistorBank(self,
                               # _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterDummy = False,
                               # _InverterVDD2VSSHeight=None, _InverterSLVT = False,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                               _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                               _TransmissionGateDummy = False , _TransmissionGateVDD2VSSHeight = None, _TransmissionGateSLVT = False,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
                               _PMOSSubringType = True, _PMOSSubringXWidth = None, _PMOSSubringYWidth = None, _PMOSSubringWidth = None,
                               _NMOSSubringType = True, _NMOSSubringXWidth = None, _NMOSSubringYWidth = None, _NMOSSubringWidth = None,
                               _TotalSubringType = True, _TotalSubringXWidth = None, _TotalSubringYWidth = None, _TotalSubringWidth = None):

        print '#########################################################################################################'
        print '                                {}  ResistorBank Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'

        _DRCObj = DRC.DRC()
        _Name = 'ResistorBank'


        # print '###############################     Inverter Generation    ##############################################'
        # _Inverterinputs = copy.deepcopy(Inverter._Inverter._ParametersForDesignCalculation)
        # _Inverterinputs['_Finger'] = _InverterFinger
        # _Inverterinputs['_ChannelWidth'] = _InverterChannelWidth
        # _Inverterinputs['_ChannelLength'] = _InverterChannelLength
        # _Inverterinputs['_NPRatio'] = _InverterNPRatio
        # _Inverterinputs['_Dummy'] = _InverterDummy
        # _Inverterinputs['_VDD2VSSHeight'] = _InverterVDD2VSSHeight
        # _Inverterinputs['_SLVT'] = _InverterSLVT
        # _Inverterinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth
        #
        # self._DesignParameter['_InverterRB'] = self._SrefElementDeclaration(_DesignObj=Inverter._Inverter(_DesignParameter=None, _Name='InverterIn{}'.format(_Name)))[0]
        # self._DesignParameter['_InverterRB']['_DesignObj']._CalculateInverter(**_Inverterinputs)

        print '##############################     TransmissionGate Generation    ########################################'
        _TransmissionGateinputs = copy.deepcopy(Transmission_Gate._TransmissionGate._ParametersForDesignCalculation)
        _TransmissionGateinputs['_Finger'] = _TransmissionGateFinger
        _TransmissionGateinputs['_ChannelWidth'] = _TransmissionGateChannelWidth
        _TransmissionGateinputs['_ChannelLength'] = _TransmissionGateChannelLength
        _TransmissionGateinputs['_NPRatio'] = _TransmissionGateNPRatio
        _TransmissionGateinputs['_Dummy'] = _TransmissionGateDummy
        _TransmissionGateinputs['_VDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
        _TransmissionGateinputs['_SLVT'] = _TransmissionGateSLVT
        _TransmissionGateinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth

        self._DesignParameter['_TransmissionGateRB'] = self._SrefElementDeclaration(_DesignObj=Transmission_Gate._TransmissionGate(_DesignParameter=None, _Name = 'TransmissionGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateinputs)


        print '###############################       Opppcres_b Generation      #########################################'
        _Opppcresinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
        _Opppcresinputs['_ResWidth'] = _ResistorWidth
        _Opppcresinputs['_ResLength'] = _ResistorLength
        _Opppcresinputs['_CONUMX'] = _ResistorMetXCO
        _Opppcresinputs['_CONUMY'] = _ResistorMetYCO

        self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_DesignParameter=None, _Name = 'OpppcresIn{}'.format(_Name)))[0]
        self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateOpppcresDesignParameter(**_Opppcresinputs)


        print '#################################       PSubring Generation      #########################################'
        _PMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _PMOSSubringinputs['_PType'] = False
        _PMOSSubringinputs['_XWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        ( self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2

        _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 2 + _DRCObj._Metal1MinSpace2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
                                            (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 2 + 1 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        _PMOSSubringinputs['_Width'] = _PMOSSubringWidth

        self._DesignParameter['_PMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name = 'PMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOSSubringRB']['_DesignObj']._CalculatePSubring(**_PMOSSubringinputs)

        _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _NMOSSubringinputs['_PType'] = True
        _NMOSSubringinputs['_XWidth'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        ( self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2

        _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 2 + _DRCObj._Metal1MinSpace2 +\
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
                                        (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 2 + 1 +\
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        _NMOSSubringinputs['_Width'] = _NMOSSubringWidth

        self._DesignParameter['_NMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='NMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOSSubringRB']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)


        _TotalSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _TotalSubringinputs['_PType'] = True
        _TotalSubringinputs['_XWidth'] = max(_PMOSSubringinputs['_XWidth'] + _PMOSSubringinputs['_Width'] * 2 + _DRCObj._PpMinExtensiononPactive * 2, _NMOSSubringinputs['_XWidth'] + _NMOSSubringinputs['_Width'] * 2 + _DRCObj._NwMinEnclosurePactive * 2) + \
                                        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + \
                                        _DRCObj._RXMinSpacetoPRES * 2 + _DRCObj._PpMinSpace
        _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width']//2 + _PMOSSubringinputs['_Width']//2 + _DRCObj._NwMinEnclosurePactive * 2 + _DRCObj._Metal1MinSpace3 + _DRCObj._PpMinSpace,
                                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + _DRCObj._RXMinSpacetoPRES * 2)

        _TotalSubringinputs['_Width'] = _TotalSubringWidth

        self._DesignParameter['_TotalSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='TotalSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_TotalSubringRB']['_DesignObj']._CalculatePSubring(**_TotalSubringinputs)


        print '#################################       Coordinates Settings      ########################################'

        ## Inverter and Transmission Gate Settings

        self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'] = [[0,0]]

        _VDD2VSSMinHeight = _NMOSSubringinputs['_Width'] * 1.5 + _NMOSSubringinputs['_YWidth'] + _DRCObj._Metal1MinSpace3 + _PMOSSubringinputs['_Width'] * 1.5 + _PMOSSubringinputs['_YWidth']

        print ('@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@# SET MINIMUM HEIGHT VALUE TO : ', _VDD2VSSMinHeight)

        if _TransmissionGateVDD2VSSHeight != _VDD2VSSMinHeight :
            raise NotImplementedError

        if _TransmissionGateVDD2VSSHeight == None :
            raise NotImplementedError


        ## MOS  SUBRING  Settings

        self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] ,
                                                                      self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight - (_PMOSSubringinputs['_YWidth'])//2 - (_PMOSSubringWidth) // 2]]

        self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + (_NMOSSubringinputs['_YWidth']) // 2 + _NMOSSubringinputs['_Width'] // 2]]



        ##Total Guardring Settings
        self._DesignParameter['_TotalSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + _TotalSubringinputs['_XWidth'] // 2
                                                                        - ((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                                                           self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) // 2 -
                                                                           (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]
                                                                            - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) +
                                                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 +
                                                                         _DRCObj._Metal1MinSpace3 + max(_PMOSSubringinputs['_Width'] + _DRCObj._NwMinEnclosurePactive ,_NMOSSubringinputs['_Width'] + _DRCObj._PpMinExtensiononPactive * 2 + _DRCObj._PpMinSpace)),
                                                                       min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2,
                                                                           self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_YWidth'] // 2 -
                                                                           (_NMOSSubringinputs['_Width']//2 + _DRCObj._PpMinExtensiononPactive * 2 + _DRCObj._PpMinSpace))]]

        ## Resistor Settings
        self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
            [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
             _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2 +_DRCObj._RXMinSpacetoPRES +
             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] // 2,
             min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]



        print '###############################       Additional Path Settings      ######################################'
        ##Additional NWell Generation
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_NWLayer']['_Width'] = _PMOSSubringinputs['_YWidth']
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
                                                                 self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] + _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]]]]


        ##Additional SLVT Generation
        # self._DesignParameter['_SLVTLayerPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_SLVTLayerNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
        #
        # _GapBtwPMOS = abs(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1] - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1])
        # _GapBtwNMOS = abs(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1] - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1])
        # if _GapBtwPMOS % 2 == 1 :
        #     _GapBtwPMOS += 1
        # if _GapBtwNMOS % 2 == 1 :
        #     _GapBtwNMOS += 1
        #
        # self._DesignParameter['_SLVTLayerPMOS']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] + _GapBtwPMOS
        # self._DesignParameter['_SLVTLayerNMOS']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] + _GapBtwNMOS
        #
        # self._DesignParameter['_SLVTLayerPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                                self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']//2,
        #                                                                max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2],
        #                                                               [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                                max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2]]]
        #
        # self._DesignParameter['_SLVTLayerNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                                 self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                             max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1],
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]) - _GapBtwNMOS // 2],
        #                                                                 [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] // 2,
        #                                                             max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_NMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]) - _GapBtwNMOS // 2]]]
        #

        ##Additional BP Generation
        # self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=100)
        # self._DesignParameter['_PPLayer']['_Width'] = self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _GapBtwPMOS
        # self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_InverterRB']['_XYCoordinates'][0][0] -
        #                                                         self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']//2,
        #                                                         max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2],
        #                                                         [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
        #                                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] // 2,
        #                                                         max(self._DesignParameter['_InverterRB']['_DesignObj']._DesignParameter['_PMOSINV']['_XYCoordinates'][0][1],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]) - _GapBtwPMOS // 2]]]


        #Additional Metal & Via Generation for Resistor
        _LengthOfAddMet1Y = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2 +
                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) * 2

        _NumViaMet12Met2COX = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
        _NumViaMet12Met2COY = _LengthOfAddMet1Y // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)

        _ViaResMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaMet12Met2COX
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaMet12Met2COY

        self._DesignParameter['_ViaMet12Met2OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaResMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'] = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                          self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +  self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]],
                                                                         [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                          self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +  self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]]]

        _ViaResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaMet12Met2COX
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaMet12Met2COY

        self._DesignParameter['_ViaMet22Met3OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnRes']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaResMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'] = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                          self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                          self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]],
                                                                         [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                          self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                          self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]]]

        _ViaResMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaMet12Met2COX
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaMet12Met2COY

        self._DesignParameter['_ViaMet32Met4OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaMet32Met4OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaResMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'] = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                            self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]]]

        _ViaResMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaMet12Met2COX
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaMet12Met2COY

        self._DesignParameter['_ViaMet42Met5OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaMet42Met5OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnRes']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaResMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnRes']['_XYCoordinates'] = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                            self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]]]


        ##Metal align for Resistor
        self._DesignParameter['_Met3LayerResAX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerResAX']['_Width'] = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_SupplyPMOSRoutingXTG']['_XYCoordinates'][0][0][1] -
                                                              self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 -
                                                              _DRCObj._MetalxMinSpace21 - self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1])


                                                      #   min(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1],
                                                      # (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1] +
                                                      # self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2 -
                                                      # (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)//4) -
                                                      # self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1])
        if self._DesignParameter['_Met3LayerResAX']['_Width'] % 2 == 1 :
            self._DesignParameter['_Met3LayerResAX']['_Width'] -= 1


        self._DesignParameter['_Met3LayerResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] +
                                                                       self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],
                                                                       self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                       self._DesignParameter['_Met3LayerResAX']['_Width'] // 2],
                                                                      [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] +
                                                                      self._DesignParameter['_ViaMet22Met3OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2,
                                                                      self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                      self._DesignParameter['_Met3LayerResAX']['_Width'] // 2]]]


        self._DesignParameter['_Met3LayerResAY'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerResAY']['_Width'] = self._DesignParameter['_ViaMet22Met3OnRes']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
        self._DesignParameter['_Met3LayerResAY']['_XYCoordinates'] = [[[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][1]],
                                                                       [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                        self._DesignParameter['_Met3LayerResAX']['_Width'] // 2]]]


        ##VDD and VSS VIA Generation.. (Make Metals first and via)
        self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met5LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met6LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met7LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met2LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met3LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met4LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met5LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met6LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met7LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)


        self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met2LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                     self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                     _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
        self._DesignParameter['_Met3LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met3LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                    _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
        self._DesignParameter['_Met4LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met4LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                    _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
        self._DesignParameter['_Met5LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met5LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                    _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
        self._DesignParameter['_Met6LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met6LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]

        self._DesignParameter['_Met7LayerVDD']['_XWidth'] = (_PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']) // 2 - _DRCObj._MetalxMinSpace5 // 2
        self._DesignParameter['_Met7LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
        if self._DesignParameter['_Met7LayerVDD']['_XWidth'] % 2 == 1 :
            self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - self._DesignParameter['_Met7LayerVDD']['_XWidth'] // 2 - _DRCObj._MetalxMinSpace5 // 2 - 1,
                                                                            self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                            _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
        else :
            self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
                                                                         self._DesignParameter['_Met7LayerVDD']['_XWidth'] // 2 - _DRCObj._MetalxMinSpace5 // 2,
                                                                         self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                         _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]


        self._DesignParameter['_Met2LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met2LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                     self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                     self._DesignParameter['_Met2LayerVSS']['_YWidth']//2 + _NMOSSubringinputs['_Width']//2]]

        self._DesignParameter['_Met3LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met3LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]

        self._DesignParameter['_Met4LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met4LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]

        self._DesignParameter['_Met5LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met5LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]

        self._DesignParameter['_Met6LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met6LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]

        self._DesignParameter['_Met7LayerVSS']['_XWidth'] = (_NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']) // 2 - _DRCObj._MetalxMinSpace5 // 2
        self._DesignParameter['_Met7LayerVSS']['_YWidth'] = _NMOSSubringinputs['_Width'] * 2 + 2 * _DRCObj._PpMinExtensiononPactive + _DRCObj._PpMinSpace
        if self._DesignParameter['_Met7LayerVSS']['_XWidth'] % 2 == 1:
            self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                         self._DesignParameter['_Met7LayerVSS']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace5 // 2 + 1,
                                                                         self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                                                                         self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]
        else:
            self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                 self._DesignParameter['_Met7LayerVSS']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace5 // 2,
                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] -
                 self._DesignParameter['_Met2LayerVSS']['_YWidth'] // 2 + _NMOSSubringinputs['_Width'] // 2]]

        #Via Generations
        _NumViaVDDCOX = int(self._DesignParameter['_Met2LayerVDD']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumViaVDDCOY = int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumViaVSSCOX = int(self._DesignParameter['_Met2LayerVSS']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumViaVSSCOY = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumVia67VDDCOX = int(self._DesignParameter['_Met7LayerVDD']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumVia67VDDCOY = int(self._DesignParameter['_Met7LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumVia67VSSCOX = int(self._DesignParameter['_Met7LayerVSS']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _NumVia67VSSCOY = int(self._DesignParameter['_Met7LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVDDCOX
        _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaVDDCOY
        _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVSSCOX
        _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaVSSCOY
        _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVDDCOX
        _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaVDDCOY
        _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVSSCOX
        _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaVSSCOY
        _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVDDCOX
        _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVDDCOY
        _ViaVSSMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVSSCOX
        _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVSSCOY
        _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVDDCOX
        _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVDDCOY
        _ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVSSCOX
        _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVSSCOY
        _ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVDDCOX
        _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVDDCOY
        _ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVSSCOX
        _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVSSCOY
        _ViaVDDMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = _NumVia67VDDCOX
        _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = _NumVia67VDDCOY
        _ViaVSSMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = _NumVia67VSSCOX
        _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = _NumVia67VSSCOY
        

        self._DesignParameter['_ViaMet12Met2OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnVDD']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVDD']['_XYCoordinates']

        self._DesignParameter['_ViaMet22Met3OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnVDD']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVDD']['_XYCoordinates']
        
        self._DesignParameter['_ViaMet32Met4OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVDDMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVDD']['_XYCoordinates']

        self._DesignParameter['_ViaMet42Met5OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVDDMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVDD']['_XYCoordinates']

        self._DesignParameter['_ViaMet52Met6OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVDDMet52Met6)
        self._DesignParameter['_ViaMet52Met6OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVDD']['_XYCoordinates']

        self._DesignParameter['_ViaMet62Met7OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaVDDMet62Met7)
        self._DesignParameter['_ViaMet62Met7OnVDD']['_XYCoordinates'] = self._DesignParameter['_Met7LayerVDD']['_XYCoordinates']

        self._DesignParameter['_ViaMet12Met2OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnVSS']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVSSMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVSS']['_XYCoordinates']

        self._DesignParameter['_ViaMet22Met3OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVSSMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVSS']['_XYCoordinates']

        self._DesignParameter['_ViaMet32Met4OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_ViaVSSMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVSS']['_XYCoordinates']

        self._DesignParameter['_ViaMet42Met5OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameter(**_ViaVSSMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVSS']['_XYCoordinates']

        self._DesignParameter['_ViaMet52Met6OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**_ViaVSSMet52Met6)
        self._DesignParameter['_ViaMet52Met6OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met2LayerVSS']['_XYCoordinates']

        self._DesignParameter['_ViaMet62Met7OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name='ViaMet62Met7OnVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet62Met7OnVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameter(**_ViaVSSMet62Met7)
        self._DesignParameter['_ViaMet62Met7OnVSS']['_XYCoordinates'] = self._DesignParameter['_Met7LayerVSS']['_XYCoordinates']


if __name__ == '__main__' :


    # _InverterFinger = 2
    # _InverterChannelWidth = 200
    # _InverterChannelLength = 30
    # _InverterNPRatio = 2
    # _InverterDummy = True    #T/F?
    # _InverterVDD2VSSHeight = 2252 ## SHOULD BE FIXED OVER MIN VALUE
    # _InverterSLVT = True     #T/F?

    _TransmissionGateFinger = 6
    _TransmissionGateChannelWidth = 200
    _TransmissionGateChannelLength = 30
    _TransmissionGateNPRatio = 2
    _TransmissionGateDummy = True     #T/F?
    _TransmissionGateVDD2VSSHeight = 2256 ## FIXED
    _TransmissionGateSLVT = True     #T/F?

    _ResistorWidth = 1250
    _ResistorLength = 1234
    _ResistorMetXCO = None
    _ResistorMetYCO = None

    _PMOSSubringType = False ## FIXED
    _PMOSSubringXWidth = None ## FIXED
    _PMOSSubringYWidth = None ## FIXED
    _PMOSSubringWidth = 170

    _NMOSSubringType = True ## FIXED
    _NMOSSubringXWidth = None ## FIXED
    _NMOSSubringYWidth = None ## FIXED
    _NMOSSubringWidth = _PMOSSubringWidth

    _TotalSubringType = True ## FIXED
    _TotalSubringXWidth = None ## FIXED
    _TotalSubringYWidth = None ## FIXED
    _TotalSubringWidth = 170

    DesignParameters._Technology = '028nm'

    ResistorBankObj = _ResistorBank(_DesignParameter=None, _Name='ResistorBank')
    #print ("A!!")
    ResistorBankObj._CalculateResistorBank(
                               #  _InverterFinger=_InverterFinger, _InverterChannelWidth=_InverterChannelWidth, _InverterChannelLength=_InverterChannelLength, _InverterNPRatio=_InverterNPRatio, _InverterDummy = _InverterDummy,
                               # _InverterVDD2VSSHeight=_InverterVDD2VSSHeight, _InverterSLVT = _InverterSLVT,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                               _TransmissionGateFinger =_TransmissionGateFinger, _TransmissionGateChannelWidth = _TransmissionGateChannelWidth, _TransmissionGateChannelLength = _TransmissionGateChannelLength, _TransmissionGateNPRatio =_TransmissionGateNPRatio,
                               _TransmissionGateDummy = _TransmissionGateDummy , _TransmissionGateVDD2VSSHeight = _TransmissionGateVDD2VSSHeight, _TransmissionGateSLVT = _TransmissionGateSLVT,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO = _ResistorMetXCO, _ResistorMetYCO = _ResistorMetYCO,
                                _PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth,_PMOSSubringWidth=_PMOSSubringWidth,
                                _NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth,_NMOSSubringWidth=_NMOSSubringWidth,
                                _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth)


    ResistorBankObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ResistorBankObj._DesignParameter)
    _fileName = 'ResistorBank.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = ResistorBankObj._CreateGDSStream(ResistorBankObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print '###############      Sending to FTP Server...      ##################'


    ftp = ftplib.FTP('141.223.29.61')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
    myfile = open('ResistorBank.gds', 'rb')
    ftp.storbinary('STOR ResistorBank.gds', myfile)
    myfile.close()
    ftp.close()


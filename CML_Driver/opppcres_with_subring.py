import copy

#
import StickDiagram
import DesignParameters
import DRC
import DRCchecker
from Private import MyInfo
from SthPack import PrintStr, CoordCalc
from SthPack import PlaygroundBot

#
import opppcres_b_iksu
import psubring
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4


class OpppcresWithSubring(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_ResWidth=None, _ResLength=None, _NumCOY=None, _NumStripes=None, _RoutingWidth=None, _Dummy=False, _SubringWidth=None)


    def __init__(self, _DesignParameter=None, _Name='Resistor_OPPPC_wSubRing'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _VSSRoutingH1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                _VSSRoutingH2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1]),
                _Met2A=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1]),
                _Met2B=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                        _Datatype=DesignParameters._LayerMapping['METAL2'][1]),
                _Met3A=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                        _Datatype=DesignParameters._LayerMapping['METAL3'][1]),
                _Met4A=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                        _Datatype=DesignParameters._LayerMapping['METAL4'][1]),
                # _Met5A=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],
                #                                         _Datatype=DesignParameters._LayerMapping['METAL5'][1]),
                # _Met6A=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],
                #                                         _Datatype=DesignParameters._LayerMapping['METAL6'][1]),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _Met1BoundaryOfSubring=dict(_DesignParametertype=7, _XWidth=None, _YWidth=None, _XYCoordinates=[]),
            )

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateDesignParameter(self, _ResWidth: int, _ResLength: int, _NumCOY: int,
                                  _NumRows: int, _NumStripes: int,
                                  _RoutingWidth: int = None, _Dummy: bool = False, _SubringWidth: int = None):
        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _XYCoordinateOfOPRES = [[0, 0]]
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        Printer = PrintStr.PrintStr()
        Printer.ThreeLine('{} Calculation Start'.format(_Name))

        assert _NumStripes > 1      # temporal condition

        print('##############################     Resistor_OPPPCRES Generation    ########################################')
        _OPPPCRES_inputs = copy.deepcopy(opppcres_b_iksu.Resistor_OPPPC._ParametersForDesignCalculation)
        _OPPPCRES_inputs['_ResWidth'] = _ResWidth
        _OPPPCRES_inputs['_ResLength'] = _ResLength
        _OPPPCRES_inputs['_NumCOY'] = _NumCOY
        _OPPPCRES_inputs['_NumStripes'] = _NumStripes
        _OPPPCRES_inputs['_RoutingWidth'] = _RoutingWidth
        _OPPPCRES_inputs['_Series'] = False
        _OPPPCRES_inputs['_Parallel'] = True
        _OPPPCRES_inputs['_Dummy'] = _Dummy
        self._DesignParameter['OPPPCRES'] = self._SrefElementDeclaration(
            _DesignObj=opppcres_b_iksu.Resistor_OPPPC(_DesignParameter=None, _Name='Opppcres_In{}'.format(_Name)))[0]
        self._DesignParameter['OPPPCRES']['_DesignObj']._CalculateDesignParameter(**_OPPPCRES_inputs)

        distanceBtwM1Port = abs(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][0][1]
                                - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XYCoordinates'][1][1])


        print('##############################     SubRing Generation    ########################################')
        XWidthOfSubring1 = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoPRES, MinSnapSpacing*2)
        XWidthOfSubring2 = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_OPLayer']['_XWidth'] + 2*_DRCObj._RXMinSpacetoOP, MinSnapSpacing*2)
        XWidthOfSubring = max(XWidthOfSubring1, XWidthOfSubring2)
        YWidthOfSubring = self.CeilMinSnapSpacing(self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] * _NumRows
                                                  - (self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] - distanceBtwM1Port) * (_NumRows-1)
                                                  + 2*_DRCObj._RXMinSpacetoPRES, MinSnapSpacing*2)

        PSubringInputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        PSubringInputs['_PType'] = True
        PSubringInputs['_XWidth'] = XWidthOfSubring
        PSubringInputs['_YWidth'] = YWidthOfSubring
        PSubringInputs['_Width'] = _SubringWidth
        self._DesignParameter['_Subring'] = self._SrefElementDeclaration(
            _DesignObj=psubring._PSubring(_DesignParameter=None, _Name='Subring_In{}'.format(_Name)))[0]
        self._DesignParameter['_Subring']['_DesignObj']._CalculatePSubring(**PSubringInputs)


        ''' Coordinates Settings '''
        tmpXYs = []
        for i in range(0, _NumRows):
            tmpXYs.append([+(XWidthOfSubring + _SubringWidth) / 2.0, distanceBtwM1Port * (i - (_NumRows - 1) / 2.0)])
            tmpXYs.append([-(XWidthOfSubring + _SubringWidth) / 2.0, distanceBtwM1Port * (i - (_NumRows - 1) / 2.0)])

        self._DesignParameter['OPPPCRES']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['_Subring']['_XYCoordinates'] = [[-(XWidthOfSubring + _SubringWidth)/2, 0],
                                                               [+(XWidthOfSubring + _SubringWidth)/2, 0]]

        # For internal calculation
        M1APortXYs = []
        M1BPortXYs = []  # VSS
        for i in range(0, _NumRows+1):
            if (i % 2) == 1:
                M1APortXYs.append([+(XWidthOfSubring + _SubringWidth) / 2, distanceBtwM1Port * (_NumRows / 2.0 - i)])
                M1APortXYs.append([-(XWidthOfSubring + _SubringWidth) / 2, distanceBtwM1Port * (_NumRows / 2.0 - i)])
            else:
                M1BPortXYs.append([+(XWidthOfSubring + _SubringWidth) / 2, distanceBtwM1Port * (_NumRows / 2.0 - i)])
                M1BPortXYs.append([-(XWidthOfSubring + _SubringWidth) / 2, distanceBtwM1Port * (_NumRows / 2.0 - i)])


        ''' Connect VSS - horizontal '''
        tmpXYs = []
        for i in range(0, (_NumRows // 2 + 1)):
            tmpXYs.append([0, distanceBtwM1Port * (_NumRows/2.0 - i*2)])
        self._DesignParameter['_VSSRoutingH1']['_XWidth'] = _SubringWidth + XWidthOfSubring * 2
        self._DesignParameter['_VSSRoutingH1']['_YWidth'] = self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_YWidth']
        self._DesignParameter['_VSSRoutingH1']['_XYCoordinates'] = tmpXYs

        YofVSSRoutingH2 = self.CeilMinSnapSpacing(((YWidthOfSubring + _SubringWidth) / 2 + abs(M1BPortXYs[0][1])) / 2, MinSnapSpacing)
        self._DesignParameter['_VSSRoutingH2']['_XWidth'] = _SubringWidth + XWidthOfSubring * 2
        self._DesignParameter['_VSSRoutingH2']['_YWidth'] = (YWidthOfSubring + _SubringWidth - distanceBtwM1Port * _NumRows)/2
        self._DesignParameter['_VSSRoutingH2']['_XYCoordinates'] = [[0, YofVSSRoutingH2]]   # Need MinSnapSpacing and lower one when even odd
        if (_NumRows % 2) == 0:
            self._DesignParameter['_VSSRoutingH2']['_XYCoordinates'].append([0, -YofVSSRoutingH2])


        ''' Connect M1-V1-M2 for VSS and Input '''
        NumViaX, NumViaY = ViaMet12Met2._ViaMet12Met2.CalcNumViaMinEnclosureY(_ResWidth/2, self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_YWidth'])
        assert NumViaX * NumViaY >= 4, f'More Via1s are needed for this _ResWidth(={_ResWidth}),\n' \
                                       f'Increase _NumCOY(={_NumCOY}).\n' \
                                       f'Calculated NumViaX, NumViaY = {NumViaX}, {NumViaY}.\n'
        # print(NumViaX, NumViaY)

        tmpXYs_A, tmpXYs_B = [], []
        dummy = 1 if _Dummy else 0
        # for i in range(0, _NumRows+1):
        #     for j in range(0, _NumStripes + dummy * 2):
        #         if ((i % 2) == 1) and ((j+dummy) % 2 == 0):
        #             tmpXYs_A.append([+(XWidthOfSubring + _SubringWidth) / 2 + self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
        #                              distanceBtwM1Port * (_NumRows / 2.0 - i)])
        #             tmpXYs_A.append([-(XWidthOfSubring + _SubringWidth) / 2 - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
        #                              distanceBtwM1Port * (_NumRows / 2.0 - i)])
        #         elif ((i % 2) == 0) and ((j+dummy) % 2 == 1):
        #             tmpXYs_B.append([+(XWidthOfSubring + _SubringWidth) / 2 + self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
        #                              distanceBtwM1Port * (_NumRows / 2.0 - i)])
        #             tmpXYs_B.append([-(XWidthOfSubring + _SubringWidth) / 2 - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
        #                              distanceBtwM1Port * (_NumRows / 2.0 - i)])
        #         else:
        #             pass

        for i in range(0, _NumRows+1):
            for j in range(dummy, _NumStripes + dummy):
                if ((i % 2) == 1) and ((j+dummy) % 2 == 0):
                    tmpXYs_A.append([+(XWidthOfSubring + _SubringWidth) / 2 + self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
                                     distanceBtwM1Port * (_NumRows / 2.0 - i)])
                    tmpXYs_A.append([-(XWidthOfSubring + _SubringWidth) / 2 - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
                                     distanceBtwM1Port * (_NumRows / 2.0 - i)])
                elif ((i % 2) == 0) and ((j+dummy) % 2 == 1):
                    tmpXYs_B.append([+(XWidthOfSubring + _SubringWidth) / 2 + self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
                                     distanceBtwM1Port * (_NumRows / 2.0 - i)])
                    tmpXYs_B.append([-(XWidthOfSubring + _SubringWidth) / 2 - self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][j][0],
                                     distanceBtwM1Port * (_NumRows / 2.0 - i)])
                else:
                    pass

        Via1Inputs = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        Via1Inputs.update({'_ViaMet12Met2NumberOfCOX':NumViaX, '_ViaMet12Met2NumberOfCOY':NumViaY})
        self._DesignParameter['_ViaMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**Via1Inputs)
        self._DesignParameter['_ViaMet12Met2']['_XYCoordinates'] = tmpXYs_A + tmpXYs_B


        ''' Connect Vertical M2 for VSS and Input '''
        tmpList = self.XYCoordinate2MinMaxXY(tmpXYs_A)
        tmpXYs = []
        for i in range(0, len(tmpList[0])):
            tmpXYs.append([tmpList[0][i], (max(tmpList[1]) + min(tmpList[1])) / 2])
        self._DesignParameter['_Met2A']['_XWidth'] = self._DesignParameter['_ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['_Met2A']['_YWidth'] = self.CeilMinSnapSpacing(max(tmpList[1]) - min(tmpList[1]), 2 * MinSnapSpacing) \
                                                     + self._DesignParameter['_ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        self._DesignParameter['_Met2A']['_XYCoordinates'] = tmpXYs

        tmpList = self.XYCoordinate2MinMaxXY(tmpXYs_B)
        tmpXYs = []
        for i in range(0, len(tmpList[0])):
            tmpXYs.append([tmpList[0][i], (max(tmpList[1]) + min(tmpList[1])) / 2])
        # print(f'Debugging...\n'
        #       f'tmpXYs_B : {tmpXYs_B}\n'
        #       f'tmpList : {tmpList}')
        self._DesignParameter['_Met2B']['_XWidth'] = self._DesignParameter['_ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['_Met2B']['_YWidth'] = self.CeilMinSnapSpacing(max(tmpList[1]) - min(tmpList[1]), 2 * MinSnapSpacing) \
                                                     + self._DesignParameter['_ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
        self._DesignParameter['_Met2B']['_XYCoordinates'] = tmpXYs


        ''' M2V2M3 for Input '''
        Via2Inputs = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        Via2Inputs.update({'_ViaMet22Met3NumberOfCOX': NumViaX, '_ViaMet22Met3NumberOfCOY': NumViaY})
        self._DesignParameter['_ViaMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**Via2Inputs)
        self._DesignParameter['_ViaMet22Met3']['_XYCoordinates'] = tmpXYs_A

        ''' M3 horizontal for Input '''
        self._DesignParameter['_Met3A']['_XWidth'] = self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_XWidth']
        self._DesignParameter['_Met3A']['_YWidth'] = self._DesignParameter['OPPPCRES']['_DesignObj']._DesignParameter['_Met1Port']['_YWidth']
        self._DesignParameter['_Met3A']['_XYCoordinates'] = M1APortXYs

        ''' V3 '''
        Via3Inputs = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        Via3Inputs.update({'_ViaMet32Met4NumberOfCOX': NumViaX, '_ViaMet32Met4NumberOfCOY': NumViaY})
        self._DesignParameter['_ViaMet32Met4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**Via3Inputs)
        self._DesignParameter['_ViaMet32Met4']['_XYCoordinates'] = tmpXYs_A

        ''' M4A '''
        self._DesignParameter['_Met4A']['_XWidth'] = self._DesignParameter['_Met2A']['_XWidth']
        self._DesignParameter['_Met4A']['_YWidth'] = self._DesignParameter['_Met2A']['_YWidth']
        self._DesignParameter['_Met4A']['_XYCoordinates'] = self._DesignParameter['_Met2A']['_XYCoordinates']

        # ''' V4 '''
        # Via4Inputs = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        # Via4Inputs.update({'_ViaMet42Met5NumberOfCOX': NumViaX, '_ViaMet42Met5NumberOfCOY': NumViaY})
        # self._DesignParameter['_ViaMet42Met5'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='M4V4M5_In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet42Met5']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**Via4Inputs)
        # self._DesignParameter['_ViaMet42Met5']['_XYCoordinates'] = tmpXYs_A

        # ''' M5A horizontal for Input '''
        # self._DesignParameter['_Met5A']['_XWidth'] = self._DesignParameter['_Met3A']['_XWidth']
        # self._DesignParameter['_Met5A']['_YWidth'] = self._DesignParameter['_Met3A']['_YWidth']
        # self._DesignParameter['_Met5A']['_XYCoordinates'] = self._DesignParameter['_Met3A']['_XYCoordinates']
        #
        # ''' V5 '''
        # Via5Inputs = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        # Via5Inputs.update({'_ViaMet52Met6NumberOfCOX': NumViaX, '_ViaMet52Met6NumberOfCOY': NumViaY})
        # self._DesignParameter['_ViaMet52Met6'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='M5V5M6_In{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet52Met6']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**Via5Inputs)
        # self._DesignParameter['_ViaMet52Met6']['_XYCoordinates'] = tmpXYs_A
        #
        # ''' M6A horizontal for Input '''
        # self._DesignParameter['_Met6A']['_XWidth'] = self._DesignParameter['_Met3A']['_XWidth']
        # self._DesignParameter['_Met6A']['_YWidth'] = self._DesignParameter['_Met3A']['_YWidth']
        # self._DesignParameter['_Met6A']['_XYCoordinates'] = self._DesignParameter['_Met3A']['_XYCoordinates']

        '''    
        Next Work...
        Outline coordinates or XYWidth
        1) Outline of M1(RX)
        2) Outline of BP
        '''

        ''' Metal1 Boundary(Outline) of Subring  '''
        upperYCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][1] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'])[1][-1] \
                         + self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'] / 2.0
        lowerYCoord_M1 = self._DesignParameter['_Subring']['_XYCoordinates'][0][1] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'])[1][0] \
                         - self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'] / 2.0

        RightXCoord_M1 = CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_XYCoordinates'])[0][-1] \
                         + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'])[0][-1] \
                         + self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] / 2.0
        LeftXCoord_M1 = CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_XYCoordinates'])[0][0] \
                        + CoordCalc.getSortedList_ascending(self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'])[0][0] \
                        - self._DesignParameter['_Subring']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] / 2.0

        self._DesignParameter['_Met1BoundaryOfSubring']['_XWidth'] = RightXCoord_M1 - LeftXCoord_M1
        self._DesignParameter['_Met1BoundaryOfSubring']['_YWidth'] = upperYCoord_M1 - lowerYCoord_M1
        self._DesignParameter['_Met1BoundaryOfSubring']['_XYCoordinates'] = [[(RightXCoord_M1 + LeftXCoord_M1) / 2.0,
                                                                              (upperYCoord_M1 + lowerYCoord_M1) / 2.0]]

        Printer.ThreeLine(f'{_Name} Calculation End')


if __name__ == '__main__':

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_OPPPCRES'
    cellname = 'OpppcresWithSubring'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ResWidth=1000,     # 3000
        _ResLength=2500,    # 2300
        _NumCOY=1,          # 4
        _NumRows=2,
        _NumStripes=3,
        _RoutingWidth=None,
        _Dummy=True,
        _SubringWidth=1000,
    )

    Mode_DRCCheck = True            # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''
            InputParams['_ResWidth'] = DRCchecker.RandomParam(start=1000, stop=5000, step=100)
            InputParams['_ResLength'] = DRCchecker.RandomParam(start=400, stop=5000, step=100)
            InputParams['_NumCOY'] = DRCchecker.RandomParam(start=2, stop=5, step=1)
            InputParams['_NumRows'] = DRCchecker.RandomParam(start=1, stop=4, step=1)
            InputParams['_NumStripes'] = DRCchecker.RandomParam(start=2, stop=10, step=1)
        else:
            pass
        print(
            "=============================   Last Layout Object's Input Parameters are   =============================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print(
            "=========================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = OpppcresWithSubring(_DesignParameter=None, _Name=cellname)
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
            Bot.send2Bot(f'Start DRCChecker...\nTotal Number Of Run : {Num_DRCCheck}')
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

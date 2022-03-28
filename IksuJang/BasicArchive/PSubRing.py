import StickDiagram
import DesignParameters
import copy
import DRC
from IksuJang.BasicArchive import PbodyContact


class PSubRing(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='p_sub_ring'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,height=5000,width=3000,contact=2):
        """

        :param height: center-to-center vertical
        :param width: center-to-center horizontal
        :param contact: the number of contacts
        :return:
        """

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['bot'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='botIn{}'.format(_Name)))[0]
        self._DesignParameter['bot']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=((int(((width - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2))) - contact) + 0), _NumberOfPbodyCOY=contact, _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['bot']['_XYCoordinates'] = [[0, ((- height) / 2)]]
        self._DesignParameter['top'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='topIn{}'.format(_Name)))[0]
        self._DesignParameter['top']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=((int(((width - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2))) - contact) + 0), _NumberOfPbodyCOY=contact, _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['top']['_XYCoordinates'] = [[0, (height / 2)]]
        self._DesignParameter['left'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='leftIn{}'.format(_Name)))[0]
        self._DesignParameter['left']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=contact, _NumberOfPbodyCOY=((0 + int(((height - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2)))) - contact), _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['left']['_XYCoordinates'] = [[((- width) / 2), 0]]
        self._DesignParameter['right'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='rightIn{}'.format(_Name)))[0]
        self._DesignParameter['right']['_DesignObj']._CalculateDesignParameter(**dict(_NumberOfPbodyCOX=contact, _NumberOfPbodyCOY=((0 + int(((height - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2)))) - contact), _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['right']['_XYCoordinates'] = [[(width / 2), 0]]
        self._DesignParameter['od'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _Width=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']))
        self._DesignParameter['od']['_XYCoordinates'] = [[[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), ((self._DesignParameter['bot']['_XYCoordinates'][0][1] + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]]
        self._DesignParameter['nw_bot'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=((width + self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
        self._DesignParameter['nw_bot']['_XYCoordinates'] = [[(0 + self._DesignParameter['bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])]]
        self._DesignParameter['nw_right'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 0), _YWidth=((0 + height) + self._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
        self._DesignParameter['nw_right']['_XYCoordinates'] = [[(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['right']['_XYCoordinates'][0][1])]]
        self._DesignParameter['nw_top'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=((width + self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
        self._DesignParameter['nw_top']['_XYCoordinates'] = [[(0 + self._DesignParameter['top']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])]]
        self._DesignParameter['nw_left'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 0), _YWidth=((0 + height) + self._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
        self._DesignParameter['nw_left']['_XYCoordinates'] = [[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['left']['_XYCoordinates'][0][1])]]
        self._DesignParameter['met_right'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']), _YWidth=((0 + height) + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
        self._DesignParameter['met_right']['_XYCoordinates'] = [[(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['right']['_XYCoordinates'][0][1])]]
        self._DesignParameter['met_left'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']), _YWidth=((0 + height) + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
        self._DesignParameter['met_left']['_XYCoordinates'] = [[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['left']['_XYCoordinates'][0][1])]]
        self._DesignParameter['met_top'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((width + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']))
        self._DesignParameter['met_top']['_XYCoordinates'] = [[(0 + self._DesignParameter['top']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])]]
        self._DesignParameter['met_bot'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((width + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
        self._DesignParameter['met_bot']['_XYCoordinates'] = [[(0 + self._DesignParameter['bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])]]


if __name__ == '__main__':
    from Private import MyInfo
    import DRCchecker
    from SthPack import PlaygroundBot

    My = MyInfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)

    libname = 'TEST_BasicArchive'
    cellname = 'PSubRing'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        height=5000,width=3000,contact=2
    )

    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 10

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Random Parameters for Layout Object '''

        else:
            pass
        print("=============================   Last Layout Object's Input Parameters are   =============================")
        tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
        print(tmpStr)
        print("=========================================================================================================")


        ''' Generate Layout Object '''
        LayoutObj = PSubRing(_Name=cellname)
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
            # Bot.send2Bot(f'Start DRCChecker...\nTotal Number Of Run : {Num_DRCCheck}')
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

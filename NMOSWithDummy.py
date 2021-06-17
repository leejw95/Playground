import StickDiagram
import DesignParameters
import DRC

class _NMOS(StickDiagram._StickDiagram):

    _ParametersForDesignCalculation= dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None, _NMOSDummy=False, _SLVT=False)
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400), #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _SLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _LVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVT'][0],
                                                           _Datatype=DesignParameters._LayerMapping['LVT'][1],
                                                           _XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _HVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['HVT'][0],
                                                           _Datatype=DesignParameters._LayerMapping['HVT'][1],
                                                           _XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PDKLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PDK'][0],_Datatype=DesignParameters._LayerMapping['PDK'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _WELLBodyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['WELLBODY'][0],_Datatype=DesignParameters._LayerMapping['WELLBODY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PCCRITLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0], _Datatype=DesignParameters._LayerMapping['PCCRIT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _CalculateNMOSDesignParameter(self, _NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None, _NMOSDummy=False, _SLVT=False, _LVT = False, _HVT = False):
        print '#########################################################################################################'
        print '                                    {}  NMOSContact Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'
        _DRCObj=DRC.DRC()

        _XYCoordinateOfNMOS = [[0,0]]

        print '#############################     POLY Layer Calculation    ##############################################'

        self._DesignParameter['_POLayer']['_XWidth']= _NMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth']= _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD  + 25*2
        _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        tmp=[]
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) \
                                 *  _LengthNMOSBtwPO + i *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]]
            elif (_NMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 \
                                 *  _LengthNMOSBtwPO + i *  _LengthNMOSBtwPO, _XYCoordinateOfNMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_POLayer']['_XYCoordinates']=tmp

        print '#############################     DIFF Layer Calculation    ##############################################'
        _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        self._DesignParameter['_ODLayer']['_XWidth']=_LengthNMOSBtwPO*_NMOSNumberofGate +_DRCObj._CoMinWidth+ 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_YWidth']=_NMOSChannelWidth

        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfNMOS

        if _NMOSDummy == True:
            print '#############################     POLY Dummy Layer Calculation    ##############################################'

            self._DesignParameter['_PODummyLayer']['_XWidth']= 30

            if  _NMOSChannelWidth < 258:
                self._DesignParameter['_PODummyLayer']['_YWidth']= _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD + 58
            else:
                self._DesignParameter['_PODummyLayer']['_YWidth']= _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD

            # POLY Dummy Layer Coordinate Setting
            _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
            if (_NMOSNumberofGate % 2) == 0: # When the number of finger is even
                _xycoordinatetmp_dummy = [
                                   [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2) ,  _XYCoordinateOfNMOS[0][1] - float(self._DesignParameter['_POLayer']['_YWidth'])/2 + float(self._DesignParameter['_PODummyLayer']['_YWidth'])/2-15],
                                   [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + (_NMOSNumberofGate -1) *  _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2,  _XYCoordinateOfNMOS[0][1] - float(self._DesignParameter['_POLayer']['_YWidth'])/2 + float(self._DesignParameter['_PODummyLayer']['_YWidth'])/2-15]
                                   ]
            elif (_NMOSNumberofGate % 2) == 1: # When the number of finger is odd
                _xycoordinatetmp_dummy = [
                                   [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfNMOS[0][1] - float(self._DesignParameter['_POLayer']['_YWidth'])/2 + float(self._DesignParameter['_PODummyLayer']['_YWidth'])/2-15],
                                   [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 *  _LengthNMOSBtwPO + (_NMOSNumberofGate -1) *  _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfNMOS[0][1] - float(self._DesignParameter['_POLayer']['_YWidth'])/2 + float(self._DesignParameter['_PODummyLayer']['_YWidth'])/2-15]
                                   ]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp_dummy
        else:
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = []

        if _NMOSChannelWidth < 258:
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = [[_xycoordinatetmp_dummy[0][0], _xycoordinatetmp_dummy[0][1]-70], [_xycoordinatetmp_dummy[1][0], _xycoordinatetmp_dummy[1][1]-70]]


        print '#############################     METAL1 Layer Calcuation    ##############################################'
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]


        for i in range(0, _NMOSNumberofGate + 1):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 *
                                    _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,   _XYCoordinateOfNMOS[0][1]]
            elif (_NMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) \
                                * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]

            tmp.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer']['_XYCoordinates']=tmp


        print '#############################     CONT Layer Calculation    ##############################################'
        _XNumberOfCOInNMOS=_NMOSNumberofGate+1
        _YNumberOfCOInNMOS=int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide , _DRCObj._Metal1MinEnclosureCO2 ] ) + _DRCObj._CoMinSpace) / ( _DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        _LengthNMOSBtwCO=_DRCObj._CoMinSpace + self._DesignParameter['_COLayer']['_YWidth']
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]
###############################################Check the number of CO On NMOS TR##############################################################################################
        if _XNumberOfCOInNMOS ==0 or _YNumberOfCOInNMOS==0:
            print '************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])
            if DesignParameters._DebugMode == 0:
                return 0
###############################################################################################################################################################################
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):

                if (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1 ) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS% 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1 ) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2)  == 0 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2)  == 0 and (_YNumberOfCOInNMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        print '#############################     NIMP Layer Calculation    ####################'
        self._DesignParameter['_NPLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
        self._DesignParameter['_NPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive if _NMOSDummy == False else \
        self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._NpMinEnclosureOfPo
        self._DesignParameter['_NPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._NpMinEnclosureOfPo

        if _SLVT == True:
            print '#############################     SLVT Layer Calculation    ##############################################'
            # SLVT Dummy Layer XWidth and YWidth Setting
            self._DesignParameter['_SLVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer'][
                                                                 '_XWidth'] + _DRCObj._SlvtMinExtensionOnOD + \
                                                             self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_SLVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_SLVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        if _LVT == True :
            print ('############      LVT Layer Generation      ############')
            self._DesignParameter['_LVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._SlvtMinExtensionOnOD + self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_LVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_LVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']
        if _HVT == True :
            print ('############      HVT Layer Generation      ############')
            self._DesignParameter['_HVTLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._SlvtMinExtensionOnOD + self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_HVTLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth']

            self._DesignParameter['_HVTLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        if DesignParameters._Technology=='028nm':
            self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
            self._DesignParameter['_PCCRITLayer']['_XWidth'] = self._DesignParameter['_ODLayer'][
                                                                   '_XWidth'] - 2 * _DRCObj._PolygateWithPCCRIT
            self._DesignParameter['_PCCRITLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        if DesignParameters._Technology=='180nm':
            print '#############################     WELLBODY Layer Calculation    #########################################'
            self._DesignParameter['_WELLBodyLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
            self._DesignParameter['_WELLBodyLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_WELLBodyLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        if DesignParameters._Technology=='065nm':
            print '################################     PDK Layer Calculation    ############################################'
            self._DesignParameter['_PDKLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
            self._DesignParameter['_PDKLayer']['_XWidth'] = self._DesignParameter['_NPLayer']['_XWidth']
            self._DesignParameter['_PDKLayer']['_YWidth'] = self._DesignParameter['_NPLayer']['_YWidth']


        print '#########################     Supply Routing Coordinates Calculation   ##################################'
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_NMOSNumberofGate % 2)==0:
            for i in range(0, _NMOSNumberofGate / 2 + 1):
                #_XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] -  _NMOSNumberofGate / 2 \
                                                                                       * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (_NMOSNumberofGate % 2)==1:
            for i in range(0,(_NMOSNumberofGate - 1) / 2 + 1 ):
                #_XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - (  (_NMOSNumberofGate + 1) / 2 - 0.5) \
                                                                                       * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']=tmp


        print '#########################     Output Routing Coordinates Calculation    ##################################'
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_NMOSNumberofGate % 2)==0:
            for i in range(0, _NMOSNumberofGate / 2 ):
                # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 \
                                                                                       * _LengthNMOSBtwMet1 + ( i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (_NMOSNumberofGate % 2)==1:
            for i in range(0, (_NMOSNumberofGate - 1) / 2 + 1):
                # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5)\
                                                                                       * _LengthNMOSBtwMet1 + ( i * 2 + 1 ) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']=tmp



        print '#########################     Gate Routing Coordinates Calculation   ##################################'
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate / 2 - 0.5) \
                                                                                    * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
                #_xycoordinatetmp = self.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[self._XYCoordinateNMOS[0] - (self._NumberOfNMOSGate / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]], _WidthX=self._LengthNMOSPO, _WidthY=self._WidthNMOSPO)
            elif (_NMOSNumberofGate % 2) == 1:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2 \
                                                                                    * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,   _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']=tmp



        del _DRCObj
        print '#########################################################################################################'
        print '                                    {}  NMOSContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name'])
        print '#########################################################################################################'


if __name__=='__main__':
    _NMOSFinger = 1
    _NMOSWidth = 200
    _NMOSChannelLength = 30
    _NMOSDummy = True
    _SLVT = True
    _LVT = False
    _HVT = False
    DesignParameters._Technology='028nm'
#    print 'Technology Process', DesignParameters._Technology
    NMOSObj=_NMOS(_DesignParameter=None, _Name='NMOS')
    NMOSObj._CalculateNMOSDesignParameter(_NMOSNumberofGate=_NMOSFinger, _NMOSChannelWidth=_NMOSWidth, _NMOSChannellength=_NMOSChannelLength, _NMOSDummy=_NMOSDummy, _SLVT=_SLVT)
    NMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=NMOSObj._DesignParameter)
    testStreamFile=open('./testStreamFile2.gds','wb')
    tmp=NMOSObj._CreateGDSStream(NMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()
   

    print '##########################################################################################'
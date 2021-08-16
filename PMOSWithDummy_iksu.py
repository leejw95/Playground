import StickDiagram
import DesignParameters
import DRC

#
from Private import MyInfo
from Private import FileManage


class _PMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False, _XVT=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),

                _PLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PLVT'][0], _Datatype=DesignParameters._LayerMapping['PLVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PHVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PHVT'][0], _Datatype=DesignParameters._LayerMapping['PHVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),

                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0], _Datatype=DesignParameters._LayerMapping['RXPIN'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _SLVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],_Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _LVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVT'][0], _Datatype=DesignParameters._LayerMapping['LVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _RVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _HVTLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['HVT'][0], _Datatype=DesignParameters._LayerMapping['HVT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0], _Datatype=DesignParameters._LayerMapping['PCPIN'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0], _Datatype=DesignParameters._LayerMapping['M1PIN'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PCCRITLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0], _Datatype=DesignParameters._LayerMapping['PCCRIT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),

                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    # Input Variable
    def _CalculatePMOSDesignParameter(self, _PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False, _XVT=None):
        print ('#########################################################################################################')
        print ('                                    {}  PMOS Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _XYCoordinateOfPMOS = [[0,0]]

        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _PMOSChannellength
        _LengthPMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        print ('#############################     POLY (PO/PC) Layer Calculation    ##############################################')
        # POLY Layer Coordinate Calc
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO,  _XYCoordinateOfPMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO, _XYCoordinateOfPMOS[0][1]]

            tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_POLayer']['_XWidth'] = _PMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs


        print ('#############################     DIFF (OD/RX) Layer Calculation    ##############################################')

        self._DesignParameter['_ODLayer']['_XWidth'] = _LengthPMOSBtwPO*_PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_YWidth'] = _PMOSChannelWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS


        if _PMOSDummy == True:  # Only for Samsung?
            print ('#############################     POLY Dummy Layer Calculation    ##############################################')
            # POLY Dummy Layer XWidth and YWidth Setting
            self._DesignParameter['_PODummyLayer']['_XWidth'] = _PMOSChannellength
            self._DesignParameter['_PODummyLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD

            # POLY Dummy Layer Coordinate Setting
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp_dummy = [
                                   [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2),  _XYCoordinateOfPMOS[0][1]],
                                   [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2,  _XYCoordinateOfPMOS[0][1]]
                                   ]
            else:
                _xycoordinatetmp_dummy = [
                                   [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + 0 * _LengthPMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfPMOS[0][1]],
                                   [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + (_PMOSNumberofGate - 1) * _LengthPMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) + (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfPMOS[0][1]]
                                   ]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp_dummy

            if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:  # Should check at TSMC
                self._DesignParameter['_PODummyLayer']['_YWidth'] = self.RoundupMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing*2)

        else:
            self._DesignParameter['_PODummyLayer']['_XWidth'] = 0
            self._DesignParameter['_PODummyLayer']['_YWidth'] = 0


        print ('#############################     METAL1 Layer Calculation    ##############################################')
        # METAL1 Layer Coordinate Setting
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmpXYs = []
        for i in range(0, _PMOSNumberofGate + 1):  # the number of the metal = the number of the gate + 1
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                    _XYCoordinateOfPMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                    _XYCoordinateOfPMOS[0][1]]

            tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']


        print ('############################# CONT (Source/Drain) Layer Calculation    ##############################################')
        # CONT XNum/YNum Calculation
        _XNumberOfCOInPMOS = _PMOSNumberofGate + 1
        _YNumberOfCOInPMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2]) + _DRCObj._CoMinSpace) / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))

        # Check the number of CO On PMOS TR
        if (_XNumberOfCOInPMOS == 0) or (_YNumberOfCOInPMOS == 0):
            print ('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

        # CONT XY coordinates Calculation
        tmpXYs = []
        for i in range(0, _XNumberOfCOInPMOS):
            for j in range(0, _YNumberOfCOInPMOS):

                if (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS% 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        print ('#############################     PIMP (PP/BP) Layer Calculation    ####################')  # Need to check

        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo

        if (DesignParameters._Technology == '065nm') and (_PMOSDummy == True):  # Unverified design / just keep the legacy code
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PODummyLayer']['_XWidth'] \
                                                           + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) \
                                                           + 2 * _DRCObj._PpMinEnclosureOfPo
        else:                                                                   # verifed when (28nm, long Channel Lnegth, w/ w/o dummy) & when (tsmc65, w/o dummy)
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] \
                                                           + 2 * _DRCObj._PpMinExtensiononPactive

        # XVT Layer Calculation
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = '_' + _XVT + 'Layer'
            elif (DesignParameters._Technology == '065nm') and _XVT in ('LVT', 'HVT'):
                _XVTLayer = '_P' + _XVT + 'Layer'
            elif (DesignParameters._Technology == '065nm') and (_XVT == None):
                _XVTLayer = None

            elif DesignParameters._Technology == '028nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 028nm".format(_XVT))
            elif DesignParameters._Technology == '065nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 065nm".format(_XVT))
            else:
                raise NotImplementedError("Not Implemented in other technology : {}".format(DesignParameters._Technology))

            if _XVTLayer != None:
                print ('#############################     {0} Layer Calculation    ##############################################'.format(_XVTLayer))
                self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX
                self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        except Exception as e:
            print('Error Occurred', e)
            raise NotImplementedError

        # ?
        if DesignParameters._Technology == '028nm':  # ?
            print ('#############################     PCCRIT Layer Calculation    ##############################################')
            if self._DesignParameter['_POLayer']['_XWidth'] < 34:
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = _PMOSNumberofGate * _LengthPMOSBtwMet1 + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS
            else:
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = []


        print ('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate / 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                            _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2) == 1:
            for i in range(0,(_PMOSNumberofGate - 1) / 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                            _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Output Routing Coordinates Calculation    ##################################')
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate / 2):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0, (_PMOSNumberofGate - 1) / 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
            else:
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'] = tmpXYs


        if DesignParameters._Technology == '028nm':  # ?
            print ('##################################################### Diff Pin Generation & Coordinates ####################################################')
            self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)
            self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

            self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [[(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                                                                              _XYCoordinateOfPMOS[0][1]],
                                                                             [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                                                                              _XYCoordinateOfPMOS[0][1]]]


            print ('##################################################### POLayer Pin Generation & Coordinates ####################################################')
            self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2
            tmp1 = []
            tmp2 = []
            for i in range(0, len(self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp1.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], - (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
                tmp2.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

            if _PMOSNumberofGate == 1:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
            else:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1


        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  PMOS Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


if __name__ == '__main__':
    _PMOSFinger = 6
    _PMOSWidth = 400    # ? (samsung) / 200 (65nm)
    _PMOSChannelLength = 30  # 30 (samsung) / 60 (65nm)
    _PMOSDummy = False
    _XVT = 'SLVT'            # 'SLVT' 'LVT' 'HVT'

    _fileName = 'PMOSWithDummy_iksu.gds'
    libname = 'TEST_MOS'

    print ('Technology Process', DesignParameters._Technology)
    PMOSObj = _PMOS(_DesignParameter=None, _Name='PMOS')
    PMOSObj._CalculatePMOSDesignParameter(_PMOSNumberofGate=_PMOSFinger, _PMOSChannelWidth=_PMOSWidth, _PMOSChannellength=_PMOSChannelLength, _PMOSDummy=_PMOSDummy, _XVT=_XVT)
    PMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PMOSObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = PMOSObj._CreateGDSStream(PMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
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

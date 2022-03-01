import DesignParameters
import NMOSWithDummy_iksu
from SthPack import CoordCalc


class _CascodeNMOS(NMOSWithDummy_iksu._NMOS):
    _ParametersForDesignCalculation = dict(_NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _XVT=None, _GateSpacing=None)


    def _CalculateDesignParameter(self, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _XVT=None, _GateSpacing=None):

        self._CalculateNMOSDesignParameter(
            _NMOSNumberofGate=2,
            _NMOSChannelWidth=_NMOSChannelWidth, _NMOSChannellength=_NMOSChannellength,
            _NMOSDummy=_NMOSDummy, _XVT=_XVT, _DistanceBtwFinger=_GateSpacing+_NMOSChannellength
        )

        # Delete middle metal1 layer and contact
        XYCoordOfNMOSDrain = CoordCalc.getXYCoords_MinX(self.getXY('_Met1Layer'))
        XYCoordOfNMOSSource = CoordCalc.getXYCoords_MaxX(self.getXY('_Met1Layer'))
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = XYCoordOfNMOSDrain + XYCoordOfNMOSSource
        self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = XYCoordOfNMOSDrain + XYCoordOfNMOSSource
        self._DesignParameter['_COLayer']['_XYCoordinates'] = \
            CoordCalc.getXYCoords_MinX(self.getXY('_COLayer')) + CoordCalc.getXYCoords_MaxX(self.getXY('_COLayer'))

        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = XYCoordOfNMOSSource
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = XYCoordOfNMOSDrain


if __name__ == '__main__':

    from Private import MyInfo
    import DRCchecker

    libname = 'TEST_MOS'
    cellname = 'CascodeNMOS'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NMOSChannelWidth=500,      # Minimum value : 200 (samsung) / 200 (65nm)
        _NMOSChannellength=30,      # Minimum value : 30 (samsung) / 60 (65nm)
        _NMOSDummy=True,
        _XVT='SLVT',                # @ 028nm, 'SLVT' 'LVT' 'RVT' 'HVT' / @ 065nm, 'LVT' 'HVT' or None
        _DistanceBtwFinger=130,
    )

    ''' Generate Layout Object '''
    LayoutObj = _NMOS(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print ('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)

    print('#############################      Finished      ################################')


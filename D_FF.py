# from re import S
from select import select
from tkinter import N
import StickDiagram
import DesignParameters
import copy
import DRC
import D_Latch

class _DFF(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='D_FF'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDFF(self, DLatch1_param={'_TGFinger':1, '_TGChannelWidth':200, '_TGChannelLength':30, '_TGNPRatio':2,
                         '_TGVDD2VSSHeight':None, '_Dummy':True, '_TGXVT':'SLVT', '_TGSupplyMet1YWidth':None,
                         '_INVFinger':5, '_INVChannelWidth':200, '_INVChannelLength':30, '_INVNPRatio':2, \
                         '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
                         '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
                         '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
                         '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
                         '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None},\
                        DLatch2_param={'_TGFinger':1, '_TGChannelWidth':200, '_TGChannelLength':30, '_TGNPRatio':2,
                         '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':None, '_TGSupplyMet1YWidth':None,
                         '_INVFinger':5, '_INVChannelWidth':200, '_INVChannelLength':30, '_INVNPRatio':2, \
                         '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
                         '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
                         '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
                         '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
                         '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None}):

        print(
            '#########################################################################################################')
        print(
            '                                   {}  D_FF Calculation Start                                         '.format(
                self._DesignParameter['_Name']['_Name']))
        print(
            '#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        self._DesignParameter['dlatch1']=self._SrefElementDeclaration(_DesignObj=D_Latch._DLatch(_Name='dlatch1'.format(_Name)))[0]
        self._DesignParameter['dlatch1']['_DesignObj']._CalculateDLatch(**dict(**DLatch1_param))

        self._DesignParameter['dlatch2']=self._SrefElementDeclaration(_DesignObj=D_Latch._DLatch(_Name='dlatch2'.format(_Name)))[0]
        self._DesignParameter['dlatch2']['_DesignObj']._CalculateDLatch(**dict(**DLatch2_param))


        _OriginXY=[[0,0]]
        self._DesignParameter['dlatch1']['_XYCoordinates']=_OriginXY

        _Xcoordinate_temp=self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-\
                          min(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0],\
                              self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0])

        _Xcoordinate_dlatch2=self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+\
                             max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter[ 'dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter[ 'dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0],\
                                 self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0])+\
                             _Xcoordinate_temp+(DLatch1_param['_TGChannelLength']+DLatch2_param['_TGChannelLength'])/2+_DRCObj._PolygateMinSpace

        self._DesignParameter['dlatch2']['_XYCoordinates'] = [[_Xcoordinate_dlatch2,self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]]]


        self._DesignParameter['_UpwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardVDDMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_Width']
        self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]]], \
                                                             ]

        self._DesignParameter['_DownwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardVDDMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_Width']
        self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]]], \
                                                             ]


        self._DesignParameter['_VSSMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_VSSMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_Width']
        self._DesignParameter['_VSSMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_UpwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpwardVDDOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_Width']
        self._DesignParameter['_UpwardVDDOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]]], \
                                                             ]

        self._DesignParameter['_DownwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownwardVDDOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_Width']
        self._DesignParameter['_DownwardVDDOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]]], \
                                                             ]


        self._DesignParameter['_VSSOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_VSSOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_Width']
        self._DesignParameter['_VSSOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_VSSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_VSSPP']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_Width']
        self._DesignParameter['_VSSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_DownPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownPMOSXVT']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_Width']
        self._DesignParameter['_DownPMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_DownNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownNMOSXVT']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_Width']
        self._DesignParameter['_DownNMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_UpPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpPMOSXVT']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_Width']
        self._DesignParameter['_UpPMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_UpNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpNMOSXVT']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_Width']
        self._DesignParameter['_UpNMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_UpPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpPMOSPP']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_Width']
        self._DesignParameter['_UpPMOSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_DownPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownPMOSPP']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_Width']
        self._DesignParameter['_DownPMOSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]], \
                                                              [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]]], \
                                                              ]

        self._DesignParameter['_UpPMOSNW']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_UpPMOSNW']['_Width']=(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)-(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)
        self._DesignParameter['_UpPMOSNW']['_XYCoordinates']=[[[((self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2, self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][1]], \
                                                              [((self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2, self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][1][1]]], \
                                                              ]

        self._DesignParameter['_DownPMOSNW']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_DownPMOSNW']['_Width']=(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)-(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)
        self._DesignParameter['_DownPMOSNW']['_XYCoordinates']=[[[((self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2, self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][1]], \
                                                              [((self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2, self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][1][1]]], \
                                                              ]

        self._DesignParameter['_Met3SigRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
        self._DesignParameter['_Met3SigRouting']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_Width']
        self._DesignParameter['_Met3SigRouting']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][1]],\
                                                                     [(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]+self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])/2, self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][1]],\
                                                                     [(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]+self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])/2, self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][0][1]],\
                                                                     [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TGtoINVOutputRouting1']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][0][1]]]]

        



if __name__ == '__main__':
    import time

    start = time.time()

    DLatch1 = {'_TGFinger': 3, '_TGChannelWidth': 200, '_TGChannelLength': 30, '_TGNPRatio': 2,
                     '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
                     '_INVFinger': 5, '_INVChannelWidth': 200, '_INVChannelLength': 30, '_INVNPRatio': 2, \
                     '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
                     '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
                     '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
                     '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
                     '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None}
    DLatch2 = {'_TGFinger': 3, '_TGChannelWidth': 200, '_TGChannelLength': 30, '_TGNPRatio': 2,
                     '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
                     '_INVFinger': 10, '_INVChannelWidth': 200, '_INVChannelLength': 30, '_INVNPRatio': 2, \
                     '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
                     '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
                     '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
                     '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
                     '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None}

    DesignParameters._Technology = '028nm'

    DFFObj = _DFF(_DesignParameter=None, _Name='D_FF')
    # print ("A!!")
    DFFObj._CalculateDFF(DLatch1_param=DLatch1,DLatch2_param=DLatch2)

    DFFObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=DFFObj._DesignParameter)
    _fileName = 'D_FF.gds'
    testStreamFile = open('./{}'.format(_fileName), 'wb')

    tmp = DFFObj._CreateGDSStream(DFFObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    print("time : ", time.time() - start)

    print('###############      Sending to FTP Server...      ##################')

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('jicho0927', 'cho89140616!!')
    ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
    myfile = open('D_FF.gds', 'rb')
    ftp.storbinary('STOR D_FF.gds', myfile)
    myfile.close()
    ftp.close()

    # import lvstest
    # _LVS = lvstest.LVStest('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/LVS_run','D_Latch','D_Latch','/mnt/sdc/junung/OPUS/Samsung28n')
    # _LVS.LVSchecker()
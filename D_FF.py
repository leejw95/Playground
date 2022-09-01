# from re import S
from re import T
from select import select
from tkinter import N
import StickDiagram
import DesignParameters
import copy
import DRC
import D_Latch
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5

class _DFF(StickDiagram._StickDiagram):
	_ParametersForDesignCalculation = dict(DLatch1_param={'_TGFinger':None, '_TGChannelWidth':None, '_TGChannelLength':None, '_TGNPRatio':None,
						 '_TGVDD2VSSHeight':None, '_Dummy':None, '_TGXVT':'SLVT', '_TGSupplyMet1YWidth':None,
						 '_INVFinger':None, '_INVChannelWidth':None, '_INVChannelLength':None, '_INVNPRatio':None, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':None, '_INVSupplyLine':None},\
						DLatch2_param={'_TGFinger':None, '_TGChannelWidth':None, '_TGChannelLength':None, '_TGNPRatio':None,
						 '_TGVDD2VSSHeight':None, '_Dummy':None, '_TGXVT':None, '_TGSupplyMet1YWidth':None,
						 '_INVFinger':None, '_INVChannelWidth':None, '_INVChannelLength':None, '_INVNPRatio':None, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':None, '_INVSupplyLine':None})



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

		if DLatch1_param['_TGVDD2VSSHeight'] == None and DLatch1_param['_INVVDD2VSSHeight'] == None and DLatch2_param['_TGVDD2VSSHeight'] == None and DLatch2_param['_INVVDD2VSSHeight'] == None:
			det = 0
		else :
			det = 1

		while det !=2 :
			self._DesignParameter['dlatch1']=self._SrefElementDeclaration(_DesignObj=D_Latch._DLatch(_Name='dlatch1In{}'.format(_Name)))[0]
			self._DesignParameter['dlatch1']['_DesignObj']._CalculateDLatch(**dict(**DLatch1_param))

			self._DesignParameter['dlatch2']=self._SrefElementDeclaration(_DesignObj=D_Latch._DLatch(_Name='dlatch2In{}'.format(_Name)),_Reflect = [1,0,0], _Angle = 0)[0]
			self._DesignParameter['dlatch2']['_DesignObj']._CalculateDLatch(**dict(**DLatch2_param))

			if det == 0 :
				_CelltotalHeight = max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_TGVDD2VSSMinHeight']['_Ignore'], self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_INVVDD2VSSMinHeight']['_Ignore'],\
									   self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_TGVDD2VSSMinHeight']['_Ignore'], self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_INVVDD2VSSMinHeight']['_Ignore'])

				DLatch1_param['_TGVDD2VSSHeight']=_CelltotalHeight
				DLatch1_param['_INVVDD2VSSHeight']=_CelltotalHeight
				DLatch2_param['_TGVDD2VSSHeight']=_CelltotalHeight
				DLatch2_param['_INVVDD2VSSHeight']=_CelltotalHeight

				det += 1

			else :
				det += 1

		_OriginXY=[[0,0]]
		self._DesignParameter['dlatch1']['_XYCoordinates']=_OriginXY

		_Xcoordinate_temp=self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-\
						  min(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0],\
							  self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0])

		_Xcoordinate_dlatch2=self.CeilMinSnapSpacing(max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+\
							 max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter[ 'dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter[ 'dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0],\
								 self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0])+\
							 _Xcoordinate_temp+(DLatch1_param['_TGChannelLength']+DLatch2_param['_TGChannelLength'])//2+_DRCObj._PolygateMinSpace,\
							  (self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][0]+\
								self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0]+abs(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0])+_DRCObj._CoMinWidth+_DRCObj._CoMinSpace)), MinSnapSpacing)

		self._DesignParameter['dlatch2']['_XYCoordinates'] = [[_Xcoordinate_dlatch2,self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]]]


		self._DesignParameter['_UpwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpwardVDDMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_Width']
		self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]]], \
															 ]

		self._DesignParameter['_DownwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownwardVDDMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_Width']
		self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]]], \
															 ]


		self._DesignParameter['_VSSMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSMet1']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_Width']
		self._DesignParameter['_VSSMet1']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_UpwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpwardVDDOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_Width']
		self._DesignParameter['_UpwardVDDOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]]], \
															 ]

		self._DesignParameter['_DownwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownwardVDDOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_Width']
		self._DesignParameter['_DownwardVDDOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]]], \
															 ]


		self._DesignParameter['_VSSOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSOD']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_Width']
		self._DesignParameter['_VSSOD']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_VSSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSPP']['_Width']=self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_Width']
		self._DesignParameter['_VSSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		if (DesignParameters._Technology == '028nm') and DLatch1_param['_TGXVT'] in ('SLVT', 'LVT', 'RVT', 'HVT'):
			_XVTPLayer = '_' + DLatch1_param['_TGXVT'] + 'Layer'
			_XVTPLayerLayerMapping = DLatch1_param['_TGXVT']
			_XVTNLayer = '_' + DLatch1_param['_TGXVT'] + 'Layer'
			_XVTNLayerLayerMapping = DLatch1_param['_TGXVT']
		elif (DesignParameters._Technology == '065nm') and DLatch1_param['_TGXVT'] in ('LVT', 'HVT'):
			_XVTPLayer = '_P' + DLatch1_param['_TGXVT'] + 'Layer'
			_XVTPLayerLayerMapping = 'P' + DLatch1_param['_TGXVT']
			_XVTNLayer = '_N' + DLatch1_param['_TGXVT'] + 'Layer'
			_XVTNLayerLayerMapping = 'N' + DLatch1_param['_TGXVT']
		elif (DesignParameters._Technology == '065nm') and (DLatch1_param['_TGXVT'] == None):
			_XVTLayer = None
			_XVTLayerMappingName = None



		self._DesignParameter['_DownPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownPMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing
		self._DesignParameter['_DownPMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_DownNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownNMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing
		self._DesignParameter['_DownNMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_UpPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpPMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing
		self._DesignParameter['_UpPMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_UpNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpNMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing
		self._DesignParameter['_UpNMOSXVT']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][0],self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][-1][0],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]]], \
															  ]

		self._DesignParameter['_UpPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpPMOSPP']['_Width']=self.CeilMinSnapSpacing(max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_Width'],self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_Width']), 2*MinSnapSpacing)
		self._DesignParameter['_UpPMOSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1])], \
															  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][-1][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1])]], \
															  ]

		self._DesignParameter['_DownPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownPMOSPP']['_Width']=self.CeilMinSnapSpacing(max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_Width'],self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_Width']), 2*MinSnapSpacing)
		self._DesignParameter['_DownPMOSPP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1])], \
																 [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][-1][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1],self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1])]], \
															  ]

		self._DesignParameter['_UpPMOSNW']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpPMOSNW']['_Width']=self.CeilMinSnapSpacing(max(self._DesignParameter['_UpPMOSXVT']['_XYCoordinates'][0][1][0]-self._DesignParameter['_UpPMOSXVT']['_XYCoordinates'][0][0][0]+2*_DRCObj._NwMinSpacetoXVT, (self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)-(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)),2*MinSnapSpacing)
		self._DesignParameter['_UpPMOSNW']['_XYCoordinates']=[[[self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][1]], \
															   [self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), self.FloorMinSnapSpacing(min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][1][1], self._DesignParameter['_UpPMOSXVT']['_XYCoordinates'][0][0][1]-self._DesignParameter['_UpPMOSXVT']['_Width']//2), MinSnapSpacing)]], \
															  ]
		if DesignParameters._Technology != '028nm':
			self._DesignParameter['_UpPMOSNW']['_XYCoordinates'].append([[self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1]], \
																		 [self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1])]])

		self._DesignParameter['_DownPMOSNW']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownPMOSNW']['_Width']=self.CeilMinSnapSpacing(max(self._DesignParameter['_DownPMOSXVT']['_XYCoordinates'][0][1][0]-self._DesignParameter['_DownPMOSXVT']['_XYCoordinates'][0][0][0]+2*_DRCObj._NwMinSpacetoXVT, (self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)-(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)),2*MinSnapSpacing)
		self._DesignParameter['_DownPMOSNW']['_XYCoordinates']=[[[self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][1]], \
															  [self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2, MinSnapSpacing), self.CeilMinSnapSpacing(max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][1][1], self._DesignParameter['_DownPMOSXVT']['_XYCoordinates'][0][0][1]+self._DesignParameter['_DownPMOSXVT']['_Width']//2), MinSnapSpacing)]], \
															  ]

		if DesignParameters._Technology != '028nm':
			self._DesignParameter['_DownPMOSNW']['_XYCoordinates'].append([[self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1])], \
																		   [self.CeilMinSnapSpacing(((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2)+(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_XYCoordinates'][0][0][0]-self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSNWRouting']['_Width']/2))/2,MinSnapSpacing), -min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1])]])


		self._DesignParameter['_Met3SigRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met3SigRouting']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_Width'], 2*MinSnapSpacing)
		self._DesignParameter['_Met3SigRouting']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][1]],\
																	 [self.CeilMinSnapSpacing((self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]+self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])/2, MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_ViaMet22Met3OnINV1Output']['_XYCoordinates'][-1][1]],\
																	 [self.CeilMinSnapSpacing((self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]+self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])/2, MinSnapSpacing), self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TGtoINVOutputRouting2']['_XYCoordinates'][0][0][1]],\
																	 [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TGtoINV1OutputRouting1']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TGtoINVOutputRouting2']['_XYCoordinates'][0][0][1]]]]

		if DesignParameters._Technology != '028nm' :
			self._DesignParameter['_UpVDDNP'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_UpVDDNP']['_Width'] = max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_Width'],  self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_Width'])
			self._DesignParameter['_UpVDDNP']['_XYCoordinates'] = [[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_XYCoordinates'][0][0][1]],\
																	[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_XYCoordinates'][0][1][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_XYCoordinates'][0][1][1]]]]

			self._DesignParameter['_DownVDDNP'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_DownVDDNP']['_Width'] = max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_Width'],  self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_Width'])
			self._DesignParameter['_DownVDDNP']['_XYCoordinates'] = [[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_XYCoordinates'][0][0][1]],\
																	  [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_XYCoordinates'][0][-1][1]]]]

			self._DesignParameter['_UpNMOSNP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_UpNMOSNP']['_Width']=max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_Width'],self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_Width'])
			self._DesignParameter['_UpNMOSNP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1])], \
																   [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][1][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1])]], \
																  ]

			self._DesignParameter['_DownNMOSNP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_DownNMOSNP']['_Width']=max(self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_Width'],self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_Width'])
			self._DesignParameter['_DownNMOSNP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1])], \
																	 [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][1][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1])]], \
																  ]

			self._DesignParameter['_AdditionalNMOSNP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_AdditionalNMOSNP']['_Width']=self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])
			self._DesignParameter['_AdditionalNMOSNP']['_XYCoordinates']=[[[self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])//2, MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1]], \
																		   [self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])//2, MinSnapSpacing), max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_NPLayer']['_XYCoordinates'][0][1][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_AdditionalNPLayer']['_XYCoordinates'][0][1][1])]]]

			self._DesignParameter['_AdditionalNWell']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_AdditionalNWell']['_Width']=self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]-(self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])
			self._DesignParameter['_AdditionalNWell']['_XYCoordinates']=[[[self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])//2, MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1]], \
																		  [self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0])//2, MinSnapSpacing), min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1])]],\
																		 [[self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0])//2, MinSnapSpacing), -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1])], \
																		  [self.CeilMinSnapSpacing((self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0])//2, MinSnapSpacing), -min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'][0][1][1])]]]





		_M2M3CLKinputparam=copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
		_M2M3CLKinputparam['_ViaMet22Met3NumberOfCOX'] = 1
		_M2M3CLKinputparam['_ViaMet22Met3NumberOfCOY'] = 2

		_M3M4CLKinputparam=copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
		_M3M4CLKinputparam['_ViaMet32Met4NumberOfCOX'] = 2
		_M3M4CLKinputparam['_ViaMet32Met4NumberOfCOY'] = 2

		self._DesignParameter['_ViaM22M3forCLK']= self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaM22M3forCLKIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM22M3forCLK']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_M2M3CLKinputparam)
		self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates']=[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1]],\
																	[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1]],\
																	[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0], -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1])],\
																	[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0], -(self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1])]]


		self._DesignParameter['_ViaM32M4forCLK']= self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaM32M4forCLKIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_M3M4CLKinputparam)
		self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates']=self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates']
																	#  [[self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2-self._DesignParameter['_ViaM22M3forCLK']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2, self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][0][1]],\
																	# [self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][1][0], self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][1][1]],\
																	# [self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][2][0], self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][2][1]],\
																	#  [self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][3][0], self._DesignParameter['_ViaM22M3forCLK']['_XYCoordinates'][3][1]]]


		self._DesignParameter['_ViaM22M3forCLKb'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaM22M3forCLKbIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM22M3forCLKb']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_M2M3CLKinputparam)
		self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates']=[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1]],\
																	[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1]],\
																	[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0], -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1])],\
																	[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0], -(self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1])]]


		self._DesignParameter['_ViaM32M4forCLKb'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaM32M4forCLKbIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_M3M4CLKinputparam)
		self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates']=self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates']
																	# [[self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][0][0], self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][0][1]], \
																	#  [self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][1][0], self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][1][1]],\
																	#  [self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][2][0]+self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2-self._DesignParameter['_ViaM22M3forCLKb']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']/2, self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][2][1]],\
																	#  [self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][3][0], self._DesignParameter['_ViaM22M3forCLKb']['_XYCoordinates'][3][1]]]

		self._DesignParameter['_Met4CLKRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met4CLKRouting']['_Width']=_DRCObj._MetalxMinWidth * 5
		self._DesignParameter['_Met4CLKRouting']['_XYCoordinates']=[[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKRouting']['_Width']/2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][0][1]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKRouting']['_Width']/2, MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1]],\
																	 [self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][1][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1]],\
																	 [self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][1][1]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)]],\
																	[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][2][0]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKRouting']['_Width']/2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][2][1]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][2][0]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKRouting']['_Width']/2, MinSnapSpacing), -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1])], \
																	 [self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][3][0], -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1])], [self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][3][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][3][1]-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)]]]


		self._DesignParameter['_Met4CLKbRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met4CLKbRouting']['_Width']=_DRCObj._MetalxMinWidth * 5
		self._DesignParameter['_Met4CLKbRouting']['_XYCoordinates']=[[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKbRouting']['_Width']/2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][0][1]+self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][0][0]-self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKbRouting']['_Width']/2, MinSnapSpacing), self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1]],\
																	 [self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][1][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NMOS']['_XYCoordinates'][0][1]],\
																	 [self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][1][1]+self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)]],\
																	[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][2][0]-self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKRouting']['_Width']/2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][2][1]+self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][2][0]-self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2+self._DesignParameter['_Met4CLKbRouting']['_Width']/2, MinSnapSpacing), -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1])], \
																	 [self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][3][0], -(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][1])], [self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][3][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLKb']['_XYCoordinates'][3][1]+self._DesignParameter['_ViaM32M4forCLKb']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']/2, MinSnapSpacing)]]]

		_M4M5CLKinputparam=copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
		_M4M5CLKinputparam['_ViaMet42Met5NumberOfCOX'] = 2
		_M4M5CLKinputparam['_ViaMet42Met5NumberOfCOY'] = 2


		self._DesignParameter['_ViaM42M5forCLK']= self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaM42M5forCLKIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_M4M5CLKinputparam)
		self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates']=[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][2][0]+self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2, MinSnapSpacing), self._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][1][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM32M4forCLK']['_XYCoordinates'][2][0]+self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2-self._DesignParameter['_ViaM32M4forCLK']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']/2, MinSnapSpacing), self._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][-1][1][1]]]

		if DesignParameters._Technology == '028nm':
			_Met5space = _DRCObj._MetalxMinSpace5
		else :
			_Met5space = _DRCObj._MetalxMinSpace3

		self._DesignParameter['_ViaM42M5forCLKb'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaM42M5forCLKbIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaM42M5forCLKb']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_M4M5CLKinputparam)
		self._DesignParameter['_ViaM42M5forCLKb']['_XYCoordinates']=[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/2+self._DesignParameter['_ViaM42M5forCLKb']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/2+_Met5space, MinSnapSpacing), self._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][1][1]], [self.CeilMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][0][0]+self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/2+self._DesignParameter['_ViaM42M5forCLKb']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth']/2+_Met5space, MinSnapSpacing), self._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][-1][1][1]]]

		self._DesignParameter['_Met5CLKRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met5CLKRouting']['_Width']=_DRCObj._MetalxMinWidth * 4
		self._DesignParameter['_Met5CLKRouting']['_XYCoordinates']=[[[self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][0][1]+self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2, MinSnapSpacing)],  [self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][1][0], self.FloorMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLK']['_XYCoordinates'][1][1]-self._DesignParameter['_ViaM42M5forCLK']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2, MinSnapSpacing)]]]

		self._DesignParameter['_Met5CLKbRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met5CLKbRouting']['_Width']=_DRCObj._MetalxMinWidth * 4
		self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates']=[[[self._DesignParameter['_ViaM42M5forCLKb']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLKb']['_XYCoordinates'][0][1]+self._DesignParameter['_ViaM42M5forCLKb']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2, MinSnapSpacing)],  [self._DesignParameter['_ViaM42M5forCLKb']['_XYCoordinates'][1][0], self.FloorMinSnapSpacing(self._DesignParameter['_ViaM42M5forCLKb']['_XYCoordinates'][1][1]-self._DesignParameter['_ViaM42M5forCLKb']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2, MinSnapSpacing)]]]

		self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		self._DesignParameter['_CLKpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='CLK')
		self._DesignParameter['_CLKbpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='CLKb')
		self._DesignParameter['_Dpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='D')
		self._DesignParameter['_Qpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Q')
		self._DesignParameter['_Qbpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Qb')

		self._DesignParameter['_VDDpin']['_XYCoordinates']=[[self.CeilMinSnapSpacing((self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][0][0]+self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][1][0])/2, MinSnapSpacing), self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][0][1]],\
															[self.CeilMinSnapSpacing((self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][0]+self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][1][0])/2, MinSnapSpacing), self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1]]]
		self._DesignParameter['_VSSpin']['_XYCoordinates']=[[(self._DesignParameter['_VSSMet1']['_XYCoordinates'][0][0][0]+self._DesignParameter['_VSSMet1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['_VSSMet1']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['_CLKpin']['_XYCoordinates']=[[self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][1][1])/2, MinSnapSpacing)]]
		self._DesignParameter['_CLKbpin']['_XYCoordinates']=[[self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][1][1])/2, MinSnapSpacing)]]

		self._DesignParameter['_Dpin']['_XYCoordinates']=[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Dpin']['_XYCoordinates'][0][0], self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Dpin']['_XYCoordinates'][0][1]]]
		self._DesignParameter['_Qbpin']['_XYCoordinates']=[[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Qpin']['_XYCoordinates'][0][0], -(self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Qpin']['_XYCoordinates'][0][1])]]
		self._DesignParameter['_Qpin']['_XYCoordinates']=[[self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing(self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+(self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][1][1])/2, MinSnapSpacing)]]



if __name__ == '__main__':
	import time
	import random
	start = time.time()

	# DLatch1 = {'_TGFinger': 3, '_TGChannelWidth': 500, '_TGChannelLength': 60, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': False, '_TGXVT': 'LVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 5, '_INVChannelWidth': 500, '_INVChannelLength': 60, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'LVT', '_INVSupplyLine': None}
	# DLatch2 = {'_TGFinger': 3, '_TGChannelWidth': 500, '_TGChannelLength': 60, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': False, '_TGXVT': 'LVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 10, '_INVChannelWidth': 500, '_INVChannelLength': 60, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'LVT', '_INVSupplyLine': None}

	for i in range(0,100):
		## 028nm ##
		# width=random.randrange(200,400,2)
		# npratio=1 + round(random.random(),1) * 2
		#
		# DLatch1 = {'_TGFinger': random.randint(1,13), '_TGChannelWidth': width, '_TGChannelLength': 30, '_TGNPRatio': npratio,
		#                  '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
		#                  '_INVFinger': random.randint(5,16), '_INVChannelWidth': width, '_INVChannelLength': 30, '_INVNPRatio': npratio, \
		#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
		#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
		#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
		#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
		#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None}
		# DLatch2 = {'_TGFinger': random.randint(1,13), '_TGChannelWidth': width, '_TGChannelLength': 30, '_TGNPRatio': npratio,
		#                  '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
		#                  '_INVFinger': random.randint(5,16), '_INVChannelWidth': width, '_INVChannelLength': 30, '_INVNPRatio': npratio, \
		#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
		#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
		#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
		#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
		#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None}


		## 065nm ##
		width=random.randrange(500,800,10)
		npratio= (width + random.randrange(500,1600,10)) / width

		DLatch1 = {'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':60, '_TGNPRatio':npratio,
						 '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':'LVT', '_TGSupplyMet1YWidth':None,
						 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':60, '_INVNPRatio':npratio, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'LVT', '_INVSupplyLine':None}
		DLatch2 = {'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':60, '_TGNPRatio':npratio,
						 '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':'LVT', '_TGSupplyMet1YWidth':None,
						 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':60, '_INVNPRatio':npratio, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'LVT', '_INVSupplyLine':None}



		#DesignParameters._Technology = '028nm'
		_Name = 'D_FF'

		DFFObj = _DFF(_DesignParameter=None, _Name='D_FF')
		# print ("A!!")
		DFFObj._CalculateDFF(DLatch1_param=DLatch1,DLatch2_param=DLatch2)

		DFFObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=DFFObj._DesignParameter)
		_fileName = 'D_FF.gds'
		testStreamFile = open('./{}'.format(_fileName), 'wb')

		tmp = DFFObj._CreateGDSStream(DFFObj._DesignParameter['_GDSFile']['_GDSFile'])

		tmp.write_binary_gds_stream(testStreamFile)

		testStreamFile.close()


		print('###############      Sending to FTP Server...      ##################')

		# import ftplib
		#
		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('jicho0927', 'cho89140616!!')
		# ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
		# myfile = open('D_FF.gds', 'rb')
		# ftp.storbinary('STOR D_FF.gds', myfile)
		# myfile.close()
		# ftp.close()

		# import DRCchecker
		# _DRC = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run','D_FF','D_FF')
		# _DRC.DRCchecker()


		import ftplib

		ftp = ftplib.FTP('141.223.29.62')
		ftp.login('jicho0927', 'cho89140616!!')
		ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
		myfile = open('D_FF.gds', 'rb')
		ftp.storbinary('STOR D_FF.gds', myfile)
		myfile.close()
		ftp.close()

		import DRCchecker
		_DRC = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','D_FF','D_FF')
		_DRC.DRCchecker()


		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('junung', 'chlwnsdnd1!')
		# ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
		# myfile = open('D_FF.gds', 'rb')
		# ftp.storbinary('STOR D_FF.gds', myfile)
		# myfile.close()
		# ftp.close()
		#
		# print ("###############        Generating Netlist...         ###############")
		# subckt_list = ['TransmissionGate', 'Inverter1', 'Inverter2']
		# essential_param = {'1Finger': DLatch1['_TGFinger'], '1ChannelWidth': DLatch1['_TGChannelWidth'], '1ChannelLength': DLatch1['_TGChannelLength'], '1NPRatio': DLatch1['_TGNPRatio'],
		#     '2Finger': DLatch1['_INVFinger'], '2ChannelWidth': DLatch1['_INVChannelWidth'], '2ChannelLength': DLatch1['_INVChannelLength'], '2NPRatio': DLatch1['_INVNPRatio'],
		#     '3Finger': DLatch2['_INVFinger'], '3ChannelWidth': DLatch2['_INVChannelWidth'], '3ChannelLength': DLatch2['_INVChannelLength'], '3NPRatio': DLatch2['_INVNPRatio']}
		#
		# import Sche
		# _Sche = Sche.Schematic(essential_param, _Name, subckt_list)
		# _Sche.SchematicGenerator()
		#
		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('junung', 'chlwnsdnd1!')
		# ftp.cwd('/mnt/sdc/junung/LVS_run')
		# myfile = open('./Netlist/D_FF.src.net', 'rb')
		# ftp.storbinary('STOR D_FF.src.net', myfile)
		# myfile.close()
		# ftp.close()


		# import LVSchecker
		# _LVS = LVSchecker.LVStest('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/LVS_run','D_FF','D_FF','/mnt/sdc/junung/OPUS/Samsung28n', Vir_Connect=True)
		# _LVS.LVSchecker()

		# import PEX
		# _PEX = PEX.PEX('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/PEX_run','D_FF','D_FF','/mnt/sdc/junung/OPUS/Samsung28n', Vir_Connect=True)
		# _PEX.PEXchecker()

		# import Posim
		# _Posim = Posim.POSIM('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/OPUS/Samsung28n/Ocean_script','Setup_Hold_CLK2Q_simulation.ocn','/mnt/sdc/junung/simulation/tb_D_FF/spectre/schematic','/mnt/sdc/junung/OPUS/Samsung28n/lib_spectre/LN28LPP_Spectre.lib', 'ss', '/mnt/sdc/junung/PEX_run/D_FF.pex.netlist')
		# _Posim.Posimchecker()

		#print("time : ", time.time() - start)
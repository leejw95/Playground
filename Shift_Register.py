# from re import S
from select import select
from tkinter import N
import StickDiagram
import DesignParameters
import copy
import DRC
import D_FF
import NbodyContact



class _ShiftRegister(StickDiagram._StickDiagram):

	def __init__(self, _DesignParameter=None, _Name='Shift_Register'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
										 _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

		if _Name == None:
			self._DesignParameter['_Name']['_Name'] = _Name

	def _CalculateShiftRegister(self,DFF_param={'DLatch1_param':{'_TGFinger':1, '_TGChannelWidth':200, '_TGChannelLength':30, '_TGNPRatio':2,
						 '_TGVDD2VSSHeight':None, '_Dummy':True, '_TGXVT':'SLVT', '_TGSupplyMet1YWidth':None,
						 '_INVFinger':5, '_INVChannelWidth':200, '_INVChannelLength':30, '_INVNPRatio':2, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None},\
						'DLatch2_param':{'_TGFinger':1, '_TGChannelWidth':200, '_TGChannelLength':30, '_TGNPRatio':2,
						 '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':None, '_TGSupplyMet1YWidth':None,
						 '_INVFinger':5, '_INVChannelWidth':200, '_INVChannelLength':30, '_INVNPRatio':2, \
						 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
						 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
						 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
						 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
						 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None}}, Xnum=None, Ynum=None,_CLK_Grid=None):

		print(
			'#########################################################################################################')
		print(
			'                                   {}  Shift_Register Calculation Start                                         '.format(self._DesignParameter['_Name']['_Name']))
		print(
			'#########################################################################################################')

		_DRCObj = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing = _DRCObj._MinSnapSpacing

		self._DesignParameter['Shift_Register_Even']=self._SrefElementDeclaration(_DesignObj=D_FF._DFF(_Name='dff_even'.format(_Name)))[0]
		self._DesignParameter['Shift_Register_Even']['_DesignObj']._CalculateDFF(**dict(**DFF_param))

		self._DesignParameter['Shift_Register_Odd']=self._SrefElementDeclaration(_DesignObj=D_FF._DFF(_Name='dff_odd'.format(_Name)),_Reflect=[1,0,0], _Angle=180)[0]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._CalculateDFF(**dict(**DFF_param))

		_tempX_distance=self.CeilMinSnapSpacing(max((self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0])- \
					   (self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])+\
						self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2+_DRCObj._PolygateMinSpace, \
						self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][-1][0]+\
					   -(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0])+_DRCObj._CoMinWidth+_DRCObj._CoMinSpace, \
					   self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2-(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+\
					   self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']/2)+_DRCObj._MetalxMinSpace, \
					   ), MinSnapSpacing)

		_tempY_distance=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][0][1]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1]

		_tempforoffset=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][-1][0]-(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2),MinSnapSpacing)

		_OriginXY=[[0,0]]
		tmp_even=[]
		tmp_odd=[]

		for j in range(0, (Ynum + 1) // 2):
			for i in range(0,Xnum):
				tmp_even.append([_OriginXY[0][0]+i*_tempX_distance, _OriginXY[0][1]-2*j*_tempY_distance])

		for j in range(0,Ynum//2):
			for i in range(0,Xnum):
				tmp_odd.append([_OriginXY[0][0]+_tempforoffset+i*_tempX_distance, _OriginXY[0][1]-(2*j+1)*_tempY_distance])

		self._DesignParameter['Shift_Register_Even']['_XYCoordinates']=tmp_even
		self._DesignParameter['Shift_Register_Odd']['_XYCoordinates']=tmp_odd

		del tmp_even
		del tmp_odd

		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]

		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]
		self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_TransmissionGate2']['_DesignObj']._DesignParameter['_NbodycontactTG']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]




		tmp=[]

		self._DesignParameter['_UpwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpwardVDDMet1']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_Width']
		for i in range(0,Ynum//2+1):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]]
					   )
		self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_DownwardVDDMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownwardVDDMet1']['_Width']=self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_Width']
		for i in range(0,(Ynum+1)//2):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]]
					   )

		self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates']=tmp

		del tmp

		if Ynum%2==0:

			M1_XWidth=self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][-1][0]-self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][0][0]
			M1_YWidth=self._DesignParameter['_UpwardVDDMet1']['_Width']

			_NumSupplyCoX=int(M1_XWidth // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))
			_NumSupplyCoY=int(M1_YWidth // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))

			_Nbodyinputs = copy.deepcopy(NbodyContact._NbodyContact._ParametersForDesignCalculation)
			_Nbodyinputs['_NumberOfNbodyCOX'] = _NumSupplyCoX
			_Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY


			self._DesignParameter['_AdditionalNbodyContact'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_DesignParameter=None, _Name='_AdditionalNbodyContactIn{}'.format(_Name)))[0]
			self._DesignParameter['_AdditionalNbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)
			self._DesignParameter['_AdditionalNbodyContact']['_XYCoordinates']=[[self.CeilMinSnapSpacing((self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][0][0]+self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][0][-1][0])/2,MinSnapSpacing), self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][-1][0][1]]]

			del _Nbodyinputs
			del M1_YWidth
			del M1_XWidth
			del _NumSupplyCoY
			del _NumSupplyCoX


		tmp=[]

		self._DesignParameter['_VSSMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSMet1']['_Width']=self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_Width']
		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSMet1Routing']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_VSSMet1']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_UpwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpwardVDDOD']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_Width']

		for i in range(0,Ynum//2+1):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDODRouting']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]]
					   )
		self._DesignParameter['_UpwardVDDOD']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_DownwardVDDOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownwardVDDOD']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_Width']

		for i in range(0,(Ynum+1)//2):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDODRouting']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]]
					   )


		self._DesignParameter['_DownwardVDDOD']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_VSSOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSOD']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_Width']

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSODRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_VSSOD']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_VSSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_VSSPP']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_Width']


		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_CenterVSSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_VSSPP']['_XYCoordinates']=tmp

		del tmp

		if (DesignParameters._Technology == '028nm') and DFF_param['DLatch1_param']['_TGXVT'] in ('SLVT', 'LVT', 'RVT', 'HVT'):
			_XVTPLayer = '_' + DFF_param['DLatch1_param']['_TGXVT'] + 'Layer'
			_XVTPLayerLayerMapping = DFF_param['DLatch1_param']['_TGXVT']
			_XVTNLayer = '_' + DFF_param['DLatch1_param']['_TGXVT'] + 'Layer'
			_XVTNLayerLayerMapping = DFF_param['DLatch1_param']['_TGXVT']
		elif (DesignParameters._Technology == '065nm') and DFF_param['DLatch1_param']['_TGXVT'] in ('LVT', 'HVT'):
			_XVTPLayer = '_P' + DFF_param['DLatch1_param']['_TGXVT'] + 'Layer'
			_XVTPLayerLayerMapping = 'P' + DFF_param['DLatch1_param']['_TGXVT']
			_XVTNLayer = '_N' + DFF_param['DLatch1_param']['_TGXVT'] + 'Layer'
			_XVTNLayerLayerMapping = 'N' + DFF_param['DLatch1_param']['_TGXVT']
		elif (DesignParameters._Technology == '065nm') and (DFF_param['DLatch1_param']['_TGXVT'] == None):
			_XVTLayer = None
			_XVTLayerMappingName = None




		tmp=[]

		self._DesignParameter['_DownPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownPMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_DownPMOSXVT']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_DownNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_DownNMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_DownNMOSXVT']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_UpPMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTPLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpPMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_UpPMOSXVT']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_UpNMOSXVT']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][0], _Datatype=DesignParameters._LayerMapping[_XVTNLayerLayerMapping][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_UpNMOSXVT']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_Width'], 2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSXVTRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance)]]
					   )

		self._DesignParameter['_UpNMOSXVT']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_UpPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		if DesignParameters._Technology != '028nm':
			self._DesignParameter['_UpPMOSPP']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSPP']['_Width'],2*MinSnapSpacing)
		elif DesignParameters._Technology == '028nm':
			self._DesignParameter['_UpPMOSPP']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSPP']['_Width'],2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][0]-_DRCObj._PpMinWidth-_DRCObj._PpMinSpace, min(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance),self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance))], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][-1][0]+_DRCObj._PpMinWidth+_DRCObj._PpMinSpace, min(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance),self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance))]]
					   )

		self._DesignParameter['_UpPMOSPP']['_XYCoordinates']=tmp

		del tmp

		tmp=[]

		self._DesignParameter['_DownPMOSPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100)
		if DesignParameters._Technology != '028nm':
			self._DesignParameter['_DownPMOSPP']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSPP']['_Width'],2*MinSnapSpacing)
		elif DesignParameters._Technology == '028nm':
			self._DesignParameter['_DownPMOSPP']['_Width']=self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSPP']['_Width'],2*MinSnapSpacing) + 2*MinSnapSpacing

		for i in range(0,Ynum):
			tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][0]-_DRCObj._PpMinWidth-_DRCObj._PpMinSpace, max(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance),self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance))], \
						[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][-1][0]+_DRCObj._PpMinWidth+_DRCObj._PpMinSpace, max(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance),self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardPMOSPPRouting']['_XYCoordinates'][0][0][1]-i*(_tempY_distance))]]
					   )

		self._DesignParameter['_DownPMOSPP']['_XYCoordinates']=tmp

		del tmp


		_CenterX=(self._DesignParameter['_VSSMet1']['_XYCoordinates'][0][0][0]+self._DesignParameter['_VSSMet1']['_XYCoordinates'][0][1][0])/2


		if Ynum > 1 :
			self._DesignParameter['_NWLayer']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],_XYCoordinates=[],_Width=100)
			if DesignParameters._Technology != '028nm':
				self._DesignParameter['_NWLayer']['_Width']=2*self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_AdditionalNWell']['_XYCoordinates'][1][1][1]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1],2*MinSnapSpacing)

			elif DesignParameters._Technology == '028nm':
				self._DesignParameter['_NWLayer']['_Width']=2*self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSNW']['_XYCoordinates'][0][1][1]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1],2*MinSnapSpacing)

			tmp=[]
			for i in range(0, Ynum-1):
				tmp.append([[self.FloorMinSnapSpacing(min(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSNW']['_XYCoordinates'][0][0][0]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSNW']['_Width']//2, self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSXVT']['_XYCoordinates'][0][0][0]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSXVT']['_Width']//2-_DRCObj._NwMinSpacetoXVT), MinSnapSpacing)-_DRCObj._NwMinWidth-_DRCObj._NwMinSpace-2*MinSnapSpacing, \
							 self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1]-_tempY_distance*i], \
							[self.CeilMinSnapSpacing(max(2*_CenterX-(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSNW']['_XYCoordinates'][0][0][0]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownPMOSNW']['_Width']//2), 2*_CenterX-(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSXVT']['_XYCoordinates'][0][0][0]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_UpPMOSXVT']['_Width']//2-_DRCObj._NwMinSpacetoXVT))+_DRCObj._NwMinWidth+_DRCObj._NwMinSpace, MinSnapSpacing), \
							 self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][0][0][1]-_tempY_distance*i]])

			self._DesignParameter['_NWLayer']['_XYCoordinates']=tmp

			del tmp

		self._DesignParameter['_Met3SigRouting_even']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met3SigRouting_even']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_Width']

		tmp_m3_even=[]
		tmp_m3_odd=[]

		for j in range(0, (Ynum+1)//2):
			for i in range(j*Xnum, j*Xnum+Xnum-1):
				tmp_m3_even.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]], \
							[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i+1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])

		self._DesignParameter['_Met3SigRouting_even']['_XYCoordinates']=tmp_m3_even



		self._DesignParameter['_Met3SigRouting_odd']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met3SigRouting_odd']['_Width']=self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_Width']


		for j in range(0, Ynum//2):
			for i in range(j*Xnum, j*Xnum+Xnum-1):
				# tmp_m3_odd.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]], \
				#             [self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i+1][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])
				tmp_m3_even.append([[2*_CenterX-(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0]), self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]], \
							[2*_CenterX-(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i+1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][-1][0]), self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyNMOSRoutingXTG']['_XYCoordinates'][0][0][1]]])



		self._DesignParameter['_Met3SigRouting_odd']['_XYCoordinates']=tmp_m3_odd

		del tmp_m3_even
		del tmp_m3_odd

		self._DesignParameter['_Met2SigRouting_X_even_odd']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met2SigRouting_X_even_odd']['_Width']=self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_Met2OnOutput']['_Width']



		if Ynum > 1 :
			tmp=[]
			for j in range(0, int((len(self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'])/2)*2)):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][0],\
							 self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][j][0][1]], \
							[(self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][0][0][0]), \
							 self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][j][0][1]]])
			if Ynum%2==1:
				tmp.pop()

			self._DesignParameter['_Met2SigRouting_X_even_odd']['_XYCoordinates']=tmp

			del tmp

		self._DesignParameter['_Met2SigRouting_Y_even_odd']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met2SigRouting_Y_even_odd']['_Width']=self._DesignParameter['_Met2SigRouting_X_even_odd']['_Width']


		tmp=[]

		for j in range(0, len(self._DesignParameter['_Met2SigRouting_X_even_odd']['_XYCoordinates'])):
			for i in range(0,len(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'])):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],\
							 self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][j*Xnum+Xnum-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]-self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][1]],\
							[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0],\
							 self.CeilMinSnapSpacing(self._DesignParameter['_Met2SigRouting_X_even_odd']['_XYCoordinates'][j][0][1]-self._DesignParameter['_Met2SigRouting_X_even_odd']['_Width']/2, MinSnapSpacing)]])
			# if Ynum % 2 == 1:
			#     del tmp[-1]
			for i in range(0,len(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'])):
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][0],\
							 self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][j*Xnum+Xnum-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][1]],\
							[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][0],\
							 self.CeilMinSnapSpacing(self._DesignParameter['_Met2SigRouting_X_even_odd']['_XYCoordinates'][j][0][1]+self._DesignParameter['_Met2SigRouting_X_even_odd']['_Width']/2, MinSnapSpacing)]])
			# if Ynum % 2 == 1:
			#     del tmp[-1]

		self._DesignParameter['_Met2SigRouting_Y_even_odd']['_XYCoordinates']=tmp

		del tmp


		self._DesignParameter['_Met2SigRouting_X_odd_even']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met2SigRouting_X_odd_even']['_Width']=self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter2']['_DesignObj']._DesignParameter['_Met2OnOutput']['_Width']

		tmp=[]


		for j in range(0, len(self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'])-1):
			tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][0]),\
						 self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][j+1][0][1]], \
						[(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][0][0][0]), \
						 self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][j+1][0][1]]])
		if Ynum%2==0:
			del tmp[-1]
		self._DesignParameter['_Met2SigRouting_X_odd_even']['_XYCoordinates']=tmp

		del tmp



		self._DesignParameter['_Met2SigRouting_Y_odd_even']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
		self._DesignParameter['_Met2SigRouting_Y_odd_even']['_Width']=self._DesignParameter['_Met2SigRouting_X_odd_even']['_Width']


		tmp=[]

		for j in range(0, len(self._DesignParameter['_Met2SigRouting_X_odd_even']['_XYCoordinates'])):
			for i in range(0,len(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'])):
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0]),\
							 self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][j*Xnum][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][1]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][1]],\
							[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Inverter1']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'][i][0]),\
							 self.CeilMinSnapSpacing(self._DesignParameter['_Met2SigRouting_X_odd_even']['_XYCoordinates'][j][0][1]-self._DesignParameter['_Met2SigRouting_X_odd_even']['_Width']/2, MinSnapSpacing)]])
			# if Ynum % 2 == 0:
			#     del tmp[-1]
			for i in range(0,len(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'])):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][0],\
							 self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][(j+1)*Xnum][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][1]],\
							[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_TransmissionGate1']['_DesignObj']._DesignParameter['_SupplyRoutingYTG']['_XYCoordinates'][i][0][0],\
							 self.CeilMinSnapSpacing(self._DesignParameter['_Met2SigRouting_X_odd_even']['_XYCoordinates'][j][0][1]+self._DesignParameter['_Met2SigRouting_Y_odd_even']['_Width']/2, MinSnapSpacing)]])
			#if Ynum % 2 == 0:
			#     del tmp[-1]

		self._DesignParameter['_Met2SigRouting_Y_odd_even']['_XYCoordinates']=tmp

		del tmp

		if DesignParameters._Technology != '028nm' :
			tmp=[]
			self._DesignParameter['_UpVDDNP'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_UpVDDNP']['_Width'] = max(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_Width'],  self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDNPRouting']['_Width'])
			for i in range(0,Ynum//2+1):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
							[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]])
			self._DesignParameter['_UpVDDNP']['_XYCoordinates']=tmp
			del tmp

			tmp=[]
			self._DesignParameter['_DownVDDNP'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_DownVDDNP']['_Width'] = max(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_Width'],  self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDNPRouting']['_Width'])
			for i in range(0,(Ynum+1)//2):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)], \
							[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1] + self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardVDDMet1Routing']['_XYCoordinates'][0][0][1]-i*(2*_tempY_distance)]])
			self._DesignParameter['_DownVDDNP']['_XYCoordinates']=tmp
			del tmp



			# self._DesignParameter['_UpNMOSNP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			# self._DesignParameter['_UpNMOSNP']['_Width']=max(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_Width'],self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_Width'])
			# self._DesignParameter['_UpNMOSNP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1])], \
			# 													   [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][1][0], max(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_UpwardNMOSNPRouting']['_XYCoordinates'][0][0][1])]], \
			# 													  ]
			#
			# self._DesignParameter['_DownNMOSNP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100)
			# self._DesignParameter['_DownNMOSNP']['_Width']=max(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_Width'],self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_Width'])
			# self._DesignParameter['_DownNMOSNP']['_XYCoordinates']=[[[self._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1])], \
			# 														 [self._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][1][0], min(self._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1], self._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+self._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_DownwardNMOSNPRouting']['_XYCoordinates'][0][0][1])]], \
			# 													  ]




		if _CLK_Grid==True:

			self._DesignParameter['_Met4CLKRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_Met4CLKRouting']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_Width']

			tmp=[]

			for j in range(0,(Ynum+1)//2):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)]])
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)]])


			for j in range(0,Ynum//2):
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)]])
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][-1][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)]])

			self._DesignParameter['_Met4CLKRouting']['_XYCoordinates']=tmp

			del tmp

			self._DesignParameter['_Met4CLKbRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_Met4CLKbRouting']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_Width']

			tmp=[]

			for j in range(0,(Ynum+1)//2):
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)]])
				tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][-1][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)]])


			for j in range(0,Ynum//2):
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][-1][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][0][1][1]-j*(2*_tempY_distance)]])
				tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][-1][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)], [self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][0]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][Xnum-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met4CLKbRouting']['_XYCoordinates'][1][1][1]-j*(2*_tempY_distance)]])

			self._DesignParameter['_Met4CLKbRouting']['_XYCoordinates']=tmp

			del tmp

			self._DesignParameter['_Met5CLKRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_Met5CLKRouting']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_Width']

			tmp=[]

			if Ynum > 1:
				for i in range(0,Xnum):
					tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][1]], \
								[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][-1][1]]])
					tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][1]], \
								[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][-1][1]]])

			# else:
			#     for i in range(0,Xnum):
			#         tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][1]], \
			#                     [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][0][-1][1]]])

			self._DesignParameter['_Met5CLKRouting']['_XYCoordinates']=tmp

			del tmp

			self._DesignParameter['_Met5CLKbRouting']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[],_Width=100)
			self._DesignParameter['_Met5CLKbRouting']['_Width']=self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_Width']

			tmp=[]

			if Ynum > 1:
				for i in range(0,Xnum):
					tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][1]], \
								[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][-1][1]]])
					tmp.append([[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][1]], \
								[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][-1][1]]])

			# else :
			#     for i in range(0,Xnum):
			#         tmp.append([[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][1]], \
			#                     [self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][-1][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][0][-1][1]]])

				self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates']=tmp

				del tmp

			self._DesignParameter['_CLKpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='CLK')
			self._DesignParameter['_CLKbpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='CLKb')

			tmp = []

			for i in range(0, len(self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'])):
				tmp.append([self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][i][0][0], (self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][i][0][1] + self._DesignParameter['_Met5CLKRouting']['_XYCoordinates'][i][1][1]) / 2])

			self._DesignParameter['_CLKpin']['_XYCoordinates'] = tmp

			del tmp

			tmp = []

			for i in range(0, len(self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'])):
				tmp.append([self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][i][0][0], (self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][i][0][1] + self._DesignParameter['_Met5CLKbRouting']['_XYCoordinates'][i][1][1]) / 2])

			self._DesignParameter['_CLKbpin']['_XYCoordinates'] = tmp

			del tmp



		self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		self._DesignParameter['_Dpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='D')

		tmp=[]

		for i in range(0, len(self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'])):
			tmp.append([self.CeilMinSnapSpacing((self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][i][0][0]+self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][i][1][0])/2, MinSnapSpacing), self._DesignParameter['_UpwardVDDMet1']['_XYCoordinates'][i][0][1]])

		for i in range(0, len(self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'])):
			tmp.append([self.CeilMinSnapSpacing((self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][i][0][0]+self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][i][1][0])/2, MinSnapSpacing), self._DesignParameter['_DownwardVDDMet1']['_XYCoordinates'][i][0][1]])

		self._DesignParameter['_VDDpin']['_XYCoordinates']=tmp

		del tmp

		tmp = []

		for i in range(0, len(self._DesignParameter['_VSSMet1']['_XYCoordinates'])):
			tmp.append([(self._DesignParameter['_VSSMet1']['_XYCoordinates'][i][0][0] + self._DesignParameter['_VSSMet1']['_XYCoordinates'][i][1][0]) / 2, self._DesignParameter['_VSSMet1']['_XYCoordinates'][i][0][1]])


		self._DesignParameter['_VSSpin']['_XYCoordinates']=tmp

		del tmp



		self._DesignParameter['_Dpin']['_XYCoordinates']=[[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Dpin']['_XYCoordinates'][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_XYCoordinates'][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch1']['_DesignObj']._DesignParameter['_Dpin']['_XYCoordinates'][0][1]]]


		for j in range(0,(Ynum+1)//2):
			for i in range(Xnum*j,Xnum*(j+1)):
				self._DesignParameter['_Q<{0}>pin'.format(i+Xnum*j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1]+(self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][1][1])/2, MinSnapSpacing)]], \
																									_Mag=0.05, _Angle=0, _TEXT='Q<{0}>'.format(i+Xnum*j))

		for j in range(0,Ynum//2):
			for i in range(Xnum*j,Xnum*(j+1)):
				self._DesignParameter['_Q<{0}>pin'.format((2*(j+1)*Xnum-1)-i+Xnum*j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing(self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][1]-(self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][1][1])/2, MinSnapSpacing)]], \
																									_Mag=0.05, _Angle=0, _TEXT='Q<{0}>'.format((2*(j+1)*Xnum-1)-i+Xnum*j))

	   # del self._DesignParameter['_Q<{0}>pin'.format(0)]



		for j in range(0,(Ynum+1)//2):
			for i in range(Xnum*j,Xnum*(j+1)):
				self._DesignParameter['_Qb<{0}>pin'.format(i+Xnum*j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_INV1OuttoINV2InRouting']['_XYCoordinates'][0][0][0], self._DesignParameter['Shift_Register_Even']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['_Qbpin']['_XYCoordinates'][0][1]]],#+self._DesignParameter['Shift_Register_Even']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Qpin']['_XYCoordinates'][0][1]]], \
																									_Mag=0.05, _Angle=0, _TEXT='Qb<{0}>'.format(i+Xnum*j))

		for j in range(0,Ynum//2):
			for i in range(Xnum*j,Xnum*(j+1)):
				self._DesignParameter['_Qb<{0}>pin'.format((2*(j+1)*Xnum-1)-i+Xnum*j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_XYCoordinates'][0][0]-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Qpin']['_XYCoordinates'][0][0], self._DesignParameter['Shift_Register_Odd']['_XYCoordinates'][i][1]+self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['_Qbpin']['_XYCoordinates'][0][1]]], #-self._DesignParameter['Shift_Register_Odd']['_DesignObj']._DesignParameter['dlatch2']['_DesignObj']._DesignParameter['_Qpin']['_XYCoordinates'][0][1]]], \
																									_Mag=0.05, _Angle=0, _TEXT='Qb<{0}>'.format((2*(j+1)*Xnum-1)-i+Xnum*j))





if __name__ == '__main__':
	import time
	import random
	start = time.time()

	# input_params={'DFF_param':{'DLatch1_param':{'_TGFinger': 3, '_TGChannelWidth': 500, '_TGChannelLength': 60, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': False, '_TGXVT': 'LVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 5, '_INVChannelWidth': 500, '_INVChannelLength': 60, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'LVT', '_INVSupplyLine': None},\
	#                             'DLatch2_param':{'_TGFinger': 3, '_TGChannelWidth': 500, '_TGChannelLength': 60, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': False, '_TGXVT': 'LVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 10, '_INVChannelWidth': 500, '_INVChannelLength': 60, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'LVT', '_INVSupplyLine': None}},
	#                     'Xnum':2,'Ynum':2,'_CLK_Grid':True}

	# input_params={'DFF_param':{'DLatch1_param':{'_TGFinger': 3, '_TGChannelWidth': 200, '_TGChannelLength': 30, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 5, '_INVChannelWidth': 200, '_INVChannelLength': 30, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None},\
	#                             'DLatch2_param':{'_TGFinger': 3, '_TGChannelWidth': 200, '_TGChannelLength': 30, '_TGNPRatio': 2,
	#                  '_TGVDD2VSSHeight': None, '_Dummy': True, '_TGXVT': 'SLVT', '_TGSupplyMet1YWidth': None,
	#                  '_INVFinger': 10, '_INVChannelWidth': 200, '_INVChannelLength': 30, '_INVNPRatio': 2, \
	#                  '_INVVDD2VSSHeight': None, '_INVNumSupplyCoX': None, '_INVNumSupplyCoY': None, \
	#                  '_INVSupplyMet1XWidth': None, '_INVSupplyMet1YWidth': None, '_INVNumViaPoly2Met1CoX': None, \
	#                  '_INVNumViaPoly2Met1CoY': None, '_INVNumViaPMOSMet12Met2CoX': None, \
	#                  '_INVNumViaPMOSMet12Met2CoY': None, '_INVNumViaNMOSMet12Met2CoX': None,
	#                  '_INVNumViaNMOSMet12Met2CoY': None, '_INVXVT': 'SLVT', '_INVSupplyLine': None}},
	#                     'Xnum':7,'Ynum':7,'_CLK_Grid':True}

	for i in range(0,50):
		### 028nm ###
		width=random.randrange(200,400,2)
		npratio=1 + round(random.random(),1) * 2

		input_params={'DFF_param':{'DLatch1_param':{'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':30, '_TGNPRatio':npratio,
		                 '_TGVDD2VSSHeight':None, '_Dummy':True, '_TGXVT':'SLVT', '_TGSupplyMet1YWidth':None,
		                 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':30, '_INVNPRatio':npratio, \
		                 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
		                 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
		                 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
		                 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
		                 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None},\
		                'DLatch2_param':{'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':30, '_TGNPRatio':npratio,
		                 '_TGVDD2VSSHeight':None, '_Dummy':True, '_TGXVT':'SLVT', '_TGSupplyMet1YWidth':None,
		                 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':30, '_INVNPRatio':npratio, \
		                 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
		                 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
		                 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
		                 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
		                 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'SLVT', '_INVSupplyLine':None}}, 'Xnum':random.randrange(1,10),'Ynum':random.randrange(1,10), '_CLK_Grid':True}

		### 065nm ###
		# width=random.randrange(500,800,10)
		# npratio= (width + random.randrange(500,1600,10)) / width
		#
		# input_params={'DFF_param':{'DLatch1_param':{'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':60, '_TGNPRatio':npratio,
		# 				 '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':'LVT', '_TGSupplyMet1YWidth':None,
		# 				 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':60, '_INVNPRatio':npratio, \
		# 				 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
		# 				 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
		# 				 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
		# 				 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
		# 				 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'LVT', '_INVSupplyLine':None},\
		# 				'DLatch2_param':{'_TGFinger':random.randint(1,13), '_TGChannelWidth':width, '_TGChannelLength':60, '_TGNPRatio':npratio,
		# 				 '_TGVDD2VSSHeight':None, '_Dummy':False, '_TGXVT':'LVT', '_TGSupplyMet1YWidth':None,
		# 				 '_INVFinger':random.randint(5,16), '_INVChannelWidth':width, '_INVChannelLength':60, '_INVNPRatio':npratio, \
		# 				 '_INVVDD2VSSHeight':None, '_INVNumSupplyCoX':None, '_INVNumSupplyCoY':None, \
		# 				 '_INVSupplyMet1XWidth':None, '_INVSupplyMet1YWidth':None, '_INVNumViaPoly2Met1CoX':None, \
		# 				 '_INVNumViaPoly2Met1CoY':None, '_INVNumViaPMOSMet12Met2CoX':None, \
		# 				 '_INVNumViaPMOSMet12Met2CoY':None, '_INVNumViaNMOSMet12Met2CoX':None,
		# 				 '_INVNumViaNMOSMet12Met2CoY':None, '_INVXVT':'LVT', '_INVSupplyLine':None}}, 'Xnum':random.randrange(1,10),'Ynum':random.randrange(1,10), '_CLK_Grid':True}



		#DesignParameters._Technology = '028nm'
		_Name = 'Shift_Register'

		SRObj = _ShiftRegister(_DesignParameter=None, _Name='Shift_Register')
		# print ("A!!")
		SRObj._CalculateShiftRegister(**input_params)

		SRObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SRObj._DesignParameter)
		_fileName = 'Shift_Register.gds'
		testStreamFile = open('./{}'.format(_fileName), 'wb')

		tmp = SRObj._CreateGDSStream(SRObj._DesignParameter['_GDSFile']['_GDSFile'])

		tmp.write_binary_gds_stream(testStreamFile)

		testStreamFile.close()


		print('###############      Sending to FTP Server...      ##################')

		import ftplib

		ftp = ftplib.FTP('141.223.29.62')
		ftp.login('jicho0927', 'cho89140616!!')
		ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
		myfile = open('Shift_Register.gds', 'rb')
		ftp.storbinary('STOR Shift_Register.gds', myfile)
		myfile.close()
		ftp.close()

		import DRCchecker
		_DRC = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run','Shift_Register','Shift_Register')
		_DRC.DRCchecker()


		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('jicho0927', 'cho89140616!!')
		# ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
		# myfile = open('Shift_Register.gds', 'rb')
		# ftp.storbinary('STOR Shift_Register.gds', myfile)
		# myfile.close()
		# ftp.close()
		#
		#
		# import DRCchecker
		# _DRC = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','Shift_Register','Shift_Register')
		# _DRC.DRCchecker()

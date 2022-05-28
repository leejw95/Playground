************************************************************************
* auCdl Netlist:
* 
* Library Name:  D_FF_test
* Top Cell Name: D_Latch
* View Name:     schematic
* Netlisted on:  May 28 13:45:13 2022
************************************************************************

.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl
*.BIPOLAR
*.RESI = 2000 
*.RESVAL
*.CAPVAL
*.DIOPERI
*.DIOAREA
*.EQUATION
*.SCALE METER
*.MEGA
.PARAM



************************************************************************
* Library Name: D_FF_test
* Cell Name:    FF_sw_600n_201909_mglee
* View Name:    schematic
************************************************************************

.SUBCKT FF_sw_600n_201909_mglee IN OUT S SB VDD VSS
*.PININFO S:I SB:I IN:B OUT:B VDD:B VSS:B
MP0 IN SB OUT VDD slvtpfet w=1.2u l=0.03u nf=3.0 pccrit=1 plorient=1 ngcon=1 
+ p_la=0u ptwell=0
MN1 IN S OUT VSS slvtnfet w=0.6u l=0.03u nf=3.0 pccrit=1 plorient=1 ngcon=1 
+ p_la=0u ptwell=0
.ENDS

************************************************************************
* Library Name: D_FF_test
* Cell Name:    FF_Inv_1u
* View Name:    schematic
************************************************************************

.SUBCKT FF_Inv_1u IN OUT VDD VSS
*.PININFO IN:I VDD:I VSS:I OUT:O
MP0 OUT IN VDD VDD slvtpfet w=2u l=0.03u nf=5.0 pccrit=1 plorient=1 ngcon=1 
+ p_la=0u ptwell=0
MN0 OUT IN VSS VSS slvtnfet w=1u l=0.03u nf=5.0 pccrit=1 plorient=1 ngcon=1 
+ p_la=0u ptwell=0
.ENDS

************************************************************************
* Library Name: D_FF_test
* Cell Name:    D_Latch
* View Name:    schematic
************************************************************************

.SUBCKT D_Latch CLK CLKb D Q
*.PININFO CLK:I CLKb:I D:I Q:O
XI11 net16 net11 CLK CLKb VDD VSS / FF_sw_600n_201909_mglee
XI3 D net11 CLKb CLK VDD VSS / FF_sw_600n_201909_mglee
XI2 Q net16 VDD VSS / FF_Inv_1u
XI1 net11 Q VDD VSS / FF_Inv_1u
.ENDS


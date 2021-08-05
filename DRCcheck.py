import paramiko
import sys
import os

def DRCcheck(server, port, username, password, Dir1) :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print ("############ Connecting to Server... ############")
    ssh.connect('141.223.22.156', port = '22', username='junung', password='chlwnsdnd1!')


    commandlines1 = "cd OPUS/Samsung28n; source setup.cshrc; strmin -library 'SlicerwtRR5' -strmFile '/mnt/sdc/junung/OPUS/Samsung28n/SlicerandSRLatchwtResistor.gds' -attachTechFileOfLib 'cmos28lp' -logFile 'strmIn.log'"
    stdin, stdout, stderr = ssh.exec_command(commandlines1)
    print (''.join(stdout.read()))

    commandlines2 = "cd OPUS/Samsung28n; source setup.cshrc; strmout -library 'SlicerwtRR5' -strmFile '/mnt/sdc/junung/OPUS/Samsung28n/DRC/run/SlicerandSRLatchwtResistor.calibre.db' -topCell 'SlicerandSRLatchwtResistor' -view layout -runDir '/mnt/sdc/junung/OPUS/Samsung28n/DRC/run/' -logFile 'PIPO.LOG.SlicerandSRLatchwtResistor' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
    stdin, stdout, stderr = ssh.exec_command(commandlines2)
    print (''.join(stdout.read()))

    commandlines4 = "cd OPUS/Samsung28n/DRC/run; sed -i '9s,.*,LAYOUT PATH  \"/mnt/sdc/junung/OPUS/Samsung28n/DRC/run/SlicerandSRLatchwtResistor.calibre.db\",' _cmos28lp.drc.cal_"
    stdin, stdout, stderr = ssh.exec_command(commandlines4)
    print (''.join(stdout.read()))

    commandlines3 = "cd OPUS/Samsung28n; source setup.cshrc; calibre -drc -hier -nowait /mnt/sdc/junung/OPUS/Samsung28n/DRC/run/_cmos28lp.drc.cal_"
    stdin, stdout, stderr = ssh.exec_command(commandlines3)
    print (''.join(stdout.read()))

    readfile = ssh.open_sftp()
    file = readfile.open(os.path.join('/mnt/sdc/junung/OPUS/Samsung28n','SlicerandSRLatchwtResistor.drc.summary'))
    for line in (file.readlines() [-2:-1]) :
        print (line)
        if "0" not in line :
            continue

        else :
            commandlines5 = "cd OPUS/Samsung28n; source setup.cshrc; virtuoso -nograph -restore Skillcode.il"
            stdin, stdout, stderr = ssh.exec_command(commandlines5)
            print (''.join(stdout.read()))



    ssh.close
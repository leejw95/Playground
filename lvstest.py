import paramiko
import ftplib
import os
import sys
import time
import DesignParameters


class LVStest :
    def __init__(self, username, password, WorkDir, LVSrunDir, libname, cellname, GDSDir) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.LVSrunDir = LVSrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir


    def LVSchecker(self) :

        '''
            This routine should be performed after modifying spice netlist file...
        '''

        if DesignParameters._Technology == '028nm' :
            LVSfile = '_ln28lpp.lvs.cal_'
            Techlib = 'cmos28lp'

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file

        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
        result1 = stdout.read().decode('utf-8')
        print('print after commandlines1 : ')
        print(result1)
        if (result1.split()[-6]) != "'0'":
            raise Exception("Library name already Existing or XStream ERROR!!")

        if DesignParameters._Technology == '028nm' :
            commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.LVSrunDir))
            result2 = stdout.read().decode('utf-8')

        print(f'print after commandlines2 :')
        print(result2)
        if (result2.split()[-6]) != "'0'":
            raise Exception("XstreamOut ERROR")

        ##### Step 2 : Modifying lvs.cal file

        commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{3}/{1}.sp\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '46s,.*,ERC RESULTS DATABASE \"{1}.erc.results\" ,' {2}; sed -i '47s,.*,ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER,' {2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir))
        print(f'print after commandlines3 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 3 : Delete previous lvs report file

        commandlines33 = f"cd {self.LVSrunDir}; rm {self.cellname}.lvs.report; rm {self.cellname}.erc.results; rm {self.cellname}.erc.summary"
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 4 : Running LVS..

        commandlines4 = "cd {0}; source setup.cshrc; cd {1}; calibre -spice {0}/{3}.sp -turbo -lvs -hier -nowait {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.LVSrunDir, LVSfile, self.cellname))
        
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 5 : Reading LVS report file..

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.lvs.report'.format(self.WorkDir, self.cellname))
        print(f"Reading '{self.WorkDir}/{self.cellname}.lvs.report' for check LVS Error......")
        if DesignParameters._Technology == '028nm' :
            lines = file.readlines()
            line = lines[30:31]
            print(line)
            if line[0][39] != 'C':
                raise Exception("LVS ERROR!!!")

            else:
                # commandlines5 = "cd {0}; rm -r {1}"
                # stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                print('No LVS ERROR for this case')
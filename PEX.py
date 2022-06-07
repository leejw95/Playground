import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

class PEX :
    def __init__(self, username, password, WorkDir, PEXrunDir, libname, cellname, GDSDir, Vir_Connect) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.PEXrunDir = PEXrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir
        self.Vir_Connect = Vir_Connect

    def PEXchecker(self) :
        if DesignParameters._Technology == '028nm' :
            PEXfile = '_calibre.run_'
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
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.PEXrunDir))
            result2 = stdout.read().decode('utf-8')

        print(f'print after commandlines2 :')
        print(result2)
        if (result2.split()[-6]) != "'0'":
            raise Exception("XstreamOut ERROR")

        ##### Step 2 : Modifying lvs.cal file , you should extract schematic once before this procedure!!!!

        if self.Vir_Connect == True :
            commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES RCNAMED ,' {2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
            print(f'print after commandlines3 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")
        
        else :
            commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '45s,.*,ERC RESULTS DATABASE \"{1}.erc.results\" ,' {2}; sed -i '46s,.*,ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER,' {2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
            print(f'print after commandlines3 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 3 : Delete previous lvs report / pex report file

        commandlines33 = f"cd {self.PEXrunDir}; rm {self.cellname}.lvs.report; rm {self.cellname}.lvs.report.ext; rm {self.cellname}.pex.netlist; rm {self.cellname}.pex.netlist.pex; rm {self.cellname}.pex.netlist.{self.cellname}.pxi; cd {self.WorkDir}; rm {self.cellname}.sp"
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 4 : Running LVS / PEX..

        commandlines4 = "cd {0}; source setup.cshrc; cd {1}; calibre -lvs -hier -spice {0}/{3}.sp -nowait -turbo {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        commandlines41 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -3d -rcc -turbo -nowait {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines41.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        commandlines42 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -3d -rcc -turbo -nowait {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines42.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        commandlines43 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -fmt -all -nowait {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines43.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 5 : Reading LVS report file..

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.lvs.report'.format(self.PEXrunDir, self.cellname))
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

        ##### Step 6 : Get pex netlist
        print('###### Gathering Parasitic Extracted Netlist from Server... ######')
        netlist = '{0}.pex.netlist'.format(self.cellname)
        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.PEXrunDir)
        fd = open("./" + netlist, 'wb')
        ftp.retrbinary("RETR " + netlist, fd.write)
        fd.close()

        f = open(netlist,'r')
        lines = f.readlines()
        subckt_list = []
        i = 0
        for index,line in enumerate(lines) : 
            if '.subckt' in line :
                subckt_list.append(line)
                i = index
            if (index == i + 1) and '+' in line :
                subckt_list.append(line)
                i = i + 1

        l = subckt_list[0].split()
        l.pop(0)
        ckt_name = l[0]
        l[0] = 'x'+ l[0]
        l = " ".join(l)
        subckt_list[0] = l

        ll = subckt_list[-1].split()
        ll.append(ckt_name)
        ll = " ".join(ll)
        subckt_list [-1] = ll

        lines = lines + subckt_list
        new_lines = "".join(lines)
        f.close() 

        with open(netlist,'w') as f :
            f.write(new_lines)
            f.close()

        print('###### Uploading Parasitic Extracted Netlist to Server... ######')
        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.PEXrunDir)
        fd = open("./" + netlist, 'rb')
        ftp.storbinary("STOR " + netlist, fd)
        fd.close()
        ftp.close()

        
import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

class POSIM :
    def __init__(self, username, password, WorkDir, OceanDir, OceanScript, cellname, GDSDir, Vir_Connect) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.OceanDir = OceanDir
        self.OceanScript = OceanScript
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir
        self.Vir_Connect = Vir_Connect

    def Posimchecker(self) :
        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file
        if DesignParameters._Technology == '028nm' :

            commandlines0 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {1};" # ocean file modification
            stdin, stdout, stderr = ssh.exec_command(commandlines0.format(self.OceanDir, self.OceanScript))
            result1 = stdout.read().decode('utf-8')

            commandlines1 = "cd {0}; source setup.cshrc; cd {1}; ocean -restore {2}'" # ocean script execution
            stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.OceanDir, self.OceanScript))
            result1 = stdout.read().decode('utf-8')

            commandlines2 = ""


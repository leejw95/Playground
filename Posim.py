import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

'''
    You should create schematic for post-layout simulation, and have a netlist on your server to run automatic posim.
'''

class POSIM :
    def __init__(self, username, password, WorkDir, OceanDir, OceanScript, SimDir, modelDir, Corner, PEXnetlist) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.OceanDir = OceanDir
        self.OceanScript = OceanScript
        self.SimDir = SimDir
        self.modelDir = modelDir
        self.Corner = Corner
        self.PEXnetlist = PEXnetlist

    def Posimchecker(self) :
        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file
        if DesignParameters._Technology == '028nm' :


            # _HomeDirectory = os.getcwd()
            # sch = open(_HomeDirectory + "/Netlist/{}".format(self.OceanScript), 'r')
            # lines = sch.readlines()
            # lst = []
            # new_lst = []
            # for line in lines :
            #     lst.append(line)
            # print (lst)

            # lst[1] = 'design( \"{0}/netlist/netlist\"'.format(self.SimDir)
            # lst[2] = 'resultsDir( \"{0}\" )'.format(self.SimDir)
            # lst[3] = 'path '


            commandlines0 = "cd {0}; sed -i '2s,.*,design(  \"{2}/netlist/netlist\"),' {1}; sed -i '3s,.*,resultsDir( \"{2}\" ),' {1}; sed -i '4s,.*,path(  \"{6}\"),' {1}; sed -i '9s,.*,    \"{5}\",' {1};" # ocean file modification
            stdin, stdout, stderr = ssh.exec_command(commandlines0.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            print(f'print after commandlines0 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines01 = "cd {0}; sed -i \"6s,.*,    \'(@{3}@ @{4}@),\" {1};"
            print (commandlines01.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            stdin, stdout, stderr = ssh.exec_command(commandlines01.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            print(f'print after commandlines01 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines02 = "cd {0}; sed -i \'s/@/\"/g\' {1};"
            print (commandlines02.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            stdin, stdout, stderr = ssh.exec_command(commandlines02.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            print(f'print after commandlines02 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")


            commandlines1 = "cd {0}; source setup.cshrc; cd {1}; ocean -nograph -restore {2}" # ocean script execution
            stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.OceanDir, self.OceanScript))
            result2 = stdout.read().decode('utf-8')

            commandlines2 = "cd {0}; cat SimulationResult.txt;"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.OceanDir))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

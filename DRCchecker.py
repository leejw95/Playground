import ftplib
import random
import paramiko
import sys
import os

'''
    This is Beta Version For auto DRC checker.
    Before you start, write your skill code at your directory.
    # File name of this skill code should be 'Skillcode.il'
    # copy and paste of this file at /mnt/sdc/junung/OPUS/Samsung28n . (Not Working for now)
    This now works only at server 141.223.22.156
    Write down every parameters as string, for example : '/mnt/sdc/username/...'
    DO NOT WRITE DOWN SLASH (/) AT THE END OF YOUR DIRECTORY!!!
    Make sure to write down Dir1 as your working directory of cadence virtuoso.
    Also do not use library name that already exists in your directory.
    
    Usage : Make an instance for this class, and use the function 'DRCchecker'

    2021-08-06 Junung
'''

class DRCchecker :
    def __init__ (self, username, password, WorkDir, DRCrunDir, libname, cellname) :
        self.server = '141.223.22.156'
        self.port = '22'
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.DRCrunDir = DRCrunDir
        self.libname = libname
        self.cellname = cellname
        

    def DRCchecker(self) :
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print ("############ Connecting to Server for DRC checking... ############")
        ssh.connect(self.server, port = self.port, username=self.username, password=self.password)


        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{0}/{2}.gds' -attachTechFileOfLib 'cmos28lp' -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname))
        result1 = ''.join(stdout.read())
        print (result1)
        if (result1.split()[-6]) != "'0'" :
            raise Exception ("Library name already Existing or XStream ERROR!!")


        commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
        stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.DRCrunDir))
        result2 = ''.join(stdout.read())
        print (result2)
        if (result2.split()[-6]) != "'0'" :
            raise Exception ("XstreamOut ERROR")

        commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' _cmos28lp.drc.cal_; sed -i '10s,.*,LAYOUT PRIMARY \"{1}\",' _cmos28lp.drc.cal_; sed -i '13s,.*,DRC RESULTS DATABASE \"{1}.drc.results\" ASCII,' _cmos28lp.drc.cal_; sed -i '18s,.*,DRC SUMMARY REPORT \"{1}.drc.summary\" REPLACE HIER,' _cmos28lp.drc.cal_"
        stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.DRCrunDir, self.cellname))
        print (''.join(stdout.read()))


        commandlines4 = "cd {0}; source setup.cshrc; calibre -drc -hier -nowait {1}/_cmos28lp.drc.cal_"
        stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.DRCrunDir))
        a = (''.join(stdout.read()))

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.drc.summary'.format(self.WorkDir, self.cellname))
        for line in (file.readlines() [-2:-1]) :
            print (line)
            if line.split()[4] != u'0' :
                raise Exception("DRC ERROR!!!")

            else :
                # commandlines5 = "cd {0}; sed -i '1s,.*,ddDeleteLocal(ddGetObj(\"{1}\" \"\" \"\" \"\")),' Skillcode.il"
                # stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                # print (''.join(stdout.read()))
                # commandlines6 = "cd {0}; source setup.cshrc; virtuoso -nograph -restore Skillcode.il"
                # stdin, stdout, stderr = ssh.exec_command(commandlines6.format(self.WorkDir))
                commandlines5 = "cd {0}; rm -r {1}"
                stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                print ('No DRC ERROR for this case, deleting library...')


        ssh.close


    def DRCchecker_PrintInputParams(self, InputParams):

        try:
            self.DRCchecker()
        except Exception as e:
            print('Error Occurred', e)
            print("=============================   Last Layout Object's Input Parameters are   =============================")
            for key, value in InputParams.items():
                print(key, ":", value)
            print("=========================================================================================================")
            raise Exception("Something ERROR with DRCchecker !!!")
        else:
            print("=============================   Last Layout Object's Input Parameters are   =============================")
            for key, value in InputParams.items():
                print(key, ":", value)
            print("=========================================================================================================")


    def Upload2FTP(self):
        """
        Upload GDS file to Working Directory
        """
        filename = self.cellname + '.gds'

        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.WorkDir)
        myFile = open(filename, 'rb')
        ftp.storbinary('STOR ' + filename, myFile)
        myFile.close()
        ftp.quit()


    def StreamIn(self, tech=None):
        """
        Only StreamIn

        :param tech:  '028nm' | '065nm'
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print ("############ Connecting to Server by SSH... ############")
        ssh.connect(hostname=self.server, port=self.port, username=self.username, password=self.password)

        ''' Not Implemented
        commandlines0 = 'cd {0}; source setup.cshrc; virtuoso -nograph;'
        stdin, stdout, stderr = ssh.exec_command(commandlines0.format(Dir_Work))
        result0 = ''.join(stdout.read())
        print('--------------result0-----------------')
        print (result0)

        ddDeleteObj(ddGetObj("{1}"))
        '''

        if tech in ('028nm', None):
            TechFile = 'cmos28lp'
        elif tech == '065nm':
            TechFile = 'tsmcN65'
        else:
            raise NotImplemented
        filename = self.cellname + '.gds'
        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{2}/{3}' -attachTechFileOfLib {4} -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.WorkDir, filename, TechFile))
        result1 = ''.join(stdout.read())
        print('--------------result1-----------------')
        print (result1)
        if (result1.split()[-6]) != "'0'":
            raise Exception("Library name already Existing or XStream ERROR!!")

        ssh.close


def RandomParam(start=None, stop=None, step=None):
    """
    ** (stop - start) should be a multiples of 'step' for uniform distribution

    :param start: <int>
    :param stop:  <int>
    :param step:  <int>
    :return:      <int> random integer number 'N' between 'start' and 'stop', ( start <= N <= stop )
    """
    assert isinstance(start, int)
    assert isinstance(stop, int)
    assert isinstance(step, int)
    assert (stop - start) % step == 0

    tmp = random.randint(start, stop + (step - 1))
    N = (tmp / step) * step

    return N

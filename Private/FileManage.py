import ftplib


def Upload2FTP(
        server=None,
        user=None,
        password=None,
        directory=None,
        filename=None
):
    """
    upload 'filename' to FTP 'server'
    """

    ftp = ftplib.FTP(server)
    ftp.login(user, password)
    ftp.cwd(directory)
    myfile = open(filename, 'rb')
    ftp.storbinary('STOR ' + filename, myfile)
    myfile.close()
    ftp.quit()


def StreamIn(
    server=None,
    port=22,
    ID=None,
    PW=None,
    Dir_Work=None,
    Dir_GDS=None,
    libname=None,
    filename=None,
    tech=None
):
    """
    Connect to server by SSH &
    Stream-in GDS file
    """
    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print ("############ Connecting to Server by SSH... ############")
    ssh.connect(server, port=port, username=ID, password=PW)

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

    commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{2}/{3}' -attachTechFileOfLib {4} -logFile 'strmIn.log'"
    stdin, stdout, stderr = ssh.exec_command(commandlines1.format(Dir_Work, libname, Dir_GDS, filename, TechFile))
    result1 = ''.join(stdout.read())
    print('--------------result1-----------------')
    print (result1)
    if (result1.split()[-6]) != "'0'":
        raise Exception("Library name already Existing or XStream ERROR!!")

    ssh.close




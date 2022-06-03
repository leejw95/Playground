import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

class PEX :
    def __init__(self, username, password, WorkDir, PEXrunDir, libname, cellname, GDSDir, Vir_connect) :
        

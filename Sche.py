import re
import sys
import os
import DesignParameters


class Schematic () :
    def __init__ (self, parameter, arch):
        self.parameter = parameter
        self.arch = arch

    def SchematicGenerator (self) :
        _HomeDirectory = os.getcwd()
        sch = open(_HomeDirectory + "/D_FF_test/{}.src.net".format(self.arch), 'r')
        lines = sch.readlines()
        for line in lines : 
            print (line)
        sch.close()


import re
import sys
import os
import ftplib
import DesignParameters

'''
    Schematic Generator for D_Latch, FF in SS28nm
'''

class Schematic () :
    def __init__ (self, parameter, arch, subckt_list):
        self.parameter = parameter
        self.arch = arch
        self.subckt = subckt_list

    def SchematicGenerator (self) :
        _HomeDirectory = os.getcwd()
        sch = open(_HomeDirectory + "/D_FF_test/{}.src.net".format(self.arch), 'r')
        lines = sch.readlines()
        lst = []
        new_string_list = []
        for index,line in enumerate(lines) :
            new_string_list.append(line)
            for i in range(0, len(self.subckt)) :
                    if '.SUBCKT {}'.format(self.subckt[i]) in line :
                        # print (line)
                        lst.append(index)
            if '.ENDS' in line :
                lst.append(index)
        
        # print (new_string_list)
        print (new_string_list[5])
        
        lst.pop(-1)
        print (lst)
        ind = len(lst) // 2
        for i in range (0, ind) :
            for line in lines[lst[2*i] : lst[2*i + 1]] :
                    if 'MP' in line :
                        mp = line.split(' ')
                        mp[6] = 'w={}u'.format(float(self.parameter['{}ChannelWidth'.format(i+1)] * self.parameter['{}NPRatio'.format(i+1)] * self.parameter['{}Finger'.format(i+1)]) / 1000)
                        mp[7] = 'l={}u'.format(float(self.parameter['{}ChannelLength'.format(i+1)]) / 1000)
                        mp[8] = 'nf={}'.format(float(self.parameter['{}Finger'.format(i+1)]))
                        print (mp)
                        new_string_list[lst[2*i] + 1] = " ".join(mp)
                    if 'MN' in line :
                        mn = line.split(' ')
                        mn[6] = 'w={}u'.format(float(self.parameter['{}ChannelWidth'.format(i+1)] * self.parameter['{}Finger'.format(i+1)]) / 1000)
                        mn[7] = 'l={}u'.format(float(self.parameter['{}ChannelLength'.format(i+1)]) / 1000)
                        mn[8] = 'nf={}'.format(float(self.parameter['{}Finger'.format(i+1)]))
                        print (mn)
                        new_string_list[lst[2*i] + 3] = " ".join(mn)
        # print (new_string_list)
        new_string = "".join(new_string_list)
        print (new_string)

        with open(_HomeDirectory + "/D_FF_test/b.src.net", 'w') as f :
            f.write(new_string)
            f.close()
        sch.close()
        
        # print (self.parameter)


import re
import sys
import os
import ftplib

from pandas import array

'''
    Schematic Generator for D_Latch, FF, Shift Register in SS28nm
'''

class Schematic () :
    def __init__ (self, parameter, arch, subckt_list):
        self.parameter = parameter
        self.arch = arch
        self.subckt = subckt_list

    def SchematicGenerator (self) :  ### change Device SIZE
        _HomeDirectory = os.getcwd()
        sch = open(_HomeDirectory + "/Netlist/{}.src.net".format(self.arch), 'r')
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
        # print (new_string_list[5])

        if len(lst) % 2 != 0 :
            lst.pop(-1)
        print (lst)
        ind = len(lst) // 2
        for i in range (0, ind) :
            for line in lines[lst[2*i] : lst[2*i + 1]] :
                    if 'MP' in line or 'Mxp' in line :
                        mp = line.split(' ')
                        mp[6] = 'w={}u'.format(float(self.parameter['{}ChannelWidth'.format(i+1)] * self.parameter['{}NPRatio'.format(i+1)] * self.parameter['{}Finger'.format(i+1)]) / 1000)
                        mp[7] = 'l={}u'.format(float(self.parameter['{}ChannelLength'.format(i+1)]) / 1000)
                        mp[8] = 'nf={}'.format(float(self.parameter['{}Finger'.format(i+1)]))
                        print (mp)
                        new_string_list[lst[2*i] + 1] = " ".join(mp)
                    if 'MN' in line or 'Mxn' in line :
                        mn = line.split(' ')
                        mn[6] = 'w={}u'.format(float(self.parameter['{}ChannelWidth'.format(i+1)] * self.parameter['{}Finger'.format(i+1)]) / 1000)
                        mn[7] = 'l={}u'.format(float(self.parameter['{}ChannelLength'.format(i+1)]) / 1000)
                        mn[8] = 'nf={}'.format(float(self.parameter['{}Finger'.format(i+1)]))
                        print (mn)
                        new_string_list[lst[2*i] + 3] = " ".join(mn)
        # print (new_string_list)
        new_string = "".join(new_string_list)
        # print (new_string)

        with open(_HomeDirectory + "/Netlist/{}.src.net".format(self.arch), 'w') as f :
            f.write(new_string)
            f.close()
        sch.close()
        
        # print (self.parameter)

    def ArrayGenerator (self, topcell, subcell, num_array) :  #### Change Connection of array
        _HomeDirectory = os.getcwd()
        sch = open(_HomeDirectory + "/Netlist/{}.src.net".format(self.arch), 'r')
        lines = sch.readlines()
        lst = []
        new_string_list = []
        array_list = []

        for index,line in enumerate(lines) :
            new_string_list.append(line)
            if '.SUBCKT {}'.format(topcell) in line :
                # print (line)
                lst.append(index)
            if '.ENDS' in line :
                if lst :
                    lst.append(index)

        # print (new_string_list)
        # print (lst)
        array_list = new_string_list[lst[0] : lst[1] + 1]
        # print (new_string_list[lst[0] : lst[1]])
        for i in range (lst[1], lst[0] - 1, -1) :
            # print (i)
            new_string_list.pop(i)
        print (new_string_list)
        print (array_list)

        new_topcell = ['.SUBCKT {} VDD VSS CLK CLKb D '.format(topcell)]
        pin_list = []
        for i in range (0, num_array) :
            pin_list.append('Q<{}>'.format(i))
            pin_list.append('Qb<{}>'.format(i))
        
        print (' '.join(str(i) for i in pin_list))
        new_topcell[0] = new_topcell[0] + ' '.join(str(i) for i in pin_list) + ' \n'
        # print (new_topcell)

        for i in range (num_array, 1, -1) :
            new_topcell.append('XI{0} CLK CLKb {1} {2} {3} VDD VSS / {4}\n'.format(i, pin_list[((i-2) * 2)], pin_list[(i - 1) * 2], pin_list[(i - 1) * 2 + 1], subcell))
        
        new_topcell.append('XI1 CLK CLKb D {0} {1} VDD VSS / {2}\n'.format(pin_list[0], pin_list[1], subcell))
        new_topcell.append('.ENDS\n')
        # print (new_topcell)
        new_string_list = new_string_list + new_topcell
        # print(new_string_list)
        new_string = "".join(new_string_list)

        with open(_HomeDirectory + "/Netlist/{}.src.net".format(self.arch), 'w') as f :
            f.write(new_string)
            f.close()
        sch.close()

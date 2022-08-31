from cProfile import label
from cmath import log
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy

# some useful constants

AVAGADRO_NUM = 6.023E23
CM_TO_BARN = 1.0E-24 # converts cm^2 to barns
SAMPLING_RATE = 100.0 # Hz
ELEMENTARY_CHARGE = 1.60E-19 # in C
D_OMEGA_= 0.00463 # slit settings in steradians
Z = 1 # Number of protons in beam 

MOLAR_MASS_49TI = 4.89E7 #ug/mol
TARGET_49TI = 413 # in micrograms/cm^2

MOLAR_MASS_47TI = 4.70E7 #ug/mol
TARGET_47TI = 441 # in micrograms/cm^2


def BCI_info_handler():
    BCI_hits_47Ti = []
    BCI_scale_47Ti = []

    BCI_hits_49Ti = []
    BCI_scale_49Ti = []
    with open("BCI_info_47Ti.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            hits, scale = line.split()
            BCI_hits_47Ti.append(float(hits))
            BCI_scale_47Ti.append(float(scale))
    
    with open("BCI_info_49Ti.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            hits, scale = line.split()
            BCI_hits_49Ti.append(float(hits))
            BCI_scale_49Ti.append(float(scale))
    
    return BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti

def volume_file_reader(dir, file):
    vol = []
    with open(dir + '/' + file) as f:
            stripped = [s.strip() for s in f]
            for line in stripped:
                vol.append(float(line))
    return vol


def cross_section_47Ti(BCI_hits_47Ti, BCI_scale_47Ti, volume_list): #func used to convert mass in ug/cm --> 1/barn
    rho_t_47Ti = (TARGET_47TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_47TI)

    j=0
    cross_section_vals = []
    for i in BCI_hits_47Ti:
        Q_beam = (i * 1E-9 * BCI_scale_47Ti[j])/(SAMPLING_RATE)
        N_beam = Q_beam / ELEMENTARY_CHARGE
        dsigma_domega = (volume_list[j] * 1000)/(N_beam * rho_t_47Ti * D_OMEGA_)  # cross-sec in mb/sr
        cross_section_vals.append(dsigma_domega)
        j +=1
    return cross_section_vals


def cross_section_49Ti(BCI_hits_49Ti, BCI_scale_49Ti, volume_list):
    rho_t_49Ti = (TARGET_49TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_49TI)

    j=0
    cross_section_vals = []
    for i in BCI_hits_49Ti:
        Q_beam = (i * 1E-9 * BCI_scale_49Ti[j])/(SAMPLING_RATE)
        N_beam = Q_beam / ELEMENTARY_CHARGE
        dsigma_domega = (volume_list[j] * 1000)/(N_beam * rho_t_49Ti * D_OMEGA_)  # cross-sec in mb/sr
        cross_section_vals.append(dsigma_domega)
        j +=1
    return cross_section_vals


def plot_cross_section(lab_angles, x_sec, energy_beforesplit):
    name_list = energy_beforesplit.split('_')
    energy = ' '.join(name_list)
    print(energy)
    plt.scatter(lab_angles, x_sec, label=energy + ' data')
    plt.yscale("log")

    miny=0.01
    maxy=1
    for val in x_sec:
        if val < miny:
            miny = 0.001
        if val > maxy:
            maxy = 10
    plt.ylim(miny, maxy)

    plt.minorticks_on()

    plt.legend(loc='upper right')
    plt.ylabel(r'Cross-Section [$\frac{mb}{sr}$]')
    plt.xlabel(r'Lab Angle [$\Theta_{lab}$]')
    plt.show()
    


def main():
    lab_angles = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti = BCI_info_handler()
    dir = os.getcwd()
    dir_47Ti = dir + '/47Ti_peaks'
    dir_49Ti = dir + '/49Ti_peaks'
    for file in os.listdir(dir_47Ti):
        '''
        To find # of subplots, just use len(files in folder)
        Can get fancy and use modulo % operator to chuck into grids, max prolly 4x4, in energy order
        The subplots can be spawned using subplots(i,i)
        '''
        vol_list = volume_file_reader(dir_47Ti, file)
        energy = file.split('.')[0]
        x_sec = cross_section_47Ti(BCI_hits_47Ti, BCI_scale_47Ti, vol_list)
        plot_cross_section(lab_angles, x_sec, energy)


    for file in os.listdir(dir_49Ti):
        vol_list = volume_file_reader(dir_49Ti, file)
        energy = file.split('.')[0]
        x_sec = cross_section_47Ti(BCI_hits_49Ti, BCI_scale_49Ti, vol_list)
        plot_cross_section(lab_angles, x_sec, energy)




if __name__ == "__main__":
    main()
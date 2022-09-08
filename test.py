import os
import numpy as np
import time
import matplotlib.pyplot as plt
import math


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
    volume_list = []
    err_list = []
    with open(dir + '/' + file) as f:
            stripped = [s.strip() for s in f]
            for line in stripped:
                if line == '':
                    volume_list.append(0.0)
                    err_list.append(0.0)
                else:
                    vol, err = line.split()
                    volume_list.append(float(vol))
                    err_list.append(float(err))
    return vol, err_list

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


def plotting(dir_47Ti, lab_angles, BCI_scale_47Ti, BCI_hits_47Ti, num_files):
    #plot info stuff
    figure_size = (15,15)

    if (num_files <= 12):
        colz=3
        row = math.ceil(num_files/3)
        fig, ax = plt.subplots(row, colz, squeeze=False, figsize=figure_size)
        fig.supxlabel(r'Lab Angle [$\Theta_{lab}$]')
        fig.supylabel(r'Cross-Section [$\frac{mb}{sr}$]')
    elif (num_files <=16 ):
        row=4
        colz =math.ceil(num_files/4)
        fig, ax = plt.subplots(colz, row, squeeze=False, figsize=figure_size)
        fig.supxlabel(r'Lab Angle [$\Theta_{lab}$]')
        fig.supylabel(r'Cross-Section [$\frac{mb}{sr}$]')
    else:
        # create 2 diff subplots, to be implemented later
        pass

    curr_row = 0
    curr_col = 0
    sorted_files = sorted(os.listdir(dir_47Ti))
    for file in sorted_files:
        miny=0.01
        maxy=1
        vol_list, err_list = volume_file_reader(dir_47Ti, file)
        fname = file.split('.')[0]
        fname_list = fname.split('_')
        plot_name = ' '.join(fname_list)
        cross_sec = cross_section_47Ti(BCI_hits_47Ti, BCI_scale_47Ti, vol_list)
        if (curr_row<row and curr_col<colz):
            ax[curr_row][curr_col].scatter(lab_angles, cross_sec, label=plot_name)
            ax[curr_row][curr_col].legend()
            ax[curr_row][curr_col].set_yscale("log")

            for val in cross_sec:
                if val < miny:
                    miny = 0.001
                if val > maxy:
                    maxy = 10

            ax[curr_row][curr_col].set_ylim(miny, maxy)
            curr_col+=1
        elif(curr_col == colz):
            curr_row+=1
            curr_col = 0
            ax[curr_row][curr_col].scatter(lab_angles, cross_sec, label=plot_name)
            ax[curr_row][curr_col].legend()
            ax[curr_row][curr_col].set_yscale("log")

            for val in cross_sec:
                if val < miny:
                    miny = 0.001
                if val > maxy:
                    maxy = 10
       
            ax[curr_row][curr_col].set_ylim(miny, maxy)
            curr_col+=1
    plt.show()


def main():

    lab_angles = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti = BCI_info_handler()

    dir = os.getcwd()
    dir_47Ti = dir + '/47Ti_peaks'
    num_files = len(os.listdir(dir_47Ti))
    plotting(dir_47Ti, lab_angles, BCI_scale_47Ti, BCI_hits_47Ti, num_files)
   


'''
Turn this sec into plotting section separately
Do not need two separate cross-section functions, just pass correct BCI scale, hits, and vol for the
peak and then also just pass sometihng that denotes whether it is 47/49Ti, then
use if statement when calculating molar mass, etc.
'''



if __name__ == "__main__":
    main()
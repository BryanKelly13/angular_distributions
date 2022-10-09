import csv
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

dir = os.getcwd()

def BCI_info_handler():
    BCI_hits_48Ti = []
    BCI_scale_48Ti = []

    BCI_hits_50Ti = []
    BCI_scale_50Ti = []
    with open("BCI_info_48Ti.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            hits, scale = line.split()
            BCI_hits_48Ti.append(float(hits))
            BCI_scale_48Ti.append(float(scale))
   
    with open("BCI_info_50Ti.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            hits, scale = line.split()
            BCI_hits_50Ti.append(float(hits))
            BCI_scale_50Ti.append(float(scale))
    return BCI_hits_48Ti, BCI_scale_48Ti, BCI_hits_50Ti, BCI_scale_50Ti


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
    return volume_list, err_list

def cross_section_calculation(BCI_hits, BCI_scale, volume_list, isotope): #func used to convert mass in ug/cm --> 1/barn
    rho_t_47Ti = (TARGET_47TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_47TI)
    rho_t_49Ti = (TARGET_49TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_49TI)

    j=0
    cross_section_vals = []
    for i in BCI_hits:
        Q_beam = (i * 1E-9 * BCI_scale[j])/(SAMPLING_RATE)
        N_beam = Q_beam / ELEMENTARY_CHARGE
        if isotope == 48:
            dsigma_domega = (volume_list[j] * 1000)/(N_beam * rho_t_47Ti * D_OMEGA_)  # cross-sec in mb/sr
        elif isotope == 50:
            dsigma_domega = (volume_list[j] * 1000)/(N_beam * rho_t_49Ti * D_OMEGA_)  # cross-sec in mb/sr
        cross_section_vals.append(dsigma_domega)
        j +=1
    return cross_section_vals

def error_handler(x_sec, vol_list, vol_err_list, BCI_hits):
    '''
    Returns a list of errors that correspond to the list of cross-sections generated for a
    given peak
    '''
    index = 0
    errs = []
    for _ in vol_list:
        err_BCI = 0.20 * BCI_hits[index]
        if vol_list[index] == 0.0:
            deltaX = 0.0
        else:
            deltaX = np.sqrt( (vol_err_list[index]/vol_list[index])**2 + (err_BCI/BCI_hits[index])**2 ) * x_sec[index]
        errs.append(deltaX)
        index +=1
    return errs

def file_writer(energy, lab_angles, cross_sec, finalError, isotope):
    path = dir + '/output_peak_files'
    file = str(isotope) + "Ti_" + energy + "_keV.txt"
    storefile = os.path.join(path, file)
    with open(storefile, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(lab_angles, cross_sec, finalError))

    print("Successfully wrote " + file + " to the output_peak_files folder")


def plotting(dir, lab_angles, BCI_scale, BCI_hits, num_files, isotope, output_vals):
    #plot info stuff
    figure_size = (15,15)

    if (num_files <= 12):
        colz=3
        row = math.ceil(num_files/3)
        fig, ax = plt.subplots(row, colz, squeeze=False, figsize=figure_size, constrained_layout=True)
        fig.supxlabel(r'Lab Angle [$\Theta_{lab}$]')
        fig.supylabel(r'Cross-Section [$\frac{mb}{sr}$]')
        if isotope == 48:
            fig.suptitle(r'$^{48}$Ti Excited States')
        else:
            fig.suptitle(r'$^{50}$Ti Excited States')
    else:
        # creates however many 4x4 plots are needed to fulfill all distributions
        row=4
        colz=4
        sorted_files = sorted(os.listdir(dir))
        file_sets = [sorted_files[x:x+16] for x in range(0, len(sorted_files), 16)]
        i = 0
        for _ in file_sets:
            curr_row = 0
            curr_col = 0
            fig, ax = plt.subplots(colz, row, squeeze=False, figsize=figure_size, constrained_layout=True)
            fig.supxlabel(r'Lab Angle [$\Theta_{lab}$]')
            fig.supylabel(r'Cross-Section [$\frac{mb}{sr}$]')
            if isotope == 48:
                fig.suptitle(r'$^{48}$Ti Excited States')
            else:
                fig.suptitle(r'$^{50}$Ti Excited States')

            for file in file_sets[i]:
                miny=0.01
                maxy=1
                vol_list, vol_err_list = volume_file_reader(dir, file)
                fname = file.split('.')[0]
                fname_list = fname.split('_')
                plot_name = ' '.join(fname_list)
                cross_sec = cross_section_calculation(BCI_hits, BCI_scale, vol_list, isotope)
                finalError = error_handler(cross_sec, vol_list, vol_err_list, BCI_hits)

                if int(fname_list[0]) in output_vals:
                    file_writer(fname_list[0], lab_angles, cross_sec, finalError, isotope)
                    
                if (curr_row<row and curr_col<colz):
                    ax[curr_row][curr_col].errorbar(lab_angles, cross_sec, finalError, label=plot_name, color='black', fmt='x', ecolor='red', capsize=2.0)
                    ax[curr_row][curr_col].minorticks_on()
                    ax[curr_row][curr_col].legend()
                    ax[curr_row][curr_col].set_yscale("log")
                    ax[curr_row][curr_col].set_title(plot_name)

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
                    ax[curr_row][curr_col].errorbar(lab_angles, cross_sec, finalError, label=plot_name, color='black', fmt='x', ecolor='red', capsize=2.0)
                    ax[curr_row][curr_col].minorticks_on()
                    ax[curr_row][curr_col].legend()
                    ax[curr_row][curr_col].set_yscale("log")
                    ax[curr_row][curr_col].set_title(plot_name)

                    for val in cross_sec:
                        if val < miny:
                            miny = 0.001
                        if val > maxy:
                            maxy = 10
           
                    ax[curr_row][curr_col].set_ylim(miny, maxy)
                    curr_col+=1
            plt.show()
            i+=1
        return
   
    # Hits here after if statement is true, plots the < 12 file case
    curr_row = 0
    curr_col = 0
    sorted_files = sorted(os.listdir(dir))
    for file in sorted_files:
        miny=0.01
        maxy=1
        vol_list, vol_err_list = volume_file_reader(dir, file)
        fname = file.split('.')[0]
        fname_list = fname.split('_')
        plot_name = ' '.join(fname_list)
        cross_sec = cross_section_calculation(BCI_hits, BCI_scale, vol_list, isotope)
        finalError = error_handler(cross_sec, vol_list, vol_err_list, BCI_hits)
        if fname_list[0] in output_vals:
            file_writer(fname_list[0], lab_angles, cross_sec, finalError, isotope)

        if (curr_row<row and curr_col<colz):
            ax[curr_row][curr_col].errorbar(lab_angles, cross_sec, finalError, label=plot_name, color='black', fmt='x', ecolor='red', capsize=2.0)
            ax[curr_row][curr_col].minorticks_on()
            ax[curr_row][curr_col].legend()
            ax[curr_row][curr_col].set_yscale("log")
            ax[curr_row][curr_col].set_title(plot_name)

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
            ax[curr_row][curr_col].errorbar(lab_angles, cross_sec, finalError, label=plot_name, color='black', fmt='x', ecolor='red', capsize=2.0)
            ax[curr_row][curr_col].minorticks_on()
            ax[curr_row][curr_col].legend()
            ax[curr_row][curr_col].set_yscale("log")
            ax[curr_row][curr_col].set_title(plot_name)

            for val in cross_sec:
                if val < miny:
                    miny = 0.001
                if val > maxy:
                    maxy = 10
       
            ax[curr_row][curr_col].set_ylim(miny, maxy)
            curr_col+=1
    plt.show()


def peak_input(isotope):
    output_vals = []
    print("Enter desired peaks you want outputted to data files for " +str(isotope) + "Ti")
    print("When done, enter -1")
    while True:
        peak = int(input("Peak [kev]: "))
        if peak == -1:
            break
        else:
            output_vals.append(peak)
    return output_vals


def main():

    lab_angles = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    BCI_hits_48Ti, BCI_scale_48Ti, BCI_hits_50Ti, BCI_scale_50Ti = BCI_info_handler()

    # 47Ti Plots & Calculations
    dir_48Ti = dir + '/48Ti_peaks'
    num_files = len(os.listdir(dir_48Ti))
    isotope_48Ti = 48
    output_vals_48Ti = peak_input(isotope_48Ti)
    plotting(dir_48Ti, lab_angles, BCI_scale_48Ti, BCI_hits_48Ti, num_files, isotope_48Ti, output_vals_48Ti)

    # 49Ti Plots & Calculations
    dir_50Ti = dir + '/50Ti_peaks'
    num_files = len(os.listdir(dir_50Ti))
    isotope_50Ti = 50
    output_vals_50Ti = peak_input(isotope_50Ti)
    plotting(dir_50Ti, lab_angles, BCI_scale_50Ti, BCI_hits_50Ti, num_files, isotope_50Ti, output_vals_50Ti)


if __name__ == "__main__":
    main()

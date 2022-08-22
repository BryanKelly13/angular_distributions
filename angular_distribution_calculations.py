from asyncore import read
from cmath import log
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

MOLAR_MASS_47TI = 4.70E7 #um/mol
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
    print(cross_section_vals)
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
    print(cross_section_vals)
    return cross_section_vals


def plot_cross_section(lab_angles, x_sec_1553):
    plt.scatter(lab_angles, x_sec_1553)
    plt.yscale("log")
    plt.ylim(0.01, 1)

    plt.minorticks_on()

    plt.ylabel(r'Cross-Section [$\frac{mb}{sr}$]')
    plt.xlabel(r'Lab Angle [$\Theta_{lab}$]')
    plt.show()
    


def main():
    lab_angles = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti = BCI_info_handler()

    #47Ti Peak Information and Cross Sections

    vol_2295keV = [43, 77.7457332306963, 227.89418754265, 344.842876437932, 163.076816088494, 119.233963306215, 171.680097630926, 
                    135.28742772684, 117.68680311569, 129.088164844895]

    x_sec_2295 = cross_section_47Ti(BCI_hits_47Ti, BCI_scale_47Ti, vol_2295keV)
    plot_cross_section(lab_angles, x_sec_2295)
    
    
    #49Ti Peak Information and Cross Sections

    vol_1553keV = [146.274290367033, 194.947937595412, 250.160644164713, 278.050425620509, 126.308096060263, 142.11518507284,
                    244.639070350995, 126.437222617944, 178.22420628184, 128.973437231083]
    cross_sec_1553 = cross_section_49Ti(BCI_hits_49Ti, BCI_scale_49Ti, vol_1553keV)



    plot_cross_section(lab_angles, cross_sec_1553)




if __name__ == "__main__":
    main()
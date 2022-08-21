from asyncore import read
import matplotlib
import matplotlib.pyplot as plt
import numpy

# some useful constants

AVAGADRO_NUM = 6.023E23
CM_TO_BARN = 1.0E-24 # converts cm^2 to barns
SAMPLING_RATE = 100 # Hz
ELEMENTARY_CHARGE = 1.60E-10 # in nC
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
            BCI_hits_47Ti.append(hits)
            BCI_scale_47Ti.append(scale)
    
    with open("BCI_info_49Ti.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            hits, scale = line.split()
            BCI_hits_49Ti.append(hits)
            BCI_scale_49Ti.append(scale)
    
    return BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti


def cross_section(BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti): #func used to convert mass in ug/cm --> 1/barn
    rho_t_47Ti = (TARGET_47TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_47TI)
    rho_t_49Ti = (TARGET_49TI * CM_TO_BARN * AVAGADRO_NUM)/(MOLAR_MASS_49TI)

    for i in BCI_hits_47Ti:
        pass







def main():
    BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti = BCI_info_handler()
    cross_section(BCI_hits_47Ti, BCI_scale_47Ti, BCI_hits_49Ti, BCI_scale_49Ti)


if __name__ == "__main__":
    main()
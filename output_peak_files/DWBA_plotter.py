import os
from turtle import color
import numpy as np
import time
import matplotlib.pyplot as plt
import math

dir = os.getcwd()
os.chdir(dir + "/output_peak_files/")

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("48Ti_2295_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))
# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)

# angle = []
# f72_x_sec = []
# f_scale = 0.09
# with open("48Ti_f72_4+_2295keV_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             f72_x_sec.append(float(f_scale*val))
# plt.plot(angle, f72_x_sec, label=r"$1f_{\frac{7}{2}}$")

# plt.yscale("log")
# plt.ylim(0.01, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=True, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{48}Ti$ 2.295 MeV Excited State")

# plt.show()





# # ####### Mixed 3224 keV State  GOOD MIX ONE

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("48Ti_3223_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)

# #l=1 wave below
# angle = []
# p32_x_sec = []
# p_scale = 0.05
# with open("48Ti_p32_3+_3223keV_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             p32_x_sec.append(float(p_scale*val))
# plt.plot(angle, p32_x_sec, label=r"$2p_{3/2}$")

# # l=3 wave below
# angle = []
# f72_x_sec = []
# f_scale = 0.05
# with open("48Ti_f72_4+_2295keV_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             f72_x_sec.append(float(f_scale*val))
# plt.plot(angle, f72_x_sec, label=r"$1f_{7/2}$", color='red')

# # combining l=1+3 contributions
# mixed_list = np.add(p32_x_sec, f72_x_sec)
# plt.plot(angle, mixed_list, label=r"$1f_{7/2}$ + $2p_{3/2}$", color='#782f40')



# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{48}Ti$ 3.223 MeV Excited State")
# plt.show()



# # ####### 3508 state below
# data_angle = []
# data_x_sec = []
# data_err = []
# with open("48Ti_3508_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)

# angle = []
# d52_x_sec = []
# f_scale = 0.4

# with open("48Ti_f72_6+_3508keV_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(f_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$1f_{\frac{7}{2}}$")

# plt.yscale("log")
# plt.ylim(0.01, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=False, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{48}Ti$ 3.508 MeV Excited State")

# plt.show()






# # ### 50 Ti States below

# # ##################### 4172 state below     GOOD ONE

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_4172_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)

# angle = []
# d52_x_sec = []
# d_scale = 0.54

# with open("50Ti_p32_3+_4172_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2p_{3/2}$", color='#782f40')

# plt.yscale("log")
# plt.ylim(0.1, 10.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 4.172 MeV Excited State")

# plt.show()

# # #####  5334 keV state

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_5334_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.04

# with open("50Ti_d52_4-_5334_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2d_{\frac{5}{2}}$")

# #1- DWBA
# new_angle = []
# d_x_sec = []
# scale = 0.04
# with open("50Ti_d52_1-_5334_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             new_angle.append(float(lab_angle))
#             val = float(value)
#             d_x_sec.append(float(scale*val))
# plt.plot(new_angle, d_x_sec, label=r"$ 1^- 2d_{\frac{5}{2}}$")

# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=False, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 5.334 MeV Excited State")

# plt.show()



# # ##### 5379 state
# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_5379_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.1

# with open("50Ti_p32_4+_5379_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2d_{\frac{5}{2}}$")


# plt.yscale("log")
# plt.ylim(0.01, 10.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=False, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 5.379 MeV Excited State")

# plt.show()


# # # 5600 state
# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_5600_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.02

# with open("50Ti_d52_1-_5600_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2d_{\frac{5}{2}}$")


# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=False, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 5.600 MeV Excited State")

# plt.show()

# # # 5837 state
# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_5837_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.03

# with open("50Ti_d52_1-_5837_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2d_{\frac{5}{2}}$")


# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 5.837 MeV Excited State")

# plt.show()


# #  6636 state

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("50Ti_6636_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.03

# with open("50Ti_d52_1-_6636_02.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$2d_{\frac{5}{2}}$")


# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{50}Ti$ 6.636 MeV Excited State")

# plt.show()



### Mark's Re-do DWBA Calculations
## 2295 state

# data_angle = []
# data_x_sec = []
# data_err = []
# with open("48Ti_2295_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


# angle = []
# d52_x_sec = []
# d_scale = 0.018

# with open("48Ti_f72_4+_2295keV_02_newOP.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             d52_x_sec.append(float(d_scale*val))
# plt.plot(angle, d52_x_sec, label=r"$1f_{7/2}$")


# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{48}Ti$ 2.295 MeV Excited State")

# plt.show()

### 3223 keV state
# data_angle = []
# data_x_sec = []
# data_err = []
# with open("48Ti_3223_keV.txt") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value, err = line.split()
#             data_angle.append(float(lab_angle))
#             data_x_sec.append(float(value))
#             data_err.append(float(err))

# plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)

# #l=1 wave
# angle = []
# p32_x_sec = []
# p_scale = 0.011
# with open("48Ti_p32_3+_3223keV_02_newOP.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             p32_x_sec.append(float(p_scale*val))
# plt.plot(angle, p32_x_sec, label=r"$2p_{3/2}$")

# #l=3 wave
# angle = []
# f72_x_sec = []
# f_scale = 0.011
# with open("48Ti_f72_3+_3223keV_02_newOP.sorted") as f:
#         stripped = [s.strip() for s in f]
#         for line in stripped:
#             lab_angle, value = line.split()
#             angle.append(float(lab_angle))
#             val = float(value)
#             f72_x_sec.append(float(f_scale*val))
# plt.plot(angle, f72_x_sec, label=r"$1f_{7/2}$")

# # # combining l=1+3 contributions
# mixed_list = np.add(p32_x_sec, f72_x_sec)
# plt.plot(angle, mixed_list, label=r"$1f_{7/2}$ + $2p_{3/2}$", color='#782f40')


# plt.yscale("log")
# plt.ylim(0.001, 1.0)
# plt.legend()
# plt.minorticks_on()
# plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
# plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

# plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
# plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
# plt.title(r"$^{48}Ti$ 2.295 MeV Excited State")

# plt.show()


data_angle = []
data_x_sec = []
data_err = []
with open("48Ti_3508_keV.txt") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            lab_angle, value, err = line.split()
            data_angle.append(float(lab_angle))
            data_x_sec.append(float(value))
            data_err.append(float(err))

plt.errorbar(data_angle, data_x_sec, data_err, color='black', fmt='x', ecolor='red', capsize=2.0)


angle = []
d52_x_sec = []
d_scale = 0.058

with open("48Ti_f72_6+_3508keV_02_newOP.sorted") as f:
        stripped = [s.strip() for s in f]
        for line in stripped:
            lab_angle, value = line.split()
            angle.append(float(lab_angle))
            val = float(value)
            d52_x_sec.append(float(d_scale*val))
plt.plot(angle, d52_x_sec, label=r"$1f_{7/2}$")


plt.yscale("log")
plt.ylim(0.001, 1.0)
plt.legend()
plt.minorticks_on()
plt.tick_params(axis='both', which='major', direction='in',labelbottom=True, top=True, right=True, length = 5)
plt.tick_params(axis='both', which='minor', direction='in',labelbottom=False, top=True, right=True, length = 3)

plt.xlabel(r"Lab Angle [$\Theta_{lab}$]")
plt.ylabel(r"Cross-Section [$\frac{mb}{sr}}$]")
plt.title(r"$^{48}Ti$ 2.295 MeV Excited State")

plt.show()
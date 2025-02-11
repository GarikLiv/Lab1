import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

def transCurrent(vBe,vT,iSat):
    return iSat*(np.exp(vBe/vT)-1)

k = 1.380649E-23
e = 1.60217663E-19

Vp23_4 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47]
Vp23_6 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47]
Vp24_4 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp25_5 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp27_0 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp28_7 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp29_1 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp32_5 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp34_1 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp35_1 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp39_6 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
Vp42_2 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
#Vp43_4 = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.44, 0.445, 0.45, 0.455, 0.46, 0.465, 0.47, 0.475, 0.48, 0.485, 0.49, 0.495]
A23_4 = [-238.396, -140.028, -52.1882, 45.5214, 217.911, 380.76, 606.446, 866.347, 1195.99, 1591.44, 2056.96, 2598.47, 3249.21, 4114.45, 5036.27, 6273.6, 7730.36, 9407.87, 11482.1, 14002.5, 17001.6, 20469.1, 24617.7, 29580.4, 35374.6, 42602.8, 50685.4, 60165.8, 71182.7, 84060.9, 99921.4, 117295, 137001, 159668, 185083, 215629, 248300, 284642, 324982, 369593, 421629, 475476, 533756, 597131, 665151, 743067, 821533, 905433, 994377, 1.09E+06, 1.19E+06, 1.30E+06, 1.41E+06, 1.53E+06, 1.65E+06, 1.78E+06, 1.92E+06, 2.06E+06, 2.20E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.37E+06, 3.60E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.08E+06, 5.34E+06, 5.61E+06, 5.90E+06, 6.18E+06, 6.47E+06, 6.76E+06, 7.07E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.42E+06, 8.64E+06, 8.93E+06, 8.86E+06, 8.82E+06, 8.79E+06]
A23_6 = [-238.396, -140.028, -52.1882, 45.5214, 217.911, 380.76, 606.446, 866.347, 1195.99, 1591.44, 2056.96, 2598.47, 3249.21, 4114.45, 5036.27, 6273.6, 7730.36, 9407.87, 11482.1, 14002.5, 17001.6, 20469.1, 24617.7, 29580.4, 35374.6, 42602.8, 50685.4, 60165.8, 71182.7, 84060.9, 99921.4, 117295, 137001, 159668, 185083, 215629, 248300, 284642, 324982, 369593, 421629, 475476, 533756, 597131, 665151, 743067, 821533, 905433, 994377, 1.09E+06, 1.19E+06, 1.30E+06, 1.41E+06, 1.53E+06, 1.65E+06, 1.78E+06, 1.92E+06, 2.06E+06, 2.20E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.37E+06, 3.60E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.08E+06, 5.34E+06, 5.61E+06, 5.90E+06, 6.18E+06, 6.47E+06, 6.76E+06, 7.07E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.42E+06, 8.64E+06, 8.93E+06, 8.86E+06, 8.82E+06, 8.79E+06]
A24_4 = [-108.445, -32.1199, 92.5667, 185.999, 344.243, 527.16, 783.113, 1041.7, 1423.32, 1822.06, 2319.49, 2891.6, 3550.89, 4451.33, 5466.92, 6783.2, 8310.69, 10086.6, 12310.9, 14885.5, 18056.3, 21750.5, 26132.6, 31326.7, 37393.9, 45056, 53635.1, 63493.2, 75081.2, 88649.6, 105348, 123397, 144252, 167736, 194570, 226493, 260677, 298654, 340720, 387148, 441235, 497338, 558001, 623834, 694452, 775377, 856562, 943464, 1.04E+06, 1.13E+06, 1.24E+06, 1.35E+06, 1.47E+06, 1.59E+06, 1.71E+06, 1.84E+06, 1.99E+06, 2.13E+06, 2.26E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.52E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.05E+06, 5.26E+06, 5.54E+06, 5.89E+06, 6.11E+06, 6.40E+06, 6.74E+06, 6.99E+06, 7.29E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.58E+06, 8.89E+06, 8.85E+06, 8.81E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.75E+06, 8.74E+06, 8.74E+06]
A25_5 = [-83.442, -26.5271, 92.8957, 228.11, 430.438, 619.935, 860.096, 1174.94, 1505.57, 1937.86, 2478.06, 3145.91, 3871.65, 4802.69, 5935.07, 7343.14, 8977.22, 10992.3, 13428.1, 16062.6, 19635.5, 23636.3, 28448.7, 33974.1, 40706.5, 48888.4, 57947.5, 68665.6, 81154, 95557.1, 113243, 132625, 154506, 179420, 207707, 241361, 277184, 316936, 360820, 409211, 465369, 523424, 586042, 653687, 726508, 809571, 892755, 981770, 1.08E+06, 1.18E+06, 1.28E+06, 1.40E+06, 1.52E+06, 1.64E+06, 1.76E+06, 1.90E+06, 2.05E+06, 2.19E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.37E+06, 3.58E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.08E+06, 5.34E+06, 5.61E+06, 5.90E+06, 6.16E+06, 6.47E+06, 6.76E+06, 7.05E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.41E+06, 8.62E+06, 8.91E+06, 8.84E+06, 8.80E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.75E+06, 8.74E+06, 8.74E+06]
A27_0 = [-64.3607, 4.72681, 127.768, 297.526, 531.108, 756.794, 1005.51, 1381.21, 1757.91, 2336.92, 2869.23, 3647.61, 4468.44, 5567.59, 6842.09, 8471.9, 10360.9, 12682.3, 15262.9, 18339.9, 22362.1, 26856.1, 32110, 38397, 45669.3, 54866.8, 65029.9, 76743.2, 90556.4, 106463, 125759, 146941, 170664, 197814, 228052, 264478, 302801, 345228, 391898, 442974, 502769, 564015, 629860, 700855, 777179, 863656, 950655, 1.04E+06, 1.14E+06, 1.24E+06, 1.35E+06, 1.48E+06, 1.60E+06, 1.72E+06, 1.85E+06, 1.99E+06, 2.14E+06, 2.27E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.52E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.05E+06, 5.29E+06, 5.55E+06, 5.90E+06, 6.11E+06, 6.40E+06, 6.74E+06, 7.00E+06, 7.29E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.58E+06, 8.89E+06, 8.84E+06, 8.80E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.75E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06]
A28_7 = [-59.7549, 11.6356, 188.631, 385.366, 621.58, 890.692, 1248.63, 1593.41, 2060.57, 2711.64, 3453.18, 4265.12, 5258.01, 6564.75, 8059.68, 9998.07, 12191.1, 14745, 17724.4, 21281.7, 25932.3, 31062.2, 37105.4, 44161.5, 52505, 62834.9, 74247.5, 87393.9, 102700, 120282, 141769, 164644, 190722, 219944, 252876, 291923, 332731, 377862, 426967, 481006, 543561, 607541, 675905, 749682, 828582, 917610, 1.01E+06, 1.10E+06, 1.20E+06, 1.31E+06, 1.42E+06, 1.54E+06, 1.66E+06, 1.79E+06, 1.92E+06, 2.06E+06, 2.22E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.37E+06, 3.58E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.08E+06, 5.34E+06, 5.61E+06, 5.90E+06, 6.15E+06, 6.43E+06, 6.74E+06, 7.03E+06, 8.40E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.59E+06, 8.91E+06, 8.87E+06, 8.82E+06, 8.80E+06, 8.79E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06]
A29_1 = [-137.067, 13.6095, 130.4, 340.624, 588.023, 877.204, 1183.49, 1672.04, 2141.51, 2793.23, 3567.01, 4457.25, 5538.31, 6826.3, 8444.59, 10425.1, 12699.7, 15373.4, 18503.4, 22195.6, 27101.2, 32330.5, 38673.3, 45957.5, 54613.8, 65349.7, 77065, 90735.4, 106530, 124602, 146670, 170231, 196997, 226872, 260603, 300505, 342263, 388236, 438319, 493247, 557056, 621922, 691412, 766306, 845908, 936550, 1.03E+06, 1.12E+06, 1.22E+06, 1.33E+06, 1.44E+06, 1.57E+06, 1.69E+06, 1.82E+06, 1.96E+06, 2.10E+06, 2.25E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.35E+06, 3.36E+06, 3.42E+06, 4.19E+06, 4.20E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.13E+06, 5.40E+06, 5.68E+06, 5.95E+06, 6.23E+06, 6.52E+06, 6.82E+06, 7.12E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.42E+06, 8.68E+06, 8.93E+06, 8.85E+06, 8.82E+06, 8.79E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06]
A32_5 = [-93.9697, 14.5965, 288.973, 555.782, 912.076, 1318.38, 1789.16, 2238.89, 2908.05, 3808.82, 4737.22, 5902.83, 7268.79, 8953.54, 10895.2, 13573.2, 16296.2, 19595, 23614.6, 28354, 34267.5, 40989.8, 48657.8, 57708.6, 68312.9, 81409.6, 95709.7, 112151, 131155, 152788, 178754, 206667, 237793, 272747, 311676, 357452, 405039, 456922, 513684, 575226, 646100, 718048, 794871, 876939, 964312, 1.06E+06, 1.16E+06, 1.27E+06, 1.37E+06, 1.49E+06, 1.61E+06, 1.74E+06, 1.88E+06, 2.01E+06, 2.16E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.37E+06, 3.53E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.05E+06, 5.26E+06, 5.55E+06, 5.90E+06, 6.11E+06, 6.38E+06, 6.71E+06, 6.97E+06, 7.29E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.53E+06, 8.87E+06, 8.85E+06, 8.81E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.75E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06]
A34_1 = [-180.823, 40.9155, 337.005, 678.495, 1027.55, 1397.66, 1975.7, 2601.76, 3359.09, 4354.94, 5514.29, 6870.38, 8544.28, 10430, 12861.6, 15721.8, 18916.3, 22823.4, 27471.3, 32747.9, 39664.3, 47071.4, 55854.4, 66178.4, 77978.6, 92739.9, 108602, 126897, 147878, 171610, 200178, 230331, 264228, 302050, 343794, 392750, 443237, 498644, 558645, 623610, 698060, 773392, 853533, 939193, 1.03E+06, 1.13E+06, 1.23E+06, 1.34E+06, 1.46E+06, 1.57E+06, 1.70E+06, 1.84E+06, 1.97E+06, 2.11E+06, 2.25E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.45E+06, 4.19E+06, 4.20E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.04E+06, 5.18E+06, 5.47E+06, 5.74E+06, 6.01E+06, 6.32E+06, 6.58E+06, 6.87E+06, 7.17E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.43E+06, 8.75E+06, 8.90E+06, 8.83E+06, 8.81E+06, 8.78E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06]
A35_1 = [-76.2043, 114.938, 390.63, 769.625, 1161.45, 1636.84, 2262.24, 2962.99, 3811.78, 4905.34, 6146.94, 7715.55, 9527.95, 11687.8, 14247.6, 17356.9, 20933.6, 25228.9, 30187.1, 36043.7, 43429.9, 51565.7, 61020.2, 72067.3, 84859.4, 100572, 117682, 137244, 159432, 184392, 214340, 246359, 281820, 321283, 364852, 415638, 467948, 525138, 586932, 653582, 730015, 807316, 889082, 976695, 1.07E+06, 1.17E+06, 1.28E+06, 1.39E+06, 1.50E+06, 1.62E+06, 1.75E+06, 1.89E+06, 2.02E+06, 2.17E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.53E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.05E+06, 5.26E+06, 5.50E+06, 5.79E+06, 6.08E+06, 6.35E+06, 6.64E+06, 6.93E+06, 7.24E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.50E+06, 8.81E+06, 8.90E+06, 8.84E+06, 8.81E+06, 8.79E+06, 8.77E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.76E+06]
A39_6 = [-138.054, 232.716, 622.896, 1125.92, 1803.31, 2539.58, 3322.9, 4303.29, 5536.34, 7093.11, 8868, 11075.8, 13689.3, 16482.4, 19972, 24403.5, 29350.5, 35044.9, 41865.5, 49786.9, 59641.7, 70476, 83018.3, 97531, 114157, 134529, 156284, 180896, 208781, 239937, 277123, 316023, 359036, 406399, 457865, 517820, 579371, 645622, 716750, 793202, 880072, 967277, 1.06E+06, 1.16E+06, 1.26E+06, 1.38E+06, 1.49E+06, 1.61E+06, 1.74E+06, 1.87E+06, 2.00E+06, 2.15E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.50E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.05E+06, 5.24E+06, 5.50E+06, 5.77E+06, 6.05E+06, 6.34E+06, 6.63E+06, 6.92E+06, 7.23E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.47E+06, 8.79E+06, 8.87E+06, 8.81E+06, 8.78E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.73E+06]
A42_2 = [-78.8362, 278.445, 870.953, 1509.52, 2267.51, 3151.83, 4216.76, 5497.19, 7038.17, 8987.75, 11208.4, 13847.2, 16810.8, 20396.4, 24694, 30027.2, 36036.5, 43007.8, 51183.8, 60625.7, 72372.6, 85184.1, 99979.3, 116964, 136385, 159821, 184736, 212853, 244454, 279801, 321374, 364787, 412312, 464202, 520792, 586171, 652570, 724194, 800721, 882368, 974916, 1.07E+06, 1.17E+06, 1.27E+06, 1.38E+06, 1.50E+06, 1.62E+06, 1.74E+06, 1.87E+06, 2.01E+06, 2.15E+06, 2.30E+06, 2.30E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 2.51E+06, 3.34E+06, 3.34E+06, 3.34E+06, 3.36E+06, 3.36E+06, 3.50E+06, 4.19E+06, 5.03E+06, 5.03E+06, 5.03E+06, 5.04E+06, 5.04E+06, 5.21E+06, 5.47E+06, 5.74E+06, 6.03E+06, 6.32E+06, 6.60E+06, 6.89E+06, 7.18E+06, 8.40E+06, 8.40E+06, 8.41E+06, 8.42E+06, 8.74E+06, 8.89E+06, 8.82E+06, 8.79E+06, 8.76E+06, 8.76E+06, 8.76E+06, 8.75E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06, 8.74E+06]
#A43_4 = [-108.774, -115.025, -89.6928, -86.4029, -96.2726, -120.618, -106.471, -116.341, -116.67, -100.878, -115.025, -121.276, -116.67, -125.224, -115.354, -116.341, -99.8915, -36.7257, -86.074, -115.354, -117.986, -107.458, -107.787, -56.136, -45.9374, -69.2956, -81.1391, -97.5885, -87.3899, -88.7059, -100.878, -112.722, -100.22, -72.5854, -99.8915, -134.435, -140.357, -127.855, -104.168, -103.839, -125.224, -90.3508, -85.745, -83.1131, -124.895, -88.7059, -61.0708, -64.0317, -17.9734, -52.8461, -13.3675, -15.3415, 35.6517, 16.2414, 76.4462, 103.752, 101.778, 159.351, 237.322, 346.546, 403.79, 509.395, 645.267, 803.839, 960.767, 1248.96, 1492.74, 1818.11, 2204.34, 2670.19, 3275.86, 3978.25, 4793.15, 5838.68, 7077.65, 8525.19, 10436.6, 12630.6, 15114.8, 18052.7, 21675.5, 26087.2, 31635, 38042.3, 45614.7, 54714.2, 65635.6, 79407.7, 95124.4, 113982, 136490, 163406, 197912, 236694, 283323, 338998, 405599, 490330, 585838, 699851]
ap23_4 = [x*1E-09 for x in A23_4]
ap23_6 = [x*1E-09 for x in A23_6]
ap24_4 = [x*1E-09 for x in A24_4]
ap25_5 = [x*1E-09 for x in A25_5]
ap27_0 = [x*1E-09 for x in A27_0]
ap28_7 = [x*1E-09 for x in A28_7]
ap29_1 = [x*1E-09 for x in A29_1]
ap32_5 = [x*1E-09 for x in A32_5]
ap34_1 = [x*1E-09 for x in A34_1]
ap35_1 = [x*1E-09 for x in A35_1]
ap39_6 = [x*1E-09 for x in A39_6]
ap42_2 = [x*1E-09 for x in A42_2]
#ap43_4 = [x*10E-09 for x in A43_4]

def getVlist(n):
    match (n):
        case 0:
            return Vp23_4,23.4
        case 1:
            return Vp23_6,23.6
        case 2:
            return Vp24_4,24.4
        case 3:
            return Vp25_5,25.5
        case 4:
            return Vp27_0,27.0
        case 5:
            return Vp28_7,28.7
        case 6:
            return Vp29_1,29.1
        case 7:
            return Vp32_5,32.5
        case 8:
            return Vp34_1,34.1
        case 9:
            return Vp35_1,35.1
        case 10:
            return Vp39_6,39.6
        case 11:
            return Vp42_2,42.2
#        case 12:
#            return Vp43_4,43.4

def getAlist(n):
    match (n):
        case 0:
            return ap23_4,23.4
        case 1:
            return ap23_6,23.6
        case 2:
            return ap24_4,24.4
        case 3:
            return ap25_5,25.5
        case 4:
            return ap27_0,27.0
        case 5:
            return ap28_7,28.7
        case 6:
            return ap29_1,29.1
        case 7:
            return ap32_5,32.5
        case 8:
            return ap34_1,34.1
        case 9:
            return ap35_1,35.1
        case 10:
            return ap39_6,39.6
        case 11:
            return ap42_2,42.2
#        case 12:
#            return ap43_4,43.4

size = 12

def pruneData(data):
    for i in range(len(data) -1):
        if ((data[i]) > (data[i+1])):
            return i
    return len(data)

Vpdata = [getVlist(i) for i in range(size)]
Apdata = [getAlist(i) for i in range(size)]

l = [pruneData(Apdata[i][0]) for i in range(size)]

Vdata = [(Vpdata[i][0][0:l[i]],Vpdata[i][1]) for i in range(size)]
Adata = [(Apdata[i][0][0:l[i]],Apdata[i][1]) for i in range(size)]

fitData = [curve_fit(transCurrent,Vdata[i][0],Adata[i][0]) for i in range(size)]

for i in range (size):
    print(f"At {Vdata[i][1]} C, V_T = {fitData[i][0][0]} with err: {np.sqrt(np.diag(fitData[i][1]))[0]}")
for i in range (size):
    print(f"At {Vdata[i][1]} C, I_S = {fitData[i][0][1]} with err: {np.sqrt(np.diag(fitData[i][1]))[1]}")
boltz = 0
boltzVar = 0
for i in range(size):
    boltz += fitData[i][0][0]*e/(Vdata[i][1]+273)
    boltzVar += (np.sqrt(np.diag(fitData[i][1]))[0]*e/(Vdata[i][1]+273))**2
boltzC = boltz/size
boltzErr = np.sqrt(boltzVar)

error = ((boltzC - k + boltzErr)*100/k,(boltzC - k - boltzErr)*100/k)
print(f"k = {boltzC} with err {boltzErr}")
print(f"We found a {error[0]}% error for the upper bound, and a {error[1]}% for the lower bound")


Is = [(Vdata[i][1]+273,fitData[i][0][1]) for i in range(size)]

def satCurrent(T,Eg):
    return Is[0][1]*(T/Is[0][0])**3*np.exp((e*Eg/k)*((1/Is[0][0])-(1/T)))

Bg = curve_fit(satCurrent,[Is[i][0] for i in range(size)],[Is[i][1] for i in range(size)])
print(f"Eg = {Bg[0]} with err: {np.sqrt(np.diag(Bg[1]))}")

'''
[Graphing Section]
'''
'''
[New Sat Current Model]
'''
lnIs = [np.log(Is[i][1]) for i in range(size)]
Trecip = [(1/Is[i][0]) for i in range (size)]
paramsSat = linregress(Trecip,lnIs)
print(paramsSat)
print(-k*paramsSat[0]/e)
intervalT = np.linspace(290,320,1000)
plt.figure()
plt.xlabel('1/T (Kelvin)^-1',fontsize = 14)
plt.ylabel('ln(I_S) (ln(Amps))',fontsize=14)
plt.scatter(Trecip,lnIs,color="black",label="data",s=5)
plt.plot((1/intervalT),(1/intervalT)*paramsSat[0] + paramsSat[1],color="black",linewidth=1.2,label ="Best-Fit Curve")
plt.legend()
plt.savefig("linGeSatCurrent.png",bbox_inches='tight')
plt.close()

intervalT = np.linspace(290,320,1000)
plt.figure()
plt.xlim(290,320)
plt.xlabel('T (Kelvin)',fontsize=14)
plt.ylabel('I_S (Pico Amps)',fontsize=14)
plt.scatter([Is[i][0] for i in range(size)],[Is[i][1] for i in range(size)],color="black",label="data",s=10)
plt.plot(intervalT,satCurrent(intervalT,Bg[0]),color="black",linewidth=1.2,label="Best-fit Curve (Eg = 0.158)")
plt.plot(intervalT,satCurrent(intervalT,.66)*1E012,color="black",linestyle="dashed",linewidth=1.2,label="Expected curve (Eg = 0.66eV)")
plt.legend()
plt.savefig("2_6GeSat_Current.png",bbox_inches='tight')
plt.close()

intervalV = np.linspace(0,0.5,1000)
for i in range(size):
    plt.figure()
    plt.xlim(0,0.5)
    plt.xlabel('V_BE (Volts)',fontsize=14)
    plt.ylabel('I_C (Nano Amps)',fontsize=14)
    name = "GeTemp" + str(getAlist(i)[1])+ ".png"
    plt.scatter(getVlist(i)[0],[x*1E+09 for x in getAlist(i)[0]],color = "black",label ="data",s=5)
    plt.plot(intervalV,[x*1E+09 for x in transCurrent(intervalV,fitData[i][0][0],fitData[i][0][1])],color ="black",linewidth=1.2,label="Best-Fit Curve")
    plt.legend()
    plt.savefig(name,bbox_inches='tight')
    plt.close()

'''
[Thermal Volt vs Temp]
'''
def thermVolt(T,k):
    return k*T/e

Temps = np.array([Vdata[i][1] + 273 for i in range(size)])
VoltsT = np.array([fitData[i][0][0] for i in range(size)])
Temps = Temps[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(Temps, VoltsT)
print(a)
print(k/e)
ssR = 0
SoSqrs = 0
for i in range(size):
    ssR += (VoltsT[i] - Temps[i]*a)**2
    SoSqrs += (VoltsT[i]-np.mean(VoltsT))**2
print(f"ssR = {ssR}")
print(f"SoSqrs = {SoSqrs}")
r = 1-(ssR/SoSqrs)
print(f"R^2 = {r}")
s = 0
for i in range(size):
    s+= (VoltsT[i] - Temps[i]*a)**2

np.sqrt(s/7)
print(f"Std dev of resiudals = {s}")
intervalT = np.linspace(290,320,1000)
plt.figure()
plt.xlim(290,320)
plt.xlabel('T (Kelvin)',fontsize=14)
plt.ylabel('V_T (Volts)',fontsize=14)
plt.scatter(Temps,VoltsT,color="black",label="data",s=5)
plt.plot(intervalT,intervalT*a,color="black",linewidth=1.2,label="Best-Fit Curve")
plt.plot(intervalT,intervalT*k/e,color="blue",linewidth=1.2,label="Expected Thermal Voltage Curve")
plt.legend()
plt.savefig("GeBoltz.png",bbox_inches="tight")

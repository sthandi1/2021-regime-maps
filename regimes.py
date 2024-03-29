# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:23:15 2019

@author: st8g14
"""

import os
import matplotlib.pyplot as plt
import csv
import numpy as np

os.environ['PATH'] = os.environ['PATH'] + ':/Library/TeX/texbin'


def lasheras_regime():
    atomisation_we = []
    atomisation_re = []
    membrane_we = []
    membrane_re = []
    shearbreakup_we = []
    shearbreakup_re = []
    non_axi_we = []
    non_axi_re = []
    rayleigh_we = []
    rayleigh_re = []
    windstress_we = []
    windstress_re = []

    # open atomisation file
    with open('atomization_lasheras_line.csv') as atomisation_line:
        readCSV_atomisation = csv.reader(atomisation_line, delimiter=',')
        for row in readCSV_atomisation:
            atom_we = float(row[0])
            atom_re = float(row[1])
            atomisation_we.append(atom_we)
            atomisation_re.append(atom_re)

    with open('membrane_breakup.csv') as membrane_breakup:
        readCSV_membrane = csv.reader(membrane_breakup, delimiter=',')
        for row in readCSV_membrane:
            mem_we = float(row[0])
            mem_re = float(row[1])
            membrane_we.append(mem_we)
            membrane_re.append(mem_re)\

    with open('shear_breakup.csv') as shear_breakup:
        readCSV_shearbreakup = csv.reader(shear_breakup, delimiter=',')
        for row in readCSV_shearbreakup:
            shear_we = float(row[0])
            shear_re = float(row[1])
            shearbreakup_we.append(shear_we)
            shearbreakup_re.append(shear_re)

    with open('non_axi_line.csv') as non_axi_line:
        readCSV_non_axi = csv.reader(non_axi_line, delimiter=',')
        for row in readCSV_non_axi:
            non_ax_we = float(row[0])
            non_ax_re = float(row[1])
            non_axi_we.append(non_ax_we)
            non_axi_re.append(non_ax_re)

    with open('rayleigh_line.csv') as rayleigh_line:
        readCSV_rayleigh = csv.reader(rayleigh_line, delimiter=',')
        for row in readCSV_rayleigh:
            ray_we = float(row[0])
            ray_re = float(row[1])
            rayleigh_we.append(ray_we)
            rayleigh_re.append(ray_re)

    with open('wind_stress_line.csv') as wind_stress_line:
        readCSV_windstress = csv.reader(wind_stress_line, delimiter=',')
        for row in readCSV_windstress:
            wind_we = float(row[0])
            wind_re = float(row[1])
            windstress_we.append(wind_we)
            windstress_re.append(wind_re)

    mu = 8.89e-4
    rho_l = 1000
    rho_g = 1.225
    sigma = 0.07

    figa_re = rho_l*0.16*7.6e-3/mu
    figa_we = rho_g*19**2*7.6e-3/sigma

    figb_re = rho_l*0.55*7.6e-3/mu
    figb_we = rho_g*21**2*7.6e-3/sigma

    figc_re = rho_l*0.86*7.6e-3/mu
    figc_we = rho_g*30**2*7.6e-3/sigma

    figd_re = rho_l*0.26*7.6e-3/mu
    figd_we = rho_g*50**2*7.6e-3/sigma

    print("Figure A Reynolds number: {:.2f}".format(figa_re))
    print("Figure A Weber number: {:.2f}".format(figa_we))

    print("\nFigure B Reynolds number: {:.2f}".format(figb_re))
    print("Figure B Weber number: {:.2f}".format(figb_we))

    print("\nFigure C Reynolds number: {:.2f}".format(figc_re))
    print("Figure C Weber number: {:.2f}".format(figc_we))

    print("\nFigure D Reynolds number: {:.2f}".format(figd_re))
    print("Figure D Weber number: {:.2f}".format(figd_we))

    # setting up the figure
    fig, ax = plt.subplots()

    # setting log scales
    ax.set_xscale('log')
    ax.set_yscale('log')

    # plotting regime lines
    ax.plot(atomisation_we, atomisation_re, color='black')
    ax.plot(membrane_we, membrane_re, color='black')
    ax.plot(shearbreakup_we, shearbreakup_re, color='black')
    ax.plot(non_axi_we, non_axi_re, color='black')
    ax.plot(rayleigh_we, rayleigh_re, color='black', linestyle='solid')
    ax.plot(windstress_we, windstress_re, color='black')

    # plotting the Lasheras points
    ax.plot(figa_we, figa_re, color='black', marker='o')
    ax.plot(figb_we, figb_re, color='black', marker='o')
    ax.plot(figc_we, figc_re, color='black', marker='o')
    ax.plot(figd_we, figd_re, color='black', marker='o')

    # plotting the Kelda point
    ax.plot(21.68, 9537.37, color='black', marker='^')

    ax.annotate("A", xy=(figa_we, figa_re), xytext=(60, 1300))
    ax.annotate("B", xy=(figb_we, figb_re), xytext=(70, 4300))
    ax.annotate("C", xy=(figc_we, figc_re), xytext=(140, 6800))
    ax.annotate("D", xy=(figd_we, figd_re), xytext=(400, 2000))
    ax.annotate("Kelda", xy=(21.68, 9537.37), xytext=(7, 9800), fontsize=9)

    ax.text(1e-2, 2e5, "Atomisation", fontsize=8)
    ax.text(1e-2, 2e4, "Wind stress", fontsize=8)
    ax.text(5e-3, 2e2, "Axisymmetric", fontsize=8)
    ax.text(1e-1, 3e3, "Non-axisymmetric", fontsize=8)
    ax.text(1e1, 5e4, "Shear breakup", fontsize=8)

    ax.grid()
    ax.set_xlim(1e-3, 1e4)
    ax.set_ylim(10, 1e6)
    ax.set_xlabel('We')
    ax.set_ylabel('$\\mathrm{Re}_l$')

    fig.set_size_inches(7, 5)
    fig.savefig(fname='lasheras_regime.pgf', bbox_inches='tight')


def farago():
    # loading files
    superpulsating = np.loadtxt('farago_regime_superpulsating.csv',
                                delimiter=',')
    rayleigh = np.loadtxt('farago_regime_data_rayleigh.csv',
                          delimiter=',')
    membrane = np.loadtxt('farago_regime_data_membrane.csv',
                          delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()
    ax.plot(superpulsating[:, 0], superpulsating[:, 1], color='black')
    ax.plot(rayleigh[:, 0], rayleigh[:, 1], color='black')
    ax.plot(membrane[:, 0], membrane[:, 1], color='black')

    # plotting case locations
    ax.plot(5.22, 1551, label='Case 1', marker='o', color='black',
            linestyle='none')
    ax.plot(11.6, 1551, label='Case 2', marker='X', color='black',
            linestyle='none')
    ax.plot(22.9, 1551, label='Case 3', marker='^', color='black',
            linestyle='none')
    ax.plot(52.7, 1551, label='Case 4', marker='s', color='black',
            linestyle='none')

    ax.plot(5.22, 2940, label='Case 5', marker='o', color='red',
            linestyle='none')
    ax.plot(11.6, 2940, label='Case 6', marker='X', color='red',
            linestyle='none')
    ax.plot(22.9, 2940, label='Case 7', marker='^', color='red',
            linestyle='none')
    ax.plot(52.7, 2940, label='Case 8', marker='s', color='red',
            linestyle='none')

    ax.plot(5.22, 6444, label='Case 9', marker='o', color='blue',
            linestyle='none')
    ax.plot(11.6, 6444, label='Case 10', marker='X', color='blue',
            linestyle='none')
    ax.plot(22.9, 6444, label='Case 11', marker='^', color='blue',
            linestyle='none')
    ax.plot(52.7, 6444, label='Case 12', marker='s', color='blue',
            linestyle='none')

    # setting log scale
    ax.set_xscale('log')
    ax.set_yscale('log')
    # setting axis limits
    ax.set_xlim(1e-3, 1e3)
    ax.set_ylim(1e2, 1e5)
    # labelling axis
    ax.set_xlabel('$\\mathrm{We}_\\mathrm{g}$')
    ax.set_ylabel('$\\mathrm{Re}_l$')
    # labelling rayleigh regime
    ax.text(1e-1, 1e3, 'Rayleigh regime')
    # labelling superpulsating regime
    ax.text(8e0, 2e2, 'Superpulsating regime')
    # labelling fiber type regime
    ax.text(1.3e2, 1e4, 'Fiber type \nregime')
    # annotating with arrow membrane type regime
    ax.annotate('Membrane type regime', xy=(5e1, 8e3), xytext=(5e0, 3e4),
                arrowprops=dict(facecolor='black', width=0.5, headwidth=7))
    ax.legend()
    fig.set_size_inches(6, 4)
    fig.savefig('farago_chigier_cases_regimes.pgf', bbox_inches='tight')


def hopfinger():
    # loading files
    rayleigh = np.loadtxt('hopfinger_rayleigh.csv', delimiter=',')
    nonaxisymmetric = np.loadtxt('hopfinger_nonaxisymmetric_rayleigh.csv',
                                 delimiter=',')
    wave_like = np.loadtxt('hopfinger_wave_like.csv', delimiter=',')
    fiber = np.loadtxt('hopfinger_fiber.csv', delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()

    # plotting regime lines
    ax.plot(rayleigh[:, 0], rayleigh[:, 1], color='black')
    ax.plot(nonaxisymmetric[:, 0], nonaxisymmetric[:, 1], color='black')
    ax.plot(wave_like[:, 0], wave_like[:, 1], color='black')
    ax.plot(fiber[:, 0], fiber[:, 1], color='black')

    # setting log scales
    ax.set_xscale('log')
    ax.set_yscale('log')

    # setting axis limits
    ax.set_xlim(1e-3, 1e5)
    ax.set_ylim(1e1, 1e6)

    # labelling axis
    ax.set_xlabel('$\\mathrm{We}_\\mathrm{g}$')
    ax.set_ylabel('$\\mathrm{Re}_l$')

    # labelling regimes
    ax.text(2e-3, 4e1, 'Rayleigh breakup', )
    ax.text(3.5e-3, 1.5e1, 'Non-axisymmetric Rayleigh breakup', rotation=-35)
    ax.text(1e-1, 5e3, 'wave-like')
    ax.text(1e2, 2e1, 'membrane breakup', rotation=-80)
    ax.text(1e1, 1e5, 'fiber type')

    # plotting case locations
    ax.plot(5.22, 1551, label='Case 1', marker='o', color='black',
            linestyle='none')
    ax.plot(11.6, 1551, label='Case 2', marker='X', color='black',
            linestyle='none')
    ax.plot(22.9, 1551, label='Case 3', marker='^', color='black',
            linestyle='none')
    ax.plot(52.7, 1551, label='Case 4', marker='s', color='black',
            linestyle='none')

    ax.plot(5.22, 2940, label='Case 5', marker='o', color='red',
            linestyle='none')
    ax.plot(11.6, 2940, label='Case 6', marker='X', color='red',
            linestyle='none')
    ax.plot(22.9, 2940, label='Case 7', marker='^', color='red',
            linestyle='none')
    ax.plot(52.7, 2940, label='Case 8', marker='s', color='red',
            linestyle='none')

    ax.plot(5.22, 6444, label='Case 9', marker='o', color='blue',
            linestyle='none')
    ax.plot(11.6, 6444, label='Case 10', marker='X', color='blue',
            linestyle='none')
    ax.plot(22.9, 6444, label='Case 11', marker='^', color='blue',
            linestyle='none')
    ax.plot(52.7, 6444, label='Case 12', marker='s', color='blue',
            linestyle='none')

    # adding legend
    ax.legend()

    # resizing chart
    fig.set_size_inches(6, 4)
    # saving as pgf file
    fig.savefig('hopfinger_cases_regime.pgf', bbox_inches='tight')


def glr_calculator(weber_number, reynolds_number):
    # liquid jet diameter
    d_l = 2e-3
    # gas jet diameter
    d_g = 7e-3
    # viscosity of liquid
    mu_l = 8.9e-4
    # density of liquid
    rho_l = 1000
    # surface tension
    sigma = 0.07
    # gas density
    rho_g = 1.225
    # liquid velocity
    u_l = reynolds_number*mu_l/(rho_l*d_l)
    # gas velocity
    u_g = np.sqrt((weber_number*sigma)/(d_l*rho_g))+u_l
    # liquid area
    A_l = np.pi*d_l**2/4
    A_g = np.pi*d_g**2/4 - A_l
    glr = (rho_g*u_g*A_g)/(rho_l*u_g*A_g)
    ar = A_l/A_g
    return glr, ar


def zhao_glr():
    # loading files
    rayleigh = np.loadtxt('zhao_glr_rayleigh.csv', delimiter=',')
    bag = np.loadtxt('zhao_glr_bag.csv', delimiter=',')
    membrane = np.loadtxt('zhao_glr_membrane.csv', delimiter=',')

    # setting up plots
    fig, ax = plt.subplots()

    # plotting regime lines
    ax.plot(rayleigh[:, 0], rayleigh[:, 1], color='black')
    ax.plot(bag[:, 0], bag[:, 1], color='black')
    ax.plot(membrane[:, 0], membrane[:, 1], color='black')

    # setting log scales
    ax.set_xscale('log')
    ax.set_yscale('log')



    # labelling regimes
    ax.text(1e0, 1e1, 'Rayleigh')
    ax.text(1e0, 2e1, 'Bag breakup')
    ax.text(1e0, 5e1, 'Membrane-fiber regime')
    ax.text(1e0, 5e2, 'Fiber breakup')

    # Plotting case locations
    ax.plot(glr_calculator(5.22, 1551), 5.22, label='Case 1', marker='o',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 1551), 11.6, label='Case 2', marker='v',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 1551), 22.9, label='Case 3', marker='^',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 1551), 52.7, label='Case 4', marker='<',
            color='black', linestyle='none')

    ax.plot(glr_calculator(5.22, 2940), 5.22, label='Case 5', marker='>',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 2940), 11.6, label='Case 6', marker='1',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 2940), 22.9, label='Case 7', marker='s',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 2940), 52.7, label='Case 8', marker='p',
            color='black', linestyle='none')

    ax.plot(glr_calculator(5.22, 6444), 5.22, label='Case 9', marker='P',
            color='black', linestyle='none')
    ax.plot(glr_calculator(11.6, 6444), 11.6, label='Case 10', marker='*',
            color='black', linestyle='none')
    ax.plot(glr_calculator(22.9, 6444), 22.9, label='Case 11', marker='X',
            color='black', linestyle='none')
    ax.plot(glr_calculator(52.7, 6444), 52.7, label='Case 12', marker='D',
            color='black', linestyle='none')

    # resizing figure
    fig.set_size_inches(6, 4)

# coding: utf-8
import re
import csv
import numpy as np
import pandas as pd
from pyteomics import mass
from Bio.SeqUtils.ProtParam import ProteinAnalysis

"""
Parent sequence
* m/z x 1: user mass from pyteomics libray

code example:
mass.calculate_mass(sequence = peptide , ion_type = 'M', charge = int(peptideLi[1]))

* composition x 20: use ProteinAnalysis from Bio.SeqUtils.ProtParam

code example:
analysed_seq = ProteinAnalysis(peptide)
featureLi.extend(list(analysed_seq.count_amino_acids().values()))

* chemical property x 7 (total: 9): use method chemical_pro from ProteinAnalysis, pephelicity, pephydrophobicity and pepbasicity
* isoelectric point 
* instability index
* aromaticity
* helicity
* hydrophobicity
* basicity
* secondary_structure_fraction ([Helix, Turn, Sheet])

Fragment ion
* m/z x 1 
* chemical property x 7

"""

# helicity
def pephelicity (peptide) :
    helicity = 0
    for word in peptide:
        if ( word == 'A'):
            helicity += 1.24; 
        elif ( word == 'B'):
            helicity += 0.92; 
        elif ( word == 'C'):
            helicity += 0.79; 
        elif ( word == 'D'):
            helicity += 0.89; 
        elif ( word == 'E'):
            helicity += 0.85; 
        elif ( word == 'F'):
            helicity += 1.26; 
        elif ( word == 'G'):
            helicity += 1.15; 
        elif ( word == 'H'):
            helicity += 0.97; 
        elif ( word == 'I'):
            helicity += 1.29; 
        elif ( word == 'K'):
            helicity += 0.88; 
        elif ( word == 'L'):
            helicity += 1.28; 
        elif ( word == 'M'):
            helicity += 1.22; 
        elif ( word == 'N'):
            helicity += 0.94; 
        elif ( word == 'P'):
            helicity += 0.57; 
        elif ( word == 'Q'):
            helicity += 0.96; 
        elif ( word == 'R'):
            helicity += 0.95; 
        elif ( word == 'S'):
            helicity += 1; 
        elif ( word == 'T'):
            helicity += 1.09; 
        elif ( word == 'V'):
            helicity += 1.27; 
        elif ( word == 'W'):
            helicity += 1.07; 
        elif ( word == 'X'):
            helicity += 1.29; 
        elif ( word == 'Y'):
            helicity += 1.11; 
        elif ( word == 'Z'):
            helicity += 0.91; 
    helicity = helicity / len(peptide)
    return helicity

# hydrophobicity
def pephydrophobicity(peptide) :
    hydrophobicity = 0
    for word in peptide:
        if ( word == 'A'):
            hydrophobicity += 0.16; 
        elif ( word == 'B'):
            hydrophobicity += -3.14; 
        elif ( word == 'C'):
            hydrophobicity += 2.5; 
        elif ( word == 'D'):
            hydrophobicity += -2.49; 
        elif ( word == 'E'):
            hydrophobicity += -1.5; 
        elif ( word == 'F'):
            hydrophobicity += 5; 
        elif ( word == 'G'):
            hydrophobicity += -3.31; 
        elif ( word == 'H'):
            hydrophobicity += -4.63; 
        elif ( word == 'I'):
            hydrophobicity += 4.41; 
        elif ( word == 'K'):
            hydrophobicity += -5; 
        elif ( word == 'L'):
            hydrophobicity += 4.76; 
        elif ( word == 'M'):
            hydrophobicity += 3.23; 
        elif ( word == 'N'):
            hydrophobicity += -3.79; 
        elif ( word == 'P'):
            hydrophobicity += -4.92; 
        elif ( word == 'Q'):
            hydrophobicity += -2.76; 
        elif ( word == 'R'):
            hydrophobicity += -2.77; 
        elif ( word == 'S'):
            hydrophobicity += -2.85; 
        elif ( word == 'T'):
            hydrophobicity += -1.08; 
        elif ( word == 'V'):
            hydrophobicity += 3.02; 
        elif ( word == 'W'):
            hydrophobicity += 4.88; 
        elif ( word == 'X'):
            hydrophobicity += 4.59; 
        elif ( word == 'Y'):
            hydrophobicity += 2; 
        elif ( word == 'Z'):
            hydrophobicity += -2.13; 
        hydrophobicity = hydrophobicity / len(peptide)
    return hydrophobicity

# basicity
def pepbasicity (peptide) :
    basicity = 0
    for word in peptide:
        if ( word == 'A'):
            basicity += 206.4; 
        elif ( word == 'B'):
            basicity += 210.7; 
        elif ( word == 'C'):
            basicity += 206.2; 
        elif ( word == 'D'):
            basicity += 208.6; 
        elif ( word == 'E'):
            basicity += 215.6; 
        elif ( word == 'F'):
            basicity += 212.1; 
        elif ( word == 'G'):
            basicity += 202.7; 
        elif ( word == 'H'):
            basicity += 223.7; 
        elif ( word == 'I'):
            basicity += 210.8; 
        elif ( word == 'K'):
            basicity += 221.8; 
        elif ( word == 'L'):
            basicity += 209.6; 
        elif ( word == 'M'):
            basicity += 213.3; 
        elif ( word == 'N'):
            basicity += 212.8; 
        elif ( word == 'P'):
            basicity += 214.4; 
        elif ( word == 'Q'):
            basicity += 214.2; 
        elif ( word == 'R'):
            basicity += 237; 
        elif ( word == 'S'):
            basicity += 207.6; 
        elif ( word == 'T'):
            basicity += 211.7; 
        elif ( word == 'V'):
            basicity += 208.7; 
        elif ( word == 'W'):
            basicity += 216.1; 
        elif ( word == 'X'):
            basicity += 210.2; 
        elif ( word == 'Y'):
            basicity += 213.1; 
        elif ( word == 'Z'):
            basicity += 214.9; 
    basicity = basicity / len(peptide)
    return basicity

# chemical property into list
def chemical_pro(Li,sequence) :
    analysed_seq = ProteinAnalysis(sequence)
    #Li.extend(list(analysed_seq.count_amino_acids().values()))
    #Li.extend(list(analysed_seq.get_amino_acids_percent().values()))
    Li.append(analysed_seq.isoelectric_point())
    Li.append(analysed_seq.instability_index())
    Li.append(analysed_seq.aromaticity())
    #Li.append(analysed_seq.secondary_structure_fraction())
    for x in analysed_seq.secondary_structure_fraction() :
        Li.append(x)
    Li.append(pephydrophobicity(sequence))
    Li.append(pephelicity(sequence))
    Li.append(pepbasicity(sequence))
    
def chemical_pro_cle(Li,sequence) :
    analysed_seq = ProteinAnalysis(sequence)
    Li.extend(list(analysed_seq.count_amino_acids().values()))
    #Li.extend(list(analysed_seq.get_amino_acids_percent().values()))
    Li.append(analysed_seq.isoelectric_point())
    Li.append(analysed_seq.instability_index())
    Li.append(analysed_seq.aromaticity())
    Li.append(pephydrophobicity(sequence))
    Li.append(pephelicity(sequence))
    Li.append(pepbasicity(sequence))
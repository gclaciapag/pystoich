"""
*******************************************************
    Author: Glenn Laciapag
    Some Basic Chemical Stoichiometry Calculations
*******************************************************
"""

from scientific_notation import ScientificNotation
from element import Element
from element import element_data

AVOGADROS_CONSTANT = ScientificNotation(6.0221415, 23)


def convert_mass_to_atoms(mass, molar_mass):
    mol = mass / molar_mass
    scinot_mol = ScientificNotation(mol, 0)
    return scinot_mol * AVOGADROS_CONSTANT


def convert_mass_to_mole(mass, molar_mass):
    return mass / molar_mass


def convert_mole_to_mass(mol, molar_mass):
    return mol * molar_mass


def convert_atoms_to_mass(atoms, molar_mass):
    scinot_mol = atoms / AVOGADROS_CONSTANT
    mol = scinot_mol.sigfig * (10 ** scinot_mol.exponent)
    return mol * molar_mass


def convert_mass_to_percentage(elements_dict):
    total_mass = 0
    for elem in elements_dict:
        total_mass += elements_dict[elem]

    converted_mass = []
    for elem in elements_dict:
        converted_mass.append(elements_dict[elem] / total_mass * 100)

    elements_detected = {}
    for index, elem in enumerate(elements_dict):
        elements_detected[elem] = converted_mass[index]

    return elements_detected


def compute_empirical_formula(**kwargs):
    elements_detected = kwargs

    total_mass = 0
    for element in elements_detected:
        total_mass += elements_detected[element]

    if total_mass != 100:
        elements_detected = convert_mass_to_percentage(kwargs)

    atomic_weights = []
    for element in elements_detected:
        for elem_data in element_data:
            if element == elem_data[" Symbol"].replace(" ", ""):
                atomic_weights.append(float(elem_data[" Atomic_Weight"]))

    num_of_moles = []
    for index, element in enumerate(elements_detected):
        mole = elements_detected[element] / atomic_weights[index]
        num_of_moles.append(mole)

    min_mole = min(num_of_moles)
    mole_ratios = []
    for mole in num_of_moles:
        mole_ratios.append(round((mole / min_mole), 1))

    isWhole = True
    for mole_ratio in mole_ratios:
        if mole_ratio - round(mole_ratio) > 0.5:
            isWhole = False

    if isWhole:
        computed_mole_ratio = [round(mol) for mol in mole_ratios]
    else:
        computed_mole_ratio = [mol * 2 for mol in mole_ratio]

    empirical_formula = {}
    for index, elem in enumerate(elements_detected):
        empirical_formula[elem] = computed_mole_ratio[index]

    return empirical_formula


print(compute_empirical_formula(C=6.00, H=1.51, O=4.0))
print(compute_empirical_formula(C=52, H=13, O=35))

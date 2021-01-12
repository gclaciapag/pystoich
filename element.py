"""
*******************************************************
    Author: Glenn Laciapag
    Implementation of Element in Python
*******************************************************
"""

import csv

element_data = []

with open("elementdata.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        element_data.append(line)


class Element:

    def __init__(self, p=1, n=0):
        self._protons = p
        self._electrons = p
        self._neutrons = n
        self._symbol = element_data[p-1][" Symbol"].replace(" ", "")
        self._atomic_weight = element_data[p-1][" Atomic_Weight"]

    @property
    def electrons(self):
        return self._electrons

    @property
    def protons(self):
        return self._protons

    @property
    def neutrons(self):
        return self._neutrons

    @property
    def symbol(self):
        return self._symbol

    @property
    def atomic_weight(self):
        return self._atomic_weight

    @electrons.setter
    def electrons(self, e):
        self._electrons = e

    def get_mass(self):
        return self._protons + self._neutrons

    def get_charge(self):
        return self._protons - self._electrons

    def is_ion(self):
        if self.get_charge() == 0:
            return False
        else:
            return True

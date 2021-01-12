"""
*******************************************************
    Author: Glenn Laciapag
    Implementation of Scientific Notation in Python
*******************************************************
"""


class ScientificNotation:

    def __init__(self, sigfig=0.0, exp=0):
        self._sigfig = sigfig
        self._exp = exp

    @property
    def sigfig(self):
        return self._sigfig

    @sigfig.setter
    def sigfig(self, sf):
        self._sigfig = sf

    @property
    def exponent(self):
        return self._exp

    @exponent.setter
    def exponent(self, exp):
        self._exp = exp

    def __str__(self):
        return f"{self._sigfig}X10^{self._exp}"

    def __add__(self, other):
        try:
            if self._exp == other._exp:
                sigfig_sum = self._sigfig + other._sigfig
                exp = self._exp
            elif self._exp > other._exp:
                exp_diff = self._exp - other._exp
                other_sigfig = float(other._sigfig)
                divisor = 10 ** exp_diff
                converted_other_sigfig = other_sigfig / divisor
                sigfig_sum = self._sigfig + converted_other_sigfig
                exp = self._exp
            else:
                exp_diff = other._exp - self._exp
                self_sigfig = float(self._sigfig)
                divisor = 10 ** exp_diff
                converted_self_sigfig = self_sigfig / divisor
                sigfig_sum = converted_self_sigfig + other._sigfig
                exp = other._exp
            return ScientificNotation(sigfig_sum, exp)
        except:
            print(
                f"[Number must be initialized to a Scientific Notation Object] ... ScientificNotation({other}, 0)")

    def __sub__(self, other):
        try:
            if self._exp == other._exp:
                sigfig_diff = self._sigfig - other._sigfig
                exp = self._exp
            elif self._exp > other._exp:
                exp_diff = self._exp - other._exp
                other_sigfig = float(other._sigfig)
                divisor = 10 ** exp_diff
                converted_other_sigfig = other_sigfig / divisor
                sigfig_diff = self._sigfig - converted_other_sigfig
                exp = self._exp
            else:
                exp_diff = other._exp - self._exp
                self_sigfig = float(self._sigfig)
                divisor = 10 ** exp_diff
                converted_self_sigfig = self_sigfig / divisor
                sigfig_diff = converted_self_sigfig - other._sigfig
                exp = other._exp
            return ScientificNotation(sigfig_diff, exp)
        except:
            print(
                f"[Number must be initialized to a Scientific Notation Object] ... ScientificNotation({other}, 0)")

    def __mul__(self, other):
        try:
            sigfig_prod = self._sigfig * other._sigfig
            exp_prod = self._exp + other._exp
            return ScientificNotation(sigfig_prod, exp_prod)
        except:
            print(
                f"[Number must be initialized to a Scientific Notation Object] ... ScientificNotation({other}, 0)")

    def __truediv__(self, other):
        try:
            sigfig_truediv = self._sigfig / other._sigfig
            exp_truediv = self._exp - other._exp
            return ScientificNotation(sigfig_truediv, exp_truediv)
        except:
            print(
                f"[Number must be initialized to a Scientific Notation Object] ... ScientificNotation({other}, 0)")

    def __floordiv__(self, other):
        try:
            sigfig_floordiv = self._sigfig // other._sigfig
            exp_floordiv = self._exp - other._exp
            return ScientificNotation(sigfig_floordiv, exp_floordiv)
        except:
            print(
                f"[Number must be initialized to a Scientific Notation Object] ... ScientificNotation({other}, 0)")

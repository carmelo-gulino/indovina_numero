import random


class Model(object):
    def __init__(self):
        self._NMax = 100
        self._Mmax = 6
        self._Mrim = None
        self._segreto = None

    @property       #dal momento che nMax è privato devo mettere property
    def NMax(self):
        return self._NMax

    @property  # dal momento che nMax è privato devo mettere property
    def Mmax(self):
        return self._Mmax

    @property  # dal momento che nMax è privato devo mettere property
    def Mrim(self):
        return self._Mrim

    @property
    def segreto(self):
        return self._segreto

    def inizializza(self):
        self._segreto = random.randint(1, self._NMax)
        self._Mrim = self._Mmax

    def indovina(self, tentativo):

        if self._Mrim == 0:
            return self._Mrim, None
        else:
            self._Mrim -= 1

        if tentativo == self._segreto:
            return self._Mrim, 0
        elif tentativo > self._segreto:
            return self._Mrim, -1
        else:
            return self._Mrim, 1


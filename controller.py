from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def handleNuova(self, e):
        """
        inizio una nuova partita
        """
        self._view._txtMrim.value = self.getMmax()      #all'inizio rim=max
        self._view._btnProva.disabled = False       #abilito il tasto prova
        self._view._txtTentativo.disabled = False
        self._view._lvOut.controls.clear()      #pulisce tutta la lvOut
        self._view._lvOut.controls.append(ft.Text("Indovina il numero", color="green"))
        self._model.inizializza()
        self._view.update()

    def handleProva(self, e):
        """
        controllo che il tentativo sia un intero, in caso negativo faccio comparire il messaggio e finisco la prova
        """
        tent = self._view._txtTentativo.value
        try:
            intTent = int(tent)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il tentativo deve essere un intero", color="red"))
            self._view._txtTentativo.value = ""
            self._view.update()
            return

        mRim, result = self._model.indovina(intTent)
        self._view._txtMrim.value=mRim
        self._view.update()

        if mRim==0:     #se ho zero tentativi, ho perso ed eventualmente esco
            self._view._btnProva.disabled=True      #ho vinto e disabilito la prova
            self._view._txtTentativo.disabled=True      #ho vinto e disabilito la prova
            self._view._lvOut.controls.append(ft.Text(f"Hai perso! Il segreto era: {self._model.segreto}"))
            self._view._txtTentativo.value = ""
            self._view.update()
            return
        if result==0:
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto!"))
            self._view._btnProva.disabled=True      #ho vinto e disabilito la prova
            self._view._txtTentativo.value = ""
            self._view.update()
            return
        elif result == -1:
            self._view._lvOut.controls.append(ft.Text(f"Il segreto è più piccolo"))
            self._view._txtTentativo.value = ""
            self._view.update()
            return
        else:
            self._view._lvOut.controls.append(ft.Text(f"Il segreto è più grande"))
            self._view._txtTentativo.value = ""
            self._view.update()
            return

    def getNmax(self):
        return self._model.NMax

    def getMmax(self):
        return self._model.Mmax

    def getMrim(self):
        return self._model.Mrim
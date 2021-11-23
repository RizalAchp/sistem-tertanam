#!/usr/bin/env python3
'''
info:
    file ini adalah class baru yang digunakan sebagia popup window baru
    berisi widget gauge yang bergunsi untuk mengukur suhu
    pada sensor lm35 pada arduino
'''

from tkinter import Toplevel, Label, BooleanVar, Button
from tk_tools.canvas import RotaryScale
from classes.arduino import *


class suhuWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("225x300")
        labels = Label(self)
        labels.grid(column=0, row=1)
        button_exit = Button(self,
                             bg='#FF0020',
                             text="EXIT",
                             activebackground='#DD0010',
                             command=self.destroy
                             )
        button_exit.grid(column=0, row=2)
        flag = BooleanVar(self)
        flag.set(True)
        running = True
        self.resizable(False, False)
        while running:
            if flag.get():
                nilai_baca = board.analog_read(lm35_pin)
                suhu = 5.0*nilai_baca[0]/10.23
                rs = RotaryScale(self, 100, 200, unit=" °C")
                rs.grid(row=0, column=0)
                rs.set_value(suhu)
                rs.update_idletasks()
                tanggal = datetime.now()
                formatwaktu = tanggal.hour, tanggal.minute, tanggal.second
                labels.config(text="pada waktu: %d:%d:%d" % (formatwaktu))
                labels.update_idletasks()
                self.update()
                delay(0.3)
            else:
                break

    def stopPopUp(self):
        global running
        running = False

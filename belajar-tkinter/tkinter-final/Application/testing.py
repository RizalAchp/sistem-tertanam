#!/usr/bin/env python3
'''
info:
    file ini adalah class baru yang digunakan sebagia popup window baru
    berisi widget gauge yang bergunsi untuk mengukur suhu
    pada sensor lm35 pada arduino
'''

from tkinter import BooleanVar, Button, Label, Toplevel

from tk_tools.canvas import RotaryScale

from Application.arduino_config import *


class suhuWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("210x320")
        self.config(bg="#232323")
        labels = Label(self)
        labels.grid(column=0, row=1)
        warning_label = Label(self)
        warning_label.grid(column=0, row=3)
        button_exit = Button(self,
                             bg='#FF6666',
                             text="EXIT",
                             activebackground='#DD3333',
                             command=self.destroy
                             )
        button_exit.grid(column=0, row=2)
        flag = BooleanVar(self)
        flag.set(True)
        self.resizable(False, False)
        while True:
            if flag.get():
                nilai = analog_suhu.read()
                # suhus = 5.0*100*nilai
                suhu = round(5.0*100*nilai, 2)
                rs = RotaryScale(self, 60, 200, unit=" °C",
                                 needle_color="blue")
                rs.grid(row=0, column=0)
                rs.set_value(suhu)
                rs.update()
                tanggal = datetime.datetime.now()
                formatwaktu = tanggal.hour, tanggal.minute, tanggal.second
                labels.config(text="pada waktu: %d:%d:%d" %
                              (formatwaktu), foreground="#f7f7f7",
                              bg="#232323")
                labels.update_idletasks()
                self.update()
                time.sleep(0.3)
                if suhu <= 30:
                    warning_label.config(
                        text="SUHU RUANGAN", foreground="#1ef98F", bg="#232323")
                    warning_label.update_idletasks()
                if suhu >= 30:
                    buzzer_pin.write(40)
                    waktu(0.2)
                    buzzer_pin.write(0)
                    warning_label.config(
                        text="WARN! SUHU DIATAS 30", foreground="#ff0000", bg="#232323")
                    warning_label.update()
            else:
                break

    def running(self):
        return True

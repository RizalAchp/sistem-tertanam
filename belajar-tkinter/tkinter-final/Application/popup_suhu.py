from tkinter import Toplevel, Label, BooleanVar, Button
from tk_tools.canvas import RotaryScale
from Application.arduino_config import *


class NewWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("225x300")
        labels = Label(self)
        labels.grid(column=0, row=1)
        button_exit = Button(self,
                             bg='#ff0000',
                             text="EXIT",
                             activebackground='#900000',
                             command=self.destroy
                             )
        button_exit.grid(column=0, row=2)
        flag = BooleanVar(self)
        flag.set(True)
        self.resizable(False, False)
        while True:
            if flag.get():
                nilai = analog_suhu.read()
                suhu = 5.0*100*nilai
                rs = RotaryScale(self, 100, 200, unit=" °C")
                rs.grid(row=0, column=0)
                rs.set_value(suhu)
                rs.update_idletasks()
                tanggal = datetime.datetime.now()
                formatwaktu = tanggal.hour, tanggal.minute, tanggal.second
                labels.config(text="pada waktu: %d:%d:%d" % (formatwaktu))
                labels.update_idletasks()
                self.update()
                time.sleep(0.3)
            else:
                break

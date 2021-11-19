#!/usr/bin/python3
import tkinter as tk
import pyfirmata as pyfir
from pyfirmata.util import Iterator
import time as tm

board = pyfir.Arduino('COM7')
it = Iterator(board)
it.start()
LM_35 = board.get_pin('a:1:i')

root = tk.Tk()
root.title("TKINTER SUHU LM35")
root.minsize(500, 100)


def suhu():
    nilai = LM_35.read()
    if nilai is not None:
        suhu = 5.0*100*nilai
        print(suhu)
        tk.Label(root, text=suhu).pack()


tombol_exit = tk.Button(root, text='EXIT', command=quit)
tombol_exit.pack(side=tk.RIGHT)

tombol_suhu = tk.Button(root, text='MUNCULKAN SUHU', command=suhu)
tombol_suhu.pack(side=tk.TOP)

root.mainloop()

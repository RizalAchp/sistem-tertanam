#!/bin/python3
import pyfirmata as pf
# import tkinter as tk
from tkinter import ttk as tk
from ttkthemes import ThemedTk
# import tkinter.tix as tk


def quit_button():
    global tkTop
    print('closing program, goodbye')
    for x in led_int:
        board.digital[x].write(0)
    tk_.destroy()


def led1_button():
    tk_label.setvar(value='LED1 ON')
    print('led1 hidup')
    board.digital[led1].write(1)


def led2_button():
    tk_label.setvar(value='LED2 ON')
    print('led2 hidup')
    board.digital[led2].write(1)


def led3_button():
    tk_label.setvar(value='LED3 ON')
    print('led3 hidup')
    board.digital[led3].write(1)


def led4_button():
    tk_label.setvar(value='Led4 Hidup')
    print('led4 hidup')
    board.digital[led4].write(1)


def special_button():
    tk_label.setvar('LED KEDIP')
    print('led pada variable int hidup berurutan')
    for x in led_int:
        board.digital[x].write(1)
        waktu(0.2)
        board.digital[x].write(0)
        waktu(0.2)


# ubah sesuai environment
# biasanya kalo windows itu 'USB...'
board = pf.Arduino('/dev/ttyACM0')
led1 = 6
led2 = 7
led3 = 8
led4 = 9
led_int = [led1, led2, led3, led4]
waktu = board.pass_time
# reset arduino saat pertama kali di jalankan
# board.digital[led_int].write(0)

# tk_ = tk.Tk()
tk_ = ThemedTk(theme="ubuntu")
tk_['bg'] = '#282a36'
tk_.geometry('300x300')
tk.Label(tk_,
         text="LED Control",
         width=30,
         )

# gabisa pake label, ntah kenapa, aneh
tk_label = tk.Label(tk_,
                    width=20,
                    )
tk_label.pack()
# button led1
btn1state = tk.Button(tk_,
                      text="LED1",
                      command=led1_button,
                      width=8,
                      )

btn1state.pack(side='top', ipadx=10, padx=10, pady=15)
# button led2
btn2state = tk.Button(tk_,
                      text="LED2",
                      command=led2_button,
                      width=8,
                      )
btn2state.pack(side='top', ipadx=10, padx=10, pady=15)
# button led 3
btn3state = tk.Button(tk_,
                      text="LED3",
                      command=led3_button,
                      width=8,
                      )
btn3state.pack(side='top', ipadx=10, padx=10, pady=15)
# button led 4
btn4state = tk.Button(tk_,
                      text="LED4",
                      command=led4_button,
                      width=8,
                      )
btn4state.pack(side='top', ipadx=10, padx=10, pady=15)
# button special :v
btnspecialstate = tk.Button(tk_,
                            text="LED WALK",
                            command=special_button,
                            width=8,
                            )
btnspecialstate.pack(side='top', ipadx=10, padx=10, pady=15)
# button sesuai dengan nanamanya, iya quit =  keluar()
btnQuit = tk.Button(
    tk_,
    text="Quit",
    command=quit_button,
    width=8,
)
btnQuit.pack(side='bottom', ipadx=10, padx=10, pady=15)

tk_.mainloop()

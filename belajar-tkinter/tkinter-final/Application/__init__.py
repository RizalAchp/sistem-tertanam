#!/usr/bin/env python3
'''
info :
    file `__init__py` pada folder `Application` ini
    sebagai object utama class yang terpanggil oleh
    file `main.py` pada directory induk
'''

from Application import fun

if __name__ == '__main__':
    main_function = fun()
    main_function.run()

name = 'Tkinter-Rizal'

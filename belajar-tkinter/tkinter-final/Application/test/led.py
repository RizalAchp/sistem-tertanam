from tkinter import Button, Tk
from tk_tools import Led
root = Tk()


def ledtored():
    led.to_red(on=True)


led = Led(root, size=20)
led.pack()

led.to_red()
led.to_green(on=True)


button = Button(root,
                command=ledtored)
button.pack()
root.mainloop()

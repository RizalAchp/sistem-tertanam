import tkinter
import pyfirmata
from pyfirmata.util import Iterator


def onStartButtonPress():
    while True:
        if flag.get():
            analogReadLabel.config(text=str(a0.read()))
            analogReadLabel.update_idletasks()
            top.update()
        else:
            break
    board.exit()
    top.destroy()


def onExitButtonPress():
    flag.set(False)


port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)

it = Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')

top = tkinter.Tk()
top.title("Reading Analog pins")
top.geometry('400x400')

descriptionLabel = tkinter.Label(top, text="Potentiometer input:- ")
descriptionLabel.grid(column=1, row=1)

analogReadLabel = tkinter.Label(top, text="Press Start..")
analogReadLabel.grid(column=2, row=1)

flag = tkinter.BooleanVar(top)
flag.set(True)

startButton = tkinter.Button(top, text="Start", command=onStartButtonPress)
startButton.grid(column=1, row=2)

exitButton = tkinter.Button(top, text="Exit", command=onExitButtonPress)
exitButton.grid(column=2, row=2)

top.mainloop()

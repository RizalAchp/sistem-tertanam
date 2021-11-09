#!/usr/bin/python3
from func import *
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

# mendefinisikan tempat aset
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def quit_button():
    analog_buzz.write(0)
    for x in ledPin:
        board.digital[x].write(0)
    window.destroy()


# memulai window dengan beberapa konfigurasinya
window = Tk()
window.geometry("500x300")
window.configure(bg="#282A36")
canvas = Canvas(
    window,
    bg="#282A36",
    height=300,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
# memasukkan gambar pada canvas
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    321.0,
    150.0,
    image=image_image_1
)
# udah tau dari nama, ini tombol (button)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    background="#000000",
    activebackground="#f1f1f0",
    highlightthickness=0,
    command=quit_button,
    relief="raised"
)
button_1.place(
    x=39.0,
    y=235.0,
    width=76.0,
    height=27.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    background="#000000",
    activebackground="#f1f1f0",
    highlightthickness=0,
    command=sensor_sonic,
    relief="raised"
)
button_2.place(
    x=135.0,
    y=188.0,
    width=76.0,
    height=27.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    background="#000000",
    activebackground="#f1f1f0",
    highlightthickness=0,
    command=sensor_suhu,
    relief="raised"
)
button_3.place(
    x=39.0,
    y=188.0,
    width=76.0,
    height=27.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    activebackground="#f1f1f0",
    background="#000000",
    highlightthickness=0,
    command=buzzer,
    relief="raised"
)
button_4.place(
    x=135.0,
    y=141.0,
    width=76.0,
    height=27.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#f1f1f0",
    background="#000000",
    command=led_blink,
    relief="raised"
)
button_5.place(
    x=39.0,
    y=141.0,
    width=76.0,
    height=27.0
)

canvas.create_text(
    39.0,
    107.0,
    anchor="nw",
    text="Dibawah ini merupakan Tombol ajaib!",
    fill="#F1F1F0",
    font=("Ubuntu Regular", 12 * -1)
)

canvas.create_text(
    39.0,
    32.0,
    anchor="nw",
    text="HALO!\nSAYA RIZAL!",
    fill="#F1F1F0",
    font=("Ubuntu Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()

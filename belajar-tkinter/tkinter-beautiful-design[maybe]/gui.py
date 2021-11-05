from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    321.0,
    150.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    background="#000000",
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
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
    background="#000000",
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
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
    background="#000000",
    command=lambda: print("button_5 clicked"),
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
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, BooleanVar
from tkinter.constants import END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("300x400")
window.configure(bg="#232222")
flag = BooleanVar(window)
flag.set(True)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))

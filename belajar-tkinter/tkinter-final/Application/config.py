'''
info:
    pada file config ini, saya menconfigurasikan semua komponen
    maupun widget pada gui, agar mudah untuk di akses
    dan lebih rapi.
'''

from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, BooleanVar
from tkinter.constants import END, INSERT
from tk_tools import Led

# variable string ``Path`` assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")

running = True


def relative_to_assets(path: str) -> Path:
    """relative_to_assets : function string
        Kegunaan:
            ,hanya sebagai string untuk menentukan lokasi assets
            widget yang digunakan, seperti halnya ``canvas``
            dan lainnya.
    """
    return ASSETS_PATH / Path(path)


"""
    memulai window utama pada ``tkinter``
    dan setting ukuran maupun warna background
    menggunakan ``_geometry`` dan ``_configure'' pada window
"""
window = Tk()
window.geometry("300x400")
window.configure(bg="#232222")
flag = BooleanVar(window)
flag.set(True)

# membuat variable dari function``relative_to_assets()``
# yang sudah  ditentukan
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
sonar_button_img = PhotoImage(
    file=relative_to_assets("sonic_button_img.png"))
suhu_button_img = PhotoImage(
    file=relative_to_assets("suhu_btn.png"))
start_button_img = PhotoImage(
    file=relative_to_assets("start_button_img.png"))
stop_button_img = PhotoImage(
    file=relative_to_assets("stop_button_img.png"))
buzzer_button_img = PhotoImage(
    file=relative_to_assets("buzzer_img.png"))
ledvar_button_img = PhotoImage(
    file=relative_to_assets("led_var_img.png"))
stop_loop_img = PhotoImage(
    file=relative_to_assets("stop_loop.png"))
led1_img = PhotoImage(
    file=relative_to_assets("button_7.png"))
led2_img = PhotoImage(
    file=relative_to_assets("button_8.png"))
led3_img = PhotoImage(
    file=relative_to_assets("button_9.png"))
led4_img = PhotoImage(
    file=relative_to_assets("button_10.png"))

# canvas
#   Menggunakan komponen ``Canvas`` agar dapat mengatur
#   warna maupun letak widget lainnya pada ``window`` utama.
canvas = Canvas(
    window,
    bg="#232222",
    height=400,
    width=300,
    bd=1,
    highlightthickness=1,
    relief="ridge"
)
canvas.place(x=0, y=0)

# entry_1
#   disini saya menggunakan ``Text`` sebagai widget
#   penampil kata Utama padda GUI.
entry_1 = Text(
    bd=2,
    bg="#F1F1F1",
    highlightthickness=0,
    font=("FreeMono", 14 * -1),
    state="normal"
)

entry_1.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=21.0,
    width=281.0,
    height=126.0
)

# entry_2
#   disini saya menggunakan ``Text`` sebagai widget
#   penampil kata Kedua dibawah widget ``Text`` Utama
entry_2 = Text(
    bd=0,
    bg="#F1F1F0",
    highlightthickness=0,
    font=("SourceCodePro-Bold", 16 * -1, "bold"),
    state="normal"
)
entry_2.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=158.0,
    width=281.0,
    height=24.0
)
# sonar_button
#   widget button untuk function sonar/hcsr04 pada ``fun.py``.
sonar_button = Button(
    image=sonar_button_img,
    borderwidth=0,
    bg="#ED5A6F",
    activebackground="#d35d6e",
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
sonar_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=342.0,
    width=97.0,
    height=30.0
)

# suhu_button
#   widget button untuk function ukur_suhu() pada ``fun.py``.
suhu_button = Button(
    image=suhu_button_img,
    borderwidth=0,
    bg="#ED5A6F",
    activebackground="#d35d6e",
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
suhu_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=297.0,
    width=97.0,
    height=30.0
)

# start_button
#   widget button untuk function start_buttonclicked()
#   pada ``fun.py``.
start_button = Button(
    image=start_button_img,
    borderwidth=0,
    highlightthickness=0,
    bg="#0075FF",
    activebackground="#133761",
    state="normal",
    relief="raised"
)
start_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=117.0,
    y=297.0,
    width=85.0,
    height=30.0
)

# stop_button
#   widget button untuk function stop() pada ``fun.py``.
stop_button = Button(
    image=stop_button_img,
    borderwidth=0,
    highlightthickness=0,
    bg="#FF0000",
    activebackground="#840303",
    state="normal",
    relief="raised"
)
stop_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=117.0,
    y=342.0,
    width=85.0,
    height=30.0
)

stop_loop_btn = Button(
    image=stop_loop_img,
    borderwidth=0,
    highlightthickness=0,
    bg="#232222",
    activebackground="#333333",
    state="disabled",
    relief="raised"
)
stop_loop_btn.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=117.0,
    y=207.0,
    width=85.0,
    height=75.0
)

buzzer_button = Button(
    image=buzzer_button_img,
    borderwidth=0,
    bg="#ED5A6F",
    activebackground="#d35d6e",
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
buzzer_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=252.0,
    width=97.0,
    height=30.0
)

led_var_button = Button(
    image=ledvar_button_img,
    borderwidth=0,
    bg="#ED5A6F",
    activebackground="#d35d6e",
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
led_var_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=9.0,
    y=207.0,
    width=97.0,
    height=30.0
)
led1_button = Button(
    image=led1_img,
    borderwidth=0,
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
led1_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=259.0,
    y=207.0,
    width=30.0,
    height=30.0
)
led1_widget = Led(canvas, size=20)
led1_widget.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=214.0,
    y=207.0,
    width=30.0,
    height=30.0,
)

led2_button = Button(
    image=led2_img,
    borderwidth=0,
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
led2_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=259.0,
    y=252.0,
    width=30.0,
    height=30.0
)

led2_widget = Led(canvas, size=20, toggle_on_click=True)
led2_widget.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=214.0,
    y=252.0,
    width=30.0,
    height=30.0
)

led3_button = Button(
    image=led3_img,
    borderwidth=0,
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
led3_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=259.0,
    y=297.0,
    width=30.0,
    height=30.0
)

led3_widget = Led(canvas, size=20, toggle_on_click=True)
led3_widget.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=214.0,
    y=297.0,
    width=30.0,
    height=30.0
)

led4_button = Button(
    image=led4_img,
    borderwidth=0,
    highlightthickness=0,
    state="disabled",
    relief="raised"
)
led4_button.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=259.0,
    y=342.0,
    width=30.0,
    height=30.0
)

led4_widget = Led(canvas,
                  size=20, toggle_on_click=True)
led4_widget.place(
    # menggunakan``_place`` sebagai penentu tempat widget
    # pada canvas
    x=214.0,
    y=342.0,
    width=30.0,
    height=30.0
)

# entry_bg_1 = canvas.create_image(
#     149.5,
#     85.0,
#     image=entry_image_1
# )

# entry_bg_2 = canvas.create_image(
#     149.5,
#     171.0,
#     image=entry_image_2
# )

# variable string kata yang akan ditamplkan pada ``entry_1``
start_kata = "\n\n==================================\n==================================\n======== SELAMAT DATANG :) =======\n==================================\n==================================\n"
led1_kata = "\n\nAnda mengaktifkan tombol led1,\nLED 1 akan berkedip satu kali\n"
led2_kata = "\n\nAnda mengaktifkan tombol led2,\nLED 2 akan berkedip satu kali\n"
led3_kata = "\n\nAnda mengaktifkan tombol led2,\nLED 3 akan berkedip satu kali\n"
led4_kata = "\n\nAnda mengaktifkan tombol led4,\nLED 4 akan berkedip satu kali\n"
ledvar_kata = "\n\nAnda mengaktifkan funsi tombol led_var, keempat led yang tervariable kan kedalam array akan berkedip berurutan."
buzzer_kata = "\n\nAnda mengaktifkan funsi tombol led_var, keempat led yang tervariable kan kedalam array akan berkedip berurutan."
stop_kata = "\n\n\n\n=Proses Dimatikan. SelamatTinggal=\n\n\n\n"
display = entry_1
display2 = entry_2

from pathlib import Path
from time import sleep
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.constants import END,  NORMAL
from pyfirmata import Arduino
from pyfirmata.util import Iterator
from datetime import datetime

# Menentukan Lokasi Asset Template
OUTPUT_PATH = Path(__file__).parent
# string full path, agar dapat di panggil setiap aset nya.
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def path_asset(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def starting():
    b1 = led_one
    b2 = led_two
    b3 = led_three
    b4 = led_four
    if b1["state"] == "disabled":
        b1["state"] = "normal"
    if b2["state"] == "disabled":
        b2["state"] = "normal"
    if b3["state"] == "disabled":
        b3["state"] = "normal"
    if b4["state"] == "disabled":
        b4["state"] = "normal"
    else:
        b1["state"] = "disabled"
        b2["state"] = "disabled"
        b3["state"] = "disabled"
        b4["state"] = "disabled"
    display = main_text_display
    display.insert(END, 'SELAMAT DATANG!\nDisini anda dapat melakukan banyak hal pada arduino dengan\nmenggunakan GUI!\n\t1. anda dapat menghidupkan LED satu persatu pada tombol\n\t   dengan icon LED dibagian kanan!\n\t2.anda juga dapat menggunakan tombol dibawahnya untuk\n\t   memulai fungsi2 pada sensor!\nDan banyak inputan2 yang dapat digunakan untuk fungsi\nyang akan dijalankan!')
    display.see(END)


def restart():
    display2 = second_text_display
    display2.insert(END, 'SELAMAT TINGGAL....\n')
    delay(1.0)
    # for x in ledVar:
    #     board.digital[x].write(0)
    window.destroy()


def led1():
    display2 = second_text_display
    display2.insert(END, '\nLED 1 HIDUP')
    display2.see(END)
    display = main_text_display
    display.insert(
        END, '\nANDA MENJALANKAN FUNGSI LED1\nLED1 AKAN BERKEDIP SEKALI.\n')
    display.see(END)
    led_1.write(1)
    delay(0.3)
    led_1.write(0)
    delay(0.3)
    led_one.config(state=NORMAL)


def led2():
    display2 = second_text_display
    display2.insert(END, '\nLED 2 HIDUP')
    display2.see(END)
    display = main_text_display
    display.insert(
        END, '\nANDA MENJALANKAN FUNSI LED2\nLED2 AKAN BERKEDIP SEKALI.\n')
    display.see(END)
    led_2.write(1)
    delay(0.3)
    led_2.write(0)
    delay(0.3)
    led_two.config(state=NORMAL)


def led3():
    display2 = second_text_display
    display2.insert(END, '\nLED 3 HIDUP')
    display2.see(END)
    display = main_text_display
    display.insert(
        END, '\nANDA MENJALANKAN FUNSI LED3\nLED3 AKAN BERKEDIP SEKALI.\n')
    display.see(END)
    led_3.write(1)
    delay(0.3)
    led_3.write(0)
    delay(0.3)
    led_three.config(state=NORMAL)


def led4():
    display2 = second_text_display
    display2.insert(END, '\nLED 4 HIDUP')
    display2.see(END)
    display = main_text_display
    display.insert(
        END, '\nANDA MENJALANKAN FUNSI LED4\nLED4 AKAN BERKEDIP SEKALI,\n')
    display.see(END)
    led_4.write(1)
    delay(0.3)
    led_4.write(0)
    delay(0.3)
    led_four.config(state=NORMAL)


def led_var():
    for x in ledVar:
        board.digital[x].write(1)
        print('led ', x, ' hidup')
        delay(0.3)
        board.digital[x].write(0)
        print('led ', x, ' mati')
        delay(0.3)
    led_four.config(state=NORMAL)


def buzzer():
    print('buzzer berbunyi')
    buzz.write(0.2)
    board.pass_time(0.5)
    buzz.write(0.6)
    board.pass_time(0.5)
    buzz.write(0.8)
    board.pass_time(0.5)
    buzz.write(0)
    board.pass_time(0.5)
    led_four.config(state=NORMAL)


def ukur_suhu():
    nilai = pin_suhu.read()
    if nilai is not None:
        delay(4)
        suhu = 5.0*100*nilai
        format_tgl = tgl.hour,\
            tgl.minute, tgl.second
        print('suhu ruangan pada ', '%d:%d:%d'
              % (format_tgl), ' adalah', suhu, ' celcius')

# TODO make function for ultrasonic sensor


def sensor_sonic():
    print('menyusul')


board = Arduino('/dev/ttyACM0')
it = Iterator(board)
delay = sleep
tgl = datetime.now()
ledVar = [6, 7, 8, 9]
led_1 = board.digital[6]
led_2 = board.digital[7]
led_3 = board.digital[8]
led_4 = board.digital[9]
pin_suhu = board.get_pin('a:1:i')
buzz = board.get_pin('d:5:p')
it.start()

window = Tk()
window.geometry("620x641")
window.configure(bg="#7C7C7C")

canvas = Canvas(
    window,
    bg="#7C7C7C",
    height=641,
    width=620,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    333.0,
    620.0,
    641.0,
    fill="#FFFFFF",
    outline="")

main_text_display_image_1 = PhotoImage(
    file=path_asset("entry_1.png"))
entry_bg_1 = canvas.create_image(
    310.0,
    155.0,
    image=main_text_display_image_1
)
main_text_display = Text(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0,
    font=("mononokiNerdFontComplete Regular", 14 * -1)
)
main_text_display.place(
    x=59.0,
    y=70.0,
    width=502.0,
    height=160.0
)

entry_image_2 = PhotoImage(
    file=path_asset("entry_2.png"))
entry_bg_2 = canvas.create_image(
    186.0,
    291.0,
    image=entry_image_2
)
second_text_display = Text(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0,
    font=("mononokiNerdFontComplete Regular", 16 * -1)
)
second_text_display.place(
    x=59.0,
    y=280.0,
    width=254.0,
    height=20.0
)

entry_image_3 = PhotoImage(
    file=path_asset("entry_3.png"))
entry_bg_3 = canvas.create_image(
    229.5,
    543.5,
    image=entry_image_3
)
value_delay = Entry(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0
)
value_delay.place(
    x=166.0,
    y=524.0,
    width=127.0,
    height=40.0
)

entry_image_4 = PhotoImage(
    file=path_asset("entry_4.png"))
entry_bg_4 = canvas.create_image(
    229.5,
    472.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0
)
entry_4.place(
    x=166.0,
    y=453.0,
    width=127.0,
    height=40.0
)

entry_image_5 = PhotoImage(
    file=path_asset("entry_5.png"))
entry_bg_5 = canvas.create_image(
    229.5,
    402.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F9F9F9",
    highlightthickness=0
)
entry_5.place(
    x=166.0,
    y=383.0,
    width=127.0,
    height=40.0
)

button_image_1 = PhotoImage(
    file=path_asset("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=restart,
    relief="raised"
)
button_1.place(
    x=465.0,
    y=265.0,
    width=111.0,
    height=52.0
)

button_image_2 = PhotoImage(
    file=path_asset("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=starting,
    relief="raised"
)
button_2.place(
    x=341.0,
    y=265.0,
    width=111.0,
    height=52.0
)

button_image_3 = PhotoImage(
    file=path_asset("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="raised"
)
button_3.place(
    x=465.3874816894531,
    y=520.7470703125,
    width=110.61251831054688,
    height=44.918792724609375
)

button_image_4 = PhotoImage(
    file=path_asset("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="raised"
)
button_4.place(
    x=334.0,
    y=520.7470703125,
    width=112.0,
    height=44.918792724609375
)

button_image_5 = PhotoImage(
    file=path_asset("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="raised"
)
button_5.place(
    x=464.0,
    y=450.0,
    width=112.0,
    height=44.918792724609375
)

button_image_6 = PhotoImage(
    file=path_asset("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="raised"
)
button_6.place(
    x=334.0,
    y=450.0,
    width=112.0,
    height=44.918792724609375
)

button_image_7 = PhotoImage(
    file=path_asset("led_four.png"))
led_four = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=led4,
    state="disabled",
    relief="raised"
)
led_four.place(
    x=529.218505859375,
    y=380.0,
    width=46.45660400390625,
    height=44.918792724609375
)

button_image_8 = PhotoImage(
    file=path_asset("led_three.png"))
led_three = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=led3,
    state="disabled",
    relief="raised"
)
led_three.place(
    x=464.14569091796875,
    y=380.0,
    width=46.45660400390625,
    height=44.918792724609375
)

button_image_9 = PhotoImage(
    file=path_asset("led_two.png"))
led_two = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=led2,
    state="disabled",
    relief="raised"
)
led_two.place(
    x=399.0728454589844,
    y=380.0,
    width=46.45660400390625,
    height=44.918792724609375
)

button_image_10 = PhotoImage(
    file=path_asset("led_one.png"))
led_one = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=led1,
    activebackground="#f1f1f0",
    highlightbackground="#FFFFFF",
    state="disabled",
    relief="raised"
)
led_one.place(
    x=334.0,
    y=380.0,
    width=46.45660400390625,
    height=44.918792724609375
)

canvas.create_text(
    42.0,
    393.0,
    anchor="nw",
    text="Input Delay >",
    fill="#000000",
    font=("mononokiNerdFontComplete Regular", 14 * -1)
)

canvas.create_text(
    44.0,
    463.0,
    anchor="nw",
    text="Input Text > ",
    fill="#000000",
    font=("mononokiNerdFontComplete Regular", 14 * -1)
)

canvas.create_text(
    44.0,
    534.0,
    anchor="nw",
    text="Input Nama >",
    fill="#000000",
    font=("mononokiNerdFontComplete  Regular", 14 * -1)
)

canvas.create_text(
    142.0,
    15.0,
    anchor="nw",
    text="Run Arduino With GUI",
    fill="#F9F9F9",
    font=("mononokiNerdFontComplete Bold", 28 * -1)
)

canvas.create_text(
    145.0,
    600.0,
    anchor="nw",
    text="Design And Created By Rizal Achmad Pahlevi",
    fill="#7C7C7C",
    font=("mononokiNerdFontComplete Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()

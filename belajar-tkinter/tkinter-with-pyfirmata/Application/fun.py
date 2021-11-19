#!/usr/bin/python3
from Application.arduino_config import *
from Application.note_music import *
from Application.config import *


def start_buttonclicked():
    # toggle tombol
    if led1_button["state"] == "disabled":
        led1_button["state"] = "normal"
    if led2_button["state"] == "disabled":
        led2_button["state"] = "normal"
    if led3_button["state"] == "disabled":
        led3_button["state"] = "normal"
    if led4_button["state"] == "disabled":
        led4_button["state"] = "normal"
    if led_var_button["state"] == "disabled":
        led_var_button["state"] = "normal"
    if suhu_button["state"] == "disabled":
        suhu_button["state"] = "normal"
    if buzzer_button["state"] == "disabled":
        buzzer_button["state"] = "normal"
    if sonar_button["state"] == "disabled":
        sonar_button["state"] = "normal"
    if stop_button["state"] == "disabled":
        stop_button["state"] = "normal"
    else:
        led1_button["state"] = "disabled"
        led2_button["state"] = "disabled"
        led3_button["state"] = "disabled"
        led4_button["state"] = "disabled"
        led_var_button["state"] = "disabled"
        suhu_button["state"] = "disabled"
        sonar_button["state"] = "disabled"
        buzzer_button["state"] = "disabled"
        stop_button["state"] = "disabled"

# func led1


def led1_blink():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led1, LED1 akan berkedip satu kali.')
    display.see(END)
    display2.insert(END, '\nled1 pada pin %s , hidup' % (ledPin[0]))
    display2.see(END)
    board.digital[ledPin[0]].write(1)
    board.pass_time(0.3)
    board.digital[ledPin[0]].write(0)

# func led2


def led2_blink():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led2, LED2 akan berkedip satu kali.')
    display.see(END)
    display2.insert(END, '\nled1 pada pin %s , hidup' % (ledPin[1]))
    display2.see(END)
    board.digital[ledPin[1]].write(1)
    board.pass_time(0.3)
    board.digital[ledPin[1]].write(0)

# func led3


def led3_blink():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led3, LED3 akan berkedip satu kali.')
    display.see(END)
    display2.insert(END, '\nled1 pada pin %s , hidup' % (ledPin[2]))
    display2.see(END)
    board.digital[ledPin[2]].write(1)
    board.pass_time(0.3)
    board.digital[ledPin[2]].write(0)

# func led4


def led4_blink():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led4, LED4 akan berkedip satu kali.')
    display.see(END)
    display2.insert(END, '\nled1 pada pin %s , hidup' % (ledPin[3]))
    display2.see(END)
    board.digital[ledPin[3]].write(1)
    board.pass_time(0.3)
    board.digital[ledPin[3]].write(0)

# func led berjalan bergantian


def led_var():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led_var, keempat led yang tervariable kan kedalam array akan berkedip berurutan.')
    display.see(END)
    for x in ledPin:
        board.digital[x].write(1)
        board.pass_time(0.3)
        board.digital[x].write(0)
        board.pass_time(0.3)
        if flag.get():
            display.insert(
                END, '\nLed pada Pin %s, hidup berurutan sesuai array' % (x))
            display.see(END)
            display.update_idletasks()
            display2.insert(
                END, '\nledpin %s,hidup' % (x))
            display2.see(END)
            display2.update_idletasks()
            window.update()
        else:
            break


def buzzer():
    display.insert(
        END, '\n\nAnda mengaktifkan funsi tombol led_var, keempat led yang tervariable kan kedalam array akan berkedip berurutan.')
    display.see(END)
    for x, (durasi, freq) in enumerate(zip(note_len, note_freq)):
        buzzer_pin.write(freq)
        board.pass_time(durasi)
        buzzer_pin.write(0)
        board.pass_time(durasi)

        if flag.get():
            display.insert(
                END, '\nBuzzer Berbunyi pada nilai = %s' % (freq), ' sesuai array lagu')
            display.see(END)
            display.update_idletasks()
            display2.insert(
                END, '\nnilai freq buzzer= '"%d" % (freq))
            display2.see(END)
            display2.update_idletasks()
            window.update()
        else:
            break


def sensor_suhu():
    while True:
        if flag.get():
            nilai = analog_suhu.read()
            tanggal = datetime.datetime.now()
            waktu(1)
            suhu = 5.0*100*nilai
            format_waktu = tanggal.hour, tanggal.minute, tanggal.second
            display.insert(
                END, '\n\nsuhu ruangan pada %d:%d:%d' % (format_waktu))
            display.see(END)
            display.update_idletasks()
            display2.insert(
                END, '\nsuhu didapat= %.2f °C' % (suhu))
            display2.see(END)
            display2.update_idletasks()
            window.update()
        else:
            break


def sensor_sonic():
    print("gatau caranya kalo di pyfirmata")
    display.insert(
        END, '\n\nGatau Carannya, Setelah Mencari2 referensi maupun dokumentasi pyfirmata, tidak menemukan jalan.')
    display.see(END)


def stop():
    display.insert(
        END, '\n\nProses Dimatikan.. Selamat Tinggal')
    display.see(END)
    display2.insert(
        END, '\nSYSTEM SHUTDOWN...')
    display2.see(END)
    waktu(2.0)
    board.exit()
    window.destroy()


canvas = Canvas(
    window,
    bg="#232222",
    height=400,
    width=300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
entry_1 = Text(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0,
    font=("SourceCodePro-Regular", 14 * -1),
    state="normal"
)
entry_1.place(
    x=9.0,
    y=21.0,
    width=281.0,
    height=126.0
)
entry_2 = Text(
    bd=0,
    bg="#F1F1F0",
    highlightthickness=0,
    font=("SourceCodePro-Regular", 16 * -1),
    state="normal"
)

entry_2.place(
    x=9.0,
    y=158.0,
    width=281.0,
    height=24.0
)

# canvas.create_rectangle(
#     214.0,
#     342.0,
#     244.0,
#     372.0,
#     fill="#232323",
#     outline="")

# canvas.create_rectangle(
#     214.0,
#     297.0,
#     244.0,
#     327.0,
#     fill="#232323",
#     outline="")

# canvas.create_rectangle(
#     214.0,
#     252.0,
#     244.0,
#     282.0,
#     fill="#232323",
#     outline="")

# canvas.create_rectangle(
#     214.0,
#     207.0,
#     244.0,
#     237.0,
#     fill="#232323",
#     outline="")

# canvas.create_rectangle(
#     117.0,
#     197.0,
#     202.0,
#     282.0,
#     fill="#232323",
#     outline="")


sonar_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sensor_sonic,
    state="disabled",
    relief="raised"
)

suhu_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sensor_suhu,
    state="disabled",
    relief="raised"
)


start_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=start_buttonclicked,
    state="normal",
    relief="raised"
)
stop_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=stop,
    state="disabled",
    relief="raised"
)
buzzer_button = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=buzzer,
    state="disabled",
    relief="raised"
)
led_var_button = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=led_var,
    state="disabled",
    relief="raised"
)
led1_button = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=led1_blink,
    state="disabled",
    relief="raised"
)
led2_button = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=led2_blink,
    state="disabled",
    relief="raised"
)
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
led3_button = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=led3_blink,
    state="disabled",
    relief="raised"
)
button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
led4_button = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=led4_blink,
    state="disabled",
    relief="raised"
)
sonar_button.place(
    x=9.0,
    y=342.0,
    width=97.0,
    height=30.0
)

suhu_button.place(
    x=9.0,
    y=297.0,
    width=97.0,
    height=30.0
)

start_button.place(
    x=117.0,
    y=297.0,
    width=85.0,
    height=30.0
)

stop_button.place(
    x=117.0,
    y=342.0,
    width=85.0,
    height=30.0
)

buzzer_button.place(
    x=9.0,
    y=252.0,
    width=97.0,
    height=30.0
)

led_var_button.place(
    x=9.0,
    y=207.0,
    width=97.0,
    height=30.0
)

led1_button.place(
    x=259.0,
    y=207.0,
    width=30.0,
    height=30.0
)

led2_button.place(
    x=259.0,
    y=252.0,
    width=30.0,
    height=30.0
)

led3_button.place(
    x=259.0,
    y=297.0,
    width=30.0,
    height=30.0
)

led4_button.place(
    x=259.0,
    y=342.0,
    width=30.0,
    height=30.0
)


entry_bg_1 = canvas.create_image(
    149.5,
    85.0,
    image=entry_image_1
)

entry_bg_2 = canvas.create_image(
    149.5,
    171.0,
    image=entry_image_2
)

display = entry_1
display2 = entry_2
window.resizable(False, False)
window.mainloop()

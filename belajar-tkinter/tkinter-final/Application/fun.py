#!/usr/bin/python3
from tkinter.constants import INSERT
from Application.arduino_config import *
from Application.note_music import *
from Application.config import *

from Application import popup_suhu


def start_text():
    display.config(foreground="#0000ff")
    display.insert(
        END, start_kata)
    display.see(END)
    display2.config(foreground="#0000ff")
    display2.insert(
        INSERT, '\n\n ➥ CLICK START AND ENJOY!')
    display2.see(INSERT)


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
    if stop_loop_btn["state"] == "disabled":
        stop_loop_btn["state"] = "normal"
    else:
        led1_button["state"] = "disabled"
        led2_button["state"] = "disabled"
        led3_button["state"] = "disabled"
        led4_button["state"] = "disabled"
        led_var_button["state"] = "disabled"
        suhu_button["state"] = "disabled"
        sonar_button["state"] = "disabled"
        buzzer_button["state"] = "disabled"
        stop_loop_btn["state"] = "disabled"


def led1_blink():
    # func led1
    global running
    running = True
    if flag.get() and running:
        led1_widget.to_green(on=True)
        display.config(foreground="black")
        display.insert(
            END, led1_kata)
        display.see(END)
        display2.config(foreground="#0000ff")
        display2.insert(
            INSERT, '\n\n➥ led1 pada pin %s , hidup' % (ledPin[0]))
        display2.see(INSERT)
        display.update_idletasks()
        display2.update_idletasks()
        board.digital[ledPin[0]].write(1)
        waktu(0.5)
        board.digital[ledPin[0]].write(0)
        led1_widget.to_grey(on=True)
        led1_widget.update_idletasks
        window.update()
    else:
        return


def led2_blink():
    # func led2
    global running
    running = True
    if flag.get() and running:
        led2_widget.to_green(on=True)
        display.config(foreground="black")
        display.insert(
            END, led2_kata)
        display.see(END)
        display2.config(foreground="#0000ff")
        display2.insert(END, '\n\n ➥ led1 pada pin %s , hidup' % (ledPin[1]))
        display2.see(END)
        display.update_idletasks()
        display2.update_idletasks()
        board.digital[ledPin[1]].write(1)
        board.pass_time(0.5)
        board.digital[ledPin[1]].write(0)
        led2_widget.to_grey(on=True)
        led2_widget.update_idletasks
        window.update()
    else:
        return


def led3_blink():
    # func led3
    global running
    running = True
    if flag.get() and running:
        led3_widget.to_green(on=True)
        display.config(foreground="black")
        display.insert(
            END, led3_kata)
        display.see(END)
        display2.config(foreground="#0000ff")
        display2.insert(END, '\n\n ➥ led1 pada pin %s , hidup' % (ledPin[2]))
        display2.see(END)
        display.update_idletasks()
        display2.update_idletasks()
        board.digital[ledPin[1]].write(1)
        board.pass_time(0.5)
        board.digital[ledPin[1]].write(0)
        led3_widget.to_grey(on=True)
        led3_widget.update_idletasks
        window.update()
    else:
        return


def led4_blink():
    # func led4
    global running
    running = True
    if flag.get() and running:
        led4_widget.to_green(on=True)
        display.config(foreground="black")
        display.insert(
            END, led4_kata)
        display.see(END)
        display2.config(foreground="#0000ff")
        display2.insert(END, '\n\n ➥ led1 pada pin %s , hidup' % (ledPin[3]))
        display2.see(END)
        display.update_idletasks()
        display2.update_idletasks()
        board.digital[ledPin[1]].write(1)
        board.pass_time(0.5)
        board.digital[ledPin[1]].write(0)
        led4_widget.to_grey(on=True)
        led4_widget.update_idletasks
        window.update()
    else:
        return


def led_var():
    # func led berjalan bergantian
    display.config(foreground="black")
    global running
    display.insert(
        END, ledvar_kata)
    display.see(END)
    display2.config(foreground="#0000ff")
    running = True
    while running:
        for x in ledPin:
            board.digital[x].write(1)
            board.pass_time(0.3)
            board.digital[x].write(0)
            board.pass_time(0.3)
            display.insert(
                END, '\n\nLed pada Pin %s, hidup berurutan sesuai array' % (x))
            display.see(END)
            display.update_idletasks()
            display2.insert(
                END, '\n\n ➥ ledpin %s,hidup' % (x))
            display2.see(END)
            display2.update_idletasks()
            window.update()


def buzzer():
    global running
    display.config(foreground="black")
    display.insert(
        END, buzzer_kata)
    display.see(END)
    display2.config(foreground="#0000ff")
    running = True
    for x, (durasi, freq) in enumerate(zip(note_len, note_freq)):
        buzzer_pin.write(freq)
        board.pass_time(durasi)
        buzzer_pin.write(0)
        board.pass_time(durasi)
        if flag.get() and running:
            display.insert(
                END, '\nBuzzer Berbunyi pada nilai = %s' % (freq), ' sesuai array lagu')
            display.see(END)
            display.update_idletasks()
            display2.insert(
                END, '\n\n ➥ nilai freq buzzer= '"%d" % (freq))
            display2.see(END)
            display2.update_idletasks()
            window.update()
        else:
            break


def sensor_suhu():
    popup_suhu.NewWindow()
    # while True:
    #     if flag.get() and running:
    #         nilai = analog_suhu.read()
    #         tanggal = datetime.datetime.now()
    #         waktu(1)
    #         suhu = 5.0*100*nilai
    #         format_waktu = tanggal.hour, tanggal.minute, tanggal.second
    #         display.insert(
    #             END, '\n\nsuhu ruangan pada %d:%d:%d' % (format_waktu))
    #         display.see(END)
    #         display.update_idletasks()
    #         display2.insert(
    #             END, '\nsuhu didapat= %.2f °C' % (suhu))
    #         display2.see(END)
    #         display2.update_idletasks()
    #         window.update()
    #     else:
    #         break


def sensor_sonic():
    print("gatau caranya kalo di pyfirmata")
    display.config(foreground="#ff0000")
    display.insert(
        END, '\n\nGatau Carannya, Setelah Mencari2 referensi maupun dokumentasi pyfirmata, tidak menemukan jalan.')
    display.see(END)


def stop():
    display.config(foreground="#FF0000")
    display2.config(foreground="#ff0000")
    display.insert(
        END, stop_kata)
    display.see(END)
    display.update_idletasks()
    display2.insert(
        END, '\n ➥ SYSTEM SHUTDOWN...')
    display2.see(END)
    display2.update_idletasks()
    waktu(1.0)
    window.after(3000, func=shutdowns())


def stop_loop():
    # flag.set(False)
    global running
    display.config(foreground="#FF0000")
    display2.config(foreground="#ff0000")
    display.insert(
        END, "\n\n\n\n====== SELAMAT TINGGAL LOOP ======\n\n\n\n")
    display.see(END)
    display.update_idletasks()
    display2.insert(
        END, '\n\n ➥ LOOP STOPPED')
    display2.see(END)
    display2.update_idletasks()
    running = False
    waktu(1)


def shutdowns():
    board.exit()
    window.destroy()


start_text()

sonar_button['command'] = sensor_sonic
suhu_button['command'] = sensor_suhu
start_button['command'] = start_buttonclicked
stop_button['command'] = stop
stop_loop_btn['command'] = stop_loop
buzzer_button['command'] = buzzer
led_var_button['command'] = led_var
led1_button['command'] = led1_blink
# led1_widget.to_green(on=False)
led2_button['command'] = led2_blink
# led2_widget.to_green(on=False)
led3_button['command'] = led3_blink
# led3_widget.to_green(on=False)
led4_button['command'] = led4_blink
# led4_widget.to_green(on=False)

window.resizable(False, False)
window.mainloop()

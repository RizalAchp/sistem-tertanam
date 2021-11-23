from classes.note_music import *
from classes.config import *
from classes.arduino import *
from classes.gui import *

from classes.popup_suhu import suhuWindow


def togle():
    for tombol in tombols:
        if tombol['state'] == 'disabled':
            tombol['state'] = 'normal'
        else:
            tombol['state'] = 'disabled'


def starting():
    global running
    running = False

    second_text_display.insert(END, kata_starting)
    second_text_display.see(END)
    main_text_display.insert(END, kata_start)
    main_text_display.see(END)
    togle()


def led1():
    second_text_display.insert(END, kata_led1_kedua)
    second_text_display.see(END)
    main_text_display.insert(
        END, kata_led1_utama)
    main_text_display.see(END)
    board.digital_write(led_string[0], 1)
    delay(1.0)
    board.digital_write(led_string[0], 0)


def led2():
    second_text_display.insert(END, kata_led2_kedua)
    second_text_display.see(END)
    main_text_display.insert(
        END, kata_led2_utama)
    main_text_display.see(END)
    board.digital_write(led_string[1], 1)
    delay(1.0)
    board.digital_write(led_string[1], 0)


def led3():
    second_text_display.insert(END, kata_led3_kedua)
    second_text_display.see(END)
    main_text_display.insert(
        END, kata_led3_utama)
    main_text_display.see(END)
    board.digital_write(led_string[2], 1)
    delay(1.0)
    board.digital_write(led_string[2], 0)


def led4():
    second_text_display.insert(END, kata_led4_kedua)
    second_text_display.see(END)
    main_text_display.insert(
        END, kata_led4_kedua)
    main_text_display.see(END)
    board.digital_write(led_string[3], 1)
    delay(1.0)
    board.digital_write(led_string[3], 0)


def led_var():
    global running
    running = True
    while running:
        for leds in led_string:
            board.digital_write(leds, 1)
            delay(0.5)
            board.digital_write(leds, 0)
            delay(0.3)
        else:
            break


def buzzer():
    global running
    running = True
    if running:
        for durasi, freq in zip(note_len, note_freq):
            board.play_tone(buzzer_pin, freq, durasi*0.9)
            ketukan = float(durasi/1000)
            delay(ketukan)
            board.play_tone_off(buzzer_pin)
            print(freq, ' hz')
            second_text_display.insert(END, kata_buzzer_kedua % freq)
            second_text_display.see(END)
            second_text_display.update_idletasks()
            main_text_display.insert(
                END, kata_buzzer_utama % freq)
            main_text_display.see(END)
            window.update()
        else:
            return


def ukur_suhu():
    global running
    running = True
    while running:
        try:
            waktu = datetime.now()
            format_waktu = waktu.hour, waktu.minute, waktu.second
            datasuhu = board.analog_read(lm35_pin)
            suhu = 5.0*datasuhu[0]/10.23
            second_text_display.insert(END, kata_suhu_kedua % (suhu))
            second_text_display.see(END)
            second_text_display.update_idletasks()
            main_text_display.insert(
                END, kata_suhu_utama % (suhu))
            main_text_display.insert(END,
                                     "\npada: %d:%d:%d" % (format_waktu))
            main_text_display.see(END)
            main_text_display.update_idletasks()
            window.update()
            delay(1.0)
        except:
            break


def hcsr_call():
    # define trigger dan echo pin pada hcsr04
    global running
    running = True
    suhuWindow()
    # loop
    while running:
        try:
            delay(1)
            baca_jarak = board.sonar_read(trigpin)
            jarak = baca_jarak[0]
            main_text_display.insert(END, kata_jarak_utama % (jarak))
            main_text_display.see(END)
            main_text_display.update_idletasks()
            second_text_display.insert(END, kata_jarak_kedua % (jarak))
            second_text_display.see(END)
            second_text_display.update_idletasks()
            window.update()
            delay(1.0)
        except:
            break


def restart():
    second_text_display.insert(END, kata_restart)
    second_text_display.see(END)
    second_text_display.update_idletasks()
    window.update()
    window.after(2000, func=exiting())


def exiting():
    global running
    running = False
    board.shutdown()
    window.destroy()


tombols = [
    led_one, led_two, led_three, led_four, led_var_button,
    buzzer_button, lm35_button, hcsr04_button
]


led_one['command'] = led1
led_two['command'] = led2
led_three['command'] = led3
led_four['command'] = led4
led_var_button['command'] = led_var
buzzer_button['command'] = buzzer
lm35_button['command'] = ukur_suhu
start_button['command'] = starting
hcsr04_button['command'] = hcsr_call
exit_button['command'] = exiting

window.resizable(False, False)
window.mainloop()

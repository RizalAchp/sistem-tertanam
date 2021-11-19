#!/usr/bin/python3
from pymata4.pymata4 import Pymata4
from classes.note_music import *
import time

board = Pymata4('/dev/ttyACM0')


def pin_led_1():
    led_var = [6, 7, 8, 9]
    board.set_pin_mode_digital_output(led_var[0])
    board.digital_write(led_var[0], 1)
    time.sleep(0.5)
    board.digital_write(led_var[0], 0)


def pin_led_2():
    led_var = [6, 7, 8, 9]
    board.set_pin_mode_digital_output(led_var[1])
    board.digital_write(led_var[1], 1)
    time.sleep(0.5)
    board.digital_write(led_var[1], 0)


def pin_led_3():
    led_var = [6, 7, 8, 9]
    board.set_pin_mode_digital_output(led_var[2])
    board.digital_write(led_var[2], 1)
    time.sleep(0.5)
    board.digital_write(led_var[2], 0)


def pin_led_4():
    led_var = [6, 7, 8, 9]
    board.set_pin_mode_digital_output(led_var[3])
    board.digital_write(led_var[3], 1)
    time.sleep(0.5)
    board.digital_write(led_var[3], 0)


def pin_led_var():
    led_var = [6, 7, 8, 9]
    for i in led_var:
        board.set_pin_mode_digital_output(i)
        board.digital_write(i, 1)
        time.sleep(0.5)
        board.digital_write(i, 0)


def buzzer_fun():
    buzzer_pin = 5
    board.set_pin_mode_tone(buzzer_pin)
    for durasi in note_len:
        for freq in note_freq:
            board.play_tone(buzzer_pin, freq, durasi)
            waktu = float(durasi/1000*0.9)
            time.sleep(waktu)
            board.play_tone_off(buzzer_pin)
            print(freq, ' hz')


def callback_lm35(data):
    data_suhu = data[2]
    suhu = 5.0*data_suhu/10.23
    print(suhu, ' derajat celcius')


def lm35_fun():
    lm35_pin = 1
    board.set_pin_mode_analog_input(lm35_pin, callback_lm35)
    try:
        board.analog_read(lm35_pin)
    except Exception:
        mati()


def call_back_sonar(data):
    # mendapatkan data bacaan sensor hcsr04
    data_pin = data[1]
    data_jarak = data[2]
    print('jarak: ', data_jarak, 'pada pin ', data_pin)


def hcsr04_fun():
    # define trigger dan echo pin pada hcsr04
    trig_pin = 12
    echo_pin = 11
    board.set_pin_mode_sonar(trig_pin, echo_pin, call_back_sonar)
    # loop
    while True:
        try:
            time.sleep(1)
            board.sonar_read(trig_pin)
        except Exception:
            mati()


def starting_again():
    board.start()


def mati():
    board.sleep_tune
    board.shutdown()
    board.shutdown_on_exception

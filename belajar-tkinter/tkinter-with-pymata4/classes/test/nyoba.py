from pymata4.pymata4 import Pymata4
from time import sleep
from dataclasses import dataclass

# def ukur_suhu():
#     sleep(2.0)
#     bacaan_suhu = board.analog_read(lm35_pin)
#     suhu_data = bacaan_suhu[0]
#     suhus = int(5.0*suhu_data/10.23)
#     return nilai_suhu(suhus)


# def ukur_jarak():
#     sleep(2.0)
#     bacaan_jarak = board.sonar_read(trigpin)
#     jaraks = bacaan_jarak[0]
#     return nilai_jarak(jaraks)

# def nilai_suhu(suhu):
#     print(suhu)


def nilai_jarak(jarak):
    print(jarak)


@dataclass
class Ukur:
    nilai_suhu: int
    nilai_jarak: int

    # def suhu(self) -> int:
    #     return self.nilai_suhu

    # def jarak(self) -> int:
    #     return self.nilai_jarak
    def data(self) -> list:
        return [self.nilai_suhu, self.nilai_jarak]


running = True
board = Pymata4('/dev/ttyACM0')
lm35_pin = 1
trigpin = 11
echopin = 12
board.set_pin_mode_analog_input(lm35_pin)
board.set_pin_mode_sonar(trigger_pin=trigpin,
                         echo_pin=echopin)
while running:
    try:
        sleep(1.0)
        bacaan_jarak = board.sonar_read(trigpin)
        bacaan_suhu = board.analog_read(lm35_pin)
        suhu = int(5.0*bacaan_suhu[0]/10.23)
        jarak = int(bacaan_jarak[0])
        data_sensor = Ukur(suhu, jarak)
        # x = data_sensor.suhu(), data_sensor.jarak()
        x = data_sensor.data()
        print(x[0], x[1])
        print(type(x))
    except KeyboardInterrupt:
        break

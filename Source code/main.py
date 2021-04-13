import machine
import utime
import hcsr04
import random

# Zdefiniowanie pinów, do których są podłączone są piny sterujące silnikami

M1A=machine.Pin(18)
M1B=machine.Pin(19)
M2A=machine.Pin(20)
M2B=machine.Pin(21)

# Zdefiniowanie pinu przycisku

buttonA=machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)
buttonB=machine.Pin(28,machine.Pin.IN,machine.Pin.PULL_DOWN)

# Utworzenie obiektów PWM na zdefiniowanych pinach sterujących silników

pwm_M1A=machine.PWM(M1A)
pwm_M1B=machine.PWM(M1B)
pwm_M2A=machine.PWM(M2A)
pwm_M2B=machine.PWM(M2B)

# Ustalenie częstotliwości działania zdefiniowanych portów pwm

pwm_M1A.freq(500)
pwm_M1B.freq(500)
pwm_M2A.freq(500)
pwm_M2B.freq(500)

# Ustalenie startowej wartości sygnału na 0 na wszystkich pinach sterujących - 0V

pwm_M1A.duty_u16(0)
pwm_M1B.duty_u16(0)
pwm_M2A.duty_u16(0)
pwm_M2B.duty_u16(0)

# Utworzenie obiektu sensor (do obsługi czujnika HC-SR04) podłączonego na określonych pinach

sensor=hcsr04.HCSR04(trigger_pin=15,echo_pin=14,echo_timeout_us=1000000)

# Zdefiniowanie zmiennej o wartościach 0/1 oznaczjącej włączenie/wyłączenie robota

on=0

# Zdefiniowanie zmienne kontrolującej pwm, domyślny max_V: 26700 (1,5 V na silnik), ale eksperymentujemy

max_V=35000

# Zdefiniowanie zmiennej bezpiecznego dystansu od przeszkody

safe_distance=30.00000

# Zdefiniowanie funkcji kroczenia na przód, w tył i skrętów

def forward():
    pwm_M1A.duty_u16(max_V)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(max_V)
    pwm_M2B.duty_u16(0)
    
def backward():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(max_V)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(max_V)

def left_in_place():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(max_V)
    pwm_M2A.duty_u16(max_V)
    pwm_M2B.duty_u16(0)

def right_in_place():
    pwm_M1A.duty_u16(max_V)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(max_V)

def stop():
    pwm_M1A.duty_u16(0)
    pwm_M1B.duty_u16(0)
    pwm_M2A.duty_u16(0)
    pwm_M2B.duty_u16(0)

# Zdefiniowanie funkcji podającej odległość w cm

def distance():
    return sensor.distance_cm()

# tymczasowa funkcja sekwencji ruchu

def test_ruchu():
    forward()
    utime.sleep(6)
    left_in_place()
    utime.sleep(6)
    right_in_place()
    utime.sleep(6)
    backward()
    utime.sleep(6)

# Jazda z omijaniem przeszkód

def power_on():
    direction=random.randrange(2)
    if distance()>safe_distance:
        forward()
        print('Jadę do przodu')
        utime.sleep(0.5)
    else:
        stop()
        print("Przede mną przeszkoda")
        backward()
        print('Cofam')
        utime.sleep(2.0)
        stop()
        if direction==0:
            right_in_place()
            print('Skręcam w prawo')
            utime.sleep(2.0)
            stop()
        else:
            left_in_place()
            print('Skręcam w lewo')
            utime.sleep(2.0)
            stop()

# Instrukcje wykonywane tylko 1 raz podczas startu    

print('Włączono zasilanie')

# Główna pętla programu

while True: 
    if buttonA.value()==1:
        on=1
        print('Jestem uruchomiony')
        utime.sleep(0.1)
    if buttonB.value()==1:
        stop()
        on=0
        print('Jestem unieruchomiony')
        utime.sleep(0.3)
    if on==1:
        print('Dystans: ',distance(),' cm')
        power_on()
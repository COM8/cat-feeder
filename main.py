from gpiozero import LED, Button
from hass import Hass
from time import sleep
from motor import Motor

led: LED = LED(21)
button: Button = Button(13, hold_time=0.1)
motor: Motor = Motor()


gearCount: int = 0
portionSize: int = 3

def play_sound():
    pass

def on_pressed():
    global gearCount
    gearCount+=1
    print(gearCount)

def give_meal(portionSize: int):
    global gearCount, motor
    motor.on()
    while gearCount < portionSize:
        sleep(0.25)
    sleep(0.2)
    gearCount = 0
    motor.off()

def feed(msg: str):
  print(msg)
  give_meal(portionSize)

hass: Hass = Hass(feed)
hass.connect("", "")
button.when_held = on_pressed

while True:
     sleep(1)



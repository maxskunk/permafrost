import time
from w1thermsensor import W1ThermSensor
from gpiozero import LED
sensor = W1ThermSensor()
led = LED(18)

cooling = True
idealTemp = 22


def toggleSwitch():
    global cooling

    if cooling:
        cooling = False
        led.off()
    else:
        cooling = True
        led.on()


while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    if temperature > idealTemp:
        print("Temp Higher Than % so cooling" % idealTemp)
        led.on()
    elif temperature < idealTemp:
        print("Temp Lower Than % stopping cooling" % idealTemp)
        led.off()
    # toggleSwitch()
    time.sleep(1)

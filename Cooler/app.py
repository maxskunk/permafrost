import time
from w1thermsensor import W1ThermSensor
from gpiozero import LED
from os import system, name
import sqlite3


sensor = W1ThermSensor()
led = LED(18)

cooling = False
# idealTemp = 66
tempBuffer = .1

# Connect to DB
conn = sqlite3.connect('/home/pi/Cooler/permafrost_db.db')
c = conn.cursor()


def convertTempToFreedom(temp):
    return ((temp * 9 / 5) + 32)


def switchCooling(isOn):
    global cooling

    if isOn and not cooling:
        cooling = True
        led.on()
    elif not isOn and cooling:
        cooling = False
        led.off()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def updateScreen():
    global cooling

    action = "Waiting"
    if cooling:
        action = "Cooling"

    clear()
    print("Current Temp: %s f" % temperature)
    print("Desired Temp: %s f" % idealTemp)
    print("Current Action: %s " % action)


def readTempSetting():
    c.execute('select * from config where "key" == "desired_temp"')
    r = c.fetchone()
    return r[1]


while True:
    # Collect Desired Temp
    idealTemp = readTempSetting()
    # COllect Actual Temp
    temperature = convertTempToFreedom(sensor.get_temperature())

    highRange = idealTemp
    lowRange = idealTemp - .2

    if temperature > highRange:
        switchCooling(True)
    elif temperature < lowRange:
        switchCooling(False)

    updateScreen()
    time.sleep(1)

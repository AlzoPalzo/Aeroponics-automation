import RPi.GPIO as GPIO  # Importing the module that controls the pins on the raspberry pi
import time  # Importing the time module to help control the timing of the misting
from Weather import settingValue, printCurrentConditions# these functions from the weather module determine the which misting schedule should be used and allow the current weather conditions to be displayed

Airpin = 14  # Broadcom pin 14
Waterpin = 15  # Broadcompin 15 These are the pins that connect to the relay board that allow me to control the solenoid valves.

pinArray = [Airpin, Waterpin]

GPIO.setmode(
    GPIO.BCM)  # Setting the program, so that the pins are selected by the number in the rectangle in io diagrams(setting board mode to broadcom)

GPIO.setup(Airpin, GPIO.OUT)
GPIO.setup(Waterpin, GPIO.OUT)  # setting up pins 14 and 15 to output signal.

GPIO.output(Airpin, GPIO.HIGH)
GPIO.output(Waterpin, GPIO.HIGH)  # Making sure both pins are off to start with.


def turnOff():
    GPIO.output(pinArray, GPIO.HIGH)#this method can be used to turn off the solenoids


def coldWet():  # 1 defining the timings for the solenoids in cold damp conditions
    print("Now in setting for cold wet weather")
    printCurrentConditions()
    loops = 0
    while (loops < 8):  #How many times this particular loop will operate before checking the settings again. All settings run for about 16 minutes.
        GPIO.output(pinArray, GPIO.HIGH)#This line makes sure the pins are turned off at the start of the loop
        time.sleep(120)  # After being turned off the function will wait for 3 seconds before turning it on
        GPIO.output(pinArray, GPIO.LOW)#This line turns the solenoids on
        time.sleep(0.5)#this value controls how long the solenoids stay open for
        print('Current loop:', loops)#Displays the progress of the setting
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()  # After the looping is finished the program switches off all the relays and calls the function settingUpdate to get a new setting.


def coldDry():
    loops = 0
    print('Now in the setting for cold dry weather')
    printCurrentConditions()
    while (loops < 10):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(100)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop:', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def warmWet():
    loops = 0
    print('Now in the setting for warm wet weather')
    printCurrentConditions()
    while(loops < 12):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(80)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop:', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def warmDry():
    loops = 0
    print('Now in the setting for warm dry weather')
    printCurrentConditions()
    while(loops < 16):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(60)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop:', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def hotWet():
    loops = 0
    print('Now in the setting for hot wet weather')
    printCurrentConditions()
    while(loops < 14):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(70)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop:', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def hotDry():
    loops = 0
    print('Now in the setting for hot dry weather')
    printCurrentConditions()
    while(loops < 20):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(50)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop:', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def defaultSettings():#This setting is different from the others. It is called when the internet connection gets interupted. It does not attempt to print the current weather conditions because they cannot be read.
    loops = 0
    print('Using default settings')
    while (loops < 10):
        GPIO.output(pinArray, GPIO.HIGH)
        time.sleep(70)
        GPIO.output(pinArray, GPIO.LOW)
        time.sleep(0.5)
        print('Current loop: ', loops)
        loops = loops + 1
    GPIO.output(pinArray, GPIO.HIGH)
    settingUpdate()

def settingUpdate():#This is the function that updates the setting that should be used
    try:
        setNum = settingValue()#Calling the settingValue function from the weather module which actually checks the current conditions
        if (setNum == 1):
            coldWet()
        elif(setNum == 2):
            coldDry()
        elif(setNum == 3):
            warmWet()
        elif(setNum == 4):
            warmDry()
        elif(setNum == 5):
            hotWet()
        elif(setNum == 6):
            hotDry()
        elif(setNum == 7):
        defaultSettings()
    except KeyboardInterrupt:#This is called when you exit the program with the keyboard it makes sure the program is closed cleanly and the GPIO pins are reset
        print('Program exitted')
    finally:
        GPIO.cleanup



settingUpdate()

turnOff()
GPIO.cleanup()# If for some reason the program turns off early we make sure the pins are set to off and not engaged.
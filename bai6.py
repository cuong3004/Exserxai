import RPi.GPIO as IO 
from config import Config
import time

def main():

    IO.setwarnings(False)

    IO.setmode(IO.BCM)

    IO.setup(Config.BT1, IO.IN, pull_up_down=IO.PUD_UP)
    IO.setup(Config.BT2, IO.IN, pull_up_down=IO.PUD_UP)
    IO.setup(Config.BT3, IO.IN, pull_up_down=IO.PUD_UP)
    IO.setup(Config.BT4, IO.IN, pull_up_down=IO.PUD_UP)

    IO.setup(Config.DIR, IO.OUT)
    IO.setup(Config.PWD, IO.OUT)

    global PWD1, PWD2

    PWD1 = IO.PWM(Config.DIR, 100)
    PWD2 = IO.PWM(Config.PWD, 100)

    PWD1.start(0)
    PWD2.start(0)

    currentPWD = 0 
    print("is ok")
    while True:

        if IO.input(Config.BT1) == IO.LOW:
            PWD2.ChangeDutyCycle(0)
            upPWD = 20
            currentPWD = currentPWD + upPWD
            print(currentPWD)
            PWD1.ChangeDutyCycle(currentPWD)
            
            time.sleep(0.5)
        
        if IO.input(Config.BT2) == IO.LOW:
            PWD2.ChangeDutyCycle(0)
            downPWD = 20
            currentPWD = currentPWD - downPWD
            print(currentPWD)
            PWD1.ChangeDutyCycle(currentPWD)
            
            time.sleep(0.5)

        if IO.input(Config.BT3) == IO.LOW:
            PWD1.ChangeDutyCycle(0)
            upPWD = 20
            currentPWD = currentPWD + upPWD
            print('-'+ str(currentPWD))
            PWD2.ChangeDutyCycle(currentPWD)
            
            time.sleep(0.5)
        
        if IO.input(Config.BT4) == IO.LOW:
            PWD1.ChangeDutyCycle(0)
            downPWD = 20
            currentPWD = currentPWD - downPWD
            print('-'+ str(currentPWD))
            PWD2.ChangeDutyCycle(currentPWD)
            
            time.sleep(0.5)

    
    print(IO.input(Config.DIR))
    PWD1.ChangeDutyCycle(100)
    print(IO.input(Config.DIR))
    time.sleep(1)
    PWD1.stop()

    PWD2.ChangeDutyCycle(100)
    time.sleep(1)
    PWD2.stop()

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        PWD1.stop()
        PWD2.stop()
        IO.cleanup()
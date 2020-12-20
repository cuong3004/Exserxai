from SG90 import *
import RPi.GPIO as GPIO
from config import Config


def controlservo(s, anglepulseBT, ):
    current = s.currentdirection()

    if current >= 100 or current <= -100:
        anglepulseBT = -anglepulseBT

    director = int(round(float(anglepulseBT)/180 * 100)) 
    print(director + current)        
    print(current)

    
    rotato = director + current
    rotato = 100 if rotato >= 100 else -100 if rotato > 100 else rotato

    
    s.setdirection(rotato, 50 )
    time.sleep(0.5)

    return anglepulseBT



def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Config.BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Config.BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    s = sg90(0)

    anglepulseBT1 = 10
    anglepulseBT2 = 50
    anglepulseBT3 = 120

    print("All OK")

    try:
        while True:
            if GPIO.input(Config.BT1) ==  GPIO.LOW:
                print("Pulse 10 angle")
                anglepulseBT1 = controlservo(s, anglepulseBT1)
            
            if GPIO.input(Config.BT2) ==  GPIO.LOW:
                print("Pulse 50 angle")
                anglepulseBT2 = controlservo(s, anglepulseBT2)

            if GPIO.input(Config.BT3) ==  GPIO.LOW:
                print("Pulse 120 angle")
                anglepulseBT3 = controlservo(s, anglepulseBT3)

    except KeyboardInterrupt:
        s.cleanup()

if __name__ == "__main__":
    main()

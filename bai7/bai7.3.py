from SG90 import *
import RPi.GPIO as GPIO
from config import Config


def controlservo(s, anglepulseBT, ):
    current = s.currentdirection()

    if current >= 100:
        s.setdirection(-100, 50 )
        time.sleep(0.5)
        return

    director = int(round(float(anglepulseBT)/180 * 100)) 
    print(director + current)        
    print(current)

    
    rotato = director + current


    
    s.setdirection(rotato, 50 )
    time.sleep(0.5)


def main():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(Config.BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    s = sg90(0)

    anglepulseBT4 = 10


    print("All OK")

    s.setdirection(-100, 50 )

    try:
        while True:
            if GPIO.input(Config.BT4) ==  GPIO.LOW:
                print("Pulse 10 angle")
                controlservo(s, anglepulseBT4)
            
            

    except KeyboardInterrupt:
        s.cleanup()

if __name__ == "__main__":
    main()

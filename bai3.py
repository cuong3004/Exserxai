import RPi.GPIO as GPIO 
import time

def main():
    
    BTN4 = 2

    LED = 22

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BTN4, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    GPIO.setup(LED, GPIO.OUT)

    status4 = False
    while True:
        if GPIO.input(BTN4) == GPIO.LOW:
            print(GPIO.input(BTN4))
        print(GPIO.input(BTN4))
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
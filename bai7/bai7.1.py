from SG90 import *

def main():

    s = sg90(0)

    try:
        while True:
            print("Turn left ...")
            s.setdirection( 100, 50 )
            time.sleep(0.5)
            print("Turn right ...")
            s.setdirection( -50, 10 )
            time.sleep(0.5)
    except KeyboardInterrupt:
        s.cleanup()

if __name__ == "__main__":
    main()

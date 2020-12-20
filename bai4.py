import sys 
import Adafruit_DHT

# set type of the sensor
sensor = 11
pin = 24
# setpin numer

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print("Temp={0:0.1f}* Humidity={1:0.1f}%".format(temperature, humidity))
else:
    ("False to get readingp")
from gpiozero import LED
import time

led = LED(2)

while True:
    led.on()
    print("on")
    time.sleep(0.5)
    led.off()
    print("off")
    time.sleep(0.5)
    

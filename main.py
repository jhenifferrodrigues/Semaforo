from machine import Pin 
from utime import sleep

led_amarelo = Pin (22, Pin.OUT)

led_verde  = Pin (21, Pin.OUT)

led_vermelho    = Pin (23, Pin.OUT)

while True:
    led_verde.on()
    print("LED Verde ON")
    sleep(20)
    led_verde.off()
    print("LED Verde OFF")
    sleep(0.5)

    led_amarelo.on()
    print("LED Amarelo ON")
    sleep(10)
    led_amarelo.off()
    print("LED Amarelo OFF")
    sleep(0.5)

    led_vermelho.on()
    print("LED Vermelho ON")
    sleep(7)
    led_vermelho.off()
    print("LED Vermelho OFF")
    sleep(0.5)



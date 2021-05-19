import machine
import utime

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

conversion_factor = 3.3 / (65535)
file = open("temps.txt", "w")

led_onboard = machine.Pin(25, machine.Pin.OUT)

def leds_off():
    """Turn off all the LEDs."""
    led_onboard.value(0)

def leds_on():
    """Turn on all the LEDs."""
    led_onboard.value(1)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    file.write(str(temperature) + "\n")
    file.flush()
    if temperature <= 12.00:
        leds_off()
        led_onboard.value(1)
    elif temperature > 28.00:
        leds_off()
        led_onboard.value(1)
    else:
        leds_off()

    print(temperature)

    # Sleep for 5 seconds.
    utime.sleep(5)

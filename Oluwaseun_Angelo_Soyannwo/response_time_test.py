import machine
import utime
import urandom

button_pressed = False
#Set button and Led pins
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
Led = machine.Pin(28, machine.Pin.OUT)

def handler_function():
    """
    This is a handler function to be called by the Pin.irq when the trigger is called.
    """
    global button_pressed
    if not button_pressed:
        button_pressed = True
        reaction_time = utime.ticks_diff(utime.ticks_ms(), start_clock)
        print("hello")
        print("Your reaction time is: " + str(reaction_time) + "milliseconds.") 


"""
#Loop
for i in range(1):
        Led.value(1)
        utime.sleep(urandom.uniform(5, 10))
        Led.value(0)
        start_clock = utime.ticks_ms()

        #handler is an optional function to be called when the interrupt triggers
        #trigger determines when the handler function is called (i.e. pin rising or pin falling)
        button.irq(trigger=machine.Pin.IRQ_RISING, handler=handler_function,)
"""


"""
handler is an optional function to be called when the interrupt triggers
trigger determines when the handler function is called (i.e. pin rising or pin falling)
button.irq returns a callback object to another function
"""
#button.irq(trigger=machine.Pin.IRQ_RISING, handler=handler_function)
for i in range(5):
    Led.low()
    utime.sleep(urandom.uniform(2, 5))
    Led.high()
    start_clock = utime.ticks_ms()
    while not button_pressed:
        if button.value() == 0:
            reaction_time = utime.ticks_diff(utime.ticks_ms(), start_clock)
            print("hello")
            print("Your reaction time is: " + str(reaction_time) + "milliseconds.")
            button_pressed = True
    button_pressed = False
    Led.low()



import machine
import utime
import urandom


def response_time(loops: int):

	button_pressed = False

	def handler_function():
	"""
	This is a handler function to be called by the Pin.irq when the trigger is called.
	"""
		gloabl button_pressed
		if not button_pressed:
			button_pressed = True
			reaction_time = utime.ticks_diff(utime.ticks_ms(), start_clock)
			print("Your reaction time is: " +str(reaction_time) + "in milliseconds") 


	#Set button and LED pin
	button = machine.Pin(1, machine.Pin.In, machine.Pin.PULL_DOWN)
	Led = machine.Pin(2, machine.Pin.In, machine.Pin.PULL_DOWN)


	#Loop

	for i in range(loops):
		utime.sleep(urandom.uniform(5, 10))
		Led.value(1)
		start_clock = utime.ticks_ms()

		#handler is an optional function to be called when the interrupt triggers	
		#trigger determines when the handler function is called (i.e. pin rising or pin falling)

		button.irq(handler=handler_function, trigger=machine.Pin.IRQ_RISING)
		Led.value(0)



def main():
	response_time(1)


if __name__ == "__main__":
	main()

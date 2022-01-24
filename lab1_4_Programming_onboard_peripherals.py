import time


# Set the number of LED, Switches and Buttons
MAX_LEDS = 4
MAX_SWITCHES = 2
MAX_BUTTONS = 4

# Create lists for each of the IO component groups
leds = [base.leds[index] for index in range(MAX_LEDS)]
switches = [base.switches[index] for index in range(MAX_SWITCHES)] 
buttons = [base.buttons[index] for index in range(MAX_BUTTONS)]


leds_state = [0, 0, 0, 0]
delay = 0
while(True):
    if buttons[0].read():
        if leds_state[0] == 0: 
            leds_state[0] = 1
        else: 
            leds_state[0] = 0
    elif buttons[1].read():
        leds_state.append(leds_state.pop(0))
    elif buttons[2].read():
        for i in range(20):
            for i in range(MAX_LEDS):
                leds[i].toggle()
            time.sleep(.1)
    elif buttons[3].read():
        if delay == 0: 
            delay = 1
        else: 
            delay = 0
    for i in range(MAX_LEDS):
        if leds_state[i] == 0:
            leds[i].off()
        else:
            leds[i].on()
    time.sleep(delay)
            

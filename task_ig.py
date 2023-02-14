from microbit import *
while True:
    light = pin0.read_analog()
    if button_a.is_pressed():
        light = light+10
    if button_b.is_pressed():
        light = 0

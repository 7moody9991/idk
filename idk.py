from microbit import *
brightness = 0
while True:
    if button_a.is_pressed():
        if brightness <= 1000:
            pin0.write_analog(brightness)
            brightness += 100
            sleep(1000)
        else:
            brightness = 0
    elif button_b.is_pressed():
        brightness = 0
        pin0.write_analog(brightness)
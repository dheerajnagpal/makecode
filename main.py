degrees = 0
temperature = 0

def on_button_pressed_a():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45:
        basic.show_arrow(ArrowNames.NORTH)
    elif degrees < 135:
        basic.show_arrow(ArrowNames.EAST)
    elif degrees < 225:
        basic.show_arrow(ArrowNames.SOUTH)
    elif degrees < 315:
        basic.show_arrow(ArrowNames.WEST)
    else:
        basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global temperature
    temperature = input.temperature()
    basic.show_number(temperature)
    basic.show_string("C")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global degrees
    degrees = input.compass_heading()
    if degrees < 23:
        basic.show_arrow(ArrowNames.NORTH)
    elif degrees < 68:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif degrees < 113:
        basic.show_arrow(ArrowNames.EAST)
    elif degrees < 158:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif degrees < 203:
        basic.show_arrow(ArrowNames.SOUTH)
    elif degrees < 248:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif degrees < 293:
        basic.show_arrow(ArrowNames.WEST)
    elif degrees < 238:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

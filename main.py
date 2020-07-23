def on_button_pressed_a():
    global Pos_X
    if Pos_X > 0:
        Pos_X += -1
    else:
        Pos_X = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Pos_X
    if Pos_X < 4:
        Pos_X += 1
    else:
        Pos_X = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Pos_X = 0
Pos_X = 2
Pos_Y = 0

def on_forever():
    global Pos_Y
    led.plot(Pos_X, Pos_Y)
    basic.pause(200)
    basic.clear_screen()
    if Pos_Y == 4:
        for index in range(4):
            Pos_Y += -1
            led.plot(Pos_X, Pos_Y)
            basic.pause(200)
            basic.clear_screen()
    Pos_Y += 1
basic.forever(on_forever)

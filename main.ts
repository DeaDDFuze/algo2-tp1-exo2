input.onButtonPressed(Button.A, function () {
    if (Pos_X > 0) {
        Pos_X += -1
    } else {
        Pos_X = 4
    }
})
input.onButtonPressed(Button.B, function () {
    if (Pos_X < 4) {
        Pos_X += 1
    } else {
        Pos_X = 0
    }
})
let Pos_X = 0
Pos_X = 2
let Pos_Y = 0
basic.forever(function () {
    led.plot(Pos_X, Pos_Y)
    basic.pause(200)
    basic.clearScreen()
    if (Pos_Y == 4) {
        for (let index = 0; index < 4; index++) {
            Pos_Y += -1
            led.plot(Pos_X, Pos_Y)
            basic.pause(200)
            basic.clearScreen()
        }
    }
    Pos_Y += 1
})

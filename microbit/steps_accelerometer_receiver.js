basic.showLeds(`
. . . . .
. # # # .
. # # # .
. # # # .
. . . . .
`)

radio.onReceivedValue(function (name, value) {
    if (name == "steps") {
        steps = value
    } else if (name == "x") {
            x = value
    } else if (name == "y") {
        y = value
    } else if (name == "z") {
        z = value
    }
})

let steps = 0
let z = 0
let y = 0
let x = 0

radio.setGroup(15)
basic.forever(function () {
    serial.writeValue("steps", steps)
    serial.writeValue("x", x)
    serial.writeValue("y", y)
    serial.writeValue("z", z)
    basic.pause(100)
})

radio.setGroup(15)

let steps = 0

input.onGesture(Gesture.Shake, function () {
    steps += 1
})

basic.forever(function () {
    radio.sendValue("steps", steps)
    radio.sendValue("x", input.acceleration(Dimension.X))
    radio.sendValue("y", input.acceleration(Dimension.Y))
    radio.sendValue("z", input.acceleration(Dimension.Z))
    basic.showNumber(steps)
})

// reset count
input.onButtonPressed(Button.AB, function () {
    steps = 0
})
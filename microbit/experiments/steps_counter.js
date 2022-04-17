let steps = 0

input.onGesture(Gesture.Shake, function () {
    steps += 1
})

basic.forever(function () {
    basic.showNumber(steps)
})

// reset count
input.onButtonPressed(Button.AB, function() {
    steps=0
})
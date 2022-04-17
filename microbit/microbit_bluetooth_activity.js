bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Giraffe)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
// reset count
input.onButtonPressed(Button.AB, function () {
    steps = 0
})
input.onGesture(Gesture.Shake, function () {
    steps += 1
})
let steps = 0
bluetooth.setTransmitPower(7)
bluetooth.startAccelerometerService()
bluetooth.startUartService()
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    basic.showNumber(steps)
    bluetooth.uartWriteNumber(steps)
})



// Transmitter code

input.onButtonPressed(Button.B, function () {
    radio.setGroup(1)
    radio.setTransmitPower(7) // Max transmission power of 7, tested with 5 and it is not so stable. 
    basic.forever(function () {
        radio.sendString("1")
        basic.pause(1000)
        basic.showIcon(IconNames.Rabbit)
    })
})

// Receiver Code, range of signal strength from -128 to -28 (microbit v2)

// Button A - shows the absolute signal strength
input.onButtonPressed(Button.A, function () {
    let signal = 0
    radio.setGroup(1)
    basic.showIcon(IconNames.Duck)
    radio.onReceivedString(function (receivedString) {
        signal = Math.abs(radio.receivedPacket(RadioPacketProperty.SignalStrength))
        basic.showNumber(signal)
    })
})

// Button B - LED blinks when radio packet is recevied. 
// If nothing is received, a timer will start counting every second until 5 seconds and error is shown. 
input.onButtonPressed(Button.B, function () {
    let signal = 0
    let time = 0
    basic.showNumber(time)
    radio.setGroup(1)
    radio.onReceivedString(function(){
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showLeds(``)
        time = 0
    })
    while (time < 5) {
        time = 1 + time
        basic.showNumber(time)
        basic.pause(1000)
    }
    if (time == 5) {
        basic.showIcon(IconNames.No)
    }    
})

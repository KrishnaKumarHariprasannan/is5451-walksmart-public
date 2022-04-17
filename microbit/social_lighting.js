// Create a NeoPixel driver - specify the pin, number of LEDs, and the type of
// the NeoPixel strip, either standard RGB (with GRB or RGB format) or RGB+White.
// Reference: https://makecode.microbit.org/pkg/Microsoft/pxt-neopixel

let strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB);
function setLed() {
    // set pixel colors to all 30 LEDs
    for (let num = 0; num < 30; num++) {
        strip.setPixelColor(num, NeoPixelColors.Indigo);
    }
    strip.show()
}

radio.setGroup(1)
basic.showIcon(IconNames.Yes)
setLed()

input.onButtonPressed(Button.A, function () {
    let time = 0
    basic.forever(function () {

        radio.sendString("1")
        basic.pause(1000)
        basic.showIcon(IconNames.Yes)

        radio.onReceivedString(function (receivedString) {
            basic.showIcon(IconNames.Heart)
            strip.showRainbow(1, 360)
            strip.show()
            radio.sendString("1")
            time = 0
        })
        while (time < 3) {
            time = 1 + time
            radio.sendString("1")
            basic.showNumber(time)
            basic.pause(1000)
        }
        if (time == 3) {
            basic.showIcon(IconNames.Yes)
            setLed()
        }
    })

})



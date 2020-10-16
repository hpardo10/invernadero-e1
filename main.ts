basic.forever(function () {
    basic.showNumber(input.temperature())
    if (input.temperature() < 8) {
        basic.showString("TB")
    } else if (input.temperature() > 30) {
        basic.showString("TA")
    }
    if (pins.analogReadPin(AnalogPin.P0) < 200) {
        basic.showString("HB")
    } else if (pins.analogReadPin(AnalogPin.P0) > 600) {
        basic.showString("HA")
    }
})

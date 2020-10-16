def on_forever():
    basic.show_number(input.temperature())
    if input.temperature() < 8:
        basic.show_string("TB")
    else:
        if input.temperature() > 30:
            basic.show_string("TA")
    if pins.analog_read_pin(AnalogPin.P0) < 200:
        basic.show_string("HB")
    else:
        if pins.analog_read_pin(AnalogPin.P0) > 600:
            basic.show_string("HA")
basic.forever(on_forever)

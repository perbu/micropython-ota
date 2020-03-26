import machine

class BlinkyLed:

    def toggle_state(self,what):
        if self.pin.value():
            self.pin.off()
        else:
            self.pin.on()

    def __init__(self):
        pin = machine.Pin(21, machine.Pin.OUT)
        pin.off()
        self.pin = pin
        tim = machine.Timer(-1)
        self.tim = tim

    def enable(self):
        self.tim.init(period=500, mode=machine.Timer.PERIODIC, callback=self.toggle_state)

    def disable(self):
        self.tim.deinit()

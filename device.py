from corerasp import *
# Define DEVICE:
# id = pin


class Device:
    def __init__(self, pin, io="OUT", description= "",high = True):

        self.pin = pin
        self.io = io
        if self.io == "OUT":
            set_pin_as_output(self.pin)
            self.state = self.get_state()
            write_to_port(self.pin, self.state)
        if self.io == "IN":
            set_pin_as_input(self.pin)
            self.state = self.get_state()
        self.description = description
        self.high = high
        self.id = pin
        self.on_off = "off" if self.state != self.high else "on"
        self.name = "device"+ description.replace(" ", "").lower().capitalize() + str(self.pin)

    def set_state(self,state):
        write_to_port(self.pin,state)
        self.on_or_off()
        return self.get_state()

    def get_state(self):
        self.state = read_port(self.pin)
        return self.state

    def swap_state(self):
        self.set_state(1-self.get_state())
        self.on_or_off()
        return self.get_state()

    def on_or_off(self):
        self.on_off = "off" if self.state != self.high else "on"
        return self.on_off
    
    def __str__(self):
        # This will be used to return to PHP, or print Device info.
        # [pin, io, description,state,high, on_off, name]
        return "[ {},{},{},{},{},{},\"{}\" ]".format(self.pin, self.io, 
        self.description, self.state, self.high,self.on_off, self.name)
        

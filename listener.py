import keyboard
import time

class Listener:
    def __init__(self):
        self.keys={"a":128,"s":64,"d":32,"f":16,"j":8,"k":4,"l":2,";":1}
        self.pressed=set()
        self.trigger="space"
        self.string=""

    def clear_pressed(self):
        self.pressed=set()

    def add_pressed(self,event):
        if event.name in self.keys:
            self.pressed.add(event.name)
            print("Added {}".format(event.name))
        if event.name==self.trigger:
            print("Triggered")
            self.type_char()

    def get_char(self):
        return chr(sum([self.keys[k] for k in self.pressed]))

    def type_char(self):
        c=self.get_char()
        self.clear_pressed()
        self.string+=c
        print("String reads: {}".format(self.string))

listener=Listener()

keyboard.on_press(listener.add_pressed)

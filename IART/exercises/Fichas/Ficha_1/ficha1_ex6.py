import os.path
from tkinter import *

from agents import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

loc_T1, loc_T2 = (0, 0), (1, 0)
AQ, AC, AJ = (0, 1), (0, 2), (0, 3)

class Gui(Environment):

    def __init__(self, root, height=300, width=380):
        super().__init__()
        self.temp = {loc_T1: 10,
                     loc_T2: 10}
        self.devices = {AQ: False,
                        AC: False,
                        AJ: False}
        self.root = root
        self.height = height
        self.width = width
        self.canvas = None
        self.displays = []
        self.create_canvas()
        self.create_displays()

    def thing_classes(self):
        return []

    def percept(self, agent):
        """Returns the the location temperature."""
        return self.temp[loc_T1], self.temp[loc_T2]

    def execute_action(self, agent, action):
        """Change the devices status (On/Off)"""
        if 22 <= self.temp[loc_T1] <= 24:
            self.devices = {AQ: False, AC: False, AJ: False}
        elif 22 > self.temp[loc_T1] >= 20:
            if self.temp[loc_T2] > self.temp[loc_T1] :
                self.devices = {AQ: False, AC: False, AJ: True}
            else:
                self.devices = {AQ: True, AC: False, AJ: False}
        elif self.temp[loc_T1] < 20 :
            self.devices = {AQ: True, AC: False, AJ: False}
        elif 24 < self.temp[loc_T1] <= 26:
            if self.temp[loc_T2] < self.temp[loc_T1] :
                self.devices = {AQ: False, AC: False, AJ: True}
            else:
                self.devices = {AQ: False, AC: True, AJ: False}
        else:
            self.devices = {AQ: False, AC: True, AJ: False}
        self.canvas.itemconfig(self.displays[0], text='T1: '+str(self.temp[loc_T1]))
        self.canvas.itemconfig(self.displays[1], text='T2: '+str(self.temp[loc_T2]))
        self.canvas.itemconfig(self.displays[2], text='AQ: '+str(self.devices[AQ]))
        self.canvas.itemconfig(self.displays[3], text='AC: '+str(self.devices[AC]))
        self.canvas.itemconfig(self.displays[4], text='AJ: '+str(self.devices[AJ]))


    def create_canvas(self):
        """Creates Canvas element in the GUI."""
        self.canvas = Canvas(
            self.root,
            width=self.width,
            height=self.height,
            background='powder blue')
        self.canvas.pack(side='bottom')

    def create_displays(self):
        """Creates the displays required in the GUI."""
        self.canvas.create_rectangle(130, 200, 180, 250, fill='white')
        display_T1 = self.canvas.create_text(155, 225, font="Helvetica 10 bold italic", text='T1: '+str(self.temp[loc_T1]))
        self.displays.append(display_T1)
        self.canvas.create_rectangle(200, 200, 250, 250, fill='white')
        display_T2 = self.canvas.create_text(225, 225, font="Helvetica 10 bold italic", text='T2: '+str(self.temp[loc_T2]))
        self.displays.append(display_T2)

        self.canvas.create_rectangle(10, 100, 110, 150, fill='white')
        display_AQ = self.canvas.create_text(60, 125, font="Helvetica 10 bold italic", text='AQ: '+str(self.devices[AQ]))
        self.displays.append(display_AQ)
        self.canvas.create_rectangle(140, 100, 240, 150, fill='white')
        display_AC = self.canvas.create_text(190, 125, font="Helvetica 10 bold italic", text='AC: '+str(self.devices[AC]))
        self.displays.append(display_AC)
        self.canvas.create_rectangle(270, 100, 370, 150, fill='white')
        display_AJ = self.canvas.create_text(320, 125, font="Helvetica 10 bold italic", text='AJ: '+str(self.devices[AJ]))
        self.displays.append(display_AJ)

    def update_env(self, agent):
        """Updates the GUI according to the agent's action."""
        if self.devices[AQ] == True:
            self.temp[loc_T1] += 1
        if self.devices[AC] == True:
            self.temp[loc_T1] -= 1
        if self.devices[AJ] == True:
            if self.temp[loc_T1] < self.temp[loc_T2]:
                self.temp[loc_T1] += 2
            elif self.temp[loc_T1] > self.temp[loc_T2]:
                self.temp[loc_T1] -= 2
        self.temp[loc_T1] += (random.randint(0, 2) - 1)
        self.temp[loc_T2] += (random.randint(0, 2) - 1)

        self.step()

def create_agent(env, agent):
    """Creates the agent in the GUI and is kept independent of the environment."""
    env.add_thing(agent)

if __name__ == "__main__":
    root = Tk()
    root.title("TemperatureX Environment")
    root.geometry("420x380")
    root.resizable(0, 0)
    frame = Frame(root, bg='black')
    next_button = Button(frame, text='Next', height=2, width=6, padx=2, pady=2)
    next_button.pack(side='left')
    frame.pack(side='bottom')
    env = Gui(root)
    agent = ReflexVacuumAgent()
    create_agent(env, agent)
    next_button.config(command=lambda: env.update_env(agent))
    root.mainloop()
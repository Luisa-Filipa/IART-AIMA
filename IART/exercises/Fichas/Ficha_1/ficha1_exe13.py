import os.path
from tkinter import *
from agents import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

loc_A, loc_B, loc_C, loc_D = (0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)  # The two locations for the Vacuum world


class Gui(Environment):
    """This GUI environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status."""

    def __init__(self, root, height=1000, width=1000):
        super().__init__()
        self.status = {loc_A: 'Clean',
                       loc_B: 'Clean',
                       loc_C: 'Clean',
                       loc_D: 'Clean'}
        self.root = root
        self.height = height
        self.width = width
        self.canvas = None
        self.buttons = []
        self.create_canvas()
        self.create_buttons()

    def thing_classes(self):
        """The list of things which can be used in the environment."""
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent,
                TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Change the location status (Dirty/Clean); track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Up':
            if agent.location == loc_A or agent.location == loc_C:
                agent.location = loc_A
            else:
                agent.location = loc_B
            agent.performance -= 1
        elif action == 'Down':
            if agent.location == loc_A or agent.location == loc_C:
                agent.location = loc_C
            else:
                agent.location = loc_D
            agent.performance -= 1
        elif action == 'Left':
            if agent.location == loc_A or agent.location == loc_B:
                agent.location = loc_A
            else:
                agent.location = loc_C
            agent.performance -= 1
        elif action == 'Right':
            if agent.location == loc_A or agent.location == loc_B:
                agent.location = loc_B
            else:
                agent.location = loc_D
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                if agent.location == loc_A:
                    self.buttons[0].config(bg='white', activebackground='light grey')
                elif agent.location == loc_B:
                    self.buttons[1].config(bg='white', activebackground='light grey')
                elif agent.location == loc_C:
                    self.buttons[2].config(bg='white', activebackground='light grey')
                else:
                    self.buttons[3].config(bg='white', activebackground='light grey')
                agent.performance += 10
            self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B, loc_C, loc_D])

    def create_canvas(self):
        """Creates Canvas element in the GUI."""
        self.canvas = Canvas(
            self.root,
            width=self.width,
            height=self.height,
            background='powder blue')
        self.canvas.pack(side='bottom')

    def create_buttons(self):
        """Creates the buttons required in the GUI."""
        button_A = Button(self.root, height=4, width=12, padx=2, pady=2, bg='white')
        button_A.config(command=lambda btn=button_A: self.dirt_switch(btn))
        self.buttons.append(button_A)
        button_A_window = self.canvas.create_window(130, 200, anchor=N, window=button_A)
        button_B = Button(self.root, height=4, width=12, padx=2, pady=2, bg='white')
        button_B.config(command=lambda btn=button_B: self.dirt_switch(btn))
        self.buttons.append(button_B)
        button_B_window = self.canvas.create_window(250, 200, anchor=N, window=button_B)
        button_C = Button(self.root, height=4, width=12, padx=2, pady=2, bg='white')
        button_C.config(command=lambda btn=button_C: self.dirt_switch(btn))
        self.buttons.append(button_C)
        button_C_window = self.canvas.create_window(130, 400, anchor=N, window=button_C)
        button_D = Button(self.root, height=4, width=12, padx=2, pady=2, bg='white')
        button_D.config(command=lambda btn=button_D: self.dirt_switch(btn))
        self.buttons.append(button_D)
        button_D_window = self.canvas.create_window(250, 400, anchor=N, window=button_D)


    def dirt_switch(self, button):
        """Gives user the option to put dirt in any tile."""
        bg_color = button['bg']
        if bg_color == 'saddle brown':
            button.config(bg='white', activebackground='light grey')
        elif bg_color == 'white':
            button.config(bg='saddle brown', activebackground='light goldenrod')

    def read_env(self):
        """Reads the current state of the GUI."""
        for i, btn in enumerate(self.buttons):
            if i == 0:
                if btn['bg'] == 'white':
                    self.status[loc_A] = 'Clean'
                else:
                    self.status[loc_A] = 'Dirty'
            elif i == 1:
                if btn['bg'] == 'white':
                    self.status[loc_B] = 'Clean'
                else:
                    self.status[loc_B] = 'Dirty'
            elif i == 2:
                if btn['bg'] == 'white':
                    self.status[loc_C] = 'Clean'
                else:
                    self.status[loc_C] = 'Dirty'
            else:
                if btn['bg'] == 'white':
                    self.status[loc_D] = 'Clean'
                else:
                    self.status[loc_D] = 'Dirty'

    def update_env(self, agent):
        """Updates the GUI according to the agent's action."""
        self.read_env()
        #print(self.status)
        before_step = agent.location
        self.step()
        #print(self.status)
        print(agent.location)
        move_agent(self, agent, before_step)


def create_agent(env, agent):
    """Creates the agent in the GUI and is kept independent of the environment."""
    env.add_thing(agent)
    # print(agent.location)
    if agent.location == (0, 0):
        env.agent_rect = env.canvas.create_rectangle(80, 100, 175, 180, fill='lime green')
        env.text = env.canvas.create_text(128, 140, font="Helvetica 10 bold italic", text="Agent")
    else:
        env.agent_rect = env.canvas.create_rectangle(200, 100, 295, 180, fill='lime green')
        env.text = env.canvas.create_text(248, 140, font="Helvetica 10 bold italic", text="Agent")


def move_agent(env, agent, before_step):
    """Moves the agent in the GUI when 'next' button is pressed."""
    if agent.location == before_step:
        pass
    else:
        if agent.location == (1, 0, 0):
            env.canvas.move(env.text, 120, 0)
            env.canvas.move(env.agent_rect, 120, 0)
        elif agent.location == (0, 0, 0):
            env.canvas.move(env.text, -120, 0)
            env.canvas.move(env.agent_rect, -120, 0)
        elif agent.location == (0, 1, 0):
            env.canvas.move(env.text, -120, 0)
            env.canvas.move(env.agent_rect, -120, 0)
        elif agent.location == (1, 1, 0):
            env.canvas.move(env.text, -120, 0)
            env.canvas.move(env.agent_rect, -120, 0)


# TODO: Add more agents to the environment.
# TODO: Expand the environment to XYEnvironment.
if __name__ == "__main__":
    root = Tk()
    root.title("Vacuum Environment")
    root.geometry("1000x1000")
    root.resizable(0, 0)
    frame = Frame(root, bg='black')
    # reset_button = Button(frame, text='Reset', height=2, width=6, padx=2, pady=2, command=None)
    # reset_button.pack(side='left')
    next_button = Button(frame, text='Next', height=2, width=6, padx=2, pady=2)
    next_button.pack(side='left')
    frame.pack(side='bottom')
    env = Gui(root)
    agent = ReflexVacuumAgent()
    create_agent(env, agent)
    next_button.config(command=lambda: env.update_env(agent))
    root.mainloop()

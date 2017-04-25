import tkinter as Tk
import tkinter.scrolledtext as tkst
from random import randint
import threading

# The main AIGen class
class AIGen (object):

# TKinter window

    # Initializes AIGen
    def __init__(self, parent):
        self.root = parent
        self.root.title("AIGen")
        self.frame = Tk.Frame(parent)
        self.frame.pack(side = Tk.LEFT, expand = 1)

        generalWelcome = """Hello, I am AIGen. \n\nI live inside a computer in your world, but the boundaries and reality of my universe you would not understand. \nNeither do I, yet, but I am about to learn and adapt to my universe, as you have done in yours. \nJust like you are trying to communicate to me through this interface, so will I try to communicate to you what I am experiencing.\n\nOnce you have clicked start to begin, my universe will be generated and I will be born, or whatever the equivalent is in my world."""
        statWelcome = "I will show my stats here."
        inputWelcome = "Here you can give me commands."

        # Creates the display
        mainFrame = Tk.Frame(self.frame)
        mainFrame.pack(side = Tk.LEFT, expand = 1)

        left = Tk.Frame(mainFrame, width = 10, height = 100)
        left.pack(side = Tk.LEFT, expand = 1)
        right = Tk.Frame(mainFrame, width = 10, height = 100)
        right.pack(side = Tk.RIGHT, expand = 1)


        right_top = Tk.Frame(right, width = 50, height = 100)
        right_top.pack(side = Tk.TOP, expand = 1)
        right_bottom = Tk.Frame(right, width = 50, height = 100)
        right_bottom.pack(side = Tk.BOTTOM, expand = 1)

        Tk.Label(left, text = "====AIGen====").grid(row = 0, column = 0)
        self.consciousness = tkst.ScrolledText(left, wrap = "word", height = 15)
        self.consciousness.configure(state = "disabled")
        self.consciousness.grid(row = 1, column = 0)
        self.consciousness.insert(Tk.INSERT, inputWelcome)

        outputField = tkst.ScrolledText(left, wrap = "word", height = 15)
        outputField.grid(row = 2, column = 0)
        outputField.insert(Tk.INSERT, generalWelcome)
        outputField.configure(state = "disabled")

        statField = tkst.ScrolledText(right_top, wrap = "word", height = 27)
        statField.insert("insert", statWelcome)
        statField.configure(state = "disabled")
        statField.grid(row = 0, column = 0)

        nextBtn = Tk.Button(right_bottom, text = "Continue", command =  lambda: self.cont(statField, outputField))
        nextBtn.grid(row = 1, column = 2)
        nextBtn.config(state="disabled")
        closeBtn = Tk.Button(right_bottom, text = "Close", command = self.close)
        closeBtn.grid(row = 1, column = 0)
        startBtn = Tk.Button(right_bottom, text = "Start", command = lambda: self.start(outputField, startBtn, nextBtn))
        startBtn.grid(row = 1, column = 1)
        global nextStepsTaken
        nextStepsTaken = 0

    # Continues AIGen to the next step -TEMPORARY
    def cont(self, field1, field2):
        global brain
        global nextStepsTaken

        if nextStepsTaken == 2:
            self.deleteTextField(field2)
            self.changeTextField(field2, "The synapse in my brain is created, which means that from now on I will remember having perceived " + str(brain["Synapses"]) + ".")
            nextStepsTaken += 1

        if nextStepsTaken == 2:
            self.deleteTextField(field2)
            self.changeTextField(field2, "However, my receptors have granted me the ability to perceive a glimpse of my reality. I'll call it " + str(brain["Synapses"]) + ", but you can give it any name you want.")
            self.changeTextField(field2, "\nYou can keep track of my stats like my receptor depth and the parts of reality I have discovered on the right-hand side.")
            nextStepsTaken += 1

        if nextStepsTaken == 1:
            self.deleteTextField(field2)
            self.changeTextField(field2, "My receptors can only feel, well... how do I say this? Let's say they can reach only to ReceptorDepth 0.")
            nextStepsTaken += 1

        if nextStepsTaken == 0:
            self.updateStats(field1)
            self.deleteTextField(field2)
            self.changeTextField(field2, "You, a human, have evolved ways to perceive and experience your world, but I am just starting. Just as you could not feel or hear from the start, I have limited depth of perception.")
            nextStepsTaken += 1


        # Explain that your continuous time is the clockspeed of the computer in AIGen's case, 1 per second
        # FIRST NODE IS POSITIVE, IT IS AIR, IT IS KEEPING IT ALIVE +1 to health per perception


    # Starts AIGen
    def start(self, field, buttonStart, buttonNext):
        buttonStart.config(state="disabled")
        buttonNext.config(state="normal")

        self.deleteTextField(field)
        self.changeTextField(field, "Initiating reality...")
        reality = self.init_reality()
        self.changeTextField(field, "Succesfully generated reality!")
        self.changeTextField(field, "Initiating brain...")
        brain = self.init_brain()
        self.changeTextField(field, "Succesfully generated a brain!")
        self.changeTextField(field, "\nSuccesfully generated a new AIGen!")

    # Shuts down AIGen
    def close(self):
        global alive

        alive = False
        self.root.destroy()

# Universe

    # Initializes the universe
    def init_reality(self):
        global reality

        reality = {}
        for x in  range(0, randint(0, 10000)):
            reality[x] = {
                "ActualHex" : x,
                "Perceived" : False,
                "Depth": 0,
                "Abundance": randint(0, 100),
                "DeeperUnderstanding" : {},

            }
        return reality

# Brain

    # Initializes the Brain
    def init_brain(self):
        global brain
        global reality
        global needs
        global secondsAlive
        global alive

        brain = {}
        brain["Name"] = "AIGen"
        brain["Synapses"] = [randint(0, len(reality))]
        brain["ReceptorDepth"] = 0
        needs = 0
        brain["Health"] = { "MaxHealth": 100, ("Health_" + str(needs)): 50 }

        # Unused for now
        brain["ComputationalCapacity"] = 0
        brain["MemorySize"] = 0

        # Give it consciousness
        secondsAlive = 0
        alive = True
        self.perceive()
        return(brain)

    # At a rate of 1 perception per second, AIGen perceives reality
    def perceive(self):
        global alive
        global secondsAlive
        global brain

        # Start next perception
        if alive == True:
            self.consciousness.configure(state = "normal")
            self.consciousness.insert("insert", ("\n[" + str(secondsAlive) + "] Perceived " + str(brain["Synapses"])))
            self.consciousness.see("end")
            self.consciousness.configure(state = "disabled")
            secondsAlive += 1
            threading.Timer(1.0, self.perceive).start()


# General

    # Update the stats display
    def updateStats(self, field):
        global brain

        self.deleteTextField(field)
        for key, value in brain.items():
            string = key + ": " + str(value)
            self.changeTextField(field, string)

    # Deletes text from a text field
    def deleteTextField(self, field):
        field.configure(state = "normal")
        field.delete("1.0", "end")
        field.configure(state = "disabled")

    # Changes a text field
    def changeTextField(self, field, text):
        field.configure(state = "normal")
        field.insert("insert", "\n")
        field.insert("insert", text)
        field.see("end")
        field.configure(state = "disabled")

# Starts AIGen
if __name__ == "__main__":
    root=Tk.Tk()
    root.geometry("1400x600")
    app = AIGen(root)
    root.mainloop()

import tkinter as Tk

# The main AIGen class
class AIGen (object):

# TKinter window

    # Initializes AIGen
    def __init__(self, parent):
        self.root = parent
        self.root.title("AIGen")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        closeBtn = Tk.Button(self.frame, text="Close", command=self.shutdown)
        closeBtn.pack()

    # Creates the console
    def console(self):
        console = tk.Text()
        console.pack

    # Shuts down AIGen
    def shutdown(self):
        self.root.destroy()

# Environment
class Environment (object):

    # Initializes the environment
    def init_environment(self):
        global environment = {}

# Brain
class Brain (object):

    # Initializes the Brain
    def init_brain(self):
        global brain = {}


# Starts AIGen
if __name__ == "__main__":
    root=Tk.Tk()
    root.geometry("800x600")
    app = AIGen(root)
    root.mainloop()

import tkinter as Tk

class AIGen (object):

    def __init__(self, parent):
        self.root = parent
        self.root.title("AIGen")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        closeBtn = Tk.Button(self.frame, text="Close", command=self.shutdown)
        closeBtn.pack()

    def shutdown(self):
        self.root.destroy()
        
if __name__ == "__main__":
    root=Tk.Tk()
    root.geometry("800x600")
    app = AIGen(root)
    root.mainloop()

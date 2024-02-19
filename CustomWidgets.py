from tkinter import *
from tkinter.ttk import *

class CustomButton(Frame):
    def __init__(self, parent, width=0, height=0, text="", bg="#fff"):
        super().__init__(master=parent, width=width, height=height, style="TFrame")
        style = Style()
        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground="#fff", pady=0, padx=0, borderwidth=0, relief="flat")
        self.Label = Label(self, text=text, font=("Arial", 24), style="TLabel")
        self.Label.place(x=15, y=0)




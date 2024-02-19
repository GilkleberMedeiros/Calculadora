from tkinter import *
from CustomWidgets import CustomButton

class Calc():
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Calculadora Python")
        self.janela.geometry("300x450")

        # Frames
        self.Frame1 = Frame(self.janela, width=300, height=80, bg="#BECDDB")
        self.Frame1.place(x=0, y=0)
        self.Frame2 = Frame(self.janela, width=300, height=40, bg="#7B92A8")
        self.Frame2.place(x=0, y=80)
        self.Frame3 = Frame(self.janela, width=300, height=330, bg="#3E5B75")
        self.Frame3.place(x=0, y=120)

        # Botões
        self.Botao1 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="(", font="Arial 24",
                             command=lambda arg="(": self.insert(arg))
        self.Botao1.place(x=20, y=20, width=50, height=42)
        self.Botao2 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text=")", font="Arial 24",
                             command=lambda arg=")": self.insert(arg))
        self.Botao2.place(x=90, y=20, width=50, height=42)
        self.Botao3 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="C", font="Arial 24",
                             command=lambda arg="C": self.insert(arg))
        self.Botao3.place(x=160, y=20, width=50, height=42)
        self.Botao4 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="/", font="Arial 24",
                             command=lambda arg="/": self.insert(arg))
        self.Botao4.place(x=230, y=20, width=50, height=42)
        self.Botao5 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="1", font="Arial 24",
                             command=lambda arg="1": self.insert(arg))
        self.Botao5.place(x=20, y=82, width=50, height=42)
        self.Botao6 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="2", font="Arial 24",
                             command=lambda arg="2": self.insert(arg))
        self.Botao6.place(x=90, y=82, width=50, height=42)
        self.Botao7 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="3", font="Arial 24",
                             command=lambda arg="3": self.insert(arg))
        self.Botao7.place(x=160, y=82, width=50, height=42)
        self.Botao8 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="*", font="Arial 24",
                             command=lambda arg="*": self.insert(arg))
        self.Botao8.place(x=230, y=82, width=50, height=42)
        self.Botao9 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="4", font="Arial 24",
                             command=lambda arg="4": self.insert(arg))
        self.Botao9.place(x=20, y=144, width=50, height=42)
        self.Botao10 = Button(self.Frame3,
                             bg="#162D42", fg="#ffffff",
                             text="5", font="Arial 24",
                             command=lambda arg="5": self.insert(arg))
        self.Botao10.place(x=90, y=144, width=50, height=42)
        self.Botao11 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="6", font="Arial 24",
                              command=lambda arg="6": self.insert(arg))
        self.Botao11.place(x=160, y=144, width=50, height=42)
        self.Botao12 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="-", font="Arial 24",
                              command=lambda arg="-": self.insert(arg))
        self.Botao12.place(x=230, y=144, width=50, height=42)
        self.Botao13 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="7", font="Arial 24",
                              command=lambda arg="7": self.insert(arg))
        self.Botao13.place(x=20, y=206, width=50, height=42)
        self.Botao14 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="8", font="Arial 24",
                              command=lambda arg="8": self.insert(arg))
        self.Botao14.place(x=90, y=206, width=50, height=42)
        self.Botao15 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="9", font="Arial 24",
                              command=lambda arg="9": self.insert(arg))
        self.Botao15.place(x=160, y=206, width=50, height=42)
        self.Botao16 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="+", font="Arial 24",
                              command=lambda arg="+": self.insert(arg))
        self.Botao16.place(x=230, y=206, width=50, height=42)
        self.Botao17 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="0", font="Arial 24",
                              command=lambda arg="0": self.insert(arg))
        self.Botao17.place(x=20, y=268, width=120, height=42)
        self.Botao18 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text=".", font="Arial 24",
                              command=lambda arg=".": self.insert(arg))
        self.Botao18.place(x=160, y=268, width=50, height=42)
        self.Botao19 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="=", font="Arial 24",
                              command=lambda arg="=": self.insert(arg))
        self.Botao19.place(x=230, y=268, width=50, height=42)

        self.janela.mainloop()

    def insert(self, s):
        print("Clicked!!!", s)


app = Calc()
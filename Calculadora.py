from tkinter import *

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

        # Labels
        self.Label1 = Label(self.Frame1,
                            text="0",
                            bg="#BECDDB",
                            fg="#000000",
                            font="Arial 30",
                            anchor="e",
                            wraplength=-13)
        self.Label1.place(x=0, y=0, width=300, height=80)
        self.Result = Label(self.Frame2,
                            text="0",
                            bg="#7B92A8",
                            fg="#000000",
                            font="Arial 18",
                            anchor="e")
        self.Result.place(x=0, y=0, width=300, height=40)

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
        self.Botao17.place(x=20, y=268, width=50, height=42)
        self.Botao18 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text=".", font="Arial 24",
                              command=lambda arg=".": self.insert(arg))
        self.Botao18.place(x=90, y=268, width=50, height=42)
        self.Botao19 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="<=", font="Arial 24",
                              command=lambda arg="<=": self.insert(arg))
        self.Botao19.place(x=160, y=268, width=50, height=42)
        self.Botao20 = Button(self.Frame3,
                              bg="#162D42", fg="#ffffff",
                              text="=", font="Arial 24",
                              command=self.canBeCalculated)
        self.Botao20.place(x=230, y=268, width=50, height=42)

        self.janela.mainloop()

    def insert(self, s):
        """
        Função para inserir elemento no display
        :param s:
        :return:
        """
        text = self.Label1['text'] # Texto
        textSize = int(self.Label1['font'][6:]) # Tamanho do texto
        textFont = self.Label1['font'][:6] # Fonte usada no texto

        text = self.check(text, s)

        # Diminui o tamanho do texto conforme o cálculo vai ficando maior
        if len(text) > 13:
            if textSize > 12:
                self.Label1['font'] = textFont + str(textSize - 6)

        self.Label1['text'] = text

    def check(self, text, s):
        """
        Função com várias condições para limitar o cálculo que é digitado pelo usuário
        :param text:
        :param s:
        :return:
        """
        lastElement = text[-1]
        # Se digitado(s) for igual C apagar tudo
        if s == "C":
            self.Label1['font'] = self.Label1['font'][:6] + "30"
            return "0"
        else:
            # Se digitado(s) for <= retornar um text menos um elemento
            if s == "<=":
                if len(text) > 1:
                    return text[:len(text) - 1]
                return "0"
            # Se digitado(s) for ( e ultimo elemento text não for um symbol(+, -, *, /)
            if s == "(" and not (self.isSymbol(lastElement) or lastElement == "("):
                self.Result['text'] = "Operação inválida"
                return text
            # Se digitado(s) for ) e ultimo elemento não for um número ou .
            if s == ")" and not (self.isNumeric(lastElement) or lastElement == ")"):
                self.Result['text'] = "Operação inválida"
                return text
            # Se digitado(s) for symbol e o ultimo elemento não for digito, . ou )
            if self.isSymbol(s) and not (self.isNumeric(lastElement) or lastElement == ")"):
                self.Result['text'] = "Operação inválida"
                return text
            # Se digitado(S) for igual a . verificar se existe outro . ou se está em um número
            if s == ".":
                number = ""
                for i in text[::-1]:
                    if i.isdigit() or i == ".":
                        number += i
                    else:
                        break
                if ("." not in number) and number != '':
                    return text + s
                else:
                    return text
            # Se digitado(s) for um numero um ( retorná-lo como primeiro elemento
            if (s.isdigit() or s == "(") and text == "0":
                return s
            # Se digitado(s) for um número e último elemento for um numero ou .
            # retorná-lo sem espaço
            elif s.isdigit() and (self.isNumeric(lastElement)):
                return text + s
            # Se o último elemento for um espaço em branco, retornar digitado(s) sem espaço
            elif lastElement == " ":
                return text + s
            # Em todos os outros casos retornar digitado(s) com espaço
            else:
                return text + " " + s


    def canBeCalculated(self):
        """
        Função para verificar se a conta pode ser calculada
        :return:
        """

        # Se passar texto.Label1 como parâmetro em command ele não vai ser atualizado
        # então peguei daqui
        text = self.Label1['text']
        pE = 0
        pD = 0
        # For que conta quantos ( e ) tem no texto
        for i in text:
            if i == "(":
                pE += 1
            if i == ")":
                pD += 1
                
        if pE != pD:
            self.Result['text'] = "Faltam parenteses!!!"
        elif not (text[-1].isdigit() or text[-1] == "." or text[-1] == ")"):
            self.Result['text'] = "operação inválida"
        else:
            self.Result['text'] = self.parentese(text)

    def parentese(self, s):
        """
        Método que seleciona os primeiros parenteses que devem ser calcu-
        lados
        """
        while True:
            if s.isdigit():
                return s
            if "(" not in s:
                s = self.converte(s, 0, len(s))
                return s

            parenteseE = 0
            parenteseD = 0
            for i, k in enumerate(s):
                if k == "(":
                    parenteseE = i
                elif k == ")":
                    parenteseD = i
                    p = self.converte(s, parenteseE + 1, parenteseD)
                    s = s[:parenteseE] + p + s[parenteseD+1:]
                    break



    def converte(self, s, indice1, indice2):
        """
        Método para fazer o cálculo da string
        """
        # Se a área selecionada dentro dos parenteses não puder ser calculada
        if s[indice1:indice2] == "" or s[indice1:indice2] == " ":
            return ""
        elif len(s[indice1:indice2]) <= 3 and s[indice1:indice2][1].isdigit():
            return s[indice1:indice2][1]

        # Se a área selecionada dentro dos parenteses puder ser calculada

        # Usando o split
        op = s[indice1:indice2].split(" ")
        for i in op:
            if i == " ":
                op.remove(i)
            elif i == "":
                op.remove(i)
        
        # Sem usar o split
        operands = [""]
        count = 0
        while False:
            if indice1 == indice2-1:
                break
            for i in range(indice1, indice2):
                if s[i].isdigit() or s[i] == ".":
                    indice1 = i
                    operands[count] += s[i]
                elif operands[count] != "":
                    count += 1
                    indice1 = i
                    break
            for i in range(indice1, indice2):
                if s[i] in ["+", "-", "*", "/"]:
                    operands.append(s[i])
                    operands.append("")
                    count += 1
                    indice1 = i
                    break

        while len(op) > 1:
            for i in range(0, len(op)):
                if i < len(op) and op[i] == "*":
                    op[i] = float(op[i-1]) * float(op[i+1])
                    op.pop(i + 1)
                    op.pop(i - 1)
                if i < len(op) and op[i] == "/":
                    op[i] = float(op[i - 1]) / float(op[i + 1])
                    op.pop(i + 1)
                    op.pop(i - 1)

            for i in range(0, len(op)):
                if i < len(op) and op[i] == "+":
                    op[i] = float(op[i-1]) + float(op[i+1])
                    op.pop(i + 1)
                    op.pop(i - 1)
                if i < len(op) and op[i] == "-":
                    op[i] = float(op[i - 1]) - float(op[i + 1])
                    op.pop(i + 1)
                    op.pop(i - 1)

        return str(op[0])


    def isNumeric(self, num):
        """
        Método para verificar se é um número
        """
        if num.isdigit() or num == ".":
            return True
        return False

    def isSymbol(self, symbol):
        """
        Método para verificar se é um símbolo de operações
        """
        if symbol in ["+", "-", "*", "/"]:
            return True
        return False


app = Calc()
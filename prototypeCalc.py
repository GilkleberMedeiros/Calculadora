def converte(s, indice1=0, indice2):
    indiceA = indice1
    indiceB = indice2
    operandA = ""
    while True:
        symbol = ""
        operandB = "0"
        operands = s[indiceA:indiceB].split(" ")
        print(operands)

        if indice1 == indice2-1:
            break
        if operandA == "":
            for i in range(indice1, indice2):
                if s[i].isdigit():
                    operandA += s[i]
                elif operandA != "":
                    indice1 = i
                    break

        for i in range(indice1, indice2):
            if s[i] in ["+", "-", "*", "/"]:
                symbol = s[i]
                indice1 = i
                break

        for i in range(indice1, indice2):
            if s[i].isdigit():
                indice1 = i 
                operandB += s[i]
            elif operandB != "":
                indice1 = i
                break

        if symbol == "+":
            operandA = int(operandA) + int(operandB)
        elif symbol == "-":
            operandA = int(operandA) - int(operandB)
        elif symbol == "*":
            operandA = int(operandA) * int(operandB)
        elif symbol == "/":
            operandA = int(operandA) / int(operandB)

        operandA = str(operandA)

    return s[:indiceA-1] + operandA + s[indiceB+1:]


def parentese(s):
    while True:
        parenteseE = 0
        parenteseD = 0
        for i, k in enumerate(s):
            if k == "(":
                parenteseE = i
            elif k == ")":
                parenteseD = i
                s = converte(s, parenteseE+1, parenteseD)
                print(s)

        if s.isdigit():
            break


parentese("5 + (6 / (7 + (0 + 5) + 2)")

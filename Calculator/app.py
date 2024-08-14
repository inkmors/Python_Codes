from os import system

def menu():
    print("\n=== |CALCULATOR| ===")
    print("____________________")
    print("|                  |")
    print("| 1. Soma          |")
    print("| 2. Subtração     |")
    print("| 3. Multiplicação |")
    print("| 4. Divisão       |")
    print("| 5. Potência      |")
    print("| 0. Sair          |")
    print("____________________")    

    operator = int(input("Escola uma das opções acima:"))
    if(operator is not 0):
        numberOne = float(input("Primeiro Valor:"))
        numberTwo = float(input("Segundo Valor:"))
        system('cls')   
    else:
        sair()
    
    return operator, numberOne, numberTwo


def sum(numberOne, numberTwo):
    result = numberOne+numberTwo
    print("O valor da operação é" f" {result}" "\n")
    return result

def subtrair(numberOne, numberTwo):
    result = numberOne-numberTwo
    print("O valor da operação é" f" {result}" "\n")
    return result

def multiply(numberOne, numberTwo):
    result = numberOne*numberTwo
    print("O valor da operação é" f" {result}" "\n")
    return result

def divide(numberOne, numberTwo):
    result = numberOne/numberTwo
    print("O valor da operação é" f" {result}" "\n")
    return result

def potencia(numberOne, numberTwo):
    result = numberOne**numberTwo
    print("O valor da operação é" f" {result}" "\n")
    return result

def sair():
    print("Saindo....")
    exit()

def escolhe(operator, numberOne, numberTwo):
    match operator:
        case 1:
            sum(numberOne, numberTwo)
        case 2:
            subtrair(numberOne, numberTwo)
        case 3:
            multiply(numberOne, numberTwo)
        case 4:
            divide(numberOne, numberTwo)
        case 5:
            potencia(numberOne, numberTwo)
        case 0:
            sair()
        case _:
            print("Opção incorreta, por favor siga os passos do menu")
            
if __name__ == "__main__":
    while True:
        operator, numberOne, numberTwo = menu()
        escolhe(operator, numberOne, numberTwo)

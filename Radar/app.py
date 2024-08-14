kmvia = 80
velocidade = int(input("Indique a velocidade do seu veiculo:"))
if velocidade > kmvia:
    limite = velocidade-kmvia
    multaatual = 20*limite
    print("você foi multado por está acima da velocidade! Valor da multa", multaatual)
else:
    print("Velocidade permitida!")
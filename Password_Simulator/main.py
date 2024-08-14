#A SENHA É 321

for tentou in range(3, 0, -1):
    senha = input("Digite a senha para desbloquear o celular: ")

    if senha == '321':
        print("Olá, Bem-vindo.")
        break
    else:
        print("Senha incorreta. Tentativas restantes:", tentou- 1)

else:
    print("Número máximo de tentativas atingido. Celular bloqueado.")
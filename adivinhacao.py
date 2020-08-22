print("*************************************")
print("* Bem vindo ao jogo de Adivinhação! *")
print("*************************************")

total_de_tentativas = 3
numero_secreto = 42

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número ente 1 e 100: "))
    print("Você digitou", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou. Seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou. Seu chute foi menor que o número secreto.")
    
    rodada = rodada + 1

print("Fim do jogo!!!")
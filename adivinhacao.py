print("*************************************")
print("* Bem vindo ao jogo de Adivinhação! *")
print("*************************************")

total_de_tentativas = 3
rodada = 1
numero_secreto = 42


while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou. Seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou. Seu chute foi menor que o número secreto.")
    
    rodada = rodada + 1

print("Fim do jogo!!!")
import random

print("Olá, bem-vindo, bom jogo!")

#definindo número a ser sorteado

numero_a_ser_descoberto = random.randrange(1,101)

#print(numero_a_ser_descoberto)

#variaveis
numero_de_tentativas = 0
tentativas = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil, (2) Médio, (3) Difícil")

nivel_de_dificuldade = int(input("Defina o nível"))

#print(nivel_dificuldade)

if(nivel_de_dificuldade == 1) :
    numero_de_tentativas = 10
elif(nivel_de_dificuldade == 2) :
    numero_de_tentativas = 5
else:
    numero_de_tentativas = 3

for tentativas in range(1, numero_de_tentativas + 1):
    print(f"Tentativa {tentativas} de {numero_de_tentativas}")
    chute_stri = input("Digite o seu chute: (1-100)")
    chute = int(chute_stri)

    if(chute < 1 or chute > 100):
        print("Opção inexistente")
        continue

    acertou = chute == numero_a_ser_descoberto
    maior = chute > numero_a_ser_descoberto
    menor = chute < numero_a_ser_descoberto

    print(f"O seu chute foi: {chute}")

    if(acertou):
        print(f"Você acertou! O número a ser descoberto era {numero_a_ser_descoberto}"
              f", seu placar foi: {pontos}")
        break
    else:
        if(maior):
            print("Você errou, seu palpite foi maior do que o número sorteado")
        elif(menor):
            print("Você errou, seu palpite foi menor do que o número sorteado")
            pontos_perdidos = abs(numero_a_ser_descoberto - numero_de_tentativas)
            pontos -= pontos_perdidos

print("Fim de jogo")

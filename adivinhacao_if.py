print('********************************')
print('Bem vindo ao jogo de adivinhacao')
print('********************************')

numero_secreto = 42

chute = input("Digite o seu número: ")
print("Você digitou:", chute)

acertou = int(chute) == numero_secreto
maior = int(chute) > numero_secreto
menor = int(chute) < numero_secreto

if (acertou):
    print("Você certou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo")

def jogar():

    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto (True)
    while not enforcou and not acertou:

        chute = input("Qual é a letra? ")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao = posicao + 1

        print(letras_acertadas)

    print("Fim do jogo")


# Quando rodamos o python, ele internamente cria uma variável "__name__". Se esta variável interna estiver criada e
# preenchida, sei que o Python rodou o arquivo. Abaixo, testamos se esta variável está preenchida com o valor especial "__main__"
if __name__ == "__main__":
    jogar()

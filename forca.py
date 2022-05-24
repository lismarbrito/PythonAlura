def jogar():

    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')


    print("Fim do jogo")

# Quando rodamos o python, ele internamente cria uma variável "__name__". Se esta variável interna estiver criada e 
# preenchida, sei que o Python rodou o arquivo. Abaixo, testamos se esta variável está preenchida com o valor especial "__main__"
if __name__ == "__main__":
    jogar()
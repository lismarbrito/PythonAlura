import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  # Vai preenchendo com anderline a cada iteração do for. Conhecido como List Comprehesions
    print(letras_acertadas)                                                               
    
    enforcou = False
    acertou = False
    erros = 0

    #enquanto (True)
    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_mensagem_vencedor():
    print("Você Ganhou!")

def imprime_mensagem_perdedor():
    print("Você Perdeu!")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1



def pede_chute():
    chute = input("Qual é a letra? ")
    chute = chute.strip().upper()
    return chute


def imprime_mensagem_abertura():
    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')

def carrega_palavra_secreta():
    # Abre o arquivo no modo leitura
    arquivo = open("palavras.txt", "r")
    palavras = []

    # Pega as palavras retiradas do arquivo e preenche a lista sem caracteres especiai(strip)
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    # Fecha o arquivo
    arquivo.close

    # Escolhe numero aleatoriamente do zero ao tamanho da lista (len)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()   
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

# Quando rodamos o python, ele internamente cria uma variável "__name__". Se esta variável interna estiver criada e
# preenchida, sei que o Python rodou o arquivo. Abaixo, testamos se esta variável está preenchida com o valor especial "__main__"
if __name__ == "__main__":
    jogar()
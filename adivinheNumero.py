import sys 
from random import randint
 
def saudar_usuario():
    print(
        "Bem Vindo ao jogo!"
        "Você acha que é capaz de acertar o número que estou pensando?"
        "Vamos lá! pensei em um número entre 1 e 100"
        "Tente descobrir! digite seu palpite!"
        "Não quer jogar? basta digitar *sair*."
    )

def checar_sair(palpite):
    if palpite.strip().lower() == "sair":
        print("Obrigador por jogar, volte logo")
        sys.exit()

def transformar_em_numero(palpite):
    try:
        palpite = int(palpite)
        return palpite
    except ValueError:
        return None

def checar_acerto(palpite, numero_aleatorio):
    if palpite > numero_aleatorio:
        print("muito alto! eu pensei em um numero menor. \n")
    elif palpite < numero_aleatorio:
        print("muito baixo! eu pensei em um numero maior. \n")
    else:
        print("parabéns! você acertou! \n")
        return True
    return False

def recomeçar_jogo_ou_sair():
    jogar = input("Jogar novamente?")
    if jogar.strip().lower() in ["s", "si", "sim"]:
        return
    
    print("Até a proxima!")
    sys.exit()

def advinhar_numero():
    saudar_usuario()
    numero_aleatorio = randint(1, 100)

    while True:
        palpite = input("Digite um número entre 1 e 100: ")
        checar_sair(palpite)

        palpite = transformar_em_numero(palpite)
        if palpite is None:
            print("Você devera digitar um número válido! tente novamente. \n")
            continue

        if 1 <= palpite <= 100:
            palpite_correto = checar_acerto(palpite, numero_aleatorio)
        else: 
            print("O número digitado deve estar entre 1 e 100! tente novamente. \n")
            continue
        
        if palpite_correto:
            checar_sair()
            saudar_usuario()
            numero_aleatorio = randint(1, 100)

if __name__ == "__name_":
    advinhar_numero()
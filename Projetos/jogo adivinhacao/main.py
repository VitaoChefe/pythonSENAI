import random

jogar_novamente = ""

while True:
    print(" bem vindo ao jogo de adivinhação")
    print("="*70)
    print("este e um jogo onde queremos desafiar o nosso participante")
    print("="*70)
    print("desejar inicial o jogo? \n[1] sim\n[0] sair")
    float(input("digite o numero "))
    print("="*70)
    print("o jogo funciona da seguinte maneira, um número é sorteado de 0 a 100, e vc tera que adivinhar, iremos lhe dar dica se o número que vc insirir sera menor ou maior")
    print("="*70)

    numero_aleatorio = random.randint(1, 100)

    while True:
        while True:
            try:
                usuario_numero = int(input("digite o numero "))
                if usuario_numero > 100 or usuario_numero < 1:
                    print("número inválido, tente de 1 - 100!")
                else:
                    break
            except ValueError:
                print("entrada invalida")

        if usuario_numero == numero_aleatorio:
            print("voce acertou")
            jogar_novamente = input("quer jogar novamente?\n[0]Sair\n[1]jogar novamente ")
            while jogar_novamente != "1" and jogar_novamente != "0":
                print("tente 1 ou 0")
                jogar_novamente = input("quer jogar novamente?\n[0]Sair\n[1]jogar novamente ")

                if jogar_novamente == "0":
                    print("ok encerrado")
                    break
                else:
                    numero_aleatorio = random.randint(1, 100)

        elif usuario_numero > numero_aleatorio:
            print("voce escolheu um numero maior")
        elif usuario_numero < numero_aleatorio:
            print("voce escolheu um numero menor")

        if jogar_novamente == "0":
            break

    if jogar_novamente == "0":
        break







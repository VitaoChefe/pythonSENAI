import random


print("jogo do par ou impar")
print("="*70)
print("escolha par ou impar e insira")
print("="*70)
print("este e um jogo onde queremos desafiar o nosso participante")
print("="*70)
input("desejar inicial o jogo? \n[1] sim\n[0] sair\n")
print("="*70)
print("o jogo funciona da seguinte maneira, voce deve escolher par ou ímpar e insira")
print("="*70)
while True:
    try:
        print("voce deseja ser par ou ímpar")
        escolha = input("[0]par\n[1]impar\n")
        numero_aleatorio = random.randint(1,10)
        if escolha == '0':
            numero_usuario = int(input("digite um numero: "))
            total = numero_usuario + numero_aleatorio
            print(f'CPU: {numero_aleatorio} + {numero_usuario} = {total}')
            if total % 2 == 0:
                print("ponto para vc")
            else:
                print("ponto para mim")

        if escolha == '1':
            numero_usuario = int(input("digite um numero: "))
            total = numero_usuario + numero_aleatorio
            print(f'CPU: {numero_aleatorio} + {numero_usuario} = {total}')
            if total % 2 == 0:
                print("ponto para mim,eu ganhei")
            else:
                print("ponto para vc,voce ganhou")

        while True:
            print("valor deu errado")
            jogar_novamente = input("Deseja jogar novamente?\n[0]sair\n[1]jogar novamente\n")

            if jogar_novamente == '0':
                break
            elif jogar_novamente == '1':
                break
            else:
                print("digite um numero valido")

        if jogar_novamente == '0':
            print("ok, encerrando")
            break

    except ValueError:
        print('entrada invalida')


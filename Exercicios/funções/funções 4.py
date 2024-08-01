def entrada_lado_1():
    while True:
        try:
            lado_1 = float(input('Digite o lado 1: '))
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')
    return lado_1


def entrada_lado_2():
    while True:
        try:
            lado_2 = float(input('Digite o lado 2: '))
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')
    return lado_2


def entrada_lado_3():
    while True:
        try:
            lado_3 = float(input('Digite o lado 3: '))
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')
    return lado_3


def classificacao_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_2 == lado_3:
        return 'equilátero'
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        return 'escaleno'
    else:
        return 'isóceles'


def exibir_mensagem(class_triangulo):
    print(f'O triângulo é {class_triangulo}')


lado_1 = entrada_lado_1()
lado_2 = entrada_lado_2()
lado_3 = entrada_lado_3()
class_triangulo = classificacao_triangulo(lado_1, lado_2, lado_3)
exibir_mensagem(class_triangulo)

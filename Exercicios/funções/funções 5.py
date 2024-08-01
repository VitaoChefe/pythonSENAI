def peso():
    while True:
        try:
            peso = float(input('Digite o peso (kg): '))
            if peso < 0:
                raise ValueError
            break
        except ValueError:
            print('Entrada invalida. Tente novamente.')
    return peso


def altura():
    while True:
        try:
            altura = float(input('Digite a altura (m): '))
            if altura < 0:
                raise ValueError
            break
        except ValueError:
            print('Entrada invalida. Tente novamente.')
    return altura


def calculo_imc(peso, altura):
    imc = peso / (altura*altura)
    return imc


def classificador(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso ideal'
    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 40:
        return 'Obesidade'
    elif imc >= 40:
        return 'Obesidade extrema'


def exibir_mensagem(imc, classificacao):
    print(f'Seu IMC é igual a {imc}, é considerado {classificacao}')


altura = altura()
peso = peso()
imc = calculo_imc(peso, altura)
classificacao = classificador(imc)
exibir_mensagem(imc, classificacao)

def menu():
    print("\nCalculadora de Ohm Calculadora")
    print("")
    print("0 - sair")
    print("1 - resistecia")
    print("2 - tensão")
    print("3 - corrente")
    print("4 - resistencia necessaria para um resistor")
    print("")
    opcao = int(input("qual opcao desejada: "))
    return opcao


def resistencia_calculo():
    print("resistencia")
    print("")
    while True:
        try:
            tensao = float(input("digite a tensao em volts: "))
            if tensao > 0:
                break
        except ValueError:
            print("valor invalido digite um numero utilizando o ponto como separador. Ex: 1.0")

    while True:
        corrente = float(input("digite a corrente em amperes: "))
        if corrente > 0:
            break

    resistencia = tensao / corrente
    #print(f"A resistencia é de {resistencia} 0")

    return resistencia


def tensao_calculo():
    print("tensao")
    print("")

    resistencia = float(input("digite a resistencia em ohms: "))
    corrente = float(input("digite a corrente em amperes: "))

    tensao = resistencia * corrente

    #print(f"A tensao e de {tensao} volts")
    return tensao


def corrente_calculo():
    print("corrente")
    print("")

    tensao = float(input("digite a tensao em volts: "))
    resistencia = float(input("digite a resistencia em ohms: "))

    corrente = tensao / resistencia

    #print(f"A corrente e de {corrente} amperes")
    return corrente


def resistencia_resistor_calulo():
    print("resistencia resistor")
    print("")
    tensao_fonte = float(input("digite a tensao da fonte em volts: "))
    tensao_dispositivo = float(input("digite a tensao do dispositivo em volts: "))
    corrente = float(input("digite a corrente em amperes: "))

    resistencia_resistor = (tensao_fonte - tensao_dispositivo) / corrente

    #print(f"A resistencia necessaria desse resistor e de {resistencia_resistor} 0")
    return resistencia_resistor

def exibir_resultado(unidade, resultado, un_medida):
    print(f'\n o valor da {unidade} é {resultado} ({un_medida})')
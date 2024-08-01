from utils import *

opcao = menu()

while opcao != 0:

    if opcao == 1:

        exibir_resultado('resistência', resistencia_calculo(), 'Ω')

    elif opcao == 2:
        exibir_resultado('tensão', tensao_calculo(), 'Volts')

    elif opcao == 3:
        exibir_resultado('corrente', corrente_calculo(), 'Amper')

    elif opcao == 4:
        exibir_resultado('resistência do resistor', resistencia_resistor_calulo(), 'Ω')

    else:
        print("opcao invalida")
        opcao = menu()


    opcao = menu()

print("fim do programa")
# while repete tudo que esta dentro dele
while True:
    # try vai tentar executar esse bloco de codigo
    try:
       idade = int(input('Digite sua idade: '))

       # o if verifica se idade é valida
       if idade > 0 and idade <= 100:
            print("idade:",idade)
            # o break sai do while
            break
       else:
             print("idade invalida")
    except ValueError:
         # caso der erro executa aqui
         print("digite sua idade em numero, ex: 26")
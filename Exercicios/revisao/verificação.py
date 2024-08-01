ano_de_nascimento = float(input('Digite o ano de nascimento: '))
if ano_de_nascimento >= 2024:
    print("ano de nascimento inserido é invalido")
idade = 2024 - ano_de_nascimento
if idade >= 120:
    print("impossivel voce tem essa idade")
elif idade >= 60:
    print(f"voce tem {idade} e é idoso")
elif idade >= 18:
    print(F"voce tem {idade} e é um adulto")
elif idade < 10:
    print(f"voce tem {idade} e é uma crianca")
elif idade > 11:
    print(F"voce tem {idade} e é um adolescente")

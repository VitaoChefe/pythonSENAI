nota = int(input('Digite a nota do aluno: '))
nota2 = int(input('Digite a nota do aluno: '))

resultado = nota + nota2 /2

if resultado >= 70:
    saudacao = 'Aprovado'

elif resultado < 50:
    saudacao = 'Reprovado'
print("devido a nota do aluno: ", saudacao)
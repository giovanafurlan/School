def calcular_nota(resp_, gab):
    nota = 0
    for x in range(len(gab)):
        if resp_[x] == gab[x]:
            nota = nota + 1
    return nota

num_questoes = int(input('Número de questões: '))
gabarito = input('Gabarito: ')
numAlunos = int(input('Quantidade de alunos: '))

if numAlunos>100:
    print('Número de alunos excedeu')

for i in range(numAlunos):
    resp = input('Resposta do aluno: ')
    nota = calcular_nota(resp, gabarito)
    media = (nota/num_questoes)
    print('Nota: ', media)

    if media >= 7 and media < 10:
        print('Aprovado')
    else:
        print('Reprovado')

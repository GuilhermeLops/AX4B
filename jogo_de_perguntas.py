# Jogo das perguntas
# O jogo das perguntas é um sistema que possui algumas perguntas, e precisamos responder de forma correta.
# No final ele exibe quantas perguntas foram acertadas.

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = ""

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    opcao_valida = ""

    while opcao_valida != True:
        escolha = input('Escolha uma opção: ')
        if escolha.isdigit() != True:
            print('Opção inválida!')
            print('Tente novamente!')
            continue
        else:
            escolha_int = int(escolha)
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['Resposta']:
                    acertou = True
                    opcao_valida = True
                print()
            else:
                print('A opção digitada não é uma opcão válida para esta pergunta')
                print('Tente novamente!')
                continue
            if acertou:
                qtd_acertos += 1
                print('Acertou')
            else:
                print('Errou')

            print()

            break        




print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

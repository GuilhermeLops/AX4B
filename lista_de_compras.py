# Lista de Compras
# O programa executa um menu com opções para inserir, apagar ou listar itens na sua lista de compras,
# também possui a opção de sair do programa caso desejar.

import os
import platform

def limpar_tela():
    os.system('cls' if platform.system() == "Windows" else 'clear')


lista_compras = []
menu_principal = ""

while True:
    print('Selecione uma opção desejada: ')
    opcao = input('[I]nserir [A]pagar [L]istar [S]air : ').lower()

    match opcao:

        case "i":
            limpar_tela()
            item = input('Digite o item que deseja adicionar: ')
            lista_compras.append(item)
            continue

        case "l":
            limpar_tela()
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
                

            continue

        case "a":
            limpar_tela()
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)

            excluir = input('Digite o número do item que deseja excluir: ')
            conversao = False

            while conversao != True:
                try:
                    exclusao = False
                    excluir = int(excluir)
                    conversao = True
                    for indice, nome in enumerate(lista_compras):
                        if excluir == indice:
                            del lista_compras[excluir]
                            print("Item excluído!")
                            exclusao = True

                    if exclusao == False:
                        print('Não foi possível excluir este item!')
                    continue
                        
                except:
                    print("Número do item não encontrado!")
                    break

            

            continue
        
        case "s":
            limpar_tela()
            input('Saindo do programa.')
            break

        case _:
            limpar_tela()
            input('Digite uma das opções listadas!')
            continue

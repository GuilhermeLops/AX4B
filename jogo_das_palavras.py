# Jogo das palavras
# Existe uma palavra secreta no sistema, você deverá digitar as letras para tentar adivinhar a palavra secreta,
# após adivinhar as letras, você deverá adivinhar as palavras com as letras que você acertou.
# O jogo termina quando você adivinhar a palavra.

import os
import platform


palavra_secreta = 'computador'  #palavra
palavra_palpite = ""
tamanho_input = 0
tamanho_txt = len(palavra_secreta)
tentativa = 0
letras_corretas = ""
letras_repetidas = []

while tamanho_txt > 0:
    # Enquanto houver letras restantes na palavra chave, o loop continua
    letra_digitada = input('Digite uma letra: ')
    tamanho_input = len(letra_digitada)
    tentativa += 1

    if tamanho_input == 0:
        # Caso nada tenha sido digitado
        print ('Você precisa digitar uma letra! ')
        continue

    elif tamanho_input == 1:
        # Executa caso algo tenha sido digitado
        if letra_digitada in palavra_secreta:
            # Verifica se a está na palavra secreta
            if letra_digitada not in letras_corretas:
                # Verifica se a letra já não foi digitada antes
                letras_repetidas_secreta = palavra_secreta.count(letra_digitada)
                letras_corretas += letras_repetidas_secreta * (letra_digitada + " | ")
                letras_repetidas.append(letra_digitada)
                tamanho_txt -= letras_repetidas_secreta

            else:
                print('Essa letra já foi digitada: ')
                print(f'Letras certas digitadas: {letras_corretas}')
                
            continue


        elif letra_digitada not in letras_repetidas:
            
            letras_repetidas.append(letra_digitada)
            print ('*Essa letra não está na palavra secreta')
            print (f'Letras já digitadas: {letras_repetidas}')
            continue

        else:
            print('Letra já digitada!')
            print (f'Letras já digitadas: {letras_repetidas}')


    else:
        print("Digite apenas uma letra!")


# Executa após acertar todas as letras da palavra secreta
os.system('cls' if platform.system() == "Windows" else 'clear')
print('Você acertou todas as letras!')
print('Fazem parte da palavra secreta as seguintes letras:')
print(letras_corretas)


palavra_palpite = input('Digite a palavra secreta: ').lower()
tentativa += 1
os.system('cls' if platform.system() == "Windows" else 'clear')


while palavra_palpite != palavra_secreta:
    print("Você errou a palavra, tente novamente!")
    print('Fazem parte da palavra secreta as seguintes letras:')
    print(letras_corretas)
    palavra_palpite = input("Digite novamente: ")
    tentativa += 1


os.system('cls' if platform.system() == "Windows" else 'clear')
print('Você acertou a palavra!!')
print(f'A palavra correta é: {palavra_secreta}')
print(f'Você precisou de {tentativa} tentativas')

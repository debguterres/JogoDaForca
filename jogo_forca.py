import re

print('#==============================================#')
print('# Bem vindo ao jogo da Forca!                  #')
print('#==============================================#')
print('# As regras são:                               #')
print('# Você precisa descobrir a palavra secreta.    #')
print('# Para isso você possui sete chances de errar  #')
print('# e uma chance de chutar a palavra inteira.    #')
print('# Boa sorte!!!                                 #')
print('#==============================================#')

palavra_secreta = 'python'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = []
numero_de_erros = 7

print(letras_acertadas)

while not acertou and not enforcou:

    chute = input('Qual letra?\n')

    if len(chute) > 1:
        print("Opa! Apenas um caractere de cada vez, por favor!")
        continue

    elif not re.match(r"[A-ZÇ]", chute.upper()):
        print("Opa! Só aceito letras! Por favor digite novamente.")
        continue

    elif chute in erros:
        print("Opa, esse erro você já cometeu. Por favor tente uma letra diferente.")
        print("Aqui esta(ão) a(s) letra(s) que você já errou: {}\n".format(", ".join(erros)))
        continue

    if chute in palavra_secreta:

        for index, letra in enumerate(palavra_secreta):
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra

        print('Você acertou a letra "{}".'.format(chute))
        print(letras_acertadas)

    else:
        print('Você errou. A letra "{}" não está na palavra secreta.'.format(chute))
        erros += chute
        print('Você ainda pode errar {} vezes.'.format(numero_de_erros - len(erros)))

    enforcou = len(erros) == numero_de_erros

    acertou = '_' not in letras_acertadas

    if len(erros) == numero_de_erros - 1:
        print('\nCalma, não se desespere. Você ainda pode chutar a palavra inteira e ganhar o jogo.')

        while True:
            deseja_palavra = input(
                'Você deseja chutar (S|N)?\n')

            if deseja_palavra.lower() == "s":
                chute_de_palavra = input('Digite a palavra:\n')

                if chute_de_palavra == palavra_secreta:
                    print('Parabéns! Você acertou!')
                else:
                    print('Oh nãaaaaaaao! Você errou!')
                    enforcou = True
                    break

            elif deseja_palavra.lower() == "n":
                break

            else:
                print('Essa opção não existe. Digite "S" ou "N".')


if acertou:
    print('Você ganhou!')
else:
    print('Que pena. Você perdeu!')

print('Fim do Jogo!')

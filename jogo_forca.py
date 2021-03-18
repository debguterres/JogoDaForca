import re
import random


def gerar_palavras_secretas():

    meses = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
    )

    return random.choice(meses)


def iniciar_jogo():

    palavra_secreta = gerar_palavras_secretas()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    return palavra_secreta, letras_acertadas


def executar_jogo(palavra, input_letras):

    acertou = False
    enforcou = False
    erros = []
    numero_de_erros = 7

    print(input_letras)

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
            print("Aqui esta(ão) a(s) letra(s) que você já errou: {}\n".format(
                ", ".join(erros)))
            continue

        if chute.upper() in palavra.upper():

            for index, letra in enumerate(palavra):
                if chute.upper() == letra.upper():
                    input_letras[index] = letra

            print('Você acertou a letra "{}".'.format(chute))
            print(input_letras)

        else:
            print('Você errou. A letra "{}" não está na palavra secreta.'.format(chute))
            erros += chute
            print('Você ainda pode errar {} vezes.'.format(
                numero_de_erros - len(erros)))

        enforcou = len(erros) == numero_de_erros

        acertou = '_' not in input_letras

        if len(erros) == numero_de_erros - 1:
            print(
                '\nCalma, não se desespere. Você ainda pode chutar a palavra inteira e ganhar o jogo.')

            while True:
                deseja_palavra = input(
                    'Você deseja chutar (S|N)?\n')

                if deseja_palavra.lower() == "s":
                    chute_de_palavra = input('Digite a palavra:\n')

                    if chute_de_palavra == palavra:
                        print('Parabéns! Você acertou!')
                    else:
                        print('Oh nãaaaaaaao! Você errou!')
                        enforcou = True
                        break

                elif deseja_palavra.lower() == "n":
                    break

                else:
                    print('Essa opção não existe. Digite "S" ou "N".')

    return acertou


def finalizar_jogo(acertou):

    if acertou:
        print('Você ganhou!')
    else:
        print('Que pena. Você perdeu!')

    print('Fim do Jogo!')


def main():

    print('#==============================================#')
    print('# Bem vindo ao jogo da Forca!                  #')
    print('#==============================================#')
    print('# As regras são:                               #')
    print('# Você precisa descobrir a palavra secreta.    #')
    print('# Para isso você possui sete chances de errar  #')
    print('# e uma chance de chutar a palavra inteira.    #')
    print('# Boa sorte!!!                                 #')
    print('#==============================================#')

    palavras, input_letras = iniciar_jogo()
    acertou = executar_jogo(palavras, input_letras)
    finalizar_jogo(acertou)


main()

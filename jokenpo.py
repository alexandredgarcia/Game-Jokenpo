# Programa simples simulando um game de JOKENPÔ

from random import randint
from time import sleep


def apresentar_menu():
    print('=+' * 16)
    print('GAME JOKENPÔ'.center(32))
    print('=+' * 16)
    print('\n\033[34mCOMANDOS:\033[m')
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    for indice, opcao in enumerate(opcoes):
        print(f'{opcao:>8}: [{indice}]')


def verificar_opção_jogador():
#Valida a entrada do usuário para garantir que seja um número válido.
    while True:
        try:
            opcao = int(input('\033[33mQual é a sua opção?  \033[m'))
            if opcao == 0 or opcao == 1 or opcao == 2:
                return opcao
            else:
                print('\033[31mOpção inválida! Por favor, digite 0, 1 ou 2.\033[m')
        except ValueError:
            print('\033[31mVocê não digitou um número válido. Por favor, digite 0, 1 ou 2.\033[m')


def temporizar_jogada_mensagem():
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)


def verificar_ganhador(jogador,computador):
# Usando constantes em maiúsculo para opções
    opcao = ('PEDRA', 'PAPEL', 'TESOURA')
    if jogador == computador:
        print(f'\033[33m EMPATAMOS!! Eu também joguei {opcao[jogador]} \033[m')
    else:
        if (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
            print(f'\033[34m PERDI! Eu joguei {opcao[computador]}. VOCÊ GANHOU!!!!\033[m')
        else:
            print(f'\033[31m GANHEI! Eu joguei {opcao[computador]}. VOCÊ PERDEU!\033[m')


def jogar():
    apresentar_menu()
    jogador = verificar_opção_jogador()
    computador = randint(0,2)
    temporizar_jogada_mensagem()
    verificar_ganhador(jogador,computador)

if __name__ == '__main__':
    jogar()


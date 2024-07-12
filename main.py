from packages.interface import *
from packages import *
from os import system
from time import sleep

choice=""
arq="clientes.txt"

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    if choice == "break":
        break
    
    menu("Clientes","verde")
    sleep(0.4)
    choice=opcao(["Clientes Cadastrados","Cadastrar Cliente","Sair"],"red")
    system('cls')
    if choice == 1:
        menu("Clientes Cadastrados","amarelo")
        lerArquivo(arq)
        print("-"*60)
        choice=opcao(["Configurar","Sair"],"red")
        system('cls')
        if choice == 1:
            menu("Clientes Cadastrados","amarelo")
            lerArquivo(arq)
            print("-"*60)

            choice=opcao(["Editar","Deletar","Sair"],"red")
            system('cls')
            if choice == 1:
                menu("Clientes Cadastrados","amarelo")
                lerArquivo(arq)
                print("-"*60)

                print("-"*60)
                cod=leiaInt("Digite o ID:")
                nome=str(input("Novo Nome:"))
                idade=leiaInt("Nova Idade:")
                print("-"*60)
                editar(arq,choice,cod,nome,idade)
                system('cls')
            elif choice == 2:
                menu("Clientes Cadastrados","amarelo")
                lerArquivo(arq)
                print("-"*60)

                print("-"*60)
                cod=leiaInt("Digite o ID:")
                print("-"*60)
                editar(arq,choice,cod)
                system('cls')
            else:
                pass
        else:
            pass
    elif choice == 2:
        menu("Cadastrar Clientes","amarelo")
        nome=str(input("Nome:"))
        idade=leiaInt("Digite um numero:")
        cadastrar(arq,nome,idade)
        system='cls'
    else:
        break
    
from packages.interface import *
from packages import *
from time import sleep
import os

os.system('cls')

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
    os.system('cls')
    if choice == 1:
        menu("Clientes Cadastrados","amarelo")
        lerArquivo(arq)
        print("-"*60)
        choice=opcao(["Configurar","Sair"],"red")
        os.system('cls')
        if choice == 1:
            menu("Clientes Cadastrados","amarelo")
            lerArquivo(arq)
            print("-"*60)

            choice=opcao(["Editar","Deletar","Sair"],"red")
            os.system('cls')
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
                os.system('cls')
            elif choice == 2:
                menu("Clientes Cadastrados","amarelo")
                lerArquivo(arq)
                print("-"*60)

                print("-"*60)
                cod=leiaInt("Digite o ID:")
                print("-"*60)
                editar(arq,choice,cod)
                os.system('cls')
            else:
                pass
        else:
            pass
    elif choice == 2:
        menu("Cadastrar Clientes","amarelo")
        nome=str(input("Nome:"))
        idade=leiaInt("Digite um numero:")
        cadastrar(arq,nome,idade)
        os.system('cls')
    else:
        break
    
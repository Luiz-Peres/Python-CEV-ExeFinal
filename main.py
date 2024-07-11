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
    
    menu("Clientes")
    sleep(0.4)
    choice=opcao(["Clientes Cadastrados","Cadastrar Cliente","Sair"])
    system('cls')
    if choice == 1:
        menu("Clientes Cadastrados")
        lerArquivo(arq)
    elif choice == 2:
        menu("Cadastra Clientes")
        pass
    else:
        break
    
from packages.interface import *
from packages import *
from os import system

choice=""
while True:
    if choice == "break":
        break
    menu("Clientes")
    choice=opcao(["Clientes Cadastrados","Cadastrar Cliente","Sair"])
    system('cls')
    
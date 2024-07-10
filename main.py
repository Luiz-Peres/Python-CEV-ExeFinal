from packages.interface import *
from packages import *
from os import system
from time import sleep

choice=""
while True:
    if choice == "break":
        break
    
    menu("Clientes")
    sleep(0.4)
    choice=opcao(["Clientes Cadastrados","Cadastrar Cliente","Sair"])
    system('cls')
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        break
    
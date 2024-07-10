from .interface import *
from time import sleep
from os import system

def menu(tit=""):
    print(bgCor("-"*60,"verde"))
    print(bgCor(f"{tit:^60}","verde"))
    print(bgCor("-"*60,"verde"))
    print("")

def opcao(op=[]):
    for c,v in enumerate(op):
        print("CHECKCHECKCHECK")
        print(c,v)
        print(f"{txtCor(c+1,"vermelho")}-{v}")
        print("")
        print("-"*60)
        sleep(0.8)
        check=str(input("Opção:"))
        try:
            check=int(check)
            return(check)
        except:
            print("ERRO: DIGITE UMA DAS OPÇÕES")
            system('cls')
from .interface import *
from time import sleep
from os import system

def menu(tit=""):
    print(bgCor("-"*60,"verde"))
    print(bgCor(f"{tit:^60}","verde"))
    print(bgCor("-"*60,"verde"))
    print("")

def opcao(op=[]):
    print("-"*60)
    for c,v in enumerate(op):
        print(f"{txtCor(c+1,"vermelho")}-{v}")
    print("-"*60)
    sleep(0.4)
    print("")
    while True:
        check=str(input("Opção:"))
        try:
            check=int(check)
            return(check)
        except:
            print("-"*60)
            print("ERRO: DIGITE UMA DAS OPÇÕES")
            print("-"*60)
            
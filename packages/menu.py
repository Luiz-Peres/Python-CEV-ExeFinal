from .interface import *
from time import sleep
from os import system


def menu(tit="",cor="reset"):
    print(bgCor("-"*60,cor))
    print(bgCor(f"{tit:^60}",cor))
    print(bgCor("-"*60,cor))
    print("")

def opcao(op=[],cor="reset"):
    print("-"*60)
    for c,v in enumerate(op):
        print(f"{txtCor(c+1,cor)}-{v}")
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
            
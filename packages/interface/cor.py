#Colorização do texto
def txtCor (x,y="reset"):
    if y.strip().upper() in "BLACKPRETO":
        return(f"\033[30m{x}\033[0m")
    elif y.strip().upper()  in "REDVERMELHO":
        return(f"\033[31m{x}\033[0m")
    elif y.strip().upper()  in "GREENVERDE":
        return(f"\033[32m{x}\033[0m")
    elif y.strip().upper()  in "YELLOWAMARELO":
        return(f"\033[33m{x}\033[0m")
    elif y.strip().upper()  in "BLUEAZUL":
        return(f"\033[34m{x}\033[0m")
    elif y.strip().upper()  in "MAGENTA":
        return(f"\033[35m{x}\033[0m")
    elif y.strip().upper()  in "CYANCIANO":
        return(f"\033[36m{x}\033[0m")
    elif y.strip().upper()  in "GRAYCINZA":
        return(f"\033[37m{x}\033[0m")
    elif y.strip().upper()  in "WHITEBRANCO":
        return(f"\033[97m{x}\033[0m")
    elif y.strip().upper() in "RESET":
        return("\033[0m")
    else:
        print("ERRO: PASSE UM PARAMETRO DE COR VALIDO")

#Colorização do fundo
def bgCor (x,y="reset"):
    if y.strip().upper() in "BLACKPRETO":
        return(f"\033[40m{x}\033[0m")
    elif y.strip().upper()  in "REDVERMELHO":
        return(f"\033[41m{x}\033[0m")
    elif y.strip().upper()  in "GREENVERDE":
        return(f"\033[42m{x}\033[0m")
    elif y.strip().upper()  in "YELLOWAMARELO":
        return(f"\033[43m{x}\033[0m")
    elif y.strip().upper()  in "BLUEAZUL":
        return(f"\033[44m{x}\033[0m")
    elif y.strip().upper()  in "MAGENTA":
        return(f"\033[45m{x}\033[0m")
    elif y.strip().upper()  in "CYANCIANO":
        return(f"\033[46m{x}\033[0m")
    elif y.strip().upper()  in "GRAYCINZA":
        return(f"\033[47m{x}\033[0m")
    elif y.strip().upper()  in "WHITEBRANCO":
        return(f"\033[100m{x}\033[0m")
    elif y.strip().upper() in "RESET":
        return("\033[0m")
    else:
        print("ERRO: PASSE UM PARAMETRO DE COR VALIDO")

def leiaInt(x):
    while True:
        y=str(input(x))
        try:
            y=int(y)
            return(y)
        except:
            print("-"*40)
            print(f"{'ERRO: DIGITE UM NUMERO':^40}")
            print("-"*40)
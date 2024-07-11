def arqExiste(x):
    try:
        a=open(x,"rt")
        a.close()
        return True
    except FileNotFoundError:
        return False
    
def criarArquivo(x):
    a=open(x,"wt+")
    a.close()

def lerArquivo(x):
    a=open(x,"rt")
    print(a.read())
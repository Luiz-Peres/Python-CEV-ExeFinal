

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
    for linha in a:
        dado = linha.split(";")
        dado[1] = dado[1].replace("\n","")
        print(f"{dado[0]}-{dado[1]:<29}{dado[2]:>29}")
    print("")
    a.close()

def cadastrar(arq,nome="desconhecido",idade=0):
    a=open(arq,"at")
    a.write(f"{nome};{idade}\n")
    print("Novo registro adicionado!")
    a.close()

def editar(arq,id,nome,idade):
    person=[]
    cadastros=[]
    a=open(arq,"rt")
    b=a.read()
    b=b.replace("\n",";")
    b=b.split(";")
    num=int(len(b)/3)
    z=0
    for x in range(num):
        for c in range(3):
            person+=[b[z]]
            z+=1
        cadastros+=[person[:]]
        person.clear()
        
    cadastros[id]=[id,nome,idade]
    a=open(arq,"w")
    for x in range(3):
        for c in range(3):
            if c != 2:
                a.write(f"{cadastros[x][c]};")
            else:
                a.write(f"{cadastros[x][c]}")            
        a.write("\n")
    
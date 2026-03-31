#Criação de media de notas com python
import os
def escreveArq(caminho,arquivo,linha_arq):
    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = "w"
        route = caminho+"/"+arquivo
        enc = "utf-8"
        if(os.path.exists(route)):
            tipo = "a"
        with open(route,tipo, encoding=enc) as file:
            file.write(linha_arq)

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_media):
    global dir
    global arq
    linha:str=""
    linha = (nm)+";"+str(nt1)+";"+str(nt2)+";"+str(nt3)+";"+str(nt4)+";"+str(vlr_media)+"\n"
    escreveArq(dir,arq,linha)

def med(n1,n2,n3,n4):
    med = ((n1+n2+n3+n4)/4)
    return med
def entrada():
    global nome
    global nota_1, nota_2, nota_3, nota_4, media
    nome = input("insira o nome do aluno\n")
    nota_1 = float(input("Insira a 1° nota:"))
    nota_2 = float(input("Insira a 1° nota:"))
    nota_3 = float(input("Insira a 1° nota:"))
    nota_4 = float(input("Insira a 1° nota:"))
    media = float(med(nota_1,nota_2,nota_3,nota_4))
    print(media)
    cadastro(nome,nota_1,nota_2,nota_3,nota_4,media)
def main():
    global nome
    global nota_1, nota_2, nota_3, nota_4, media
    global dir
    global arq
    nome=str("")
    nota_1 = float
    nota_2 = float
    nota_3 = float
    nota_4 = float
    media = float
    dir="/tmp/exercicios"
    arq="ex21.txt"
    os.makedirs(dir,exist_ok=True)
    os.chmod(dir,0o744)
    contador=0
    for contador in range(0,5):
        entrada()

if __name__ == "__main__":
    main()
#Ex38-Recebe 100 numeros inteiros e mostrar o maior e menor
import os
def gravar(c,linha_arq):
    global dir,arq
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo="w"
        rota=dir+"/"+arq
        enc="utf-8"
        if (os.path.exists(rota) and c > 0):
            tipo = "a"
        with open(rota,tipo,encoding=enc) as file:
            file.write(linha_arq)

def inserir(num,cont,fin):
    global maior,menor
    linha = str()
    if fin == False:
        linha = f"{num}\n"
        gravar(cont,linha)
    if fin == True:
        linha = f"Maior numero:{maior}\nMenor numero:{menor}"
        gravar(cont,linha)

def maior_menor():
    global maior,menor
    contador = int(0)
    final = bool(False)
    for contador in range(10):
        numero = int(input("insira um numero:"))
        if (numero > maior and numero>=0):
            maior = numero
        if(numero < menor and numero>=0)or(menor==0 and contador==0):
            menor = numero
        inserir(numero,contador,final)
    final = True
    inserir(numero,contador,final)

def main():
    global dir
    global arq
    global maior, menor
    maior = int(0) 
    menor = int(0)
    dir=r"/tmp/exercicios"
    arq="ex38.txt"
    os.makedirs(dir,exist_ok=True)
    os.chmod(dir,0o744)
    maior_menor()

if __name__ == "__main__":
    main()
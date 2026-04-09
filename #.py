#Ex36-some a serie 1+1/1!+1/2!.....+1/n!
import os
def gerar_arquivo(sum,cont):
    global dir,arq
    if (os.path.exists and os.path.isdir):
        tipo="w"
        rota=dir+"/"+arq
        enc="utf-8"
        if (os.path.exists(rota) and cont > 1):
            tipo = "a"
        with open(rota,tipo,encoding=enc) as file:
            file.write(str(sum)+"\n")

def fator_calc(num):
    fatorial=int(1)
    for i in range(1,num+1):
        fatorial = fatorial * i
    return fatorial


def serie(n):
    soma = int()
    for i in range(1,n+1):
        fat = fator_calc(i)
        soma = soma + (1/fat)
        gerar_arquivo(soma,i)

def main():
    global dir,arq
    dir = r"/tmp/exercicios"
    arq = "ex36.txt"
    os.chmod(dir,0o744)
    os.makedirs(dir,exist_ok=True)
    numero = int(input("Insira um numero:"))
    serie(numero)

if __name__ == "__main__":
    main()
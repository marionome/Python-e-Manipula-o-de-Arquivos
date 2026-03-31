#Tabuada com arquivos
import os
def multi(vlr,tab):
    res = vlr * tab
    return res

def gravar(c,rslt):
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = "w"
        arquivo = dir + "/" + arq
        enc = "utf-8"
        if (os.path.exists(arquivo) and c > 0):
            tipo = "a"
        linha = f"{c}+{valor}="+(str(rslt)) + ("\n")
        with open(arquivo,tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print("erro")

def main():
    global valor
    global dir
    global arq
    contador:int=0
    result:int=0
    dir="/tmp/exercicios"
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir,0o744)
    arq="ex34.txt"
    valor = int(input("Insira um valor entre 1 a 10:"))
    for contador in range(0,11):
        result = multi(valor,contador) 
        gravar(contador,result)
if __name__ == "__main__":
    main()
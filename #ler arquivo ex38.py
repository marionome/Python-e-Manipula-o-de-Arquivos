#ler arquivo ex38.py e pegar qualquer numero divisivel por 5 e registrar-lo
import os
def ler_arq(dir,arqu):
    rota = dir+"/"+arqu
    new_arq= dir+"/read38.txt"
    valor = int()
    c = int(0)
    if (os.path.exists(dir) and os.path.isdir):
        with open(rota) as file:
            for linha in file:
                
                linha.strip()
                if any(c.isalpha() for c in linha):
                    continue
                valor = int(linha)
                if valor%5 == 0:
                    tipo="w"
                    enc="utf-8"
                    if (os.path.exists(rota) and c > 0):
                        tipo="a"
                    with open(new_arq,tipo,encoding=enc) as file:
                        file.write(str(valor)+"\n")
                    c+=1
               
def main():
    global arq
    global dir
    dir = r"/tmp/exercicios"
    arq = "ex38.txt"
    os.chmod(dir,0o744)
    ler_arq(dir,arq)

if __name__ == "__main__":
    main()
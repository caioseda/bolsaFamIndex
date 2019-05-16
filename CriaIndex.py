import sys

#Feito em conjunto: Caio Seda e Gabriel Marques 

def primeiro(x):
   return x[0]

f = open("bolsa.csv","r")
i = open("index.txt","w")

data= []

f.seek(0,2)
tamanho = f.tell()

contador = 0

f.seek(0,0)
line = f.readline()

while f.tell() <tamanho:
    pos = f.tell()
    line =f.readline()
    coluna= line.split("\t")    
    nis = coluna[7]
    
    sub = [nis,pos]
   
    data.append(sub)
  
   #[nis1,nis2,nis3]

    contador = contador +1

print("\nLista preenchida\n")

data.sort(key = primeiro)

#escreve arquivo
for x in data:
    i.write(str(x[0])+":"+str(x[1])+"\n")
    print(str(x[0])+":"+str(x[1])+"\n")

print(len(data))
f.close()
i.close()
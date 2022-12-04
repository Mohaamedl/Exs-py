import os
pasta ="paises_conti\pasta\info.txt"

#_______________________________________________________________Functions________________________________________________________________________________
def writeInFile():
    with open(pasta,"r+", encoding="utf8") as file:
            isEmpty = os.path.getsize(pasta)
            pais = input("País      :")
            broken=False
            fileLines = file.readlines()
            
            for line in fileLines:
                if line.split(";")[0]==pais:
                    print("Este pais ja esta na lista. Tente outro.")
                    broken=True
            if broken==False:
                continente = input("Continente :")
                if isEmpty==0:
                    file.write(pais+";"+continente)
                else:
                    file.write("\n"+pais+";"+continente)
            else:
                return
#_________________________________________________________________________________________________________________________________________________

def consultaInfo():
    with open(pasta,'r',encoding="utf8") as file:
        print("\t\t País\t\t\t Continente")
        print('-------------------------------------------------------------------')
        fileLines = file.readlines()
        for nline in fileLines:
            line=nline.split(";")

            print("\t\t %s\t\t\t%s" %(line[0],line[1]))
#_________________________________________________________________________________________________________________________________________________
def consultaContiEnumP(conti,c):
    dict = {}
    with open(pasta,"r",encoding="utf8") as file:
        fileLines = file.readlines()
        for nline in fileLines:
            line = nline.split(";")
            continente = line[1].replace("\n","")
            pais = line[0]
            if continente in dict.keys():
                dict[continente].append(pais)
            else:
                dict[continente]=[pais]
    paises = dict[conti]
    nump=len(paises)
    if c =="conti":
        dict = {}
        print("\t\t paises:%s"%(paises))
    elif c=="num":
        print("Pelo ficheiro, no continente %s existem %d paises"%(conti,nump))

#_________________________________________________________________________________________________________________________________________________

def prog1():
    n=9
    while n!=0:
        n = int(input("Menu\n1 - Inserir País\n2 - Consultar países\n3 - Consulta por continente\n4 - Consulta nº de países num continente\n0 - sair do menu\n"))
        if n ==1:
            writeInFile()
        elif n==2:
            consultaInfo()
        elif n==3:
            continente = input("\t\tContinente:  ")
            consultaContiEnumP(continente,"conti")
        elif n==4:
            continente = input("\t\tContinente:  ")
            consultaContiEnumP(continente,"num")
    print("Bye Bye :))")

prog1()




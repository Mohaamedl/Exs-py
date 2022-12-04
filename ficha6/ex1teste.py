def imprimePalavras(texto1):
    pos = texto1.find(" ")
    cont_pal = 0
    while pos!= -1:
        pal = texto1[cont_pal:pos]
        print(pal)
        cont_pal+=1
        pos = texto1.find(" ", pos+1)

texto = input("texto") + " "
cont = imprimePalavras(texto)

print("o texto contem", cont)
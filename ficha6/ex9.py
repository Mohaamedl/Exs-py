lista = []
semana = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
semanaNova = []
for dia in semana:
    print(dia, ": ", end="")
    visitantes = int(input())
    lista.append(visitantes)

def numVisitantes(lista, semana, semanaNova):
    copiaLista = lista.copy()
    copiaLista.sort()
    copiaLista.reverse()
    print(copiaLista)
    for n in copiaLista:
        semanaNova.append(semana[lista.index(n)])
        print(semana[lista.index(n)])
    print(" ")

    for i in range(len(semana)):
        print(semanaNova[i], ": ", copiaLista[i])
numVisitantes(lista, semana, semanaNova)

soma = sum(lista)
media = float(soma/len(semana))
mediaFinal = round(media, 2)
print("a media é: ",mediaFinal)


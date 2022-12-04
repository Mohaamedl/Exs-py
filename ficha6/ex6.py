meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
listaPluviosidade = []
mesesNovos = []

for mes in meses:
    print("pluviosidade do mes", mes, ": ", end="")
    pluviosidade = int(input(""))
    listaPluviosidade.append(pluviosidade)

def funPluviosidade(meses, listaPluviosidade, mesesNovos):
    copiaLista = listaPluviosidade.copy()
    copiaLista.sort()
    for n in copiaLista:
        mesesNovos.append(meses[listaPluviosidade.index(n)])
    print(" ")
    for i in range(len(meses)):
        print("pluviosidade do mes ", mesesNovos[i], ": ", copiaLista[i])
funPluviosidade(meses, listaPluviosidade, mesesNovos)
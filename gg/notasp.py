notas =[]
listaPositivos = []
listaAlunos = []
listaPositivosAlunos = []

try:
    for i in range(10):
        alunos = input("indique o seu nome: ")
        listaAlunos.append(alunos)
        pontos = int(input("pontuacao: "))
        notas.append(pontos)
        if pontos < 0 or pontos > 20:
            raise ValueError
except ValueError:
    print("indique um valor entre 0 e 20")
except:
    print("erro no sistema, tente novamente")


def positiveList(notas, listaAlunos,listaPositivos,listaPositivosAlunos):
    for pontos in notas:
        if pontos >= 10:
            listaPositivos.append(pontos)
            listaPositivosAlunos.append(listaAlunos[notas.index(pontos)])
    print("pontuacoes positivas: ", listaPositivos)
    print("nome: ", listaPositivosAlunos)
    return 
positiveList(notas,listaAlunos,listaPositivos,listaPositivosAlunos)
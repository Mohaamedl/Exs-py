resposta = "S"
while resposta.upper() == "S":
    sexo = input("indique o seu sexo(F/M): ")
    idade = int(input("indique a sua idade: "))
    freqCardiaca = int(input("indique a sua frequencia cardiaca: "))
#determinamos a fmc dependendo do sexo indicado
    if sexo.upper() == "F":
        fmc = 226 - idade
        
    elif sexo.upper() == "M":
        fmc = 220 - idade
        
    #no seguinte passo, vamos ver a qual intervalo pertence a frequencia cardiaca indicada pelo utilizador
    if (fmc*0.50) <= freqCardiaca <= (fmc * 0.60):
        print("atividade moderada")
    elif (0.61 * fmc) <= freqCardiaca <= (0.70 * fmc):
        print("treino de resistencia")
    elif (0.71*fmc) <= freqCardiaca <= (0.80 * fmc):
        print("nivel aerobico")
    elif (0.81 * fmc) <= freqCardiaca <= (0.90 * fmc):
        print("nivel anaerobico")
    elif (0.91 * fmc) <= freqCardiaca <= fmc:
        print("red zone")
    else:
        print("aaaaaaa")

    resposta = input("Deseja indicar novos dados(S/N)") #se o utilizador indicar S, volta ao while, se nao o programa termina


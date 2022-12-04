import random
def generateNum(limMin,limMax,quant):
    list=[]
    try:
        for i in range(quant):
            list.append(random.randint(limMin,limMax))
    except:
        print("Error:404")
    else:
        return list

print("chaves: " ,generateNum(1,51,5))
print("estrelas: ",generateNum(1,12,2))
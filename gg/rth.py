def abunda(nInt):
    sum=0
    for i in range(nInt-1,0,-1):
        r = nInt % i
        if r == 0:
            sum+=i
    if sum>nInt:
        return "hehe boy"
    else:
        return "nop"


print(abunda(12))
print(abunda(21))
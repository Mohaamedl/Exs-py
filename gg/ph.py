def soma(n1,n2):
    sum=n1
    for l in range(n1,n2):
        sum+=l+1
    return sum


print(soma(1,3))
print(soma(3,6))
print(soma(10,11))
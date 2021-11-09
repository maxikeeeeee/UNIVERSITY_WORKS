def Laba(n,k):
    res = 0
    for i in range(1,n):
        if i %k == 0:
            res += i 
    return res 
n = int(input("Введите n"))
k = int(input("Введите k"))
print(Laba(n,k))

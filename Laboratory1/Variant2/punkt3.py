N = [1,2,3,-4,5,6,7,-8,9,10,0]
print(max(N))



J = []
M = []
for i in N:
    if i<0:
        M.append(i)
    elif(i>0):
        J.append(i)

print(sum(M)/len(M))
print(sorted(J, reverse=True))




    
vetor=[0,0,0,0,0]
for x in range(5):
    vetor[x]=int(input("quais são os números? "))

for y in range(4,-1,-1):
    vetor[y]= vetor[y]
    print(vetor[y], end=" ")



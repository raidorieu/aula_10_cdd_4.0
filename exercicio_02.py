alunos=int(input("quantos alunos tem na turma? "))
nomes=[]
for x in range(alunos):
    nomes.append(input("qual o nome do aluno? "))

for y in range(alunos):
    print(f"{nomes[y]} está na posição {y}. seu rank é: {y+1}.")



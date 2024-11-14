# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

alunos = []
total_alunos = 7

for i in range(0, total_alunos):
    aluno = []
    aluno.append(int(input("Informe a idade do aluno: ")))
    aluno.append(float(input("Informe a altura do aluno: ")))
    alunos.append(aluno)
    
somaAltura = 0.0
for aluno in alunos:
    somaAltura += aluno[1]
    
mediaAltura = somaAltura / float(total_alunos)

total_alunos_altos = 0
for aluno in alunos:
    if (aluno[0] > 13) and (aluno[1] < mediaAltura):
        total_alunos_altos += 1
        
print(f"O total de alunos com idade > 13 abaixo da media de altura é {total_alunos_altos}")
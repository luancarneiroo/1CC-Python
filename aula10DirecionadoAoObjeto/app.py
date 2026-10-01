from disciplina import Disciplina
from aluno import Aluno

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456","Ciencia da computação")

# criar instanciar
sers = Disciplina ("soluções renovaveis","andré")
dsa = Disciplina("data strucutures", "erick")

#MATRICULAR o aluno
aluno1.matricular(sers)
aluno1.matricular(sers)
# print(aluno1.disciplinas[1].nome)

# ATRIBUTO
aluno1.adicionar_notas(sers, 10)
aluno1.adicionar_notas(sers, 8)
aluno1.adicionar_notas(dsa, 5)
aluno1.adicionar_notas(dsa, 3)

print (aluno1.calcular_media(dsa))
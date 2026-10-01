class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"disciplina:, {self.nome} | (professor: ,{self.professor}")

# temporario
# prompt_ia = disciplina("prompt ia", professor="Jorge")
# print(prompt_ia.nome)
# # print(prompt_ia.exibir_infos())
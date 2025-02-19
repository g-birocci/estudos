import json
from instrutor import Instrutor
from aluno import Aluno
from usuario import Usuario

class Base:
    def __init__(self):
        self.alunos = []
        self.instrutores = []
        self.cursos_disponiveis = {
            1: "TI",
            2: "Programador",
            3: "Web Developer",
            4: "Front End",
            5: "Back End",
        }

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

    def add_instrutor(self, instrutor):
        self.instrutores.append(instrutor)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno.exibir_info())

    def listar_instrutores(self):
        for instrutor in self.instrutores:
            print(instrutor.exibir_info())

    def salvar_usuarios(self, arquivo):
        usuarios = self.alunos + self.instrutores
        usuarios_dict = [usuario.to_dict() for usuario in usuarios]
        with open(arquivo, 'w') as f:
            json.dump(usuarios_dict, f, indent=4)

    def carregar_usuarios(self, arquivo):
        with open(arquivo, 'r') as f:
            usuarios_dict = json.load(f)
            for user_dict in usuarios_dict:
                if user_dict['tipo'] == 'aluno':
                    usuario = Aluno(user_dict['nome'], user_dict['email'], user_dict['cursos_inscritos'])
                    self.alunos.append(usuario)
                elif user_dict['tipo'] == 'instrutor':
                    usuario = Instrutor(user_dict['nome'], user_dict['email'], user_dict['cursos_ministrados'])
                    self.instrutores.append(usuario)
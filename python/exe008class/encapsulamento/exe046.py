class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas = []

    # Getter
    @property
    def nome(self):
        return self.__nome  
    
    def add_notas(self, lista):
        if all(isinstance(nota, (int, float)) and 0 <= nota <= 10 for nota in lista):
            if len(lista) == 3:
                self.__notas = lista
            else:
                print("A lista deve conter exatamente 3 notas.")
        else:
            print("Nota inválida encontrada!")

    @property
    def media(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        return 0.0

    @property
    def notas(self):
        return self.__notas.copy()




aluno = Aluno("João")
aluno.add_notas([8, 9, 10])
print(aluno.media) 
aluno.add_notas([7, 5, 11])  
print(aluno.media)  
aluno.notas = [10, 10, 10]  
    
'''
Exercício 7: Falsy Truthy

Crie uma função que receba um dicionário onde as chaves são nomes de alunos e os valores são as suas notas (ou None se a nota não estiver disponível). A função deve calcular a média das notas disponíveis e retornar um dicionário com as chaves "aprovados" e "reprovados", onde "aprovados" são os alunos com notas acima ou iguais à média e "reprovados" são os alunos com notas abaixo da média. Os alunos sem notas (None) não devem ser incluídos na média nem na classificação.
'''

def classificar_alunos(notas_alunos):

    notas_aceitas = [nota for nota in notas_alunos.values() if nota is not None]

    media = sum(notas_aceitas) / len(notas_aceitas)

    aprovado = [aluno for aluno, nota in notas_alunos.items() if nota is not None and nota >= media]
    reprovado = [aluno for aluno, nota in notas_alunos.items() if nota is not None and nota < media]
    
    return {"aprovado": aprovado, "reprovado": reprovado}


notas_alunos = {
    "Ana": 16,
    "Bruno": 14,
    "Carlos": None,
    "Diana": 10,
    "Eduardo": 18,
    "Fábio": None,
    "Gabriela": 12
}

resultado = classificar_alunos(notas_alunos)
print(resultado)
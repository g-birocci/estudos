import json
import requests

CHAVE_API = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MDRjZWQ0YzlkNTAyMDEwZTNmM2MxODliNDNiNmQxOCIsIm5iZiI6MTczOTg4OTA4Mi4yNTUsInN1YiI6IjY3YjQ5OWJhYTY1ZDYzMDNlN2UxMGVjYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gVFPoy5BQw3gJAp7oresyw8r3QkXfQeLe7ChKG33sWA"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {CHAVE_API}"
}

URL_FILMES = "https://api.themoviedb.org/3/movie/top_rated"

def buscar_filmes_melhor_avaliados():
    resposta = requests.get(URL_FILMES, headers=HEADERS)
    if resposta.status_code == 200:
        filmes = resposta.json()['results'][:10]  
        return filmes
    else:
        print(f"Erro na requisição: {resposta.status_code}")
        return []

def salvar_filmes_json(filmes, nome_arquivo="top_10_filmes.json"):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(filmes, arquivo, ensure_ascii=False, indent=4)

def exibir_filmes(filmes):
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['title']} ({filme['release_date']}) - Nota: {filme['vote_average']}")

def main():
    filmes = buscar_filmes_melhor_avaliados()
    if filmes:
        salvar_filmes_json(filmes)
        exibir_filmes(filmes)

if __name__ == "__main__":
    main()
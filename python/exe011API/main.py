import requests
import json
#from filme import Film

url = "https://api.themoviedb.org/3/movie/top_rated"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTFmMjVmN2M3NTUyNTk2MmRlYzk0ODRjYzA1ZjNiYyIsIm5iZiI6MTczOTkwNjAxMi42MzkwMDAyLCJzdWIiOiI2N2I0ZGJkY2VlMDc1Nzk2OTM1ODMzNmMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ohwXd02kBpeoW_-knKRskWCRYIlEKm54JMX0j5a0zkM"
}

response = requests.get(url, headers=headers)

info = response.json()

with open("film.json", "w", encoding="utf-8") as arquivo:
    json.dump(info, arquivo, indent=4, ensure_ascii=False)

print("Dados salvo com sucesso!")


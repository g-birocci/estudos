import requests

url = "https://api.themoviedb.org/3/authentication"
url = "https://api.themoviedb.org/3/tv/series_id/season/season_number/episode/episode_number/images"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTFmMjVmN2M3NTUyNTk2MmRlYzk0ODRjYzA1ZjNiYyIsIm5iZiI6MTczOTkwNjAxMi42MzkwMDAyLCJzdWIiOiI2N2I0ZGJkY2VlMDc1Nzk2OTM1ODMzNmMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ohwXd02kBpeoW_-knKRskWCRYIlEKm54JMX0j5a0zkM"
}

response = requests.get(url, headers=headers)

print(response.text)



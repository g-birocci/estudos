import os
from classe import WeatherData

if __name__ == "__main__":
    
    caminho_atual = os.path.dirname(__file__)
    caminho_dados = os.path.join(caminho_atual, 'dados.json') # temho que usar isso sempre para o VSCODE funcionar
    #Não esquecer !!!!!!

    weather = WeatherData(0, 0, 0)
    dados_climaticos = weather.deserializar(caminho_dados)   

    for dado in dados_climaticos:
        print(f"Temperatura: {dado.temperatura}, Humidade: {dado.humidade}, Pressão: {dado.pressao}")


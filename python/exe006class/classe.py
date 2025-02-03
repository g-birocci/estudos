# classe.py
import json

class WeatherData:
    def __init__(self, temperatura, humidade, pressao):
        self.temperatura = temperatura
        self.humidade = humidade
        self.pressao = pressao

    def deserializar(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as file: #abre o arquivo
            dados = json.load(file)
            
            lista_dados = [] #com essa lista eu vou adicionar as informação dos dados lidos
            for item in dados: #faço o ciclo pra ler todos dados no arquivo
                temperatura = item.get('temperature')
                humidade = item.get('humidity')
                pressao = item.get('pressure')

                lista_dados.append(WeatherData(temperatura, humidade, pressao)) #add a minha lista pra retorna para o meu main
            
            return lista_dados

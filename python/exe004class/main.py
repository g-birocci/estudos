import json
from sensor import SensorData

if __name__ == '__main__':
    dados = SensorData(temperatura=22, humidade=55, pressao=1012) # Criando um objeto da classe SensorData
    arquivo_json = "sensor_data.json" # Caminho do arquivo JSON
    dados.serializar(arquivo_json) #utilizo o meu objeto para usar o meu metodo criado na clase

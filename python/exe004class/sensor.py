import json
class SensorData:
    def __init__(self, temperatura = 0, humidade = 0, pressao = 0): #Posso ou não já colocar os valores na var.
        self.temperatura = temperatura
        self.humidade = humidade
        self.pressao = pressao
        

    def serializar(self, json_file): # no paramentro eu coloco o nome que eu quiser.
        tempo = self.__dict__  #Transfora em dicionario.
        with open(json_file, "w", encoding = "utf-8") as arquivo:
            json.dump(tempo, arquivo, indent = 4)
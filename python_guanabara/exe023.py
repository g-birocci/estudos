import math
angulo = float(input("Digite o valor do angulo: "))

angulo_rad = math.radians(angulo) #converte o valor para radianos

seno = math.sin(angulo_rad) #sin calula o ceno
coseno = math.cos(angulo_rad) #cos calcula o cosceno 
tangente = math.tan(angulo_rad) #tan calcula a tangente

print(f"O valor do angulo {angulo}º: seno é {seno:.2f}.")
print(f"O valor do angulo {angulo}º: o cesseno é {coseno:.2f}")
print(f"O valor do angulo {angulo}º: o tangente é {tangente:.2f}")

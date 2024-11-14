alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(text, shift):
    texto = ""
    if shift > 26:
        shift = 26
    for letra in text:
        pos = alphabet.index(letra)
        des = (pos + shift) %26
        texto += alphabet[des]
    return texto

def decrypy(text, shift):
    texto = ""
    if shift > 26:
        shift = 26
    for letra in text:
        pos = alphabet.index(letra)
        des = (pos - shift) %26
        texto += alphabet[des]
    return texto

if __name__ == "__main__":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    match direction:
        
        case "encode":
            print(encrypt(text, shift))
    
        case "decode":
            print(decrypy(text, shift))

        case "":
            print("Opção inválida seu burro!")


#A Fazer - 1: Crie uma função chamada 'encrypt' que recebe 'text' e 'shift' como entradas.

    #A Fazer - 2: Dentro da função 'criptografar', desloque cada letra do 'text' para frente no alfabeto pela quantidade de deslocamento e retorna o texto criptografado.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Alerta de bug: o que acontece se você tentar codificar a palavra 'civilization'?🐛

#A Fazer - 3: Crie uma função diferente chamada 'decrypt' que recebe 'text' e 'shift' como entradas.

    #A Fazer - 4: Dentro da função 'decrypt', desloque cada letra do 'text' *para trás* no alfabeto pela quantidade de deslocamento e retorna o texto descriptografado.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"


    #A Fazer - 4: Verifique se o usuário deseja criptografar ou descriptografar a mensagem verificando a variável ‘shift’. Em seguida, chame a função correta com 
    # base nessa 'shift' variável. Você deve ser capaz de testar o código para criptografar *E* descriptografar uma mensagem.
let array = []

function addarray() {

    let num = document.getElementById("txtnum").value;

    if (num == "") {
        window.alert("é nessesario digitar um numero pra adiocinar")
    } else if (num < 1 || num > 200) {
        window.alert("O numero tem que ser entre 1 e 200")
    } else {
        array.push(Number(num))
    }

    document.getElementById("resultado").innerHTML = "O primeiro elemento é " + array[0] + "<br>" + " todos os elementos são: " + array.join(", ");
}

function finalizar() {
    let max = Math.max(...array);
    let min = Math.min(...array);
    let total = array.length
    let soma = 0
    let media = 0

    for (let x = 0; x < array.length; x++) {
        soma += array[x]   
    }
    media = (soma / array.length)

    document.getElementById("final").innerHTML =
    "O maior elemento é " + max + "<br>" +
    "O menos elemento é " + min + "<br>" +
    "A soma total dos elementos é " + soma + "<br>" +
    "A media entre os elemntos é " + media.toFixed(2); //formata pra duas casas 
}

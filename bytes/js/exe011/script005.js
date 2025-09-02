function arrey(i) {
    let lista = []

    if (i <= 0) {
        return "O numero tem que ser maior que '0'. "
    } else {
        for (let j = 0; j < i; j++) {
            lista.push(j)
        }
        return lista
    }
}

let numero = 30
let resp = arrey(numero)
console.log(resp)
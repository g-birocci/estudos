function checkpay(a,b) {
    cont = 0

    if (a === b) {
        return "Por favor introduz valores diferentes!"
    } else if (a > b) {
        return "O priemro valor tem que ser menor que o segundo."
    } else {
        for (let i = a; i <= b; i++) {
            if (i % 2 == 0) {
                cont++
            }       
        }
        return "Existe " + cont + " numeros pares entre " + a + " e " + b;
    }
}

let c = 100
let d = 1000

let resultado = checkpay(c, d)
console.log(resultado)
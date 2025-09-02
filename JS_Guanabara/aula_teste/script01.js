function parimp(num) {
    if (num % 2 === 0) {
        return "Par"
    } else {
        return "Ímpar"
    }
}

let cal = parimp(9)
console.log(cal)


function soma(n1 = 0, n2 = 0) { //eu posso declarar já o valor do parametro caso eu passe apenas um parametro e for passaso apenas um valor na chamada da função.
    return n1 + n2
}

let res = soma(34, 80)
console.log(res)
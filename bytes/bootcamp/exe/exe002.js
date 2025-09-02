function umOuOutro (a, b, c) {
    //return (a || b || c) //retorna apenas se um deles for verdadeiro

    return (a && !b && !c) || (!a && !b && c) || (!a && b && !c) //retorna treu se tem apenas verdadeiro
}

console.log(umOuOutro(true, true, true))
console.log(umOuOutro(false, true, false))
console.log(umOuOutro(true, false, true))
console.log(umOuOutro(false, false, false))

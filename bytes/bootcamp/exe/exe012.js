function garanteComprimentoDaString (string, n) {
    if (string.length < n) {
        string = string.padEnd(n, "*") //Função pra adicionar caraterer a uma string
        return string
    } else if (string.length > n) { 
        return string.substring(0, n) //Ela conta a string e só imprime a quantiade de carater 

    } else {
        return string
    }
}

console.log(garanteComprimentoDaString("abcdefghik", 6))
//console.log(garanteComprimentoDaString(string.length))~


function somatorioAteN(n){
    let x = 0;
    let soma = 0

    while (x <= n) {
        soma += x
        x++
    }
    return soma
}

console.log(somatorioAteN(10))
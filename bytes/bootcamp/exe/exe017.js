function superDigito(string) {

    let soma = 0;

    if (string.length === 1) {
        return parseInt(string)
    }
    
    for (let digito of string) {
        soma += parseInt(digito)
    }

    return superDigito(soma.toString())
}

console.log(superDigito("1"))
console.log(superDigito("12"))
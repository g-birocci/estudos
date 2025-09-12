function map (array) {
    return  arrayNumerosDeCaracter = array.map(palavra => palavra.length)
}

function mapOrdena (array) {
    return arrayPalavrasOrdenadas = array.sort(((a, b) => a.length - b.length)); //uso o leng para contar o tamnho da string para ordena da > para a <.
}

function mapAlfabeto(array) {
     return [...array].sort((a, b) =>  a.toLowerCase().localeCompare(b.toLowerCase())
  );
}

const arrayPalavras = ["ewfefe", "gabriel", "freire", "amor", "ester", "pipoca","let", "neguinha","Pipoca"]

console.log(map(arrayPalavras))
console.log(mapOrdena(arrayPalavras))
console.log(mapAlfabeto(arrayPalavras))
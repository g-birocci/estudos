function contaParesRec(arr) {
    if (arr.length === 0) return 0; // caso base: array vazio

    let primeiro = arr[0];
    let resto = arr.slice(1);

    if (primeiro % 2 === 0) {
        return 1 + contaParesRec(resto);
    } else {
        return contaParesRec(resto);
    }
}

let array = [2,3,77,54,33,55,33,233,66,56,6];

console.log(`Tem ${contaParesRec(array)} números pares neste array`);


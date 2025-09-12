function pares (arr) {
    return arr
        .filter(x => x % 2 === 0)
        .map(x => (x ** 2))
        .reduce((acc, n) => acc + n, 0);
}

const numeros = [2,3,6,67,43,113,3,64,42,2,3,43,2,3,22,2,2]

console.log(pares(numeros))

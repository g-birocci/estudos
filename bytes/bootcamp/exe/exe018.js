function minMax(lista, n) {

    max = 0
    min = 0

    for (let i = 1; i <= n; i++) {
        lista.sort((a,b) => a - b)
        max += lista[i]
    }

    for (let i = 1; i <=n; i++) {
        lista.sort((a,b ) => b - a)
        min += lista[i]
    }

    return max + " " + min
}

let listas = [3,1,25,23,1,6,4]
console.log(minMax(listas, 2))
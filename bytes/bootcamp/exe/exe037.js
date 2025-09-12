function todosPar (arr) {
    return arr.every(n => n % 2 === 0)
}

const numeros = [3,2,4,3,2,4,2,4,2]
const numeross = [2,4,2,2,2,]

console.log(todosPar(numeros))
console.log(todosPar(numeross))
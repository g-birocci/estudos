let array = [1,3,12,4,6,3,5,6,7,42,1]

array.sort((a,b) => a - b) //ordena os numeros

console.log(array)

array.push(2,4,5)

console.log(array)

for (let n in array) {
    console.log(array[n])
}

let pos = array.indexOf(9) //retorna o index do valor se existir no array, se não tiver ele retorna (-1)
console.log(pos)
console.log(array)
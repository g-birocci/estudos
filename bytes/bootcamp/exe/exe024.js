function removeDuplicados (array) {

    let novo = [];

    for (let n of array) {
        if(!novo.includes(n)) {
            novo.push(n);
        }
    }
    return novo
}

let array = [3,2,4,2,24,4,5,3,4,43,4,4,3]

console.log(removeDuplicados(array))

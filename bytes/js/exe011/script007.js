function validaarrey(arrey) {
    let arreyBase = [1,2,3,4,5]
    let i = 0 //Declara a varaivel pra interagir

    for (let j = 0; j < arreyBase.length; j++) {
        if (arreyBase[j] === arrey[i]) { //Compara os arrey pelo valor do elemento e se um elemento for igual ele incrementa no i
            i++
        }
        if (i === arrey.length) { // se o i for igual ao tamnho do arrey, significa que todos os elemento existe no arrey
            return true
        }
    }
    return false

}

let arrey = [1,4,2]
resp = validaarrey(arrey)
console.log(resp)
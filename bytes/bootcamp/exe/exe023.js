function removerDuplicados (arrey) {
    const  novo = new Set(arrey)
        return [...novo] // usar o ... faz pra retorna em array 
}


let arrey = ([2,66,44,66,77,66,7,66,2])
console.log(removerDuplicados(arrey))
console.log(arrey)
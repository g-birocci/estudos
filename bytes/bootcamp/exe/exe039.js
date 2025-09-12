function pessoa (arr) {

    const updateinfo = arr.map(newobj => {return {...newobj, age: "27"}})
    //         var       array pra criar o novo array     retorna o mesmo copiado + o age
    return updateinfo
}

const info = [{name: "Gabriel",birthday: "1997-09-27"}]
console.log(pessoa(info))

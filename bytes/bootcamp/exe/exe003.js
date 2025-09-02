function contrarioDoE (a,b) {
    return (!a && b) || (a && !b) || (!a && !b) 

}

console.log(contrarioDoE(true, true))
console.log(contrarioDoE(false, true))
console.log(contrarioDoE(true, false))
console.log(contrarioDoE(false, false))
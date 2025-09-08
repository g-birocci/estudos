class Inteiro{
    constructor (n) {
        this.n = n
    }

    static nulo = 0;

    static eInteiro(n) { //verefica de o numero é interiro
        return Number.isInteger(n) 
    }

}

console.log(Inteiro.nulo);
console.log(Inteiro.eInteiro(10))
console.log(Inteiro.eInteiro(2.5))
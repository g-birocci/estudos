class SoInteiro {

    #segredo = 0;

    get Inteiro() {
        return this.#segredo
    }


    set Inteiro(n) {
    if (Number.isInteger(n)) {
        this.#segredo = n;
    }
}
}

const a = new SoInteiro()
console.log(a.Inteiro)
a.Inteiro = 40
console.log(a.Inteiro)
29
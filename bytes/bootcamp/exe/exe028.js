class Porta {
    constructor(trinco = false) {
        this.trinco = trinco
    }

    trancar() {
        this.trinco = true;
        return ("Aporta foi trancada.");
    }

    destrancar() {
        this.trinco = false
        return ("A porta foi aberta")
    }

    toString() {
        return this.trinco ? "Aberta" : "Fechada";
    }
}


class PortaBlindada extends Porta {
    constructor() {
        super(false);
        this.trincoSuperior = false
        this.trincoInferior = false
        this.trincoTraseiro = false
    }

    trancar() {
        super.trancar();
        this.trincoSuperior = true
        this.trincoInferior = true
        this.trincoTraseiro = true
        return "A porta foi trancada"
    }

    destrancar() {
        super.destrancar();
        this.trincoSuperior = false
        this.trincoInverior = false
        this.trincoTraseiro = false
        return "A Porta foi aberta"
    }
}
//const p = new PortaComTrinco();
const p = new Porta();

//console.log(p.toString())
//console.log(p.destrancar())

const PBlindada = new PortaBlindada()

console.log(PBlindada.destrancar())
console.log(PBlindada.trancar())


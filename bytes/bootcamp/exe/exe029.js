class Retangulo {
    constructor(altura, largura) {
        this.altura = altura
        this.largura = largura

    }
    calcularArea() {
        return this.altura * this.largura
    }

}

class Quadrado extends Retangulo {
    constructor(lado) {
        super(lado, lado); //chama o constructor da classe base, passando os mesmo parametro
    }
}

const area = new Retangulo(10,5)
console.log(area.calcularArea());

const q = new Quadrado(10);
console.log(q.calcularArea())
class Pasta {
    constructor(nome) {
        if (this.constructor === Pasta) { // só aplica singleton se for a própria Pasta
            if (Pasta.instancia) {
                return Pasta.instancia;
            }
            this.nome = nome;
            this.itens = [];
            Pasta.instancia = this;
        } else {
            // se for subclasse, não aplica singleton
            this.nome = nome;
            this.itens = [];
        }
    }

    adicionar(item) {
        this.itens.push(item);
    }

    imprimir() {
        return {
            pasta: this.nome,
            conteudo: this.itens.map(i => i.imprimir())
        };
    }
}

class Documento extends Pasta {
    constructor(nome) {
        super(nome); // agora cria um objeto normal (sem singleton)
        this.nomeDoc = nome;
    }

    imprimir() {
        return this.nomeDoc;
    }
}

// 🔹 Testando
const raiz1 = new Pasta("Meus Arquivos");
const raiz2 = new Pasta("Outro Nome");

console.log(raiz1 === raiz2); // true ✅ (singleton só na raiz)

const doc1 = new Documento("Contrato.pdf");
const doc2 = new Documento("Relatório.docx");

raiz1.adicionar(doc1);
raiz1.adicionar(doc2);

console.log(raiz1.imprimir());
/*
{
  pasta: 'Meus Arquivos',
  conteudo: [ 'Contrato.pdf', 'Relatório.docx' ]
}
*/

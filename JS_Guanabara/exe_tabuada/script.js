function gerarTabuada() {
    let numero = Number(document.getElementById("txtnun").value);
    let resultado = "";

    if (numero === 0) {
        alert("Digite um numero!");
        return;
    }

    for (let x = 0; x <= 10; x++) {
        resultado += numero + " x " + x + " = " + (numero * x) +  "<br>";
    }

    document.getElementById("resultado").innerHTML = resultado; // ele pego atravez do ID a sua div, e com o innerhtml ele altera o conteudo dela
    
}   
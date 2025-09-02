function contadorDePassos() {
    let inicio = Number(document.getElementById('txtinicio').value);
    let fim = Number(document.getElementById('txtfim').value);
    let passo = Number(document.getElementById('txtpasso').value);
    let msg = document.getElementById('msg');

    if (isNaN(inicio) || isNaN(fim) || isNaN(passo)) {
        window.alert("Por favor, preencha todos os campos corretamente!");
        return;
    }

    if (passo <= 0) {
        window.alert("Passo inválido! Considerando passo 1.");
        passo = 1;
    }

    msg.innerHTML = "Contando: <br>";

    if (inicio < fim) {
        // Contagem crescente
        for (let i = inicio; i <= fim; i += passo) {
            msg.innerHTML += `${i} \u{1F449} `;
        }
    } else {
        // Contagem decrescente
        for (let i = inicio; i >= fim; i -= passo) {
            msg.innerHTML += `${i} \u{1F449} `;
        }
    }

    msg.innerHTML += "\u{1F3C1}";
}

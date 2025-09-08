function estacaoDoAno(dia, mes) {
    // validação do mês
    if (mes < 1 || mes > 12) {
        return "Por favor introduza um mês entre 1 e 12.";
    }

    // validação dos dias conforme o mês
    let diasNoMes;
    if (mes === 2) {
        diasNoMes = 28;
    } else if ([4, 6, 9, 11].includes(mes)) {
        diasNoMes = 30;
    } else {
        diasNoMes = 31;
    }

    if (dia < 1 || dia > diasNoMes) {
        if (mes === 2) {
            return "Por favor introduza um dia entre 1 e 28.";
        } else if ([4, 6, 9, 11].includes(mes)) {
            return "Por favor introduza um dia entre 1 e 30.";
        } else {
            return "Por favor introduza um dia entre 1 e 31.";
        }
    }

    // determinar a estação do ano (hemisfério norte)
    if ((mes === 12 && dia >= 21) || (mes <= 3 && (mes < 3 || (mes === 3 && dia < 20)))) {
        return "Inverno";
    } else if ((mes === 3 && dia >= 20) || mes === 4 || mes === 5 || (mes === 6 && dia < 21)) {
        return "Primavera";
    } else if ((mes === 6 && dia >= 21) || mes === 7 || mes === 8 || (mes === 9 && dia < 23)) {
        return "Verão";
    } else {
        return "Outono";
    }
}

// Exemplos de uso
console.log(estacaoDoAno(15, 2));  // Inverno
console.log(estacaoDoAno(25, 4));  // Primavera
console.log(estacaoDoAno(10, 8));  // Verão
console.log(estacaoDoAno(30, 10)); // Outono

// Exemplos de erro
console.log(estacaoDoAno(32, 1));  // Por favor introduza um dia entre 1 e 31.
console.log(estacaoDoAno(31, 4));  // Por favor introduza um dia entre 1 e 30.
console.log(estacaoDoAno(29, 2));  // Por favor introduza um dia entre 1 e 28.
console.log(estacaoDoAno(10, 13)); // Por favor introduza um mês entre 1 e 12.

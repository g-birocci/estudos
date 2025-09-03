function escadaComCardinalInvertido (degraus) {
    degrau = ""

    for (let n = 1; n <= degraus; n++) {
        degrau += "#".repeat(n) + "\n"
    } 
    return degrau
}

console.log(escadaComCardinalInvertido(5))
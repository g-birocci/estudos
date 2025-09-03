function escadaComCardinalInvertido (escada) {
    degrau = ""
    for (let i = 1; i <= escada; i++) { 
        degrau += " ".repeat(escada-i) + "#".repeat(i) + "\n"
    }
    return degrau

}

console.log(escadaComCardinalInvertido(10)) 
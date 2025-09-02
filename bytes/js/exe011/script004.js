function trimestre (x) {
    caso = x
    switch (caso) {
        case 1:
            tri = [ "janeiro" , "Fevereiro" , "março"]
            break
        case 2:
            tri = ["Abril", "Maio", "Junho"]
            break
        case 3:
            tri = ["Julho","Agosto","Setembro"]
            break
        case 4:
            tri = ["Outubro", "Novembro", "Dezembro"]
        default: {
            tri = "Opação invalida"
            break
        }
    }
    return tri
}

let op = 6

resp = trimestre(op)
console.log(resp)
function carregar() {
    let msg = window.document.getElementById("msg");
    let img = window.document.getElementById("imagen");
    let data = new Date()
    let hora = data.getHours()
    msg.innerHTML = "Agora são " + hora + "Horas"
    if (hora >= 0 && hora < 12) {
        img.src = "/aula_12/exe001/img/manha.jpg"
        document.body.style.backgroundColor = "#ACA698"
        document.body.style.borderRadius = "50%"
    } else if (hora >= 12 && hora <= 18) {
        img.src = "/aula_12/exe001/img/tarde.jpg"
        document.body.style.backgroundColor = "#7EB2EE"
    } else {
        img.src = "/aula_12/exe001/img/noite.jpg"
        document.body.style.backgroundColor = "#A34F04"

    }
}




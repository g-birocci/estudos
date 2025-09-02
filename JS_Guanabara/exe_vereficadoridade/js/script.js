function verificar() {
    let data = new Date()
    let ano = data.getFullYear()
    let fano = document.getElementById("txtano")
    let res = document.getElementById("res")

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("Verifique os dados e tente novamente.")
    } else {
        let fsex = document.getElementsByName("radisexo")
        let idade = ano - Number(fano.value)
        let img = document.createElement("img") //criando imagens dinamicas com o js, mas pode usar o html pra adionar as fotos tbm
        img.setAttribute("id", "foto")

        // Estilo via JS
        img.style.height = '250px'
        img.style.width = '250px'
        img.style.borderRadius = '50%'
        img.style.objectFit = 'cover'
        img.style.display = 'block'
        img.style.margin = 'auto'
        img.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.3)'

        let genero = ''

        if (fsex[0].checked) {
            genero = "Homem"
            if (idade >= 65) {
                img.setAttribute('src', 'img/men/idoso.jpg') //caminho das pastas das fotos
            } else if (idade >= 18) {
                img.setAttribute('src', 'img/men/adulto.jpg')
            } else if (idade >= 12) {
                img.setAttribute('src', 'img/men/adolecente.jpg')
            } else if (idade >= 5) {
                img.setAttribute('src', 'img/men/crianca.jpg')
            } else {
                img.setAttribute('src', 'img/men/bebe.jpg')
            }
        } else if (fsex[1].checked) {
            genero = "Mulher"
            if (idade >= 65) {
                img.setAttribute('src', 'img/women/idosa.jpg')
            } else if (idade >= 18) {
                img.setAttribute('src', 'img/women/adulta.jpg')
            } else if (idade >= 12) {
                img.setAttribute('src', 'img/women/adolecente.jpg')
            } else if (idade >= 5) {
                img.setAttribute('src', 'img/women/crianca.jpg')
            } else {
                img.setAttribute('src', 'img/women/bebe.jpg')
            }
        }

        // Exibe o resultado
        res.innerHTML = `<p>Detectamos ${genero} com ${idade} anos.</p>`
        res.appendChild(img) //com isso eu coloco a foto em baixo da resposta
    }
}

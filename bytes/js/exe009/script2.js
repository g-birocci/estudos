let idade = 20
const CARTA = true

if (idade >= 18 && CARTA == true) {
    console.log("Voce pode conduzir!!!")
} else if (CARTA == false || idade >=18) {
    console.log("Voce é maior de idade mas não tem carta !!!")
} else {
    console.log("Voce é menor de idade!!!")
}
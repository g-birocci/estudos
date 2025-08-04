let numeros = [2, 4, 6, 8];
let j = 0

for (let i = 0; i <= numeros.length -1; i++) { //lebrar de colocar o - 1, pra que o indice 0 seja calculado
    j = numeros[i] * 2 // dobra os valores da lista
    console.log(j)
}
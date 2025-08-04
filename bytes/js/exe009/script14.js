let numeros = [7, 12, 3, 29, 6];
let maior = 0

for (let i = 0; i <= numeros.length -1; i++) {
     if (maior < numeros[i]) {
        maior = numeros[i]
     }         
}
console.log(maior)

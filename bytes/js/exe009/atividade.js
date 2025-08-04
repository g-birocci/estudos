let num = [3, 15, 8, 22, 5]
let cont = 0

for(let x = 0; x <= num.length; x++) {
    if (num[x] >= 10) {
        console.log(num[x])
        cont++;
    }   
}

console.log("Tem um total de ", + cont + " numeros maior que 10");

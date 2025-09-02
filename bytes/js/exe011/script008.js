function maiorNum(x) {
    let maior = x[0]; //primeiro elemento
    
    for (let i = 1; i < x.length; i++) {
        if (x[i] > maior) {
            maior = x[i]; // Atualiza se achar um maior
        }
    }
    return maior;
}

let arrey = [2, 7, 4, 3, 9, 3, 6];
let res = maiorNum(arrey);
console.log(res); 

function maiorNum(x) {
    let menor = x[0]; //primeiro elemento
    let index = 0
    
    for (let i = 1; i < x.length; i++) {
        if (x[i] < menor) {
            menor = x[i]; // Atualiza se achar um maior elemento 
            index = i //
        }
    }
    return menor + " " + index;
}

let arrey = [9, 7, 4, 8, 9, 3, 6];
let res = maiorNum(arrey);
console.log(res); 

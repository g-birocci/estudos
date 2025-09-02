let num = [1,2,3,4,55,6,7,3,66]
let cont = 0

for (let i = 0; i < num.length; i++) {
    if (num[i] >= 10) {
        cont++;
    }
}
console.log(cont)
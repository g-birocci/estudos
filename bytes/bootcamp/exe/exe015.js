class Cat {
    constructor(name, weight, maxjumpHeight, verticalPosition) {
        this.name = name;
        this.weight = weight;
        this.maxjumpHeight = maxjumpHeight;
        this.verticalPosition = verticalPosition;
    }

    jump(power) {
        this.verticalPosition = this.maxjumpHeight * power;
    }
}



const gato = new Cat("Gabriel", 10, 11, 11)
const gato2 = new Cat("birocci", 34, 43, 43)  

console.log(gato.verticalPosition)
gato.jump(0.2)
console.log(gato.verticalPosition)

let listaAnimal = [] 

listaAnimal.push(gato, gato2)
console.log(gato)

console.log(listaAnimal)


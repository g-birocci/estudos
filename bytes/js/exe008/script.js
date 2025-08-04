let person = {name: "alice", age: 30, job: "teacher"}; //chave - Valor

console.log(person)
console.log(person.name)
console.log(person.age)

person.name = "gabriel"
person.city = "São Paulo"
console.log(person)

let carro = {marca: "Opel", modelo: "Corsa", ano: 2015, cor: "Azul"}

console.log(carro)

carro.cor = "Preto"

console.log(carro)

carro.km = 2344;
console.log(carro)

delete carro.km;
console.log(carro)


let animais = ["Cão","Gato","Coelho","Pássaro","Peixe"];
console.log("Arrey completo: " + animais);

animais.pop(4); //remove o item pelo index
console.log(animais);

animais.push("Hamster"); // add vlor ao fim do arrey
console.log(animais);

animais.shift(); // remove o primeiro elemento
console.log(animais);

animais.unshift("Cavalo");
console.log(animais);

animais.splice(2, 1, "tartaruga");
console.log(animais);

animais.forEach(function(animal) {
    console.log(animal)
});


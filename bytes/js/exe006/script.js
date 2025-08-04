// arrey
let frutas = ["banana", "uva", "maca"];

console.log(frutas);

frutas[2] = "abacaxi";

console.log(frutas);

console.log(frutas.length); //conta o tamanho do arrey

frutas.push("gabriel", 22); //o push add dentro do arrey
console.log(frutas); 

console.log("------------------EXE ARREY-------------------")

let cidades = ["São Paulo", "Porto", "Madri"];

console.log(cidades);

console.log(cidades[0]); //exibir o valor do arrey de acordo com o seu index
console.log(cidades[2]);

cidades[1] = "Sevilha"; //alteradno o valor do arrey indicando o seu index

console.log(cidades);

cidades.push("Barueri"); //adicionando um novo itens ao arrey
console.log(cidades);

console.log(cidades.length); //Contando os itens dentro do arrey

cidades.pop(3); //Removendo um itens do arrey de falando o seu index.
console.log(cidades);
function palavraExisteEmSopaDeLetras(sopa, nome) {
  for (let i = 0; i < sopa.length; i++) {
    let cont = 0;

    for (let j = 0; j < sopa[i].length; j++) {
      if (sopa[i][j] === nome[cont]) {
        cont++;
        if (cont === nome.length) {
          return true; 
        }
      } else {
        cont = 0;
      }
    }
  }
  return false; // não encontrou em nenhuma linha
}

let sopa = [
  ["a", "d", "c"],
  ["a", "n", "a"],
  ["m", "w", "w"]
];

let nome = "anana";

console.log(palavraExisteEmSopaDeLetras(sopa, nome)); // true

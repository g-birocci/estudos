function inverte (arr) {
    return arr.map(str => str.split("").reverse().join(""));
}

let string = ["gabriel","ester","let"]

console.log(inverte(string))
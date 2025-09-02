function fizzBuzz(x) {
    let arrey = []

    if (x <= 0) {
        return "O numero tem que ser maior que zero '0'."
    } else {
        for (let j = 1; j <= x; j++) {
            if (j % 3 === 0 && j % 5 === 0) {
                arrey.push("FizzBuzz")
            } else if (j % 3 === 0) {
                arrey.push("Fizz")
            } else if (j % 5 === 0) {
                arrey.push("Buzz")
            } else {
                arrey.push(j)
            }
        }
    }
    return arrey
}
    
let fiiz = 50
resp = fizzBuzz(fiiz)
console.log(resp)
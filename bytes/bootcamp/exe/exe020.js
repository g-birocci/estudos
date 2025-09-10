function diferecaDiagonal (matrix)  {
    let firt = 0
    let segund = 0
    

    for (let i = 0; i < matrix.length; i++) {
        firt += matrix[i][i]
        segund += matrix[i][matrix.length - 1 - i]
        }
    return Math.abs(firt - segund)
}

matrix = [
            [3,3,3],
            [4,8,9],
            [1,8,9]
        ]
console.log(diferecaDiagonal(matrix))


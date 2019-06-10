let reader = require('./reader.js')

let sortedWOrds = reader.JSONtoArray('./data/words/sortedWords.json')
console.log(sortedWOrds)
let yourSearch = "true"

let startingPoint = 0
let endPoint = theWords.length - 1
let middle = Math.floor((endPoint+startingPoint)/2)
let operations = 0

while (theWords[middle] != yourSearch.toLowerCase() && startingPoint < endPoint) {
    if (theWords[middle] < yourSearch.toLowerCase()) {
        startingPoint = middle + 1
        console.log(`Word is in the second half`)
    } else {
        endPoint = middle - 1
        console.log(`Word is the first half`)
    }
    middle = Math.floor((endPoint+startingPoint)/2)
    console.log("updated middle: ", middle)
    operations ++
}
console.log(`\n`)
console.log(`Word is at index ${middle}`)
console.log('startingPoint:', startingPoint)
console.log('endPoint:', endPoint)
console.log("Number of operations: ", operations)

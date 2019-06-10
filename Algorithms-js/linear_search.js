let reader = require('./reader.js')

let theWords = reader.sortedWords()
console.log(theWords)

let yourDictSearch = "turmoil"

for (word of theWords) {
    if (word == yourDictSearch.toLowerCase()){
        console.log("Success")
    }
}
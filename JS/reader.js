/* Data sources: https://github.com/dwyl/english-words, https://github.com/adambom/dictionary */
const fs = require('fs');

function JSONtoArray(JSONFilePath){
let jsonFile = fs.readFileSync(JSONFilePath);  
let parsedJSONFile = JSON.parse(jsonFile);  
let array = []
for (word in parsedJSONFile) {
    array.push(word)
}
return array
}

function JSONtoArrayAsync(){
    fs.readFile('./data/dictionary/dictionary.json', (err, data) => {  
        if (err) throw err;
        let parsedJSONFile = JSON.parse(data);
        let array = []
        for (word in parsedJSONFile) {
            array.push(word)
        }
        return array
    });
}



function jsonIterator(JSONFile, attributename){
    for(var attributename in JSONFile){
        console.log(attributename+": "+JSONFile[attributename]);
    }
}

jsonIterator('./data/dictionary/dictionary.json', 'Hello');


module.exports = {
    JSONtoArrayAsync: JSONtoArrayAsync,
    JSONtoArray: JSONtoArray,
}

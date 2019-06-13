function mergeSort(anArray) {
    if (anArray.length > 1) {
        var mid = Math.floor(anArray.length/2)
        var leftHalf = anArray.slice(0, mid)
        var rightHalf = anArray.slice(mid, anArray.length)
        // console.log(JSON.stringify(leftHalf))
        // console.log(JSON.stringify(rightHalf))
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        var i = 0
        var j = 0
        var k = 0

        while (i < leftHalf.length && j < rightHalf.length) {
            if(leftHalf[i]<rightHalf[j]){
                anArray[k]=leftHalf[i]
                i++
            } else {
                anArray[k] = rightHalf[j]
                j++
            }
            k++
        }

        while (i < leftHalf.length) {
            anArray[k]= leftHalf[i]
            i++
            k++
        }

        while (j < rightHalf.length) {
            anArray[k]= rightHalf[j]
            j++
            k++
        }
    }
    // console.log(JSON.stringify(anArray))
}

const array = [54,26,93,17,77,31,44,55,20]

for (var i = 1; i<100000; i++) {
    var aNumber = Math.floor(Math.random()*1000)
    array.push(aNumber)
}

var start = console.time('test')
// var start = new Date().getTime();
mergeSort(array)
// var end = new Date().getTime();
var end = console.timeEnd('test')

// console.log(start-end)

// console.log("Call to doSomething took " + (end - start) + "units(ms?)")
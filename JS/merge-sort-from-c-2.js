
function mergeSort(array, length) {
    var a = array
    var b = []
    var low =0
    var newLength = Math.floor(length / 2)
    if (newLength>0) {
        console.log('length:', length)
        console.log('newLength:', newLength)
        mergeSort(low, newLength)
        mergeSort(newLength + 1, length)

        var low2, newLength2, i

        for (low2 = low, newLength2 = newLength + 1, i = low; low2 <= newLength && newLength2 <= length; i++) {
            if (a[low2] <= a[newLength2])
                b[i] = a[low2++]
            else
                b[i] = a[newLength2++]
        }

        while (low2 <= newLength)
            b[i++] = a[low2++]

        while (newLength2 <= length)
            b[i++] = a[newLength2++]

        for (i = low; i <= length; i++)
            a[i] = b[i]
    } 
    return b
}

const array = [54,26,93,17,77,31,44,55,20]

// for (var i = 1; i<100000; i++) {
//     var aNumber = Math.floor(Math.random()*1000)
//     array.push(aNumber)
// }

theLength = array.length

var start = console.time('test')
console.log(mergeSort(array, theLength))
var end = console.timeEnd('test')

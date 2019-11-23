
function mergeSort(array) {
    var a = array
    var b = []
    var length = array.length
    var low = 0
    if (low < length) {
        var mid = (low + length) / 2
        mergeSort(low, mid)
        mergeSort(mid + 1, length)

        var low2, mid2, i

        for (low2 = low, mid2 = mid + 1, i = low; low2 <= mid && mid2 <= length; i++) {
            if (a[low2] <= a[mid2])
                b[i] = a[low2++]
            else
                b[i] = a[mid2++]
        }

        while (low2 <= mid)
            b[i++] = a[low2++]

        while (mid2 <= length)
            b[i++] = a[mid2++]

        for (i = low; i <= length; i++)
            a[i] = b[i]
    } else {
        return console.log('b:', JSON.stringify(b))
    }
}

const array = [54,26,93,17,77,31,44,55,20]

// for (var i = 1; i<100000; i++) {
//     var aNumber = Math.floor(Math.random()*1000)
//     array.push(aNumber)
// }

var start = console.time('test')
mergeSort(array)
var end = console.timeEnd('test')

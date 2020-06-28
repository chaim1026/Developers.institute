let arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8]

function bubbleSort(arr) {
    let len = arr.length
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (inputArr[j] > inputArr[j + 1]) {
                let tmp = inputArr[j]
                inputArr[j] = inputArr[j + 1]
                inputArr[j + 1] = tmp
            }
        }
    }
    return arr
    console.log(arr)
};
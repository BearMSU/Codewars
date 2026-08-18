function mergeArrays(arr1, arr2) {
    let arr3 = [...arr1, ...arr2].sort((a, b) => a -b);
    let arr4 = arr3.filter((item, index) => arr3.indexOf(item) === index);  
    return arr4;
}
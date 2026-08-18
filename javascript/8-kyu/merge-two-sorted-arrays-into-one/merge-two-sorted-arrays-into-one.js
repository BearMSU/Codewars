function mergeArrays(arr1, arr2) {
    const arr3 = [...arr1, ...arr2].sort((a, b) => a - b);
    const unique = [...new Set(arr3)];
    return unique;
}
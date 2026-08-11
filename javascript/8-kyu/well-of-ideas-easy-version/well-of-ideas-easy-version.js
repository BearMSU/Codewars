function well(x){
    const goodCount = x.filter(n => n === 'good').length;
    if (goodCount === 1 || goodCount === 2) {
        return 'Publish!';
    } else if (goodCount > 2) {
        return 'I smell a series!'
    } else {
        return 'Fail!'
    }
}
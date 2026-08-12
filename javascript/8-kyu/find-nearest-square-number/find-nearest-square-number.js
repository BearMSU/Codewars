function nearestSq(n){
    // your code
    const x = Math.floor(Math.sqrt(n)) ** 2;
    const y = Math.ceil(Math.sqrt(n)) ** 2;
  
    if (n === 1 || n === 2) {
      return 1;
    } else if (n === 3) {
      return 2;
    } else if ((n - x) > (y - n)) {
      return y;
    } else {
      return x;
    }
}
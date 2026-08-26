function descendingOrder(n){
  //...
    const numArray = Array.from(String(n), Number);
    numArray.sort((a, b) => b - a);
    return Number(numArray.join(''));
}
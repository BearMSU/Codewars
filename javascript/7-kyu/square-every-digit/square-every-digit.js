function squareDigits(num){
  let numArr = Array.from(String(num), Number);
  let squaredArr = []
  for (let i = 0; i < numArr.length; i++) {
    squaredArr.push(numArr[i] ** 2);
  }
  return Number(squaredArr.join(""));
}
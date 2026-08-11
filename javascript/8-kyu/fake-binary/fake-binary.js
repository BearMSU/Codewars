function fakeBin(x){
  xArr = Array.from(x);
  fakeBinary = [];
  for (let i = 0; i < xArr.length; i++) {
    if (x[i] < 5) {
      fakeBinary.push('0')
    } else {
      fakeBinary.push('1')
    }
  }
  fakeString = fakeBinary.join("");
  return fakeString;
}
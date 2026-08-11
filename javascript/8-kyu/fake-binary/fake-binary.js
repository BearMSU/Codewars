function fakeBin(x){
  fakeString = "";
  for (let i = 0; i < x.length; i++) {
    if (x[i] < 5) {
      fakeString += '0';
    } else {
      fakeString += 1;
    }
  }
  return fakeString;
}
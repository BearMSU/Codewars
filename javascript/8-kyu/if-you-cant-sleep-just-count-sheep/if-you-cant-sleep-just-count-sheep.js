var countSheep = function (num){
  //your code here
  let sheepString = "";
  for (let i = 1; i <= num; i++) {
    sheepString += `${i} sheep...`.replace("\n", "");
  }
  return sheepString;
}
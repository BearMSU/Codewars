var countSheep = function (num){
  //your code here
  let string = "";
  for (let i = 1; i <= num; i++){
      string += `${i} sheep...`.replaceAll("\n", "");
  }
  return string;
}
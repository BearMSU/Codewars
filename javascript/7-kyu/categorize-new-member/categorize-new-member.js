function openOrSenior(data){
  let membership = [];
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] >= 55 && data[i][1] > 7) {
      membership.push('Senior');
    } else {
      membership.push('Open');
    }
  }
  return membership;
}
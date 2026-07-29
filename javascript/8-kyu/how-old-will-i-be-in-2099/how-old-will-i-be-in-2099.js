function  calculateAge(bYear, eYear) {  
  // enter your code here.
  let age = Math.abs(eYear - bYear);
  if (bYear < eYear && age === 1) {
    return `You are ${age} year old.`
  } else if (bYear > eYear && age === 1) {
    return `You will be born in ${age} year.`
  } else if (bYear < eYear) {
    return `You are ${age} years old.`
  } else if (bYear > eYear) {
    return `You will be born in ${age} years.`
  } else {
    return `You were born this very year!`
  }
}
​
​
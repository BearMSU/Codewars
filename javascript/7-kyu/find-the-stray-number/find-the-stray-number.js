function stray(numbers) {
  if (numbers[0] !== numbers[1] && numbers[0] !== numbers[2]) {
    return numbers[0];
  } else {
    const outlier = numbers.filter(item => item !== numbers[0]);
    return outlier[0];
  }
}
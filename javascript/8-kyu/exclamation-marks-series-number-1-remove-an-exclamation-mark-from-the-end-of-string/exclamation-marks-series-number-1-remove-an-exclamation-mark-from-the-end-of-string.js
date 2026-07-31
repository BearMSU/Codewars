function remove (string) {
  //coding and coding....
  lastChar = string.charAt(string.length - 1);
  lastIndex = string.length - 1;
  return lastChar === '!' ? string.slice(0, lastIndex) : string;
}
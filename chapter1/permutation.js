function permutation(str1, str2) {
  newStr1 = str1.split("").sort().join("");
  newStr2 = str1.split("").sort().join("");

  if (newStr1 == newStr2) {
    return true;
  }

  return false;
}

console.log(permutation("dog", "god"));

module.exports = permutation;

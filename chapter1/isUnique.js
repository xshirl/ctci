function isUnique(str) {
  let dic = {};

  for (let char of str) {
    if (char in dic) {
      return false;
    }
    dic[char] = true;
  }
  return true;
}

console.log(isUnique("abccd"));

module.exports = isUnique;

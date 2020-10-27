function romanToInt(s) {
  let roman = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

  let num = 0;

  for (let i = 0; i < s.length; i++) {
    let curr_num = roman[s[i]];
    let next_num;
    if (i < s.length - 1) {
      next_num = roman[s[i + 1]];
    } else {
      next_num = 0;
    }
    if (next_num > curr_num) {
      num -= curr_num;
    } else {
      num += curr_num;
    }
  }
  return num;
}

console.log(romanToInt("IV"));
console.log(romanToInt("XIII"));

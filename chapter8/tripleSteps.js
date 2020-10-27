var numWays = function (N) {
  let answer = 0;
  var recurse = function (number) {
    if (number === 0) {
      answer++;
    } else if (number > 0) {
      recurse(number - 1);
      recurse(number - 2);
      recurse(number - 3);
    }
  };
  recurse(N);
  return answer;
};

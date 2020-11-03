// 2, 3
// 2 + 2, 2
// 2 + 2 + 2, 1
// 2 + 2 + 2

// 3, 3
// 3 + 3, 2
// 3 + 3 +  3, 1
// 3 + 3 + 3

function recursiveMultiply(a, b) {
  if (a < 0 || b < 0) {
    throw "error, should be positive";
  }
  if (b === 0) {
    return 0;
  } else if (b === 1) {
    return a;
  } else {
    return recursiveMultiply(a, b - 1);
  }
}

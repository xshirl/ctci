function reverseInt(x) {
  let res = 0;
  let num = Math.abs(x);

  while (num > 0) {
    res = res * 10 + (num % 10);
    num = parseInt(num / 10);
    console.log(num);
  }
  if (res > Math.pow(2, 31) || res < -Math.pow(2, 31)) {
    return 0;
  }
  if (x < 0) {
    return -res;
  }
  return res;
}

console.log(reverseInt(123));

function palinInt(x) {
  let res = 0;
  if (x < 0) {
    return false;
  }
  let num = Math.abs(x);
  while (num > 0) {
    res = res * 10 + (num % 10);
    num = parseInt(num / 10);
  }

  if (res == x) {
    return true;
  }
}

console.log(palinInt(1331));

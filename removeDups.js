function removeDups(arr) {
  let i = 0;
  let j = 1;
  while (j < arr.length) {
    if (arr[i] != arr[j]) {
      i++;
      j++;
    } else {
      arr.splice(j, 1);
    }
  }
  return arr.length;
}

console.log(removeDups([1, 1, 1, 2, 2]));

function removeEl(arr, el) {
  let i = 0;
  while (i < arr.length) {
    if (arr[i] != el) {
      i++;
    } else {
      arr.splice(i, 1);
    }
  }
  return arr;
}

console.log(removeEl([1, 2, 3, 4, 5], 3));

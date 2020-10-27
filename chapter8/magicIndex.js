var findMagic = function (arr, start, end) {
  if (start == undefined) {
    start = 0;
  }
  if (end == undefined) {
    end = arr.length - 1;
  }
  let mid = Math.floor(start + (end - start) / 2);

  if (mid == start && arr[mid] !== mid) {
    return -1;
  } else if (arr[mid] == mid) {
    return mid;
  } else if (mid < arr[mid]) {
    return findMagic(arr, start, mid);
  } else {
    return findMagic(arr, mid, end);
  }
};

console.log(findMagic([-1, 0, 1, 3, 9, 100]), 3);

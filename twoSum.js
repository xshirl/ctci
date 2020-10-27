function twoSum(arr, target) {
  let hashmap = {};
  for (let i = 0; i < arr.length; i++) {
    let diff = target - arr[i];
    if (diff in hashmap) {
      return [i, hashmap[diff]];
    }
    hashmap[arr[i]] = i;
  }
}

console.log(twoSum([2, 7, 11, 15], 9));

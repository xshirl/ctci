// You are given a list of unsorted integers with values
//   from 0 to 9 inclusive. The list can be very long
//   (millions of items). Fill out the `sort` function
//   below and sort the list.

function sort(unsorted) {
  let hashmap = {};
  for (let num of unsorted) {
    if (hashmap.hasOwnProperty(num)) {
      hashmap[num]++;
    } else {
      hashmap[num] = 1;
    }
  }

  console.log(hashmap);
  let res = [];
  for (let i = 0; i <= 9; i++) {
    for (let j = 0; j < hashmap[i]; j++) {
      res.push(i);
    }
  }
  return res;
}

const iterations = 1;
const input = [];
for (let i = 0; i < iterations; i++) {
  input.push(Math.floor(Math.random() * Math.floor(10)));
}

console.log(input);
console.log(sort(input));

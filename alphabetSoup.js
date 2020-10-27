function alphabet(phrase, bank) {
  let hashmap = {};
  for (let char of bank) {
    if (hashmap.hasOwnProperty(char)) {
      hashmap[char]++;
    } else {
      hashmap[char] = 1;
    }
  }
  let newPhrase = [];
  for (let char of phrase) {
    if (newPhrase.indexOf(char) == -1) {
      newPhrase.push(char);
    }
  }
  let count = 0;
  for (let char of newPhrase) {
    if (hashmap[char] > 0) {
      count++;
    }
  }
  if (count == newPhrase.length) {
    return true;
  }
  return false;
}

const reject = function (arr, func) {
  return arr.filter((word) => !func(word));
};

const testWord = (word) => {
  return word.length > 3;
};

const list = reject(["one", "four", "tw", "six"], testWord);

console.log(list);

function filterEvensDoubleAndSum(arr) {
  return arr
    .filter((num) => num % 2 == 0)
    .map((num) => num * 2)
    .reduce((acc, num) => acc + num, 0);
}

Array.prototype.map2 = function (callback) {
  let arr = [];
  for (let index = 0; i < this.length; i++) {
    arr.push(callback[this[index]]);
  }
  return arr;
};

function forEach(arr, callback) {
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]);
  }
}
function doubler(element) {
  return element * 2;
}
function map(arr, callback) {
  const newArr = [];
  for (let item of arr) {
    newArr.push(callback(item));
  }
  return newArr;
}
function filter(arr, callback) {
  const res = [];
  for (let item of arr) {
    if (callback(item)) {
      res.push(item);
    }
  }
  return res;
}

function includes(collection, elem) {
  for (let key in collection) {
    if (collection.hasOwnProperty(key)) {
      if (collection[key] == elem) {
        return true;
      }
    }
  }
  return false;
}

function countWords(num, string) {
  let arr = string.split(" ");
  return (num += arr.length);
}

function reduce(arr, start, callback) {
  let val = start;
  arr.forEach((item) => {
    val = callback(val, item);
  });
  return val;
}

function sum(arr) {
  let add = (a, b) => a + b;
  return reduce(arr, 0, add);
}

function every(arr, callback) {
  let count = 0;
  arr.forEach((item) => {
    if (callback(item)) {
      count++;
    }
  });
  if (count == arr.length) {
    return true;
  }

  return false;
}

function some(arr, callback) {
  let count = 0;
  arr.forEach((item) => {
    if (callback(item)) {
      count++;
    }
  });
  if (count >= 1) {
    return true;
  }

  return false;
}

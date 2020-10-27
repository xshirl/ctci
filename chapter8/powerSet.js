var powerSet = function (nums) {
  let res = [];
  dfs([], 0);

  function dfs(current, idx) {
    res.push(current);
    for (let i = idx; i < nums.length; i++) {
      dfs(current.concat(nums[i]), i + 1);
    }
  }

  return res;
};

console.log(powerSet([1, 2, 3, 4, 5]));

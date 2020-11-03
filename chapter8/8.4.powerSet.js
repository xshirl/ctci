const returnSubsets = function (set) {
  const subsets = [];
  const recurse = function (currSet, remainingSet) {
    subsets.push(currSet);
    console.log(subsets);
    for (let i = 0; i < remainingSet.length; i++) {
      recurse(currSet.concat([remainingSet[i]]), remainingSet.slice(i + 1));
    }
  };
  recurse([], set);
  return subsets;
};

console.log(returnSubsets([1, 2, 3, 4]));

function subsets(nums) {
  let res = [];
  dfs([], 0);
  function dfs(current, idx) {
    res.push(current);
    for (let i = idx; i < nums.length; i++) {
      dfs(current.concat(nums[i]), i + 1);
    }
  }
  return res;
}

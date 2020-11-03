const findPaths = function (grid) {
  const paths = [];
  let endRow = grid.length - 1;
  let endCol = grid[0].length - 1;
  let recurse = function (row, col, currPath) {
    if (row === endRow && col === endCol) {
      paths.push(currPath.concat([[row, col]]));
    } else if (row <= endRow && col <= endCol) {
      recurse(row + 1, col, currPath.concat([[row, col]]));
    }
    if (col < endCol && grid[row][col + 1] !== "x") {
      recurse(row, col + 1, currPath.concat([[row, col]]));
    }
  };
  recurse(0, 0, []);
  return paths;
};

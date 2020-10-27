function buySellStock(arr) {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (let price of arr) {
    if (price < minPrice) {
      minPrice = price;
    } else if (maxProfit < price - minPrice) {
      maxProfit = price - minPrice;
    }
  }
  return maxProfit;
}

class Main {
  public static void main(String[] args) {

    System.out.println(maxProfit(new int[] { 3, 1, 9, 4, 20 }));
    System.out.println(maxProfit1(new int[] { 3, 1, 9, 4, 20 }));
  }

  public static int maxProfit(int[] prices) {
    if (prices == null || prices.length == 0) {
        return 0;
    }

    int n = prices.length;
    int maxProfit = 0;
    int maxPriceSoFar = prices[n - 1];  // Start from the last day's price

    for (int i = n - 2; i >= 0; i--) {  // Start iterating from the second last day
        if (prices[i] < maxPriceSoFar) {  // If current price is less than max, sell at max price
            maxProfit += maxPriceSoFar - prices[i];
            maxPriceSoFar = prices[i];  // update the maxPrice with the current price
        } else {  // If current price is more than the max price seen so far, update max price
            maxPriceSoFar = prices[i];
        }
    }

    return maxProfit;
}
public static int maxProfit1(int[] prices) {
  if (prices == null || prices.length == 0) {
      return 0;
  }

  int n = prices.length;
  int maxProfit = 0;

  for (int i = 1; i < n; i++) {
      if (prices[i] > prices[i - 1]) {
          maxProfit += prices[i] - prices[i - 1];
      }
  }

  return maxProfit;
}
}
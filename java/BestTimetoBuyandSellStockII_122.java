public class BestTimetoBuyandSellStockII_122 {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)
            return 0;
        else {
            int max_value = 0;
            for(int i=0;i<prices.length-1;i++){
                if(prices[i+1]>prices[i]){
                    max_value=max_value+prices[i+1]-prices[i];
                }
            }
            return max_value;
        }

    }

    public static void main(String[] args){
        int[] prices = {1,2,3,4,5};
        BestTimetoBuyandSellStockII_122 bt2 = new BestTimetoBuyandSellStockII_122();
        int result = bt2.maxProfit(prices);
        System.out.println(result);
    }
}

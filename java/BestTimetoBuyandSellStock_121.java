public class BestTimetoBuyandSellStock_121 {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)
            return 0;
        else{
            int max_value = Integer.MIN_VALUE;
            for(int i=0;i<prices.length-1;i++){
                for(int j=i;j<prices.length;j++){
                    if(prices[j]-prices[i]>max_value){
                        max_value = prices[j]-prices[i];
                    }
                }
            }
            return max_value;
        }


    }

    public static void main(String[] args){
        BestTimetoBuyandSellStock_121 bt = new BestTimetoBuyandSellStock_121();
        int[] prices = {7,1,5,3,6,4};
        int result = bt.maxProfit(prices);
        System.out.println(result);

    }
}

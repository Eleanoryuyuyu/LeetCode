public class Count_Primes_204 {
    public int countPrimes(int n) {
        int count=0;
        for(int i=2;i<n;i++){
            if(isPrime(i))
                count++;
        }
        return count;
    }
    private boolean isPrime(int n){
        for(int i=2;i*i<=n;i++){
            if(n%i==0)
                return false;
        }
        return true;
    }

    public static void main(String[] args){
        Count_Primes_204 cp = new Count_Primes_204();
        System.out.println(cp.countPrimes(10));
    }
}

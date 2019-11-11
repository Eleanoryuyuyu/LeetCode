public class Sqrt {
    public int mySqrt(int x) {
        return (int)Math.sqrt(x);
    }

    public static void main(String[] args){
        Sqrt sqrt = new Sqrt();
        int a=16;
        System.out.println(sqrt.mySqrt(a));
    }
}

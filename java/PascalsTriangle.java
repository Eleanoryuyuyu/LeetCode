import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {
    public List<List<Integer>> generate(int rows){
        List<List<Integer>> list = new ArrayList<>();
        for(int i=0;i<rows;i++){
            List<Integer> sublist = new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0||j==i)
                    sublist.add(1);
                else {
                    sublist.add(list.get(i-1).get(j-1)+list.get(i-1).get(j));
                }
            }
            list.add(sublist);
        }
        return list;
    }

    public static void main(String[] args){
        PascalsTriangle pt = new PascalsTriangle();
        List<List<Integer>> list = pt.generate(5);
        for(int i=0;i<5;i++){
            System.out.print(list.get(i));
        }
    }
}

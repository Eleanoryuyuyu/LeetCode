package tree;

public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null || q==null){
            if(p==q)
                return true;
            else
                return false;
        }
        else return p.val==q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }

    public static void main(String[] args){
        /** 测试数据*/
        TreeNode p =new TreeNode(1);
        TreeNode q =new TreeNode(1) ;
        p.left = new TreeNode(2);
        p.right = null;
        q.left = null;
        q.right = new TreeNode(2);
        SameTree st = new SameTree();
        System.out.println(st.isSameTree(p,q));

    }
}

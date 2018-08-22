package tree;

public class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        return isSymmetrichelper(root,root);
    }

    public boolean isSymmetrichelper(TreeNode left,TreeNode right){
        if(left==null && right==null)
            return true;
        if(left==null || right == null)
            return  false;
        return left.val==right.val
                && isSymmetrichelper(left.left,right.right)
                && isSymmetrichelper(left.right,right.left);
    }

    public static void main(String[] args){
        /** 测试数据*/
        TreeNode root =new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(2);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(4);
        root.left.left=new TreeNode(3);
        root.right.right = new TreeNode(3);
        SymmetricTree symmetricTree = new SymmetricTree();
        System.out.println(symmetricTree.isSymmetric(root));



    }
}

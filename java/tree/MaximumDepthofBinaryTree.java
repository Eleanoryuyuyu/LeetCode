package tree;

public class MaximumDepthofBinaryTree {
    public int maxDepth(TreeNode root) {
       if(root==null)
           return 0;
       else
           return 1+Math.max(maxDepth(root.left),maxDepth(root.right));

    }

    public static void main(String[] args){
        MaximumDepthofBinaryTree mdbt = new MaximumDepthofBinaryTree();
        TreeNode root =new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(2);
        root.left.right = new TreeNode(5);
        int n = mdbt.maxDepth(root);
        System.out.println(n);

    }
}

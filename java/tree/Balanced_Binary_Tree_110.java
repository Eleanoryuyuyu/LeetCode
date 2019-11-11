package tree;

public class Balanced_Binary_Tree_110 {
    public boolean isBalanced(TreeNode root) {
        if(root==null)
            return true;
        int depth = getDepth(root);
        return depth>=0;
    }
    private int getDepth(TreeNode t){
        if(t==null)
            return 0;
        int left = getDepth(t.left);
        int right = getDepth(t.right);
        if(left==-1 || right==-1 || Math.abs(left-right)>1)
            return -1;
        return 1+Math.max(left,right);

    }

    public static void main(String[] args){
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(2);
        TreeNode node4 = new TreeNode(3);
        TreeNode node5 = new TreeNode(3);
        TreeNode node6 = new TreeNode(4);
        TreeNode node7 = new TreeNode(4);

        node1.left=node2;
        node1.right=node3;
        node2.left=node4;
        node2.right=node5;
        node4.left = node6;
        node4.right = node7;

        Balanced_Binary_Tree_110 bbt = new Balanced_Binary_Tree_110();
        System.out.println(bbt.isBalanced(node1));
    }
}

package tree;

public class MinimumDepthofBinaryTree_111 {
    public int minDepth(TreeNode root) {
        if(root==null)
            return 0;
        else if(root.left==null && root.right==null)
            return 1;
        else if(root.left!=null && root.right==null)
            return minDepth(root.left)+1;
        else if(root.left==null && root.right!=null)
            return minDepth(root.right)+1;
        else
            return Math.min(minDepth(root.left),minDepth(root.right))+1;
    }

    public int maxDepth(TreeNode root){
        if(root==null)
            return 0;
        int ldepth = maxDepth(root.left);
        int rdepth = maxDepth(root.right);
        return Math.max(ldepth,rdepth)+1;
    }

    public static void main(String[] args){
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);

        node1.left=node2;
        node1.right=node3;
        node3.left=node4;
        node3.right=node5;

        MinimumDepthofBinaryTree_111 mdp = new MinimumDepthofBinaryTree_111();
        int min = mdp.minDepth(node1);
        int max = mdp.maxDepth(node1);
        System.out.println(min);
        System.out.println(max);

    }
}

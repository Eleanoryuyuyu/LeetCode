package tree;

import java.util.*;

public class BinaryTreeInorderTraversal_94 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderTraversalHelper(result,root);
        return result;
    }
    private void inorderTraversalHelper(List<Integer> list,TreeNode root){
        if(root!=null){
            inorderTraversalHelper(list,root.left);
            list.add(root.val);
            inorderTraversalHelper(list,root.right);
        }
    }
    public List<Integer> inorderTraversal2(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        while (root!=null ||!stack.isEmpty()){
            if(root!=null){
                stack.push(root);
                root = root.left;
            }else {
                TreeNode pop = stack.pop();
                result.add(pop.val);
                root=pop.right;
            }
        }return result;
    }

    public static void main(String[] args){
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);

        node1.right = node2;
        node2.left = node3;

        BinaryTreeInorderTraversal_94 btin = new BinaryTreeInorderTraversal_94();
        List<Integer> result,result2;
        result = btin.inorderTraversal(node1);
        result2 = btin.inorderTraversal2(node1);
        System.out.println(result2);
    }
}

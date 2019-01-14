import java.util.Queue;
import java.util.LinkedList;

class TreeLinkNode {
      int val;
      TreeLinkNode left, right, next;
      TreeLinkNode(int x) { val = x; }
}
class Solution {
    public void connect(TreeLinkNode root) {
        //breadth first search
        Queue<TreeLinkNode> thisQueue = new LinkedList<TreeLinkNode>();
	thisQueue.add(root);
        Queue<TreeLinkNode> nextQueue;
	while (thisQueue.peek() != null) {
		nextQueue = new LinkedList<TreeLinkNode>();
		while (thisQueue.peek() != null) {
			TreeLinkNode temp = thisQueue.remove();
			System.out.println();
			System.out.print("Val: " + temp.val);
			if (temp.left != null) {
				System.out.print(" Left Node: " + temp.left.val);
				nextQueue.add(temp.left);
			}
			if (temp.right != null) {
				System.out.print(" Right Node: " + temp.right.val);
				nextQueue.add(temp.right);
			}
			temp.next = thisQueue.peek();
			
			if (temp.next != null)  
			System.out.print(" Next Node: " + temp.next.val);
		}
		thisQueue = nextQueue;
	}
    }
}
public class populatingRightPointers {
    public static void main(String[] args) {
    	Solution sol = new Solution();
	TreeLinkNode root = new TreeLinkNode(5);
	root.left = new TreeLinkNode(1);
	root.left.left = new TreeLinkNode(1);
	root.left.right = new TreeLinkNode(2);
	root.right = new TreeLinkNode(2);
	root.right.left = new TreeLinkNode(3);
	root.right.right = new TreeLinkNode(4);
	sol.connect(root);
	sol.connect(null);

    }
}

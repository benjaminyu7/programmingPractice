/*class Node<T> {
	T value;
	Node(T new_value) {
		this.value = new_value;
	}
}*/
class BinaryNode<T> extends Node<T> {
	BinaryNode left;
	BinaryNode right;
	BinaryNode(T new_value) {
		super(new_value);
	}
}
	
public class binaryTree {
	public void printInorder(BinaryNode root) {
		if(root==null){
		return;
		}
		printInorder(root.left);
		System.out.println(root.value);
		printInorder(root.right);
	}
	public static void main(String [] args) {
		binaryTree bt = new binaryTree();
		BinaryNode<Integer> root = new BinaryNode<>(2);
		root.left= new BinaryNode<Integer> (1);
		root.right=new BinaryNode<Integer> (3);
		bt.printInorder(root);
	}
}

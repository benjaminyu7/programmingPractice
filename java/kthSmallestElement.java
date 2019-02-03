import java.util.Arrays; 

class Solution {
	public int kthSmallest(int[][] matrix, int k) {
		int[] newArr = new int[matrix.length*matrix.length];
		int index = 0;
		for (int[] arr: matrix) {
			for (int element: arr) {
				newArr[index]=element;
				index++;
			}
		}
		Arrays.sort(newArr);
		return newArr[k-1];
	}
}

class kthSmallestElement {
	public static void main (String [] args) {
		Solution sol = new Solution();
		System.out.println(sol.kthSmallest(
				new int[][]{
					{1,4,9},
					{10,11,13},
					{12,13,15}
				},
				8	
			)
		);
	}
}

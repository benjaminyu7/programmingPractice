using DataStructures;

namespace Algorithms
{
    public class BinaryTreeSerialize
    {

        static int DEFAULT_NULL = 1002;
        public static string Serialize(TreeNode head)
        {
            int arrSize = MaxTreeArrayIndex(head, 0);
            Console.WriteLine(arrSize);
            int[] ints = new int[arrSize+1];
            Array.Fill<int>(ints, DEFAULT_NULL);

            SerializeHelper(head, ints, 0);
            return String.Join(",", ints);
        }
        
        public static TreeNode Deserialize(String str)
        {
            Console.WriteLine(str);
            int[] ints = str.Split(',').Select(int.Parse).ToArray();
            return DeserializeHelper(ints, 0);

        }

        private static TreeNode? DeserializeHelper(int[] ints, int index)
        {
            if(ints[index] == DEFAULT_NULL)
            {
                return null;
            }
            TreeNode? left = null;
            TreeNode? right = null;
            int leftIndex=index*2+1;
            if(leftIndex<ints.Length)
            {
                left = DeserializeHelper(ints, leftIndex);
            }
            int rightIndex=index*2+2;
            if(rightIndex<ints.Length)
            {
                right = DeserializeHelper(ints, rightIndex);
            }
            return new TreeNode(ints[index], left, right);
        }

        private static void SerializeHelper(TreeNode head, int[] ints, int index)
        {
            ints[index] = head.val;
            if (head.left != null)
            {
                SerializeHelper(head.left, ints, index * 2 +1);
            }
            if (head.right != null)
            {
                SerializeHelper(head.right, ints, index*2+2);
            }
        }

        // Find the size of an array needed for this binary tree
        private static int MaxTreeArrayIndex(TreeNode head, int index)
        {
            int right = 0;
            int left = 0;
            if (head.right != null)
            {
                right = MaxTreeArrayIndex(head.right,2*index+2);
            }
            if (head.left != null)
            {
                left = MaxTreeArrayIndex(head.left,2*index+1);
            }
            return int.Max(index, int.Max(right, left));
        }
    }
}
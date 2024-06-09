/* Write code to Remove duplicate from an unsorted linked list
   Would this be a doubly linked list?
   What values do we expect to see in the list?
*/
namespace Algorithms
{
    using DataStructures;
    public class RemoveDuplicates 
    {
        public RemoveDuplicates  () {}

        public Node<int>? RemoveDuplicateSet (Node<int> head) 
        {
            HashSet<int> duplicates = new HashSet<int>();
            Node<int>? pointer = head;
            while(pointer != null)
            {
                duplicates.Add(pointer.value);
                pointer = pointer.next;
            }

            Node<int>? newHead = null;
            Node<int>? newPointer = null;
            foreach(int item in duplicates)
            {
                if(newPointer != null)
                {
                    newPointer.next = new Node<int>{
                        value = item
                    };
                    newPointer = newPointer.next;
                }
                else
                {
                    newHead = new Node<int>{value=item};
                    newPointer = newHead;
                }
            }
            return newHead;
        }

        public Node<int> RemoveDuplicatesNoMem(Node<int> numbers)
        {
            numbers = LinkedListHelper.mergeSort(numbers);
            Node<int> pointer = numbers;
            while(pointer.next != null)
            {
                if(pointer.value == pointer.next.value)
                {
                    pointer.next = pointer.next.next;
                }
                else
                {
                    pointer = pointer.next;
                }
            }
            return numbers;
        }
    }
}
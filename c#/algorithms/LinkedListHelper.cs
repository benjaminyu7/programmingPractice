using System.Text;
using DataStructures;

namespace Algorithms
{
    public class LinkedListHelper
    {
        public static Node<int> mergeSort(Node<int> head)
        {
            if(head.next == null)
            {
                return head;
            }

            //Find mid node
            Node<int>? fastPointer = head;
            Node<int> midPointer = new Node<int>{next = head};
            while(fastPointer != null)
            {
                fastPointer = fastPointer?.next?.next;
                midPointer = midPointer.next;
            }
            Node<int> secondList = midPointer.next;
            midPointer.next = null;
            
            return LinkedListHelper.Merge(mergeSort(head), mergeSort(secondList));
        }

        private static Node<int> Merge (Node<int> listOne, Node<int> listTwo)
        {
            Node<int> pointer = null;
            if(listTwo.value < listOne.value)
            {
                pointer = listOne;
                listOne = listTwo;
                listTwo = pointer;
            }
            Node<int> head = listOne;
            while(listOne.next != null && listTwo != null)
            {
                if(listOne.next.value < listTwo.value) 
                {
                    listOne = listOne.next;
                }
                else
                {
                    pointer = listOne.next;
                    listOne.next = listTwo;
                    listTwo = listTwo.next;
                    listOne = listOne.next;
                    listOne.next = pointer;
                }
            }

            if (listOne.next == null) 
            {
                listOne.next = listTwo;
            }

            return head;
        }
    
        public static void printLinkedList(Node<int> head)
        {
            StringBuilder builder = new StringBuilder();
            builder.Append(head.value);
            Node<int>? pointer = head.next;
            while (pointer != null)
            {
                builder.Append(',');
                builder.Append(pointer.value);
                pointer=pointer.next;
            }
            Console.WriteLine(builder.ToString());
        }
    }
}
namespace DataStructures.Factory
{
    public static class LinkedListFactory 
    {
        public static Node<T> ListToLinkedList<T>(List<T> list) 
        {
            Node<T> head = null;
            Node<T> pointer = null;
            foreach(T element in list)
            {
                if(pointer != null) 
                {
                    pointer.next = new Node<T>{value = element};
                    pointer = pointer.next;
                }
                else
                {
                    head = new Node<T>
                    {
                        value = element
                    };
                    pointer = head;
                }
            }
            return head;
        }
    }
}
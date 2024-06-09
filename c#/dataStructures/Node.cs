using System.Dynamic;

namespace DataStructures 
{
    public class Node<T>
    {
        public Node<T>? next {get; set;}
        public T value {get; set;}

        public Node () {}
    }
}
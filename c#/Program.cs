// See https://aka.ms/new-console-template for more information

using System.Data;
using System.Text;
using Algorithms;
using DataStructures;
using DataStructures.Factory;

var removeDuplicates = new RemoveDuplicates();

Node<int>? head = removeDuplicates.RemoveDuplicateSet(LinkedListFactory.ListToLinkedList(new List<int>(){1,5,7,7,5,5,6,6,2,3,4,5}));
LinkedListHelper.printLinkedList(head);

head = removeDuplicates.RemoveDuplicatesNoMem(LinkedListFactory.ListToLinkedList(new List<int>(){1,5,7,7,5,5,6,6,2,3,4,5}));
LinkedListHelper.printLinkedList(head);

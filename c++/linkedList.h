#ifndef LINKED_LIST
#define LINKED_LIST
#include <iostream>
#include <vector>

struct linkedListNode {
	int value;
	linkedListNode * next;
	linkedListNode(int);
};

void printLinkedList(linkedListNode*);
struct linkedListNode * vectorToList (std::vector<int> );

#endif

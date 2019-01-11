#include <iostream>
#include "linkedList.h"
void testLinkedList () {
	std::vector<int> numvec;
	numvec.push_back(1);
	numvec.push_back(2);
	struct linkedListNode * head = vectorToList(numvec);
	printLinkedList(head);
}
void testQueue () {
	class Queue* q = new Queue();
	q->addElement(1);
	q->addElement(2);
	q->addElement(3);
	q->printQueue();
	q->popElement();
	q->printQueue();
}
int main () {
	return 0;
}

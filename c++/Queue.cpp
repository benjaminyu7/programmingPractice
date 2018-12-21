#include "Queue.h"

Queue::Queue() {
	head = NULL;
	tail = NULL;
}
int Queue::addElement (int value) {
	if(tail == NULL) {
		head = new linkedListNode(value);
		tail = head;
	} else {
		tail->next = new linkedListNode(value);
		tail = tail->next;
	}
	return 0;
}
int Queue::popElement () {
	if (head == NULL) {
		std::cout << "Error: empty queue\n";
	} else {
		int temp = head->value;
		head = head-> next;
		//free memory
		return temp; 
	}
	return 0;
}
void Queue::printQueue () {
	printLinkedList(head);
}

int main () {
	class Queue* q = new Queue();
	q->addElement(1);
	q->addElement(2);
	q->addElement(3);
	q->printQueue();
	q->popElement();
	q->printQueue();
	return 0;
}

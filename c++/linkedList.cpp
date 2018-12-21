#include "linkedList.h"

linkedListNode::linkedListNode(int newValue) {
	value = newValue;
	next = NULL;
}
	
struct linkedListNode * vectorToList (std::vector<int> vec) {
	struct linkedListNode * head = new linkedListNode(vec[0]);
	struct linkedListNode * temp = head;
	for(int x = 1; x < vec.size(); x++){
		temp->next = new linkedListNode(vec[x]);
		temp = temp->next;
	}
	return head;
}

void printLinkedList(linkedListNode*head) {
	while(head != NULL) {
		std::cout << head->value;
		std::cout << "\n";
		head = head->next;
	}

}


#include <iostream>
#include "linkedList.h"
int main () {
	std::vector<int> numvec;
	numvec.push_back(1);
	numvec.push_back(2);
	struct linkedListNode * head = vectorToList(numvec);
	printLinkedList(head);
	return 0;
}

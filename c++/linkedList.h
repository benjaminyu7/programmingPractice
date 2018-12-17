#ifndef LINKED_LIST
#define LINKED_LIST
namespace linkedList {
	struct linkedListNode {
		int value;
		linkedListNode * next;
	};
}

struct linkedList * arrToList (int * array);

#ifndef QUEUE
#define QUEUE
#include "linkedList.h"
class Queue {
	private:
		struct linkedListNode * head;
		struct linkedListNode * tail;
	public:
		Queue();
		int addElement(int);
		int popElement();
		void printQueue();
};

#endif

class Node {
	int value;
	Node next;
	public Node (int value) {
		this.value = value;
		this.next = null;
	}
}

class Queue {
	private Node head;
	private Node tail;
	public Queue () {
		head = null;
		tail = null;
	}
	public void addValue (int value) {
		if (this.head == null) {
			this.head = new Node(value);
			this.tail = head;
		} else {
			this.tail.next = new Node (value);
			this.tail = this.tail.next;
		}
	}
	public int popValue () {
		int value;
		if (this.head != null) {
			value = this.head.value;
			this.head = this.head.next;
			return value;
		} else {
			//throw empty queue exception
		}
		return 0;
	}
}

class intQueue {
	static void testQueue() {
		Queue q = new Queue();
		q.addValue(5);
		q.addValue(3);
		q.addValue(1);
		System.out.println(q.popValue());
		System.out.println(q.popValue());
		System.out.println(q.popValue());
	}
	public static void main (String [] args) {
		System.out.println("Hello World!");
		testQueue();
	}
}

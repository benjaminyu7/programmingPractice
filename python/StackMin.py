class StackNode:
	def __init__(self,node_value, stack_minimum):
		self.node_value=node_value
		self.stack_minimum=stack_minimum
		self.next=None

class StackMin:
	def __init__(self):
		self.head=None
	def push(self,value):
		if(self.head==None):
			self.head=StackNode(value, value)
		else:
			if(value<self.head.stack_minimum):
				temp=StackNode(value,value)
				temp.next=self.head
				self.head = temp
			else:
				temp=StackNode(value,self.head.stack_minimum)
				temp.next=self.head
				self.head = temp
	def pop(self):
		if(self.head == None):
			return None
		temp=self.head
		self.head=self.head.next
		return temp.node_value
	def min(self):
		if(self.head == None):
			return None
		return self.head.stack_minimum

sm=StackMin()
sm.push(5)
sm.push(4)
print(sm.min())
print(sm.pop())
print(sm.min())
print(sm.pop())
print(sm.min())
print(sm.pop())

'''
This is the implementation of stack using python3.So, stack works on principle
'Last in First Out (FILO)'.This implementation uses adapter design pattern to
adapt list class of python3.
'''

class Stack():
    def __init__(self):
        self._stack = []         # empty list to store items

    def size(self):
        '''return length of stack'''
        return len(self._stack)

    def push(self,item):
        '''to add items in stack'''
        self._stack.append(item)

    def pop(self):
        '''to remove the last item from stack'''
        if len(self._stack) == 0:
            print('Stack is Empty')
        else:
            return self._stack.pop()

    def top(self):
        '''it's only return the last inserted or top item of the stack'''
        if len(self._stack) == 0:
            print('Stack is Empty')
        else:
            return self._stack[-1]

    def is_empty(self):
        'check stack is empty or not.'
        if len(self._stack) == 0:
            print('Stack is empty')
        else:
            print('Stack is not empty')

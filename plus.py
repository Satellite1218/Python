class ArrayStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return 1
        else:
            return 0

    def isFull(self):
        if self.top == self.stack_size - 1:
            return 1
        else:
            return 0

    def pop(self):
        if not self.isEmpty():
            item = self.list[self.top]
            self.top -= 1
            return item
        else:
            return 'stack is empty'

    def push(self, i):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = i
        else:
            return 'stack is full'

    def peek(self):
        if not self.isEmpty():
            return self.list[self.top]
        else:
            return "stack is empty"

def precedence(op):
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or op == '/' : return 2
    else : return -1

def infixToPostfix(expr):
    s=ArrayStack(100)
    output = []
    for term in expr :
        if term in '(':
            s.push('(')
        elif term in (')'):
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else: output.append(term)
    while not s.isEmpty(): output.append(s.pop())
    return output

infix1=input()
infix1=list(infix1)
postfix1=infixToPostfix(infix1)
print(postfix1)
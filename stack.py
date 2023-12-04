stack_size=5
list=[None]*stack_size
top=-1
def isEmpty(): #스택이 비어 있는지 확인한다
    if top==-1:
        return 1
    else:
        return 0

def isFull(): #스택이 차있는지 확인한다
    if top==stack_size-1:
        return 1
    else:
        return 0

def pop(): #스택의 맨 위에서 데이터를 제거하고, 그 데이터를 반환한다
    global top
    if not isEmpty():
        item=list[top]
        top-=1
        print(item)
        return
    else:
        print('stack is empty')
        return
    
def push(i): #스택의 맨 위에 데이터를 추가한다
    global top
    if not isFull():
        top+=1
        list[top]=i
        print(list)
        return
    else:
        print('stack is full')
        return

def peek(): #스택의 맨 위의 데이터를 조회한다
    if not isEmpty():
        print(list[top])
        return
    else:
        print("stack is empty")
        return

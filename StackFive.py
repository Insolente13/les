class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, element):
        self.stack.insert(self.size(), element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None



def five(brackets):
    brackets_stack = Stack()
    break_pop = None

    for x in brackets:
        if x == '(':
            brackets_stack.push(x)
        elif x == ')':
            break_pop = brackets_stack.pop()
            if break_pop is None:
                break

    if brackets_stack.size() == 0 and break_pop is not None:
        print('Cбалансированы')
    else:
        print('Не сбалансированы')


def post_fix(expression):
    S1 = Stack()
    S2 = Stack()
    for x in expression.replace(' ', ''):
        S1.push(x)

    for y in range(S1.size()):
        pops1 = S1.pop()
        if pops1.isdigit():
            S2.push(int(pops1))
        elif pops1 == '+':
            S2.push(S2.pop() + S2.pop())
        elif pops1 == '-':
            S2.push(S2.pop() - S2.pop())
        elif pops1 == '*':
            S2.push(S2.pop() * S2.pop())
        elif pops1 == '/':
            S2.push(S2.pop() / S2.pop())
        elif pops1 == '//':
            S2.push(S2.pop() // S2.pop())
        elif pops1 == '%':
            S2.push(S2.pop() % S2.pop())

    return S2.peek()

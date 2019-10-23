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


def post_fix(expression):
    S1 = Stack()
    S2 = Stack()
    for x in expression:
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
        elif pops1 == '=':
            return S2.peek()


def five(brackets):
    brackets_stack = Stack()
    answer = None

    for x in range(len(brackets)):
        if brackets[x] == '(':
            brackets_stack.push(brackets[x])
        elif brackets[x] == ')' and brackets_stack.pop() is None:
            if brackets_stack.pop() is None:
                answer = 'Не сбалансированы'
                break

    if brackets_stack.size() == 0 and answer is None:
        answer = 'Cбалансированы'
    elif brackets_stack.size() > 0:
        answer = 'Не сбалансированы'
    print(answer)

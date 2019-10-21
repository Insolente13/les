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



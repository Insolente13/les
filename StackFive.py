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
    break_point = 0
    count_pops = 0

    for x in brackets:
        brackets_stack.push(x)
    if brackets_stack.size() % 2 == 0 and brackets_stack.peek() != '(':
        for brack in range(brackets_stack.size()):
            brack_pop = brackets_stack.pop()
            if count_pops < 0:
                break_point += 1
                break
            else:
                if brack_pop == '(':
                    count_pops += 1
                elif brack_pop == ')':
                    count_pops -= 1
    else:
        break_point += 1

    if break_point == 0 and count_pops == 0:
        print('Cбалансированы')
    else:
        print('Не сбалансированы')


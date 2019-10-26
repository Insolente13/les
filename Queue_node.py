class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def delete(self):
        node = self.head
        #  удаляем первое и единственное
        if node is not None and node.next is None:
            self.head = None
            self.tail = None
        #  удаляем первое и НЕ единственное
        elif node is not None and node.next is not None:
            self.head = node.next
        else:
            return None

    def len(self):
        node = self.head
        count_node = 0
        while node is not None:
            count_node += 1
            node = node.next
        return count_node

    def in_stack(self):
        stack_list = []
        node = self.head
        while node is not None:
            stack_list.append(node.value)
            node = node.next
        return stack_list


class QueueDoubleStack:
    def __init__(self):
        self.stack_1 = LinkedList()
        self.stack_2 = LinkedList()
        # инициализация хранилища данных

    def enqueue(self, item):
        self.stack_1.add_in_tail(Node(item))
        # вставка в хвост

    def dequeue(self):
        if self.stack_2.len() == 0 and self.stack_1.len() != 0:
            self.stack_2.add_in_tail(self.stack_1.head)
            while self.stack_1.len() != 0:
                self.stack_1.delete()

        del_element = self.stack_2.head
        self.stack_2.delete()
        if del_element is None:
            return None
        else:
            return del_element.value
        # выдача из головы

    def size(self):
        return self.stack_1.len() + self.stack_2.len()  # размер очереди

    '''6.3. Напишите функцию, которая "вращает" очередь по кругу на N элементов.'''
    def circle(self, count):
        for x in range(count):
            self.enqueue(self.dequeue())

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # Если стек пустой, ничего не удаляем

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None  # Если стек пустой, возвращаем None

    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


# Пример использования:
input_expression = input("Введите строку со скобками: ")
result = is_balanced(input_expression)
print(result)

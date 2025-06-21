# 作者:python11-刘杰
# 2025年06月03日21时30分31秒
# xxx@qq.com
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.empty():
            return "stack is empty"
        return self.stack[-1]

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    stack.pop()
    stack.pop()
    print(stack.stack)
    stack.pop()
    stack.push(2)
    print(stack.stack)
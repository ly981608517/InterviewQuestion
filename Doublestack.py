#　第一种方法　
class DoubleStack():
    def __init__(self, limit=100):
        self.stack = []
        self.limit = limit

    def l_push(self, data):
        if len(self.stack) >= self.limit:
            print("在添加就溢出了")
        else:
            self.stack.insert(0, data)
        return self.check_stack()

    def r_push(self, data):
        if len(self.stack) >= self.limit:
            print("在添加就溢出了")
        else:
            self.stack.append(data)
        return self.check_stack()

    def l_pop(self):
        if len(self.stack) > 0:
            del self.stack[0]
        else:
            print("空栈不能执行pop操作")
        return self.check_stack()

    def r_pop(self):
        if len(self.stack) > 0:
            del self.stack[-1]
        else:
            print("空栈不能执行pop操作")
        return self.check_stack()

    # 查看整个栈
    def check_stack(self):
        return self.stack


# 用Python实现双头栈
if __name__ == '__main__':
    stack = DoubleStack(limit=10)
    print(stack.l_push(1))

    # print(stack.limit)
    #
    # print(stack.check_stack())
    # stack.r_push(1)
    # stack.r_push(2)
    # stack.r_push(3)
    # stack.r_push(4)
    # stack.r_push(5)
    # stack.r_push(6)
    #
    # print(stack.check_stack())
    #
    # stack.l_push(5)
    # stack.l_push(6)
    # stack.l_push(6)
    # stack.l_push(7)
    # stack.l_push(8)
    # stack.l_push(9)
    # print(stack.check_stack())
    #
    # stack.r_pop()
    # print(stack.check_stack())
    #
    # stack.l_pop()
    # print(stack.check_stack())
    #
    # stack.l_pop()
    # stack.l_pop()
    # stack.r_pop()
    # stack.l_pop()
    # stack.l_pop()
    # stack.l_pop()
    # stack.l_pop()
    # stack.r_pop()
    # print(stack.check_stack())

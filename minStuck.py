# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
#
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。

# 示例
# 输入：
# ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
# [[], [-2], [0], [-3], [], [], [], []]
#
# 输出：
# [null, null, null, null, -3, null, 0, -2]
#
# 解释：
# MinStack
# minStack = new
# MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();  --> 返回 - 3.
# minStack.pop();
# minStack.top();     --> 返回0.
# minStack.getMin();  --> 返回 - 2.
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStuck = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStuck and val <= self.minStuck[-1]:
            self.minStuck.append(val)

    def pop(self) -> None:
        x=self.stack.pop()
        if x == self.minStuck[-1]:
            self.minStuck.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStuck[-1]

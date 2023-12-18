class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        # ＃list
    # 加資料
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        # stack #LIFO  last in first out
        if len(self.stack)!=0:   #假設他不是空
            self.stack.pop()
            #else 啥都不做  None ,pop 也沒有return
        #要把最上面東西給人家
    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]

    def get_min(self) -> int:
        if len(self.stack)!=0:
            my_min =self.stack[0]
            for i in range(1,len(self.stack)):
                ele = self.stack[i]
                if ele<my_min:
                    my_min=ele
                return my_min



if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')
    print(my_stack.get_min(), end=', ')
    my_stack.pop()    #避免error
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top(), end=', ')
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top())
    # none,none,-1,3,-2,-2

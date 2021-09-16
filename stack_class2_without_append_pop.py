class Stack:
    def __init__(self, n):
        # self.stack = [None] * n
        self.stack = [None for _ in range(n)]
        # self.stack = [i+1 for i in range(n)]
        self.stack_size = 0
    
    def push(self, num):
        self.stack[self.size()] = int(num)
        self.stack_size += 1
    
    def pop(self):
        if self.size() > 0:
            last_val = self.top()
            # self.stack[self.size()-1] = None
            self.stack_size -= 1
            return last_val
        
        return -1
    
    def size(self):
        return self.stack_size

    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1

    def top(self):
        if self.size() > 0:
            return self.stack[self.size()-1]
        
        return -1

def run_cmd_with_stack(cmd, stack_lst):
    cmd_type = cmd[0]
    
    if cmd_type == "push":
        _, num = cmd
        stack_lst.push(num)
    elif cmd_type == "pop":
        print(stack_lst.pop())
    elif cmd_type == "size":
        print(stack_lst.size())
    elif cmd_type == "empty":
        print(stack_lst.empty())
    elif cmd_type == "top":
        print(stack_lst.top())
    
    return stack_lst

n = int(input())
stack_lst = Stack(n)

for _ in range(n):
    command = input().split()
    stack_lst = run_cmd_with_stack(command, stack_lst)

    print(stack_lst.stack)
    print(stack_lst.size())

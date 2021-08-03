class Stack:
    stack = []
    def push(self, n):
        self.stack.append(n)
        print('ok')
    def pop(self):
        out_elem = self.stack[-1]
        self.stack.pop()
        print(out_elem)
    def back(self):
        print(self.stack[-1])
    def size(self):
        print(len(self.stack))
    def clear(self):
        self.stack = []
        print('ok')
    def exit(self):
        print('bye')
        quit()


finish = False

while finish == False:
    s = Stack()
    func = ''
    param = ''
    input_str = input()
    if input_str == 'exit':
        finish = True

    for element in input_str:
        if element not in (' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            func += element
        elif element != ' ':
            param += element

    a = 's' + '.' + func + f'({param})'
    eval(a)
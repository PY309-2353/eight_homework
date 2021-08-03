class Queue:
    queue = []
    def push(self, n):
        self.queue.insert(0, n)
        print('ok')
    def pop(self):
        out_elem = self.queue[-1]
        self.queue.pop()
        print(out_elem)
    def front(self):
        print(self.queue[-1])
    def size(self):
        print(len(self.queue))
    def clear(self):
        self.queue.clear()
        print('ok')
    def exit(self):
        print('bye')
        quit()


finish = False

while finish == False:
    s = Queue()
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
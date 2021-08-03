class Deck:
    deck = []
    def push_front(self, n):
        self.deck.insert(-1, n)
        print('ok')
    def push_back(self, n):
        self.deck.insert(0, n)
        print('ok')
    def pop_front(self):
         out_elem = self.deck[-1]
         self.deck.pop()
         print(out_elem)
    def pop_back(self):
         out_elem = self.deck[0]
         del(self.deck[0])
         print(out_elem)

    def front(self):
        print(self.deck[-1])
    def back(self):
        print(self.deck[0])

    def size(self):
        print(len(self.deck))
    def clear(self):
        self.deck.clear()
        print('ok')
    def exit(self):
        print('bye')
        quit()


finish = False

while finish == False:
    s = Deck()
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
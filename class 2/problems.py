

def balance_check(s):
     
        if len(s)%2 != 0:
            return False

        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{','}')])
        stack = []
        for paren in s:
            if paren in opening:
                stack.append(paren)
                print("paren is found in opening; stack: %s" % stack)
            else:
                if len(stack) == 0:
                    print("Last open(last item from stack): %s" % last_open)
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False
        return len(stack) == 0

        if __name__ == "__main__":
            print(balance_check("({[]})"))

class Queue2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())\
        return self.stack2.pop()
        
        # reverse a string using this class

""" homework
    def test():

        q = Queue2Stacks()
        for i in range(5):
            q.enqueue(i)
        for i in range(5):
            print(q.dequeue())
"""

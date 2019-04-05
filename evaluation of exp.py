
class Node(object):
    """
    Creates a Node.
    Attributes: data, next_val
    """
    def __init__(self, data = None):
        self.data = data
        self.next_val = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_val

    def set_next(self, next_val):
        self.next_val = next_val

class Stack(object):
    """
    Creates a Stack using Linked Lists.
    Attributes: top
    """
    def __init__(self):
        self.top = None
        
    def push(self, value):
        """Pushes the element on the top"""
        new_node = Node(value)
        curr = self.top

        if curr == None:
            self.top = new_node

        else:
            new_node.next_val = self.top
            self.top = new_node

    def pop_element(self):
        """it pops out the element which is addeed recenty"""
        curr = self.top

        if curr == None:
            print("Stack is already empty.")

        else:
            temp = self.top.data
            self.top = self.top.next_val
            return temp
            
    def is_empty(self):
        return self.top == None
                            
def infix_postfix(expr):
# To convert infix exprssion into postfix
    res = ""
    prec = {'-': 0, '+': 0, '*': 1, '/': 1, '^': 2, '(': 3}
    s = Stack()
    
    for ch in expr:
        if ch == '(':
            s.push(ch)
        elif ch == ')':
            while s.top.data != '(':
                res += s.pop_element()
            s.pop_element()
        elif ch in prec:
            if s.top != None and prec[s.top.data] > prec[ch]:
                while s.top != None and prec[s.top.data] < prec[ch]:
                    res += s.pop_element()
                s.push(ch)
            else:
                s.push(ch)
        elif ch.isalnum():
            res += ch
    while s.top:
        res += s.pop_element()
    return res
    
def evaluate(expr):
# to evaluate the postfix expression
    expr = infix_postfix(expr)
    s = Stack()
    
    op = ['+', '-', '*', '/','^']
    
    for ch in expr:
        if ch not in op and ch != " ":
            
            s.push(ch)
        else:
            b = s.pop_element()
            a = s.pop_element()
            
            if ch == '+':
                s.push(int(a) + int(b))
            elif ch == '-':
                s.push(int(a) - int(b))
            elif ch == '*':
                s.push(int(a) * int(b))
            elif ch == '/':
                s.push(int(a) / int(b))
            elif ch == '^':
                s.push(int(a) ** int(b))
    return s.pop_element()

def is_expr_correct(expr):
# to check whether the given expressios is correct or not
    left = ['(', '[', '{']
    right = [')', ']', '}']
    s = Stack()    
    
    for ch in expr:
        if ch in left:
            s.push(ch)
            
        elif ch in right:
            if s.is_empty():
                return False
            if left.index(s.pop_element()) != right.index(ch):
                return False
                
    if s.is_empty():
        return True
    else:
        return False

def main():
    opt = -1
    while opt != 2:
        opt = input("1) to evalute \n2) to exit\n")
        if opt == '1':
            expression = input("Enter the expression with single digits and correctly paranthesized: ")
            if is_expr_correct(expression):
                print(evaluate(expression))
            else:
                print("Expression is not correct!!")
        else:
            break
            
if __name__ == "__main__":
    main()
'''
sample input     
(3*(2+6))/1
(2*9)+(4/2)
(2*(9+(8/2)))             
'''                            

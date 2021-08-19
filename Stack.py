"""
Stack Program
"""

class Stack(object):

    def __init__(self):
        """
        constructor for initialized
        """
        self.item=[]

    def push(self, item=''):
        """
        Push the element at last index
        :return: None
        """
        self.item.append(item)
        pass

    def pop(self):
        """
        This will remove last index
        :return: None
        """
        self.item.pop()
        pass

    def peek(self):
        """
        Allow us to see last element
        :return: Last item
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        """
        For display size of stack
        :return: length
        """
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):
        """
        tells whether the stack is empty or not
        :return: None
        """
        if self.item == []:
            print("stack is empty")
        else:
            return False

    def display(self):
        """
        To display stack element
        :return:None
        """
        if self.isempty():
            print("stack is empty")
        else:
            for item in self.item:
                print(item)

if __name__ == "__main__":

    stack=Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    stack.push("4")
    stack.push("5")
    stack.push("6")

    print("display all elements in stack")
    stack.display()
    print("size of stack")
    print(stack.size())
    print("Top element of stack")
    print(stack.peek())

    #print("Delete top element")
    stack.pop()
    print("After deleting element size of stack")
    print(stack.size())
    print("Top of element of stack")
    print(stack.peek())
    print("check stack is empty or not")
    #print(stack.isempty())
    if stack.isempty()==False:
        print("stack is not empty")

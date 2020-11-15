'''
Created on 13. lis 2020.

@author: bkumpar
'''

class Stack(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.container = []
        self.name = name
        pass

    def size(self):
        return len(self.container)

    def push(self, value):
        if value != None:
            self.container.append(value)

    def drop(self):
        self.container = self.container[0:-1]

    def peek(self):
        item = None
        if self.notEmpty() :
            item = self.container[-1]
        return item

    def pop(self):
        item = None
        if self.notEmpty() :
            item = self.container[-1]
            self.container = self.container[0:-1]
        return item

    def over(self):
        if len(self.container)>1:
            item =  self.container[-1]
            self.push(item)

    def rot(self):
        if len(self.container)>2:
            item1 = self.pop()
            item2 = self.pop()
            item3 = self.pop()
            self.push(item2)
            self.push(item1)
            self.push(item3)

    def rot2(self):
        self.rot()
        self.rot()

    def swap(self, value):
        self.container.append(value)
        if len(self.container)>1:
            val1 = self.pop()
            val2 = self.pop()
            self.push(val1)
            self.push(val2)

    def notEmpty(self):
        return self.size()>0

    def printMe(self):
        print( '{}: ({})'.format(self.name, self.container))


def main():        
    pass
    
    s = Stack('stack')
    s.push('a')
    s.push('b')
    s.push('c')
    s.printMe()
    s.rot2()
    s.printMe()
    
if __name__ == "__main__":
    main()
        
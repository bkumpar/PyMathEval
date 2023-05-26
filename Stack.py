#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bkumpar
#
# Created:     16.11.2020
# Copyright:   (c) bkumpar 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Stack:

    name = ''
    def __init__(self, name):
        self.container = []
        self.name = name
        pass

    def clear(self):
        self.container = []

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
        item = None
        if len(self.container)>1:
            item =  self.container[-1]
        return item

    def swap(self):
        if len(self.container)>1:
            val1 = self.pop()
            val2 = self.pop()
            self.push(val1)
            self.push(val2)

    def notEmpty(self):
        return self.size()>0

    def printMe(self):
        i = 1
        print(self.name)
        for item in self.container:
            print(i,": ", item)
            i += 1

def main():
    pass

if __name__ == '__main__':
    main()

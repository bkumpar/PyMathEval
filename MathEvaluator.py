'''
Created on 7. lis 2020.

@author: bkumpar
'''

#-------------------------------------------------------------------------------
# Name:        Evaluator
# Purpose:
#
# Author:      bkumpar
#
# Created:     06.10.2020
# Copyright:   (c) bkumpar 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import sqrt, sin
from Stack import Stack

class Evaluator:

    def add(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = val2 + val1
        self.valueStack.push(res)

    def sub(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = val2 - val1
        self.valueStack.push(res)

    def mul(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = val2 * val1
        self.valueStack.push(res)

    def div(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = val2 / val1
        self.valueStack.push(res)

    def powr(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = pow(val2, val1)
        self.valueStack.push(res)
        return 

    def sqrt(self):
        val1 = self.valueStack.pop()
        res = sqrt(val1)
        self.valueStack.push(res)
        return 

    def sin(self):
        val = self.valueStack.pop()
        res = sin(val)
        self.valueStack.push(res)
        return 

    def max(self):
        val1 = self.valueStack.pop()
        val2 = self.valueStack.pop()
        res = max(val2, val1)
        self.valueStack.push(res)
        return 
    
    def pi(self):
        res = 3.14
        self.valueStack.push(res)
        return 
    
    def nop(self):
        return None
    

    def __init__(self):
        self.digits = '0123456789.'
        # Operator:(Precedence,Associativity, function )
        self.operators = {'+': (2, 'left',self.add) 
                        , '-': (2, 'left', self.sub)
                        , '*': (3, 'left' ,self.mul)
                        , '/': (3, 'left', self.div)
                        , '^': (4, 'right', self.powr)
                        , 'sin': (5, 'right', self.sin)
                        , 'max': (5, 'right', self.max)
                        , 'pi': (5, 'right', self.pi)
                        , 'sqrt': (5, 'right', self.sqrt)
                        }
        self.output=''
        self.valueStack = Stack('values');
        self.operatorStack = Stack('operators');
    
        
    def processFunction(self, token):
        self.operatorStack.push(token)
 

    def procesLeftParenthesis(self, token):
        self.operatorStack.push(token)

    def procesRightParenthesis(self):
        while self.operatorStack.peek()!= '(':
            token = self.operatorStack.pop()
            self.pushToOutput(token)
        if self.operatorStack.peek() == '(':
            self.operatorStack.drop()
                    
    def processNumber(self,number):
        self.valueStack.push(float(number))
        self.pushToOutput(number)               
                   
    def operatorStackIsNotEmpty(self):
        return self.operatorStack.notEmpty()
                        
    def operatorOnStackHasGreaterPrecedence(self, operator):
        operatorOnStack = self.operatorStack.peek();
        operatorOnStackPrecedence = self.operators[operatorOnStack][0]
        operatorPrecedence = self.operators[operator][0]
        return operatorOnStackPrecedence > operatorPrecedence
    
    def operatorOnStackHasEqualPrecedenceAndLeftAssociativity(self, operator):
        operatorOnStack = self.operatorStack.peek();
        operatorOnStackPrecedence = self.operators[operatorOnStack][0]
        operatorPrecedence = self.operators[operator][0]
        operatorAssociativity = self.operators[operator][1]
        return (operatorOnStackPrecedence == operatorPrecedence) and operatorAssociativity == 'left'
        
    def operatorOnStackIsNotLeftParentheses(self):
        operatorOnStack = self.operatorStack.peek();
        return operatorOnStack != '('
        
        
    def processOperator(self, operator):
        while ((self.operatorStackIsNotEmpty())
              and (self.operatorOnStackIsNotLeftParentheses())
              and (( self.operatorOnStackHasGreaterPrecedence(operator))
                   or (self.operatorOnStackHasEqualPrecedenceAndLeftAssociativity( operator))
                   )
              ):        
            op = self.operatorStack.pop()
            self.pushToOutput(op) 
        
        self.operatorStack.push(operator)
        
    def finish(self):
        while self.operatorStack.notEmpty():
            op = self.operatorStack.pop()
            self.pushToOutput(op) 
            
    def pushToOutput(self, value):
        self.output+= '{} '.format(value)
        print(self.output)
                        
                        
    def parse(self,expression):
        self.output = ''
        number = ''
        token = ''
        for char in expression:
            if char == '=':
                break
            
            if char in self.digits:
                number += char
                
                if token!='':
                    self.processFunction(token)
                    token = ''
            elif char == ',':
                if token!='':
                    self.processFunction(token)
                    token = ''
                elif number != '':
                    self.processNumber(number)
                    number = ''
                
                pass        
            elif char == '(':
                if token!='':
                    self.processFunction(token)
                elif number != '':
                    self.processNumber(number)
                    number = ''
                self.procesLeftParenthesis(char)
                token = ''
                
            elif char == ')':
                if token!='':
                    self.processFunction(token)
                    token = ''
                elif number != '':
                    self.processNumber(number)
                    number = ''
               
                self.procesRightParenthesis()

            elif char in self.operators.keys():
                    if number != '':
                        self.processNumber(number)
                        number = ''
                    self.processOperator(char)
            else:
                token += char

        if number != '':
            self.processNumber(number)
            number = ''
            
        self.finish()              
                    
    def printMe(self):
        self.valueStack.printMe()
        self.operatorStack.printMe()
        print('--------------')


def main():
    expressions = [ ('sin(max(2,3)/3*pi())', '2 3 max 3 / pi * sin'), ('sqrt(9)', '9 sqrt'), ('10+12+33', '10 12 + 33 +'),('12/3/2', '12 3 / 2 /'), ('2^3*4^5+6=','2 3 ^ 4 5 ^ * 6 +'),]
    e = Evaluator()
    for expression in expressions:
        e.parse(expression[0])
        print(expression)
        print(e.output)
        
if __name__ == '__main__':
    main()

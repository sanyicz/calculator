import tkinter as tk

class Calculator(tk.Frame): #class inheritance
    def __init__(self, parentWindow):
        tk.Frame.__init__(self, parentWindow) #?
        self.mainWindow = parentWindow #?
        self.mainWindow.title('Calculator')
        self.font = ('Helvetica 30 bold')
        self.entryVar = tk.StringVar()
        self.entry = tk.Entry(self.mainWindow, width=19, font=self.font, textvariable=self.entryVar)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.buttons = []
        self.symbols = [[7, 8, 9, '+'], [4, 5, 6, '-'], [1, 2, 3, '*'], ['C', 0, '=', '/']]
        for i in range(0, len(self.symbols)):
            for j in range(0, len(self.symbols[i])):
                button = tk.Button(self.mainWindow, text=str(self.symbols[i][j]), width=4, height=2, font=self.font, command=lambda x=i, y=j: self.getSymbol(x, y))
                button.grid(row=i+1, column=j)
                self.buttons.append(button)
        self.expression = ''
        self.result = None

    def getSymbol(self, i, j):
        '''get the symbol of the button clicked and append self.expression
        if = is clicked, evaluate this expression'''
        self.symbol = self.symbols[i][j]
        #print(self.symbol)

        if self.result != None:
            self.expression = ''
            self.result = None

        if self.symbol == 'C':
            self.expression = ''
        elif self.symbol != '=':
            self.expression += str(self.symbol)
        else:
            self.result = self.evaluateExpression(self.expression)
##            self.result = eval(self.expression)
            if self.result == '':
                self.expression = 'Invalid operation.'
            else:
                self.expression += '=' + str(self.result)
        self.entryVar.set(self.expression)

    def evaluateExpression(self, expression):
        '''calculate self.expression assuming it is a binary operation on two integers'''
        a, b = '', ''
        operation = ''
        for symbol in expression:
            if symbol in '0123456789' and operation == '':
                a += symbol
            elif symbol in '0123456789':
                b += symbol
            elif symbol in '+-*/':
                operation = symbol
                b = ''
        #print(expression)
        #print(a, b, operation, sep=', ')
        if expression == str(a) + operation + str(b) and expression not in  ' +-*/':
            #used as intented
            if a != '':
                a = int(a)
            if b != '':
                b = int(b)
            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                result = a / b
            else:
                result = a
            #print(a, b, operation, result, sep=', ')
        else:
            #tried an invalid operation
            result = ''
            #print('invalid')
        return result
    
if __name__ == '__main__':
    root = tk.Tk()
    Calculator = Calculator(root)
    Calculator.grid(row=0, column=0)
    root.mainloop

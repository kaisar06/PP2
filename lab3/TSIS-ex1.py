class upperString:

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())


upperString = upperString()
upperString.getString()
upperString.printString()

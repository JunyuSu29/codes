class FormulaError(Exception): 

    def __init__(self,expression):
        self.expression=expression
        super().__init__(f"Invalid formula: {expression}")
    
    def checkElement(expression):
        lst=expression.split()
        if len(lst)!=3:
            raise FormulaError(expression)
try:
    expression="1 +"
    FormulaError.checkElement(expression)
    print("expression is valid")
except FormulaError as e:
    print(e)
    def countElement(e):
        print("This is TypeError")
            


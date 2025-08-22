class Shape:
    def __init__(self,color):
        self.__color=color
    
    def set_color(self,color):
        self.__color=color
        if not color:
            raise SyntaxError("Color cannot be empty")
    
    def get_color(self):
        return f"Color:{self.__color}"
    
class Square(Shape):
    def __init__(self,color,side_length):
        super().__init__(color)
        self.__side_length=side_length
         
    def set_side_length(self,side_length):
        self.__side_length=side_length
        if side_length<=0:
            raise ValueError("Side length must be positive in Geometry")
        
    def get_side_length(self):
        return f"Side Length:{self.__side_length}"
        
    def area(self):
        area=self.__side_length ** 2
        return f"Area of the square:{area}"
    
shape=Shape("Blue")
print(shape.get_color())
square=Square("Red",4)
print(square.get_color())
print(square.get_side_length())
print(square.area())
square.set_side_length(5)
print(square.get_side_length())

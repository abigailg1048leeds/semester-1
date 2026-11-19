# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

        try:
            if height <=0 or width <=0:
                raise ValueError
        except:
            raise TypeError
        
    def is_square(self):
        """check if rectangle has a secret alter ego as a square"""
        if self.height == self.width:
            return True
        else:
            return False
        
    def area(self):
        """calculates the area of the rectangle :D"""
        return int(self.height*self.width)
    
    def perimeter(self):
        """adds up the lenghts of each of the sides of the rectangle that might actually be a square"""
        return int(2*(self.height+self.width))


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

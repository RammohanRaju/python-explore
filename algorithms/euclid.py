__author__ = "Ramamohan Raju Gadiraju"
__email__ = "rammohan2419@gmail.com"

class Euclid(object):
    """Class to find Greatest Common Divisor between the given two numbers using Euclid's algorithm."""

    def __init__(self, x, y):
        """
        Initializes the Class with the given two numbers.

        Args:
            x(int): first number.
            y(int): second number.
        """
        self.x = x;
        self.y = y;
        self.input_x = x;
        self.input_y = y;

    def findGCD(self):
        """
        Finds the Greatest Common Divisor (GCD) of the given two numbers.

        Returns:
            greatest common divisor (number).
        """
        while self.y != 0:
            if self.x > self.y:
                self.x = self.x - self.y;
            else:
                self.y = self.y - self.x;
        return self.x;

    def printGCD(self):
        """
        Prints the Greatest Common number of the given two numbers.
        """
        print "Greatest Common Divisor of ",self.input_x," and ",self.input_y," is: ",self.findGCD();


print "### Greatest Common Divisor(GCD) using Euclid's algorithm. ###"
euclid = Euclid(102,24);
euclid.printGCD();

euclid = Euclid(24,48);
euclid.printGCD();

euclid = Euclid(1,48);
euclid.printGCD();

euclid = Euclid(15,0);
euclid.printGCD();

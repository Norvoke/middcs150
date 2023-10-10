"""
CS150 OOP Example
Parts of this example were adapted from Alvarado C. et al. (2020). CS for all. Franklin Beedle & Associates
"""

# Define a class named Rational (we capitalize class names to distinguish them from functions, etc.).
# Note that classes need docstrings too!
class Rational:
    """Represent a rational number as the ratio of two integers

    Attributes:
        numerator, denominator: Integers defining this rational number
    """
    
    # Define an initializer that sets the numerator and denominator attributes. It too needs a
    # docstring, but note we don't include a return value since it does not return. We also
    # don't document the self parameter since it already has a defined role in the Python
    # language specification.
    def __init__(self, numerator, denominator):
        """Initialize a rational number from the numerator and denominator

        Args:
            numerator, denominator: Integers defining this rational number
        """
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
        
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator 
    
    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return self.__class__(numerator, denominator)
    
    
    
# The Dollar class is derived from Rational, that is Rational is the "base" class (sometimes called 
# "parent" class) and Dollar the "derived" (or "child") class. As a result, Dollar inherits all of 
# Rational's attributes and methods.
class Dollar(Rational):
    """Represent US dollars without loss of precision"""
    def __init__(self, cents, denominator=100):
        """Initialize Dollar from a number of cents

        Args:
            cents: Number of US cents
            denominator: Optional integer >= 100 that must be a multiple of 100. If it is
            greater than 100, i.e., cents represents fractions of a penny, cents are renormalized
            to be an integer numer of pennies. Default value of 100.
        """
        # Reduce numerator to have 100 as the denominator, so the values stay "normalized"
        assert denominator % 100 == 0, "Denominator is not a multiple of 100"
        normalize = (denominator // 100)
        assert cents == 0 or cents >= normalize, "Not a valid number of cents given denominator"
        # Initialize the parent Rational class with the desired numerator and denominator
        super().__init__(cents // normalize, 100)
    
    def __str__(self):
        # Use the format method to specify 0 padding up to two digits for cents
        return "${}.{:02d}".format(self.numerator // 100, self.numerator % 100)
        
        
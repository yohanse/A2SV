from math import gcd

class Fraction:
    
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        common = gcd(abs(numerator), abs(denominator))
        self.__numerator = numerator // common
        self.__denominator = denominator // common

    @property
    def get_numerator(self):
        return self.__numerator
    
    @property
    def get_denominator(self):
        return self.__denominator
    
    # Method for addition
    @staticmethod
    def add(fraction1, fraction2):
        fraction1_nem, fraction1_den = fraction1.get_numerator, fraction1.get_denominator
        fraction2_nem, fraction2_den = fraction2.get_numerator, fraction2.get_denominator
        new_numerator = fraction1_nem * fraction2_den + fraction2_nem * fraction1_den
        new_denominator = fraction2_den * fraction1_den
        return Fraction(new_numerator, new_denominator)
    
    # Method for subtraction
    @staticmethod
    def subtract(fraction1, fraction2):
        fraction1_nem, fraction1_den = fraction1.get_numerator, fraction1.get_denominator
        fraction2_nem, fraction2_den = fraction2.get_numerator, fraction2.get_denominator
        new_numerator = fraction1_nem * fraction2_den - fraction2_nem * fraction1_den
        new_denominator = fraction2_den * fraction1_den
        return Fraction(new_numerator, new_denominator)
    
    # Method for multiplication
    @staticmethod
    def multiply(fraction1, fraction2):
        fraction1_nem, fraction1_den = fraction1.get_numerator, fraction1.get_denominator
        fraction2_nem, fraction2_den = fraction2.get_numerator, fraction2.get_denominator
        new_numerator = fraction1_nem * fraction2_nem
        new_denominator = fraction1_den * fraction2_den
        return Fraction(new_numerator, new_denominator)

    # Method for division
    @staticmethod
    def divide(fraction1, fraction2):
        fraction1_nem, fraction1_den = fraction1.get_numerator, fraction1.get_denominator
        fraction2_nem, fraction2_den = fraction2.get_numerator, fraction2.get_denominator
        new_numerator = fraction1_nem * fraction2_den
        new_denominator = fraction1_den * fraction2_nem
        return Fraction(new_numerator, new_denominator)
    
    # Method to represent the fraction as a string
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    

# Example usage:
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

sum_fractions = Fraction.add(fraction1, fraction2)
print(f"Sum: {sum_fractions}")

difference_fractions = Fraction.subtract(fraction1, fraction2)
print(f"Difference: {difference_fractions}")

product_fractions = Fraction.multiply(fraction1, fraction2)
print(f"Product: {product_fractions}")

quotient_fractions = Fraction.divide(fraction1, fraction2)
print(f"Quotient: {quotient_fractions}")
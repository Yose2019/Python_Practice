# this is an initial simple project to design a math module as your choice

# ------ARITHMETIC CALCULATOR SECTION-----
# ----mostly deals with two digit calculator
class arithmeticCalculator:
    
    @staticmethod
    def add(a,b):
        return a+b 
    
    @staticmethod
    def subtract(a,b):
        return a-b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
    @staticmethod
    def integerDivision(a,b):
        # handle exception for denominator and zero division error
        try:
            return a//b
        except ZeroDivisionError:
            return "ZeroDivisionError"
    
    @staticmethod
    def floatDivision(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "ZeroDivisionError"
    
    @staticmethod
    def power(a,b):
        return a**b
    
    @staticmethod
    def sqr(a):
        return a**2
    
    @staticmethod
    def sqrt(a):
        return round(a**(0.5),4)
    
# --- CERTAIN FUNCTIONALITIES OF MATHEMTICIS LIKE---
# --- FINDING GCD, FACTORIAL, FIBONACCI, LCM, HCF ---
class mathFunctional:

    @staticmethod
    def fact(self, num):
        if num==0:
            return 1
        else:
            factorial = 1
            while num != 0:
                factorial *= num
                num -= 1
            return factorial


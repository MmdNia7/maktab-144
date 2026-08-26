#4
from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        # انتقال علامت منفی مخرج به صورت
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # ساده کردن کسر
        common_divisor = gcd(numerator, denominator)

        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    # نمایش کسر با print
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # جمع
    def __add__(self, other):
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # تفریق
    def __sub__(self, other):
        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # ضرب
    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # تقسیم
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Fraction(numerator, denominator)

    # برابر
    def __eq__(self, other):
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    # نابرابر
    def __ne__(self, other):
        return not self == other

    # کوچک‌تر از
    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    # کوچک‌تر یا مساوی
    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    # بزرگ‌تر از
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    # بزرگ‌تر یا مساوی
    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction3 = Fraction(2, 4)

print(fraction1)  # 1/2
print(fraction2)  # 3/4

print(fraction1 + fraction2)  # 5/4
print(fraction1 - fraction2)  # -1/4
print(fraction1 * fraction2)  # 3/8
print(fraction1 / fraction2)  # 2/3

fraction3 = Fraction(4, 8)
print(fraction3)

print(fraction1 < fraction2)   # True
print(fraction1 <= fraction3)  # True
print(fraction1 == fraction3)  # True
print(fraction1 != fraction2)  # True
print(fraction2 > fraction1)   # True
print(fraction2 >= fraction1)  # True
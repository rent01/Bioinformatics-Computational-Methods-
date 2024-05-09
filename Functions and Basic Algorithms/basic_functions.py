# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/20/2023 4:25 PM
# @File : basic_functions.py
# -------------------------------
# Probelm 1
def multiply(a, b):
    """
    find the product of two number
    """
    return a * b
# if __name__ == "__main__":
x = multiply(5, 10)
print("The value of x is {}".format(x))


# Problem 2
def hello_name(name=None):
    """
    test a name
    """
    if name:
        return "Hello, " + name + "!"
    else:
        return "Hello, you!"

print(hello_name("Akbar"))
print(hello_name())


# Probelm 3,
def less_than_ten(a):
    # a = [1, 5, 81, 10, 8, 2, 102]
    b = []
    for i in a:
        if i < 10:
            b.append(i)
    return b
print(less_than_ten([1, 5, 81, 10, 8, 2, 102]))

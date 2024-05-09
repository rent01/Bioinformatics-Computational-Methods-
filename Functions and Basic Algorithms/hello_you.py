# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/25/2023 5:16 PM
# @File : hello_you.py
# -------------------------------
import sys

def hello_name(name=None):
    """
    test a name
    """
    if name:
        return "Hello, " + name + "!"
    else:
        return "Hello, you!"

if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count > 1:
        # raise Exception("This script requires only 1 arguments")
        name = sys.argv[1]
    else:
        name = None
    print(hello_name(name))

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:24:48 2024

@author: ADMIN
"""

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a== 0 and b != 0:
    print("phương trình vô nghiệm.")
elif a==0 and b==0 :
    print("phương trình có vô số nghiệm.")
else:
    print("nghiệm của phương trình là: ", -b/a)
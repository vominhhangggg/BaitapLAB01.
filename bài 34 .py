# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:29:00 2024

@author: ADMIN
"""

n = int(input("Nhập vào một số nguyên dương n: "))

if n <= 1:
    print(n, "không phải là số nguyên tố.")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "không phải là số nguyên tố.")
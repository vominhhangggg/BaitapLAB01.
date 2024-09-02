# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:21:22 2024

@author: ADMIN
"""

n = int(input("Nhập vào số nguyên n: "))
if n>0 :
    S = n * (n + 1) * (2 * n + 1) // 6
    print("Tổng bình phương dãy số là: ", S)
else:
    print("Không thỏa mãn bài toán.")
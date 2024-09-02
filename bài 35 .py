# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:37:31 2024

@author: ADMIN
"""

N = int(input("Nhập vào số nguyên n: "))
if N>0 :
    S = N*(N+1)//2
    print("Tổng dãy số là: ", S)
else:
    print("Không thỏa mãn bài toán.")
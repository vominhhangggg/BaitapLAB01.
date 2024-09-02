# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:32:01 2024

@author: ADMIN
"""

N = int(input("Nhập vào số nguyên n: "))
if N % 2 == 0 and N>0:
    S = (N / 2) * ((N / 2)+ 1)
    print("Tổng dãy số chẵn là: ", S)
else:
    print("Không thỏa mãn đề bài toán.")
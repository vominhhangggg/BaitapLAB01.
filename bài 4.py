# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:01:23 2024

@author: ADMIN
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
if 10 <= N <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong = hang_chuc + hang_don_vi
    print("Tổng các chữ số của N là: ", tong)
else:
    print("Vui lòng nhập một số nguyên dương có 2 chữ số.")
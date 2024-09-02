# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:22:32 2024

@author: ADMIN
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
if 0 <= a <= 24 and 0 <= b <= 59 and 0 <= c <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ.")
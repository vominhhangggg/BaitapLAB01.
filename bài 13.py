# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:35:47 2024

@author: ADMIN
"""

a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))
# Ngày tháng năm 
print("ngày tháng năm:"f"{a}/{b}/{c}")
# Ngày tháng năm ( chỉ lấy 2 số cuối của năm)
d = c % 100
print("ngày tháng (năm lấy 2 số cuối ):", f"({a}/{b}/{d})")
# đổi vị trí năm ngày
print(" Đổi vị trí Ngày, năm :", f"{c}/{b}/{a}")
# ngược lại
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
print(f"Ngày sinh là: {ngay}/{thang}/{nam}")
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:43:51 2024

@author: ADMIN
"""

a = int(input("Nhập năm sinh của bạn: "))
if 1900 <= a < 2024:
    tuổi = 2024 - a
    print("Tuổi của bạn hiện nay là: ", tuổi)
elif a == 2024:
    print("Bạn chưa tròn 1 tuổi")
else:
    print("Năm sinh bạn nhập không hợp lệ")
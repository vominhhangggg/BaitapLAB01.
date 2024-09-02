# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:07:01 2024

@author: ADMIN
"""

hinh = input("Nhập hình bạn muốn tính (v: vuông, n: chữ nhật, t: tròn): ")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    dien_tich = canh * canh
    print("Diện tích hình vuông là: ", dien_tich)
    chu_vi = 4 * canh
    print("Chu vi hình vuông là: ", chu_vi)
elif hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    dien_tich = chieu_dai * chieu_rong
    print("Diện tích hình chư nhật là: ", dien_tich)
    chu_vi = 2 * (chieu_dai + chieu_rong)
    print("Chu vi hình chữ nhật là: ", chu_vi)
elif hinh == 't':
    r = float(input("Nhập bán kính hình tròn: "))
    dien_tich = 3.14 * r * r 
    print("Diện tích hình tròn là: ", dien_tich)
    chu_vi = 2 * 3.14 * r
    print("Chu vi hình tròn là: ", chu_vi)
else:
    print("Hình bạn nhập không hợp lệ!")  
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:06:48 2024

@author: ADMIN
"""
number_to_string={0: "không",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",6:"sáu",7:"bảy", 8:"tám",9:"chín" }
a = int(input("Nhập số của bạn: "))
if 0 <= a <= 9:
    print(" chữ số :",number_to_string[a])
else:
    print("không hợp lệ")
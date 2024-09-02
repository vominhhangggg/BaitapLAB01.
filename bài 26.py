# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:33:47 2024

@author: ADMIN
"""

#Câu a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a>b:
    a,b=b,a
elif a>c:
    a,c=c,a
elif b>c:
    b,c=c,b
print("Thứ tự tăng dần của các số: ", a,b,c)
#Câu b
N = int(input("Nhập số nguyên N: "))
digits = [int(d) for d in str(N)]
digits.sort()
ketqua=int(''.join(map(str,digits)))
print("Kết quả là: ",ketqua)
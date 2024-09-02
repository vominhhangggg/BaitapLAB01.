# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:29:30 2024

@author: ADMIN
"""

a= float(input("Nhập quãng đường(km ) : "))
if a<=1 :
   print ("tiền cước taxi là : 15000đ")
elif 2<=a<=5:
    print ("tiền cước taxi là : ", 15000+(a-1)*13500 ,"đ")
elif a>6 and a<=120 :
    print ("tiền cước taxi là : ", 15000+4*13500+(a-6)*11000, "đ")
else : 
    print("tiền cước taxi là : ", (15000+4*13500+(a-6)*11000)-((15000+4*13500+(a-6)*11000)*(10/100)), "đ")
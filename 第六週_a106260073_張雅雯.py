# -*- coding: utf-8 -*-
"""第六週-A106260073 張雅雯

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T3MLGRXgZ5NykD54f6qzm6sDGFFmvh9O
"""

第一次=int(input("第一次期中考成績為?"))

第二次=int(input("第二次期中考成績為?"))

第三次=int(input("期末考成績為?"))

總分 = 第一次*1+第二次*1+第三次*1
平均 =總分/3
print("總分為",總分,'平均為',平均)

第一次=int(input("請輸入幾尺?"))

第二次=int(input("請輸入幾吋?"))


轉換公式 = (第一次*12+第二次*1)*2.54
print("轉換成",轉換公式,"公分")

x=float(input('請輸入座號?'))
y=x/4.75
print('組別為',y)

幾罐=float(input('輸入購買飲料的罐數'))
幾打=幾罐/12
剩餘=int(幾打)
幾打的價格=(幾打-剩餘)*200 #2.5-2 

剩餘的價格=剩餘*200

總共=幾打的價格+剩餘的價格
print('需花費',總共)


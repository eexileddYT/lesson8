#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:40:54 2021

@author: 蔡侑廷
"""

inv = int(input('amount of apples in inventory? '))
cost = int(input('price per apple? '))
purchase = int(input('how many apples purchased? '))
sold = int(input('how many apples sold today? '))
trans = int(input('how many transactions? '))
income = (cost * sold)
left = (inv - sold + purchase)

i = 0

tr = []

while i < trans:
    w = int(input('number of apples sold in transaction? '))
    tr.append(w)
    i = 1 + i
    
print('there are ', left, 'apples left')
print('income today is ', income)

# -*- coding: utf-8 -*-

"""
Test program for practicing Korean numbers

Script randomly generates plain numbers, ages, or times in either english
or korean and asks for the translation.

If you only want to practice a subset of these, change the `options` array

Author: Frank Cangialosi <frankc@csail.mit.edu, fcangialosi94@gmail.com>

usage:
    python knum.py

"""

import sys
from math import log
from random import randint,choice

sino_ones = ["","일","이","삼","사","오","육","칠","팔","구"]
sino_powers = ["","십","백","전","만"]

def sino_num(i):
    if i == 0:
        return "공"
    s = ""
    place = 1
    while i >= (10**(place-1)):
        val = (i % 10**place) / (10**(place-1))
        if place == 1:
            s = sino_ones[val] + s
        else:
            s = (sino_ones[val] if val!=1 else "") + (sino_powers[place-1] if val != 0 else "") + s
        place+=1
    return s

native_ones = ["","하나","둘","셋","넷","다섯","여섯","일곱","여덟","아홉","열"]
native_tens = ["","열","스물","서른","마흔","쉰","예순","일흔","여든","아흔"]

def native_num(i):
	if i >= 100:
		return sino_num((i/100)*100) + native_num(i % 100)
	else:
		return (native_tens[(i % 100 / 10)] if i >= 10 else "") + native_ones[(i % 10)]

ages = ["한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열", "열한", "열두", "열세", "열네", "열다섯", "열여섯", "열일곱"," 열여덟살", "열아홉", "스무", "스물한", "스물두", "스물세", "스물네", "스물다섯", "스물여섯", "스물일곱", "스물여덟", "스물아홉", "서른", "서른한", "서른두", "서른세", "서른네", "서른다섯", "서른여섯", "서른일곱", "서른여덟", "서른아홉", "마흔", "마흔한", "마흔두", "마흔세", "마흔네", "마흔다섯", "마흔여섯", "마흔일곱", "마흔여덟", "마흔아홉", "쉰"," 쉰한", "쉰두", "쉰세", "쉰네", "쉰다섯", "쉰여섯", "쉰일곱", "쉽여덟", "쉰아홉", "예순", "예순한", "예순두", "예순세", "예순네", "예순다섯", "예순여섯", "예순일곱", "예순여덟", "예순아홉", "일흔", "일흔한", "일흔두", "일흔세", "일흔네", "일흔다섯", "일흔여섯", "일흔일곱", "일흔여덟", "일흔아홉", "여든", "여든한", "여든두", "여든세", "여든네", "여든다섯", "여든여섯", "여든일곱", "여든여덟", "여든아홉", "아흔", "아흔한", "아흔두", "아흔세", "아흔네", "아흔다섯", "아흔여섯", "아흔일곱", "아흔여덟", "아흔아홉", "백"]

def pick_sino():
	x = randint(1,9999)
	sino_x = sino_num(x)
	if randint(0,1):
		guess = raw_input("{0} Sino = ".format(x)).strip()
		return guess == sino_x, sino_x
	else:
		guess = raw_input("{0} = ".format(sino_x)).strip()
		return guess == str(x), str(x)

def pick_native():
	x = randint(1,9999)
	native_x = native_num(x)
	if randint(0,1):
		guess = raw_input("{0} Native = ".format(x)).strip()
		return guess == native_x, native_x
	else:
		guess = raw_input("{0} = ".format(native_x)).strip()
		return guess == str(x), str(x)

def pick_time():
	hour = randint(1,12)
	minute = randint(1,59)
	time_string = "{0:02d}:{1:02d}".format(hour,minute)
	if minute == 30:
		korean_time = ages[hour-1] + "시" + "반"
	else:
		korean_time = ages[hour-1] + "시" + sino_num(minute) + "분"
	if randint(0,1):
		guess = raw_input("{0} = ".format(time_string)).strip()
		return guess == korean_time, korean_time
	else:
		guess = raw_input("{0} = ".format(korean_time)).strip()
		return guess == time_string, time_string

def pick_age():
	age = randint(1,len(ages))
	korean_age = ages[age-1]+" 살"
	if randint(0,1):
		guess = raw_input("{0} years = ".format(age)).strip()
		return guess == korean_age, korean_age
	else:
		guess = raw_input("{0} = ".format(korean_age)).strip()
		return guess == str(age), str(age)

# NOTE Change this to limit the types of questions asked
options = [pick_sino, pick_native, pick_time, pick_age]

if __name__ == '__main__':
    while True:
            correct,real = choice(options)()
            if correct:
                    print u'\u2713'
            else:
                    print u'\u2718',real


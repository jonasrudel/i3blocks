#!/bin/python3

import time

hour=int(time.strftime("%I"))
minute=int(time.strftime("%M"))

texthours = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]


textminutes = ["", "five past ", "ten past ", "fifteen past ", "twenty past ", "twentyfive past ", "half past ", "twentyfive to ", "twenty to ", "fifteen to ", "ten to ", "five to "]

if minute > 32:
    if hour < 12: 
        hour+=1
    else:
        hour = 1
if (minute > 57):
    minute-=60

minute+=2

print(textminutes[int(minute/5)] + texthours[hour-1])

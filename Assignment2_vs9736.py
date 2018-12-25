
## [Assignment 2] Vinayak Sahal vs9736

import turtle

#1

import math

length = float(input('Enter the length from the center to a vertex: '))
side = ((2 * length) * (math.sin(math.pi / 5)))
area = (((3 * math.sqrt(3)) / 2) * (side * side))
print('The area of the pentagon is ' + str(round(area,2)))


#2

name = str(input('Enter employee\'s name: '))
hoursWorked = float(input('Enter number of hours worked this week: '))
hourlyRate = float(input('Enter hourly rate: '))
fedTax = int(input('Enter federal tax withholding rate (%): '))
stateTax = float(input('Enter state tax withholding rate (%): '))

grossPay = hoursWorked * hourlyRate
federalWithholding = grossPay * (fedTax / 100)
stateWithholding = grossPay * (stateTax / 100)
netPay = float(grossPay - (federalWithholding + stateWithholding))
print('Weekly Pay Statement for ' + name)
print('Hours Worked:', '{:>8.1f}'.format(hoursWorked))
print('Pay Rate: {:>12}'.format('${:.2f}'.format(hourlyRate)))
print('Gross Pay: {:>11}'.format('${:.2f}'.format(grossPay)))
print('Deductions:')
print('  Federal Withholding (' + str(fedTax) + '%' + '):', '{:>6}'.format('${:.2f}'.format(federalWithholding)))
print('  State Withhholding (' + str(stateTax) + '%' + '):', '{:>6}'.format('${:.2f}'.format(stateWithholding)))
print('Net Pay: $' + str(round(netPay,2)))


#3

v = turtle.Turtle()
v.circle(50)
v.penup()
v.goto(0,100)
v.pendown()
v.circle(40)
v.penup()
v.goto(0,180)
v.pendown()
v.circle(30)
v.penup()
v.goto(0,120)
v.pendown()
v.dot(5)
v.penup()
v.goto(0,135)
v.pendown()
v.dot(5)
v.penup()
v.goto(0,150)
v.pendown()
v.dot(5)
v.penup()
v.goto(-10,210)
v.pendown()
v.dot(5)
v.penup()
v.goto(10,210)
v.pendown()
v.dot(5)
v.penup()
v.goto(0,205)
v.pendown()
v.dot(5)
v.penup()
v.goto(-7,195)
v.pendown()
v.circle(50,20)
v.penup()
turtle.bye()






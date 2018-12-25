## [Assignment 1] Vinayak Sahal vs9736

#1

name = input('What is your name? ')
print('Hello ' + name + '!' ' You\'ve just delved into Python.')


#2

c_temperature = int(input('Enter a degree in Celsius: '))
f_temperature = float((9/5 * c_temperature) + 32)
print(str(c_temperature) + ' Celsius is ' + str(f_temperature) + ' Fahrenheit')


#3

bill, gratuityRate = eval(input('Enter the bill and gratuity rate: '))
gratuity = (bill * (gratuityRate/100))
totalBill = bill + gratuity
print('The gratuity is $' + str(format(gratuity,'.2f')) + ' and the total is $' + str(format(totalBill,'.2f')))


#4

number = int(input('Enter a number between 0 and 1000:'))
x1 = number % 10
x11 = number // 10
x2 = x11 % 10
x22 = x11 // 10
x3 = x22 % 10
x33 = x22 // 10
print('The sum of the digits is ', x1 + x2 + x3)


#5

currentPopulation = int(input('Enter the current population: '))
birthSeconds = 7
deathSeconds = 13
immigrantSeconds = 45
yearSeconds = 60*60*24*365
year1population = currentPopulation + ((yearSeconds // birthSeconds) + (yearSeconds // immigrantSeconds)) - (yearSeconds // deathSeconds)
year2population = year1population + ((yearSeconds // birthSeconds) + (yearSeconds // immigrantSeconds)) - (yearSeconds // deathSeconds)
year3population = year2population + ((yearSeconds // birthSeconds) + (yearSeconds // immigrantSeconds)) - (yearSeconds // deathSeconds)
year4population = year3population + ((yearSeconds // birthSeconds) + (yearSeconds // immigrantSeconds)) - (yearSeconds // deathSeconds)
year5population = year4population + ((yearSeconds // birthSeconds) + (yearSeconds // immigrantSeconds)) - (yearSeconds // deathSeconds)

print('The population in 1 year will be:', year1population)
print('The population in 2 years will be:', year2population)
print('The population in 3 years will be:', year3population)
print('The population in 4 years will be:', year4population)
print('The population in 5 years will be:', year5population)


#6

poundWeight = int(input('Enter your weight in pounds: '))
feet, inches = eval(input('Enter your height (feet, inches): '))
kgWeight = poundWeight * 0.454
heightFeet = feet + float((inches / 12))
heightMeter = heightFeet * 0.3048
BMI = kgWeight / (heightMeter ** 2)
print('Your BMI is ' + str(round(BMI,2)))


































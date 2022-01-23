#Задача №1

#a = [0]*100
#a[0] = '1'
#a[-1] = '1'
#print(a)

#Задача №2

#a = list(range(0, 90, 2))
#print(a)

#Задача №3

#x = int(input())
#numbers = [1, 2, 3, 4, 5]

#if x in numbers:
#    print('Это число есть в списке')
#else:
#    print('Этого числа нет в списке')

#Задача №4

#sum = 0
#proizv = 1

#numbers = [1, 2, 3, 4, 5]

#for number in numbers:
#    sum += number
#    proizv *= number

#print(sum)
#print(proizv)

#Задача №5

#numbers = [1, 2, 3, 4, 5]
#max = 0

#for number in numbers:
#    if number > max:
#        max = number

#print(max)

#Задача №6

#numbers = [1, 2, 3, 4, 4]

#for number in numbers:
#    if numbers.count(number) > 1:
#        print(number)
#    else:
#        None

#Задача №7  (НЕ ПОЛУЧИЛАСЬ)

#numbers = [1, 2, 3, 4, 5]
#max = 0
#min = numbers[0]

#for number in numbers:
#    if number > max:
#        max = number
#    if number < min:
#        min = number

#print(max)
#print(min)

#for number in numbers:
#    if number == max:
#       numbers.insert(number,min)
#    if number == min:
#        numbers.insert(number,max)

#print(numbers)

#Задача №8

#numbers = [1, 2, 3, 4, 5]
#print(numbers[::-1])
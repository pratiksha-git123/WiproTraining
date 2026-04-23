#functions
# def add(n1,n2):
#     return n1 + n2
#
# def sub(n1,n2):
#     return n1 - n2
#
# def mul(n1,n2):
#     return n1 * n2
#
# def div():
#     pass
#
# #driver
# num1 = int(input("enter a num:"))
# num2 = int(input("enter another num:"))
#
# res = add(num1, num2)
# print('Addition: ', res)
# res = sub(num1, num2)
# print('Subtraction: ', res)
# res = mul(num1, num2)
# print('Multiplication: ', res)


#Arbitary
# def add(nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum
#
# numbers = list()
# count = int(input('How many ? '))
#
# for _ in range(1, count+1):
#     numbers.append(int(input('No: ')))
# print(numbers)
# result = add(numbers)
# print("Sum:", result)


#optional
# def add(n1, n2, n3=10):
#     return n1 + n2 + n3
# num1 = int(input("enter a num:"))
# num2 = int(input("enter a num:"))
# print(add(num1,num2))
# print(add(num1, num2, n3=100))


#lambda

# num1 = int(input("enter a num:"))
# num2 = int(input("enter another num:"))
# add = lambda n1, n2 : n1+n2
# print(add(num1,num2))


numbers = [1,2,3,4,5]
sq = lambda nums : [num*num for num in nums if num%2==0]
print(tuple(sq(numbers)))
print(sq(numbers))







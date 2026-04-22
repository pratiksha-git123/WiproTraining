
#nat nos print

# num = int(input("Enter a number:"))
# value = 1
# while value <= num:
#     print(value)
#     value = value + 1

#armstrong num
num = int(input("Enter a number: "))
count = len(str(num))

sum = 0
n1 = num
comp = num

while n1 > 0:
    rem = n1 % 10
    sum = sum + rem ** count
    n1 = n1 // 10
if comp == sum:
    print("Armstrong")
else:
    print("NA")


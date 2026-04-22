#for loop
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1,num+1):
#     sum = sum + i**2
#     print(sum)

#print *
# num = int(input("Enter how many *: "))
# for i in range(1, num+1):
#     print("*")

#print * in same line
# num = int(input("Enter how many *: "))
# for _ in range(1, num+1):
#     print("*",sep=" ",end="\t")


num = int(input("Enter how many *: "))
for _ in range(1, num+1):
    print("*","#",sep="$$",end="---")
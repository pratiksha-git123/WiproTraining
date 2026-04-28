from oops_concept.calc import Calc

calc = Calc()
print(Calc.add(a=10, b=5))
print(Calc.sub(a=10, b=5))
print(Calc.mul(a=10, b=5))
numbers = [10, 20, 30]
count = len(numbers)
print(f'length: {count}')

try:
    res = calc.fdiv(10,0)
    for i in range(count+1):
        print(numbers[i])
except IndexError:
    print("Check the index")
except ZeroDivisionError:
    print("Zero is in denominator")
else:
    print(res)
finally:
    print("Done")

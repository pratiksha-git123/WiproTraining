def add(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Both inputs must be numbers")
print(add(10,5))
print(add(10,"hii"))
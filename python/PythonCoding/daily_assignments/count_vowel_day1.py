s = input("Enter your text: ").lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(" Total vowels count: ", count)

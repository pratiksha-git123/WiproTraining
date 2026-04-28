import re

# txt = input("Enter a text: ")
#
# bpat = input("Enter the pattern: ")
# epat = input("Enter ending pattern: ")
# bpat = '^' + bpat
# epat = epat + '$'
#
# if re.search(pattern=bpat, string=txt):
#     print("Beginning pattern available.")
# else:
#     print("Beginning pattern not available.")
#
# if re.search(pattern=epat, string=txt):
#     print("Ending pattern available.")
# else:
#     print("Ending pattern not available.")

#Digit
# mobno = input("Enter a text: ")
# pat = r"[0-9]"
# if re.search(pattern=pat, string=mobno):
#     print("Only digits.")
# else:
#     print("Contains other character also.")

#username
# un = input("Enter Username: ")
# pat = r"[a-z_]{8}$"
# if re.match(pattern=pat, string=un):
#     print("Valid")
# else:
#     print("Invalid")


#email
# emailadd = input("Email: ")
# pat = r"[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
# if re.match(pattern=pat, string=emailadd):
#     print("Valid")
# else:
#      print("Invalid")

#password
# pwdtxt = input("Enter Password: ")
# pat = r"^(?=.*[A-Z])(?.*=[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
# if re.match(pattern=pat, string=pwdtxt):
#      print("Valid")
# else:
#       print("Invalid")


#substitute
txt = input("Enter a text: ")
pat = r"\s+"
# print(re.split(pattern=pat, string=txt))
print(re.sub(pattern=pat, string=txt, repl=" "))
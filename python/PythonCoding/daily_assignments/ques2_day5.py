# from multiprocessing.pool import worker
from daily_assignments.ques1_day5 import content
with open("Output.txt", "r")as f:
    content = f.read()
line = content.split("\n")
words = content.split()
characters = len(content)
print("Number of lines: ", len(line))
print("Number of words: ", len(words))
print("Number of characters: ", characters)

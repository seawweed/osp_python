import sys
from collections import Counter

program_name = sys.argv[0]
n = sys.argv[2]
text = ""
f = open(sys.argv[1], "rt")
dic = {}
text = f.readline()
while text:
    print(text)
    text = f.readline()

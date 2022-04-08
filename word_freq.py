import sys

program_name = sys.argv[0]
n = sys.argv[2]
text = ""
counts = []
f = open(sys.argv[1], "rt")
dic = dict()
text = f.readline()
while text:
    for c in text:
        if c.isalpha() == False:
            continue
        c = c.lower()
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    text = f.readline()
counts = list(dic.values())
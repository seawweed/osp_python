import sys

program_name = sys.argv[0]
n = sys.argv[2]
text = ""

f = open(sys.argv[1], "rt")
dic = dict()
dic2 = dict()
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
words = list(dic.keys())
counts = list(dic.values())
print(words)
print(counts)
for i in range(len(words)):
    dic2[counts[i]] = words[i]

print(dic2)
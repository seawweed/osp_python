import sys

program_name = sys.argv[0]
n = sys.argv[2]
text = ""

f = open(sys.argv[1], "rt")
dic = dict()
dic2 = dict()
text = f.readline()
line = []
while text:
    line = list(text.split())
    for c in line:
        c = c.lower()
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    text = f.readline()
words = list(dic.keys())
counts = list(dic.values())

for i in range(len(words)):
    dic2[counts[i]] = words[i]

counts.sort(reverse=True)
for i in range(int(n)):
    print("%-7s%7d" %(dic2[counts[i]], counts[i]))
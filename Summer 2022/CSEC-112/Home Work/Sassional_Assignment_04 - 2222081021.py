# TASK-1: 71A "Way Too Long Words" problem in codeforces
print("""TASK-1: 71A "WAY TOO LONG WORDS" PROBLEM IN CODEFORCES
===============================================================================""")

n = int(input())
w_list = []
for x in range(n):
  a = input()
  w_list.append(a)

for x in w_list:
  if len(x) <= 10: print(x)
  elif len(x) >= 11: print(x[0], (len(x) - 2), x[-1], sep="")

# TASK-2: 231A "Team" problem in codeforces
print("""\n\nTASK-2: 231A "TEAM" PROBLEM IN CODEFORCES
===============================================================================""")

n = int(input())
a = []
for x in range(n):
    b = input().split()
    b = [int(i) for i in b]
    a.append(b)

c = [a[i][0] + a[i][1] + a[i][2] for i in range(len(a))]

count = 0
for y in c:
    if y >= 2:
        count += 1
print(count)

# TASK-3: 4A "Watermelon" problem in codeforces
print("""\n\nTASK-3: 4A "WATERMELON" PROBLEM IN CODEFORCES
===============================================================================""")

n = int(input())

a = [sorted([i, n-i]) for i in range(1, n) if i % 2 == 0 and (n-i) % 2 == 0]
b = []
[b.append(i) for i in a if i not in b]

if len(b) >= 1:
    print("YES")
else:
    print("NO")

# TASK-4: 158B "Taxi" Problem in Codeforces
print("""\n\nTASK-4: 158B "TEXI" PROBLEM IN CODEFORCES
===============================================================================""")

from math import ceil

n = int(input())
s = input().split()
s = [int(i) for i in s]

g_1, g_2, g_3, g_4 = [], [], [], []
for i in s:
    if i == 1: g_1.append(i)
    elif i == 2: g_2.append(i)
    elif i == 3: g_3.append(i)
    elif i == 4: g_4.append(i)

count_g = len(g_4) + len(g_2)/2

for i in range(2):
    if len(g_2) % 2 != 0 and len(g_1) >= 1:
        count_g += 0.25
        g_1.pop(0)
for i in range(len(g_3)):
    if len(g_3) >= 1 and len(g_1) >= 1:
        count_g += 1
        g_3.pop(0)
        g_1.pop(0)
for i in range(len(g_1)):
    if len(g_1) >= 4:
        count_g += 1
        [g_1.pop(0) for i in range(4)]
if len(g_1) >= 1:
    count_g += 1
if len(g_3) >= 1:
    for i in g_3:
        count_g += 1

print(ceil(count_g))

print("""\n\n===============================================================================
===============================================================================""")
input("Press enter to exit: ")
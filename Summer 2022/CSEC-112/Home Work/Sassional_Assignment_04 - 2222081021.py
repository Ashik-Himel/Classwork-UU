# TASK-1: Letter count in a word.
print("""TASK-1: LETTER COUNT IN A WORD
===============================================================================""")

word = input("Write a word: ")

count = 0
for x in word: count += 1

if count <= 10: print(word)
elif count == 11: print(word[0], count - 1)
elif count > 11: print(word[0], count - 2, word[-1])

# TASK-2: Count problem solving ability in a group.
print("""\n\nTASK-2: COUNT PROBLEM SOLVING ABILITY IN A GROUP
===============================================================================""")

n = int(input("Enter the number of problems: "))
a = []
for x in range(n):
    a.append([])
    a[x].append(int(input("Enter 1st candidate's ability: ")))
    a[x].append(int(input("Enter 2nd candidate's ability: ")))
    a[x].append(int(input("Enter 3rd candidate's ability: ")))

b = [a[i][0] + a[i][1] + a[i][2] for i in range(len(a))]

count = 0
for y in b:
    if y >= 2:
        count += 1
print(count)

# TASK-3: How many even pairs creatable from a number
print("""\n\nTASK-3: HOW MANY EVEN PAIRS CREATABLE FROM A NUMBER
===============================================================================""")

n = int(input("Enter a number: "))

if n % 2 != 0 or n < 6:
    print("Not possible by this number.")
else:
    a = [sorted([i, n - i]) for i in range(2, n, 2)]
    b = []
    [b.append(i) for i in  a if i not in b]
    print(len(b))

# TASK-4: "Taxi" Problem in Codeforces
print("""\n\nTASK-4: "TEXI" PROBLEM IN CODEFORCES
===============================================================================""")

from math import ceil

n = int(input("Enter the number of groups: "))
s = input("Enter group member numbers of each group using space: ").split()
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
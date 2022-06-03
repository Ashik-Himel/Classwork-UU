# TASK-1: Find the given number is even or odd.
print("""TASK-1: FIND THE GIVEN NUMBER IS EVEN OR ODD
===============================================================================""")

number = int(input("Enter an integer number: "))
if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")

# TASK-2: Find if the last 2 digit of given number is divisible by 3 or not.
print("""\n\nTASK-2: FIND IF THE LAST 2 DIGIT OF GIVEN NUMBER IS DIVISIBLE BY 3 OR NOT
===============================================================================""")

number = int(input("Enter an integer number: "))
x = number % 100
if x % 3 == 0:
    print(f"Yes! Last 2 digit of {number} is divisible by 3.")
else:
    print(f"No! Last 2 digit of {number} is not divisible by 3.")

print("""\n\n===============================================================================
===============================================================================""")
input("Press enter to exit: ")
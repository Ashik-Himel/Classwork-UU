# Task-1: Print About YourSelf.
print("""TASK-1: PRINT ABOUT YOURSELF
===============================================================================""")
name = input("Enter your name: ")
id_no = input("Enter your id number: ")
section = input("Enter your section number: ")
batch = input("Enter your batch number: ")
cr_name = input("Enter CR name of your class: ")

print(f"""\nHello {name},
Your ID No. is {id_no}. Welcome to section {section} and batch {batch}.
Talk to your CR {cr_name}, about any class issues. Thank you!""")

print("""\n\n===============================================================================
===============================================================================""")
input("Press enter to exit: ")
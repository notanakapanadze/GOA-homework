# task 1
#task2
def hello_world():
    print("Hello, World!")
hello_world()

#task3
def even_or_odd(number):
    if number % 2 != 0:
        return "კი არის კენტი"
    else:
        return "არ არის კენტი"


print(even_or_odd(23))
print(even_or_odd(44))

#task4
def print_patterns():
    for _ in range(120):
        # FIRST
        print("******")
        print("******")
        print("******")
        
        # SECOND
        print("     *")
        print("    ***")
        print("  *******")
        print("***********")
        print("     *")
        print("     *")
        
        # THIRD
        print("*******")
        print(" *******")
        print("  ********")
        print("    ********")

print_patterns()

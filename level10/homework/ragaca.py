# task 1
age = int(input("How old are you? "))

for i in range(1, age + 1):
    print("Iteration", i)

# task 2 
# Ask for the temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the result
print(f"The temperature in Fahrenheit is: {fahrenheit}")


#task 3
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print(5 == 5)  # True
print(5 != 3)  # True
print(10 > 3)  # True


#task 4
# Use a for loop to create a triangle
for i in range(1, 6):  # Adjust the range for the size of the triangle
    print("<3 " * i)

#task 5 
# Ask for the user's age
age = int(input("How old are you? "))

# Check if the user is 20 years old
if age == 20:
    print(True)
else:
    print(False)

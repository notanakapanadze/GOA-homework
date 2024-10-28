# task 1
name = input("What is your name? ")
result = ""

for letter in name:
    result += letter + " "

result = result.strip()

print(result)

# task 2

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))


for number in range(start, end + 1):
   
    if number % 2 == 0 and number % 3 == 0:
        print("These numbers are multiples of 3 and 2")
    else:
        print("This number is unique <3")

# task 3
result = 0

for i in range(5):
    number = int(input("Enter a number: "))
    result += number

mean = result / 5

print("The total sum is:", result)
print("The arithmetic mean is:", mean)


#task 4

for number in range(-100, 101):
   
    if number > 0:
        print(number)




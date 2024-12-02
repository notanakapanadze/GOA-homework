#task 1
def custom_split(string, delimiter=" "):
    result = []
    temp = ""
    for char in string:
        if char == delimiter:
            result.append(temp)
            temp = ""
        else:
            temp += char
    if temp:  # ბოლო ნაწილი დავამატოთ
        result.append(temp)
    return result

print(custom_split("Hello world, this is Python", " "))

#task2
def custom_join(delimiter, items):
    result = ""
    for i, item in enumerate(items):
        result += item
        if i < len(items) - 1:  # არ დავამატოთ საბოლოო ელემენტზე
            result += delimiter
    return result

print(custom_join(", ", ["Hello", "world", "Python"]))

#task3
def custom_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result

print(custom_replace("hello world", "world", "Python"))

#task4
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "/"))

#task 5
words = []
count = int(input("How many words do you want to add? "))

for _ in range(count):
    word = input("Enter a word: ")
    words.append(word)

joined = " ".join(words)  # array-ს დავაჯოინოთ
print("Array:", words)
print("Joined:", joined)

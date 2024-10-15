# 1) (1, 50 , 2) დარინტეთ რაც გინდათ! while/for
for i in range(1, 51, 2):
    print(i)

i = 1
while i <= 50:
    print(i)
    i += 2

# 2) კვადრატი დავხაზოთ "*",  for/while
size = 5 
for i in range(size):
    print("* " * size)


    size = 5
i = 0
while i < size:
    print("* " * size)
    i += 1


# 3) მართკუთხედი დავხაზე "*", for/while

width = 6
height = 4
for i in range(height):
    print("* " * width)

width = 6
height = 4
i = 0
while i < height:
    print("* " * width)
    i += 1

# 4) for loop ( საიტერაციო ცვლადს დაარქვით num1 ) გამოვიყენოთ და შიგნით ჩავაშენოთ(შიგნიშთ კიდევ შევქმანთ) for loop (საიტერაციო ცვლადს დაარქვით num)  და დაპრიმტეთ მეორე ლუპში ორივე, საიტერაციო ცვლადის მნიშნვნელობა
for num1 in range(3):
    for num in range(4): 
        print(num1, num)

# 5) difculty porject ( შექმნით, სარეგისტრაციო ფორმა ჩვენი, სოციალური ქსელისთვის <3 input, while, loop )
# Simple registration form for a social network
print("Welcome to Our Social Network!")

while True:
    print("\nPlease fill out the registration form:")


    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

   
    if len(name) < 2:
        print("Name must be at least 2 characters.")
       
    if "@" not in email or "." not in email:
        print("Invalid email format.")

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
       

   
    print("Thank you, for registering!")
    print("Registration complete. Goodbye!")


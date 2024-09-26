#first task
age=input("enter the year of your birth")
print(2024-int(age))

#second task
length=input("enter the length")
width=input("enter the width")

#area
print(int(length)*int(width))

#perimeter
print((int(length)+int(width))*2)

#third task
distance=input("enter the distance from your school to your house in km-s")

#km
print(distance)
#meters
print(float(distance)*1000)
#cm
print(float(distance)*100000)
#mm
print(float(distance)*1000000)


#fourth task
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
parents_last_name = input("Enter your parent's last name: ")
favorite_color = input("Enter your favorite color: ")
favorite_animal = input("Enter your favorite animal: ")


hobby1 = input("Enter your first favorite hobby: ")
hobby2 = input("Enter your second favorite hobby: ")
hobby3 = input("Enter your third favorite hobby: ")

#print everything in one sentence
sentence = ("Your name is " + first_name + " " + last_name + ", your parent's last name is " + parents_last_name +
            ". Your favorite color is " + favorite_color + " and your favorite animal is " + favorite_animal + 
            ". You enjoy " + hobby1 + ", " + hobby2 + ", and " + hobby3 + " as your hobbies.")
print(sentence)

#fifth task
number = int(input("Enter a two-digit number: "))

ateuli = number // 10
erteuli = number % 10

sum = ateuli + erteuli

# Print the result
print(sum)

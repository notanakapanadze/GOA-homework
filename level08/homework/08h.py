# nummber 1
#ask the user for their age
age = int(input("Enter your age: "))

# Check if age is between 13 and 19
if age > 13 and age < 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")

#nummber 2
# Ask Nugzari for his math test score
score = float(input("Enter your math test score (1-10): "))

is_A = score >= 9
is_B = score >= 8 and score < 9
is_C = score >= 7 and score < 8
is_D = score >= 6 and score < 7
is_F = score < 6

# Print the results
print("is_A:", is_A)
print("is_B:", is_B)
print("is_C:", is_C)
print("is_D:", is_D)
print("is_F:", is_F)

#  nummber 3
# Create two variables
var1 = True
var2 = False

print("var1 AND var2:", var1 and var2)
print("var1 OR var2:", var1 or var2)
print("NOT var1:", not var1)
print("NOT var2:", not var2)
print("var1 XOR var2:", var1 != var2)


#nummber 4
# Ask the user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the two numbers
print("num1 == num2:", num1 == num2)
print("num1 < num2:", num1 < num2)
print("num1 > num2:", num1 > num2)
print("num1 <= num2:", num1 <= num2)
print("num1 >= num2:", num1 >= num2)
print("num1 != num2:", num1 != num2)

#nummber 5
# Assign values to a, b, and c
a = 5
b = 3
c = 7

# find out which is the biggest, middle, and smallest
is_a_biggest = a > b and a > c
is_b_middle = (b > a and b < c) or (b < a and b > c)
is_c_smallest = c < a and c < b

# Print the results
print("is_a_biggest:", is_a_biggest)
print("is_b_middle:", is_b_middle)
print("is_c_smallest:", is_c_smallest)

#nummber 6
# Assign a score (0-100)
score = 88

is_pass = score >= 50
is_high_pass = 75 <= score < 90
is_perfect = score == 100
is_failing = score < 50

# Print the results
print("is_pass:", is_pass)
print("is_high_pass:", is_high_pass)
print("is_perfect:", is_perfect)
print("is_failing:", is_failing)


#nummber 7
# Assign True or False to P and Q
P = True
Q = False


P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = P != Q

# Print the results
print("P_and_not_Q:", P_and_not_Q)
print("not_P_and_Q:", not_P_and_Q)
print("P_xor_Q:", P_xor_Q)

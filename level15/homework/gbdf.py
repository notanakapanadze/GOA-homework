# task 1
number = int(input("enter a nummber: "))
if number < 10:
    print("the nummber is smaller then 10")
else:
    print("the nummber is ten or bigger")

# task 2
number = int(input("შეიტანეთ რიცხვი: "))
if number % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი ლუწი არ არის.")

#task 3

number = int(input("შეიტანეთ რიცხვი: "))
if number > 0:
    print("რიცხვი დადებითია.")
else:
    print("რიცხვი არ არის დადებითი.")

#task 4
number1 = int(input("შეიტანეთ პირველი რიცხვი: "))
number2 = int(input("შეიტანეთ მეორე რიცხვი: "))

if number1 == number2:
    print("რიცხვები ტოლია.")
else:
    print("რიცხვები არ არის ტოლი.")

#task 5
number = int(input("შეიტანეთ რიცხვი: "))
if number > 100 and number % 2 == 0:
    print("რიცხვი 100-ზე მეტია და ლუწია.")
else:
    print("რიცხვი 100-ზე არაა მეტი ან არ არის ლუწი.")

#task 5
number = int(input("შეიტანეთ რიცხვი: "))
if number % 5 == 0 or number % 10 == 0:
    print("რიცხვი 5-ის ან 10-ის ჯერადია.")
else:
    print("რიცხვი არც 5-ის და არც 10-ის ჯერადი არ არის.")


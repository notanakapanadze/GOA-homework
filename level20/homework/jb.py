letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']
vowels = ['ა', 'ე', 'ი', 'ო', 'უ']
count_vowels = len([letter for letter in letters if letter in vowels])
print("ხმოვნების რაოდენობაა:", count_vowels)

multiples = [num for num in range(1, 101) if num % 5 == 0 or num % 3 == 0]
print("5-ის ან 3-ის ჯერადები:", multiples)

elements = ['ა', 'ბ', 'გ', 1, 2, 3, 'დ', 'ე', 4, 5, 'ვ']
combined_string = ''.join(str(el) for el in elements)
print("სტრინგად გარდაქმნილი ელემენტები:", combined_string)

rows = 4
for i in range(rows):
    print(' ' * i + '*' * 6)

age = int(input("რამდენი წლის ხარ? "))
if age > 12:
    print("შენ არ ხარ 12 წლის")


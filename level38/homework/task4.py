database = [] 

def AddToDatabase(first_name, last_name, age):
    entry = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }
    database.append(entry) 
    print("Current Database:", database)


AddToDatabase('Nugzari', 'Giorgadze', 30)
AddToDatabase('Anna', 'Smith', 25)

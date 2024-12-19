def high_and_low(numbers):
    num_list = numbers.split()
   
    int_list = []
    for num in num_list:
        int_list.append(int(num))
    
    highest = max(int_list)
    lowest = min(int_list)


    result = str(highest) + " " + str(lowest)
    
    return result



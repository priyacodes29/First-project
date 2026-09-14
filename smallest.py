def show_number(numbers): 
    smallest = numbers[0]
    for number in numbers: 
        if number < smallest: 
            smallest = number 
        return smallest 
    my_list = [5,2,9,1,7]
    print(show_number(my_list))
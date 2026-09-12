
def show_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

my_list = [5,2,9,7,1]
print(show_smallest(my_list))
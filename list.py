def number():
    number_list = list(map(int, input("Enter numbers separated by space: ").split()))
    add = 0
    for i in number_list: 
        add = add + i
    return add
print(number())
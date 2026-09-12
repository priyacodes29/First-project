def numbers():
 numbers_list = list(map(int,input("enter the number").split()))
 add = 0
 for number in numbers_list: 
   add = add + number 
 return add

print(numbers())

import random

user1 = "priya"
user1 = int(input("entert the number "))

if 1 <= user1 <= 10:
        print("valid number")
    else:
        print("Invalid number")

user2 ="Riya"
user2 = int(input("enter the number: "))

if 1 <= user2 <= 10:
        print("valid number")
    else:
        print("Invalid number")


random_number = random.randint(1, 10)

print("Random number:", random_number)

answer1 = user1 * random_number
answer2 = user2 * random_number

print("User 1:", answer1)
print("User 2 :", answer2)



if answer1 == answer2:
    print("pass")
else:
    print("fail")
import random


user1 = int(input("User 1, 1 se 10 ke beech number enter karo: "))

if 1 <= user1 <= 10:
        print("valid number")
else:
        print("Invalid number")



user2 = int(input("User 2, 1 se 10 ke beech number enter karo: "))

if 1 <= user2 <= 10:
        print("valid number")
else:
        print("Invalid number")




random_number = random.randint(1, 10)

print("Random number:", random_number)



answer1 = user1 * random_number
answer2 = user2 * random_number

print("User 1 :", answer1)
print("User 2 :", answer2)



if answer1 == answer2:
    print("Aap jeet gaye!")
else:
    print("Aap haar gaye!")
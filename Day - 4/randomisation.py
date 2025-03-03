# Randomisation

import random


# random_int = random.randint(1,10)
# random_number = round(random.random() * 10, 2)
# random_float = random.uniform(1, 10)
#
# # This return number the range of 1 to 10
#
# # A module in python is basically the splitting of large code base into smaller files to enhance collaboration
#
# print(random_int)
# print(random_number)
# print(random_float)


# random_head_or_tail = random.randint(1, 2)
#
# if random_head_or_tail == 1:
#     print("Head!")
# else:
#     print("Tail!")
#




friends = ["Alice", "Bob", "Elsa", "Jake", "Moana"]


#1
randomNum = random.randint(0,len(friends)-1)
print(friends[randomNum])

#2
print(random.choice(friends))
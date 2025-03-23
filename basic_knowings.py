#  Copying a List
#  So how do you create a similar list without altering the original? You copy it! Let’s see
# how:
from curses.ascii import isalpha
from logging import raiseExceptions

# using [:] to copy a list
data = [5, 10, 15, 20]
data_copy = data[ : ]
# a single colon copies the list
data[0] = 50
# print( "data: { }\t data_copy: { }".format(data, data_copy) )

print(f"data:{data}\t data_copy: {data_copy}")



# breaking out of a loop using the 'break' keyword
for num in range(5):
    if num == 3:
        # raise Exception("Yeah bro the number is 3! and it sucks! so no three!")
        break
    print(num)




# using pop to remove items and saving to a variable to use later
items = [5, "ball", True]
items.pop( )
# by default removes the last item
removed_item = items.pop(0)
# removes 5 and saves it into the variable
print(removed_item, "\n", items)



# sorted( )
#  The sorted function will work on either numerical or alphabetical lists, but not one that is
# mixed. Sorted also returns a copy of the list, so it doesn’t alter the original. Usually if you
# need to keep the original intact, be sure to use this function:
nums = [5, 8, 0, 2]
sorted_nums = sorted(nums)
print(f"This the sorted nums: {sorted_nums}\nWhiles this is original form which is not altered: {nums}")


# .sort( )
#  The sort method is used for the same purpose that our previous sorted function is used
# for; however, it will change the original list directly:
nums_2 = [5, 8, 0, 2]
nums_2.sort() #This alters the original form
print(f"This is original form which is altered: {nums_2}")



 # using conditional statements on a list
names = [ "Jack", "Robert", "Mary" ]
if "Mary" in names:
    print("found")
# will run since Mary is in the list
if "Jimmy" not in names:
    print("not found")
# will run since Jimmy is not in the list



# Output Names: Write a loop that will iterate over a list of items
# and only output items which have letters inside of a string. Take
# the following list, for example, only “John” and “Amanda” should
# be output:
# names_2 = ['John', '  ', 'Amanda', 5]
# for name in names_2:
#     if isalpha(name):
#         print(name)


name = "godi"
print(type(name))
print(isalpha(name))




# shopping list
print("Welcome to Shopping List Captain")

# show list
## use of copy()
shop_list =["Mango", "potato", "flour", "cookies", "T-shirt"]
print("Here is your Shopping List: ", shop_list)
shoplist_ = shop_list.copy()

# add item
## use of append() & insert()
new_item = input("would you like to add something in it?(Yes/No) ")

if new_item == ("No" or "no"):
    print("Okay!")

elif new_item == ("Yes" or "yes"):
    function = int(input("on which serial no do you want to add: "))
    
    if function <= 5:
        shop_list.insert(function, item)
    else:
        item = input("which item do you want to add: ")
        shop_list.append(item)

else:
    print("Sorry! It seems you did some mistake, no problem let's continue")


# remove item
# use of pop() & remove()
remo_item = input("Would you like to remove item from shopping list?(Yes/No) ")

if remo_item == ("No" or "no"):
    print("Alright!")

elif remo_item == ("Yes" or "yes"):
    function = int(input("of which serial no of item do you want to remove: "))
    
    if function <= 5:
        shop_list.pop(function)
    else:
        item = input("Sorry! which item do you want to remove? write name: ")
        shop_list.remove(item)
else:
    print("Sorry! It seems you did some mistake, no problem let's continue")
        
# check list
check = input("do you want to check you current list(Yes/No) ")


if check == ("No" or "no"):
    print("No Problem!")

else: #we dont use yes condition here, for by default action
    print(shop_list)


# use of index(), sort(), copy(), reverse(), 

# use of index
ind = input("which index do you want to check(String): ")
print(shop_list.index(ind))

# List indexing
int_ind = int(input("which index do you want to check(Integer): "))
print(shop_list[int_ind])



# use of sort & slicing
pattern = input("would you like to see list in Sort?(type 'Skip' if you not) ")
if pattern == 'Skip':
    print("okay we will move forword")
else:
    shop_list.sort()
    print("Here is List in Sort", shop_list)
## we can use also sorted
# List slicing in Python
print("slicing - ", shop_list[2:5])

# earlier we use copy, here it work
pattern = input("would you like see to previous list?(type 'Skip' if you not)")
if pattern == 'Skip':
    print("okay we will move forword")
else:
    print("here is your previous List ", shoplist_)

# use of reverse
pattern = input("would you like to list in reverse?(type 'Skip' if you not) ")
if pattern == 'Skip':
    print("okay we will move forword")
else:
    shop_list.reverse()
    print("here is your list in reverse form ", shop_list)

# use of clear
now = input("should I remove your previous list(Yes/No): ")

if now == ("No" or "no"):
    print("No Problem!")

elif now == ("Yes" or "yes"):
    shoplist_.clear()
    print("your previous list is removed ", shoplist_)

else:
    print("please choose the correct option")


# Expending
## use of expend()

new_i = input("write your new item list ")
new_i = new_i.split()

for it in new_i:
    y = 5
    if y > 0:
        print(it, end=" ")
    del y
    
shop_list.extend(new_i)
print(shop_list)

###these are some use of list methods###

feedback_ =input("Please share you feedback ")
print("Thank You! Hope you Enjoy I'm Practing soon will improve. Bye!Bye! Have a Nice Day")




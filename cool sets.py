#set

year_set = {2000, 2001, 2002, 2003}
print(year_set)

# check type 
print(type(year_set))

# To add an element
year_set.add(2005)
print(year_set)

# To add multiple elements

year_set.update([2006, 2007])
print(year_set)

# To add list and set

year_set.update([2009, 2010], {2011, 2012, 2013, 2014})
print(year_set)

# use of discard() & remove()

year_set.discard(2013)
year_set.remove(2014)

print(year_set)

# to pop an element

year_set.pop()
print(year_set)


## leap year
leapyr_set = {2000, 2004, 2008, 2012}


# use union() for all items, both side
allyr_set = year_set.union(leapyr_set)
print(allyr_set)

# for dublicate
year_set.intersection_update(leapyr_set)
print(year_set)

# for no dublicate
year_set.symmetric_difference_update(leapyr_set)
print(year_set)

## To clear sets

print(year_set.clear())

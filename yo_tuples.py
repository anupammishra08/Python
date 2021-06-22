# Accessing tuple elements using indexing
yo_tuple = ('A','n','u','p','a','m')

print(yo_tuple[0])   
print(yo_tuple[5])   



# nested tuple
n_tuple = ("Anupam", [0, 8], [1, 1], (1, 9, 9, 7))

# nested index
print(n_tuple[0][3])       
print(n_tuple[1][1])

# Negative indexing for accessing tuple elements
print(yo_tuple[-6])


# Accessing tuple elements using slicing

print(yo_tuple[1:4])

## elements beginning to 2nd

print(yo_tuple[:-7])

# Changing tuple values
hi_tuple = (4, 2, 3, [6, 5])


# item of mutable element can be changed
hi_tuple[3][0] = 9    
print(hi_tuple)

# Can delete an entire tuple
del hi_tuple



#use of count() & index()

print(yo_tuple.count('p'))  
print(yo_tuple.index('u'))


# In operation
print('a' in yo_tuple)
print('p' in yo_tuple)

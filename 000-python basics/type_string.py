quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'


# A GOOD PROGRAMMER IS SOMEONE WHO ALWAYS LOOKS BOTH WAYS BEFORE CROSSING A ONE-WAY STREET
print(quote.upper())

# a good programmer is someone who always looks both ways before crossing a one-way street
print(quote.lower())


# True
print(quote.endswith('street'))


# False
print(quote.isupper())
# True
print(quote.upper().isupper())


# 25
print(quote.find('one'))
# A good programmer is some1 who always looks both ways before crossing a 1-way street
# ...is some1 who...
print(quote.replace('one','1'))
# A good programmer is some1 who always looks 2 ways before crossing a 1-way street
print(quote.replace('one','1').replace('both','2'))


# ['A', 'good', 'programmer', 'is', 'someone', 'who', 'always', 'looks', 'both', 'ways', 'before', 'crossing', 'a', 'one-way', 'street']
print(quote.split(' '))


# False
print(quote.isdigit())
# False
print(quote.isdecimal())
# False
print(quote.isalpha())
# False
print(quote.isalnum())
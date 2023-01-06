# repeat the same text several times
# first way
print('My text')
print('My text')
print('My text')
print('\n')

# second way - we can use """ text """ or ''' text '''
print('''My text
My text
My text''')
print()

# third way
print("My text \nMy text \nMy text\n")

# fourth way
print("My text\n"*3)

message = "This is test message"
message_2 = "Second message"
print(f"Show message: {message}. Next message: {message_2}")

print("Hello", "Jenny")
# but 
print("Hello"+"Jenny")
# extended case 1
print("Hello" "Jenny" "Margaret")
# but 
print("Hello", "Jenny", "Margaret")
print()

# format stings
# 1.
value_1 = 'example 1'
value_2 = 'example 2'
value_3 = 'example 3'

result = "Value 1 is: %s value 2 is %s value 3 is %s"%(value_1, value_2, value_3)

print(result)
#2
result = "This is example no 1: {}, example no 2: {}, example no 3: {}".format(value_1, value_2, value_3)
print(result)
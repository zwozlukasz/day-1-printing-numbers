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
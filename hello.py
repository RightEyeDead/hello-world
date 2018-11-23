# This program say "Hello world" and aks me for my name and age.

print('Hello world!')
print('What is your name?') # asks the user for their name
myName = input()
print('Nice to meet you ' + myName)
print('Your name has ' + str(len(myName)) + ' characters')
print('What is your age?') # asks the user for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

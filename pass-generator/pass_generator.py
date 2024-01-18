import random

print('Welcome to the password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){\}[],./'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Character length of password: ')
length = input(length)

print('\nHere are your passwords:')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
# try guessing a num
import random
print("welcome to number guess game")
# “Random Integer”
secret_num=random.randint(1,15)
print("Choose a number between 1 to 15")
print("you have only three choices ")
print("BEST OF LUCK")
for i in range(3):
# while user_guess!=secret_num:
      user_guess=int(input("your guess number is : "))
      if user_guess == secret_num:
         print("your guess is right")
      elif user_guess > secret_num:
         print("too high guess")
      elif user_guess < secret_num:
         print(" too low ")
      else:
          print("you lost all your turn to guess it ... ")
print("the secret number is :",secret_num)
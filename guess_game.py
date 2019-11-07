#python 3.7.1

#Alireza Tavakoli

guess_word       =  "Ya Ali"
guess            =   ""

guess_count      =    0
guess_limit      =    8

out_of_guesses   =    False

while guess_word != guess and not (out_of_guesses):
  if guess_count < guess_limit:
    guess   =  input("Please, Enter Guess: ")
    guess_count  +=  1
  else : 
    out_of_guesses   =  True
    
if out_of_guesses :
  print ("You lose.")

else : 
  print ("You win!")
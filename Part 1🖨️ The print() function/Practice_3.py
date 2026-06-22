#6. Print a box like this using * and \n:
 #  **********
  # *        *
  # **********

print("**********\n*        *\n**********")
print("*" * 10 + "\n" + "*" + " " * 8 + "*" + "\n" + "*" * 10)

"""
How it works
"*" * 10

gives:
**********

and
" " * 8

gives 8 spaces:
Then we join everything together with "\n".
"""


#7. Print your full name, city, age all on same line
 #  separated by " | " using sep
 
print("Satyam Pandey","Atarra","age = 20", sep=("|"))
# sep = what goes BETWEEN items (default is space)
print("a","b","c")               # a b c
print("a","b","c", sep="")       # abc
print("a","b","c", sep="-")      # a-b-c
print("a","b","c", sep=", ")     # a, b, c


# end = what goes at END of print (default is new line)
print("Hello", end=" ")
print("World")                     # Hello World  (same line!)

print("Hello", end="!!!\n")        # Hello!!!
print("Satyam, ", end="")
print("How are you??")


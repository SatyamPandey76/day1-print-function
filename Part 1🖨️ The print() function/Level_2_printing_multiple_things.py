# Method 1: comma separated (adds space automatically)
print("My age is", 20)    # My age is 20

# Method 2: + operator (no auto space)
print("My age is " + "20")   # My age is 20

# ⚠️ Common Mistake!
print("My age is " + 20)       # ❌ CRASHES! Can't mix text + number
print("My age is " + str(20))  # ✅ Convert number to text first
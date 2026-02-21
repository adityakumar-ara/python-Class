# number = (1,2,3,3,3,4,5,6,7)
# print(number)
# print(number[5])
# print(number)
# print(type(number))
# print(number.count(3))
# print(number.count(1))
# print(number.index(1))
# print(number.index(3))
# print(len(number))

# ----------------Negative indexing tuple-------------------------------------------
  # -9  -8 -7 -6 -5 -4  -3 -2 -1
# n = (1,  2, 3, 4, 5, 6,  7, 8, 9)

# n = (1,2,3,4,5,6,7,8,9)
# print(max(n))
# print(min(n))
# print(sum(n))
# print(n)
# print(n[2])
# print(n[-2])
# slacing = n[0:10:2]
# print(slacing)

# nu = (3,2,1,4,5,6,7,8)
# print(sorted(nu))

# -------------------------------unpacking------------------------------------------
fruits = ("apple", "banana", "cherry")

# Unpacking the tuple into three separate variables
(green, yellow, red) = fruits

print(green)  # Output: apple
print(yellow) # Output: banana
print(red)    # Output: cherry

# ----------------------Advanced Unpacking: The Asterisk * (Star) Operator---------------------------
grades = (100, 90, 85, 88, 72)

(highest, *middle, lowest) = grades

print(highest) # Output: 100
print(middle)  # Output: [90, 85, 88]
print(lowest)  # Output: 72
## 07) WAP to do String slicing

#  a)	Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
 
#  b)	Right (Or clockwise) rotate the given string by d elements (where d <= n).

name = "chirag"

count = 1

left_rotated = name[count:] + name[:count]
print(f"Left Rotated String: {left_rotated}")

right_rotated = name[-count:] + name[:-count]
print(f"Right Rotated String: {right_rotated}")

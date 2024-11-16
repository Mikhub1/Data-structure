#Write a Python program to rotate a Deque Object
#a specified number (positive) of times
#

# Import the collections module to use the deque data structure
import collections

# Declare an empty deque object named 'dq_object'
dq_object = collections.deque()

# Add elements to the deque from left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)

# Print a message to indicate the display of the deque before rotation
print("Deque before rotation:")

# Print the content of 'dq_object'
print(dq_object)

# Rotate the deque once in the positive direction (to the right)
dq_object.rotate()

# Print a message to indicate the display of the deque after 1 positive rotation
print("\nDeque after 1 positive rotation:")

# Print the content of 'dq_object' after one rotation
print(dq_object)

# Rotate the deque twice in the positive direction (to the right)
dq_object.rotate(2)

# Print a message to indicate the display of the deque after 2 positive rotations
print("\nDeque after 2 positive rotations:")

# Print the content of 'dq_object' after two rotations
print(dq_object) 

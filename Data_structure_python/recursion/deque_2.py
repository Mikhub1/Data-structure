#Write a Python program that copies a deque object and verifies shallow copying.

# Import the collections module to use the deque data structure
import collections

# Create a tuple 'tup1' containing numbers 1, 3, 5, 7, and 9
tup1 = (1, 3, 5, 7, 9)

# Create a deque 'dq1' from the 'tup1' tuple
dq1 = collections.deque(tup1)

# Create a shallow copy 'dq2' of 'dq1'
dq2 = dq1.copy()

# Print a message to indicate the display of the content of 'dq1'
print("Content of dq1:")

# Print the content of 'dq1'
print(dq1)

# Print a message indicating the ID of 'dq1'
print("dq2 id:")

# Print the ID of 'dq1'
print(id(dq1))

# Print a message to indicate the display of the content of 'dq2'
print("\nContent of dq2:")

# Print the content of 'dq2'
print(dq2)

# Print a message indicating the ID of 'dq2'
print("dq2 id:")

# Print the ID of 'dq2'
print(id(dq2))

# Print a message to check if the first element of 'dq1' and 'dq2' are shallow copies
print("\nChecking the first element of dq1 and dq2 are shallow copies:")

# Print the ID of the first element of 'dq1'
print(id(dq1[0]))

# Print the ID of the first element of 'dq2'
print(id(dq2[0]))
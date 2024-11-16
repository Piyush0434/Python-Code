import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Perform basic operations
squared = array ** 2  # Square each element
sum_of_elements = np.sum(array)  # Sum of all elements
mean = np.mean(array)  # Mean of the elements

# Print the results
print("Original Array:", array)
print("Squared Array:", squared)
print("Sum of Elements:", sum_of_elements)
print("Mean of Elements:", mean)
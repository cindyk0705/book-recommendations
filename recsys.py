# Cindy Kuang 
# Homework 8 Part 1
# March 27, 2024 
# This function calculates the similarity between two vectors of the same length
# Input: Two vectors (lists of numbers) of the same length 
# Output: The cosine similarity of the inputs

import math

"""
This module contains functions for building 
recommendation systems.
"""

def similarity(vector1, vector2):
    """
    Returns the cosine similarity between two vectors.  The vectors 
    must have the same length.  If either vector is all zeros, then the 
    similarity is defined to be zero.  Vectors are assumed to be lists that
    contain numbers (ints and floats).
    """
    if len(vector1) != len(vector2):
        raise ValueError("vectors must be same length")
    # add your code below

    # compute the dot product of the two vectors
    dot_prod = dot_product(vector1, vector2)

    # if the dot product = 0, return similarity = 0 now to avoid possible division by 0
    if dot_prod == 0: 
        return 0.0

    # calculate the magnitudes of the two vectors
    magnitude1 = magnitude(vector1)
    magnitude2 = magnitude(vector2)
    
    return dot_prod / (magnitude1 * magnitude2) 


# a function to calculate the dot product of two vectors
def dot_product(vector1, vector2):

    dot_product = 0 
    for i in range(len(vector1)):
        dot_product = dot_product + vector1[i] * vector2[i]
    
    return dot_product

# a function to calculate the magnitude of a vector
def magnitude(vector):
    magnitude_squared = 0 
    for i in range(len(vector)):
        magnitude_squared = magnitude_squared + (vector[i] ** 2)
    
    magnitude = math.sqrt(magnitude_squared)

    return magnitude





# Cindy Kuang 
# Homework 8 Part 1
# March 27, 2024 
# This function tests the recsys.py's similarity function 
# Input: None 
# Output: Test results (successful or otherwise) of the listed tests 

import math
from recsys import *

def test_similarity_identical_books():
    """
    This test sends two identical vectors to the recsys.similarity function
    and asserts that the similarity is reported to be 1.0 within a tolerance of
    0.0001.  The test checks many different vectors and lengths of vectors 
    (typical vector lengths of 1 to 3).
    """
    # To be written by student.
    expected = 1.0 
    vector1 = [1, 5, 7]
    vector2 = vector1
    result1 = similarity(vector1, vector2)
    assert math.isclose(expected, result1, rel_tol = 0.0001) == True 

    vector3 = [8, 8]
    vector4 = vector3
    result2 = similarity(vector3, vector4)
    assert math.isclose(expected, result2, rel_tol = 0.0001) == True 

    vector5 = [2]
    vector6 = vector5
    result3 = similarity(vector5, vector6)
    assert math.isclose(expected, result3, rel_tol = 0.0001) == True  


def test_similarity_diff_books():
    """
    This test sends two different vectors to the recsys.similarity function
    and asserts that the similarity is reported to be within a tolerance of
    0.0001 of the hand computed cosine similarity.  The test checks many 
    different vector pairs and lengths of vectors (typical vector lengths of
    1 to 3).
    """
    # To be written by student.

    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    expected1 = 0.974632
    result1 = similarity(vector1, vector2)
    assert math.isclose(result1, expected1, rel_tol = 0.0001) == True 

    vector3 = [2, 6]
    vector4 = [7, -3]
    expected2 = -0.083045
    result2 = similarity(vector3, vector4)
    assert math.isclose(result2, expected2, rel_tol = 0.0001) == True 

    vector5 = [-4]
    vector6 = [-2]
    expected3 = 1.0
    result3 = similarity(vector5, vector6)
    assert math.isclose(result3, expected3, rel_tol = 0.0001) == True 

    

def test_similarity_no_ratings():
    """
    This test sends a vector with all zeros into recsys.similarity and
    verifies that the result is 0.0.
    """
    # To be written by student.

    vector1 = [0, 0, 0]
    expected = 0.0
    result = similarity(vector1, vector1)
    assert result == expected


def main(): 
    test_similarity_diff_books()
    test_similarity_identical_books()
    test_similarity_no_ratings()

main()



# Cindy Kuang 
# Homework 8 Part 2
# March 27, 2024 
# This program reads a list of books and a list of user ratings, and outputs the most similar book
# for each book.
# Input: A file containing 53 titles and a file containing 32 users' ratings for each of the 
# 53 titles. 
# Output: Each book and its most similar book. 
from recsys import *

# Do not change this function.  You must use this function.
def format_similar_message(source_book_title, 
                           most_similar_title, 
                           similarity_score):
    """Function to produce a properly formatted string for output of Problem1."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
    return result

# add your code below

# This procedure reads the books.txt file and store the titles into the titles() list 
# E.g. titles(0) = A Hitchhiker's Guide, due to it being the first title in the file. 
def get_titles(): 
    # set books.txt as the open file 
    title_file = open('books.txt', 'r')

    # create an empty files for titles()
    titles = list()

    # iterate through the file line by line and add each title to titles()
    line = title_file.readline()
    while line != '':
        titles.append(line)
        line = title_file.readline() 

    # close and return titles()
    title_file.close()
    return titles

# This procedure reads through the ratings.txt file and organize them into a 53 x 32 matrix called
# book_ratings. Each of the 53 rows represent a book, and each row contains 32 user ratings for that book.  
# e.g. book_ratings[0][1] = The rating that User 1 gave for A Hitchhiker's guide (since it is book 0)
def get_ratings():

    # open the ratings.txt file 
    ratings_file = open('ratings.txt', 'r')

    NUM_OF_BOOKS = 53
    NUM_OF_RATINGS = 32

    # create a 32 x 52 matrix called user_ratings. Each of the 32 rows represent a user,
    # and each row contain 52 ratings given by that specific user.
    # e.g. user_ratings[0][1] = The rating that user 0 gave to Watership Down (the second book in list)
    user_ratings = list()

    # iterate through the ratings.txt file
    for i in range(NUM_OF_RATINGS): 
        # skip the line containiner the user ID
        ratings_file.readline()
        # populate a list with the 53 book ratings given by the ith user
        ratings = list()
        for j in range(NUM_OF_BOOKS):
                line = float(ratings_file.readline())
                ratings.append(line)
        
        # append each ratings list to the user_ratings list 
        user_ratings.append(ratings)
    
    # create the 52 x 32 book_ratings matrix, and organize the values from user_rating into it.
    # Each of the 53 rows represent a book, and each row contains 32 user ratings for that book.  
    book_ratings = list()
    for i in range(NUM_OF_BOOKS):
        ratings_for_this_book = list()
        for j in range(NUM_OF_RATINGS):
            # Take all the 32 ratings corresponding to the ith book from the user_ratings matrix,
            # populate them into the ratings_for_this_book matrix
            ratings_for_this_book.append(user_ratings[j][i])
        # populate the book_ratings matrix with the 32 ratings_for_this_book matrix
        book_ratings.append(ratings_for_this_book)

    # close file and return the book_ratings matrix 
    ratings_file.close()
    return book_ratings

    # For each book, find its similarity with the 52 other books. Store the title and similarity score
    # of the book most similar to it into a 53 x 2 matrix. 
    # e.g. most_similar_matrix[0][0] = the title of the book most similar to The Hitchhiker's Guide 
    # e.g. most_similar_matrix[0][1] = the similarity score of the book most similar to The Hitchhiker's
    # Guide. 
def find_most_similar(titles, ratings):
    NUM_OF_BOOKS = 53

    # create the empty most_similar_matrix 
    most_similar_matrix = list()
    for i in range(0, NUM_OF_BOOKS):
        # current_book_to_compare_rating = the rating vector of the ith book 
        current_book_to_compare_ratings = ratings[i]

        # start with -1.0 as the highest similarity score and update it whenever a higher similarity 
        # score is found. 
        most_similar_rating = -1.0
        for j in range(0, NUM_OF_BOOKS - 1):
            # find the similarity of the ith book with the 52 other books 
            # the (i - j - 1) ensures that the ith book does not compare its similarity to itself. 
            similarity_comparison = similarity(current_book_to_compare_ratings, ratings[i - j - 1])
            # whenever a higher similarity score is found, update the rating benchmark and the title 
            # of the most similar book. 
            if (similarity_comparison >= most_similar_rating) == True: 
                most_similar_rating = similarity_comparison
                most_similar_title = titles[i - j - 1]
                most_similar = [most_similar_title, most_similar_rating]

        # once all 52 books have been checked, append the matrix containing the title and similarity 
        # rating of the most similar book into the ith row. 
        most_similar_matrix.append(most_similar)

    # return the 53 x 2 similarity matrix . 
    return most_similar_matrix
    

def main():
    NUM_OF_BOOKS = 53
    # get the list containing all titles 
    titles_list = get_titles()
    # get the 53 x 32 matrix containing the user ratings for each book 
    book_ratings = get_ratings()
    # find the similarity matrix that has the title and ratings of the books most similar to each book. 
    similarity_matrix = find_most_similar(titles_list, book_ratings)

    # In the most-similar-books.txt file, write the similarity result for the 53 books in the desired format. 
    output_file = open('most-similar-books.txt', 'w')
    for i in range(0, NUM_OF_BOOKS):
        line = format_similar_message(titles_list[i], similarity_matrix[i][0], similarity_matrix[i][1])
        output_file.write(line)

    # close file
    output_file.close()

main()
    
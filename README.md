# book-recommendations
> *This program was originally written for the MSCI 121 course at the University of Waterloo, taught by Mark Smucker. The included features were written to match > the requirements of the assignment.*

A program for generating book recommendations using collaborative filtering. 

### Explanation
Given a list of book titles, in the file `books.txt`, a book recommendation is generated for each title in `most-similar-books.py`.
Users' rating data in `ratings.txt` are used to create rating vectors for each books. The vectors are compared to find the titles with the most similar vectors to each other. 
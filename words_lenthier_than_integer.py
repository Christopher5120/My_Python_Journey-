""" Write a program that given list of words and an integer value 'n', finds the words that are longer than n from a given list of words"""

#naming of function and defining parameters
def words_lenthier_than_integer(given_list_words, integer):

  #creating an empty list to receive the returned list of words
  returned_list = []

#looping throught the given list
  for word in given_list_words:

    #handling different data types and coverting them to strings
    word = str(word)

    #comparing the length of words in the given list of words to the integers
    if len(word) > integer:

    #adding the list of words greater than the specified integer in the empty list.
      returned_list.append(word)
    #to return the list
  return returned_list
#To return the
print(words_lenthier_than_integer([8, "ama", "daniel", "university", 111111111111111111, "kwameowusu", "jgjkhjhbugfgl", "ocansey", "newmexico"], 25))
print(words_lenthier_than_integer(["8", "ama", 885551256985], 5))
print(words_lenthier_than_integer(["8", "ama", "daniel", "university", "sharis", "kwameowusu", "annabeth", "ocansey", "newmexico"], 4))

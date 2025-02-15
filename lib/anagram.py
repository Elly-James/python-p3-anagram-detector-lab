# your code goes here!


# You will write a program that, given a word and a list of possible anagramsLinks to an external site., selects the correct one(s).

# Your class, Anagram should take a word on initialization; instances should respond to a match() instance method that takes a list of possible anagrams. It should return all matches in a list. If no matches exist, it should return an empty list.

# In other words, given: 'listen' and ['enlists', 'google', 'inlets', 'banana'] the program should return ['inlets'].

# listen = Anagram("listen")
# listen.match(['enlists', 'google', 'inlets', 'banana'])
#  => ['inlets']


# How will you determine if one word is an anagram for another?

# You'll need to iterate over the list of words that the match() method takes as an argument. You will compare each word of that list to the word that the Anagram class is initialized with.

# To determine one word is an anagram of another word, try determining if they are composed of the same letters. You can use a list interpretation on a string to get a list of its individual letters:

# [letter for letter in "hello"]
# # ["h", "e", "l", "l", "o"]
# You can compare two lists using the ==. For example:

# [1, 2, 3] == [1, 2, 3]
# # => True

# [1, 3, 2] == [1, 2, 3]
# # => False
# Two lists are equal if they contain the same elements, in the same order. Remember that you can use sorted() on a list. This will help in your comparison:

# sorted([1, 3, 2]) == sorted([3, 2, 1])
# # => True


class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_letters = sorted(list(word))
    
    def match(self, words):
        return [word for word in words if sorted(list(word)) == self.word_letters]
    
  
listen = Anagram("banana")
print(listen.match(['bwanana', 'onana', 'ndizi', 'nabana']))  
   
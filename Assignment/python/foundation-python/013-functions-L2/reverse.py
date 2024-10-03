# Reverse a Sentence

# Write a function named reverseSentence that takes a sentence (a string containing words separated by spaces) as input and returns the sentence with its words reversed.

# Sample Input: "Hello World" Sample Output: "olleH dlroW"

def reverseSentence(Sentence):
    words=Sentence.split(" ")
    for word in words:
        print(word[::-1],end=" ")
    
reverseSentence("Hello World") 
              


# Problem:  Take a sentence form the user as an input and then find the palandrom words 
#           and avoid the punchuations?

sentence = input("Enter the sentence to find the palendrom: ")
words = sentence.split()

for word in words:
    clean_word = word.strip(',.?!')
    if clean_word.lower() == clean_word[::-1].lower():
        print(word)
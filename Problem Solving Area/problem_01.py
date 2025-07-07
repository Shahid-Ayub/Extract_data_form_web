
# Problem: Write a Python function that takes a string of text as input and returns a 
# dictionary where the keys are the words in the text, and the values are the number of 
# times each word appears.

text = input("Enter your text: ") 

text = text.lower()
for pun in [',','.','?','!']:
    text = text.replace(pun,"")

word = text.split()

word_count = {}

for words in word:
    if words in word_count:
        word_count[words] += 1
    else:    
        word_count[words] = 1

print(word_count,text)



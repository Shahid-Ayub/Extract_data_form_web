word = 'programming'
vowel = "aeiou"
count = 0

for char in word:
    if char in vowel:
        count += 1

print("Number of vowel are",count)
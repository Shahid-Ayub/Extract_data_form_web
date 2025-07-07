word  = 'shahid ayub'
vowel = 'aeiou'
count = 0

for char in word:
    if char in vowel:
        count += 1

print("the number of vowel are:",count)
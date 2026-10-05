# WAP to find  the word1 and word2 is ANnagram or not

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("The words are Anagrams")
else:
    print("The words are not Anagrams")
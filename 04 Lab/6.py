## 06) WAP to count numbers of vowels in given string.

name=input("Enter a String ::")

vowelCount = name.lower().count("a") + name.lower().count("e") + name.lower().count("i") + name.lower().count("o") + name.lower().count("u")

print(vowelCount)
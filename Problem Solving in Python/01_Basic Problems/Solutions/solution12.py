def countVowelsAndConsonants(string):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    vowel_count, consonant_count = 0, 0
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    return {vowel_count, consonant_count}

string = str(input("Enter the string: "))
vowels, consonants = countVowelsAndConsonants(string)
print(f"Vowels: {vowels}, Consonants: {consonants}")
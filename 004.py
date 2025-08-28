# 4. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Interview"))  # Output: 4

def cv(s):
    v = "aeiouAEIOU"
    c = 0
    for char in s:
        if char in v:
            c += 1

    return c

print(cv("interviews"))
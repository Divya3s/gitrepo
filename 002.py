# 2. Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True


# 👉 Compares string with its reverse.

def pal(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
print(pal("racrcar")) # output True


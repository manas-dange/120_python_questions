def is_palindrome(s):
    if len(s) <= 1:  # Base case: empty or single character is a palindrome
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Example
s = "racecar"
print(f"Is '{s}' a palindrome?", is_palindrome(s))

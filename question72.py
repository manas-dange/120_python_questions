def count_vowels(s):
    if not s:  # Base case: empty string
        return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels(s[1:])

# Example
s = "hello world"
print("Number of vowels:", count_vowels(s))
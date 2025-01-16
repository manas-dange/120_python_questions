#21
# Count the number of vowels in a string
s = input("enter string")
vowels = "aeiouAEIOU"
count = 0  
for char in s:
        if char in vowels:
            count += 1;
print(count)
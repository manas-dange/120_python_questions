#28
# Use break and continue
for i in range(1, 11):
    if i % 3 == 0:
        continue
    if i == 9:
        break
    print(i)
s = input().strip()
if len(s) == 2:
    print(0)
else:
    print(len(set(s[1:-1].split(', '))))
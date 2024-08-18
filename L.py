a = int(input())
b = int(input())
c = int(input())
if a == b and a == c and c == b:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

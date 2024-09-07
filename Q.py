n = int(input())
if n % 100 >= 11 and n % 100 <= 14 or n % 10 == 0 or n % 10 >= 5:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
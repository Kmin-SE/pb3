# n = 5 => 1 + 2 + 3 + 4 + 5 = 15

# s = 0
# s += 1
# s += 2
# s += 3
# s += x

n = 4
s = 0
x = 1
while x <= n:
    s += x
    x += 1

print(s)

# x = 1 => s = 1
# x = 2 => s = 1 + 2 = 3
# x = 3 => s = s + 3 = 3 + 3 = 6
# x = 4 => s = s + 4 = 6 + 4 = 10
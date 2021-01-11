a = [11, 22, 33, 44]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
# print(a[4]) -> IndexError: list index out of range

# list slicing is non-mutative — creates a copy
print(a[1:3])
print(a[1:])
print(a[:2])
print(a[:])

for elem in a:
    print(elem)
print()

for i, elem in enumerate(a):
    print(i, elem)
print()

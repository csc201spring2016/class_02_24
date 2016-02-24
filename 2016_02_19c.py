height = int(input('What is the height of the square? '))
print("Squares of height ", height)

size = height
for i in range(size):
    print ('*' * size)

print("")

size = height
inner_size = size - 2
print ('*' * size)
for i in range(inner_size):
    print ('*' + ' ' * inner_size + '*')
print ('*' * size)

print("")

height = int(input('What is the height of the rectangle? '))
width = int(input('What is the width of the rectangle? '))
m = height
n = width

print("Rectangle of height ", height)
print("Rectangle of width ", width)
m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
    print()

print("")

height = int(input('What is the height of the right triangle? '))
width = int(input('What is the width of the right triangle? '))
m = height
n = width

print("right triangle of height ", height)
print("right triangle of width ", width)
m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [j, m-1] or j == 0 else ' ', end='')
    print()

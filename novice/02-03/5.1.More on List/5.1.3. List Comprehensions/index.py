squares = []
for x in range(10):
    squares.append(x**2)

squares
print(squares)
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
           combs.append((x, y))

combs
print(combs)   
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
print([x*2 for x in vec])  
[x for x in vec if x >= 0]
print( [x for x in vec if x >= 0]) 
[abs(x) for x in vec]
print( [abs(x) for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
print( [weapon.strip() for weapon in freshfruit])
[(x, x**2) for x in range(6)]
print( [(x, x**2) for x in range(6)])
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
print([num for elem in vec for num in elem])
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
print([str(round(pi, i)) for i in range(1, 6)])

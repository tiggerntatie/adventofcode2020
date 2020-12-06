# advent of code day 3

data = ["..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

def charat(forest, x, y):
    w = len(forest[0])
    return forest[y][x%w]
    
xstep = 3
ystep = 1
y = 0
x = 0
count = 0
w = len(data[0])
while y < len(data):
    if data[y][x%w] == '#':
        count += 1
    x += xstep
    y += ystep
    
print(count)
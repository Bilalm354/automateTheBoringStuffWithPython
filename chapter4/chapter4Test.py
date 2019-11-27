spam = ['apples', 'bananas', 'tofu', 'cats']

def listToString (words):
    words[-1] = 'and ' +words[-1]
    string=''
    for word in words:
        if word == words[-1]:
            string += words[-1]
            break
        elif word == words[-2]:
            string+=word + ' '
        else:
            string += word + ', '
    return string

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid (grid):
    for y in range(len(grid[0])):
        for x in grid:
            print (x[y], end='')
        print()


printGrid (grid)  

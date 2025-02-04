"""this program for solving a game of sudoku has been 
inspired by this youtube video from ComputerPhile
https://www.youtube.com/watch?v=G_UYXzGuqvM"""

import pyautogui as pg
import time
grid=[]
x=1
while True:
    row=list(input(f'Row {x}:'))
    x+=1
    ints=[]
    for i in row:
        ints.append(int(i))
    grid.append(ints)
    if len(grid)==9:
        break
    print("Row" + str(x-1) + "Complete")

time.sleep(4)
def possible(x, y, n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True
def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            for x in range(8):
                pg.hotkey('left')

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)
    input("More?")
solve()

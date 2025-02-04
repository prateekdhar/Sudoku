# Sudoku

Hello. Welcome to my repository for a code which solves sudoku online, just a fun little side project.

Libraries Used: Time, AutoGUI
**How it works:**:
The algorithm used here is a brute force algorithm, which checks for if a number is possible for each empty square(marked as 0). It picks the first number that fits the criteria and places it in the puzzle. If it hits a dead end, it will accordingly trace back and set the square to 0 again, and look for the next availaible number to place in it. This is recursively called until the sudoku puzzle is solved.

**How to use it:**

https://sudoku.com Please visit this site, and then run the program on your preferred console. Then, input each row of the puzzle into the terminal. 

Please input as a string with "0" to represent any square that is empty.

After all nine rows have been given as input, please navigate to the site and click on the top left corner of the puzzle.

Thank you for taking the time to read this :)

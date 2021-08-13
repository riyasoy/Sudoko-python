# Sudoko-python
This is a Sudoko game built with python.
I wanted to work with the Backtracing method, so like all the other Backtracing method sudoko can be solved by assigning numbers to empty cells one by one. Before assigning a number, we need to check whether it is safe to assign or not.
Check that the same number is not present in the current row, current column and in current 3X3 grid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. 
If the assignment doesn’t lead to a solution, then try the next number for the current empty cell.
And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.
This project helped me to learn the process behind the Backtracing method.

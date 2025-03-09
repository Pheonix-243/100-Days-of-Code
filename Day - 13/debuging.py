# ---------------- Day 13: Debugging ----------------

"""
Debugging is the process of finding and fixing errors in your code.
There are different types of errors:
1. **Syntax Errors** - Issues with the structure of the code (e.g., missing colons, incorrect indentation).
2. **Runtime Errors** - Errors that occur while the program is running (e.g., division by zero, accessing an undefined variable).
3. **Logical Errors** - The program runs but gives incorrect output (e.g., incorrect calculations, wrong conditions in loops).

### Debugging Strategies:
1. **Use Print Statements**
   - Print variables and check their values at different points in your code.
   - Example:
     ```python
     age = "twenty"
     print(type(age))  # Debugging: Checking the data type
     ```

2. **Use a Debugger**
   - Most IDEs (like VS Code, PyCharm) have built-in debuggers.
   - You can set breakpoints and inspect values step by step.

3. **Check for Off-by-One Errors**
   - Common mistake in loops where iteration runs one time too many or too few.
   - Example:
     ```python
     for i in range(1, 5):  # This runs 1 to 4, not 1 to 5
         print(i)
     ```

4. **Comment Out Code**
   - Temporarily remove sections of code to isolate the problem.

5. **Check Function Arguments**
   - Make sure correct values are passed into functions.

6. **Use Try-Except for Error Handling**
   - Helps prevent crashes and catch unexpected errors.
   - Helps prevent crashes and catch unexpected errors.
   - Example:
     ```python
     try:
         num = int(input("Enter a number: "))
         print(10 / num)
     except ZeroDivisionError:
         print("You can't divide by zero!")
     except ValueError:
         print("Invalid input! Please enter a number.")
     ```

7. **Rubber Duck Debugging**
   - Explain your code line by line (even to an inanimate object). It helps you find errors yourself!

Debugging is an essential skill, and improving it will make you a better programmer!
"""

# Build-an-Arithmetic-Formatter-Project

# Arithmetic Arranger
**Description**
**The Arithmetic Arranger is a Python function that takes a list of arithmetic problems and formats them vertically and side-by-side. This function is especially useful for displaying math problems in a clear and readable format. It supports addition and subtraction problems.**

# Features
- **Formats multiple arithmetic problems side-by-side.**
- **Ensures proper alignment of operands and operators.**
Provides an option to display the answers.
Function Signature
python
Copy code
def arithmetic_arranger(problems, display_answers=False):
    # Function implementation
Parameters
problems: A list of strings where each string represents an arithmetic problem (e.g., "32 + 698").
display_answers: A boolean (optional, default is False). If True, the function will also display the answers to the arithmetic problems.
Returns
A string with the arithmetic problems arranged vertically and side-by-side.
Usage
Example
python
Copy code
# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
Output:

diff
Copy code
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
python
Copy code
# Test with answers
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
Output:

yaml
Copy code
   32         1      9999      523
+   8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Installation
To use this function, simply clone the repository and import the function into your Python script.

git clone [https://github.com/your-username/arithmetic-arranger.git](https://github.com/Granny14/Build-an-Arithmetic-Formatter-Project.git)
Running the Tests
You can run the provided test cases to check the functionality of the arithmetic_arranger function.

python
Copy code
# Include your test cases here to verify the functionality
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please submit an issue or a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

# Mean-Variance-Standard Deviation Calculator

This project calculates the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix using NumPy.

## Usage

The `calculate()` function takes a list of 9 numbers and returns a dictionary containing statistical calculations along both axes and for the flattened matrix.

### Example

\`\`\`python
import mean_var_std

result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
\`\`\`

### Output Format

The function returns a dictionary with the following structure:
- **axis 0**: Statistics calculated down the columns
- **axis 1**: Statistics calculated across the rows  
- **flattened**: Statistics calculated on the flattened array

### Error Handling

If a list with fewer than 9 elements is provided, the function raises a `ValueError` with the message: "List must contain nine numbers."

## Running the Code

To test the calculator, run:
\`\`\`bash
python3 main.py
\`\`\`

This will execute the example calculation and run the unit tests.

## Requirements

- Python 3.x
- NumPy

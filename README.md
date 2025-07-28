Mean-Variance-Standard Deviation Calculator

This project is a part of the freeCodeCamp Data Analysis with Python certification.  
It calculates key statistics — mean, variance, standard deviation, max, min, and sum — for a given 3x3 matrix.


 Project Description

The function `calculate()` accepts a list of 9 numerical values, reshapes it into a 3x3 matrix using NumPy, and returns a dictionary containing:

- Row-wise, column-wise, and overall:
  - Mean
  - Variance
  - Standard deviation
  - Maximum
  - Minimum
  - Sum

If the input list contains anything other than 9 numbers, the function raises a `ValueError`.

 Example

```python
from mean_var_std import calculate

print(calculate([0,1,2,3,4,5,6,7,8]))

Sample Output :
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.44..., 2.44..., 2.44...], [0.81..., 0.81..., 0.81...], 2.58...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}




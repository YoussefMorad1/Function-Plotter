# Function Plotter Application

A GUI-based application that allows users to input mathematical functions and visualize them over a specified range of x-values. The application uses PySide2 for the GUI and Matplotlib for plotting, and it integrates functionality for evaluating user-entered functions.


## Examples

### Working Example

- **Function**: `x^2 + 2*x + 1`
- **x-range**: From -10 to 10

**Snapshot**:
![image](https://github.com/user-attachments/assets/2ac0cc30-09d7-4128-bea8-f550a877acbc)


**Explanation**: This plot shows the correct behavior of a quadratic function. The curve represents the equation `x^2 + 2*x + 1`, which is a parabola. The x-values from -10 to 10 are correctly plotted, and the function is displayed as expected.

### Wrong Example

- **Function**: `x / 0`

**Snapshot**:
![image](https://github.com/user-attachments/assets/13951692-853a-4105-b67a-bdefc7cc7f77)


**Explanation**: This example demonstrates a divide-by-zero error. The plot indicates an issue where division by zero is attempted, which results in an error message. In this case, the application should display an error and not plot the function.

### Wrong Example

- **Function**: `x ^ 2 + `

**Snapshot**:
![image](https://github.com/user-attachments/assets/58ffc153-1397-4934-912d-b17202d91f1f)


**Explanation**: This example demonstrates an invalid function error. In this case, the application should display an error and not plot the function.

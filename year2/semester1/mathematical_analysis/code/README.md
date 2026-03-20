# ***GENERAL INFO: here are mathematical analysis tasks***

---

## ***DESCRIPTION FOR cauchy_problem.py***
+ This script implements the Modified Euler method (Heun's method) to numerically solve ordinary differential equations.

## ***The script consists of the following steps:***
1. #### *Initialization*
   + defines an example function (in this case, a simple addition) to represent the differential equation;
   + initializes the starting values for x0 and y0, the step size h, and the number of iterations n.
2. #### *Modified Euler Method*
    + iterates n times to compute the next values of x and y;
    + for each step, it calculates an intermediate y1_next value using the standard Euler method;
    + then, it computes the final y_next value by averaging the slopes at the current and next points;
    + the new values of x and y are stored in their respective lists.
3. #### *Result*
   + the script prints the computed x-values and y-values after completing all iterations of the method.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR derivative_for_the_tabularly_defined_function.py***
+ This script calculates the first and second numerical derivatives of a function using finite differences.

## ***The script consist of the following steps:***
1. #### *Derivative Calculation*
   + uses the central difference method to compute the first and second derivatives of a list of function values;
   + for the first derivative, the script calculates the difference between adjacent values using a step size;
   + for the second derivative, it calculates the difference between the first derivatives using a similar approach.
2. #### *Boundary Handling*
   + special handling is applied at the boundaries (first and last points) of the data, using forward and backward difference formulas respectively.
3. #### *Result*
   + the script calculates and prints both the first and second derivatives for a given set of values based on the function x^3.

## ***REQUIREMENTS***
+ **Python 3.x**

--- 

## ***DESCRIPTION FOR integral_method_of_central_rectangles.py***
+ This script calculates the approximate value of a definite integral using the method of central rectangles.

## ***The script consists of the following steps:***
1. #### *Step Size Calculation*
   + the script first calculates the step size based on the given range of integration and the number of intervals.
2. #### *Central Rectangles Method*
   + for each interval, the script computes the x-values at the midpoints of the subintervals;
   + these midpoints are used to approximate the area under the curve using the central rectangle's method.
3. #### *Function Evaluation*
   + the function f(x) = x^2 is evaluated at each midpoint.
4. #### *Integral Approximation*
   + the script sums up the areas of all the rectangles, which is the approximation of the integral over the given range.
5. #### *Result*
   + the script prints the approximate value of the integral with two decimal places.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR integral_method_of_trapeziums.py***
+ This script calculates the approximate value of a definite integral using the trapezium method.

## ***The script consists of the following steps:***
1. #### *Step Size Calculation*
   + the script calculates the step size based on the given range of integration and the number of intervals.
2. #### *Trapezium method*
   + computes the x-values at the endpoints and at each step along the interval using the trapezium method. 
3. #### *Function Evaluation*
   + the function f(x) = x^2 is evaluated at each x-value in the list.
4. #### *Integral Approximation*
   + the script applies the trapezium method formula, which sums up the areas of the trapezoids formed between adjacent points;
   + the first and last terms are averaged (using 1/2 weight), while the intermediate terms are added as usual.
5. #### *Result*
   + the script prints the approximate value of the integral with two decimal places.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR integral_monte_carlo_method.py***
+ This script approximates the value of a definite integral using the Monte Carlo method.

## ***The script consists of the following steps:***
1. #### *Random Sample Generation*
   + the script generates random numbers uniformly disturbed between the start and end points of the integration interval;
   + these random numbers represent the x-values at which the function is evaluated.
2. #### *Function Evaluation*
   + the function f(x) = x^2 is evaluated at each randomly generated x-value.
3. #### *Integral Approximation*
   + the Monte Carlo method is applied by averaging the function values at the random points and multiplying by the range of integration.
4. #### *Result*
   + the script prints the approximate value of the integral based on the random sampling.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR integral_simpson's_method.py***
+ This script calculates the approximate value of a definite integral using Simpson's method.

## ***The script consists of the following steps:***
1. #### *Step Size Calculation*
   + the script calculates the step size based on the given range of integration and the number of intervals.
2. #### *Simpson's Points Generation*
   + the script generates the x-values at which the function will be evaluated, ensuring that the number of intervals is even, as required by Simpson's method;
3. #### *Function Evaluation*
   + the function f(x) = x^2 is evaluated at each x-value in the generated list.
4. #### *Integral Approximation*
   + the script applies Simpson's method by summing the function values at the even and odd indexed points, with different weights for each set;
   + the first and last function values are weighted by 1, even-indexed function values are weighted by 4, and odd-indexed function values are weighted by 2.
5. #### *Result*
    + the script prints the approximate value of the integral.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR lagrangian_interpolation.py***
+ This script calculates the value of a polynomial at a given point using the Lagrange interpolation method.

## ***The script consists of the following steps:***
1. #### *Basis Polynomial Calculation*
   + for each given point in the dataset, the script calculates the corresponding Lagrange basis polynomial;
   + the basis polynomial for a point is computed by multiplying terms involving the other points in the dataset, ensuring that the polynomial equals 1 at the target point and 0 at the others.
2. #### *Lagrange Polynomial Calculation*
   + the script calculates the Lagrange polynomial by summing the products of the function values at each point and the corresponding basis polynomial;
   + each term in the sum is weighted by the value of the basis polynomial at the target point.
3. #### *Result*
   + the script computes and prints the value of the polynomial at a specified point based on the given set of points.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR taylor_series.py***
+ This script approximates the sine function using the Taylor series expansion and compares it with the built-in sine function.

## ***The script consists of the following steps:***
1. #### *Taylor Series for Sine*
   + the script approximates the sine of a number x using the Taylor series expansion;
   + the series continues adding terms until the difference between successive terms is less than a specified epsilon value.
2. #### *Comparison with Built-in Function*
   + for each x value in the range [0, π], the script computes the sine using both the Taylor series and the built-in math.sin() function;
   + the script calculates and stores the difference between the two results for comparison.
3. #### *Performance Comparison*
   + the script also measures the execution time for both the custom Taylor series function and the built-in sine function.
4. #### *Result*
   + the script prints a table showing the computed sine values from both methods and the differences;
   + it also displays the time taken by both methods to perform the calculations.

## ***REQUIREMENTS***
+ **Python 3.x**

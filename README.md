# Interpolation with Taylor Series Approximation function from random scattering values (taylorseries)

**taylorseries** is a small package that computes the Taylor Series function from random scattering values. Normally, it is hard to achieve a function that fits to all the points on a xy-diagramm. This method helps us to figure out the function.

## Installation

Please use **gitclone**.

## Usage

Initialize to ensure that all required packages are installed (numpy & matplotlib)
```bash
make init
```

Run the program **./taylorseries/taylorseries.py**
```bash
make run
```

Run the test for this small package
```bash
make test
```

Generate the **README.md** from **README.ipynb** (makesure jupyter is installed)
```bash
make readme
```

Generate the documentation with Sphinx, the documentation is the file **./docs/build/html/index.html**:
```bash
cd ./docs/
make html
```

## Explanation
Before that, let's import some packages that will be used in this section. Numpy and Matplotlib will be used.


```python
import numpy as np
import matplotlib.pyplot as plt
```

Let's import the small package that I have written, which is in the file "./taylorseries/taylorseries.py"


```python
from taylorseries import taylorseries as ts
```

Then, we generate some values for the x-axis with the domain of [0.01, 0.02, 0.03, 0.04]


```python
x_src = np.arange(start=0.01, stop=0.05, step=0.01)
x_src
```




    array([0.01, 0.02, 0.03, 0.04])



And some random y-axis value, which corresponds witht the x_src


```python
y_src = np.random.uniform(75.5, 125.5, size=len(x_src))
y_src
```




    array([78.62200548, 89.13151148, 92.72868552, 83.67896822])



Let's see how the graph of x_src and y_src are correlated.


```python
plt.plot(x_src, y_src, 'bo')
```




    [<matplotlib.lines.Line2D at 0x7f09f9483ac0>]




    
![png](README_files/README_12_1.png)
    


According to Taylor Series Approximation, we know that the function is defined as

$y = f(x) = c_0*x^0 + c_1*x^1 + c_2*x^2 + c_3*x^3 + ... + c_n*x^n$.

If we have multiple input variables x and output variables y, we can figure out a Taylor Series function from these domains (input variables x) and co-domains (output variables y) through matrix multiplication:

$\vec{y} = X*\vec{c}$

where

$$
\vec{y} = 
\begin{bmatrix}
y_0\\
y_1\\
...\\
y_n
\end{bmatrix}
$$

$$
X = 
\begin{bmatrix} 
    1 & x_1 & x_1^2 & ... & x_1^{n-1} \\ 
    1 & x_2 & x_2^2 & ... & x_2^{n-1} \\
    1 & ... \\
    1 & x_n & x_n^2 & ... & x_n^{n-1} \\
\end{bmatrix}
$$

$$
\vec{c} = 
\begin{bmatrix}
c_0\\
c_1\\
...\\
c_n
\end{bmatrix}
$$

Since, the vector $\vec{y}$ and matrix $X$ are known, so

$\vec{c} = X^{-1}*\vec{y}$

So, first we need to calculate the matrix $X$.

And here is the function the I have written to generate the matrix X from x_src:


```python
X = ts.gen_matrix_X(x_src)
X
```




    array([[1.0e+00, 1.0e-02, 1.0e-04, 1.0e-06],
           [1.0e+00, 2.0e-02, 4.0e-04, 8.0e-06],
           [1.0e+00, 3.0e-02, 9.0e-04, 2.7e-05],
           [1.0e+00, 4.0e-02, 1.6e-03, 6.4e-05]])



To compute the vector constants:


```python
consts = ts.gen_constants(X, y_src)
consts
```




    array([ 6.69347269e+01,  1.03646450e+03,  2.27839343e+04, -9.55759900e+05])



Let's test the computed vector constants are working well, I have written the taylor function which accepts the input vector x and the vector constants as variables. Then, the output vector y is returned:


```python
y_test = ts.fcn_taylors(x_src, consts)
y_test
```




    array([78.62200548, 89.13151148, 92.72868552, 83.67896822])



We can see the value difference between the original vector y_src and the test result vector y_test. The differences are very small which can be ignored.


```python
y_test - y_src
```




    array([ 0.00000000e+00, -1.13686838e-13, -4.83169060e-13, -1.17950094e-12])



And now the interpolation can be tested:


```python
x_interpolate = np.arange(start=0.01, stop=0.04, step=0.001)
x_interpolate
```




    array([0.01 , 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018,
           0.019, 0.02 , 0.021, 0.022, 0.023, 0.024, 0.025, 0.026, 0.027,
           0.028, 0.029, 0.03 , 0.031, 0.032, 0.033, 0.034, 0.035, 0.036,
           0.037, 0.038, 0.039])




```python
y_interpolate = ts.fcn_taylors(x_interpolate, consts)
y_interpolate
```




    array([78.62200548, 79.82057607, 81.00163438, 82.15944585, 83.28827591,
           84.38239001, 85.43605359, 86.44353208, 87.39909093, 88.29699559,
           89.13151148, 89.89690405, 90.58743874, 91.197381  , 91.72099626,
           92.15254996, 92.48630754, 92.71653445, 92.83749612, 92.843458  ,
           92.72868552, 92.48744413, 92.11399927, 91.60261638, 90.94756089,
           90.14309825, 89.1834939 , 88.06301329, 86.77592184, 85.316485  ])




```python
plt.plot(x_interpolate, y_interpolate, 'ro')
plt.plot(x_src, y_src, 'bo')
```




    [<matplotlib.lines.Line2D at 0x7f09f94af550>]




    
![png](README_files/README_24_1.png)
    


As we can see that the interpolation and the taylor function from random scattering values are successfully computed.

## Contributing

I'm writing this to test out how sphinx documentation and unittest works. The most important is to have fun. ^^

If there is some other algorithms that seems interesting, Maybe I will do some updates.

If you want to contribute too, you can fork it, but I'm still figuring it how the github works. ^^

## License

[MIT](./LICENSE)

## Reference

- Abramowitz, Milton; Stegun, Irene A. (1970), Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, New York: Dover Publications, Ninth printing
- Thomas, George B., Jr.; Finney, Ross L. (1996), Calculus and Analytic Geometry (9th ed.), Addison Wesley, ISBN 0-201-53174-7
- Greenberg, Michael (1998), Advanced Engineering Mathematics (2nd ed.), Prentice Hall, ISBN 0-13-321431-1
- 3Blue1Brown (2017), Taylor series | Essence of calculus, chapter 11, https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=15s


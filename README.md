# Polynomial-Interpolation with Taylor Series Approximate function from random scattering values (taylorseries)

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




    array([112.69596425,  85.95851041,  96.29335033,  95.65531046])



Let's see how the graph of x_src and y_src are correlated.


```python
plt.plot(x_src, y_src, 'bo')
```




    [<matplotlib.lines.Line2D at 0x7f44a5830af0>]




    
![png](README_files/README_12_1.png)
    


According to Taylor Series Approximation, we know that the function is defined as

![png](README_files/ts_fcn.png)

If we have multiple input variables x and output variables y, we can figure out a Taylor Series function from these domains (input variables x) and co-domains (output variables y) through matrix multiplication:


![png](README_files/y=Xc.png)


where

![png](README_files/vect_y.png),
![png](README_files/matrix_X.png),
![png](README_files/vect_c.png)

Since, the vector ![png](README_files/y.png) and matrix ![png](README_files/X.png) are known, so

![png](README_files/c=X-1y.png)


So, first we need to calculate the matrix ![png](README_files/X.png)

And here is the function the I have written to generate the matrix ![png](README_files/X.png) from x_src:


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




    array([ 2.24550885e+02, -1.70428713e+04,  6.65813204e+05, -8.00752893e+06])



Let's test the computed vector constants are working well, I have written the taylor function which accepts the input vector x and the vector constants as variables. Then, the output vector y is returned:


```python
y_test = ts.fcn_taylors(x_src, consts)
y_test
```




    array([112.69596425,  85.95851041,  96.29335033,  95.65531046])



We can see the value difference between the original vector y_src and the test result vector y_test. The differences are very small which can be ignored.


```python
y_test - y_src
```




    array([1.42108547e-14, 2.55795385e-13, 3.97903932e-13, 6.53699317e-13])



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




    array([112.69596425, 106.9846782 , 102.07652165,  97.92344942,
            94.47741635,  91.69037726,  89.51428697,  87.90110032,
            86.80277212,  86.17125721,  85.95851041,  86.11648654,
            86.59714044,  87.35242694,  88.33430084,  89.494717  ,
            90.78563022,  92.15899534,  93.56676718,  94.96090057,
            96.29335033,  97.5160713 ,  98.5810183 ,  99.44014615,
           100.04540968, 100.34876372, 100.30216309,  99.85756263,
            98.96691715,  97.58218149])




```python
plt.plot(x_interpolate, y_interpolate, 'ro')
plt.plot(x_src, y_src, 'bo')
```




    [<matplotlib.lines.Line2D at 0x7f44a7897160>]




    
![png](README_files/README_24_1.png)
    


As we can see that the interpolation and the taylor function from random scattering values are successfully computed.

## Contributing

I'm writing this to test out how sphinx documentation and unittest works. The most important is to have fun. ^^

If there is some other algorithms that seems interesting, Maybe I will do some updates.

If you want to contribute too, you can fork it, but I'm still figuring it how the github works. ^^

contact: yeeyang.tan@live.com

## License

[MIT](./LICENSE)

## Reference

- Abramowitz, Milton; Stegun, Irene A. (1970), Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, New York: Dover Publications, Ninth printing
- Thomas, George B., Jr.; Finney, Ross L. (1996), Calculus and Analytic Geometry (9th ed.), Addison Wesley, ISBN 0-201-53174-7
- Greenberg, Michael (1998), Advanced Engineering Mathematics (2nd ed.), Prentice Hall, ISBN 0-13-321431-1
- 3Blue1Brown (2017), Taylor series | Essence of calculus, chapter 11, https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=15s


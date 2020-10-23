#!python3
# -*- coding: utf-8 -*-

import numpy as np


def gen_matrix_X(xs):
    """
    Generate the matrix X  from the given input vector x.

    Example:
        xs = [1, 2, 3]

        X = [[1, 1, 1], [1, 2, 4], [1, 3, 9]]


    Parameters
    ----------
    xs : np.array(dtype=float)..shape==(n,)
        the input vector x

    Returns
    -------
    np.array(dtype=float)..shape==(n,n)
        The generated matrix X from the vector x.
    """

    # if the length of xs is 1, the return the matrix [[1]] of size 1*1
    if (len(xs) == 1):
        return np.array([[1]])

    ones = np.full(len(xs), 1)
    X = [ones, xs]
    temps = xs
    for i in range(len(xs) - 2):
        temps = np.multiply(temps, xs)
        X.append(temps)
    X = np.array(X).T

    return X


def gen_constants(X, ys):
    """Generate the constants vector of the taylor series from the matrix M and product vector y, where y = X*a.

    Parameters
    ----------
    X : np.array(dtype=float)..shape==(n,n)
        the matrix X, which is generated from the input vector x
    ys : np.array(dtype=float)..shape==(n,)
        the resulting vector of the matrix multiplication of :math:`X*a`

    Returns
    -------
    np.array(dtype=float)..shape==(n,)
        the parameter of taylor series for each variable :math:`x^n`, where :math:`a = X^-1 * y`
    """

    X_inv = np.linalg.inv(X)

    return np.dot(X_inv, ys.T)


def fcn_taylor(x, consts):
    """Taylor series function: :math:`y = f(x) = c_0*x^0 + c_1*x^1 + c_2*x^2 + c_3*x^3 + ...`

    Where consts = [c0, c1, c2, ...] and x is the input value for the talor series function

    Parameters
    ----------
    x : float
        the input variable x of the function f
    consts : np.array(dtype=float)..shape==(n,n)
        the constants value for taylor series

    Returns
    -------
    float
        the result of the taylor series function
    """

    y = consts[0]
    temp = x
    for const in consts[1:]:
        y += const*temp
        temp *= x

    return y


def fcn_taylors(xs, consts):
    """
    Vector input type for taylor series functions, where
        xs = [x0, x1, x2, ...]
        consts = [c0, c1, c2, ...]

        ys = [y0, y1, y2, ...].T
           = [xs^0, xs^1, xs^2, ...].T * consts
           = [[ 1, x0, x0^2, ...],
              [ 1, x1, x1^2, ...],
              [ 1, x2, x2^2, ...],
              ...                ] * consts


    Parameters
    ----------
    xs : np.array(dtype=float)..shape==(n,)
        the input vector x
    consts : np.array(dtype=float)..shape==(n,n)
        the constants value for taylor series, where :math:`f(x) = c_0*x^0 + c_1*x^1 + c_2*x^2 + c_3*x^3 + ...`

    Returns
    -------
    np.array(dtype=float)..shape==(n,)
        the matrix multiplication of X*xs
    """

    ys = [fcn_taylor(x, consts) for x in xs]
    return np.array(ys)



#######################################################
# main
#######################################################
def _main_():

    print("Get random x_src & y_src:")
    x_src = np.arange(start=0.01, stop=0.04, step=0.01)
    y_src = np.random.uniform(75.5, 125.5, size=len(x_src))
    print("x_src: shape-", x_src.shape, "data-", x_src)
    print("y_src: shape-", y_src.shape, "data-", y_src, "\n")

    print("Generate the matrix X from x_src:")
    X = gen_matrix_X(x_src)
    print("shape: ", X.shape)
    print("data:")
    print(X, "\n")

    print("Calculate the constants of the Taylor Series from x_src & y_src:")
    consts = gen_constants(X, y_src)
    print("consts: shape-", consts.shape, "data-", consts, "\n")

    print("Check the correctness of the calculated Taylor Series constants")
    y_test = fcn_taylors(x_src, consts)
    print("y_test = fcn_taylors(x_src, consts)")
    print("y_test: shape-", y_test.shape, "data-", y_test)
    print("y_src: shape-", y_src.shape, "data-", y_src, "\n")

    print("y_test - y_src =", y_test - y_src)


if __name__ == "__main__":
    _main_()
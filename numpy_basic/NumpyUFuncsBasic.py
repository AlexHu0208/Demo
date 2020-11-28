from math import log
import numpy as np


def np_ufunc():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    z = np.add(x, y)
    print(z)


def np_create_function():
    def myadd(x, y):
        return x + y;

    myadd = np.frompyfunc(myadd, 2, 1)
    print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
    print(type(np.add))


def np_arithmetic():
    arr1 = np.array([10, 11, 12, 13, 14, 15])
    arr2 = np.array([20, 21, 22, 23, 24, 25])
    print(np.add(arr1, arr2))
    print(np.subtract(arr1, arr2))
    print(np.multiply(arr1, arr2))
    print(np.divide(arr1, arr2))
    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([6, 5, 4, 3, 2, 1])
    print(np.power(arr1, arr2))
    print(np.mod(arr1, arr2))
    print(np.remainder(arr1, arr2))
    print(np.divmod(arr1, arr2))
    print(np.abs(arr1))


def np_decimals():
    x = [-3.1666, 3.6667]
    print(np.trunc(x))
    print(np.fix(x))
    print(np.round(x))
    print(np.floor(x))
    print(np.ceil(x))


def np_log():
    arr = np.arange(1, 10)
    print(arr)
    print(np.log10(arr))
    print(np.log(arr))
    nplog = np.frompyfunc(log, 2, 1)
    print(nplog(100, 15))


def np_sum():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])
    print(np.add(arr1, arr2))
    print(np.sum([arr1, arr2]))
    print(np.sum([arr1, arr2], axis=1))
    print(np.cumsum(arr1))


def np_prod():
    arr = np.array([1, 2, 3, 4])
    x = np.prod(arr)
    print(x)
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    x = np.prod([arr1, arr2])
    print(x)
    print(np.prod([arr1, arr2], axis=0))
    print(np.prod([arr1, arr2], axis=1))
    print(np.cumprod(arr))


def np_diff():
    arr = np.array([10, 15, 25, 5])
    print(np.diff(arr))
    print(np.diff(arr, n=2))


def np_LCM():
    x = 4
    y = 6
    print(np.lcm(x, y))
    arr = np.array([3, 6, 9])
    x = np.lcm.reduce(arr)
    print(x)
    arr = np.arange(1, 10)
    x = np.lcm.reduce(arr)
    print(x)


def np_gcd():
    x = 6
    y = 9
    print(np.gcd(x, y))
    arr = np.array([20, 8, 32, 36, 16])
    x = np.gcd.reduce(arr)
    print(x)


def np_trigono():
    print(np.sin(np.pi/2))
    print(np.sin(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])))
    print(np.deg2rad(np.array([90, 180, 270, 360])))
    print(np.rad2deg(np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])))
    print(np.arcsin(1.0))
    print(np.arcsin(np.array([1, -1, 0.1])))
    print(np.hypot(3, 4))


def np_hyperbolic():
    print(np.sinh(np.pi/2))
    print(np.cosh(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])))
    print(np.arcsinh(1.0))
    print(np.arctanh(np.array([0.1, 0.2, 0.5])))


def np_set():
    arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
    print(np.unique(arr))
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])
    print(np.union1d(arr1, arr2))
    print(np.intersect1d(arr1, arr2))
    print(np.setdiff1d(arr1, arr2, assume_unique=True))
    print(np.setxor1d(arr1, arr2, assume_unique=True))


if __name__=="__main__":
    # np_ufunc()
    # np_create_function()
    # np_arithmetic()
    # np_decimals()
    # np_log()
    # np_sum()
    # np_prod()
    # np_diff()
    # np_LCM()
    # np_gcd()
    # np_trigono()
    # np_hyperbolic()
    np_set()
